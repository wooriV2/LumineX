"""
cleanup_root_v1.py
루트의 add_* / patch_* 파일들을 preset_builders 폴더로 이동
실행: python cleanup_root_v1.py
"""

from pathlib import Path
import shutil

ROOT = Path(".")
TARGET = Path("preset_builders")
TARGET.mkdir(exist_ok=True)

# 이동 대상 파일 목록
MOVE_FILES = [
    "add_new_presets_v23.py",
    "add_new_presets_v24.py",
    "add_new_presets_v25.py",
    "patch_dashboard_v25.py",
    "patch_model_types_v27.py",
    "patch_model_types_v28.py",
    "patch_presets_v26.py",
    "patch_ss_tier_v29.py",
    "patch_ss_tier_v30.py",
]

def move_files():
    moved = 0
    skipped = 0
    for filename in MOVE_FILES:
        src = ROOT / filename
        dst = TARGET / filename
        if src.exists():
            if dst.exists():
                print(f"[SKIP] 이미 존재: preset_builders/{filename}")
                skipped += 1
            else:
                shutil.move(str(src), str(dst))
                print(f"[OK] 이동: {filename} → preset_builders/")
                moved += 1
        else:
            print(f"[WARN] 파일 없음: {filename}")
            skipped += 1

    print(f"\n총 {moved}개 이동 완료, {skipped}개 건너뜀")

if __name__ == "__main__":
    print("=== 루트 정리 시작 ===")
    move_files()
    print("=== 완료 ===")
    print("이후 패치 스크립트는 preset_builders/ 폴더에서 생성/실행하세요.")
