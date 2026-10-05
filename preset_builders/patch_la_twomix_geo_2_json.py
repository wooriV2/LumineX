# -*- coding: utf-8 -*-
r"""
la_twomix_geo2_180_bundle.json (180개) -> 2혼합 프리셋 덮어쓰기
  la_craftblend2_{solo|duo|trio}_{01~30} (공예 90) + la_matblend2_{solo|duo|trio}_{01~30} (재질 90)

패턴(재질) 2종을 3~4구역에 A, B, A(, B) 순서로 번갈아 배치(구조: 가로·세로·대각 띠, 동심원, 부채꼴 x 매끈/물결, 희미한 경계).
재질 쪽은 꽃(보태니컬)·수정(크리스탈)을 뺐고, 팔 올린 자세와 문장부호 오타("it.,", ",,")를 제거했습니다.
키·카테고리가 기존과 같아 메타 등록은 필요 없습니다.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_twomix_geo_2_json.py
사전 준비: la_twomix_geo2_180_bundle.json 을 preset_builders\ 폴더에 두세요.
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_twomix_geo2_180_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)
    missing = [it["key"] for it in presets if not os.path.exists(os.path.join(PRESETS_DIR, it["key"] + ".json"))]
    if missing:
        print(f"주의: 기존에 없던 키 {len(missing)}개가 새로 생성됩니다 (예: {missing[0]})")
    written = 0
    by_group = {}
    for item in presets:
        out = {k: item[k] for k in ("key", "category", "title", "prompt", "meta")}
        with open(os.path.join(PRESETS_DIR, f"{item['key']}.json"), "w", encoding="utf-8") as f2:
            json.dump(out, f2, ensure_ascii=False, indent=2)
        written += 1
        g = "_".join(item["key"].split("_")[1:3])
        by_group[g] = by_group.get(g, 0) + 1
    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 덮어썼습니다.")
    for g, c in sorted(by_group.items()):
        print(f"  la_{g}: {c}개")

if __name__ == "__main__":
    main()
