# -*- coding: utf-8 -*-
"""
la_180_bundle.json(180개: 크리스탈·비늘(Scale) 재질 솔로·듀오·트리오 각 30개)을
presets/la_*.json 개별 파일로 생성.

크리스탈(la_crystal_{type}_{번호}): 10색(아이스블루·로즈쿼츠핑크·자수정바이올렛·
시트린옐로우·에메랄드그린·스모키그레이·사파이어블루·루비레드·토파즈오렌지·클리어화이트)
중 매번 랜덤 선택.

비늘(la_scale_{type}_{번호}): 5개 동물타입(나비날개·코이·뱀·드래곤·인어) 중
매번 랜덤 선택, 동물별 전용 모양+색상 팔레트 적용(SCALE_ANIMAL_DB).

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_180_1_json.py

사전 준비: la_180_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요.

이후 2단계: 기존에 쓰시던 카테고리 등록 스크립트를 그대로 실행하세요.
  python preset_builders\patch_livingartifact_2_meta.py
(카테고리 2개가 새로 생깁니다: Crystal Formula / Scale Formula)
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_180_bundle.json")
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
