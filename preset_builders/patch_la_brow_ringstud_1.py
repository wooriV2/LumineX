# -*- coding: utf-8 -*-
r"""
등록된 피어싱 프리셋의 '눈썹 바' 문장을 '작은 링 + 둥근 구슬 스터드' 문장으로 교체한다.
(시험 결과: 눈썹 바는 바 중간이 노출되는 경우가 많고, 링+스터드가 더 안정적. 핸드오프 v6.37 32장)

- presets\la_*.json 전체를 훑어 'Piercings:' 문단(Piercing depth: 앞)에 있는 눈썹 바 문장 5종만 바꾼다.
  (다른 문단·다른 바(귀·코·입술)는 건드리지 않는다. 개수는 유지: 바 N개 -> 링/스터드 합계 N개)
- 이미 바뀐 파일은 다시 바꾸지 않는다(여러 번 실행해도 안전).
- 되돌리기: git checkout <커밋 이전> -- presets  (또는 git revert)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_brow_ringstud_1.py
"""
import glob
import json
import os
import re
import sys

PRESETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "presets")
MIX = ("alternating small rings that pass through the brow skin with the skin visible through each loop "
       "and small round ball studs sitting on the skin")
M = r"(?P<m>[\w\-]+)"
RULES = [
    ("thick-each", re.compile(rf"\b(?P<n>one|two|three|four|five|six|seven|eight|nine|ten) thick {M} bars stacked through the outer half of each eyebrow"),
     lambda m: f"{m['n']} {m['m']} pieces in a row along the outer half of each eyebrow, {MIX}"),
    ("thin-half-left", re.compile(rf"\b(?P<n>one|two|three|four|five|six|seven|eight|nine|ten) thin {M} bars pass through the outer half of the left eyebrow"),
     lambda m: f"{m['n']} {m['m']} pieces in a row along the outer half of the left eyebrow, {MIX}"),
    ("thin-end-left", re.compile(rf"\b(?P<n>one|two|three|four|five|six|seven|eight|nine|ten) thin {M} bars pass through the outer end of the left eyebrow"),
     lambda m: f"{m['n']} {m['m']} pieces in a row along the outer end of the left eyebrow, {MIX}"),
    ("thick-each-nomat", re.compile(r"\b(?P<n>one|two|three|four|five|six|seven|eight|nine|ten) thick bars stacked through the outer half of each eyebrow"),
     lambda m: f"{m['n']} pieces in a row along the outer half of each eyebrow, {MIX}"),
    ("thin-end-each", re.compile(rf"\b(?P<n>one|two|three|four|five|six|seven|eight|nine|ten) thin {M} bars pass through the outer end of each eyebrow"),
     lambda m: f"{m['n']} {m['m']} pieces in a row along the outer end of each eyebrow, {MIX}"),
    ("one-end-each", re.compile(rf"\ba thin {M} bar passes through the outer end of each eyebrow"),
     lambda m: f"a small {m['m']} ring passes through the outer end of each eyebrow, with the skin visible through the loop"),
    ("one-end-left", re.compile(rf"\ba thin {M} bar passes through the outer end of the left eyebrow"),
     lambda m: f"a small {m['m']} ring passes through the outer end of the left eyebrow, with the skin visible through the loop"),
]


def fix(prompt):
    i = prompt.find("Piercings:")
    j = prompt.find("Piercing depth:")
    if i < 0 or j < 0 or j < i:
        return prompt, {}
    seg = prompt[i:j]
    hits = {}
    for name, rx, fn in RULES:
        seg, k = rx.subn(fn, seg)
        if k:
            hits[name] = k
    return prompt[:i] + seg + prompt[j:], hits


def main():
    files = sorted(glob.glob(os.path.join(PRESETS_DIR, "la_*.json")))
    changed = 0
    by_rule = {}
    by_prefix = {}
    left = 0
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            d = json.load(fh)
        p = d.get("prompt", "")
        new, hits = fix(p)
        if hits:
            d["prompt"] = new
            with open(f, "w", encoding="utf-8") as fh:
                json.dump(d, fh, ensure_ascii=False, indent=2)
            changed += 1
            for k, v in hits.items():
                by_rule[k] = by_rule.get(k, 0) + v
            pre = re.sub(r"_(solo|duo|trio|quartet|quintet)?_?\d+$", "", os.path.basename(f)[:-5])
            by_prefix[pre] = by_prefix.get(pre, 0) + 1
        # 남은 눈썹 바(검증)
        i = new.find("Piercings:"); j = new.find("Piercing depth:")
        if i >= 0 and j > i and any("bridge of the nose" not in new[i:j][mm.start():(re.search(r"[;.]", new[i:j][mm.end():]) or re.search(r"$", new[i:j][mm.end():])).start() + mm.end()] for mm in re.finditer(r"\beyebrows?\b[^;.]*\b(bar|bars|barbell)\b|\b(bar|bars|barbell)\b[^;.]*\beyebrows?\b", new[i:j])):
            left += 1
    print(f"완료: {changed}개 파일의 눈썹 바 문장을 링+스터드로 교체했습니다. (검사한 파일 {len(files)}개)")
    for k in sorted(by_rule):
        print(f"  규칙 {k}: {by_rule[k]}곳")
    for k in sorted(by_prefix):
        print(f"  {k}: {by_prefix[k]}개")
    print(f"눈썹 바 문장이 남은 파일: {left}개" + ("  <- 0이어야 정상" if left else "  (정상)"))
    return 0 if left == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
