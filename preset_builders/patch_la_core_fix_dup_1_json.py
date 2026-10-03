# -*- coding: utf-8 -*-
"""
la_core_bundle.json(472개 중복문장 버그 수정본 — 기존 Core Formula 솔로~10인
500개 중 중복이 있던 472개를 고치고, 나머지 28개는 원본 그대로 포함)을
presets/la_core_*.json 개별 파일로 덮어쓰기.

버그 내용: Physique 문단에 "An extraordinarily large woman, far beyond any
real person."이 BODY_FULL 딕셔너리 자체의 같은 문장과 겹쳐 두 번 연속
반복되던 문제. 이번 수정으로 한 문장으로 정리됨.

영향 범위: la_core_solo_*, la_core_duo_*, la_core_trio_*, la_core_quartet_*,
la_core_quintet_*, la_core_sextet_*, la_core_septet_*, la_core_octet_*,
la_core_nonet_*, la_core_decet_* (1~10인). 11~14인(undecet~quattuordecet)은
애초에 이 버그가 없어 이번 파일에 포함되지 않음 — 그대로 둬도 됩니다.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_core_fix_dup_1_json.py

사전 준비: la_core_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요
(기존에 있던 동명 파일이 있다면 이걸로 덮어쓰세요).
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_core_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)

    os.makedirs(PRESETS_DIR, exist_ok=True)

    written = 0
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

    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 덮어썼습니다.")

if __name__ == "__main__":
    main()
