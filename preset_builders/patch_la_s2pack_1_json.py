# -*- coding: utf-8 -*-
r"""
la_s2pack_geo_120_bundle.json (120개) -> presets/la_s2pack_{solo|duo|trio}_{01~40}.json 새로 생성.
Structure Pack Formula (신규 카테고리): 2단계 구조 5종(굵은 스트라이프·셰브론·비대칭 몬드리안·폴카도트·큰 조각 4개)에
재질 2~4종을 섞음. 일반인·임산부·맥시멀리스트 문장 구조, 트리오는 트랙 최대 2종. 꽃·수정·촛농 제외, UV네온은 맥시멀리스트 1명.
사용법: python preset_builders\patch_la_s2pack_1_json.py  ->  python preset_builders\patch_livingartifact_2_meta.py
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_s2pack_geo_120_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)
    os.makedirs(PRESETS_DIR, exist_ok=True)
    existing = [it["key"] for it in presets if os.path.exists(os.path.join(PRESETS_DIR, it["key"] + ".json"))]
    if existing:
        print(f"주의: 이미 있던 키 {len(existing)}개를 덮어씁니다 (예: {existing[0]})")
    written, by_cat = 0, {}
    for item in presets:
        out = {k: item[k] for k in ("key", "category", "title", "prompt", "meta")}
        with open(os.path.join(PRESETS_DIR, f"{item['key']}.json"), "w", encoding="utf-8") as f2:
            json.dump(out, f2, ensure_ascii=False, indent=2)
        written += 1
        by_cat[item["category"]] = by_cat.get(item["category"], 0) + 1
    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    for c, cnt in by_cat.items():
        print(f"  {c}: {cnt}개")

if __name__ == "__main__":
    main()
