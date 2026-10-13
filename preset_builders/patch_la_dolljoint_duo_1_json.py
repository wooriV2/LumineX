# -*- coding: utf-8 -*-
r"""
la_dolljoint_duo_30_bundle.json(인형 관절 듀오 30개, 인형끼리)을 presets/la_dolljoint_duo_*.json 개별 파일로 생성.
카테고리는 기존 '🏺 Living Artifact · Doll Joint Formula'을 그대로 쓴다(새 카테고리 없음, 키 30개 추가).

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_dolljoint_duo_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py

사전 준비: la_dolljoint_duo_30_bundle.json 을 preset_builders\ 폴더에 함께 두세요.
"""
import json
import os

HERE = os.path.dirname(__file__)
BUNDLE = os.path.join(HERE, "la_dolljoint_duo_30_bundle.json")
PRESETS_DIR = os.path.join(HERE, "..", "presets")

def main():
    with open(BUNDLE, "r", encoding="utf-8") as f:
        items = json.load(f)
    os.makedirs(PRESETS_DIR, exist_ok=True)
    written = overwritten = 0
    for item in items:
        out = {"key": item["key"], "category": item["category"], "title": item["title"],
               "prompt": item["prompt"], "meta": item["meta"]}
        path = os.path.join(PRESETS_DIR, f"{item['key']}.json")
        if os.path.exists(path):
            overwritten += 1
        with open(path, "w", encoding="utf-8") as f2:
            json.dump(out, f2, ensure_ascii=False, indent=2)
        written += 1
    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다. ({items[0]['category']})")
    if overwritten:
        print(f"  (기존 파일 덮어쓰기: {overwritten}개)")

if __name__ == "__main__":
    main()
