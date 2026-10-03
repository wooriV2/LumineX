# -*- coding: utf-8 -*-
"""
la_120_bundle.json(120개: 왁스(촛농)·흑요암+금빛이음새 솔로·듀오·트리오 각 20개)을
presets/la_*.json 개별 파일로 생성.

왁스(la_wax_{type}_{번호}): 3색 팔레트(크림슨/앰버·에메랄드/골드·바이올렛/로즈)
중 매번 랜덤 선택.

흑요암+금(la_obsidian_{type}_{번호}): 색상 고정 1종(킨츠기와 컨셉 겹쳐 확장 안 함).

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_120_1_json.py

사전 준비: la_120_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요.

이후 2단계: 기존에 쓰시던 카테고리 등록 스크립트를 그대로 실행하세요.
  python preset_builders\patch_livingartifact_2_meta.py
(카테고리 2개가 새로 생깁니다: Wax Formula / Obsidian Gold Formula)
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_120_bundle.json")
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
