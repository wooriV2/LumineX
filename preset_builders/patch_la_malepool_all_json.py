# -*- coding: utf-8 -*-
r"""
새 남성 체형 풀(맨즈 피지크·머슬 모델·피트니스 모델 추가, 스트롱맨 제외)로 다시 만든 번들 7개를 한 번에 등록한다.
  기존 6개 번들(Mixed Gender / Mat / Stone / Wood / Axis Mix / BoyIdol Male)은 같은 키를 덮어쓰고,
  남성 테마 번들(la_maletheme_solo/duo/trio, 100개)은 새 카테고리 1개로 추가된다.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_malepool_all_json.py
  python preset_builders\patch_livingartifact_2_meta.py

사전 준비: 아래 JSON 7개를 preset_builders\ 폴더에 함께 두세요.
"""
import json
import os

HERE = os.path.dirname(__file__)
BUNDLES = ["la_mixedgender_100_bundle.json", "la_mixedmat_100_bundle.json", "la_mixedstone_100_bundle.json", "la_mixedwood_100_bundle.json", "la_mixedaxis_100_bundle.json", "la_boyidolmale_100_bundle.json", "la_maletheme_100_bundle.json"]
PRESETS_DIR = os.path.join(HERE, "..", "presets")

def main():
    os.makedirs(PRESETS_DIR, exist_ok=True)
    total = overwritten = 0
    for fn in BUNDLES:
        with open(os.path.join(HERE, fn), "r", encoding="utf-8") as f:
            items = json.load(f)
        n = 0
        for item in items:
            out = {"key": item["key"], "category": item["category"], "title": item["title"],
                   "prompt": item["prompt"], "meta": item["meta"]}
            path = os.path.join(PRESETS_DIR, f"{item['key']}.json")
            if os.path.exists(path):
                overwritten += 1
            with open(path, "w", encoding="utf-8") as f2:
                json.dump(out, f2, ensure_ascii=False, indent=2)
            n += 1
        total += n
        print(f"  {fn}: {n}개")
    print(f"완료: {total}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    if overwritten:
        print(f"  (기존 파일 덮어쓰기: {overwritten}개)")

if __name__ == "__main__":
    main()
