# -*- coding: utf-8 -*-
r"""
Ext Formula 번들 6개(727개)를 presets/ 개별 파일로 생성한다.
  la_ext_fm_bundle.json      -> la_fmart/fmmin/fmbond/fmpub_solo_*      (여얼굴+남체형 250)
  la_ext_mf_bundle.json      -> la_mfart/mfmin/mfpub/mfbond_solo_*      (남얼굴+여체형 206)
  la_ext_mfpreg_bundle.json  -> la_mfpreg/mfpregmin_solo_*              (남얼굴+임산부 70)
  la_ext_duo_bundle.json     -> la_mfduopg_duo_*                        (남성+임산부 듀오 30)
  la_ext_prop_bundle.json    -> la_prop_solo_*                          (소품 들기 114)
  la_ext_echo_bundle.json    -> la_uvecho_solo_*, la_paintecho_solo_*   (에코 57)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_extformula_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py --dry
  python preset_builders\patch_livingartifact_2_meta.py

사전 준비: 위 번들 JSON 6개를 이 스크립트와 같은 preset_builders\ 폴더에 두세요.
"""
import json
import os

HERE = os.path.dirname(__file__)
BUNDLES = ["la_ext_fm_bundle.json", "la_ext_mf_bundle.json", "la_ext_mfpreg_bundle.json",
           "la_ext_duo_bundle.json", "la_ext_prop_bundle.json", "la_ext_echo_bundle.json"]
PRESETS_DIR = os.path.join(HERE, "..", "presets")

def main():
    os.makedirs(PRESETS_DIR, exist_ok=True)
    total = overwritten = 0
    for fn in BUNDLES:
        with open(os.path.join(HERE, fn), "r", encoding="utf-8") as f:
            items = json.load(f)
        n = 0
        for item in items:
            out = {"key": item["key"], "category": item["category"], "title": item["title"],
                   "prompt": item["prompt"], "meta": item["meta"]}
            path = os.path.join(PRESETS_DIR, f"{item['key']}.json")
            if os.path.exists(path):
                overwritten += 1
            with open(path, "w", encoding="utf-8") as f2:
                json.dump(out, f2, ensure_ascii=False, indent=2)
            n += 1
        total += n
        print(f"  {fn}: {n}개")
    print(f"완료: {total}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    if overwritten:
        print(f"  (기존 파일 덮어쓰기: {overwritten}개)")

if __name__ == "__main__":
    main()
