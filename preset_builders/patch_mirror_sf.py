"""
LumineX Tier 패치 — 거울&반사 G1~G4 + SF&바이오펑크 G1~G4
실행: python preset_builders/patch_mirror_sf.py (C:\Dev\LumineX\ 에서)

판정 요약:
🪞 거울&반사 (24종): HOF 7 / SSS 13 / SS 4
🧬 SF&바이오펑크 (23종): HOF 10 / SSS 10 / SS 2 / 미판정 1(synthetic_skin_tear → SS 잠정)
"""

DASHBOARD_PATH = "dashboard.py"

# ── 🪞 거울 & 반사 ──────────────────────────────────────
MIRROR_HOF = [
    "hall_of_mirrors_glam",
    "mercury_lake_reflection",
    "flooded_temple_mirror",
    "glass_box_all_angles",
    "crystal_cave_skin_facets",
    "chrome_sphere_world",
    "liquid_metal_pool",
]

MIRROR_SSS = [
    "infinity_mirror_goddess",
    "venetian_mirror_boudoir",
    "broken_mirror_multiplied",
    "salt_flat_sky_merge",
    "rain_puddle_city_invert",
    "prism_light_body_split",
    "window_rain_double",
    "soap_bubble_dome",
    "polished_obsidian_floor",
    "supercar_chrome_reflect",
    "foil_room_crush",
    "mirrored_skyscraper_facade",
    # HOF도 SSS에 포함
    "hall_of_mirrors_glam",
    "mercury_lake_reflection",
    "flooded_temple_mirror",
    "glass_box_all_angles",
    "crystal_cave_skin_facets",
    "chrome_sphere_world",
    "liquid_metal_pool",
]

MIRROR_SS = [
    "obsidian_mirror_ritual",
    "cheval_mirror_reveal",
    "infinity_pool_edge_reflect",
    "morning_dew_skin_reflection",
    "two_way_mirror_watcher",
    # SSS도 SS에 포함
    "infinity_mirror_goddess",
    "venetian_mirror_boudoir",
    "broken_mirror_multiplied",
    "salt_flat_sky_merge",
    "rain_puddle_city_invert",
    "prism_light_body_split",
    "window_rain_double",
    "soap_bubble_dome",
    "polished_obsidian_floor",
    "supercar_chrome_reflect",
    "foil_room_crush",
    "mirrored_skyscraper_facade",
    "hall_of_mirrors_glam",
    "mercury_lake_reflection",
    "flooded_temple_mirror",
    "glass_box_all_angles",
    "crystal_cave_skin_facets",
    "chrome_sphere_world",
    "liquid_metal_pool",
]

# ── 🧬 SF & 바이오펑크 ──────────────────────────────────
SF_HOF = [
    "specimen_amber_suspended",
    "gene_sequencer_data_skin",
    "petri_dish_giant_macro",
    "coral_organism_absorption",
    "carnivorous_plant_trap",
    "jellyfish_bloom_float",
    "neural_lace_crown",
    "spine_tech_implant",
    "virus_pattern_body",
    "metamorphosis_editorial",
]

SF_SSS = [
    "cryo_emergence_wet",
    "clean_room_latex_protocol",
    "quarantine_protocol_breach",
    "abyssal_pressure_glam",
    "mycelium_web_consumed",
    "symbiote_second_skin",
    "cyborg_partial_reveal",
    "prosthetic_art",
    "mutation_bloom",
    "toxic_spore_cloud",
    "alien_host_glam",
    # HOF도 SSS에 포함
    "specimen_amber_suspended",
    "gene_sequencer_data_skin",
    "petri_dish_giant_macro",
    "coral_organism_absorption",
    "carnivorous_plant_trap",
    "jellyfish_bloom_float",
    "neural_lace_crown",
    "spine_tech_implant",
    "virus_pattern_body",
    "metamorphosis_editorial",
]

SF_SS = [
    "exoskeleton_stripped",
    "infection_glam",
    "synthetic_skin_tear",  # 잠정 SS — 이미지 확인 후 수정 가능
    # SSS도 SS에 포함
    "cryo_emergence_wet",
    "clean_room_latex_protocol",
    "quarantine_protocol_breach",
    "abyssal_pressure_glam",
    "mycelium_web_consumed",
    "symbiote_second_skin",
    "cyborg_partial_reveal",
    "prosthetic_art",
    "mutation_bloom",
    "toxic_spore_cloud",
    "alien_host_glam",
    "specimen_amber_suspended",
    "gene_sequencer_data_skin",
    "petri_dish_giant_macro",
    "coral_organism_absorption",
    "carnivorous_plant_trap",
    "jellyfish_bloom_float",
    "neural_lace_crown",
    "spine_tech_implant",
    "virus_pattern_body",
    "metamorphosis_editorial",
]


def add_to_set(content: str, set_name: str, keys: list[str]) -> tuple[str, int]:
    import re
    pattern = rf'({re.escape(set_name)}\s*=\s*\{{)'
    match = re.search(pattern, content)
    if not match:
        return content, 0

    added = 0
    insert_pos = match.end()
    for key in keys:
        if f'"{key}"' not in content[match.start():match.start()+500]:
            content = content[:insert_pos] + f'\n    "{key}",' + content[insert_pos:]
            added += 1
    return content, added


def patch():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    report = []

    # HOF_TIER
    all_hof = MIRROR_HOF + SF_HOF
    content, n = add_to_set(content, "HOF_TIER", all_hof)
    report.append(f"  HOF_TIER: {n}종 추가")

    # SSS_TIER
    all_sss = list(dict.fromkeys(MIRROR_SSS + SF_SSS))
    content, n = add_to_set(content, "SSS_TIER", all_sss)
    report.append(f"  SSS_TIER: {n}종 추가")

    # SS_TIER
    all_ss = list(dict.fromkeys(MIRROR_SS + SF_SS))
    content, n = add_to_set(content, "SS_TIER", all_ss)
    report.append(f"  SS_TIER: {n}종 추가")

    if content == original:
        print("변경 사항 없음.")
        return

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {DASHBOARD_PATH} 패치 완료\n")
    for r in report:
        print(r)

    print("\n📋 검증:")
    print('  Select-String -Path dashboard.py -Pattern "hall_of_mirrors_glam|specimen_amber_suspended|jellyfish_bloom_float"')


if __name__ == "__main__":
    print("=" * 60)
    print("LumineX Tier 패치: 거울&반사 + SF&바이오펑크")
    print("=" * 60)
    patch()
