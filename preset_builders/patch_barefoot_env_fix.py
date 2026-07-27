# -*- coding: utf-8 -*-
"""
patch_barefoot_env_fix.py

목적:
  바디페인팅 프리셋에서 _build_wearing_line() 이 강제하는 "Barefoot." 과
  presets/*.json 의 environment 필드에 명시된 신발 기술이 충돌하는 문제 수정.
  environment 에 신발이 있으면 barefoot 강제를 생략한다.

수정 대상: core/builders.py (단 하나)
프리셋 JSON 은 건드리지 않는다.

안전장치:
  - 전체를 메모리에서 조립 → ast.parse 통과 시에만 디스크 기록
  - core/builders.py.bak 백업 생성
  - 각 치환은 정확히 1회 매칭 필수, 아니면 즉시 중단
  - environment 변수명은 추측하지 않고 소스에서 탐지, 실패 시 중단
"""
import ast
import glob
import json
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "core" / "builders.py"
BACKUP = ROOT / "core" / "builders.py.bak"

FAIL = []


def read(p):
    return Path(p).read_text(encoding="utf-8-sig")


def write(p, s):
    Path(p).write_text(s, encoding="utf-8")


def sub_once(src, pattern, repl_fn, label):
    """정확히 1회만 치환. 0회 또는 2회 이상이면 실패 기록."""
    new, n = re.subn(pattern, repl_fn, src, flags=re.M)
    if n != 1:
        FAIL.append(f"[{label}] 매칭 {n}회 (1회여야 함)")
        return src
    print(f"  OK  {label}")
    return new


# ────────────────────────────────────────────────────────────
# PART 0. 읽기 전용 검증 (패치와 무관하게 먼저 실행)
# ────────────────────────────────────────────────────────────
FOOTWEAR_KW = [
    "sandal", "heel", "shoe", "boot", "pump", "stiletto",
    "loafer", "mule", "sneaker", "moccasin", "slipper",
    "geta", "zori", "espadrille", "clog",
]


def verify_presets():
    print("=" * 62)
    print("PART 0. bp_*.json 검증 (읽기 전용)")
    print("=" * 62)

    files = sorted(glob.glob(str(ROOT / "presets" / "bp_*.json")))
    print(f"\n총 {len(files)}개 파일 (기대값 28)\n")

    groups = {"bp_solo_": [], "bp_duo_": [], "bp_trio_": [], "기타": []}
    suffix_count = {}
    with_shoes, without_shoes, broken = [], [], []

    for f in files:
        name = os.path.basename(f)
        for pref in ("bp_solo_", "bp_duo_", "bp_trio_"):
            if name.startswith(pref):
                groups[pref].append(name)
                break
        else:
            groups["기타"].append(name)

        stem = name[:-5]
        suf = stem.rsplit("_", 1)[-1]
        suffix_count[suf] = suffix_count.get(suf, 0) + 1

        try:
            d = json.loads(Path(f).read_text(encoding="utf-8-sig"))
        except Exception as e:
            broken.append(f"{name}: {e}")
            continue

        env = (d.get("environment") or "").lower()
        if any(k in env for k in FOOTWEAR_KW):
            with_shoes.append(name)
        else:
            without_shoes.append(name)

    for k, v in groups.items():
        if v:
            print(f"  {k:<10} {len(v):>2}개")
    print(f"\n  접미사 분포: {suffix_count}")

    print(f"\n  environment 에 신발 명시 있음 : {len(with_shoes)}개")
    print(f"  environment 에 신발 명시 없음 : {len(without_shoes)}개")
    if without_shoes:
        print("\n  [신발 없는 프리셋 — 패치 후에도 barefoot 유지됨]")
        for n in without_shoes:
            print(f"    - {n}")
    if broken:
        print("\n  [JSON 파싱 실패]")
        for b in broken:
            print(f"    ! {b}")

    # 기존(6월) 바디페인팅 프리셋 회귀 영향 확인
    others = [
        p for p in glob.glob(str(ROOT / "presets" / "*.json"))
        if not os.path.basename(p).startswith("bp_")
    ]
    affected = []
    for f in others:
        try:
            d = json.loads(Path(f).read_text(encoding="utf-8-sig"))
        except Exception:
            continue
        outfit = (d.get("outfit") or "").lower()
        env = (d.get("environment") or "").lower()
        if "painted" in outfit and any(k in env for k in FOOTWEAR_KW):
            affected.append(os.path.basename(f))

    print(f"\n  기존 프리셋 중 이번 변경으로 출력이 바뀌는 것: {len(affected)}개")
    for n in affected[:20]:
        print(f"    - {n}")
    if len(affected) > 20:
        print(f"    ... 외 {len(affected) - 20}개")
    print()


# ────────────────────────────────────────────────────────────
# PART 1. builders.py 패치
# ────────────────────────────────────────────────────────────
HELPER_BLOCK = '''

# environment 텍스트에 신발이 명시돼 있는지 판별
# 'platform'은 전시 대좌("a low platform")와 혼동되므로 의도적으로 제외
FOOTWEAR_IN_ENV_KEYWORDS = [
    "sandal", "heel", "shoe", "boot", "pump", "stiletto",
    "loafer", "mule", "sneaker", "moccasin", "slipper",
    "geta", "zori", "espadrille", "clog",
]


def _env_has_footwear(env_text: str) -> bool:
    """environment에 신발이 명시돼 있으면 True -> barefoot 강제를 생략"""
    if not env_text:
        return False
    low = env_text.lower()
    return any(kw in low for kw in FOOTWEAR_IN_ENV_KEYWORDS)
'''


def find_env_var(lines, call_idx):
    """call_idx 를 포함하는 함수 안에서 ENVIRONMENTS.get(...) 대입 변수명을 찾는다."""
    start = 0
    for i in range(call_idx, -1, -1):
        if lines[i].startswith("def "):
            start = i
            break
    pat = re.compile(r"^\s*(\w+)\s*=\s*ENVIRONMENTS?\s*(?:\.get\(|\[)")
    for i in range(start, call_idx):
        m = pat.match(lines[i])
        if m:
            return m.group(1), lines[i].strip()
    return None, None


def patch():
    print("=" * 62)
    print("PART 1. core/builders.py 패치")
    print("=" * 62 + "\n")

    if not TARGET.exists():
        FAIL.append(f"{TARGET} 없음")
        return None

    src = read(TARGET)

    if "_env_has_footwear" in src:
        print("  이미 패치된 파일입니다. 중단.")
        return None

    # 1) 헬퍼 삽입
    src = sub_once(
        src,
        r"(return any\(kw\.lower\(\) in combined for kw in BODYPAINT_KEYWORDS\)\n)",
        lambda m: m.group(1) + HELPER_BLOCK,
        "헬퍼 _env_has_footwear 삽입",
    )

    # 2) _build_wearing_line 시그니처
    src = sub_once(
        src,
        r"^def _build_wearing_line\(outfit_wearing: str, material_text: str, footwear: str\) -> str:$",
        lambda m: (
            "def _build_wearing_line(outfit_wearing: str, material_text: str, footwear: str,\n"
            '                        env_text: str = "") -> str:'
        ),
        "_build_wearing_line 시그니처",
    )

    # 3) Gemini barefoot 조건화
    src = sub_once(
        src,
        r'^(\s*)f"NOT clothing, NOT fabric, painted with \{material_text\}\. Barefoot\."$',
        lambda m: (
            f'{m.group(1)}f"NOT clothing, NOT fabric, painted with {{material_text}}."\n'
            f"{m.group(1)}f\"{{'' if _env_has_footwear(env_text) else ' Barefoot.'}}\""
        ),
        "Gemini barefoot 조건화",
    )

    # 4) _build_wearing_phrase_chatgpt 시그니처
    src = sub_once(
        src,
        r"^def _build_wearing_phrase_chatgpt\(outfit_wearing: str, material_text: str, footwear: str\) -> str:$",
        lambda m: (
            "def _build_wearing_phrase_chatgpt(outfit_wearing: str, material_text: str, footwear: str,\n"
            '                                  env_text: str = "") -> str:'
        ),
        "_build_wearing_phrase_chatgpt 시그니처",
    )

    # 5) ChatGPT barefoot 조건화
    src = sub_once(
        src,
        r'^(\s*)f"painted with \{material_text\}, barefoot\. "$',
        lambda m: (
            f'{m.group(1)}f"painted with {{material_text}}"\n'
            f"{m.group(1)}f\"{{'' if _env_has_footwear(env_text) else ', barefoot'}}. \""
        ),
        "ChatGPT barefoot 조건화",
    )

    if FAIL:
        return None

    # ── environment 변수명 탐지 ─────────────────────────────
    lines = src.split("\n")

    def locate(needle):
        for i, ln in enumerate(lines):
            if needle in ln:
                return i
        return -1

    targets = {
        "Gemini":     "_build_wearing_line(outfit_wearing, material_text, footwear)",
        "ChatGPT":    "_build_wearing_phrase_chatgpt(outfit_wearing, material, footwear)",
        "Midjourney": 'footwear_short = "barefoot"',
    }
    envvars = {}
    print()
    for label, needle in targets.items():
        idx = locate(needle)
        if idx < 0:
            FAIL.append(f"[{label}] 호출부를 찾지 못함: {needle}")
            continue
        var, decl = find_env_var(lines, idx)
        if not var:
            FAIL.append(
                f"[{label}] {idx + 1}행 부근에서 ENVIRONMENTS 대입 변수를 찾지 못함"
            )
            continue
        envvars[label] = var
        print(f"  탐지  {label:<11} line {idx + 1:>4}  env 변수 = '{var}'")
        print(f"        └ {decl}")

    if FAIL:
        return None

    # 6) Gemini 호출부
    src = sub_once(
        src,
        r"_build_wearing_line\(outfit_wearing, material_text, footwear\)",
        lambda m: f"_build_wearing_line(outfit_wearing, material_text, footwear, {envvars['Gemini']})",
        "Gemini 호출부",
    )

    # 7) ChatGPT 호출부
    src = sub_once(
        src,
        r"_build_wearing_phrase_chatgpt\(outfit_wearing, material, footwear\)",
        lambda m: f"_build_wearing_phrase_chatgpt(outfit_wearing, material, footwear, {envvars['ChatGPT']})",
        "ChatGPT 호출부",
    )

    # 8) Midjourney 조건화
    src = sub_once(
        src,
        r'^(\s*)footwear_short = "barefoot"$',
        lambda m: (
            f"{m.group(1)}if not _env_has_footwear({envvars['Midjourney']}):\n"
            f'{m.group(1)}    footwear_short = "barefoot"'
        ),
        "Midjourney 조건화",
    )

    if FAIL:
        return None

    # AST 검증
    try:
        ast.parse(src)
    except SyntaxError as e:
        FAIL.append(f"AST 파싱 실패: {e}")
        return None
    print("\n  OK  AST 검증 통과")
    return src


def main():
    verify_presets()
    new_src = patch()

    print("=" * 62)
    if FAIL or new_src is None:
        print("결과: 중단 — 파일을 수정하지 않았습니다.")
        for f in FAIL:
            print(f"  ! {f}")
        if not FAIL:
            print("  (이미 패치됨 또는 대상 없음)")
        print("=" * 62)
        sys.exit(1)

    shutil.copy2(TARGET, BACKUP)
    write(TARGET, new_src)
    print("결과: 성공")
    print(f"  수정  {TARGET}")
    print(f"  백업  {BACKUP}")
    print("=" * 62)
    print("\n되돌리려면:")
    print(r"  copy core\builders.py.bak core\builders.py")


if __name__ == "__main__":
    main()
