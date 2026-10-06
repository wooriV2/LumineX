# -*- coding: utf-8 -*-
r"""
피어싱 확장 번들 2종(120개) -> presets/ 에 새로 생성합니다.

  la_pframe_maxmk_60_bundle.json    Piercing Frame Formula   60   (기존 카테고리에 키 추가: 맥시멀리스트 메이크업 얼굴 컷)
  la_pstatue_ext_60_bundle.json    Piercing Statue Formula  60   (기존 카테고리에 키 추가: 새 재질 단일·P200 반영 혼합)

키: la_pframe_maxmk_NNN, la_pstatue_ext_NNN
사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_pierce3_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py        # 새 카테고리·키 등록
사전 준비: 위 번들 2개를 preset_builders\ 폴더에 두세요.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS_DIR = os.path.join(HERE, "..", "presets")
BUNDLES = ["la_pframe_maxmk_60_bundle.json", "la_pstatue_ext_60_bundle.json"]

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
