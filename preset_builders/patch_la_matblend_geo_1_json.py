# -*- coding: utf-8 -*-
r"""
la_matblend_geo_180_bundle.json (180개) -> presets/la_matblend{3|4}_{solo|duo|trio}_{01~30}.json 덮어쓰기.

Material Blend Formula 의 3·4혼합 전체(솔로·듀오·트리오 각 30개씩 x 2)를 새 방식으로 교체합니다.
 - 구역 배치: 가로 띠 / 세로 띠 / 대각 띠 / 동심원 / 부채꼴 5종 x 경계선(매끈/물결) 중 인물마다 랜덤,
   같은 이미지 안에서는 구조가 겹치지 않음. 위치 숫자(%)는 매번 1% 단위로 랜덤.
 - 경계는 전부 희미한 전환 구간, 구조는 부위 이름 없이 선·중심점·시계 방향으로만 기술.
 - 재질 16종(공작눈무늬 포함)에서 인물마다 랜덤. 석재와 목재는 한 인물에 같이 넣지 않음(미검증 조합).
 - UV네온이 들어간 인물에는 해당 구역 전용 블랙라이트 문장. 포즈는 구역이 보이는 정면 계열만 사용.
키와 카테고리가 기존과 같으므로 메타 등록 스크립트(patch_livingartifact_2_meta.py)는 필요 없습니다.
2혼합(90개)과 Craft Blend 는 이번에 바꾸지 않습니다.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_matblend_geo_1_json.py

사전 준비: la_matblend_geo_180_bundle.json 을 preset_builders\ 폴더에 두세요.
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_matblend_geo_180_bundle.json")
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
