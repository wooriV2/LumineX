# -*- coding: utf-8 -*-
r"""
la_extreme_180_bundle.json(180개: Extreme Body Formula — 극단 체형(USSBBW·hourglass SSBBW) 솔로 120 + 듀오 30 + 트리오 30,
B 60 : A 40 페인트 연동, 솔로 앉은 자세, 하이앵글 제외, 듀오 이상 극단 포즈 제외)를 presets/la_xb_*.json 개별 파일로 생성.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_extreme_1_json.py

사전 준비: la_extreme_180_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요.

이후 2단계: 기존에 쓰시던 카테고리 등록 스크립트를 그대로 실행하세요.
  python preset_builders\patch_livingartifact_2_meta.py
(카테고리 1개가 새로 생깁니다: Extreme Body Formula, "🏺 Living Artifact ·" 접두어 사용)
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_extreme_180_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)

    os.makedirs(PRESETS_DIR, exist_ok=True)

    written = 0
    overwritten = 0
    by_track = {}
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
        if os.path.exists(out_path):
            overwritten += 1
        with open(out_path, "w", encoding="utf-8") as f2:
            json.dump(out, f2, ensure_ascii=False, indent=2)
        written += 1
        track = key.rsplit("_", 2)[0]
        by_track[track] = by_track.get(track, 0) + 1

    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    if overwritten:
        print(f"  (기존 파일 덮어쓰기: {overwritten}개)")
    for t in sorted(by_track):
        print(f"  {t}: {by_track[t]}개")

if __name__ == "__main__":
    main()
