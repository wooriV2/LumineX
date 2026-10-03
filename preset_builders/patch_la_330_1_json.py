# -*- coding: utf-8 -*-
"""
la_330_bundle.json(330개: 7개 고정조합(3·4·5인) 30개씩=210개 +
완전랜덤조합(2~5인) 30개씩=120개)을 presets/la_*.json 개별 파일로 생성.

고정조합 7종(배치는 매번 랜덤 셔플):
  3a_bp2preg1       = 바디페인팅2 + 임산부1
  3b_preg2bp1       = 임산부2 + 바디페인팅1
  3c_preggoldbot    = 임산부 + 금박 + 보태니컬
  4a_bpppregireuv   = 바디페인팅 + 임산부 + 이레즈미 + UV네온
  4b_ireuvglassgold = 이레즈미 + UV네온 + 스테인드글라스 + 금박
  5a_bpppregireuvglass = 바디페인팅 + 임산부 + 이레즈미 + UV네온 + 스테인드글라스
  5b_ireuvglassgoldbot = 이레즈미 + UV네온 + 스테인드글라스 + 금박 + 보태니컬
키: la_mix3_{조합코드}_{번호}, 카테고리: "🏺 Living Artifact · Fixed Combo Formula"

완전랜덤조합(2~5인, 7개 트랙 중 매번 랜덤 선택+랜덤 배치):
키: la_mixedrand_{duo/trio/quartet/quintet}_{번호}, 카테고리: "🏺 Living Artifact · Random Combo Formula"

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_330_1_json.py

사전 준비: la_330_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요.

이후 2단계: 기존에 쓰시던 카테고리 등록 스크립트를 그대로 실행하세요.
  python preset_builders\patch_livingartifact_2_meta.py
(카테고리 2개가 새로 생깁니다: Fixed Combo Formula / Random Combo Formula)
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_330_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)

    os.makedirs(PRESETS_DIR, exist_ok=True)

    written = 0
    by_cat = {}
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
        by_cat[item["category"]] = by_cat.get(item["category"], 0) + 1

    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    for c,cnt in by_cat.items():
        print(f"  {c}: {cnt}개")

if __name__ == "__main__":
    main()
