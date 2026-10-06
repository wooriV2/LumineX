# -*- coding: utf-8 -*-
r"""
제목에 재질명(금박 색 혼합은 색 이름)을 추가합니다. 프리셋 파일의 "title" 항목만 바꾸고 프롬프트는 건드리지 않습니다.

  la_pregmat{3|4}_*   임산부 재질 블렌드        180
  la_genmat{3|4}_*    일반 재질 블렌드          180
  la_trackmix{3|4}_*  트랙 혼합                 120
  la_s2pack_*         Structure Pack            120
  la_leafmix_*        금박 색 혼합              120   (합 720)

제목 형식: "... (구조·경계선 / 구조·경계선 | 재질+재질+재질 / 재질+재질+재질)"  — 인물 순서대로, 구역 순서대로.
키·카테고리가 그대로라 메타 등록은 필요 없습니다.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_titles_1_json.py
사전 준비: la_titles_patch_bundle.json 을 preset_builders\ 폴더에 두세요.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS_DIR = os.path.join(HERE, "..", "presets")

def main():
    with open(os.path.join(HERE, "la_titles_patch_bundle.json"), "r", encoding="utf-8") as f:
        titles = json.load(f)
    updated = unchanged = missing = 0
    for key, title in titles.items():
        path = os.path.join(PRESETS_DIR, key + ".json")
        if not os.path.exists(path):
            missing += 1
            continue
        with open(path, "r", encoding="utf-8") as f:
            item = json.load(f)
        if item.get("title") == title:
            unchanged += 1
            continue
        item["title"] = title
        with open(path, "w", encoding="utf-8") as f2:
            json.dump(item, f2, ensure_ascii=False, indent=2)
        updated += 1
    print(f"완료: 제목 수정 {updated}개 / 이미 같음 {unchanged}개 / 파일 없음 {missing}개 (대상 {len(titles)}개)")

if __name__ == "__main__":
    main()
