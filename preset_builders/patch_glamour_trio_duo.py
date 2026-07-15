# -*- coding: utf-8 -*-
"""
LumineX 신규 3개 카테고리 HOF 프리셋 패치
- 🎭 Archetype Glamour (8종 HOF)
- 👯 Duo Glamour (11종 HOF)
- 🎭 Trio Glamour (11종 HOF)
타깃: presets/ JSON 생성 + core/presets_meta.py 업데이트
실행: python preset_builders/patch_glamour_trio_duo.py
"""
import json
from pathlib import Path

PRESETS_DIR = Path("presets")
TARGET = Path("core/presets_meta.py")

# ══════════════════════════════════════════════════════════
# 프리셋 데이터
# ══════════════════════════════════════════════════════════

PRESETS = {

    # ── 🎭 Archetype Glamour ──────────────────────────────
    "bond_girl_casino": {
        "name": "Bond Girl Casino",
        "category": "🎭 Archetype Glamour",
        "background": "Monte Carlo grand casino interior, crystal chandeliers, roulette tables, crowd of tuxedos",
        "outfit": "Liquid gold micro plunge dress, neckline to navel, sides completely open, extreme thigh-high slit, gold stilettos",
        "material": "Gold metallic liquid fabric, body-hugging, sides bare",
        "lighting": "Warm gold chandelier light, shallow depth of field",
        "pose": "One leg up on roulette table, champagne glass, smoldering gaze at camera",
        "style": "Cinematic fashion editorial, Vogue glamour",
        "negative": "no conservative dress, no full coverage",
    },
    "spy_rooftop_latex": {
        "name": "Spy Rooftop Latex",
        "category": "🎭 Archetype Glamour",
        "background": "Tokyo rooftop at night, city lights below, wind in hair, urban skyline",
        "outfit": "Black latex catsuit unzipped from collar to hip bone, nothing underneath, curves fully defined, thigh holster prop",
        "material": "High-shine black latex, second-skin fit, zipper open to hip",
        "lighting": "Blue-black color grade, hard rim light, deep shadow",
        "pose": "Back arched against ventilation unit, one hand in hair, dangerous expression",
        "style": "High concept fashion editorial, Helmut Newton spy aesthetic",
        "negative": "no full zip, no conservative outfit",
    },
    "spy_hotel_noir": {
        "name": "Spy Hotel Noir",
        "category": "🎭 Archetype Glamour",
        "background": "Luxury hotel corridor, dramatic shadow geometry, single warm light source at end of hallway",
        "outfit": "Black micro dress, completely backless to base of spine, high slit to hip, walking away glancing back",
        "material": "Black matte crepe, backless, high slit",
        "lighting": "High contrast chiaroscuro, cool shadow tones, single corridor light",
        "pose": "Walking toward camera, glancing back over shoulder, stilettos on carpet",
        "style": "Cinematic noir editorial, femme fatale aesthetic",
        "negative": "no front-facing only, no conservative coverage",
    },
    "dark_queen_cliff": {
        "name": "Dark Queen Cliff",
        "category": "🎭 Archetype Glamour",
        "background": "Active volcano cliff edge at night, river of lava below, ash and embers in air",
        "outfit": "Floor-length black cape completely open at front, nothing underneath, volcanic wind lifting cape dramatically",
        "material": "Black silk cape, open front, body silhouetted against lava glow",
        "lighting": "Deep orange-red lava light, dark sky, ember particles floating",
        "pose": "Arms spread wide, face to sky, primal goddess energy, barefoot on volcanic rock",
        "style": "Apocalyptic fashion editorial, dark goddess aesthetic",
        "negative": "no closed cape, no conservative outfit",
    },
    "villain_penthouse": {
        "name": "Villain Penthouse",
        "category": "🎭 Archetype Glamour",
        "background": "Glass penthouse, midnight city skyline silhouetted, rain on windows, minimalist dark interior",
        "outfit": "Crystal-encrusted sheer organza midi dress, fully transparent, strategic crystal clusters coverage only",
        "material": "Completely sheer organza with crystal embellishment, body fully visible through fabric",
        "lighting": "Cool blue city light through rain-streaked glass, hard shadow, cinematic grade",
        "pose": "Standing at floor-to-ceiling window, silhouetted against city lights, one hand on glass",
        "style": "Dark glamour editorial, femme fatale villain aesthetic",
        "negative": "no opaque fabric, no full coverage",
    },
    "assassin_rain": {
        "name": "Assassin Rain",
        "category": "🎭 Archetype Glamour",
        "background": "Rain-soaked narrow alley, neon reflections on wet cobblestones, midnight neon signs",
        "outfit": "White oversized dress shirt soaking wet clinging to body, only top two buttons fastened, micro denim shorts, bare legs",
        "material": "White cotton shirt completely soaked, transparent when wet, micro shorts",
        "lighting": "Neon color reflections on wet surfaces, rain streaks, dramatic contrast",
        "pose": "Leaning against wet brick wall, rain pouring, wet hair plastered to face, intense gaze",
        "style": "Cinematic wet editorial fashion, urban noir",
        "negative": "no dry clothing, no conservative coverage",
    },
    "goddess_warrior": {
        "name": "Goddess Warrior",
        "category": "🎭 Archetype Glamour",
        "background": "Ancient Greek temple ruins at golden hour, marble columns, Aegean sea below, birds flying",
        "outfit": "Minimal hammered gold breastplate, bare midriff and hips fully exposed, micro draped gold fabric at hip only, gold arm cuffs",
        "material": "Hammered gold metal breastplate, minimal hip drape, sides and midriff fully bare",
        "lighting": "Warm golden hour light, marble reflection, wind lifting fabric",
        "pose": "Standing between columns, wind lifting fabric, warrior goddess posture, barefoot",
        "style": "Mythological fashion editorial, Pirelli Calendar aesthetic",
        "negative": "no full coverage, no modern clothing",
    },
    "rockstar_stage": {
        "name": "Rockstar Stage",
        "category": "🎭 Archetype Glamour",
        "background": "Stadium stage, massive crowd behind, laser lights everywhere, smoke machine haze",
        "outfit": "Black crystal tape art covering chest in X pattern only, black micro leather shorts, fishnet thigh-highs, platform boots, guitar prop",
        "material": "Crystal tape X pattern on bare chest, micro leather shorts, fishnet",
        "lighting": "Stage lighting from above, smoke machine, backlight halo, crowd energy behind",
        "pose": "Center stage, arms raised with guitar, rockstar energy, hair flying",
        "style": "Concert fashion editorial, Rolling Stone cover aesthetic",
        "negative": "no full top, no conservative stage outfit",
    },

    # ── 👯 Duo Glamour ────────────────────────────────────
    "duo_penthouse_black": {
        "name": "Duo Penthouse Black",
        "category": "👯 Duo Glamour",
        "background": "Tokyo penthouse, floor-to-ceiling windows, Skytree visible, midnight blue city glow",
        "outfit": "Model A standing: black one-shoulder bandage dress, extreme thigh-high slit. Model B seated on marble floor: black satin backless slip dress, spine fully bare, legs extended",
        "material": "Black bandage vs black satin, minimal coverage, both backless or slit",
        "lighting": "Cool blue night light, deep shadow, city light from windows",
        "pose": "Both facing camera, Model A standing power pose, Model B seated on floor looking up",
        "style": "Luxury fashion editorial, Helmut Newton duo aesthetic",
        "negative": "no conservative dresses, no full coverage",
    },
    "duo_pool_wet_night": {
        "name": "Duo Pool Wet Night",
        "category": "👯 Duo Glamour",
        "background": "Private infinity pool, Maldives, midnight, Milky Way above, overwater bungalows in distance",
        "outfit": "Model A: white micro string bikini, completely wet, water streaming. Model B: gold micro bikini, wet, leaning back on pool edge",
        "material": "White and gold micro string bikinis, both completely wet, glistening skin",
        "lighting": "Moonlight and pool light from below, rim lighting on wet skin, stars above",
        "pose": "Both emerging from pool simultaneously, wet hair, eye contact with camera",
        "style": "Sports Illustrated night edition, luxury lifestyle editorial",
        "negative": "no dry clothing, no conservative swimwear",
    },
    "duo_couture_sheer": {
        "name": "Duo Couture Sheer",
        "category": "👯 Duo Glamour",
        "background": "White gallery space, single overhead spotlight, white sculpture in background",
        "outfit": "Both models: impossible architectural couture — transparent organza structured gowns, internal wire boning framework only coverage, sheer tulle floor train, completely see-through",
        "material": "Transparent organza with 3D wire boning structure, body fully visible, sheer tulle train",
        "lighting": "Clean white hard light, precise double shadow on floor",
        "pose": "Back-to-back, hands interlinked, both in profile",
        "style": "Avant-garde fashion editorial, Iris van Herpen aesthetic",
        "negative": "no opaque fabric, no conventional clothing",
    },
    "duo_mirror_boudoir": {
        "name": "Duo Mirror Boudoir",
        "category": "👯 Duo Glamour",
        "background": "Art deco boudoir, infinite mirror room, hundreds of candles everywhere, gold and black decor",
        "outfit": "Model A: black lace bralette, micro thong, garter belt, thigh-high stockings. Model B: ivory silk micro slip, spaghetti straps, completely backless",
        "material": "Black lace lingerie vs ivory silk slip, both minimal, boudoir aesthetic",
        "lighting": "Warm candlelight, golden mirror multiplication effect, infinite reflections",
        "pose": "Facing giant ornate mirror together, infinite reflections behind them",
        "style": "Intimate fashion editorial, Pirelli Calendar boudoir aesthetic",
        "negative": "no conservative coverage, no daywear",
    },
    "duo_jungle_primal": {
        "name": "Duo Jungle Primal",
        "category": "👯 Duo Glamour",
        "background": "Dense tropical rainforest, massive waterfall behind, golden filtered light through canopy",
        "outfit": "Model A: snakeskin micro bikini, body glistening with water, damp hair. Model B: tropical vine and flower arrangement covering body minimally, wet skin",
        "material": "Snakeskin micro bikini vs tropical flowers and vines as natural cover",
        "lighting": "Warm dappled forest light, waterfall mist, lush green surround",
        "pose": "Model A standing, Model B crouching on mossy rock, both looking at camera",
        "style": "Nature goddess editorial, primal fashion",
        "negative": "no city clothing, no conservative coverage",
    },
    "duo_champagne_pour": {
        "name": "Duo Champagne Pour",
        "category": "👯 Duo Glamour",
        "background": "Grand ballroom, champagne tower behind, gold confetti raining down, crowd in background",
        "outfit": "Model A: silver micro sequin deep plunge dress, extreme high slit. Model B: gold micro sequin backless dress, pouring champagne",
        "material": "Silver and gold micro sequin dresses, both deep plunge and high slit",
        "lighting": "Warm ballroom light, confetti and sparkle everywhere, dynamic motion",
        "pose": "Model B pouring champagne over Model A's shoulder, both laughing, hair flying",
        "style": "Luxury celebration editorial, dynamic fashion",
        "negative": "no conservative dresses, no static poses",
    },
    "duo_ice_bath_noir": {
        "name": "Duo Ice Bath Noir",
        "category": "👯 Duo Glamour",
        "background": "Dark industrial studio, two glass ice baths side by side, single overhead spotlight",
        "outfit": "Both models submerged to waist in ice water, upper bodies bare and wet, ice cubes surrounding them",
        "material": "No clothing, bare upper body, ice and water as compositional element",
        "lighting": "Cold blue-white single spotlight, steam rising from breath, ice refraction",
        "pose": "Both seated in glass ice baths, upper bodies upright, intense expressions toward camera",
        "style": "Avant-garde art editorial, ice goddess concept",
        "negative": "no warm setting, no conventional clothing",
    },
    "duo_versailles_gold": {
        "name": "Duo Versailles Gold",
        "category": "👯 Duo Glamour",
        "background": "Palace of Versailles Hall of Mirrors, gold ceiling, crystal chandeliers, infinite mirror reflections",
        "outfit": "Both models: micro gold sculptural breastplate top, bare midriff, micro pleated gold skirt, thigh-high gold boots",
        "material": "Gold metal sculptural breastplate, micro gold pleated skirt, thigh-high gold boots",
        "lighting": "Warm gold chandelier light, infinite mirror multiplication",
        "pose": "Symmetrical mirrored poses, arms reaching toward each other, touching fingertips",
        "style": "Opulent baroque fashion editorial, Versailles goddess aesthetic",
        "negative": "no full gowns, no conservative coverage",
    },
    "duo_neon_cage": {
        "name": "Duo Neon Cage",
        "category": "👯 Duo Glamour",
        "background": "Underground neon dance club, laser grid, smoke machine, neon pink blue green lights",
        "outfit": "Model A: crystal body harness over bare skin, micro neon bikini bottom. Model B: holographic string bikini, UV body paint patterns glowing",
        "material": "Crystal body harness + neon micro bottom vs holographic bikini + UV paint",
        "lighting": "Neon rim lighting, laser beams crossing, smoke haze, UV reactive",
        "pose": "Both in dynamic dance poses, hair flying, electric energy",
        "style": "Cyberpunk nightlife editorial, UV fashion",
        "negative": "no conservative clothing, no static poses",
    },

    # ── 🎭 Trio Glamour ───────────────────────────────────
    "trio_glacier_emergence": {
        "name": "Trio Glacier Emergence",
        "category": "🎭 Trio Glamour",
        "background": "Icelandic glacier cave interior, deep blue ice walls and tunnel, electric blue glowing crevasses",
        "outfit": "Front model: white latex micro dress, ice crystals on skin. Middle model: silver sheer bodysuit. Back model: barely visible silhouette in blue glow, minimal",
        "material": "White latex, silver sheer, blue-lit silhouette — three depth levels",
        "lighting": "Ice refraction blue-white light, breath visible, blue-white cold palette",
        "pose": "Three models at different depths in ice tunnel, front closest to camera, back in glow",
        "style": "Dramatic nature editorial, ice goddess fashion",
        "negative": "no warm setting, no conservative outfits",
    },
    "trio_colosseum_dawn": {
        "name": "Trio Colosseum Dawn",
        "category": "🎭 Trio Glamour",
        "background": "Rome Colosseum interior at golden dawn, ancient arches, sand floor, birds flying in golden sky",
        "outfit": "Ground level center: gold gladiator micro armor, barefoot on sand. Mid-tier left: crimson silk one-shoulder draped, stone steps. Upper arch right: black sheer flowing gown, silhouetted against sunrise",
        "material": "Gold micro armor vs crimson silk vs black sheer — three distinct levels",
        "lighting": "Warm amber dawn light, dramatic long shadows, birds silhouetted",
        "pose": "Three models at different arena levels — ground, mid-tier steps, upper arch",
        "style": "Epic fashion editorial, Roman goddess aesthetic",
        "negative": "no modern setting, no conservative coverage",
    },
    "trio_tokyo_shibuya_rain": {
        "name": "Trio Tokyo Shibuya Rain",
        "category": "🎭 Trio Glamour",
        "background": "Shibuya crossing at midnight in heavy rain, neon reflections on flooded street, thousands of umbrellas in crowd",
        "outfit": "Left: white wet shirt open, micro shorts, soaked. Center: black latex micro dress, rain streaming. Right: neon pink wet bodysuit, arms raised",
        "material": "Wet white cotton vs black latex vs neon pink bodysuit — three color contrast",
        "lighting": "Neon exploding behind, rain streaks, wet pavement reflections, crowd umbrellas",
        "pose": "Three standing without umbrellas in middle of crossing, crowd moving around them",
        "style": "Cinematic wet editorial, Tokyo urban fashion",
        "negative": "no umbrellas for models, no dry clothing",
    },
    "trio_underwater_temple": {
        "name": "Trio Underwater Temple",
        "category": "🎭 Trio Glamour",
        "background": "Sunken ancient Greek temple underwater, shafts of light from surface, coral growing on marble columns",
        "outfit": "Top: white sheer flowing in water currents, arms raised toward light. Middle: gold micro bikini, hair floating. Bottom: black bodysuit, crouching on coral column",
        "material": "White sheer vs gold micro bikini vs black bodysuit — vertical underwater composition",
        "lighting": "Deep turquoise light, sunlight shafts from surface, ethereal underwater glow, bubbles rising",
        "pose": "Three models suspended at different depths — surface, mid-water, seafloor",
        "style": "Surreal fashion editorial, underwater goddess concept",
        "negative": "no surface setting, no opaque coverage on top model",
    },
    "trio_volcano_crater": {
        "name": "Trio Volcano Crater",
        "category": "🎭 Trio Glamour",
        "background": "Active volcano at night, river of lava below, ash and embers in air, eruption in distance",
        "outfit": "Lowest: red sheer gown open front, lava glow behind. Middle: black cape arms spread, embers surrounding. Highest: gold micro dress, silhouetted against eruption",
        "material": "Red sheer vs black cape vs gold micro — three volcanic level contrast",
        "lighting": "Deep orange-red lava light, dramatic ash clouds, ember particles",
        "pose": "Three models on different volcanic rock outcroppings at different heights",
        "style": "Extreme nature editorial, fire goddess trio",
        "negative": "no safe calm setting, no conservative coverage",
    },
    "trio_opera_house_stage": {
        "name": "Trio Opera House Stage",
        "category": "🎭 Trio Glamour",
        "background": "Massive opera house stage, red velvet curtains parting, full orchestra pit visible, packed audience",
        "outfit": "Left: white swan ballet corset, micro tutu. Center: black latex opera gown, extreme slit, center stage. Right: red sequin backless gown, high slit",
        "material": "White ballet corset vs black latex vs red sequin — theatrical trio",
        "lighting": "Dramatic spotlights from above, rich theatrical red and gold, orchestra pit glowing",
        "pose": "Three in dramatic performance triangle, left en pointe, center dominant, right spinning",
        "style": "Theatrical fashion editorial, opera house spectacle",
        "negative": "no empty theater, no conservative stage wear",
    },
    "trio_desert_salt_flat": {
        "name": "Trio Desert Salt Flat",
        "category": "🎭 Trio Glamour",
        "background": "Bolivian salt flats at blue hour, perfect mirror reflection of sky, infinite horizon",
        "outfit": "Left: orange micro silk dress, wind lifting. Center: nude-tone sheer bodysuit, arms wide, completely transparent. Right: electric blue micro dress, spinning",
        "material": "Orange silk vs nude sheer vs blue micro — three color reflections on perfect mirror",
        "lighting": "Blue-purple sky, perfect mirror reflection doubling all three models, wide open space",
        "pose": "Three evenly spaced, reflections below creating six figures",
        "style": "Surreal nature editorial, salt flat mirror goddess",
        "negative": "no overcast sky, no opaque center dress",
    },
    "trio_cherry_blossom_storm": {
        "name": "Trio Cherry Blossom Storm",
        "category": "🎭 Trio Glamour",
        "background": "Ancient Japanese shrine, massive cherry blossom storm, thousands of pink petals in wind, red torii gates",
        "outfit": "Left: black latex bodysuit, petals sticking to surface. Center: white sheer kimono open, nothing underneath, petals covering naturally. Right: pink micro silk dress, arms raised catching petals",
        "material": "Black latex vs white sheer open vs pink micro — blossom contrast",
        "lighting": "Soft pink-white diffused light, magical petal atmosphere, torii gates in background",
        "pose": "Three in sakura blizzard, left stoic, center ethereal, right joyful",
        "style": "Ethereal nature editorial, sakura goddess trio",
        "negative": "no winter setting, no opaque center kimono",
    },
    "trio_aurora_iceland": {
        "name": "Trio Aurora Iceland",
        "category": "🎭 Trio Glamour",
        "background": "Icelandic black sand beach at night, massive aurora borealis filling sky in green-purple, volcanic rocks, ocean waves",
        "outfit": "Left: silver liquid metal micro dress, aurora reflected. Center: sheer white bodysuit, aurora visible through fabric, arms raised to sky. Right: black wetsuit unzipped to hip, ocean spray",
        "material": "Silver metallic vs white sheer vs black unzipped wetsuit — aurora light on all three",
        "lighting": "Neon aurora light, ocean spray, otherworldly green-purple sky",
        "pose": "Three at water's edge, center arms raised to aurora, left and right flanking",
        "style": "Magical nature editorial, aurora goddess trio",
        "negative": "no daylight, no opaque center bodysuit",
    },
    "trio_art_museum_after_hours": {
        "name": "Trio Art Museum After Hours",
        "category": "🎭 Trio Glamour",
        "background": "Empty Louvre Grande Galerie at night, masterpiece paintings lining walls, Venus de Milo sculpture center, moonlight shaft",
        "outfit": "Left: Renaissance-inspired gold draped fabric, minimal, hand on painting frame. Center: nude body paint as marble statue, grey-white. Right: black velvet micro dress, examining painting",
        "material": "Gold drape vs marble body paint vs black velvet — living art concept",
        "lighting": "Cool blue moonlight, warm painting glow, single spotlight on sculpture",
        "pose": "Left touching painting, center posed as living statue, right contemplating",
        "style": "Conceptual fashion editorial, living art vs fashion",
        "negative": "no daytime museum, no conventional all-clothed trio",
    },
    "trio_penthouse_pool_dawn": {
        "name": "Trio Penthouse Pool Dawn",
        "category": "🎭 Trio Glamour",
        "background": "Dubai Burj Khalifa penthouse infinity pool at dawn, golden horizon, city awakening below",
        "outfit": "Left: red micro bikini, stepping into pool, one leg raised. Center: gold body chain only, waist deep in water, arms raised. Right: white sheer coverup soaking wet, sitting on pool edge",
        "material": "Red micro bikini vs gold body chain vs wet sheer coverup",
        "lighting": "Dawn light painting everything gold, Burj Khalifa silhouetted, pool reflections",
        "pose": "Three at different pool entry points — standing edge, waist deep, seated edge",
        "style": "Luxury lifestyle editorial, Dubai dawn goddesses",
        "negative": "no nighttime, no conservative swimwear",
    },
}

# ══════════════════════════════════════════════════════════
# PRESET_CATEGORIES 추가 내용
# ══════════════════════════════════════════════════════════

ARCHETYPE_KEYS = [k for k, v in PRESETS.items() if v["category"] == "🎭 Archetype Glamour"]
DUO_KEYS       = [k for k, v in PRESETS.items() if v["category"] == "👯 Duo Glamour"]
TRIO_KEYS      = [k for k, v in PRESETS.items() if v["category"] == "🎭 Trio Glamour"]

CATEGORY_INSERT = (
    '    "🎭 Archetype Glamour": [\n' +
    ''.join(f'        "{k}",\n' for k in ARCHETYPE_KEYS) +
    '    ],\n'
    '    "👯 Duo Glamour": [\n' +
    ''.join(f'        "{k}",\n' for k in DUO_KEYS) +
    '    ],\n'
    '    "🎭 Trio Glamour": [\n' +
    ''.join(f'        "{k}",\n' for k in TRIO_KEYS) +
    '    ],\n'
)

HOF_INSERT = (
    '    # 🎭 Archetype Glamour\n' +
    ''.join(f'    "{k}",\n' for k in ARCHETYPE_KEYS) +
    '    # 👯 Duo Glamour\n' +
    ''.join(f'    "{k}",\n' for k in DUO_KEYS) +
    '    # 🎭 Trio Glamour\n' +
    ''.join(f'    "{k}",\n' for k in TRIO_KEYS)
)

HOF_ANCHOR = '    "amalfi_cliff_storm",'

# ══════════════════════════════════════════════════════════
# 실행
# ══════════════════════════════════════════════════════════

def write_jsons():
    created, skipped = [], []
    for key, data in PRESETS.items():
        path = PRESETS_DIR / f"{key}.json"
        if path.exists():
            skipped.append(key)
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        created.append(key)
    print(f"✅ JSON 생성: {len(created)}개")
    if skipped:
        print(f"⚠️  스킵: {len(skipped)}개")

def patch_meta():
    content = TARGET.read_text(encoding="utf-8")

    # PRESET_CATEGORIES 추가 — "🌧️ Wet Dress Glamour" 뒤
    cat_anchor = '"🌧️ Wet Dress Glamour"'
    if "Archetype Glamour" in content:
        print("⚠️  PRESET_CATEGORIES 이미 존재 — 스킵")
    else:
        idx = content.find(cat_anchor)
        if idx == -1:
            # 영어 변환된 버전
            cat_anchor = '"🌧️ Wet Dress Glamour"'
            idx = content.find(cat_anchor)
        if idx == -1:
            print("❌ 카테고리 앵커 미발견")
            return
        # 해당 카테고리 블록 끝(},) 찾기
        close = content.find('],', idx)
        insert_at = close + 2
        content = content[:insert_at] + '\n' + CATEGORY_INSERT + content[insert_at:]
        print("✅ PRESET_CATEGORIES 삽입 완료")

    # HOF_TIER 추가
    if '"bond_girl_casino"' in content:
        print("⚠️  HOF_TIER 이미 존재 — 스킵")
    else:
        idx = content.find(HOF_ANCHOR)
        if idx == -1:
            print("❌ HOF 앵커 미발견")
            return
        line_start = content.rfind("\n", 0, idx) + 1
        content = content[:line_start] + HOF_INSERT + content[line_start:]
        print("✅ HOF_TIER 삽입 완료")

    TARGET.write_text(content, encoding="utf-8")
    print("💾 저장 완료")

def verify():
    content = TARGET.read_text(encoding="utf-8")
    json_count = sum(1 for k in PRESETS if (PRESETS_DIR / f"{k}.json").exists())
    hof_start = content.find("HOF_TIER = {")
    hof_end = content.find("\n}", hof_start)
    hof_block = content[hof_start:hof_end]
    hof_count = sum(1 for k in PRESETS if f'"{k}"' in hof_block)
    print(f"\n── 검증 ──────────────────────")
    print(f"JSON: {json_count}/{len(PRESETS)}개")
    print(f"HOF_TIER: {hof_count}/{len(PRESETS)}개")
    print(f"──────────────────────────────")

if __name__ == "__main__":
    print("=" * 50)
    print("🎭👯 Archetype/Duo/Trio Glamour 패치")
    print("=" * 50)
    write_jsons()
    patch_meta()
    verify()
    print('\ngit add presets/ core/presets_meta.py; git commit -m "🎭👯 Archetype/Duo/Trio Glamour 30종 HOF 추가"; git push')
