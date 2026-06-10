"""
preset_builders/patch_ss_tier_v32.py
SS tier 추가: 럭셔리 글래머 검증 완료 24종
- 그룹1 블랙/다크 7종
- 그룹2 골드/화이트 9종
- 그룹3 레드카펫/런웨이 8종
대상: dashboard.py
실행: python preset_builders/patch_ss_tier_v32.py
"""

from pathlib import Path

DASHBOARD_PATH = Path("dashboard.py")

ANCHOR = '    "anime_swordmistress","anime_mecha_pilot","anime_shrine_maiden",\n    "anime_galaxy_idol","anime_battle_angel","anime_cyber_ninja",\n}'

NEW_BLOCK = '''    "anime_swordmistress","anime_mecha_pilot","anime_shrine_maiden",
    "anime_galaxy_idol","anime_battle_angel","anime_cyber_ninja",
    # 2026-06-10 럭셔리 글래머 그룹1 — 블랙/다크 7종
    "black_mirror","noir_opulence","velvet_darkness","luxury_noir",
    "lace_noir","midnight_couture","velvet_serpent",
    # 2026-06-10 럭셔리 글래머 그룹2 — 골드/화이트 9종
    "golden_oil","golden_nude","gold_temptress","golden_hour_editorial",
    "platinum_elite","ivory_silk","pearl_essence","velvet_gold","diamond_couture",
    # 2026-06-10 럭셔리 글래머 그룹3 — 레드카펫/런웨이 8종
    "runway_power","red_carpet","red_temptress","crimson_gown",
    "opera_glam","silver_screen","crystal_gown","baroque_glam",
}'''

def patch():
    if not DASHBOARD_PATH.exists():
        print(f"[ERROR] {DASHBOARD_PATH} 없음.")
        return

    text = DASHBOARD_PATH.read_text(encoding="utf-8")

    ss_start = text.find("SS_TIER = {")
    ss_end = text.find("\n}", ss_start) + 2
    ss_block = text[ss_start:ss_end]

    if "black_mirror" in ss_block:
        print("[WARN] 이미 패치됨.")
        return

    if ANCHOR not in text:
        print("[ERROR] 앵커 미발견.")
        return

    new_text = text.replace(ANCHOR, NEW_BLOCK)
    DASHBOARD_PATH.write_text(new_text, encoding="utf-8")
    print("[OK] SS tier 24종 추가 완료")
    print("  그룹1 블랙/다크: 7종")
    print("  그룹2 골드/화이트: 9종")
    print("  그룹3 레드카펫/런웨이: 8종")
    print("  SS tier 총계: 150 + 24 = 174개")

if __name__ == "__main__":
    patch()
