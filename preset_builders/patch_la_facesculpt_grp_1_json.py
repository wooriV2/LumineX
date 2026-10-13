# -*- coding: utf-8 -*-
r"""
Face Sculpt Group Formula 140개(2인 60 · 3인 40 · 4인 25 · 5인 15) -> presets/la_facesculpt_grp_NNN.json

  la_facesculpt_grp_140_bundle.json  (신규 카테고리: 🏺 Living Artifact · Face Sculpt Group Formula)
  구성: 한 장면·같은 배경, 인물마다 눈/입술/유형 주인공 + 서로 다른 귀 장식(철 추·혼합 금속 추·단일 금속 추·대형 귀걸이), 실사 문구 포함

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_facesculpt_grp_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py     (신규 카테고리라 메타 등록 필요)
사전 준비: la_facesculpt_grp_140_bundle.json 을 preset_builders\ 폴더에 두세요.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS_DIR = os.path.join(HERE, "..", "presets")
BUNDLES = ["la_facesculpt_grp_140_bundle.json"]

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
