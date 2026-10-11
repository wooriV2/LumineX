# -*- coding: utf-8 -*-
r"""
등록된 프리셋(presets/la_*.json)의 prompt에서 문법·중복 오류를 고칩니다. (이미 고쳐진 파일은 건드리지 않음 — 여러 번 실행해도 안전)
  1) "beach at with"                          -> "beach at midday with"
  2) "a open-air"                             -> "an open-air"
  3) "a autumn"                               -> "an autumn"
  4) "metallic platinum metallic leather"     -> "metallic platinum leather"

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_textfix_1.py          # 실제 수정
  python preset_builders\patch_la_textfix_1.py --dry    # 수정 없이 개수만 확인
"""
import glob, json, os, re, sys

PRESETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "presets")
FIXES = [
    ("beach at with", re.compile(r"beach at with"), "beach at midday with"),
    ("a open-air", re.compile(r"\ba open-air"), "an open-air"),
    ("a autumn", re.compile(r"\ba autumn"), "an autumn"),
    ("platinum 중복", re.compile(r"metallic platinum metallic leather"), "metallic platinum leather"),
]

def main():
    dry = "--dry" in sys.argv
    counts = {n: 0 for n, _, _ in FIXES}
    files_changed = 0
    by_prefix = {}
    for path in sorted(glob.glob(os.path.join(PRESETS_DIR, "la_*.json"))):
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        p = d.get("prompt", "")
        new = p
        hit = False
        for n, rx, rep in FIXES:
            new, k = rx.subn(rep, new)
            if k:
                counts[n] += k
                hit = True
        if hit:
            files_changed += 1
            pre = os.path.basename(path).rsplit("_", 2)[0]
            by_prefix[pre] = by_prefix.get(pre, 0) + 1
            if not dry:
                d["prompt"] = new
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(d, f, ensure_ascii=False, indent=2)
    print(("[DRY] " if dry else "") + f"수정 대상 파일 {files_changed}개")
    for n, c in counts.items():
        print(f"  {n}: {c}곳")
    for k in sorted(by_prefix):
        print(f"  {k}: {by_prefix[k]}개 파일")

if __name__ == "__main__":
    main()
