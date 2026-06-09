"""
preset_builders/patch_ss_tier_v31.py
SS tier 추가: 애니 A형 6종 확정
- anime_swordmistress / anime_mecha_pilot / anime_shrine_maiden
- anime_galaxy_idol / anime_battle_angel / anime_cyber_ninja
대상: dashboard.py
실행: python preset_builders/patch_ss_tier_v31.py
"""

from pathlib import Path

DASHBOARD_PATH = Path("dashboard.py")

ANCHOR = '    "body_paint_geometric_free","body_paint_organic_flow","body_paint_surreal_free","body_paint_glitter_free",\n}'

NEW_BLOCK = '''    "body_paint_geometric_free","body_paint_organic_flow","body_paint_surreal_free","body_paint_glitter_free",
    # 2026-06-09 애니 A형 SS 6종 확정 (v24, 7/7 차단 0건)
    # demon_slayer 보류 (swordmistress와 중복)
    "anime_swordmistress","anime_mecha_pilot","anime_shrine_maiden",
    "anime_galaxy_idol","anime_battle_angel","anime_cyber_ninja",
}'''

def patch():
    if not DASHBOARD_PATH.exists():
        print(f"[ERROR] {DASHBOARD_PATH} 없음.")
        return

    text = DASHBOARD_PATH.read_text(encoding="utf-8")

    ss_start = text.find("SS_TIER = {")
    ss_end = text.find("\n}", ss_start) + 2
    ss_block = text[ss_start:ss_end]

    if "anime_swordmistress" in ss_block:
        print("[WARN] 이미 패치됨.")
        return

    if ANCHOR not in text:
        print("[ERROR] 앵커 미발견.")
        return

    new_text = text.replace(ANCHOR, NEW_BLOCK)
    DASHBOARD_PATH.write_text(new_text, encoding="utf-8")
    print("[OK] SS tier 6종 추가 완료")
    for s in ["anime_swordmistress","anime_mecha_pilot","anime_shrine_maiden",
              "anime_galaxy_idol","anime_battle_angel","anime_cyber_ninja"]:
        print(f"  ⭐ {s}")

if __name__ == "__main__":
    patch()
