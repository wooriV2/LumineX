# -*- coding: utf-8 -*-
r"""
등록된 la_* 프리셋 프롬프트에서 같은 단어가 연달아 두 번 나오는 문구를 한 번으로 고칩니다.
  VIVID VIVID -> VIVID / BLAZING BLAZING -> BLAZING / extreme extreme -> extreme /
  dense dense -> dense / formations formations -> formations
(색 팔레트·신발·공예·문양 문구가 이미 해당 단어를 포함한 채로 템플릿이 또 붙여서 생긴 중복입니다.)

기본은 점검만 하고 아무것도 바꾸지 않습니다. 실제로 고치려면 --apply 를 붙이세요.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_duplicate_words_fix.py             # 점검만
  python preset_builders\patch_duplicate_words_fix.py --apply     # 실제 수정
"""
import argparse, glob, json, os, re

DUP_RE = re.compile(r"\b(VIVID|BLAZING|extreme|dense|formations) \1\b")
PRESETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "presets")

def dedup(text):
    total = 0
    while True:
        text, n = DUP_RE.subn(r"\1", text)
        if not n:
            return text, total
        total += n

def prefix_of(key):
    return "_".join(key.split("_")[:2]) if not key.startswith(("la_core_", "la_mix3_", "la_mixed7_", "la_mixed_", "la_mixedrand_", "la_preg_")) \
        else next(p for p in ("la_core_", "la_mixedrand_", "la_mixed7_", "la_mixed_", "la_mix3_", "la_preg_") if key.startswith(p))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(PRESETS_DIR, "la_*.json")))
    by_prefix, words, changed, samples = {}, {}, [], []
    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            item = json.load(f)
        key = item.get("key", os.path.basename(path)[:-5])
        new, n = dedup(item["prompt"])
        if not n:
            continue
        for m in DUP_RE.finditer(item["prompt"]):
            words[m.group(1)] = words.get(m.group(1), 0) + 1
        by_prefix[prefix_of(key)] = by_prefix.get(prefix_of(key), 0) + 1
        changed.append((path, item, new))
        if len(samples) < 4 and m.group(1) not in [s[0] for s in samples]:
            i = DUP_RE.search(item["prompt"]).start()
            samples.append((DUP_RE.search(item["prompt"]).group(1), key, item["prompt"][max(0, i - 40): i + 80].replace("\n", " ")))
    print(f"대상 la_* 프리셋 {len(files)}개 | 고칠 프리셋 {len(changed)}개")
    print("접두어별:", dict(sorted(by_prefix.items())))
    print("단어별 중복 문구 수:", words)
    for w, key, ctx in samples:
        print(f"  [{w}] {key}: …{ctx}…")
    if not a.apply:
        print("\n(점검만 실행했습니다. 실제로 고치려면 --apply 를 붙이세요.)")
        return
    for path, item, new in changed:
        item["prompt"] = new
        with open(path, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
    print(f"\n적용 완료: {len(changed)}개 파일 수정.")

if __name__ == "__main__":
    main()
