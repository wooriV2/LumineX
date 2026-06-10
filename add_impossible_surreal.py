"""
add_impossible_surreal.py
==========================
🌌 불가능 & 초현실 카테고리 신설 — 27종 프리셋
개방형 설계: outfit/material 비워둠 → 배경이 의상 분위기 자동 결정
수동 조합에서 의상/소재 오버라이드 가능

실행: python add_impossible_surreal.py
"""

import json
import re
from pathlib import Path

PRESETS_DIR = Path("presets")
DASHBOARD = Path("dashboard.py")

# ── 27종 프리셋 정의 ───────────────────────────────────────
PRESETS = {
    "storm_eye_editorial": {
        "tag": "Storm Eye Editorial",
        "subject": "a goddess-like woman standing in absolute stillness",
        "body": "commanding serene figure, hair and clothing perfectly still, full body shot",
        "outfit": "",
        "material": "",
        "environment": "perfect eye of a hurricane, circle of calm around her, violent storm walls of rain and lightning raging in every direction, destroyed landscape beyond, apocalyptic sky, debris orbiting at high speed",
        "lighting": "ethereal soft light within the eye, violent lightning illuminating the storm walls, dramatic contrast between calm and chaos",
        "style": "supernatural fashion editorial, forces-of-nature luxury photography, impossible calm",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "living_fabric": {
        "tag": "Living Fabric",
        "subject": "a serene powerful woman wearing a gown that appears to be alive",
        "body": "statuesque elegant figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "minimalist black studio, fabric tendrils filling the entire frame, organic movement everywhere",
        "lighting": "single dramatic spotlight, iridescent fabric catching prismatic light",
        "style": "living couture editorial, impossible fashion photography, Alexander McQueen supernatural aesthetic",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "macro_goddess": {
        "tag": "Macro Goddess",
        "subject": "an impossibly tall glamorous woman striding through a city skyline",
        "body": "goddess-scale towering figure, legs as tall as skyscrapers, full body shot",
        "outfit": "",
        "material": "",
        "environment": "nighttime megalopolis far below her feet, neon city grid, tiny cars and buildings at her feet, storm clouds at her shoulders level",
        "lighting": "city glow from below, lightning at her eye level, scale-defying drama",
        "style": "surrealist fashion editorial, scale-defying luxury photography, goddess of the city",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "time_freeze_editorial": {
        "tag": "Time Freeze Editorial",
        "subject": "a breathtaking female model standing perfectly still in absolute chaos",
        "body": "calm untouched figure amidst explosion, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dramatic dark studio, thousands of suspended glass shards frozen mid-air, water droplets suspended like diamonds, debris exploding outward in all directions",
        "lighting": "multiple strobes creating prismatic light through frozen glass shards, explosive light rays",
        "style": "impossible physics fashion editorial, bullet-time fashion photography, Vogue cinematic",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "gravity_defiance": {
        "tag": "Gravity Defiance",
        "subject": "a powerful woman standing firmly on the ground",
        "body": "grounded commanding figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "all surrounding objects floating upward — furniture, debris, water, flowers all rising into the sky, only the model remains earthbound, dramatic sky above",
        "lighting": "dramatic upward light as objects float away, ethereal anti-gravity atmosphere",
        "style": "anti-gravity surrealist editorial, impossible physics luxury photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "magnetic_field_goddess": {
        "tag": "Magnetic Field Goddess",
        "subject": "a powerful magnetic goddess woman",
        "body": "commanding center figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "hundreds of metal objects — coins, needles, chains, shards — all frozen mid-air flying toward the model from all directions, visible magnetic field lines in the air",
        "lighting": "dramatic center spotlight, metallic objects catching light from all angles",
        "style": "magnetic force surrealist editorial, impossible attraction luxury photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "micro_world": {
        "tag": "Micro World",
        "subject": "a tiny finger-sized glamorous woman",
        "body": "perfect miniature figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "standing on a single rose petal, surrounded by giant dewdrops like glass spheres, enormous flower stamens like columns, macro photography world",
        "lighting": "soft natural macro light, dewdrops refracting rainbow light, magical garden glow",
        "style": "macro world surrealist editorial, miniature luxury fashion photography, fantastical scale",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "mirror_shatter_dress": {
        "tag": "Mirror Shatter Dress",
        "subject": "a stunning woman wearing a dress made of thousands of mirror fragments",
        "body": "elegant commanding figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dark void studio, each mirror fragment reflecting a different scene or dimension, cascading reflections in all directions",
        "lighting": "multiple light sources creating infinite reflections, prismatic light explosion from mirror dress",
        "style": "mirror dimension surrealist editorial, multidimensional luxury fashion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "dissolution": {
        "tag": "Dissolution",
        "subject": "a breathtaking woman dissolving at the edges into particles",
        "body": "solid center figure dissolving outward into golden dust and particles, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dark minimalist void, particles and dust streaming away from her edges like smoke, dramatic dispersion effect",
        "lighting": "backlit golden light making particles glow, dramatic silhouette with dissolving edges",
        "style": "dissolution surrealist editorial, particle dispersion luxury photography, ephemeral beauty",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "crystallization": {
        "tag": "Crystallization",
        "subject": "a woman transforming into living crystal",
        "body": "half human half crystal figure, transformation boundary visible, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dark cave with crystal formations growing around her, the crystal transformation spreading from her feet upward",
        "lighting": "light refracting through growing crystal formations, prismatic rainbow light, dramatic transformation glow",
        "style": "crystallization surrealist editorial, mineral transformation luxury photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "giant_flora": {
        "tag": "Giant Flora",
        "subject": "a normal-sized elegant woman dwarfed by impossible giant flowers",
        "body": "small graceful figure among giants, full body shot",
        "outfit": "",
        "material": "",
        "environment": "forest of impossibly giant flowers — roses the size of houses, petals like sails, stamens like golden towers, soft magical light filtering through giant petals",
        "lighting": "soft filtered light through giant petals, golden hour magical glow, scale-defying wonder",
        "style": "giant flora surrealist editorial, botanical scale luxury photography, fairy tale fashion",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "supernova_burst": {
        "tag": "Supernova Burst",
        "subject": "a cosmic goddess woman at the center of a stellar explosion",
        "body": "radiant epicenter figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "explosive burst of light and energy radiating outward from her body in all directions, cosmic scale explosion, nebula colors erupting, star matter flying outward",
        "lighting": "blinding white center light, cosmic color explosion — deep purple, gold, electric blue radiating outward",
        "style": "supernova surrealist editorial, cosmic explosion luxury photography, stellar goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "portal_threshold": {
        "tag": "Portal Threshold",
        "subject": "a mysterious woman standing half-through a glowing dimensional portal",
        "body": "figure bisected by portal boundary, one half in each world, full body shot",
        "outfit": "",
        "material": "",
        "environment": "luminous circular portal showing two completely different worlds — one side dark gothic the other side bright ethereal, portal edge crackling with energy",
        "lighting": "portal glow illuminating both sides differently, dramatic dimensional boundary light",
        "style": "dimensional portal surrealist editorial, two-world luxury photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "escher_staircase": {
        "tag": "Escher Staircase",
        "subject": "an elegant woman on an impossible Escher-like staircase",
        "body": "poised graceful figure navigating impossible architecture, full body shot",
        "outfit": "",
        "material": "",
        "environment": "physically impossible staircase structure — stairs going in all directions simultaneously, gravity working differently in each section, infinite looping architecture",
        "lighting": "dramatic architectural lighting emphasizing impossible geometry, multiple shadow directions",
        "style": "impossible architecture surrealist editorial, Escher luxury fashion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "aurora_embodied": {
        "tag": "Aurora Embodied",
        "subject": "a ethereal woman wearing the northern lights as a living gown",
        "body": "luminous ethereal figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "arctic night sky, aurora borealis descending and wrapping around her body like a living dress, vast starfield above, frozen tundra below",
        "lighting": "aurora light in greens purples and blues emanating from her gown, starlight, magical arctic glow",
        "style": "aurora embodied surrealist editorial, living light luxury photography, arctic goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "nebula_goddess": {
        "tag": "Nebula Goddess",
        "subject": "a cosmic goddess woman at the scale of a nebula",
        "body": "universe-scale divine figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "floating in deep space surrounded by a vast colorful nebula, galaxies and star clusters visible behind her, cosmic dust and gas clouds forming around her silhouette",
        "lighting": "nebula light in deep purples pinks and golds, distant starlight, cosmic scale illumination",
        "style": "cosmic nebula surrealist editorial, universe-scale luxury photography, space goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "shadow_independent": {
        "tag": "Shadow Independent",
        "subject": "a poised elegant woman whose shadow has a completely different life",
        "body": "still controlled figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "minimalist white gallery space, her shadow on the wall behind her striking a completely different dramatic pose, shadow moving independently with its own personality",
        "lighting": "single strong directional spotlight casting one impossible independent shadow, stark white surroundings",
        "style": "shadow surrealist editorial, Magritte impossible reality luxury photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "negative_space": {
        "tag": "Negative Space",
        "subject": "a woman whose body silhouette is a window into the cosmos",
        "body": "outline present but body is cosmic void, only face visible, full body shot",
        "outfit": "",
        "material": "",
        "environment": "stark white minimalist studio, her body silhouette is a perfect void revealing deep space within — galaxies nebulae and stars visible through the shape of her",
        "lighting": "soft even white light on surroundings, cosmos glowing from within the void silhouette",
        "style": "negative space surrealist editorial, cosmic void luxury photography, impossible body",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "flame_dress": {
        "tag": "Flame Dress",
        "subject": "a fearless powerful woman wearing a gown made entirely of living fire",
        "body": "fearless untouched figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dark dramatic void, real flames sculpted into haute couture ball gown shape, burning blue and white at the bodice transitioning to deep orange and red at the hem",
        "lighting": "fire light from the dress itself illuminating everything, deep dramatic shadows beyond",
        "style": "fire couture surrealist editorial, living flame luxury photography, elemental goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "reflection_rebel": {
        "tag": "Reflection Rebel",
        "subject": "a composed woman whose mirror reflection does something completely different",
        "body": "still controlled figure facing mirror, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dramatic dark room with a large ornate mirror, the reflection showing a completely different pose, expression and action — as if the reflection has its own free will",
        "lighting": "dramatic side lighting, mirror creating its own independent light source",
        "style": "reflection surrealist editorial, impossible mirror luxury photography, dual reality",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "time_lapse_body": {
        "tag": "Time Lapse Body",
        "subject": "a woman existing simultaneously across multiple time periods",
        "body": "multiple overlapping translucent versions of the same figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dramatic dark studio, three or four ghost-like versions of the same woman overlapping — each in a different era, different styling, different pose, all occupying same space",
        "lighting": "each time layer lit differently, dramatic temporal overlap effect",
        "style": "time collapse surrealist editorial, temporal overlay luxury photography, multiple selves",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "invisible_outline": {
        "tag": "Invisible Outline",
        "subject": "a woman who is completely invisible except for her floating clothing",
        "body": "absent invisible body, clothes floating in human shape, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dramatic dark studio, an entire couture outfit floating in perfect human form with nothing inside — dress shoes accessories all suspended as if worn by an invisible person",
        "lighting": "dramatic spotlight on the floating clothes, shadows cast as if someone is wearing them",
        "style": "invisible body surrealist editorial, floating clothes luxury photography, absence as presence",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "waterfall_gown": {
        "tag": "Waterfall Gown",
        "subject": "a goddess woman wearing a gown made of a living waterfall",
        "body": "powerful serene figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dramatic cliff edge, actual waterfall water flowing and sculpted into the shape of a couture gown around her body, water cascading from hem to ground",
        "lighting": "natural dramatic light through waterfall mist, rainbow in the spray, golden hour glow",
        "style": "waterfall couture surrealist editorial, living water luxury photography, elemental goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "cloud_couture": {
        "tag": "Cloud Couture",
        "subject": "a celestial woman wearing actual clouds sculpted into haute couture",
        "body": "ethereal divine figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "high altitude above the clouds, sunset sky in deep oranges and purples, clouds gathering and sculpting themselves around her into a dramatic ball gown silhouette",
        "lighting": "golden sunset light through cloud gown, god rays, heavenly illumination",
        "style": "cloud couture surrealist editorial, sky goddess luxury photography, celestial fashion",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "weather_maker": {
        "tag": "Weather Maker",
        "subject": "a powerful weather goddess controlling the elements",
        "body": "commanding figure mid-gesture, full body shot",
        "outfit": "",
        "material": "",
        "environment": "panoramic sky view, one hand raised causing lightning to strike, other hand lowering causing rain to stop, sun breaking through clouds on one side while storm rages on other",
        "lighting": "split dramatic lighting — golden sun on one side, electric storm light on the other",
        "style": "weather control surrealist editorial, elemental power luxury photography, climate goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "gravity_well": {
        "tag": "Gravity Well",
        "subject": "a cosmic woman creating a visible gravity well around herself",
        "body": "powerful centered figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "dark space-like void, visible light bending around her like a black hole effect, stars and light rays curving toward her, spacetime fabric visibly warping",
        "lighting": "light bending and distorting around her body, gravitational lensing effect, cosmic darkness",
        "style": "gravity well surrealist editorial, spacetime luxury photography, black hole goddess",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
    "double_exposure_self": {
        "tag": "Double Exposure Self",
        "subject": "a woman as a double exposure of two completely different worlds",
        "body": "dual-world translucent figure, full body shot",
        "outfit": "",
        "material": "",
        "environment": "two realities occupying the same space — half the frame is a dark city at night, the other half is a wild tropical forest, the model exists as a double exposure bridge between both worlds",
        "lighting": "dual lighting from each world — neon city light and natural tropical light simultaneously",
        "style": "double exposure surrealist editorial, dual world luxury photography, between realities",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, cinematic, realistic proportions"
    },
}

# ── 카테고리 목록 ──────────────────────────────────────────
CATEGORY_LIST = list(PRESETS.keys())

print("=" * 55)
print("add_impossible_surreal.py 시작")
print(f"총 {len(PRESETS)}종 프리셋 생성")
print("=" * 55)

# ── 1. JSON 파일 생성 ──────────────────────────────────────
created = []
skipped = []
for name, data in PRESETS.items():
    path = PRESETS_DIR / f"{name}.json"
    if path.exists():
        skipped.append(name)
    else:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        created.append(name)

print(f"\n✅ 새로 생성: {len(created)}종")
if skipped:
    print(f"⚠️  이미 존재 (스킵): {skipped}")

# ── 2. dashboard.py 카테고리 추가 ─────────────────────────
content = DASHBOARD.read_text(encoding="utf-8")

if "불가능 & 초현실" in content:
    print("\n⚠️  카테고리 이미 존재 — 스킵")
else:
    # PRESET_CATEGORIES 닫는 } 직전에 새 카테고리 삽입
    new_category = '\n    "🌌 불가능 & 초현실": [\n'
    for name in CATEGORY_LIST:
        new_category += f'        "{name}",\n'
    new_category += '    ],\n'

    # PRESET_CATEGORIES = { ... } 의 마지막 항목 뒤에 삽입
    pattern = r'(PRESET_CATEGORIES\s*=\s*\{.*?)(^\})'
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    if match:
        new_content = content[:match.end(1)] + new_category + content[match.end(1):]
        DASHBOARD.write_text(new_content, encoding="utf-8")
        print("✅ 카테고리 추가 완료: 🌌 불가능 & 초현실")
    else:
        print("❌ PRESET_CATEGORIES 패턴 매칭 실패 — 수동 추가 필요")

# ── 3. 검증 ───────────────────────────────────────────────
print("\n[ 검증 ]")
for name in CATEGORY_LIST:
    path = PRESETS_DIR / f"{name}.json"
    status = "✅" if path.exists() else "❌"
    print(f"  {status} {name}.json")

verify = DASHBOARD.read_text(encoding="utf-8")
cat_status = "✅" if "불가능 & 초현실" in verify else "❌"
print(f"\n  {cat_status} dashboard.py 카테고리 등록")

total = sum(len(v) for v in re.findall(r'"🌌 불가능 & 초현실":\s*\[([^\]]+)\]', verify))
print(f"\n완료! 커밋:")
print('  git add -A')
print('  git commit -m "feat: 🌌 불가능&초현실 카테고리 신설 (27종)"')
print('  git push')
