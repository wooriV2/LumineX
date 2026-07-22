# -*- coding: utf-8 -*-
"""
deepblack_trio.json → 개별 JSON 파일 분리 스크립트

저장 위치: C:\Dev\LumineX\preset_builders\split_deepblack_trio_json.py
"""

import json
import shutil
from pathlib import Path

BASE = Path("C:/Dev/LumineX")
JSON_PATH = BASE / "presets/deepblack_trio.json"
PRESETS_DIR = BASE / "presets"

def split_json():
    # 백업
    shutil.copy(JSON_PATH, str(JSON_PATH) + ".bak2")
    print(f"📦 백업 완료: {JSON_PATH}.bak2")

    # 읽기
    with open(JSON_PATH, encoding="utf-8-sig") as f:
        data = json.load(f)

    print(f"📋 총 {len(data)}개 키 발견")

    created, skipped = [], []

    for key, val in data.items():
        out_path = PRESETS_DIR / f"{key}.json"
        if out_path.exists():
            skipped.append(key)
            continue

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(val, f, ensure_ascii=False, indent=2)
        created.append(key)
        print(f"  ✅ {key}.json")

    print(f"\n완료: 생성 {len(created)}개 / 스킵 {len(skipped)}개")
    if skipped:
        print("스킵 목록:")
        for s in skipped:
            print(f"  ⚠️ {s}")

    # deepblack_trio.json 삭제 여부 확인
    print(f"\n⚠️ deepblack_trio.json은 수동으로 삭제하거나 git rm 하세요:")
    print(f"   git rm presets/deepblack_trio.json")

if __name__ == "__main__":
    split_json()
