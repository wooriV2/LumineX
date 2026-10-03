# -*- coding: utf-8 -*-
"""
la_fix_ire_uv_bundle.json(300개: 이레즈미·UV네온 섹스텟~데켓(6~10인) 각 30개,
기존 좁은 문양풀(6/7종) 버그를 확장된 문양풀(이레즈미 26종·UV네온 27종)로 수정)을
presets/la_irezumi_*.json / presets/la_uvneon_*.json 개별 파일로 덮어쓰기.

버그 내용: 기존 섹스텟~데켓은 이레즈미 6종·UV네온 7종 문양 풀만 순환해서,
한 이미지 안에 같은 트랙이 여러 번(예: 10인 중 이레즈미 출신 문양 담당 인원이
여럿) 나올 때 문양이 겹칠 수 있었음. 이번 수정으로 각 이미지 안에서 문양이
겹치지 않도록 확장 풀에서 순차 배정.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_fix_ire_uv_1_json.py

사전 준비: la_fix_ire_uv_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요.
카테고리는 기존 그대로(Irezumi Formula / UV Neon Formula)라 메타 등록 스크립트는
다시 실행하지 않아도 됩니다(이미 존재하는 카테고리).
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_fix_ire_uv_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)

    os.makedirs(PRESETS_DIR, exist_ok=True)

    written = 0
    by_type = {}
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
        type_name = "_".join(key.split("_")[:2])
        by_type[type_name] = by_type.get(type_name, 0) + 1

    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 덮어썼습니다.")
    for t,cnt in by_type.items():
        print(f"  {t}: {cnt}개")

if __name__ == "__main__":
    main()
