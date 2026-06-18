"""
LumineX 애니&글래머 tier 패치 스크립트
실행: C:\Dev\LumineX\ 루트에서
  python preset_builders/patch_anime_glam_tiers.py
"""

import json, os

# ── 최종 등급 ──────────────────────────────────────────────────────
SSS = [
    # 그룹 1
    "kunoichi_glam", "samurai_bride", "oni_warrior", "cosmic_warrior_glam",
    # 그룹 2
    "dragon_princess", "dark_sorceress_glam",
    # 그룹 3
    "neon_android", "android_2b",
    # 그룹 4
    "vampire_seductress", "vampirella_dark", "manhwa_villainess", "dark_elsa",
    # 그룹 5
    "anime_battle_angel",
    # 그룹 6
    "poison_ivy_vines", "storm_goddess",
    # 그룹 7
    "jessica_rabbit_glam", "barbarella_retro",
]

SS = [
    # 그룹 1
    "anime_demon_slayer",
    # 그룹 2
    "dark_magical_girl", "witch_apprentice", "anime_shrine_maiden", "sailor_moon_dark",
    # 그룹 3
    "android_girl", "ghost_shell", "anime_cyber_ninja",
    # 그룹 4
    "succubus_anime", "dark_jester_glam",
    # 그룹 5
    "battle_bikini", "street_fighter_chun", "anime_swordmistress", "anime_mecha_pilot",
    # 그룹 6
    "anime_galaxy_idol",
    # 그룹 7
    "anime_cel_shaded",
]

S = [
    "zero_suit", "pilot_suit",
    "catgirl_luxe", "fallen_angel_anime", "webtoon_heroine",
]

A = ["anime_webtoon_style"]

PRESETS_DIR = "presets"

def patch(name, tier):
    path = os.path.join(PRESETS_DIR, f"{name}.json")
    if not os.path.exists(path):
        print(f"  [SKIP] {name}.json 없음")
        return
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    changed = False
    if tier == "SSS":
        for k in ["SSS_TIER", "SS_TIER"]:
            if not data.get(k):
                data[k] = True; changed = True
    elif tier == "SS":
        if data.pop("SSS_TIER", None): changed = True
        if not data.get("SS_TIER"):
            data["SS_TIER"] = True; changed = True
    else:
        for k in ["SSS_TIER", "SS_TIER"]:
            if data.pop(k, None): changed = True
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  [OK] {name} → {tier}")
    else:
        print(f"  [--] {name} 변경 없음")

print("=== JSON 패치 ===")
for tier, lst in [("SSS", SSS), ("SS", SS), ("S", S), ("A", A)]:
    print(f"\n[ {tier} ]")
    for name in lst:
        patch(name, tier)

print("\n=== dashboard.py SSS_TIER set에 추가할 항목 ===")
for p in SSS:
    print(f'    "{p}",')

print(f"\n완료: SSS {len(SSS)}종 / SS {len(SS)}종 / S {len(S)}종 / A {len(A)}종")
