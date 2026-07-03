"""
LumineX 2026-07-03 패치 스크립트 #2
preset_builders/ 에 저장 후 C:\Dev\LumineX 에서 실행

처리 내용:
1. QUAD 4인 신규 — HOF 3종 + SSS 3종 + SS 2종 (총 8종)
2. QUINT 5인 신규 — HOF 3종 + SSS 3종 + SS 1종 (총 7종)
3. HEXA 6인 신규 — HOF 1종 + SSS 1종 (총 2종)
4. OCTET 8인 신규 — SSS 1종 (총 1종)
5. 신규 컨셉 대기 4종 — SSS 예정 (trio_inside_outside 등)
6. HOF_TIER에 신규 7종 추가
7. PRESET_CATEGORIES 멀티바디페인팅에 전체 추가
"""

from pathlib import Path
import re

DASHBOARD = Path("dashboard.py")

# ── 신규 HOF 7종 ─────────────────────────────────────────
NEW_HOF = [
    "quad_four_ages_bodypaint",
    "quad_four_classical_elements_klimt",
    "quad_four_seasons_night_bodypaint",
    "quint_five_senses_bodypaint",
    "quint_five_worlds_bodypaint",
    "quint_five_elements_wuxing_bodypaint",
    "hexa_rainbow_spectrum_bodypaint",
]

# ── 신규 SSS 9종 ─────────────────────────────────────────
NEW_SSS = [
    # QUAD SSS
    "quad_four_civilizations_bodypaint",
    "quad_four_gemstones_bodypaint",
    "quad_cmyk_bodypaint",
    "quad_four_metals_bodypaint",
    # QUINT SSS
    "quint_five_mythologies_bodypaint",
    "quint_five_oceans_deep_bodypaint",
    "quint_five_sacred_colors_bodypaint",
    # HEXA SSS
    "hexa_six_chakras_bodypaint",
    # OCTET SSS
    "octet_planets_solar_bodypaint",
]

# ── 신규 SS 전용 3종 ──────────────────────────────────────
NEW_SS_ONLY = [
    "quad_four_goddesses_bodypaint",
    "quad_lunar_phases_bodypaint",
    "quint_five_dance_cultures_bodypaint",
]

# ── 검증 대기 신규 컨셉 4종 (SSS 예정) ───────────────────
NEW_CONCEPT_SSS = [
    "trio_inside_outside_bodypaint",
    "quad_four_horsewomen_apocalypse",
    "trio_human_evolution_bodypaint",
    "quad_fashion_capitals_bodypaint",
]

# ── PRESET_CATEGORIES 멀티바디페인팅에 추가할 전체 목록 ──
NEW_PRESETS_CATEGORY = (
    NEW_HOF + NEW_SSS + NEW_SS_ONLY + NEW_CONCEPT_SSS
)


def read():
    return DASHBOARD.read_text(encoding="utf-8")


def write(content):
    DASHBOARD.write_text(content, encoding="utf-8")


def add_to_hof_tier(content):
    """HOF_TIER set에 신규 7종 추가"""
    anchor = '    "trio_fog_rain_snow_bodypaint",       # 색감+통일감 압도적 안개/물/눈 완벽표현'

    new_block = """    # 2026-07-03 신규 HOF — QUAD/QUINT/HEXA 검증 완료
    "quad_four_ages_bodypaint",               # 금/은/동/철 그라데이션 배경 완벽
    "quad_four_classical_elements_klimt",     # 클림트 금빛홀+4원소 완벽 융합
    "quad_four_seasons_night_bodypaint",      # 4계절 배경 분할+야간 여신 압도적
    "quint_five_senses_bodypaint",            # 5감 바로크홀 5인 세로 완벽
    "quint_five_worlds_bodypaint",            # 5세계 배경분할+여신 역대급
    "quint_five_elements_wuxing_bodypaint",   # 오행+자금성 황금시간 최고
    "hexa_rainbow_spectrum_bodypaint",        # 6인 무지개 세로4:5 HOF급"""

    if anchor in content:
        content = content.replace(
            anchor,
            anchor + "\n" + new_block
        )
    return content


def add_to_sss_tier(content):
    """SSS_TIER에 신규 추가"""
    anchor = "    # 2026-07-03 신규 SSS 52종 (신규 66종 검증 완료)"

    all_new = NEW_HOF + NEW_SSS + NEW_CONCEPT_SSS

    new_block = "    # 2026-07-03 신규 QUAD/QUINT/HEXA/OCTET + 컨셉 SSS\n"
    for p in all_new:
        new_block += f'    "{p}",\n'
    new_block += "\n"

    if anchor in content:
        content = content.replace(anchor, new_block + "    " + anchor)
    else:
        content = content.replace(
            "SSS_TIER = {\n",
            "SSS_TIER = {\n" + new_block
        )
    return content


def add_to_ss_tier(content):
    """SS_TIER에 신규 추가 (SSS + SS전용 모두)"""
    anchor = "    # 2026-07-03 신규 SS 62종 반영 (SSS 52 + SS전용 10)"

    all_new = NEW_HOF + NEW_SSS + NEW_SS_ONLY + NEW_CONCEPT_SSS

    new_block = "    # 2026-07-03 신규 QUAD/QUINT/HEXA/OCTET SS 전체\n"
    for p in all_new:
        new_block += f'    "{p}",\n'
    new_block += "\n"

    if anchor in content:
        content = content.replace(anchor, new_block + "    " + anchor)
    else:
        content = content.replace(
            "SS_TIER = {\n",
            "SS_TIER = {\n" + new_block
        )
    return content


def add_to_preset_categories(content):
    """PRESET_CATEGORIES 멀티바디페인팅 섹션에 추가"""
    # QUAD 섹션 앵커 (기존 QUAD 목록 바로 앞)
    anchor = '        # 4인 QUAD (5종)'

    new_block = """        # 2026-07-03 신규 QUAD 8종
        "quad_four_civilizations_bodypaint",
        "quad_four_goddesses_bodypaint",
        "quad_four_ages_bodypaint",
        "quad_four_metals_bodypaint",
        "quad_four_gemstones_bodypaint",
        "quad_cmyk_bodypaint",
        "quad_four_classical_elements_klimt",
        "quad_four_seasons_night_bodypaint",
        # 2026-07-03 신규 QUINT 7종
        "quint_five_senses_bodypaint",
        "quint_five_worlds_bodypaint",
        "quint_five_elements_wuxing_bodypaint",
        "quint_five_mythologies_bodypaint",
        "quint_five_oceans_deep_bodypaint",
        "quint_five_sacred_colors_bodypaint",
        "quint_five_dance_cultures_bodypaint",
        # 2026-07-03 신규 HEXA 2종
        "hexa_rainbow_spectrum_bodypaint",
        "hexa_six_chakras_bodypaint",
        # 2026-07-03 신규 OCTET 1종
        "octet_planets_solar_bodypaint",
        # 2026-07-03 신규 컨셉 4종
        "trio_inside_outside_bodypaint",
        "quad_four_horsewomen_apocalypse",
        "trio_human_evolution_bodypaint",
        "quad_fashion_capitals_bodypaint",
"""

    if anchor in content:
        content = content.replace(anchor, new_block + "        " + anchor)
    return content


def create_preset_jsons():
    """presets/ 폴더에 JSON 파일 생성"""
    presets_dir = Path("presets")

    preset_data = {
        # QUAD HOF
        "quad_four_civilizations_bodypaint": {
            "subject": "four women in a museum",
            "body": "quad group bodypaint",
            "outfit": "Four civilizations — Egyptian gold hieroglyphics, Roman marble white, Chinese red dragon, Mayan jade green",
            "environment": "grand museum hall with ancient artifacts and display cases",
            "lighting": "dramatic museum warm lighting",
            "style": "Vogue Italia high-fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quad_four_goddesses_bodypaint": {
            "subject": "four women in ancient ruins",
            "body": "quad group bodypaint",
            "outfit": "Four goddesses — Aphrodite rose gold, Isis midnight blue gold, Kali deep indigo crimson, Ishtar lapis lazuli",
            "environment": "ancient ruined temple columns at golden sunset",
            "lighting": "golden hour dramatic lighting",
            "style": "Vogue Italia high-fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quad_four_ages_bodypaint": {
            "subject": "four women in dramatic studio",
            "body": "quad group bodypaint",
            "outfit": "Four ages — Golden Age pure gold sun patterns, Silver Age cool silver moon phases, Bronze Age warm copper warrior, Iron Age dark charcoal industrial",
            "environment": "gradient studio background warm gold to cold iron",
            "lighting": "split dramatic lighting warm to cool",
            "style": "Vogue Italia high-fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quad_four_metals_bodypaint": {
            "subject": "four women in a forge workshop",
            "body": "quad group bodypaint",
            "outfit": "Four metals — Gold lustrous crown sun motifs, Silver cool filigree moonlight, Copper warm reddish verdigris circuit, Iron dark gunmetal chain rivets",
            "environment": "dramatic forge and metallurgy workshop with glowing furnaces",
            "lighting": "orange furnace glow fading to cool steel blue",
            "style": "industrial fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quad_four_gemstones_bodypaint": {
            "subject": "four women in jewelry gallery",
            "body": "quad group bodypaint",
            "outfit": "Four gemstones — Ruby deep crimson faceted patterns, Emerald forest green hexagonal lattice, Sapphire royal blue star patterns, Diamond pure white prismatic rainbow",
            "environment": "luxury jewelry gallery with crystal displays",
            "lighting": "prismatic studio lighting",
            "style": "luxury fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quad_cmyk_bodypaint": {
            "subject": "four women in print studio",
            "body": "quad group bodypaint",
            "outfit": "CMYK — Cyan geometric halftone dots, Magenta flowing organic ink splash, Yellow angular sunburst patterns, Key Black matte fine line minimal",
            "environment": "sleek modern print studio white gallery space",
            "lighting": "high key even studio lighting",
            "style": "graphic design fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quad_four_classical_elements_klimt": {
            "subject": "four women in Viennese art nouveau gallery",
            "body": "quad group bodypaint",
            "outfit": "Klimt four elements — Fire crimson gold spiral Byzantine, Water deep teal gold wave serpentine, Earth brown gold tree of life botanical, Air silver white gold feather wind",
            "environment": "grand Viennese art nouveau gallery with gold mosaic walls",
            "lighting": "warm chandelier lighting",
            "style": "Gustav Klimt art nouveau fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quad_four_seasons_night_bodypaint": {
            "subject": "four women in panoramic night scene",
            "body": "quad group bodypaint",
            "outfit": "Four seasons night — Spring pink cherry blossom jade, Summer emerald firefly bioluminescent, Autumn amber maple harvest moon, Winter ice blue snowflake aurora",
            "environment": "background transitions spring blossoms to summer jungle to autumn forest to winter snowfield with full moon",
            "lighting": "dramatic night sky moonlight",
            "style": "fantasy fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quad_four_horsewomen_apocalypse": {
            "subject": "four women in apocalyptic landscape",
            "body": "quad group bodypaint",
            "outfit": "Four Horsewomen — Conquest gleaming white crown eagle, War blood crimson armor flames, Famine obsidian black scales drought, Death pale grey-green skull hourglass",
            "environment": "apocalyptic burning city ruins dark stormy sky lightning",
            "lighting": "dramatic cinematic rim lighting from behind",
            "style": "dark cinematic fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        # QUINT HOF
        "quint_five_senses_bodypaint": {
            "subject": "five women in baroque hall",
            "body": "quint group bodypaint",
            "outfit": "Five senses — Sight silver violet eye peacock, Hearing deep blue cyan sound wave musical, Smell rose gold green floral jasmine, Taste amber crimson honeycomb fruit, Touch skin gold copper fingerprint nerve",
            "environment": "grand baroque hall with ornate gilded ceiling and chandeliers",
            "lighting": "dramatic chandelier lighting",
            "style": "Vogue Italia high-fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quint_five_worlds_bodypaint": {
            "subject": "five women in composite world backdrop",
            "body": "quint group bodypaint",
            "outfit": "Five worlds — Celestial sky blue white cloud lightning birds, Earth forest green brown tree roots mountains, Underworld obsidian black burning orange lava bone, Ocean abyssal blue teal bioluminescent coral, Cosmos deep space black gold galaxy nebula constellation",
            "environment": "composite backdrop showing sky earth underground ocean cosmos simultaneously",
            "lighting": "cinematic split lighting per zone",
            "style": "fantasy epic fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quint_five_elements_wuxing_bodypaint": {
            "subject": "five women in Forbidden City courtyard",
            "body": "quint group bodypaint",
            "outfit": "Wuxing five elements — Wood deep forest green bamboo dragon, Fire brilliant crimson gold phoenix calligraphy, Earth warm ochre terracotta shanshui landscape, Metal gleaming gold white imperial dragon coins, Water deep indigo black koi river calligraphy mist",
            "environment": "traditional Chinese imperial palace Forbidden City courtyard at golden hour",
            "lighting": "golden hour dramatic lighting",
            "style": "Chinese imperial fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quint_five_mythologies_bodypaint": {
            "subject": "five women before composite temple backdrop",
            "body": "quint group bodypaint",
            "outfit": "Five mythologies — Greek white marble gold laurel lightning, Egyptian gold lapis hieroglyphics Ra lotus scarab, Norse grey-blue silver runes Yggdrasil Mjolnir, Hindu saffron gold lotus mandala chakra Om peacock, East Asian red imperial gold dragon phoenix yin-yang",
            "environment": "composite ancient temple backdrop from five civilizations",
            "lighting": "golden hour dramatic lighting",
            "style": "mythological fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quint_five_oceans_deep_bodypaint": {
            "subject": "five women in aquarium research facility",
            "body": "quint group bodypaint",
            "outfit": "Five oceans — Arctic ice white pale blue polar bear narwhal iceberg aurora, Atlantic deep navy whale Gulf Stream sailing ship, Pacific deep teal giant wave tropical fish volcanic island, Indian warm cerulean coral monsoon sea turtle spice route, Southern grey-blue white penguin stormy wave albatross",
            "environment": "massive circular aquarium research facility floor-to-ceiling ocean windows",
            "lighting": "dramatic blue underwater lighting",
            "style": "scientific fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quint_five_sacred_colors_bodypaint": {
            "subject": "five women in sacred composite space",
            "body": "quint group bodypaint",
            "outfit": "Five sacred colors — Tibetan saffron orange mandala Dharma lotus Om, Native American turquoise eagle feather tribal spirit animal, Hindu vermilion red peacock mehndi lotus Rangoli, Egyptian lapis lazuli Eye of Horus cartouche sacred geometry, Celtic forest emerald green knotwork triskelion tree of life runes",
            "environment": "sacred ceremonial composite space from five world traditions",
            "lighting": "mystical golden lighting",
            "style": "spiritual fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quint_five_dance_cultures_bodypaint": {
            "subject": "five women on world stage",
            "body": "quint group bodypaint",
            "outfit": "Five dances — Flamenco crimson black rose Spanish tile, Samba tropical green gold carnival feather Brazilian, Ballet pure white silver pointe ribbon tutu, Hip Hop urban grey neon yellow graffiti street art, Korean traditional white jade green Joseon sleeve lotus crane",
            "environment": "grand performance stage with world dance cultural backdrop",
            "lighting": "dramatic spotlight lighting",
            "style": "performance fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        # HEXA
        "hexa_rainbow_spectrum_bodypaint": {
            "subject": "six women in white gallery",
            "body": "hexa group bodypaint",
            "outfit": "Rainbow spectrum — Red pure geometric fire, Orange citrus flame organic, Yellow sunflower honeycomb starburst, Green botanical leaf mandala, Blue ocean wave crystal, Violet cosmic nebula galaxy",
            "environment": "large white minimalist gallery seamless backdrop",
            "lighting": "perfect even studio lighting",
            "style": "minimalist art fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "hexa_six_chakras_bodypaint": {
            "subject": "six women in Balinese temple garden",
            "body": "hexa group bodypaint",
            "outfit": "Six chakras — Root crimson red square earth lotus, Sacral orange crescent moon water lotus, Solar Plexus golden yellow fire triangle sun wheel, Heart emerald green star lotus compassion, Throat sky blue sound wave mantra calligraphy, Third Eye deep indigo all-seeing eye sacred geometry Om",
            "environment": "sacred Balinese temple garden with lotus pond and ancient stone architecture",
            "lighting": "mystical golden light",
            "style": "spiritual fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        # OCTET
        "octet_planets_solar_bodypaint": {
            "subject": "eight women in planetarium",
            "body": "octet group bodypaint",
            "outfit": "Eight planets — Mercury dark grey craters, Venus yellow sulfuric clouds, Earth blue green continents clouds, Mars rusty red Olympus Mons dust storms, Jupiter orange brown gas bands Great Red Spot, Saturn golden amber ring belt, Uranus pale ice blue-green methane, Neptune deep cobalt Great Dark Spot wind streaks",
            "environment": "vast dark planetarium with galaxy projection dome ceiling deep space Milky Way backdrop",
            "lighting": "dramatic space lighting",
            "style": "cosmic science fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        # 신규 컨셉
        "trio_inside_outside_bodypaint": {
            "subject": "three women in medical science museum",
            "body": "trio group bodypaint",
            "outfit": "Three body layers — Skin porcelain white fingerprint capillary dermatological patterns, Muscle deep crimson burgundy anatomical muscle groups Leonardo da Vinci study, Skeleton pure white bones on black X-ray negative ribcage spine skull",
            "environment": "dramatic medical science museum with anatomical displays glass cases",
            "lighting": "cool clinical blue-white lighting",
            "style": "scientific art fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "trio_human_evolution_bodypaint": {
            "subject": "three women in panoramic evolution backdrop",
            "body": "trio group bodypaint",
            "outfit": "Human evolution — Primal earth brown ochre cave painting handprints mammoth bison tribal dots, Modern Human natural skin sacred geometry DNA helix neural network circuit hybrid, Posthuman Cyborg chrome silver electric blue circuit board mechanical joints binary data streams",
            "environment": "background transitions dense jungle to modern city to neon cyberpunk megacity",
            "lighting": "dramatic cinematic lighting",
            "style": "sci-fi fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
        "quad_fashion_capitals_bodypaint": {
            "subject": "four women on composite runway stage",
            "body": "quad group bodypaint",
            "outfit": "Fashion capitals — Paris ivory gold Eiffel Tower lace filigree Art Nouveau, Milan deep black gold Duomo Gothic Renaissance Versace baroque, New York urban grey blue Manhattan skyline graffiti subway grid, Tokyo white neon red Torii gate sakura circuit manga kanji",
            "environment": "composite runway backdrop showing all four cities simultaneously",
            "lighting": "high fashion editorial rim lighting",
            "style": "global fashion editorial",
            "quality": "ultra-sharp 8K professional photography"
        },
    }

    created = 0
    skipped = 0
    for name, data in preset_data.items():
        path = presets_dir / f"{name}.json"
        if path.exists():
            print(f"  ⚠️  스킵 (이미 존재): {name}.json")
            skipped += 1
        else:
            import json
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  ✅ 생성: {name}.json")
            created += 1

    return created, skipped


def main():
    print("=" * 60)
    print("LumineX 2026-07-03 패치 #2 — QUAD/QUINT/HEXA/OCTET")
    print("=" * 60)

    # 1. JSON 파일 생성
    print("\n📁 JSON 파일 생성")
    created, skipped = create_preset_jsons()
    print(f"  생성: {created}개 / 스킵: {skipped}개")

    # 2. dashboard.py 로드
    content = read()
    print(f"\n✅ dashboard.py 로드 ({len(content):,} chars)")

    # 3. PRESET_CATEGORIES 추가
    print("\n📂 PRESET_CATEGORIES 멀티바디페인팅 추가")
    before = len(content)
    content = add_to_preset_categories(content)
    print(f"  ✅ {len(NEW_PRESETS_CATEGORY)}종 추가")

    # 4. HOF_TIER 추가
    print("\n👑 HOF_TIER 신규 7종 추가")
    content = add_to_hof_tier(content)
    print("  ✅ 완료")

    # 5. SSS_TIER 추가
    all_sss = NEW_HOF + NEW_SSS + NEW_CONCEPT_SSS
    print(f"\n🌟 SSS_TIER {len(all_sss)}종 추가")
    content = add_to_sss_tier(content)
    print("  ✅ 완료")

    # 6. SS_TIER 추가
    all_ss = NEW_HOF + NEW_SSS + NEW_SS_ONLY + NEW_CONCEPT_SSS
    print(f"\n⭐ SS_TIER {len(all_ss)}종 추가")
    content = add_to_ss_tier(content)
    print("  ✅ 완료")

    # 7. 저장
    write(content)
    print("\n✅ dashboard.py 저장 완료")

    # 8. 검증
    print("\n📊 검증")
    final = DASHBOARD.read_text(encoding="utf-8")

    # HOF 검증
    hof_check = [
        "quad_four_ages_bodypaint",
        "hexa_rainbow_spectrum_bodypaint",
        "quint_five_worlds_bodypaint",
    ]
    for p in hof_check:
        count = final.count(f'"{p}"')
        print(f"  HOF {p}: {'✅' if count > 0 else '❌'} ({count}회)")

    # SSS 검증
    sss_check = [
        "octet_planets_solar_bodypaint",
        "quad_four_civilizations_bodypaint",
        "hexa_six_chakras_bodypaint",
    ]
    for p in sss_check:
        count = final.count(f'"{p}"')
        print(f"  SSS {p}: {'✅' if count > 0 else '❌'} ({count}회)")

    # HOF_TIER 총 카운트
    hof_lines = [l for l in final.split('\n')
                 if '"' in l and 'HOF_TIER' not in l
                 and l.strip().startswith('"')
                 and 'HOF_TIER = {' not in l]
    print(f"\n  총 HOF_TIER 항목: 확인은 streamlit 실행 후 사이드바에서")

    # presets/ 파일 수
    presets_count = len(list(Path("presets").glob("*.json")))
    print(f"  총 presets JSON: {presets_count}개")

    print("\n" + "=" * 60)
    print("패치 완료!")
    print("git add -A")
    print('git commit -m "2026-07-03 QUAD/QUINT/HEXA/OCTET 신규 프리셋 + HOF 확장"')
    print("git push")
    print("=" * 60)


if __name__ == "__main__":
    main()
