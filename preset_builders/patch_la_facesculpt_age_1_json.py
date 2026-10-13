# -*- coding: utf-8 -*-
r"""
Face Sculpt 연령 번들 2종(혼합 연령 300 + 실버폭스 300) -> presets/la_facesculpt_mix_NNN.json, la_facesculpt_sf_NNN.json

  la_facesculpt_mix_300_bundle.json  (🏺 Living Artifact · Face Sculpt Mixed-Age Formula)
      눈 120 + 입술 120(연령 4단계: 아이돌·20대 후반·30대 후반·실버폭스 균등) + 얼굴 유형 60(원래 나이·머리 유지)
  la_facesculpt_sf_300_bundle.json   (🏺 Living Artifact · Face Sculpt Silverfox Formula)
      눈 150 + 입술 150, 전원 실버폭스(40대 초반~50대 초반, 은발)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_facesculpt_age_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py     (신규 카테고리 2개라 메타 등록 필요)
사전 준비: 위 번들 2개를 preset_builders\ 폴더에 두세요.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS_DIR = os.path.join(HERE, "..", "presets")
BUNDLES = ["la_facesculpt_mix_300_bundle.json", "la_facesculpt_sf_300_bundle.json"]

def main():
    os.makedirs(PRESETS_DIR, exist_ok=True)
    written, by_cat, overwritten = 0, {}, 0
    for name in BUNDLES:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            raise SystemExit(f"번들 파일이 없습니다: {path}")
        with open(path, "r", encoding="utf-8") as f:
            presets = json.load(f)
        for item in presets:
            if not item["category"].startswith("🏺 Living Artifact"):
                raise SystemExit(f"카테고리 접두어 오류: {item['key']}")
            target = os.path.join(PRESETS_DIR, item["key"] + ".json")
            if os.path.exists(target):
                overwritten += 1
            out = {k: item[k] for k in ("key", "category", "title", "prompt", "meta")}
            with open(target, "w", encoding="utf-8") as f2:
                json.dump(out, f2, ensure_ascii=False, indent=2)
            written += 1
            by_cat[item["category"]] = by_cat.get(item["category"], 0) + 1
    if overwritten:
        print(f"주의: 이미 있던 키 {overwritten}개를 덮어썼습니다.")
    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    for c, cnt in by_cat.items():
        print(f"  {c}: {cnt}개")

if __name__ == "__main__":
    main()
