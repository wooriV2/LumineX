# -*- coding: utf-8 -*-
r"""
la_kintsuliquid_120_bundle.json(120개: Kintsugi Liquid Metal — 킨츠기(붙임·그림)·리퀴드골드·리퀴드실버를 마스터 생성기의 모든 축(체형 36·포즈 44·나이 12·인종 10·배경 70·조명·분위기·앵글·신발 35종·2인 구도 9종)과
함께 전부 랜덤으로 섞은 번들. 솔로~5인 각 24개, 그룹에서는 다른 18재질도 섞임)를 presets/la_kl_*.json 개별 파일로 생성.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_kintsuliquid_1_json.py

사전 준비: la_kintsuliquid_120_bundle.json 파일을 preset_builders\ 폴더에 함께 두세요.

이후 2단계: python preset_builders\patch_livingartifact_2_meta.py
(카테고리 1개가 새로 생깁니다: Kintsugi Liquid Metal Formula, "🏺 Living Artifact ·" 접두어 사용)
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_kintsuliquid_120_bundle.json")
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
