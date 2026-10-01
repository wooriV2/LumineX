# -*- coding: utf-8 -*-
"""
la_core_bundle.json(300개: solo/duo/trio/quartet/quintet/sextet 각 50개)을
presets/la_core_*.json 개별 파일로 생성.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_core_1_json.py

사전 준비: la_core_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요
(또는 아래 BUNDLE_PATH를 실제 위치로 수정).

이후 2단계: 기존에 쓰시던 카테고리 등록 스크립트를 그대로 실행하세요.
  python preset_builders\patch_livingartifact_2_meta.py
(presets/la_*.json을 category별로 스캔해서 PRESET_CATEGORIES에 자동 반영하는 그 스크립트입니다.
이 배치는 전부 category = "🏺 Living Artifact · Core Formula" 하나뿐이라 한 번에 등록됩니다.)

주의: 이 스크립트는 각 preset JSON에 key/category/title/prompt/meta 필드를 씁니다.
기존 la_*.json 파일 하나를 열어서 실제 필드명과 비교해보시고, 다르면
아래 OUTPUT_FIELDS 매핑만 고치면 됩니다 — 본문(prompt) 텍스트 자체는 그대로 재사용 가능합니다.
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_core_bundle.json")
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
