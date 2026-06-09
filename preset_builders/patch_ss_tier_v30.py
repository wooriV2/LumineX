"""
patch_ss_tier_v30.py
SS tier 추가 + v23 차단 2종 삭제
1. unicorn_opal SS 확정
2. v23 개방형 바디페인팅 SS 12종 추가
3. pastel_dream / minimalist_free 삭제 (차단 확인)
대상: dashboard.py, presets/ 폴더
실행: python patch_ss_tier_v30.py
"""

from pathlib import Path
import shutil

DASHBOARD_PATH = Path("dashboard.py")
PRESETS_DIR = Path("presets")
DELETED_DIR = Path("_deleted_presets")

# SS tier 추가 13종
NEW_SS = [
    "unicorn_opal",
    "body_paint_watercolor_free",
    "body_paint_metallic_free",
    "body_paint_impasto",
    "body_paint_airbrush",
    "body_paint_monochrome",
    "body_paint_earth_tones",
    "body_paint_jewel_tones",
    "body_paint_iridescent_free",
    "body_paint_geometric_free",
    "body_paint_organic_flow",
    "body_paint_surreal_free",
    "body_paint_glitter_free",
]

# 차단 확인 삭제 2종
DELETE_PRESETS = [
    "body_paint_pastel_dream",
    "body_paint_minimalist_free",
]

# SS_TIER 앵커
ANCHOR = '    "anime_eu_ligne_claire",\n}'

INSERT_BLOCK = '''    "anime_eu_ligne_claire",
    # 2026-06-09 unicorn_opal SS 확정 (2장 일관성 검증 완료)
    "unicorn_opal",
    # 2026-06-09 v23 개방형 바디페인팅 SS 12종 확정
    # 타율 90% (18/20) — pastel_dream/minimalist_free 차단 삭제
    "body_paint_watercolor_free","body_paint_metallic_free","body_paint_impasto","body_paint_airbrush",
    "body_paint_monochrome","body_paint_earth_tones","body_paint_jewel_tones","body_paint_iridescent_free",
    "body_paint_geometric_free","body_paint_organic_flow","body_paint_surreal_free","body_paint_glitter_free",
}'''

def patch_ss_tier():
    if not DASHBOARD_PATH.exists():
        print(f"[ERROR] {DASHBOARD_PATH} 없음.")
        return False

    text = DASHBOARD_PATH.read_text(encoding="utf-8")

    # SS_TIER 섹션 체크
    ss_start = text.find("SS_TIER = {")
    ss_end = text.find("\n}", ss_start) + 2
    ss_block = text[ss_start:ss_end]

    if "unicorn_opal" in ss_block:
        print("[WARN] 이미 패치됨.")
        return False

    if ANCHOR not in text:
        print(f"[ERROR] 앵커 미발견.")
        return False

    new_text = text.replace(ANCHOR, INSERT_BLOCK)
    DASHBOARD_PATH.write_text(new_text, encoding="utf-8")
    print(f"[OK] SS tier 13종 추가 완료")
    for s in NEW_SS:
        print(f"  ⭐ {s}")
    return True

def delete_presets():
    DELETED_DIR.mkdir(exist_ok=True)
    for name in DELETE_PRESETS:
        src = PRESETS_DIR / f"{name}.json"
        dst = DELETED_DIR / f"{name}.json"
        if src.exists():
            shutil.move(str(src), str(dst))
            print(f"[OK] 삭제(이동): {name}.json → _deleted_presets/")
        else:
            print(f"[WARN] 파일 없음: {name}.json")

def patch_preset_categories():
    """dashboard.py PRESET_CATEGORIES에서 삭제 프리셋 제거"""
    text = DASHBOARD_PATH.read_text(encoding="utf-8")
    for name in DELETE_PRESETS:
        text = text.replace(f'        "{name}",\n', '')
        text = text.replace(f"        '{name}',\n", '')
    DASHBOARD_PATH.write_text(text, encoding="utf-8")
    print(f"[OK] PRESET_CATEGORIES에서 {len(DELETE_PRESETS)}종 제거 완료")

if __name__ == "__main__":
    print("=== patch_ss_tier_v30 시작 ===")
    if patch_ss_tier():
        delete_presets()
        patch_preset_categories()
        print("\n=== 완료 ===")
        print(f"SS tier +13종 (unicorn_opal + v23 바디페인팅 12종)")
        print(f"삭제: pastel_dream, minimalist_free")
