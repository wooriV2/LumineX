"""
generate_multi_bodypaint_presets.py
멀티 바디페인팅 프리셋 JSON 24종 자동 생성
실행: python generate_multi_bodypaint_presets.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path("C:/Dev/LumineX/presets")

# ──────────────────────────────────────────────────────────
# 공통 퀄리티 suffix
# ──────────────────────────────────────────────────────────
QUALITY = "ultra-sharp, 8K, professional editorial photography, hyperrealistic skin texture"

# ──────────────────────────────────────────────────────────
# 듀오 인코딩 헬퍼
# 두 모델 정보를 subject/body/outfit에 인코딩
# (builders.py 수정 없이 기존 바디페인팅 분기 활용)
# ──────────────────────────────────────────────────────────

def duo(name, subject, body, outfit, environment, lighting, style, extras=""):
    return {
        "name": name,
        "subject": subject,
        "body": body,
        "outfit": outfit,          # _is_bodypaint() 트리거 키워드 포함
        "material": "body paint pigment applied directly on bare skin",
        "environment": environment,
        "lighting": lighting,
        "style": style,
        "quality": QUALITY,
        "extras": extras,
    }

def trio(name, subject, body, outfit, environment, lighting, style, extras=""):
    return {
        "name": name,
        "subject": subject,
        "body": body,
        "outfit": outfit,
        "material": "body paint pigment applied directly on bare skin",
        "environment": environment,
        "lighting": lighting,
        "style": style,
        "quality": QUALITY,
        "extras": extras,
    }

# ──────────────────────────────────────────────────────────
# G1 — 대비형 듀오 (6종)
# ──────────────────────────────────────────────────────────

PRESETS = []

PRESETS.append(duo(
    name="duo_fire_and_ice_bodypaint",
    subject="Two stunning female models standing side by side, Model A and Model B, dramatic contrast",
    body="Model A: slim toned athletic build. Model B: identical physique, perfect symmetry pair",
    outfit=(
        "Model A: full body paint art — blazing fire and lava, orange red crimson flame patterns "
        "covering entire body, molten magma veins, volcanic ember glow. "
        "Model B: full body paint art — arctic ice and frost crystals, deep blue white silver "
        "patterns, crystalline ice formations, frozen breath texture. "
        "Both: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="split volcanic-glacier landscape: left half volcanic crater glowing orange, right half arctic ice cave blue, dramatic divide at center",
    lighting="dual split lighting: warm orange fire glow from left, cold blue ice glow from right, dramatic contrast meeting at center",
    style="high concept fashion editorial, dueling elements art photography, Vogue Italia avant-garde",
))

PRESETS.append(duo(
    name="duo_day_and_night_bodypaint",
    subject="Two stunning female models standing back to back, elegant complementary pair",
    body="Model A: golden radiant presence. Model B: silver midnight presence",
    outfit=(
        "Model A: full body paint art — golden sun rays, daylight sky, clouds and sunbeams "
        "painted across entire body, warm golden yellow orange palette. "
        "Model B: full body paint art — deep night sky, silver moon, stars and galaxy "
        "painted across entire body, midnight blue silver white palette. "
        "Both: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="twilight horizon at the exact moment of day-night transition, gradient sky from gold to midnight blue",
    lighting="Model A lit by warm golden sunlight, Model B lit by cool silver moonlight, meeting at center twilight",
    style="celestial duality editorial, Harper's Bazaar conceptual, day-night contrast art photography",
))

PRESETS.append(duo(
    name="duo_bloom_and_void_bodypaint",
    subject="Two stunning female models, one vibrant, one minimal, extreme contrast editorial",
    body="Model A: lush colorful presence. Model B: stark minimal presence",
    outfit=(
        "Model A: full body paint art — riotous flower garden explosion, every type of flower "
        "blooming across entire body, vivid color botanical illustration painted on skin. "
        "Model B: full body paint art — pure black void with subtle deep space darkness, "
        "anti-color absence, deep matte black with faint cosmic depth. "
        "Both: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="split minimalist white studio with abstract floral garden on left, pure black void on right",
    lighting="bright soft botanical garden light on Model A, absolute darkness with single rim light on Model B",
    style="maximum contrast conceptual editorial, existence vs void art photography, Alexander McQueen avant-garde",
))

PRESETS.append(duo(
    name="duo_gold_and_shadow_bodypaint",
    subject="Two stunning female models, one in light, one in shadow, art history editorial",
    body="Model A: baroque luminous presence. Model B: chiaroscuro shadow presence",
    outfit=(
        "Model A: full body paint art — Gustav Klimt gold leaf patterns, Byzantine mosaics, "
        "ornate golden geometric shapes, intricate gold ornamentation across entire body. "
        "Model B: full body paint art — deep black ink calligraphy, dramatic shadow painting, "
        "Rembrandt-style chiaroscuro patterns, ink wash darkness across entire body. "
        "Both: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="dark baroque gallery interior, gilt-framed paintings, candlelit opulence",
    lighting="dramatic chiaroscuro: single golden spotlight on Model A, deep shadow enveloping Model B",
    style="Klimt meets Rembrandt editorial, art history duality, Numéro magazine avant-garde",
))

PRESETS.append(duo(
    name="duo_ocean_and_desert_bodypaint",
    subject="Two stunning female models side by side, elemental nature contrast editorial",
    body="Model A: fluid ocean presence. Model B: sculpted desert presence",
    outfit=(
        "Model A: full body paint art — deep ocean waves, coral reef patterns, bioluminescent "
        "sea creatures, turquoise blue teal navy ocean depths painted across entire body. "
        "Model B: full body paint art — Sahara sand dunes, cracked desert earth, "
        "golden sand patterns, sun-bleached warm ochre terracotta across entire body. "
        "Both: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="dramatic nature divide: turquoise ocean on left, red desert dunes on right, horizon line at center",
    lighting="Model A in cool ocean blue underwater glow, Model B in harsh desert golden hour direct sun",
    style="elemental nature editorial, National Geographic luxury fashion, Vogue environmental concept",
))

PRESETS.append(duo(
    name="duo_circuit_and_nature_bodypaint",
    subject="Two stunning female models facing each other, technology vs nature tension editorial",
    body="Model A: geometric precision presence. Model B: organic flowing presence",
    outfit=(
        "Model A: full body paint art — printed circuit board patterns, neon green blue "
        "electronic pathways, microchip grids, LED light effects, cyberpunk tech patterns "
        "painted across entire body. "
        "Model B: full body paint art — deep forest moss and lichen, tree bark textures, "
        "fern and vine botanicals, earth green brown patterns painted across entire body. "
        "Both: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="abandoned industrial space reclaimed by nature: concrete walls with vines growing, server racks with plants",
    lighting="Model A in cold neon electronic blue-green glow, Model B in warm dappled forest sunlight",
    style="technology vs nature conceptual editorial, cyberpunk botanical art photography",
))

# ──────────────────────────────────────────────────────────
# G2 — 대비형 트리오 (6종)
# ──────────────────────────────────────────────────────────

PRESETS.append(trio(
    name="trio_rgb_trinity_bodypaint",
    subject="Three stunning female models standing in a row, primary color trinity editorial",
    body="Model A: pure energy. Model B: pure energy. Model C: pure energy. All three identical athletic builds creating perfect color symmetry",
    outfit=(
        "Model A: full body paint art — pure saturated RED across entire body, rich crimson "
        "scarlet body paint, vivid red gradient. "
        "Model B: full body paint art — pure saturated GREEN across entire body, emerald "
        "forest green body paint, vivid green gradient. "
        "Model C: full body paint art — pure saturated BLUE across entire body, cobalt "
        "royal blue body paint, vivid blue gradient. "
        "All three: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="pure black minimalist studio, complete darkness emphasizing color purity",
    lighting="three separate colored spotlights: red for Model A, green for Model B, blue for Model C, colors mixing where models overlap",
    style="primary color art installation editorial, RGB light theory, Andy Warhol meets body art photography",
))

PRESETS.append(trio(
    name="trio_earth_water_sky_bodypaint",
    subject="Three stunning female models in sacred triangle formation, elemental trinity",
    body="Model A at center: grounded earthy presence. Model B left: fluid water presence. Model C right: ethereal sky presence",
    outfit=(
        "Model A: full body paint art — rich earth and soil, brown ochre clay terracotta "
        "patterns, ancient rock formations painted across entire body. "
        "Model B: full body paint art — flowing water, ocean waves, river currents, "
        "turquoise blue flowing patterns painted across entire body. "
        "Model C: full body paint art — open sky, clouds, atmospheric light, "
        "pale blue white gradient, sunset colors painted across entire body. "
        "All three: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="dramatic nature landscape: cliff edge with ocean below and sky above, all three elements visible",
    lighting="natural outdoor golden hour light, warm ambient glow unifying all three models",
    style="elemental goddess trilogy, mythology editorial, Vogue Italia conceptual art photography",
))

PRESETS.append(trio(
    name="trio_past_present_future_bodypaint",
    subject="Three stunning female models representing three eras of time, timeline editorial",
    body="Model A: ancient classical presence. Model B: contemporary sleek presence. Model C: futuristic otherworldly presence",
    outfit=(
        "Model A: full body paint art — ancient Egyptian hieroglyphs, Byzantine mosaic "
        "patterns, classical mythology motifs painted across entire body in gold ochre. "
        "Model B: full body paint art — modern geometric patterns, clean contemporary "
        "lines, current art movement design painted across entire body in black white grey. "
        "Model C: full body paint art — futuristic circuit patterns, holographic iridescent "
        "neon cyberpunk tech art painted across entire body in electric blue silver. "
        "All three: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="surreal infinite corridor with ancient ruins on left, modern gallery at center, futuristic architecture on right",
    lighting="ancient warm torch light, modern clean white light, futuristic neon glow, each lighting their respective model",
    style="time continuum conceptual editorial, past present future art photography",
))

PRESETS.append(trio(
    name="trio_predator_prey_apex_bodypaint",
    subject="Three stunning female models in dynamic wildlife triangle, nature hierarchy editorial",
    body="Model A: feline predator grace. Model B: swift prey elegance. Model C: aerial apex presence",
    outfit=(
        "Model A: full body paint art — leopard and cheetah spots, feline predator "
        "patterns, spotted rosettes across entire body, tawny gold black. "
        "Model B: full body paint art — deer and gazelle patterns, delicate fawn "
        "markings, gentle spotted deer texture across entire body, soft brown cream. "
        "Model C: full body paint art — eagle and hawk feather patterns, raptor wing "
        "markings, fierce bird of prey plumage across entire body, dark brown white. "
        "All three: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="dramatic savanna at golden hour, acacia tree silhouettes, vast African sky",
    lighting="warm African golden hour sunlight, dramatic shadows, natural wildlife photography lighting",
    style="wildlife editorial, National Geographic luxury fashion, nature hierarchy art photography",
))

PRESETS.append(trio(
    name="trio_ink_gold_chrome_bodypaint",
    subject="Three stunning female models in minimalist studio, material trinity editorial",
    body="Model A: dark ink presence. Model B: warm gold presence. Model C: cold chrome presence",
    outfit=(
        "Model A: full body paint art — deep black sumi ink calligraphy, Japanese ink wash "
        "painting patterns, fluid black strokes across entire body on pale skin. "
        "Model B: full body paint art — hammered gold leaf, Byzantine gold mosaic, "
        "warm gilded patterns, liquid gold across entire body. "
        "Model C: full body paint art — chrome silver mirror finish, liquid metal "
        "reflective patterns, futuristic chrome across entire body. "
        "All three: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="minimal pure white studio with polished floor reflecting all three models",
    lighting="perfect three-point studio lighting emphasizing ink darkness, gold warmth, chrome reflection respectively",
    style="materials trilogy editorial, Vogue minimalist conceptual, fine art body photography",
))

PRESETS.append(trio(
    name="trio_season_trinity_bodypaint",
    subject="Three stunning female models representing spring summer winter seasons",
    body="Model A: spring blossoming presence. Model B: summer heat presence. Model C: winter frost presence",
    outfit=(
        "Model A: full body paint art — cherry blossom sakura, spring flowers in bloom, "
        "soft pink peach lavender botanical spring patterns painted across entire body. "
        "Model B: full body paint art — tropical flowers, summer sun, ocean waves, "
        "vibrant coral orange yellow green summer patterns painted across entire body. "
        "Model C: full body paint art — snowflakes, ice crystals, bare winter branches, "
        "silver white pale blue frost patterns painted across entire body. "
        "All three: painted directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="triptych studio setup with spring garden, summer beach, winter snow backdrop panels",
    lighting="Model A in soft warm spring light, Model B in bright summer sun, Model C in cold blue winter light",
    style="seasons editorial, botanical art photography, Vogue seasonal concept",
))

# ──────────────────────────────────────────────────────────
# G3 — 연결형 듀오 (6종)
# 두 몸을 합치면 하나의 완성된 이미지
# ──────────────────────────────────────────────────────────

PRESETS.append(duo(
    name="duo_butterfly_split_bodypaint",
    subject="Two stunning female models standing close together side by side, their bodies forming one complete butterfly when viewed together",
    body="Model A: left half of butterfly. Model B: right half of butterfly. Bodies touching at center to complete the image",
    outfit=(
        "Model A body paint: LEFT WING of a giant monarch butterfly — orange black white "
        "wing pattern precisely covering the right side of her body (facing center), "
        "seamlessly connecting to Model B. "
        "Model B body paint: RIGHT WING of the same giant monarch butterfly — mirror image "
        "of wing pattern precisely covering the left side of her body (facing center), "
        "completing the full butterfly when viewed together. "
        "CONNECTED ART: when both models stand together their painted bodies form ONE complete "
        "butterfly. Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="lush flower garden with natural bokeh, spring meadow, flowers at their feet",
    lighting="soft natural garden light, gentle golden hour glow, warm botanical atmosphere",
    style="connected body art editorial, nature symmetry concept, Vogue Italia botanical",
))

PRESETS.append(duo(
    name="duo_yin_yang_merge_bodypaint",
    subject="Two stunning female models standing back to back forming a perfect yin yang symbol",
    body="Model A: light yang energy. Model B: dark yin energy. Perfect philosophical complementarity",
    outfit=(
        "Model A: full body paint art — pure WHITE with one BLACK circle dot painted on "
        "body, representing yang half of yin-yang, white curves flowing to match Model B. "
        "Model B: full body paint art — pure BLACK with one WHITE circle dot painted on "
        "body, representing yin half of yin-yang, black curves mirroring Model A. "
        "CONNECTED ART: when viewed together their bodies form the complete yin-yang taijitu symbol. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="zen minimalist Japanese garden, raked sand, bamboo, peaceful atmosphere",
    lighting="perfectly even diffused studio light, no shadows to maintain graphic clarity",
    style="philosophical duality editorial, Eastern philosophy art concept, minimalist fine art photography",
))

PRESETS.append(duo(
    name="duo_world_map_bodypaint",
    subject="Two stunning female models standing side by side, their bodies forming one complete world map",
    body="Model A: Eastern hemisphere presence. Model B: Western hemisphere presence",
    outfit=(
        "Model A: full body paint art — detailed map of EASTERN HEMISPHERE: Europe Africa Asia "
        "Australia painted across entire body, continents in terracotta blue ocean background, "
        "latitude longitude lines, cartographic detail. "
        "Model B: full body paint art — detailed map of WESTERN HEMISPHERE: Americas "
        "painted across entire body, North South America in terracotta blue ocean, "
        "cartographic precision connecting seamlessly to Model A. "
        "CONNECTED ART: together they form one complete world map. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="minimalist blue studio suggesting ocean, celestial globe atmosphere",
    lighting="soft even cartographic studio light, clean map-reading clarity",
    style="cartography art editorial, world geography concept photography",
))

PRESETS.append(duo(
    name="duo_klimt_tree_bodypaint",
    subject="Two stunning female models standing side by side, their bodies forming Klimt's Tree of Life",
    body="Model A: left half of the tree. Model B: right half of the tree. Together: one complete Klimt masterpiece",
    outfit=(
        "Model A: full body paint art — LEFT HALF of Gustav Klimt's Tree of Life: "
        "swirling golden branches, jeweled ornaments, spiral tendrils, Klimt's distinctive "
        "gold leaf and mosaic style painted across entire body, right edge seamlessly connects. "
        "Model B: full body paint art — RIGHT HALF of same Klimt Tree of Life: "
        "mirror swirling branches, jeweled elements, perfect continuation of Model A's "
        "painting. CONNECTED ART: together they form one complete Tree of Life. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="dark art nouveau gallery with golden ornamental details, Viennese Secession atmosphere",
    lighting="warm golden gallery lighting, Klimt's characteristic gold leaf glow",
    style="Klimt body art editorial, Vienna Secession living painting, fine art photography",
))

PRESETS.append(duo(
    name="duo_galaxy_split_bodypaint",
    subject="Two stunning female models standing back to back forming one complete spiral galaxy",
    body="Model A: near galaxy arm. Model B: far galaxy arm. Together they complete the spiral",
    outfit=(
        "Model A: full body paint art — RIGHT SIDE of spiral galaxy: spiral arm of stars "
        "and nebula, deep space blues purples, star clusters, cosmic dust painted "
        "across entire body, galaxy center at sternum. "
        "Model B: full body paint art — LEFT SIDE of same spiral galaxy: opposite spiral "
        "arm, mirrored star patterns, cosmic continuation painted across entire body. "
        "CONNECTED ART: back to back they form one complete Milky Way spiral galaxy. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="pure black studio with subtle star field projection, deep space atmosphere",
    lighting="bioluminescent cosmic glow from the painted galaxy itself, purple blue constellation lighting",
    style="cosmic art editorial, NASA astronomy meets fashion, deep space concept photography",
))

PRESETS.append(duo(
    name="duo_wave_hokusai_bodypaint",
    subject="Two stunning female models side by side forming Hokusai's Great Wave",
    body="Model A: left wave crest. Model B: right wave and Mt Fuji. Together: The Great Wave off Kanagawa",
    outfit=(
        "Model A: full body paint art — LEFT HALF of Hokusai's Great Wave: "
        "massive blue white wave crest with foam tips, Japanese woodblock print style, "
        "characteristic Prussian blue and white painted across entire body. "
        "Model B: full body paint art — RIGHT HALF of same Great Wave: "
        "wave continuation and distant Mt Fuji in background, same woodblock style, "
        "seamlessly connecting to Model A. "
        "CONNECTED ART: together their bodies recreate the complete Great Wave off Kanagawa. "
        "Both: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="minimal Japanese studio with subtle tatami floor suggestion, zen atmosphere",
    lighting="soft Japanese art paper light quality, even woodblock print illumination",
    style="Hokusai living painting editorial, ukiyo-e body art, Japanese fine art photography",
))

# ──────────────────────────────────────────────────────────
# G4 — 연결형 트리오 (6종)
# ──────────────────────────────────────────────────────────

PRESETS.append(trio(
    name="trio_triptych_klimt_bodypaint",
    subject="Three stunning female models side by side forming a Klimt triptych, living painting",
    body="Model A: left panel. Model B: center panel. Model C: right panel. Three bodies one masterpiece",
    outfit=(
        "Model A: full body paint art — LEFT PANEL of Klimt triptych: golden ornamental "
        "border designs, female figure embedded in gold mosaic on skin surface. "
        "Model B: full body paint art — CENTER PANEL: Klimt's The Kiss central motif, "
        "embracing figures in gold, jeweled patterns, densest ornament at center. "
        "Model C: full body paint art — RIGHT PANEL: mirror of left panel, golden "
        "ornamental designs completing the triptych. "
        "CONNECTED ART: three bodies form one complete Klimt triptych. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="grand art nouveau gallery, gilded frames on walls, Viennese Secession atmosphere",
    lighting="warm golden museum lighting, art gallery spotlights, Klimt's golden aura",
    style="Klimt living triptych editorial, art installation fashion, Vogue fine art photography",
))

PRESETS.append(trio(
    name="trio_phoenix_rising_bodypaint",
    subject="Three stunning female models forming one massive phoenix in flight",
    body="Model A left wing: fire feathers. Model B center body: phoenix core. Model C right wing: fire feathers mirror",
    outfit=(
        "Model A: full body paint art — LEFT WING of phoenix: fiery orange red gold "
        "feather patterns flowing from body, flame-tipped wing feathers, fire gradients "
        "painted across entire body reaching right side. "
        "Model B: full body paint art — PHOENIX BODY CENTER: dense golden fire scales, "
        "phoenix breast and torso in crimson gold, most intense fire patterns. "
        "Model C: full body paint art — RIGHT WING mirror: identical mirror wing to "
        "Model A, completing bilateral phoenix symmetry. "
        "CONNECTED ART: three bodies form one massive phoenix in flight. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="dark dramatic sky with fire and embers, phoenix rising from flames concept",
    lighting="warm dramatic fire orange glow from below, ember light, phoenix fire illumination",
    style="phoenix mythology editorial, living mythology art photography, power fashion concept",
))

PRESETS.append(trio(
    name="trio_world_tree_bodypaint",
    subject="Three stunning female models forming Yggdrasil the World Tree",
    body="Model A roots: deep earth. Model B trunk: life force. Model C canopy: sky realm",
    outfit=(
        "Model A: full body paint art — ROOTS of Yggdrasil: deep twisting root systems, "
        "underground earth patterns, ancient Norse runes, dark brown black earth tones "
        "painted across entire body. "
        "Model B: full body paint art — TRUNK of Yggdrasil: massive bark texture, "
        "life force channels, vertical wood grain rising through body, earth to sky browns. "
        "Model C: full body paint art — CANOPY of Yggdrasil: spreading branches, "
        "leaves and sky, nine worlds in the branches, green gold leaf patterns. "
        "CONNECTED ART: vertically aligned they form complete World Tree. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="primordial Norse forest, ancient trees, cosmic axis atmosphere, ethereal light",
    lighting="mystical dappled forest light, roots in shadow, trunk in earth tones, canopy in bright sky light",
    style="Norse mythology editorial, world tree art concept, spiritual fashion photography",
))

PRESETS.append(trio(
    name="trio_ocean_depth_bodypaint",
    subject="Three stunning female models forming ocean depth vertical cross-section",
    body="Model A surface: sunlit. Model B midwater: dimmer. Model C deep: bioluminescent abyss",
    outfit=(
        "Model A: full body paint art — OCEAN SURFACE ZONE: turquoise bright shallow "
        "water, tropical fish, coral, sunlight dappling, vivid colors, sea surface life. "
        "Model B: full body paint art — MIDWATER TWILIGHT ZONE: deeper blue, "
        "jellyfish and squid, fading light, transitional marine life, blue purple tones. "
        "Model C: full body paint art — ABYSSAL DEEP ZONE: pitch black with "
        "bioluminescent creatures, anglerfish lights, glowing deep sea life, "
        "darkness with electric blue bioluminescence. "
        "CONNECTED ART: vertically they form complete ocean depth cross-section. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="seamless gradient ocean atmosphere from bright surface to dark abyss",
    lighting="Model A in bright surface light, Model B in dim blue midwater, Model C in pure darkness with bioluminescent glow only",
    style="ocean science editorial, deep sea art concept, National Geographic luxury fashion",
))

PRESETS.append(trio(
    name="trio_aurora_spectrum_bodypaint",
    subject="Three stunning female models forming one vast aurora borealis across the sky",
    body="Model A: left aurora curtain. Model B: center aurora peak. Model C: right aurora curtain",
    outfit=(
        "Model A: full body paint art — LEFT AURORA CURTAIN: flowing green and teal "
        "aurora ribbons, vertical light curtains, soft green atmospheric glow patterns. "
        "Model B: full body paint art — CENTER AURORA PEAK: most intense aurora, "
        "purple pink and white at maximum intensity, star field background, full spectrum. "
        "Model C: full body paint art — RIGHT AURORA CURTAIN: blue and violet aurora "
        "ribbons mirroring left side, completing the panoramic sky display. "
        "CONNECTED ART: three bodies form one complete aurora borealis across the sky. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="Arctic tundra night, snow-covered landscape, dark sky perfect for aurora viewing",
    lighting="ethereal bioluminescent aurora glow from the paintings themselves, cold arctic night light",
    style="aurora art installation editorial, arctic conceptual photography, cosmic fashion concept",
))

PRESETS.append(trio(
    name="trio_cosmic_creation_bodypaint",
    subject="Three stunning female models representing the timeline of cosmic creation",
    body="Model A: primordial Big Bang. Model B: star nebula formation. Model C: planet and life birth",
    outfit=(
        "Model A: full body paint art — BIG BANG: pure white and gold explosion radiating "
        "from body center, energy burst patterns, primordial light, pure energy chaos. "
        "Model B: full body paint art — NEBULA FORMATION: deep space purple and blue, "
        "swirling gas clouds, proto-stars forming, nebula dust in deep space colors. "
        "Model C: full body paint art — PLANET AND LIFE: blue green Earth patterns, "
        "continents forming, DNA helix, first life emergence, organic forms. "
        "CONNECTED ART: three bodies narrate complete cosmic creation sequence. "
        "All three: body paint pigment applied directly on bare skin, NOT clothing, NOT fabric"
    ),
    environment="deep space infinite blackness with subtle cosmic background radiation visualization",
    lighting="Model A in brilliant white big bang flash, Model B in cool nebula purple glow, Model C in warm life-giving golden light",
    style="cosmic creation mythology editorial, universe origin art concept, scientific fashion photography",
))

# ──────────────────────────────────────────────────────────
# 저장
# ──────────────────────────────────────────────────────────

def save_presets(presets, target_dir):
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
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
    print(f"\n🎨 멀티 바디페인팅 프리셋 생성 — {len(PRESETS)}종\n")
    print(f"대상 디렉토리: {PRESETS_DIR}\n")

    categories = {
        "G1 대비형 듀오": [p for p in PRESETS if p["name"].startswith("duo_") and "bodypaint" in p["name"] and any(k in p["name"] for k in ["fire","day","bloom","gold","ocean","circuit"])],
        "G2 대비형 트리오": [p for p in PRESETS if p["name"].startswith("trio_") and any(k in p["name"] for k in ["rgb","earth","past","predator","ink","season"])],
        "G3 연결형 듀오": [p for p in PRESETS if p["name"].startswith("duo_") and any(k in p["name"] for k in ["butterfly","yin","world_map","klimt","galaxy","wave"])],
        "G4 연결형 트리오": [p for p in PRESETS if p["name"].startswith("trio_") and any(k in p["name"] for k in ["triptych","phoenix","world_tree","ocean_depth","aurora","cosmic"])],
    }

    for cat, items in categories.items():
        print(f"\n📁 {cat} ({len(items)}종):")
        for p in items:
            print(f"   - {p['name']}")

    print(f"\n총 {len(PRESETS)}종 생성 준비 완료")
    print("\n실제 저장하려면 아래 줄의 주석을 해제하세요:")
    print("# saved = save_presets(PRESETS, PRESETS_DIR)")
    print("\n또는 지금 바로 저장:")
    answer = input("저장하시겠습니까? (y/n): ")
    if answer.lower() == 'y':
        saved = save_presets(PRESETS, PRESETS_DIR)
        print(f"\n✅ {len(saved)}개 프리셋 저장 완료")
    else:
        print("저장 취소됨")
