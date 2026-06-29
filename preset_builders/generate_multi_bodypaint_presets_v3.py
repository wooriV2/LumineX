"""
generate_multi_bodypaint_presets_v3.py
멀티 바디페인팅 확장 — 27종 추가
G1+6 / G2+6 / G3+6 / G4+6 / 4인5종 / 5인4종
실행: python preset_builders/generate_multi_bodypaint_presets_v3.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path("C:/Dev/LumineX/presets")
QUALITY = "ultra-sharp, 8K, professional editorial photography, hyperrealistic skin texture"

PRESETS = []

# ──────────────────────────────────────────────────────────
# G1 대비형 듀오 추가 (6종)
# ──────────────────────────────────────────────────────────

PRESETS.append({
    "name": "duo_east_and_west_bodypaint",
    "subject": "Two stunning female models standing side by side in the same minimalist studio",
    "body": "Model A: Eastern elegance. Model B: Western classical. Both in same clean space",
    "outfit": (
        "Model A: full body paint art — Eastern Asian art: Korean dancheong patterns, "
        "Chinese ink brush strokes, Japanese sumi-e bamboo, deep navy indigo gold across entire body. "
        "Model B: full body paint art — Western Renaissance fresco: Michelangelo-style classical "
        "figures, baroque ornamentation, cream gold marble patterns across entire body. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME minimalist studio background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure neutral grey minimalist studio, both models in same clean space",
    "lighting": "soft even studio light for both, Eastern warmth on Model A, Western cool light on Model B",
    "style": "East meets West conceptual editorial, cultural duality art photography, Vogue global",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_macro_and_micro_bodypaint",
    "subject": "Two stunning female models standing side by side in same black studio",
    "body": "Model A: cosmic macro scale. Model B: microscopic micro scale. Both in same dark space",
    "outfit": (
        "Model A: full body paint art — vast universe and galaxy: swirling nebula, "
        "spiral galaxies, star clusters, deep space blues purples across entire body. "
        "Model B: full body paint art — microscopic world: cell structures, DNA double helix, "
        "bacteria patterns, biological micro detail in teal green across entire body. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME black studio background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black minimalist studio, both models in same dark space",
    "lighting": "bioluminescent glow from both paintings, cosmic and cellular light for both",
    "style": "macro vs micro science editorial, scale contrast art photography, National Geographic luxury",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_ancient_and_future_bodypaint",
    "subject": "Two stunning female models standing together in same neutral grey studio",
    "body": "Model A: ancient civilization. Model B: far future. Both in same timeless space",
    "outfit": (
        "Model A: full body paint art — ancient Egypt: golden hieroglyphs, pharaoh cartouches, "
        "Anubis and Ra symbols, deep gold ochre across entire body. "
        "Model B: full body paint art — year 3000 future: holographic circuit patterns, "
        "neon blue data streams, cyberpunk tech art across entire body. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME neutral grey studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "neutral grey minimalist studio, same clean space for both timeless models",
    "lighting": "warm golden ancient light on Model A, cool neon futuristic light on Model B, same studio",
    "style": "time contrast editorial, ancient vs future art concept, Vogue timeless fashion",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_poison_and_medicine_bodypaint",
    "subject": "Two stunning female models standing together in same botanical studio space",
    "body": "Model A: dark toxin energy. Model B: healing light energy. Both in same space",
    "outfit": (
        "Model A: full body paint art — poison and venom: deadly nightshade, venomous snake "
        "scales, toxic mushroom patterns, deep crimson black purple across entire body. "
        "Model B: full body paint art — healing herbs and medicine: lavender chamomile "
        "aloe vera patterns, soft healing green white across entire body. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME botanical apothecary space"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dark botanical apothecary interior, dried herbs and plants, both models in same moody space",
    "lighting": "dramatic chiaroscuro, dark red glow on Model A, soft green healing light on Model B",
    "style": "botanical duality editorial, poison vs medicine art concept, dark nature photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_storm_and_calm_bodypaint",
    "subject": "Two stunning female models standing together on same coastal location",
    "body": "Model A: storm fury energy. Model B: serene calm energy. Both on same shore",
    "outfit": (
        "Model A: full body paint art — storm and lightning: dark thunderclouds, electric "
        "lightning bolts, turbulent waves, deep charcoal blue silver across entire body. "
        "Model B: full body paint art — dawn calm: gentle sunrise ripples, soft golden "
        "morning light, still water reflections, pale gold peach across entire body. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME coastal outdoor location"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dramatic coastal cliff, same ocean backdrop, both models on same rocky shore",
    "lighting": "dramatic split: stormy dark light on Model A, golden dawn light on Model B, same location",
    "style": "elemental contrast editorial, storm vs calm nature photography, Harper's Bazaar dramatic",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_deep_sea_bodypaint",
    "subject": "Two stunning female models standing together in same deep blue studio",
    "body": "Model A: dark depths creature. Model B: vibrant reef goddess. Both in same aquatic space",
    "outfit": (
        "Model A: full body paint art — deep sea abyss: anglerfish bioluminescence, "
        "dark ocean depths, mysterious black blue with glowing spots across entire body. "
        "Model B: full body paint art — tropical coral reef: vivid coral, tropical fish, "
        "bright turquoise teal orange reef colors across entire body. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME deep blue underwater studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "deep blue studio with underwater atmosphere, both models in same aquatic space",
    "lighting": "Model A in near darkness with bioluminescent glow, Model B in bright tropical light, same studio",
    "style": "ocean depth contrast editorial, deep sea vs reef art photography",
    "quality": QUALITY,
})

# ──────────────────────────────────────────────────────────
# G2 대비형 트리오 추가 (6종)
# ──────────────────────────────────────────────────────────

PRESETS.append({
    "name": "trio_sun_moon_star_bodypaint",
    "subject": "Three stunning female models standing in a row in same black cosmic studio",
    "body": "Model A: sun goddess. Model B: moon goddess. Model C: star goddess. All in same dark space",
    "outfit": (
        "Model A: full body paint art — blazing SUN: radiant golden solar flares, sunspot "
        "patterns, corona rays, warm gold orange red across entire body. "
        "Model B: full body paint art — silver MOON: crescent phases, lunar craters, "
        "moonlight glow, cool silver white grey across entire body. "
        "Model C: full body paint art — crystalline STARS: constellation maps, star cluster "
        "patterns, diamond sparkle, ice white blue across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME black cosmic studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black cosmic studio, star field background, all three in same celestial space",
    "lighting": "warm golden glow on Model A, cool silver on Model B, crystalline sparkle on Model C",
    "style": "celestial trinity editorial, cosmic goddess art photography, Vogue avant-garde",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_three_oceans_bodypaint",
    "subject": "Three stunning female models standing together in same blue studio",
    "body": "Model A: Pacific deep. Model B: Indian emerald. Model C: Arctic ice. All in same aquatic space",
    "outfit": (
        "Model A: full body paint art — PACIFIC OCEAN: deep navy blue, powerful waves, "
        "Pacific marine life across entire body. "
        "Model B: full body paint art — INDIAN OCEAN: warm emerald turquoise, tropical "
        "coral, exotic sea creatures across entire body. "
        "Model C: full body paint art — ARCTIC OCEAN: pale ice blue white, frozen surface "
        "cracks, polar bear and seal motifs across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME blue gradient studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "deep blue gradient studio, underwater atmosphere, all three in same oceanic space",
    "lighting": "cool blue lighting for all three, each model slightly different ocean tone",
    "style": "three oceans editorial, world ocean art concept, National Geographic luxury fashion",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_three_civilizations_bodypaint",
    "subject": "Three stunning female models standing together in same neutral museum space",
    "body": "Model A: Egyptian queen. Model B: Chinese empress. Model C: Mayan priestess. All in same museum",
    "outfit": (
        "Model A: full body paint art — ANCIENT EGYPT: gold hieroglyphs, pharaoh patterns, "
        "Eye of Ra, deep gold ochre across entire body. "
        "Model B: full body paint art — IMPERIAL CHINA: red dragon patterns, Chinese cloud "
        "motifs, Ming dynasty art, deep red gold across entire body. "
        "Model C: full body paint art — MAYAN CIVILIZATION: jade green geometric patterns, "
        "Mayan calendar motifs, serpent designs, deep green jade across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME museum space"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "grand museum interior, ancient artifacts, all three models in same historical space",
    "lighting": "warm museum lighting for all three, golden archaeological atmosphere",
    "style": "three civilizations editorial, world heritage art concept, archaeological fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_fire_water_earth_bodypaint",
    "subject": "Three stunning female models standing together on same dramatic cliff",
    "body": "Model A: fire element. Model B: water element. Model C: earth element. All on same cliff",
    "outfit": (
        "Model A: full body paint art — FIRE element: blazing flames, ember patterns, "
        "volcanic heat, deep orange red gold across entire body. "
        "Model B: full body paint art — WATER element: flowing waves, rain drops, "
        "ocean currents, deep blue aqua across entire body. "
        "Model C: full body paint art — EARTH element: stone textures, tree roots, "
        "soil and rock patterns, deep brown green across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE on SAME dramatic cliff"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dramatic sea cliff with visible elements: fire sky, ocean, rocky ground, all three together",
    "lighting": "warm fire light on Model A, cool water light on Model B, earthy natural light on Model C",
    "style": "elemental trinity editorial, classical elements art photography, mythology fashion",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_angel_human_demon_bodypaint",
    "subject": "Three stunning female models in dramatic triangle formation in same dark studio",
    "body": "Model A: divine angel. Model B: mortal human. Model C: dark demon. All in same space",
    "outfit": (
        "Model A: full body paint art — ANGEL: white feather patterns, golden halo motifs, "
        "celestial light rays, pure white gold across entire body. "
        "Model B: full body paint art — HUMAN: natural skin tones, organic botanical "
        "patterns, earth colors, warm natural hues across entire body. "
        "Model C: full body paint art — DEMON: dark crimson black scales, shadow patterns, "
        "infernal symbols, deep black red across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME dramatic dark studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dramatic dark studio with atmospheric smoke, all three models in same mysterious space",
    "lighting": "divine white light on Model A, warm natural on Model B, deep red shadow on Model C",
    "style": "divine hierarchy editorial, angel human demon art concept, dark fantasy fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_three_big_cats_bodypaint",
    "subject": "Three stunning female models standing together in same jungle clearing",
    "body": "Model A: leopard. Model B: tiger. Model C: black panther. All in same jungle",
    "outfit": (
        "Model A: full body paint art — LEOPARD: golden tawny rosette spots, "
        "amber yellow black patterns across entire body. "
        "Model B: full body paint art — TIGER: orange black white stripes, "
        "bold tiger stripe patterns across entire body. "
        "Model C: full body paint art — BLACK PANTHER: deep matte black with subtle "
        "shadow rosettes, midnight black patterns across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME jungle clearing"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "lush jungle clearing, dappled light through canopy, all three models in same tropical space",
    "lighting": "warm dappled jungle light for all three, golden hour filtering through trees",
    "style": "big cat trinity editorial, wildlife fashion photography, National Geographic luxury",
    "quality": QUALITY,
})

# ──────────────────────────────────────────────────────────
# G3 연결형 듀오 추가 (6종)
# ──────────────────────────────────────────────────────────

PRESETS.append({
    "name": "duo_dna_helix_bodypaint",
    "subject": "Two stunning female models standing back to back in same blue science studio, their bodies forming one complete DNA double helix",
    "body": "Model A: one DNA strand. Model B: complementary strand. Back to back forming complete helix",
    "outfit": (
        "Model A: full body paint art — LEFT STRAND of DNA double helix: blue phosphate "
        "backbone running down body, base pairs extending to right connecting to Model B. "
        "Model B: full body paint art — RIGHT STRAND of same DNA helix: complementary "
        "strand, base pairs connecting to Model A, completing double helix. "
        "CONNECTED ART: back to back they form one complete DNA double helix structure. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME blue science studio background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "deep blue science laboratory studio, both models in same space back to back",
    "lighting": "cool blue science lab light, bioluminescent DNA glow from both",
    "style": "science art editorial, DNA helix living sculpture, conceptual biology photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_solar_eclipse_bodypaint",
    "subject": "Two stunning female models overlapping in same black studio, together forming perfect solar eclipse",
    "body": "Model A: blazing sun. Model B: dark moon. Overlapping to create eclipse",
    "outfit": (
        "Model A: full body paint art — BLAZING SUN: radiating golden corona, solar flares, "
        "sunspot patterns, intense gold orange white across entire body. "
        "Model B: full body paint art — DARK MOON: deep matte black with subtle crater "
        "texture, blocking the sun, perfect disc darkness across entire body. "
        "CONNECTED ART: Model B slightly overlapping Model A creates perfect solar eclipse. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME pure black studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black studio, cosmic atmosphere, both models in same space slightly overlapping",
    "lighting": "golden corona glow from Model A radiating around Model B creating eclipse halo effect",
    "style": "solar eclipse art editorial, celestial event living sculpture, astronomical fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_human_shadow_bodypaint",
    "subject": "Two stunning female models in same spotlight studio, one model as person one as her shadow",
    "body": "Model A: living person in full color. Model B: her shadow in pure black silhouette",
    "outfit": (
        "Model A: full body paint art — LIVING PERSON: vibrant full color botanical flowers "
        "and nature painted across entire body, warm living colors. "
        "Model B: full body paint art — THE SHADOW: pure matte black silhouette, "
        "exact mirror shape of Model A but completely black, shadow texture across entire body. "
        "CONNECTED ART: together one is the person, one is the living shadow. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME dramatic spotlight studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dramatic spotlight studio, strong directional light creating shadow effect, both in same space",
    "lighting": "single strong spotlight creating real shadow effect, living vs shadow contrast",
    "style": "shadow art editorial, person and shadow concept, surrealist fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_tiger_split_bodypaint",
    "subject": "Two stunning female models standing close together in same jungle, their bodies forming one complete tiger",
    "body": "Model A: left half of tiger. Model B: right half. Together one complete tiger",
    "outfit": (
        "Model A: full body paint art — LEFT HALF of Bengal tiger: orange black white "
        "stripes covering right side of her body, tiger face elements on her torso, "
        "seamlessly connecting to Model B at center. "
        "Model B: full body paint art — RIGHT HALF of same tiger: mirror stripe pattern "
        "on her left side, completing the full tiger body. "
        "CONNECTED ART: together they form one complete Bengal tiger. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME jungle background"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "lush jungle with dappled light, both models in same tropical forest space",
    "lighting": "warm jungle golden hour light falling equally on both",
    "style": "wildlife connected art editorial, tiger body art concept, nature fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_starry_night_split_bodypaint",
    "subject": "Two stunning female models standing side by side in same minimal studio, together forming Van Gogh Starry Night",
    "body": "Model A: left panel of painting. Model B: right panel. Together complete masterpiece",
    "outfit": (
        "Model A: full body paint art — LEFT HALF of Van Gogh Starry Night: swirling "
        "blue night sky with stars, cypress tree on left edge, village below, "
        "characteristic Van Gogh brushstroke texture across entire body. "
        "Model B: full body paint art — RIGHT HALF of Starry Night: continuation of "
        "swirling sky, moon and stars, village continuing, same Van Gogh style connecting. "
        "CONNECTED ART: together they recreate complete Starry Night. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME minimal studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "minimal clean studio, both models in same space, Van Gogh blue atmosphere",
    "lighting": "soft even art studio light, blue starry night atmosphere",
    "style": "Van Gogh living painting editorial, post-impressionist body art, fine art fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "duo_peacock_split_bodypaint",
    "subject": "Two stunning female models standing close side by side in same garden, together forming complete peacock",
    "body": "Model A: left peacock wing. Model B: right peacock wing. Together one magnificent peacock",
    "outfit": (
        "Model A: full body paint art — LEFT WING of peacock: iridescent teal blue green "
        "peacock feathers with eye patterns, plumage spread across her entire body "
        "flowing outward, connecting at center. "
        "Model B: full body paint art — RIGHT WING of same peacock: mirror peacock "
        "plumage, iridescent eye feathers, completing the full peacock display. "
        "CONNECTED ART: together they form one complete peacock in full display. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "SAME botanical garden"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "lush botanical garden, flowers and greenery, both models in same garden space",
    "lighting": "soft warm garden light, iridescent peacock colors glowing on both",
    "style": "peacock connected art editorial, bird plumage body art, nature fashion photography",
    "quality": QUALITY,
})

# ──────────────────────────────────────────────────────────
# G4 연결형 트리오 추가 (6종)
# ──────────────────────────────────────────────────────────

PRESETS.append({
    "name": "trio_last_supper_bodypaint",
    "subject": "Three stunning female models standing in a row in same art gallery forming Leonardo da Vinci Last Supper triptych",
    "body": "Left panel, center panel, right panel of the Last Supper, all in same gallery",
    "outfit": (
        "Model A: full body paint art — LEFT THIRD of Last Supper: disciples from left "
        "section, da Vinci style figures and architectural details across entire body. "
        "Model B: full body paint art — CENTER THIRD: Christ figure at center, central "
        "architectural window, most important section across entire body. "
        "Model C: full body paint art — RIGHT THIRD: right disciples, right architecture "
        "completing the full Last Supper composition. "
        "CONNECTED ART: three bodies form complete Last Supper painting. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME art gallery"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "grand art gallery with Renaissance architectural details, all three in same space",
    "lighting": "warm Renaissance golden light, museum spotlight for all three",
    "style": "da Vinci living triptych editorial, Renaissance body art, fine art fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_rainbow_arc_bodypaint",
    "subject": "Three stunning female models standing together under same outdoor sky, their bodies forming one complete rainbow arc",
    "body": "Model A: warm spectrum. Model B: center peak. Model C: cool spectrum. Together one rainbow",
    "outfit": (
        "Model A: full body paint art — WARM RAINBOW: red orange yellow spectrum "
        "in rainbow arc pattern across entire body, warm end of spectrum. "
        "Model B: full body paint art — RAINBOW CENTER: yellow green at peak, "
        "brightest most intense rainbow colors across entire body. "
        "Model C: full body paint art — COOL RAINBOW: blue indigo violet spectrum "
        "in rainbow arc pattern completing the other end. "
        "CONNECTED ART: together they form one complete rainbow arc. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE under SAME sky after rain"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "outdoor field after rain, fresh sky, all three under same rainbow sky",
    "lighting": "fresh clean light after rain, rainbow atmosphere for all three",
    "style": "rainbow arc living art editorial, spectrum body art concept, nature fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_milky_way_panorama_bodypaint",
    "subject": "Three stunning female models standing in a row in same black studio, together forming complete Milky Way panorama",
    "body": "Model A: left galaxy arm. Model B: galactic center. Model C: right arm. Together full Milky Way",
    "outfit": (
        "Model A: full body paint art — LEFT ARM of Milky Way: outer spiral arm stars, "
        "deep space nebula, star clusters, dark blues purples across entire body. "
        "Model B: full body paint art — GALACTIC CENTER: brightest densest star region, "
        "golden white core, maximum star density across entire body. "
        "Model C: full body paint art — RIGHT ARM of Milky Way: opposite spiral arm "
        "mirroring left side, completing the panoramic galaxy. "
        "CONNECTED ART: three bodies form complete Milky Way panorama. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME black cosmic studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black cosmic studio, star field, all three in same deep space atmosphere",
    "lighting": "cosmic bioluminescent glow from galaxy paintings, same dark cosmic atmosphere",
    "style": "Milky Way panorama living art, cosmic body art editorial, astronomical fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_coral_reef_zones_bodypaint",
    "subject": "Three stunning female models standing together in same blue studio forming complete coral reef ecosystem",
    "body": "Model A: sandy floor. Model B: mid reef. Model C: surface zone. Together complete reef",
    "outfit": (
        "Model A: full body paint art — SANDY REEF FLOOR: sand dollar patterns, "
        "bottom-dwelling creatures, sea anemone, warm sandy tones across entire body. "
        "Model B: full body paint art — MID REEF ZONE: dense coral formations, "
        "clownfish, sea turtles, vivid rainbow coral colors across entire body. "
        "Model C: full body paint art — SURFACE ZONE: sunlit shallow water, "
        "tropical fish, bright turquoise light patterns across entire body. "
        "CONNECTED ART: three bodies form complete reef vertical cross-section. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME blue underwater studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "deep blue underwater studio, coral reef atmosphere, all three in same aquatic space",
    "lighting": "Model A in warm sandy tones, Model B in vivid reef light, Model C in bright surface light",
    "style": "coral reef ecosystem editorial, underwater art concept, National Geographic luxury fashion",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_creation_of_adam_bodypaint",
    "subject": "Three stunning female models in same art gallery forming Michelangelo Creation of Adam triptych",
    "body": "Model A: God section. Model B: the space between. Model C: Adam section. Same gallery",
    "outfit": (
        "Model A: full body paint art — GOD side of Creation of Adam: Michelangelo's "
        "God figure, angels surrounding, Sistine ceiling style across entire body. "
        "Model B: full body paint art — THE DIVINE SPACE: the famous gap between "
        "fingers, heavenly clouds, the moment of creation across entire body. "
        "Model C: full body paint art — ADAM side: Michelangelo's Adam reclining "
        "figure, earthly tones, the receiving hand across entire body. "
        "CONNECTED ART: three bodies recreate complete Creation of Adam. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME Sistine-inspired gallery"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "grand classical gallery with vaulted ceiling, all three in same Renaissance space",
    "lighting": "warm divine golden light for all three, Sistine Chapel atmosphere",
    "style": "Michelangelo living triptych, Sistine Chapel body art, Renaissance fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "trio_poles_and_equator_bodypaint",
    "subject": "Three stunning female models standing together in same studio representing Earth climate zones",
    "body": "Model A: North Pole. Model B: tropical equator. Model C: South Pole. All in same space",
    "outfit": (
        "Model A: full body paint art — NORTH POLE: aurora borealis, polar ice, "
        "Arctic fox and polar bear motifs, ice white blue silver across entire body. "
        "Model B: full body paint art — TROPICAL EQUATOR: lush rainforest, "
        "tropical birds and flowers, vivid green orange yellow across entire body. "
        "Model C: full body paint art — SOUTH POLE: Antarctic ice shelf, "
        "penguins and orcas, deep blue white patterns across entire body. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL THREE in SAME neutral studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "clean neutral studio, all three in same space, contrast from body paint only",
    "lighting": "cool icy for Models A and C, warm tropical for Model B, same studio",
    "style": "Earth climate zones editorial, geographical body art concept, science fashion photography",
    "quality": QUALITY,
})

# ──────────────────────────────────────────────────────────
# 4인 (QUAD) 프리셋 (5종)
# ──────────────────────────────────────────────────────────

PRESETS.append({
    "name": "quad_four_seasons_bodypaint",
    "subject": "Four stunning female models standing in a row in same outdoor garden, representing four seasons",
    "body": "Model A: spring. Model B: summer. Model C: autumn. Model D: winter. All in same garden",
    "outfit": (
        "Model A: full body paint art — SPRING: cherry blossoms, fresh green shoots, "
        "soft pink lavender botanical spring patterns across entire body. "
        "Model B: full body paint art — SUMMER: sunflowers, tropical heat, "
        "vivid orange yellow green summer patterns across entire body. "
        "Model C: full body paint art — AUTUMN: maple leaves, harvest colors, "
        "deep orange red brown golden autumn patterns across entire body. "
        "Model D: full body paint art — WINTER: snowflakes, bare branches, "
        "silver white ice crystal patterns across entire body. "
        "All four: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL FOUR in SAME garden setting"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "beautiful garden with seasonal elements, all four models in same outdoor space wide composition",
    "lighting": "soft natural light for all four, each with subtle seasonal color temperature",
    "style": "four seasons complete editorial, seasonal body art, Vogue nature fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "quad_four_elements_bodypaint",
    "subject": "Four stunning female models in dramatic formation in same dark studio, four classical elements",
    "body": "Model A: fire. Model B: water. Model C: earth. Model D: air/wind. All in same dramatic space",
    "outfit": (
        "Model A: full body paint art — FIRE element: blazing flames, ember patterns, "
        "volcanic crimson orange gold across entire body. "
        "Model B: full body paint art — WATER element: ocean waves, rain drops, "
        "flowing currents, deep blue aqua across entire body. "
        "Model C: full body paint art — EARTH element: stone and soil textures, "
        "tree roots, deep brown green earthy patterns across entire body. "
        "Model D: full body paint art — AIR/WIND element: cloud formations, "
        "wind currents, light white silver grey across entire body. "
        "All four: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL FOUR in SAME dramatic dark studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "dramatic dark studio, wide composition, all four models in same powerful space",
    "lighting": "each element lighting: fire warm glow, water cool blue, earth natural, air diffused white",
    "style": "four elements complete editorial, classical elements body art, mythology fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "quad_four_directions_bodypaint",
    "subject": "Four stunning female models in compass formation in same Asian art studio, Korean four guardian deities",
    "body": "East: blue dragon. West: white tiger. South: red phoenix. North: black turtle. All in same space",
    "outfit": (
        "Model A EAST: full body paint art — BLUE DRAGON (청룡): East guardian, "
        "blue green dragon scales and cloud patterns across entire body. "
        "Model B WEST: full body paint art — WHITE TIGER (백호): West guardian, "
        "white silver tiger stripes and fierce patterns across entire body. "
        "Model C SOUTH: full body paint art — RED PHOENIX (주작): South guardian, "
        "crimson red gold phoenix feathers and flame patterns across entire body. "
        "Model D NORTH: full body paint art — BLACK TURTLE (현무): North guardian, "
        "dark serpent turtle shell and water patterns across entire body. "
        "All four: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL FOUR in SAME Asian art studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "elegant Asian art studio with traditional decorative elements, wide composition, all four in same space",
    "lighting": "each guardian color lighting: blue east, white west, red south, dark north",
    "style": "Korean four guardian deities editorial, Asian mythology body art, cultural fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "quad_four_seasons_klimt_bodypaint",
    "subject": "Four stunning female models standing in a row in same art nouveau gallery, Klimt four seasons triptych extended",
    "body": "Four panels of Klimt seasonal cycle, all in same Klimt gallery",
    "outfit": (
        "Model A: full body paint art — KLIMT SPRING: gold leaf patterns with spring "
        "flowers embedded, Klimt's decorative spring panel across entire body. "
        "Model B: full body paint art — KLIMT SUMMER: golden baroque summer patterns, "
        "Klimt's summer opulence across entire body. "
        "Model C: full body paint art — KLIMT AUTUMN: rich harvest gold patterns, "
        "Klimt's autumn mosaic across entire body. "
        "Model D: full body paint art — KLIMT WINTER: silver and dark gold winter "
        "patterns, Klimt's winter cycle across entire body. "
        "All four: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL FOUR in SAME art nouveau gallery"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "grand art nouveau gallery with golden ornamental details, wide composition, all four in same space",
    "lighting": "warm golden museum lighting for all four, Klimt's characteristic golden glow",
    "style": "Klimt four seasons complete editorial, Vienna Secession living art, fine art fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "quad_rgba_spectrum_bodypaint",
    "subject": "Four stunning female models standing in a row in same black studio, four bold color spectrum",
    "body": "Model A: red. Model B: gold. Model C: green. Model D: blue. All in same dark space",
    "outfit": (
        "Model A: full body paint art — DEEP RED with rose and fire patterns, "
        "rich crimson across entire body. "
        "Model B: full body paint art — WARM GOLD with sun and wheat patterns, "
        "radiant golden across entire body. "
        "Model C: full body paint art — FOREST GREEN with leaf and nature patterns, "
        "lush emerald across entire body. "
        "Model D: full body paint art — ROYAL BLUE with wave and geometric patterns, "
        "deep cobalt across entire body. "
        "All four: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL FOUR in SAME black studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black studio, wide composition showing all four, same dark seamless space",
    "lighting": "each model lit by matching color spotlight, colors blending at edges between models",
    "style": "color spectrum editorial, four color body art, bold fashion photography",
    "quality": QUALITY,
})

# ──────────────────────────────────────────────────────────
# 5인 (QUINT) 프리셋 (4종)
# ──────────────────────────────────────────────────────────

PRESETS.append({
    "name": "quint_five_continents_bodypaint",
    "subject": "Five stunning female models standing in a row in same neutral museum space, five continents",
    "body": "Asia, Europe, Africa, Americas, Oceania — five models five continents in same space",
    "outfit": (
        "Model A: full body paint art — ASIA: Korean dancheong and Chinese dragon, "
        "Eastern art patterns, gold red across entire body. "
        "Model B: full body paint art — EUROPE: Renaissance fresco and Celtic knotwork, "
        "classical Western art, cream gold across entire body. "
        "Model C: full body paint art — AFRICA: tribal geometric and Ndebele patterns, "
        "bold African art, earth tones across entire body. "
        "Model D: full body paint art — AMERICAS: Mayan calendar and Native American "
        "patterns, terracotta and turquoise across entire body. "
        "Model E: full body paint art — OCEANIA: Maori tattoo and Aboriginal dot art, "
        "Pacific cultural patterns across entire body. "
        "All five: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL FIVE in SAME wide museum space"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "grand world culture museum, wide panoramic composition, all five in same space",
    "lighting": "warm museum lighting for all five, world heritage atmosphere",
    "style": "five continents world culture editorial, global heritage body art, anthropological fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "quint_five_elements_asia_bodypaint",
    "subject": "Five stunning female models in a row in same Asian studio, five elements of Eastern philosophy",
    "body": "Wood, Fire, Earth, Metal, Water — five Asian elements in same space",
    "outfit": (
        "Model A: full body paint art — WOOD (목): tree growth, bamboo, spring green, "
        "forest patterns across entire body. "
        "Model B: full body paint art — FIRE (화): flames, summer heat, crimson red "
        "orange patterns across entire body. "
        "Model C: full body paint art — EARTH (토): soil clay, harvest, late summer "
        "golden brown patterns across entire body. "
        "Model D: full body paint art — METAL (금): gold silver chrome, autumn crisp, "
        "metallic patterns across entire body. "
        "Model E: full body paint art — WATER (수): ocean flow, winter deep blue, "
        "fluid wave patterns across entire body. "
        "All five: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL FIVE in SAME Asian studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "elegant Asian studio with traditional elements, wide panoramic composition, all five together",
    "lighting": "each element's color lighting, same warm Asian atmosphere for all five",
    "style": "five elements Eastern philosophy editorial, Asian cultural body art, philosophy fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "quint_rainbow_five_bodypaint",
    "subject": "Five stunning female models in a row in same black studio forming complete rainbow spectrum",
    "body": "Red, orange-yellow, green, blue, violet — five rainbow bands in same dark space",
    "outfit": (
        "Model A: full body paint art — RED: deep crimson red with rose patterns, "
        "rich red tones across entire body. "
        "Model B: full body paint art — ORANGE-YELLOW: warm amber orange with sun "
        "and fire patterns across entire body. "
        "Model C: full body paint art — GREEN: emerald green with nature leaf patterns "
        "across entire body. "
        "Model D: full body paint art — BLUE: deep cobalt blue with wave patterns "
        "across entire body. "
        "Model E: full body paint art — VIOLET: deep purple violet with cosmic "
        "nebula patterns across entire body. "
        "All five: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL FIVE in SAME black studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "pure black studio, wide panoramic composition showing all five rainbow models",
    "lighting": "each model lit by matching spectrum spotlight, rainbow colors blending across all five",
    "style": "rainbow spectrum complete editorial, five color body art, vibrant fashion photography",
    "quality": QUALITY,
})

PRESETS.append({
    "name": "quint_five_oceans_bodypaint",
    "subject": "Five stunning female models in a row in same blue studio, five world oceans",
    "body": "Pacific, Atlantic, Indian, Arctic, Antarctic — five oceans in same aquatic space",
    "outfit": (
        "Model A: full body paint art — PACIFIC OCEAN: deepest darkest blue, "
        "powerful typhoon waves, Pacific marine life across entire body. "
        "Model B: full body paint art — ATLANTIC OCEAN: navy blue, shipping routes, "
        "Atlantic whale and dolphin patterns across entire body. "
        "Model C: full body paint art — INDIAN OCEAN: warm turquoise emerald, "
        "tropical monsoon patterns across entire body. "
        "Model D: full body paint art — ARCTIC OCEAN: pale ice blue white, "
        "polar bear and aurora patterns across entire body. "
        "Model E: full body paint art — ANTARCTIC OCEAN: deep cold blue silver, "
        "iceberg and penguin patterns across entire body. "
        "All five: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric. "
        "ALL FIVE in SAME blue studio"
    ),
    "material": "body paint pigment applied directly on bare skin",
    "environment": "deep blue panoramic studio, all five models in same wide oceanic space",
    "lighting": "cool blue ocean lighting for all five, gradient from warm Pacific to cold Antarctic",
    "style": "five oceans world editorial, ocean body art panorama, maritime fashion photography",
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
    categories = {
        "G1 대비형 듀오 추가": [p for p in PRESETS if p["name"].startswith("duo_") and any(k in p["name"] for k in ["east_and_west","macro_and_micro","ancient_and_future","poison","storm_and_calm","deep_sea"])],
        "G2 대비형 트리오 추가": [p for p in PRESETS if p["name"].startswith("trio_") and any(k in p["name"] for k in ["sun_moon","three_oceans","three_civilizations","fire_water_earth","angel_human","three_big"])],
        "G3 연결형 듀오 추가": [p for p in PRESETS if p["name"].startswith("duo_") and any(k in p["name"] for k in ["dna","solar_eclipse","human_shadow","tiger_split","starry_night","peacock"])],
        "G4 연결형 트리오 추가": [p for p in PRESETS if p["name"].startswith("trio_") and any(k in p["name"] for k in ["last_supper","rainbow_arc","milky_way","coral_reef","creation_of_adam","poles"])],
        "4인 QUAD": [p for p in PRESETS if p["name"].startswith("quad_")],
        "5인 QUINT": [p for p in PRESETS if p["name"].startswith("quint_")],
    }

    total = sum(len(v) for v in categories.values())
    print(f"\n🎨 멀티 바디페인팅 v3 확장 — {total}종\n")
    for cat, items in categories.items():
        print(f"📁 {cat} ({len(items)}종):")
        for p in items:
            print(f"   - {p['name']}")
        print()

    print(f"기존 24종 + 신규 {total}종 = 총 {24 + total}종")
    answer = input("\n저장하시겠습니까? (y/n): ")
    if answer.lower() == 'y':
        saved = save_presets(PRESETS, PRESETS_DIR)
        print(f"\n✅ {len(saved)}개 프리셋 저장 완료")
    else:
        print("저장 취소됨")
