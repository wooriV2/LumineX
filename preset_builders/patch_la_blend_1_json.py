# -*- coding: utf-8 -*-
r"""
la_blend_540_bundle.json (540개) -> presets/la_*.json 개별 파일 생성.

  A. Material Blend Formula (270개)  키: la_matblend{2|3|4}_{solo|duo|trio}_{번호}
     - 재질 16종(이레즈미·UV네온·스테인드글라스·금박·보태니컬·크리스탈·비늘6종(공작 포함)·흑요암금·왁스·목재·석재)
       중 인물마다 독립 랜덤, 석재·목재는 각 1슬롯, {석재+목재}만의 2혼합은 제외
     - 경계: 2혼합=좌우흐림/전신마블링, 3·4혼합=자유형 구역
     - UV네온 포함 인물은 해당 구역만 전용 블랙라이트
  B. Craft Blend Formula (270개)     키: la_craftblend{2|3|4}_{solo|duo|trio}_{번호}
     - 바디페인팅 북엔드 구조 유지, 실존 전통공예 40종 풀, 부피 큰 체형 6종
     - 헤어스타일 31종 x 헤어컬러 30종 적용(메이크업 설명 속 머리 문장은 충돌 방지를 위해 제거)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_blend_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py

사전 준비: la_blend_540_bundle.json 을 preset_builders\ 폴더에 두세요.
카테고리 2개가 새로 생깁니다: Material Blend Formula / Craft Blend Formula
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_blend_540_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)
    os.makedirs(PRESETS_DIR, exist_ok=True)
    written = 0
    by_cat = {}
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
