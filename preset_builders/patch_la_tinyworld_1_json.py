# -*- coding: utf-8 -*-
r"""
소인 여성 × 거대 세계 솔로 200 (정원·보석·유리·음악·사물·손·라이트 트레일)
  la_tinyworld_200_bundle.json
    la_tinyworld_001~200

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_tinyworld_1_json.py

사전 준비: la_tinyworld_200_bundle.json 을 preset_builders\ 폴더에 함께 두세요.
이후 2단계(새 카테고리이므로 필요):
  python preset_builders\patch_livingartifact_2_meta.py
"""
import json
import os

HERE = os.path.dirname(__file__)
BUNDLES = ["la_tinyworld_200_bundle.json"]
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
