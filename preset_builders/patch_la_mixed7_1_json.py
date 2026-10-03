# -*- coding: utf-8 -*-
"""
la_mixed7_bundle.json(270개: 7트랙 혼합(바디페인팅·임산부·이레즈미·UV네온·
스테인드글라스·금박·보태니컬) 듀오~데켓(2~10인) 각 30개)을
presets/la_mixed7_*.json 개별 파일로 생성.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_mixed7_1_json.py

사전 준비: la_mixed7_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요.

이후 2단계: 기존에 쓰시던 카테고리 등록 스크립트를 그대로 실행하세요.
  python preset_builders\patch_livingartifact_2_meta.py
(카테고리가 1개 새로 생깁니다: "🏺 Living Artifact · Mixed-Track Formula")
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_mixed7_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)

    os.makedirs(PRESETS_DIR, exist_ok=True)

    written = 0
    by_type = {}
    for item in presets:
        key = item["key"]
        out = {
            "key": key,
            "category": item["category"],
            "title": item["title"],
            "prompt": item["prompt"],
            "meta": item["meta"],
        }
        out_path = os.path.join(PRESETS_DIR, f"{key}.json")
        with open(out_path, "w", encoding="utf-8") as f2:
            json.dump(out, f2, ensure_ascii=False, indent=2)
        written += 1
        type_name = key.rsplit("_", 1)[0]
        by_type[type_name] = by_type.get(type_name, 0) + 1

    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    for t in sorted(by_type):
        print(f"  {t}: {by_type[t]}개")

if __name__ == "__main__":
    main()
