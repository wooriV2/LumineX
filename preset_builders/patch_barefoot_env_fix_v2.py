# -*- coding: utf-8 -*-
"""
patch_barefoot_env_fix_v2.py

v1 대비 변경:
  - environment 변수 자동 탐지 제거 (Gemini 빌더에는 대입 변수가 없음이 확인됨)
  - 세 빌더 모두 ENVIRONMENTS[data['env']] 를 직접 전달
  - Midjourney 는 잘린 env_short 대신 전체 값으로 감지

목적:
  바디페인팅 프리셋에서 _build_wearing_line() 이 강제하는 "Barefoot." 과
  presets/*.json 의 environment 에 명시된 신발 기술이 충돌하는 문제 수정.

수정 대상: core/builders.py (단 하나)

안전장치:
  - 메모리에서 조립 → ast.parse 통과 시에만 디스크 기록
  - core/builders.py.bak 백업 생성
  - 각 치환은 정확히 1회 매칭 필수, 아니면 즉시 중단
  - 각 호출부가 속한 함수 안에 data['env'] 가 실제로 존재하는지 사전 확인
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

ENV_EXPR = "ENVIRONMENTS[data['env']]"

FAIL = []


def read(p):
    return Path(p).read_text(encoding="utf-8-sig")


def write(p, s):
    Path(p).write_text(s, encoding="utf-8")


def sub_once(src, pattern, repl_fn, label):
    new, n = re.subn(pattern, repl_fn, src, flags=re.M)
    if n != 1:
        FAIL.append(f"[{label}] 매칭 {n}회 (1회여야 함)")
        return src
    print(f"  OK  {label}")
    return new


# ────────────────────────────────────────────────────────────
# PART 0. 프리셋 요약 (읽기 전용)
# ────────────────────────────────────────────────────────────
FOOTWEAR_KW = [
    "sandal", "heel", "shoe", "boot", "pump", "stiletto",
    "loafer", "mule", "sneaker", "moccasin", "slipper",
    "geta", "zori", "espadrille", "clog",
]


def verify_presets():
    print("=" * 62)
    print("PART 0. bp_*.json 요약 (읽기 전용)")
    print("=" * 62)

    files = sorted(glob.glob(str(ROOT / "presets" / "bp_*.json")))
    with_shoes = 0
    for f in files:
        try:
            d = json.loads(Path(f).read_text(encoding="utf-8-sig"))
        except Exception as e:
            print(f"  ! JSON 파싱 실패 {os.path.basename(f)}: {e}")
            continue
        env = (d.get("environment") or "").lower()
        if any(k in env for k in FOOTWEAR_KW):
            with_shoes += 1

    print(f"\n  총 {len(files)}개 / 신발 명시 {with_shoes}개 / 미명시 {len(files) - with_shoes}개\n")


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


def check_scope(src, needle, label):
    """needle 이 속한 함수 안에서 data['env'] 가 실제로 쓰이는지 확인."""
    lines = src.split("\n")
    idx = -1
    for i, ln in enumerate(lines):
        if needle in ln:
            idx = i
            break
    if idx < 0:
        FAIL.append(f"[{label}] 호출부를 찾지 못함: {needle}")
        return

    start = 0
    for i in range(idx, -1, -1):
        if lines[i].startswith("def "):
            start = i
            break
    end = len(lines)
    for i in range(idx + 1, len(lines)):
        if lines[i].startswith("def "):
            end = i
            break

    region = "\n".join(lines[start:end])
    if "data['env']" not in region and 'data["env"]' not in region:
        FAIL.append(
            f"[{label}] {idx + 1}행이 속한 함수({lines[start].strip()[:50]}) 안에서 "
            f"data['env'] 를 찾지 못함 — 전달 시 NameError 위험"
        )
        return
    print(f"  확인  {label:<11} line {idx + 1:>4}  (같은 함수에 data['env'] 존재)")


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

    # ── 사전 스코프 검증 ────────────────────────────────────
    check_scope(src, "_build_wearing_line(outfit_wearing, material_text, footwear)", "Gemini")
    check_scope(src, "_build_wearing_phrase_chatgpt(outfit_wearing, material, footwear)", "ChatGPT")
    check_scope(src, 'footwear_short = "barefoot"', "Midjourney")
    if FAIL:
        return None
    print()

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

    # 6) Gemini 호출부 (인라인 전달)
    src = sub_once(
        src,
        r"_build_wearing_line\(outfit_wearing, material_text, footwear\)",
        lambda m: f"_build_wearing_line(outfit_wearing, material_text, footwear, {ENV_EXPR})",
        "Gemini 호출부",
    )

    # 7) ChatGPT 호출부
    src = sub_once(
        src,
        r"_build_wearing_phrase_chatgpt\(outfit_wearing, material, footwear\)",
        lambda m: f"_build_wearing_phrase_chatgpt(outfit_wearing, material, footwear, {ENV_EXPR})",
        "ChatGPT 호출부",
    )

    # 8) Midjourney 조건화 (잘린 env_short 대신 전체 값으로 감지)
    src = sub_once(
        src,
        r'^(\s*)footwear_short = "barefoot"$',
        lambda m: (
            f"{m.group(1)}if not _env_has_footwear({ENV_EXPR}):\n"
            f'{m.group(1)}    footwear_short = "barefoot"'
        ),
        "Midjourney 조건화",
    )

    if FAIL:
        return None

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
