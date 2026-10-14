# -*- coding: utf-8 -*-
r"""
새 영역 4종 400개를 presets/ 개별 파일로 생성한다.
  la_area4_400_bundle.json -> la_chrome_solo_001~060 / duo_001~030 (🏺 Living Artifact · Chrome Formula)
                              la_rhine_*  (Rhinestone Formula), la_proj_*  (Projection Formula), la_splash_* (Splash Formula) 각 솔로60·듀오30
                              la_a4mix_trio_001~014 / quartet_001~013 / quintet_001~013 (Four-Element Mix Formula)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_area4_1_json.py

사전 준비: 위 번들 JSON 1개를 preset_builders\ 폴더에 함께 두세요.
이후 2단계(새 카테고리 5개이므로 필요):
  python preset_builders\patch_livingartifact_2_meta.py
"""
import json
import os

HERE = os.path.dirname(__file__)
BUNDLES = ["la_area4_400_bundle.json"]
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
