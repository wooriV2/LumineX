"""
generate_multi_bodypaint_presets_v2.py
단일 배경 + 대비 바디페인팅 구조로 전면 수정
핵심 원칙: 하나의 공간에 2~3인이 같이 있고, 페인팅만 극명하게 대비
"""

import json
from pathlib import Path

PRESETS_DIR = Path("C:/Dev/LumineX/presets")
QUALITY = "ultra-sharp, 8K, professional editorial photography, hyperrealistic skin texture"

# ──────────────────────────────────────────────────────────
# G1 — 대비형 듀오 (6종) — 단일 배경
# ──────────────────────────────────────────────────────────

PRESETS = []

# 1. fire & ice — 단일: 미니멀 다크 스튜디오
PRESETS.append({
    "name": "duo_fire_and_ice_bodypaint",
    "subject": "Two stunning female models standing side by side in the same dark studio space",
    "body": "Model A and Model B, identical slim toned builds, standing close together",
    "outfit": (
        "Model A: full body paint art — blazing fire and lava, orange red crimson flame "
        "patterns covering entire body, molten magma veins, volcanic ember glow. "
        "Model B: full body paint art — arctic ice and frost crystals, deep blue white silver "
        "patterns, crystalline ice formations, frozen breath texture. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME dark studio background for both models"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black minimalist studio, dark seamless backdrop, both models in the same space",
    "lighting": "dual split lighting from opposite sides: warm orange fire glow on Model A from left, cold blue ice glow on Model B from right, colors meeting and mixing at center between them",
    "style": "high concept fashion editorial, dueling elements art photography, Vogue Italia avant-garde",
    "quality": QUALITY,
})

# 2. day & night — 단일: 황혼 루프탑
PRESETS.append({
    "name": "duo_day_and_night_bodypaint",
    "subject": "Two stunning female models standing together on a rooftop at twilight",
    "body": "Model A: golden radiant presence. Model B: silver midnight presence. Both standing in same twilight space",
    "outfit": (
        "Model A: full body paint art — golden sun rays, daylight sky clouds and sunbeams "
        "painted across entire body, warm golden yellow orange palette. "
        "Model B: full body paint art — deep night sky, silver moon, stars and galaxy "
        "painted across entire body, midnight blue silver white palette. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME rooftop twilight background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "luxury rooftop at exact twilight moment, same sky background for both models, city lights beginning to appear",
    "lighting": "Model A bathed in warm golden last sunlight, Model B in cool rising moonlight, both in same twilight sky atmosphere",
    "style": "celestial duality editorial, Harper's Bazaar conceptual, twilight fashion photography",
    "quality": QUALITY,
})

# 3. bloom & void — 단일: 화이트 스튜디오
PRESETS.append({
    "name": "duo_bloom_and_void_bodypaint",
    "subject": "Two stunning female models standing together in a clean white studio",
    "body": "Model A: lush colorful presence. Model B: stark minimal presence. Both in same white space",
    "outfit": (
        "Model A: full body paint art — riotous flower garden explosion, every type of flower "
        "blooming across entire body, vivid color botanical illustration painted on skin. "
        "Model B: full body paint art — pure matte black void with subtle deep space star "
        "dust, anti-color darkness, deep black with faint cosmic depth. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME white studio background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure white minimalist studio, seamless white backdrop, both models sharing same clean space",
    "lighting": "soft even white studio light for both, the contrast comes entirely from the body paint not the lighting",
    "style": "maximum contrast conceptual editorial, existence vs void, Alexander McQueen avant-garde",
    "quality": QUALITY,
})

# 4. gold & shadow — 단일: 바로크 갤러리
PRESETS.append({
    "name": "duo_gold_and_shadow_bodypaint",
    "subject": "Two stunning female models standing together in a dark baroque gallery",
    "body": "Model A: luminous gold. Model B: deep shadow ink. Both in same gallery space",
    "outfit": (
        "Model A: full body paint art — Gustav Klimt gold leaf patterns, Byzantine mosaics, "
        "ornate golden geometric shapes, intricate gold ornamentation across entire body. "
        "Model B: full body paint art — deep black sumi ink calligraphy, Rembrandt-style "
        "chiaroscuro shadow painting, ink wash darkness across entire body. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME baroque gallery background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dark baroque gallery interior, gilt-framed paintings on walls, candles, both models in same opulent space",
    "lighting": "warm golden candlelight for both models, gold body paint glowing, shadow body paint absorbing light",
    "style": "Klimt meets Rembrandt editorial, art history duality, Numéro magazine avant-garde",
    "quality": QUALITY,
})

# 5. ocean & desert — 단일: 중성 스튜디오 or 자연 경계
PRESETS.append({
    "name": "duo_ocean_and_desert_bodypaint",
    "subject": "Two stunning female models standing together on a flat natural terrain",
    "body": "Model A: fluid ocean goddess. Model B: sculpted desert goddess. Both in same landscape",
    "outfit": (
        "Model A: full body paint art — deep ocean waves, coral reef patterns, bioluminescent "
        "sea creatures, turquoise blue teal navy ocean depths painted across entire body. "
        "Model B: full body paint art — Sahara sand dunes, cracked desert earth, "
        "golden sand patterns, sun-bleached warm ochre terracotta across entire body. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME neutral terrain background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "vast flat salt flat or neutral terrain, simple horizon, both models sharing same open landscape background",
    "lighting": "natural even outdoor light falling on both models equally, contrast is purely from body paint",
    "style": "elemental nature editorial, National Geographic luxury fashion, Vogue environmental concept",
    "quality": QUALITY,
})

# 6. circuit & nature — 단일: 폐공장 (검증에서 이미 최고 결과)
PRESETS.append({
    "name": "duo_circuit_and_nature_bodypaint",
    "subject": "Two stunning female models facing each other in an abandoned industrial space",
    "body": "Model A: geometric precision. Model B: organic flowing nature. Both in same decayed space",
    "outfit": (
        "Model A: full body paint art — printed circuit board patterns, neon green blue "
        "electronic pathways, microchip grids, LED light effects painted across entire body. "
        "Model B: full body paint art — deep forest moss and lichen, tree bark textures, "
        "fern and vine botanicals, earth green brown patterns painted across entire body. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME abandoned factory background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "abandoned industrial factory reclaimed by nature, concrete walls with vines, server racks, both models in same decayed space",
    "lighting": "mixed industrial light for both: cold neon tubes overhead, warm natural light through broken ceiling, same atmosphere",
    "style": "technology vs nature conceptual editorial, cyberpunk botanical, Dazed magazine",
    "quality": QUALITY,
})

# ──────────────────────────────────────────────────────────
# G2 — 대비형 트리오 (6종) — 단일 배경
# ──────────────────────────────────────────────────────────

# 7. RGB trinity — 단일: 블랙 스튜디오
PRESETS.append({
    "name": "trio_rgb_trinity_bodypaint",
    "subject": "Three stunning female models standing in a row in the same black studio",
    "body": "Three models with identical athletic builds, equal spacing, same black studio",
    "outfit": (
        "Model A: full body paint art — pure saturated RED across entire body, rich crimson scarlet. "
        "Model B: full body paint art — pure saturated GREEN across entire body, emerald forest green. "
        "Model C: full body paint art — pure saturated BLUE across entire body, cobalt royal blue. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in the SAME black studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black minimalist studio, all three models in same dark seamless space",
    "lighting": "each model lit by matching color spotlight: red on A, green on B, blue on C, colors blending where they meet",
    "style": "primary color art installation editorial, RGB light theory, Andy Warhol meets body art",
    "quality": QUALITY,
})

# 8. earth water sky — 단일: 절벽 야외
PRESETS.append({
    "name": "trio_earth_water_sky_bodypaint",
    "subject": "Three stunning female models standing together on a dramatic cliff edge",
    "body": "Three models in sacred triangle formation, all standing on same cliff",
    "outfit": (
        "Model A: full body paint art — rich earth and soil, brown ochre clay terracotta rock formations across entire body. "
        "Model B: full body paint art — flowing water ocean waves river currents, turquoise blue patterns across entire body. "
        "Model C: full body paint art — open sky clouds atmospheric light, pale blue white gradient across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE on the SAME cliff overlooking ocean"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dramatic sea cliff edge, all three models standing together on same rocky cliff, ocean and sky visible behind all of them",
    "lighting": "natural golden hour light falling equally on all three, same warm outdoor atmosphere",
    "style": "elemental goddess trilogy, mythology editorial, Vogue Italia conceptual",
    "quality": QUALITY,
})

# 9. past present future — 단일: 미니멀 스튜디오
PRESETS.append({
    "name": "trio_past_present_future_bodypaint",
    "subject": "Three stunning female models standing together in a clean minimalist studio",
    "body": "Three models representing three eras, all in same neutral studio space",
    "outfit": (
        "Model A: full body paint art — ancient Egyptian hieroglyphs, Byzantine mosaic patterns, classical mythology motifs in gold ochre across entire body. "
        "Model B: full body paint art — modern geometric patterns, clean contemporary lines, current art movement in black white grey across entire body. "
        "Model C: full body paint art — futuristic circuit patterns, holographic iridescent neon cyberpunk tech art in electric blue silver across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in the SAME neutral studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "neutral grey minimalist studio, clean seamless backdrop, all three models sharing same simple space",
    "lighting": "clean even studio lighting for all three, contrast is entirely from the body paint styles",
    "style": "time continuum conceptual editorial, past present future, Vogue minimalist concept",
    "quality": QUALITY,
})

# 10. predator prey apex — 단일: 사바나
PRESETS.append({
    "name": "trio_predator_prey_apex_bodypaint",
    "subject": "Three stunning female models standing together on African savanna at golden hour",
    "body": "Three models in wildlife triangle, all standing on same savanna ground",
    "outfit": (
        "Model A: full body paint art — leopard and cheetah spots, feline predator rosettes across entire body, tawny gold black. "
        "Model B: full body paint art — deer and gazelle patterns, delicate fawn markings, spotted deer texture across entire body, soft brown cream. "
        "Model C: full body paint art — eagle and hawk feather patterns, raptor wing markings, bird of prey plumage across entire body, dark brown white. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE on the SAME savanna"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "African savanna at golden hour, acacia tree silhouettes, vast sky, all three models on same grassland",
    "lighting": "warm African golden hour sunlight falling equally on all three models",
    "style": "wildlife editorial, National Geographic luxury fashion, nature hierarchy art photography",
    "quality": QUALITY,
})

# 11. ink gold chrome — 단일: 화이트 스튜디오
PRESETS.append({
    "name": "trio_ink_gold_chrome_bodypaint",
    "subject": "Three stunning female models standing in a row in pure white studio",
    "body": "Three models representing three materials, all in same white space",
    "outfit": (
        "Model A: full body paint art — deep black sumi ink calligraphy, Japanese ink wash painting, fluid black strokes across entire body. "
        "Model B: full body paint art — hammered gold leaf, Byzantine gold mosaic, warm gilded patterns across entire body. "
        "Model C: full body paint art — chrome silver mirror finish, liquid metal reflective patterns, futuristic chrome across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in the SAME white studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure white minimalist studio, polished reflective floor, all three models in same clean space",
    "lighting": "perfect studio lighting for all three, emphasizing ink darkness, gold warmth, chrome reflection",
    "style": "materials trilogy editorial, Vogue minimalist conceptual, fine art body photography",
    "quality": QUALITY,
})

# 12. season trinity — 단일: 중성 야외
PRESETS.append({
    "name": "trio_season_trinity_bodypaint",
    "subject": "Three stunning female models standing together in a neutral outdoor space",
    "body": "Three models representing three seasons, all in same outdoor setting",
    "outfit": (
        "Model A: full body paint art — cherry blossom sakura, spring flowers in bloom, soft pink peach lavender botanical spring patterns across entire body. "
        "Model B: full body paint art — tropical flowers, summer sun, ocean waves, vibrant coral orange yellow green summer patterns across entire body. "
        "Model C: full body paint art — snowflakes, ice crystals, bare winter branches, silver white pale blue frost patterns across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in the SAME outdoor setting"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "neutral outdoor open field with soft horizon, all three models together in same space, contrast from body paint only",
    "lighting": "soft natural light falling equally on all three, warm neutral atmosphere",
    "style": "seasons editorial, botanical art photography, Vogue seasonal concept",
    "quality": QUALITY,
})

# ──────────────────────────────────────────────────────────
# G3 — 연결형 듀오 (6종) — 단일 배경 + 연결 강조
# ──────────────────────────────────────────────────────────

# 13. butterfly split
PRESETS.append({
    "name": "duo_butterfly_split_bodypaint",
    "subject": "Two stunning female models standing close together side by side, bodies touching, forming one complete butterfly",
    "body": "Model A carries left wing, Model B carries right wing, standing touching at center",
    "outfit": (
        "Model A: full body paint art — LEFT WING of giant monarch butterfly, orange black white "
        "wing pattern on her right side of body facing center, seamlessly connecting to Model B. "
        "Model B: full body paint art — RIGHT WING of same giant monarch butterfly, mirror wing "
        "pattern on her left side of body facing center. "
        "CONNECTED ART: their bodies together form ONE complete butterfly. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME flower garden background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "lush flower garden, soft bokeh flowers, both models in same garden space standing close together",
    "lighting": "soft natural garden light, gentle golden hour glow, same warm atmosphere for both",
    "style": "connected body art editorial, nature symmetry concept, Vogue Italia botanical",
    "quality": QUALITY,
})

# 14. yin yang merge
PRESETS.append({
    "name": "duo_yin_yang_merge_bodypaint",
    "subject": "Two stunning female models standing back to back forming perfect yin yang in same zen garden",
    "body": "Model A: white yang. Model B: black yin. Back to back in same space",
    "outfit": (
        "Model A: full body paint art — pure WHITE body paint across entire body with one BLACK circle dot, yang energy. "
        "Model B: full body paint art — pure BLACK body paint across entire body with one WHITE circle dot, yin energy. "
        "CONNECTED ART: back to back they form complete yin-yang taijitu symbol. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME zen garden background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "zen Japanese garden, raked sand, bamboo, both models in same peaceful garden space",
    "lighting": "perfectly even diffused light for both models, same atmosphere, graphic clarity",
    "style": "philosophical duality editorial, Eastern philosophy art, minimalist fine art photography",
    "quality": QUALITY,
})

# 15. world map
PRESETS.append({
    "name": "duo_world_map_bodypaint",
    "subject": "Two stunning female models standing side by side forming complete world map in same blue studio",
    "body": "Model A: eastern hemisphere. Model B: western hemisphere. Both in same studio",
    "outfit": (
        "Model A: full body paint art — EASTERN HEMISPHERE map: Europe Africa Asia Australia "
        "painted across entire body, continents in terracotta on blue ocean background. "
        "Model B: full body paint art — WESTERN HEMISPHERE map: Americas painted across "
        "entire body, seamlessly connecting to Model A at center. "
        "CONNECTED ART: together they form one complete world map. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME blue studio background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "minimalist blue studio, both models in same space standing side by side",
    "lighting": "soft even cartographic studio light, clean map-reading clarity, same for both",
    "style": "cartography art editorial, world geography concept photography",
    "quality": QUALITY,
})

# 16. klimt tree
PRESETS.append({
    "name": "duo_klimt_tree_bodypaint",
    "subject": "Two stunning female models standing side by side in dark art nouveau gallery forming Klimt Tree of Life",
    "body": "Model A: left half of tree. Model B: right half. Both in same gallery",
    "outfit": (
        "Model A: full body paint art — LEFT HALF of Gustav Klimt Tree of Life: swirling golden "
        "branches jeweled ornaments spiral tendrils in Klimt gold leaf style across entire body. "
        "Model B: full body paint art — RIGHT HALF of same Klimt Tree of Life: mirror swirling "
        "branches jeweled elements perfect continuation of Model A. "
        "CONNECTED ART: together they form complete Tree of Life. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME art nouveau gallery background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dark art nouveau gallery, golden ornamental details, both models in same Viennese gallery space",
    "lighting": "warm golden gallery lighting for both, Klimt's characteristic gold leaf glow",
    "style": "Klimt body art editorial, Vienna Secession living painting, fine art photography",
    "quality": QUALITY,
})

# 17. galaxy split
PRESETS.append({
    "name": "duo_galaxy_split_bodypaint",
    "subject": "Two stunning female models standing back to back forming spiral galaxy in same dark studio",
    "body": "Model A: one galaxy arm. Model B: opposite arm. Back to back in same space",
    "outfit": (
        "Model A: full body paint art — RIGHT spiral arm of galaxy: stars and nebula, "
        "deep space blues purples, star clusters painted across entire body. "
        "Model B: full body paint art — LEFT spiral arm of same galaxy: opposite arm, "
        "mirrored star patterns, cosmic continuation. "
        "CONNECTED ART: back to back they form one complete spiral galaxy. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME dark cosmic studio background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black studio with subtle star field, both models in same deep space atmosphere",
    "lighting": "bioluminescent cosmic glow from paintings themselves, same purple blue constellation lighting for both",
    "style": "cosmic art editorial, NASA astronomy meets fashion, deep space concept photography",
    "quality": QUALITY,
})

# 18. wave hokusai
PRESETS.append({
    "name": "duo_wave_hokusai_bodypaint",
    "subject": "Two stunning female models standing side by side forming Hokusai Great Wave in same minimalist studio",
    "body": "Model A: left wave crest. Model B: right wave and Mt Fuji. Both in same studio",
    "outfit": (
        "Model A: full body paint art — LEFT HALF of Hokusai Great Wave: massive blue white "
        "wave crest with foam tips, Japanese woodblock Prussian blue and white across entire body. "
        "Model B: full body paint art — RIGHT HALF of Great Wave: wave continuation and "
        "distant Mt Fuji, same woodblock style, connecting to Model A. "
        "CONNECTED ART: together they recreate complete Great Wave off Kanagawa. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME minimal Japanese studio background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "minimal Japanese studio, subtle tatami floor, both models in same zen space",
    "lighting": "soft even Japanese art paper light quality, same woodblock print illumination for both",
    "style": "Hokusai living painting editorial, ukiyo-e body art, Japanese fine art photography",
    "quality": QUALITY,
})

# ──────────────────────────────────────────────────────────
# G4 — 연결형 트리오 (6종) — 단일 배경
# ──────────────────────────────────────────────────────────

# 19. triptych klimt
PRESETS.append({
    "name": "trio_triptych_klimt_bodypaint",
    "subject": "Three stunning female models standing side by side in same gold art nouveau gallery forming Klimt triptych",
    "body": "Left panel, center panel, right panel — all three in same gallery",
    "outfit": (
        "Model A: full body paint art — LEFT PANEL Klimt triptych: golden ornamental border, "
        "female figure in gold mosaic on skin. "
        "Model B: full body paint art — CENTER PANEL: Klimt The Kiss central motif, "
        "embracing figures in gold, jeweled patterns, densest ornament. "
        "Model C: full body paint art — RIGHT PANEL: mirror of left, golden ornamental "
        "completing the triptych. "
        "CONNECTED ART: three bodies form one complete Klimt triptych. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME art nouveau gallery"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "grand art nouveau gallery, gilded frames on walls, all three models in same Viennese Secession space",
    "lighting": "warm golden museum lighting for all three, Klimt golden aura atmosphere",
    "style": "Klimt living triptych editorial, art installation fashion, Vogue fine art photography",
    "quality": QUALITY,
})

# 20. phoenix rising
PRESETS.append({
    "name": "trio_phoenix_rising_bodypaint",
    "subject": "Three stunning female models forming one massive phoenix in same dramatic dark studio",
    "body": "Left wing, phoenix body center, right wing — all three in same fiery space",
    "outfit": (
        "Model A: full body paint art — LEFT WING of phoenix: fiery orange red gold feather "
        "patterns, flame-tipped wing feathers across entire body. "
        "Model B: full body paint art — PHOENIX BODY CENTER: dense golden fire scales, "
        "phoenix breast and torso in crimson gold, most intense fire patterns. "
        "Model C: full body paint art — RIGHT WING mirror: identical mirror wing to Model A. "
        "CONNECTED ART: three bodies form one massive phoenix in flight. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME dramatic dark studio with fire atmosphere"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dark dramatic studio with ember and fire atmosphere, all three models in same space, dark background with orange glow",
    "lighting": "warm dramatic fire orange glow from below for all three, ember light, same phoenix fire illumination",
    "style": "phoenix mythology editorial, living mythology art photography, power fashion concept",
    "quality": QUALITY,
})

# 21. world tree
PRESETS.append({
    "name": "trio_world_tree_bodypaint",
    "subject": "Three stunning female models arranged vertically in same primordial forest forming Yggdrasil",
    "body": "Roots model, trunk model, canopy model — all in same ancient forest",
    "outfit": (
        "Model A: full body paint art — ROOTS of Yggdrasil: deep twisting root systems, "
        "underground earth, ancient Norse runes, dark brown black earth tones across entire body. "
        "Model B: full body paint art — TRUNK: massive bark texture, life force channels, "
        "vertical wood grain, earth to sky browns across entire body. "
        "Model C: full body paint art — CANOPY: spreading branches, leaves and sky, "
        "green gold leaf patterns across entire body. "
        "CONNECTED ART: vertically together they form complete World Tree. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME primordial forest"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "primordial ancient Norse forest, all three models in same mystical woodland space, cosmic axis atmosphere",
    "lighting": "mystical forest light for all three, same dappled ancient atmosphere",
    "style": "Norse mythology editorial, world tree art concept, spiritual fashion photography",
    "quality": QUALITY,
})

# 22. ocean depth
PRESETS.append({
    "name": "trio_ocean_depth_bodypaint",
    "subject": "Three stunning female models standing together in same deep blue studio forming ocean depth cross-section",
    "body": "Surface model, midwater model, deep model — all in same underwater atmosphere",
    "outfit": (
        "Model A: full body paint art — OCEAN SURFACE ZONE: turquoise bright shallow water, "
        "tropical fish, coral, vivid colors across entire body. "
        "Model B: full body paint art — MIDWATER TWILIGHT ZONE: deeper blue, jellyfish and "
        "squid, fading light, blue purple tones across entire body. "
        "Model C: full body paint art — ABYSSAL DEEP ZONE: pitch black with bioluminescent "
        "creatures, anglerfish lights, electric blue bioluminescence across entire body. "
        "CONNECTED ART: together they form complete ocean depth. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME deep blue studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "deep blue studio, underwater atmosphere, all three models in same aquatic space with gradient blue darkness",
    "lighting": "gradient underwater light: bright turquoise for Model A, dim blue for Model B, near darkness with bioluminescent glow for Model C — but same studio space",
    "style": "ocean science editorial, deep sea art concept, National Geographic luxury fashion",
    "quality": QUALITY,
})

# 23. aurora spectrum
PRESETS.append({
    "name": "trio_aurora_spectrum_bodypaint",
    "subject": "Three stunning female models standing together under same arctic night sky forming aurora borealis",
    "body": "Left aurora curtain, center peak, right curtain — all three under same northern lights",
    "outfit": (
        "Model A: full body paint art — LEFT AURORA CURTAIN: flowing green teal aurora "
        "ribbons, vertical light curtains across entire body. "
        "Model B: full body paint art — CENTER AURORA PEAK: most intense aurora, purple pink "
        "white at maximum intensity, full spectrum across entire body. "
        "Model C: full body paint art — RIGHT AURORA CURTAIN: blue violet aurora ribbons "
        "mirroring left side across entire body. "
        "CONNECTED ART: three bodies form one complete aurora borealis panorama. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE under SAME arctic night sky"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "Arctic tundra night, snow-covered landscape, all three models under same northern lights sky",
    "lighting": "ethereal aurora glow from paintings themselves, same cold arctic night atmosphere for all three",
    "style": "aurora art installation editorial, arctic conceptual photography, cosmic fashion concept",
    "quality": QUALITY,
})

# 24. cosmic creation
PRESETS.append({
    "name": "trio_cosmic_creation_bodypaint",
    "subject": "Three stunning female models standing together in same pure black space studio representing cosmic creation timeline",
    "body": "Big Bang model, nebula model, planet-life model — all in same cosmic void",
    "outfit": (
        "Model A: full body paint art — BIG BANG: pure white gold explosion radiating from "
        "body center, energy burst patterns, primordial light across entire body. "
        "Model B: full body paint art — NEBULA FORMATION: deep space purple blue, swirling "
        "gas clouds, proto-stars, nebula dust across entire body. "
        "Model C: full body paint art — PLANET AND LIFE: blue green Earth patterns, "
        "continents forming, DNA helix, first life emergence across entire body. "
        "CONNECTED ART: three bodies narrate complete cosmic creation sequence. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME deep black cosmic studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black studio with cosmic background, all three models in same deep space void",
    "lighting": "Model A in brilliant white light, Model B in cool nebula purple glow, Model C in warm golden life light — but same dark studio space for all three",
    "style": "cosmic creation mythology editorial, universe origin art concept, scientific fashion photography",
    "quality": QUALITY,
})

# ──────────────────────────────────────────────────────────
# 저장
# ──────────────────────────────────────────────────────────

def save_presets(presets, target_dir):
    target_dir = Path(target_dir)
    saved = []
    for preset in presets:
        name = preset["name"]
        path = target_dir / f"{name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(preset, f, ensure_ascii=False, indent=2)
        saved.append(name)
        print(f"  ✅ {name}.json")
    return saved

if __name__ == "__main__":
    print(f"\n🎨 멀티 바디페인팅 v2 — 단일 배경 전면 수정 ({len(PRESETS)}종)\n")
    print("핵심 변경: 분할 배경 → 단일 공간, 2~3인이 같은 배경에 다른 페인팅\n")
    
    for p in PRESETS:
        print(f"  - {p['name']}")
    
    print(f"\n총 {len(PRESETS)}종")
    answer = input("\n저장하시겠습니까? (y/n): ")
    if answer.lower() == 'y':
        saved = save_presets(PRESETS, PRESETS_DIR)
        print(f"\n✅ {len(saved)}개 프리셋 저장 완료 (덮어쓰기)")
    else:
        print("저장 취소됨")
