# -*- coding: utf-8 -*-
"""
la_pregnant_solo_bundle.json(500개: 임산부 솔로~데켓 각 50개, 융합형 포맷) +
la_mixed_bundle.json(450개: 일반+임산부 혼합 듀오~데켓 각 50개)을
presets/la_preg_*.json, la_mixed_*.json 개별 파일로 생성.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_pregnant_1_json.py

사전 준비: la_pregnant_solo_bundle.json, la_mixed_bundle.json 두 파일을
preset_builders\ 폴더에 함께 두세요.

이후 2단계: 기존에 쓰시던 카테고리 등록 스크립트를 그대로 실행하세요.
  python preset_builders\patch_livingartifact_2_meta.py
(이번엔 카테고리 2개가 새로 생깁니다: "🤰 Living Artifact · Pregnant Formula"와
"🤰 Living Artifact · Pregnant Mixed Formula")
"""
import json
import os

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")
BUNDLES = [
    os.path.join(os.path.dirname(__file__), "la_pregnant_solo_bundle.json"),
    os.path.join(os.path.dirname(__file__), "la_mixed_bundle.json"),
]

def main():
    os.makedirs(PRESETS_DIR, exist_ok=True)
    total_written = 0
    for bundle_path in BUNDLES:
        with open(bundle_path, "r", encoding="utf-8") as f:
            presets = json.load(f)
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
            t = item["meta"]["group_size"]
            by_type[t] = by_type.get(t, 0) + 1
        print(f"완료: {written}개 preset 파일을 {os.path.basename(bundle_path)} 에서 생성했습니다.")
        for t in sorted(by_type):
            print(f"  인원 {t}: {by_type[t]}개")
        total_written += written
    print(f"총 {total_written}개 preset 파일 생성 완료.")

if __name__ == "__main__":
    main()
