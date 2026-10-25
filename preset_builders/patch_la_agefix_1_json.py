# -*- coding: utf-8 -*-
r"""
구속·임산부 6계열의 40·50대 나이를 20대 초반~30대 후반으로 치환한 번들을 presets/ 에 덮어쓴다.
  la_hsball_200_age_bundle.json     -> la_hsball_solo_001~200
  la_hsbar_150_age_bundle.json      -> la_hsbar_solo_001~150
  la_hswall_100_age_bundle.json     -> la_hswall_solo_001~100
  la_pregball_150_age_bundle.json   -> la_pregball_solo_001~150
  la_ychain_200_age_bundle.json     -> la_ychainmat/bp/preg_solo (200)
  la_pregoutfit_150_age_bundle.json -> la_pregoutfit_solo_001~150
키·제목·카테고리·메타는 그대로이고 나이 표기만 바뀝니다(새 키·새 카테고리 없음 → 메타 스크립트 불필요).

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_agefix_1_json.py

사전 준비: 위 번들 JSON 6개를 preset_builders\ 폴더에 함께 두세요.
"""
import json
import os

HERE = os.path.dirname(__file__)
BUNDLES = [
    "la_hsball_200_age_bundle.json",
    "la_hsbar_150_age_bundle.json",
    "la_hswall_100_age_bundle.json",
    "la_pregball_150_age_bundle.json",
    "la_ychain_200_age_bundle.json",
    "la_pregoutfit_150_age_bundle.json",
]
PRESETS_DIR = os.path.join(HERE, "..", "presets")

def main():
    total = missing = 0
    for fn in BUNDLES:
        with open(os.path.join(HERE, fn), "r", encoding="utf-8") as f:
            items = json.load(f)
        n = 0
        for item in items:
            out = {"key": item["key"], "category": item["category"], "title": item["title"],
                   "prompt": item["prompt"], "meta": item["meta"]}
            path = os.path.join(PRESETS_DIR, f"{item['key']}.json")
            if not os.path.exists(path):
                missing += 1
            with open(path, "w", encoding="utf-8") as f2:
                json.dump(out, f2, ensure_ascii=False, indent=2)
            n += 1
        total += n
        print(f"  {fn}: {n}개")
    print(f"완료: {total}개 preset 파일을 덮어썼습니다 (기대값 950).")
    if missing:
        print(f"  (주의: 기존에 없던 파일 {missing}개가 새로 생성됨)")

if __name__ == "__main__":
    main()
