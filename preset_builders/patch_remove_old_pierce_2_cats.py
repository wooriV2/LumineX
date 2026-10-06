# -*- coding: utf-8 -*-
r"""
구 피어싱 프리셋 삭제 후 비어 있는 카테고리 2개를 core\presets_meta.py 에서 제거합니다.

  🏺 Living Artifact · Piercing Mixed-Material 8
  🏺 Living Artifact · Vessel Piercing 8

문법 검사(ast)를 통과하지 못하면 원본을 유지하고 해당 위치를 알려 줍니다. 성공하면 앞 단계에서 생긴 .bak 파일도 지웁니다.
사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_remove_old_pierce_2_cats.py
"""
import ast
import glob
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
META = os.path.join(ROOT, "core", "presets_meta.py")
CATS = ["🏺 Living Artifact · Piercing Mixed-Material 8", "🏺 Living Artifact · Vessel Piercing 8"]


def main():
    with open(META, "r", encoding="utf-8-sig", newline="") as fh:
        text = fh.read()
    new, removed, manual = text, [], []
    for c in CATS:
        pat = re.compile(r"[ \t]*[\"']" + re.escape(c) + r"[\"']\s*:\s*\[[\s,]*\]\s*,?[ \t]*(?:\r?\n)?")
        new, n = pat.subn("", new)
        if n:
            removed.append(c)
        else:
            lines = text.splitlines()
            idx = next((i for i, l in enumerate(lines) if c in l), None)
            manual.append((c, idx))
    for c in removed:
        print(f"제거: {c}")
    for c, idx in manual:
        if idx is None:
            print(f"이미 없음: {c}")
        else:
            print(f"⚠ 자동 제거 실패(수동 확인): {c} — core\\presets_meta.py {idx + 1}줄 근처")
            for j in range(max(0, idx - 1), min(len(text.splitlines()), idx + 6)):
                print(f"    {j + 1}: {text.splitlines()[j][:110]}")
    if not removed:
        print("변경 없음.")
        return
    try:
        ast.parse(new)
    except SyntaxError as e:
        print(f"⚠ 제거 후 문법 오류가 생겨 원본을 유지했습니다: {e}")
        return
    shutil.copyfile(META, META + ".bak2")
    with open(META, "w", encoding="utf-8", newline="") as fh:
        fh.write(new)
    for b in glob.glob(os.path.join(ROOT, "core", "*.bak")) + glob.glob(os.path.join(ROOT, "*.bak")):
        os.remove(b)
    os.remove(META + ".bak2")
    print("완료. 문법 검사 통과, .bak 파일 정리됨. 이제 git add -A / commit / push 하세요.")


if __name__ == "__main__":
    main()
