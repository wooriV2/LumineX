# -*- coding: utf-8 -*-
r"""
la_wax_duo01_replace_bundle.json (1개) -> presets/la_wax_duo_01.json 덮어쓰기.
정면 포즈·부위 나열 표현 제거·마지막 문장 수정을 반영한 새 프롬프트(시험에서 정상 생성 확인). 키·카테고리·제목·메타는 기존 그대로입니다.
사용법: python preset_builders\patch_la_wax_duo01_1_json.py   (메타 등록 불필요)
사전 준비: la_wax_duo01_replace_bundle.json 을 preset_builders\ 폴더에 두세요.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS_DIR = os.path.join(HERE, "..", "presets")

def main():
    with open(os.path.join(HERE, "la_wax_duo01_replace_bundle.json"), "r", encoding="utf-8") as f:
        items = json.load(f)
    for it in items:
        out = {k: it[k] for k in ("key", "category", "title", "prompt", "meta")}
        with open(os.path.join(PRESETS_DIR, it["key"] + ".json"), "w", encoding="utf-8") as f2:
            json.dump(out, f2, ensure_ascii=False, indent=2)
        print("덮어씀:", it["key"])

if __name__ == "__main__":
    main()
