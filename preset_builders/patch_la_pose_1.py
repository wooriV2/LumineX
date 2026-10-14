# -*- coding: utf-8 -*-
r"""
의상 번들(la_clothes_*)에서 가슴을 가리는 팔 포즈(팔짱, 얼굴 감싸기)를 다른 포즈로 교체한다.
  - 프롬프트의 "Pose: ..." 포즈 문장, 제목의 포즈 표기, meta.poses 만 바꾼다. 키·카테고리·나머지 문장은 그대로.
  - 교체 포즈는 키 이름으로 정해져 재실행해도 같은 결과(재실행 시 0개 변경).
  - 옛 값은 preset_builders\pose_swap_backup.json 에 저장 → --undo 로 복구.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_pose_1.py --dry     # 먼저 개수만 확인
  python preset_builders\patch_la_pose_1.py           # 실제 교체
  python preset_builders\patch_la_pose_1.py --undo    # 되돌리기
"""
import glob
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS = os.path.join(HERE, "..", "presets")
BACKUP = os.path.join(HERE, "pose_swap_backup.json")
OLD = {
    "standing tall, arms crossed under her bust, chin raised, looking down at the camera": "팔짱",
    "full frontal, both hands framing the face, chin raised": "얼굴 감싸기",
}
NEW = [
    ("standing full height, both arms slightly spread commanding the frame", "서 있기"),
    ("walking confidently toward the camera, shoulders back, chin lifted", "걷기"),
    ("three-quarter angle, one hand on the outer hip, the other raised overhead", "양팔 들기"),
    ("one hand sweeping her hair back, the other resting on her hip, one leg crossed in front to show the boot", "머리 넘기기"),
    ("turned in profile, back arched, looking over her shoulder, one hand on her hip", "옆모습"),
    ("leaning a shoulder against the doorway, one knee bent, a hand on her thigh", "기대기"),
    ("one hand on her waist, the other lifted to her chin, weight on one leg", "손 허리"),
]


def pick(key):
    h = int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)
    return NEW[h % len(NEW)]


def main():
    dry = "--dry" in sys.argv
    if "--undo" in sys.argv:
        if not os.path.exists(BACKUP):
            print("백업 파일이 없습니다.")
            return
        with open(BACKUP, "r", encoding="utf-8") as f:
            bk = json.load(f)
        n = 0
        for key, old in bk.items():
            path = os.path.join(PRESETS, key + ".json")
            if not os.path.exists(path):
                continue
            with open(path, "w", encoding="utf-8") as f:
                json.dump(old, f, ensure_ascii=False, indent=2)
            n += 1
        print(f"복구 {n}개")
        return
    changed = skipped = 0
    backup = {}
    for path in sorted(glob.glob(os.path.join(PRESETS, "la_clothes_*.json"))):
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        poses = d.get("meta", {}).get("poses") or []
        hit = [p for p in poses if p in OLD]
        if not hit:
            skipped += 1
            continue
        old_pose = hit[0]
        old_ko = OLD[old_pose]
        new_pose, new_ko = pick(d["key"])
        marker = f"Pose: {old_pose} —"
        if d["prompt"].count(marker) != 1 or d["title"].count(f" · {old_ko} · ") != 1:
            print("건너뜀(형식 불일치):", d["key"])
            skipped += 1
            continue
        backup[d["key"]] = json.loads(json.dumps(d))
        d["prompt"] = d["prompt"].replace(marker, f"Pose: {new_pose} —")
        d["title"] = d["title"].replace(f" · {old_ko} · ", f" · {new_ko} · ")
        d["meta"]["poses"] = [new_pose if p == old_pose else p for p in poses]
        changed += 1
        if not dry:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
    if not dry and backup:
        old = {}
        if os.path.exists(BACKUP):
            with open(BACKUP, "r", encoding="utf-8") as f:
                old = json.load(f)
        old.update(backup)
        with open(BACKUP, "w", encoding="utf-8") as f:
            json.dump(old, f, ensure_ascii=False, indent=1)
    print(("[DRY] " if dry else "") + f"포즈 교체 {changed}개 / 건너뜀 {skipped}개")


if __name__ == "__main__":
    main()
