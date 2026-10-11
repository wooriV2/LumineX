# -*- coding: utf-8 -*-
r"""
등록된 프리셋의 제목(title)만 공통 틀로 바꿉니다. 프롬프트·메타는 건드리지 않습니다. (여러 번 실행해도 안전)
  새 틀: 시리즈 인원 #번호 · 체형 · 재질 · (솔로만 포즈) · 배경 · 메이크업

대상 12개 시리즈 2,850개: la_mx, la_lm, la_sm, la_pm, la_mm, la_wood2, la_stone2, la_wsmix, la_xb, la_kl, la_tank_db, la_tank_hip

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_retitle_1.py --dry    # 수정 없이 개수만 확인
  python preset_builders\patch_la_retitle_1.py          # 실제 수정 (옛 제목은 preset_builders\retitle_old_titles_backup.json 에 저장)

사전 준비: la_retitle_map.json 을 preset_builders\ 폴더에 함께 두세요.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAP_PATH = os.path.join(HERE, "la_retitle_map.json")
BACKUP_PATH = os.path.join(HERE, "retitle_old_titles_backup.json")
PRESETS_DIR = os.path.join(HERE, "..", "presets")

def main():
    dry = "--dry" in sys.argv
    with open(MAP_PATH, "r", encoding="utf-8") as f:
        mapping = json.load(f)
    old = {}
    if os.path.exists(BACKUP_PATH):
        with open(BACKUP_PATH, "r", encoding="utf-8") as f:
            old = json.load(f)
    changed = same = missing = 0
    for key, new_title in mapping.items():
        path = os.path.join(PRESETS_DIR, key + ".json")
        if not os.path.exists(path):
            missing += 1
            continue
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        if d.get("title") == new_title:
            same += 1
            continue
        changed += 1
        if not dry:
            old.setdefault(key, d.get("title"))
            d["title"] = new_title
            with open(path, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
    if not dry and changed:
        with open(BACKUP_PATH, "w", encoding="utf-8") as f:
            json.dump(old, f, ensure_ascii=False, indent=1)
    print(("[DRY] " if dry else "") + f"제목 변경 {changed}개 / 이미 같음 {same}개 / 파일 없음 {missing}개 (대상 {len(mapping)}개)")

if __name__ == "__main__":
    main()
