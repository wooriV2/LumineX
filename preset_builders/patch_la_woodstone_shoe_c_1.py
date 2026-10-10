# -*- coding: utf-8 -*-
r"""
목재·석재 프리셋의 신발 문장 속 '다리를 늘이라'는 표현을 절충 문구 C로 교체한다.
(시험 결과: 'her legs stretched impossibly long ... stilts' 문구는 다리만 길어지고 체형이 깎임.
 C = 다리 늘이기는 빼고 stilts 표현은 유지 + '체형은 그대로(굵은 허벅지·넓은 힙·큰 가슴)'. 핸드오프 v6.37 32장)

대상(기본): la_wood2_*, la_stone2_*, la_wsmix_*  (v2 840개)
옵션 --v1 : 기존 la_wood_*, la_stone_* 중 극단 힐 문장이 있는 프리셋(221개)도 같이 교체
이미 바뀐 파일은 건드리지 않는다(여러 번 실행해도 안전).

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_woodstone_shoe_c_1.py
  (v1도 함께: python preset_builders\patch_la_woodstone_shoe_c_1.py --v1)
"""
import glob
import json
import os
import re
import sys

PRESETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "presets")
OLD = "her legs stretched impossibly long and her whole body lifted far above the ground on them as if standing on stilts"
NEW = ("her whole body lifted far above the ground on them as if standing on stilts, while her body keeps its full "
       "original proportions — thick heavy thighs, wide full hips and a huge bust exactly as massive as before")


def main():
    v1 = "--v1" in sys.argv
    pats = ["la_wood2_*.json", "la_stone2_*.json", "la_wsmix_*.json"] + (["la_wood_*.json", "la_stone_*.json"] if v1 else [])
    files = sorted({f for p in pats for f in glob.glob(os.path.join(PRESETS_DIR, p))})
    changed = 0
    replaced = 0
    by_prefix = {}
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            d = json.load(fh)
        p = d.get("prompt", "")
        k = p.count(OLD)
        if not k:
            continue
        d["prompt"] = p.replace(OLD, NEW)
        with open(f, "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=2)
        changed += 1
        replaced += k
        pre = re.sub(r"_(solo|duo|trio|quartet|quintet)_\d+$", "", os.path.basename(f)[:-5])
        by_prefix[pre] = by_prefix.get(pre, 0) + 1
    print(f"완료: {changed}개 파일, {replaced}곳의 신발 문구를 C로 교체했습니다. (검사한 파일 {len(files)}개, v1 포함={v1})")
    for k in sorted(by_prefix):
        print(f"  {k}: {by_prefix[k]}개")


if __name__ == "__main__":
    main()
