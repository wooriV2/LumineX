# -*- coding: utf-8 -*-
r"""
신규 번들 5종을 한 번에 presets/ 에 생성합니다(총 690개).

  la_pregmat_geo_180_bundle.json   임산부 재질 블렌드            180  (신규 카테고리)
  la_pregblend2_geo_90_bundle.json 임산부 2혼합                   90  (기존 Pregnant Blend Formula에 키 추가)
  la_genmat_geo_180_bundle.json    일반인 재질 블렌드            180  (신규 카테고리)
  la_trackmix_geo_120_bundle.json  트랙 혼합(일반·임산부·맥시)   120  (신규 카테고리)
  la_leafmix_geo_120_bundle.json   금박 색 혼합(검은 피부 맥시)  120  (신규 카테고리)

추가로, 앞서 등록된 la_pregblend3_* / la_pregblend4_* (180개)의 카테고리 이모지(🤰)를 🏺로 고칩니다.
메타 등록 스크립트가 🏺로 시작하는 카테고리만 받아서, 그 180개가 메타에서 빠져 있었습니다.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_new5_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py        # 새 카테고리·키 등록
사전 준비: 위 번들 5개를 preset_builders\ 폴더에 두세요.
"""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS_DIR = os.path.join(HERE, "..", "presets")
BUNDLES = ["la_pregmat_geo_180_bundle.json", "la_pregblend2_geo_90_bundle.json", "la_genmat_geo_180_bundle.json",
           "la_trackmix_geo_120_bundle.json", "la_leafmix_geo_120_bundle.json"]

def fix_existing_category():
    fixed = 0
    for pat in ("la_pregblend3_*.json", "la_pregblend4_*.json"):
        for path in sorted(glob.glob(os.path.join(PRESETS_DIR, pat))):
            with open(path, "r", encoding="utf-8") as f:
                item = json.load(f)
            if item.get("category", "").startswith("\U0001F930"):
                item["category"] = item["category"].replace("\U0001F930", "\U0001F3FA")
                with open(path, "w", encoding="utf-8") as f2:
                    json.dump(item, f2, ensure_ascii=False, indent=2)
                fixed += 1
    print(f"기존 Pregnant Blend Formula 카테고리 이모지 수정: {fixed}개")

def main():
    missing = [b for b in BUNDLES if not os.path.exists(os.path.join(HERE, b))]
    if missing:
        print("번들 파일이 없습니다:", ", ".join(missing))
        return
    os.makedirs(PRESETS_DIR, exist_ok=True)
    fix_existing_category()
    total, by_cat = 0, {}
    for b in BUNDLES:
        with open(os.path.join(HERE, b), "r", encoding="utf-8") as f:
            presets = json.load(f)
        exist = sum(os.path.exists(os.path.join(PRESETS_DIR, it["key"] + ".json")) for it in presets)
        if exist:
            print(f"주의: {b} 에서 이미 있던 키 {exist}개를 덮어씁니다")
        for it in presets:
            out = {k: it[k] for k in ("key", "category", "title", "prompt", "meta")}
            with open(os.path.join(PRESETS_DIR, it["key"] + ".json"), "w", encoding="utf-8") as f2:
                json.dump(out, f2, ensure_ascii=False, indent=2)
            total += 1
            by_cat[it["category"]] = by_cat.get(it["category"], 0) + 1
        print(f"  {b}: {len(presets)}개")
    print(f"완료: 총 {total}개 preset 파일을 생성했습니다.")
    for c, n in by_cat.items():
        print(f"  {c}: {n}개")

if __name__ == "__main__":
    main()
