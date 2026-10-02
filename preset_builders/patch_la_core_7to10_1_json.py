# -*- coding: utf-8 -*-
"""
la_core_7to10_bundle.json(200개: 7/8/9/10인 각 50개, 하이브리드 포맷)을
presets/la_core_*.json 개별 파일로 생성.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_core_7to10_1_json.py

사전 준비: la_core_7to10_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요.

이후 2단계: 기존에 쓰시던 카테고리 등록 스크립트를 그대로 실행하세요.
  python preset_builders\patch_livingartifact_2_meta.py
(이번 배치도 category = "🏺 Living Artifact · Core Formula"로 기존 300개와 동일한
카테고리라서, 새 카테고리는 추가되지 않고 키 500개만 늘어납니다.)
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_core_7to10_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)

    os.makedirs(PRESETS_DIR, exist_ok=True)

    written = 0
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
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        written += 1

    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    by_type = {}
    for item in presets:
        t = item["meta"]["group_size"]
        by_type[t] = by_type.get(t, 0) + 1
    for t in sorted(by_type):
        print(f"  인원 {t}: {by_type[t]}개")

if __name__ == "__main__":
    main()
