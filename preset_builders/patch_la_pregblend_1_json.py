# -*- coding: utf-8 -*-
r"""
la_pregblend_geo_180_bundle.json (180개) -> presets/la_pregblend{3|4}_{solo|duo|trio}_{01~30}.json 새로 생성.

Pregnant Blend Formula (신규 카테고리): 임산부 바디페인팅에서 전통 공예 패턴 3~4종을 구조(가로·세로·대각 띠, 동심원,
부채꼴) x 경계선(매끈/물결)으로 나눠 섞음. 경계는 전부 희미한 전환 구간, 구조는 부위 이름 없이 선·중심점·시계 방향으로만
기술. 기존 Pregnant Formula(공예 1종)는 그대로 유지.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_pregblend_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py     # 새 카테고리 등록

사전 준비: la_pregblend_geo_180_bundle.json 을 preset_builders\ 폴더에 두세요.
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_pregblend_geo_180_bundle.json")
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
