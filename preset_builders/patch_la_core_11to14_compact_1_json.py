# -*- coding: utf-8 -*-
"""
la_core_11to14_compact_bundle.json(200개: 11/12/13/14인 각 50개, 압축포맷,
체형도 BODY_SHORT, 피어싱·쥬얼리 포함)을 presets/la_core_*.json 개별 파일로 생성.

참고: 11인 이상은 인원수가 가끔 요청과 다르게 나올 수 있습니다(11인이 12인으로
나오는 등 약간의 편차 확인됨). 압축포맷이 하이브리드보다는 안정적이라 이걸로
등록하지만, 100% 정확하진 않습니다.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_core_11to14_compact_1_json.py

사전 준비: la_core_11to14_compact_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요.

이후 2단계: 기존에 쓰시던 카테고리 등록 스크립트를 그대로 실행하세요.
  python preset_builders\patch_livingartifact_2_meta.py
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_core_11to14_compact_bundle.json")
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
