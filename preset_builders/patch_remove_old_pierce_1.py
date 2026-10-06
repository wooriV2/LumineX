# -*- coding: utf-8 -*-
r"""
구 체계 피어싱 프리셋 14개 삭제:  la_pierce8mix_* (6) + la_vesselpierce8_* (8)

1) presets\ 에서 해당 파일 삭제
2) 코드(core\*.py, 레포 루트 *.py)에 남은 해당 키 문자열을 제거(집합·리스트 항목). 제거 후 문법 검사(ast)를 통과하지 못하면
   원본으로 되돌리고 "수동 확인 필요"로 알려 줍니다. 수정한 파일은 .bak 백업이 생깁니다.
3) 삭제로 비게 된 카테고리가 있으면 presets_meta.py 의 해당 줄 위치를 알려 줍니다(자동 수정하지 않음).

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_remove_old_pierce_1.py
  (결과를 확인한 뒤 git add -A / commit / push. 잘못되면 커밋 전에 `git checkout -- .` 로 되돌릴 수 있습니다.)
"""
import ast
import glob
import json
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
PRESETS = os.path.join(ROOT, "presets")
PREFIXES = ("la_pierce8mix_", "la_vesselpierce8_")
PAIR = re.compile(r"""[ \t]*["']la_(?:pierce8mix|vesselpierce8)_[^"']*["']\s*:\s*(?:"[^"\n]*"|'[^'\n]*'|[\w.\-]+)[ \t]*,?""")
TOKEN = re.compile(r"""[ \t]*["']la_(?:pierce8mix|vesselpierce8)_[^"']*["'][ \t]*,?""")


def main():
    # 1) 프리셋 파일 삭제
    files = sorted(f for p in PREFIXES for f in glob.glob(os.path.join(PRESETS, p + "*.json")))
    cats = {}
    for f in files:
        try:
            with open(f, "r", encoding="utf-8-sig") as fh:
                cat = json.load(fh).get("category", "")
        except Exception:
            cat = ""
        cats[cat] = cats.get(cat, 0) + 1
    for f in files:
        os.remove(f)
    by_prefix = {p: sum(1 for f in files if os.path.basename(f).startswith(p)) for p in PREFIXES}
    print(f"[1] 프리셋 파일 삭제: {len(files)}개  {by_prefix}")
    for c, n in cats.items():
        print(f"    카테고리 '{c}': {n}개")

    # 2) 코드 속 키 문자열 정리
    targets = glob.glob(os.path.join(ROOT, "core", "*.py")) + glob.glob(os.path.join(ROOT, "*.py"))
    fixed, manual = [], []
    for path in sorted(set(targets)):
        with open(path, "r", encoding="utf-8-sig", newline="") as fh:
            text = fh.read()
        hits = PAIR.findall(text) + TOKEN.findall(PAIR.sub('', text))
        if not hits:
            continue
        shutil.copyfile(path, path + ".bak")
        new = TOKEN.sub("", PAIR.sub("", text))
        try:
            ast.parse(new)
        except SyntaxError as e:
            manual.append((os.path.relpath(path, ROOT), len(hits), str(e)))
            continue
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(new)
        fixed.append((os.path.relpath(path, ROOT), len(hits)))
    if fixed:
        print("[2] 코드에서 키 문자열 제거:")
        for p, n in fixed:
            print(f"    {p}: {n}곳 (백업 {p}.bak)")
    else:
        print("[2] 코드에서 해당 키 문자열은 발견되지 않았습니다.")
    for p, n, err in manual:
        print(f"    ⚠ 수동 확인 필요: {p} ({n}곳) — 자동 제거 시 문법 오류라 원본 유지 ({err})")

    # 3) 비게 된 카테고리 확인
    remaining = {}
    for f in glob.glob(os.path.join(PRESETS, "*.json")):
        try:
            with open(f, "r", encoding="utf-8-sig") as fh:
                c = json.load(fh).get("category", "")
        except Exception:
            continue
        remaining[c] = remaining.get(c, 0) + 1
    meta_path = os.path.join(ROOT, "core", "presets_meta.py")
    empty = [c for c in cats if c and remaining.get(c, 0) == 0]
    if empty:
        print("[3] 프리셋이 0개가 된 카테고리:")
        for c in empty:
            print(f"    '{c}'")
            if os.path.exists(meta_path):
                with open(meta_path, "r", encoding="utf-8-sig") as fh:
                    for i, line in enumerate(fh, 1):
                        if c in line:
                            print(f"      core\\presets_meta.py {i}줄: {line.strip()[:120]}")
    else:
        print("[3] 비게 된 카테고리 없음.")
    print(f"\n남은 la_ 프리셋 파일 수: {sum(1 for f in glob.glob(os.path.join(PRESETS, 'la_*.json')))}")
    print("확인 후: git add -A / git commit / git push   (.bak 파일은 커밋 전에 지우셔도 됩니다)")


if __name__ == "__main__":
    main()
