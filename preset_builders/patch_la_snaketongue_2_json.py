# -*- coding: utf-8 -*-
r"""
뱀 혀 솔로 240개를 presets/ 개별 파일로 생성한다.
  la_snaketongue_240_bundle.json -> la_snaketongue_solo_001~240
  (001~120: 기존 키에 피부 문장 수정본 덮어쓰기, 121~240: 새 조립 방식 추가분)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_snaketongue_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py

사전 준비: 번들 JSON을 이 스크립트와 같은 preset_builders\ 폴더에 두세요.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLES = ["la_snaketongue_240_bundle.json"]
PRESETS_DIR = os.path.join(HERE, "..", "presets")
CAT_PREFIX = "\U0001F3FA Living Artifact"


def main():
    os.makedirs(PRESETS_DIR, exist_ok=True)
    total = overwritten = 0
    for fn in BUNDLES:
        with open(os.path.join(HERE, fn), "r", encoding="utf-8-sig") as f:
            items = json.load(f)
        n = 0
        for item in items:
            assert item["category"].startswith(CAT_PREFIX), item["category"]
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
