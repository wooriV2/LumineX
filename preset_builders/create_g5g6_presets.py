"""
LumineX G5 연결형 듀오 30종 + G6 대비형 트리오 35종
개별 JSON 프리셋 파일 생성 스크립트
저장위치: preset_builders/
실행: python preset_builders/create_g5g6_presets.py
결과: presets/ 폴더에 JSON 파일 65개 생성
"""

import json
from pathlib import Path

PRESETS_DIR = Path("C:/Dev/LumineX/presets")

PRESETS = {

# ════════════════════════════════════════════
# G5 연결형 듀오 (30종)
# ════════════════════════════════════════════

# ── 자연/우주 ──

"duo_earth_hemisphere_bodypaint": {
    "name": "duo_earth_hemisphere_bodypaint",
    "subject": "Two female models standing side by side, bodies touching at the shoulder",
    "body": "ultra-slim high fashion model, elongated silhouette",
    "outfit": "Left model: Eastern Hemisphere map bodypaint — Asia Africa Europe Pacific Ocean in deep blue, land masses in green and brown with geographic relief detail, latitude longitude grid lines. Right model: Western Hemisphere bodypaint — Americas Atlantic in deep blue, Amazon green, Arctic white. Together their bodies form a complete world map sphere. Body fully painted with map pigment directly on bare skin NOT clothing NOT fabric barefoot.",
    "material": "cartographic bodypaint pigment applied directly on bare skin, NOT clothing",
    "environment": "dark studio with subtle starfield background",
    "lighting": "soft rim light emphasizing map detail, cool blue tones, globe-like illumination",
    "style": "Vogue Italia high-fashion editorial, avant-garde luxury photography",
    "quality": "ultra-sharp 8K, professional body paint photography, National Geographic meets Vogue",
},

"duo_day_city_night_city_bodypaint": {
    "name": "duo_day_city_night_city_bodypaint",
    "subject": "Two female models standing side by side touching shoulders",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: daytime cityscape bodypaint — golden skyscrapers blue sky white clouds sunlight glinting off buildings across chest and torso, street-level city detail on legs. Right model: same city at night bodypaint — neon lights glowing windows dark navy sky with stars reflections on wet streets on legs. Together they form one city panorama from day to night. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "architectural cityscape bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "pure black studio background",
    "lighting": "split lighting — warm golden left side, cool neon blue right side",
    "style": "Vogue Italia high-fashion editorial, avant-garde luxury photography",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_volcano_glacier_bodypaint": {
    "name": "duo_volcano_glacier_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: active volcano bodypaint — molten lava flows in orange and red ash clouds on shoulders volcanic rock texture on legs glowing magma cracks across torso. Right model: glacier bodypaint — ice blue and white crystalline formations crevasse detail snow fields on shoulders meltwater streams on legs. Earth's temperature extremes. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "volcanic and glacial bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dramatic split background — warm orange haze left, cool ice blue right",
    "lighting": "dramatic contrast — fiery warm left, icy cool right",
    "style": "National Geographic meets Vogue Italia editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_storm_eye_bodypaint": {
    "name": "duo_storm_eye_bodypaint",
    "subject": "Two female models standing face to face very close together",
    "body": "ultra-slim high fashion model",
    "outfit": "Both models together form a complete hurricane viewed from above — left model has the left spiral arm of the storm dark grey and white clouds swirling inward. Right model has the right spiral arm. The space between their bodies at center forms the calm eye of the hurricane. When viewed together they create a perfect typhoon satellite image. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "storm cloud bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "aerial satellite view aesthetic, dark atmospheric background",
    "lighting": "dramatic top-down lighting, stormy grey tones",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_aurora_milkyway_bodypaint": {
    "name": "duo_aurora_milkyway_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: aurora borealis bodypaint — green and purple curtains of light flowing across body gossamer light ribbons on arms deep navy sky with scattered stars on legs. Right model: Milky Way galaxy bodypaint — dense star field nebula clouds in pink and gold galactic core swirl on torso star clusters on arms. Together they form one complete night sky panorama. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "celestial bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "pure black studio background",
    "lighting": "very subtle edge lighting, body paint as primary light source, aurora green glow left, galaxy gold glow right",
    "style": "Vogue Italia high-fashion editorial, avant-garde luxury photography",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_coral_abyss_bodypaint": {
    "name": "duo_coral_abyss_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: shallow coral reef bodypaint — vibrant colorful corals tropical fish turquoise warm water sunlight filtering down on upper body sandy seafloor on feet. Right model: deep ocean abyss bodypaint — pitch black with bioluminescent creatures anglerfish glow deep sea jellyfish crushing dark pressure. Together they show the full vertical cross-section of the ocean. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "ocean bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "underwater gradient studio background from turquoise to pitch black",
    "lighting": "gradient — bright turquoise coral light left, deep black with bioluminescent accents right",
    "style": "National Geographic meets Vogue Italia editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_tree_root_bodypaint": {
    "name": "duo_tree_root_bodypaint",
    "subject": "Two female models standing back to back",
    "body": "ultra-slim high fashion model",
    "outfit": "Front-facing model: above-ground tree bodypaint — green canopy on shoulders and head brown trunk on torso bark texture branches on arms reaching upward autumn and spring leaves. Back-facing model: underground root system bodypaint — mirror image as roots brown and earthy soil texture root tips on feet going into earth mycorrhizal fungi detail. Standing back to back they form the complete tree above and below ground. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "organic tree and root bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "split background — natural forest above, rich dark soil below",
    "lighting": "warm natural light from above, deep earthy tones below",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_lightning_rainbow_bodypaint": {
    "name": "duo_lightning_rainbow_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: lightning storm bodypaint — electric white and blue lightning bolts fracturing across entire body dark storm clouds on shoulders thunder energy crackling on arms rain streaks on legs. Right model: rainbow after the storm bodypaint — perfect ROYGBIV spectrum arc flowing from head to foot soft pastel wash clear sky blue background wash golden sunlight glow. Storm and aftermath side by side. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "lightning and rainbow bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "stormy sky transitioning to clear background",
    "lighting": "electric blue dramatic left, warm golden right",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

# ── 동물/생물 ──

"duo_eagle_serpent_bodypaint": {
    "name": "duo_eagle_serpent_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: golden eagle bodypaint — brown and gold feathers covering entire body wing feathers on arms spread wide eagle eye detail on face talons on feet sharp beak motif on chin. Right model: green serpent bodypaint — emerald green scales covering entire body snake eye on face coiling snake pattern spiraling down torso and legs. Together they recreate the Mexican coat of arms eagle and serpent. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "eagle feather and serpent scale bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dramatic natural rock background, eagle's perch aesthetic",
    "lighting": "golden hour warm light, natural drama",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_wolf_moon_bodypaint": {
    "name": "duo_wolf_moon_bodypaint",
    "subject": "Two female models — one standing tall, one kneeling beside her with head tilted back",
    "body": "ultra-slim high fashion model",
    "outfit": "Standing model: full moon bodypaint — silver and white lunar surface covering entire body crater detail across skin soft moonlight glow emanating. Kneeling model: howling wolf bodypaint — grey wolf fur texture covering body wolf face painted across her face howling pose with head tilted back. Together they recreate wolf howling at the moon. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "lunar and wolf fur bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dark forest silhouette background, midnight blue sky with stars",
    "lighting": "cool silver moonlight, dramatic nocturnal shadows",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_butterfly_cocoon_bodypaint": {
    "name": "duo_butterfly_cocoon_bodypaint",
    "subject": "Two female models — one with arms spread open, one tightly wrapped arms close to body",
    "body": "ultra-slim high fashion model",
    "outfit": "Open-arms model: emerged butterfly bodypaint — iridescent Morpho blue butterfly wings painted on spread arms wing eye patterns across entire body antenna detail on head. Wrapped model: chrysalis cocoon bodypaint — silk-wrapped texture covering entire body in gold and green tightly cocooned appearance metamorphosis beginning to break open at chest. Transformation before and after. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "butterfly and chrysalis bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "lush green garden background with filtered sunlight",
    "lighting": "warm dappled natural light, iridescent accent on butterfly wings",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_shark_whale_bodypaint": {
    "name": "duo_shark_whale_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: great white shark bodypaint — grey and white shark skin texture gill slits on ribcage shark fin motif on back rows of teeth pattern on torso predator eye detail on face paint. Right model: blue whale bodypaint — deep blue and grey whale skin barnacle detail baleen plate texture across chest whale flukes on legs gentle giant presence. Ocean apex predator meets ocean's largest creature. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "shark and whale skin bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "deep ocean blue background with light rays filtering from above",
    "lighting": "underwater caustic light patterns, blue depth",
    "style": "National Geographic meets Vogue editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_dragon_phoenix_bodypaint": {
    "name": "duo_dragon_phoenix_bodypaint",
    "subject": "Two female models standing side by side, angled slightly toward each other",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Eastern dragon bodypaint — azure blue and gold dragon scales covering entire body dragon claws on hands dragon horns in head paint cloud motifs the dragon coiling upward from feet to head. Right model: phoenix bodypaint — crimson and gold fire feathers phoenix tail on legs flame wings on arms phoenix crown in head paint rising upward in eternal rebirth. Two mythical creatures facing each other. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "dragon scale and phoenix feather bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dramatic cloudy sky background with celestial divine light",
    "lighting": "dramatic epic fantasy — cool blue left, warm gold and red right",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_lion_zebra_bodypaint": {
    "name": "duo_lion_zebra_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: lion bodypaint — golden tawny fur texture across body lion mane detail around face and shoulders predator amber eyes in face paint powerful paw patterns on hands. Right model: zebra bodypaint — bold black and white stripes covering entire body zebra nose and eye detail in face paint hoof patterns on feet. Predator and prey in impossible harmony. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "lion fur and zebra stripe bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "African savanna background, golden grass, acacia tree silhouette",
    "lighting": "warm African golden hour light, natural documentary",
    "style": "National Geographic meets Vogue editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_spider_web_bodypaint": {
    "name": "duo_spider_web_bodypaint",
    "subject": "Two female models standing side by side, arms slightly spread",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: spider bodypaint — black spider body shape across torso multiple eye detail across face spider legs extending from torso across arms intricate spider anatomy rendered. Right model: spider web bodypaint — geometric silk web pattern covering entire body radial and spiral web lines in silver white across skin morning dew droplets on web threads. Together spider in its complete web. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "spider and web silk bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dark forest background with misty morning backlight",
    "lighting": "backlit morning light catching web detail, dew drop sparkle",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

# ── 명화/문화 ──

"duo_sistine_hands_bodypaint": {
    "name": "duo_sistine_hands_bodypaint",
    "subject": "Two female models reaching their arms toward each other with outstretched hands almost touching fingertips",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: God from Sistine Chapel bodypaint — classical Renaissance fresco colors red and beige robes as body art elderly bearded face elements in body paint angelic figures on torso clouds and divine light. Right model: Adam from Sistine Chapel bodypaint — nude classical figure paint in warm flesh Renaissance tones reclining figure elements classical ideal. Both reach arms recreating iconic fingertip touch. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "Renaissance fresco bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "Sistine Chapel ceiling-style background, Vatican aesthetic",
    "lighting": "warm Renaissance golden light, fresco illumination",
    "style": "tableau vivant, Renaissance painting come to life as body art",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_mona_lisa_split_bodypaint": {
    "name": "duo_mona_lisa_split_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Both models together recreate Leonardo da Vinci's Mona Lisa — left model has the left half of the painting the famous sfumato technique left side of the enigmatic smile landscape background left painted across body. Right model has the right half — right side of the smile right landscape the Italian hills. Together they form the complete masterpiece. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "Da Vinci sfumato style bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "Louvre museum gallery interior background",
    "lighting": "warm museum gallery lighting, Renaissance golden aesthetic",
    "style": "tableau vivant, Da Vinci masterpiece in living body paint",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_birth_venus_split_bodypaint": {
    "name": "duo_birth_venus_split_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Both models together recreate Botticelli's Birth of Venus — left model painted as left half of the masterpiece including Venus's flowing hair and left figure with roses and wind gods on left body. Right model painted as right half — the handmaiden figure flowing pink fabric being offered. Together their bodies recreate the complete Botticelli masterpiece. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "Botticelli Renaissance style bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "Renaissance seascape background, Italian coast",
    "lighting": "soft Renaissance golden light, Botticelli aesthetic",
    "style": "tableau vivant, Botticelli masterpiece in living body paint",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_yin_yang_koi_bodypaint": {
    "name": "duo_yin_yang_koi_bodypaint",
    "subject": "Two female models facing each other in circular pose, mirroring each other",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: white body with yin element — white koi fish swimming upward across white-painted skin black dot on chest as yin eye black swirling water patterns. Right model: black body with yang element — black koi fish swimming downward across black-painted skin white dot on chest as yang eye white swirling water patterns. Together their circular facing pose forms the complete Taoist yin-yang symbol. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "yin-yang koi bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "minimal zen garden background, still water reflection",
    "lighting": "perfectly balanced soft even light, Zen aesthetic",
    "style": "Vogue Italia high-fashion editorial, Taoist philosophy meets fashion",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_chess_board_bodypaint": {
    "name": "duo_chess_board_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: white chess side bodypaint — perfect black and white checkerboard squares covering body white chess pieces queen king rook painted across torso and limbs white side of the board. Right model: black chess side bodypaint — mirror checkerboard squares black chess pieces across body black side. Together their bodies form a complete 8x8 chess board with all pieces. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "chess board geometric bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "elegant marble floor, minimal luxury background",
    "lighting": "clean high-contrast studio lighting, chess aesthetic",
    "style": "Vogue Italia high-fashion editorial, intellectual glamour",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_map_east_west_bodypaint": {
    "name": "duo_map_east_west_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: antique Eastern world map bodypaint — East Asia South Asia Middle East ancient cartography style in sepia and gold decorative compass roses old Portuguese exploration aesthetic. Right model: antique Western world map bodypaint — Europe Africa Americas in matching sepia and gold antique cartography style. Together they form a complete historical world map. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "antique cartography bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "antique library study background, aged wood and leather volumes",
    "lighting": "warm candlelight antique golden tones, aged paper aesthetic",
    "style": "Vogue Italia high-fashion editorial, antique exploration meets fashion",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

# ── SF/판타지 ──

"duo_android_human_bodypaint": {
    "name": "duo_android_human_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: android robot bodypaint — exposed circuit boards and mechanical components across torso titanium metal plating on arms and legs LED light dots across body mechanical joint detail wiring exposed at shoulders. Right model: organic human biology bodypaint — anatomical cross-section heart on chest nervous system on arms muscle fiber on legs human biology made visible. Machine and biology as perfect mirrors. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "android circuit and organic anatomy bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "futuristic laboratory background, half organic half metallic aesthetic",
    "lighting": "cool blue LED light left, warm organic amber right",
    "style": "Vogue Italia high-fashion editorial, sci-fi meets humanity",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_black_hole_star_bodypaint": {
    "name": "duo_black_hole_star_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: black hole bodypaint — pure black void at center of torso accretion disk of glowing orange and white swirling around event horizon gravitational lensing effect warping surrounding paint. Right model: supernova star bodypaint — brilliant white-hot core on chest radiating arms of stellar explosion gold and purple nebula clouds across body star formation in legs. Destroyer and creator of stars. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "cosmic astrophysics bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "deep space black background with distant galaxy clusters",
    "lighting": "the body paint itself as primary light source, cosmic glow",
    "style": "Vogue Italia high-fashion editorial, NASA meets Vogue",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_past_future_city_bodypaint": {
    "name": "duo_past_future_city_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: ancient city bodypaint — Rome or Athens in sepia and stone colors columns and marble temples across torso toga-draped figures in miniature ancient street life on legs classical antiquity. Right model: futuristic city 2100 bodypaint — chrome and glass skyscrapers flying vehicles neon lights holographic advertisements cyberpunk urban future across body. Same location 2000 years apart. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "historical and futuristic cityscape bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "split background — ancient ruins left, neon future city right",
    "lighting": "warm sepia left, cool neon right",
    "style": "Vogue Italia high-fashion editorial, time travel concept",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_virus_antibody_bodypaint": {
    "name": "duo_virus_antibody_bodypaint",
    "subject": "Two female models standing facing each other",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: virus bodypaint — microscopic virus particle patterns spike proteins covering body in red and black viral replication imagery pathogen aesthetic at cellular scale. Right model: antibody immune response bodypaint — Y-shaped antibody molecules in white and blue across body immune cells white blood cells defense system aesthetic. The eternal battle inside human body made visible. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "microscopic biological bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "microscopic cellular environment background, scientific aesthetic",
    "lighting": "dramatic scientific bioluminescent lighting, medical blue tones",
    "style": "Vogue Italia high-fashion editorial, science meets art",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_matrix_reality_bodypaint": {
    "name": "duo_matrix_reality_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Matrix digital world bodypaint — cascading green binary code and matrix characters covering entire body digital grid lines data streams on arms pure code reality. Right model: physical reality bodypaint — hyperrealistic skin texture trompe l'oeil effect normal world colors brick wall texture on torso real world breaking through the code. The moment of waking from simulation. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "digital code and reality bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dark background with faint green code rain falling",
    "lighting": "green matrix light left, natural warm light right",
    "style": "Vogue Italia high-fashion editorial, cyberpunk philosophy",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_crystal_lava_bodypaint": {
    "name": "duo_crystal_lava_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: crystal cave bodypaint — amethyst and quartz crystal formations growing across body purple and white crystalline facets geode interior on torso stalactite detail on arms cave crystal glow. Right model: lava tube bodypaint — molten orange and red lava flows cooling black basalt edges heat shimmer effect volcanic cave walls lava drips on legs. Earth underground extremes. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "crystal and lava bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "underground cave environment, geological drama",
    "lighting": "purple crystal glow left, orange lava glow right",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

# ── 인체/철학 ──

"duo_skeleton_bloom_bodypaint": {
    "name": "duo_skeleton_bloom_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: anatomical skeleton bodypaint — white bones on dark skin accurate skull in face paint ribcage on torso vertebrae visible femur and tibia on legs memento mori aesthetic. Right model: explosive flower bloom bodypaint — thousands of colorful flowers covering entire body roses and peonies on torso vines on arms spring blossoms everywhere life and growth in maximum abundance. Death and life as counterparts. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "skeleton and floral bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "half dark half bright split background",
    "lighting": "dark somber left, bright vibrant floral right",
    "style": "Vogue Italia high-fashion editorial, vanitas meets vitality",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_shadow_light_figure_bodypaint": {
    "name": "duo_shadow_light_figure_bodypaint",
    "subject": "Two female models in identical poses standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: pure light bodypaint — painted entirely in brilliant white with luminescent highlight gradients she IS the light glowing from within pure illumination made flesh. Right model: pure shadow bodypaint — painted entirely in deepest matte black she IS the shadow absorbing all light darkness made flesh. Same pose, same body, light and darkness as separate beings. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "white light and black shadow bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "middle grey neutral studio background",
    "lighting": "perfectly balanced split — white light source from left half, pure shadow right half",
    "style": "Vogue Italia high-fashion editorial, philosophical duality",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"duo_ink_wash_split_bodypaint": {
    "name": "duo_ink_wash_split_bodypaint",
    "subject": "Two female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Both models together form one complete East Asian sumi-e ink wash mountain landscape — left model has the left half misty mountain peaks bamboo grove ink wash gradients in black and grey on skin. Right model has the right half continuation of mountains pine trees distant pagoda flowing river at feet. Together they form one complete traditional ink wash masterpiece. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "sumi-e ink wash bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "misty white background like rice paper, East Asian minimalism",
    "lighting": "soft diffused natural light, ink wash aesthetic, no harsh shadows",
    "style": "East Asian traditional art meets Vogue Italia editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},


# ════════════════════════════════════════════
# G6 대비형 트리오 (35종)
# ════════════════════════════════════════════

# ── 시간/역사 ──

"trio_stone_bronze_iron_bodypaint": {
    "name": "trio_stone_bronze_iron_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Stone Age bodypaint — rough stone texture ochre and earth pigment cave painting motifs handprint patterns ancient hunting scenes prehistoric art. Center model: Bronze Age bodypaint — metallic bronze skin bronze armor patterns ancient Mediterranean geometric ornament. Right model: Iron Age bodypaint — iron grey metallic Celtic knotwork Viking rune patterns iron weapon motifs. Humanity's three ages of material culture. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "prehistoric to iron age bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "museum of human history background, archaeological aesthetic",
    "lighting": "warm archaeological golden light",
    "style": "Vogue Italia high-fashion editorial meets National Geographic",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_ancient_medieval_modern_bodypaint": {
    "name": "trio_ancient_medieval_modern_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Ancient civilization bodypaint — Greek or Roman fresco style classical marble white and terracotta toga draping as body art laurel wreath in face paint. Center model: Medieval era bodypaint — stained glass cathedral window patterns gothic arch motifs chainmail texture crusader cross. Right model: Modern city bodypaint — urban architecture grid neon lights contemporary abstract pattern present day. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "historical era bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "timeline background from ancient ruins to modern city",
    "lighting": "warm sepia left, neutral center, cool blue right",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_past_present_future_self_bodypaint": {
    "name": "trio_past_present_future_self_bodypaint",
    "subject": "Three female models who look similar, representing the same person across time",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model (past self): vintage sepia photograph aesthetic bodypaint — faded sepia tones old photograph grain texture 1920s art deco motifs across body. Center model (present self): vivid natural skin bodypaint — pure naturalistic skin tones perfectly rendered living present moment hyperrealistic. Right model (future self): holographic chrome bodypaint — digital pixel dissolution data visualization silver and chrome the future self. Same person three time states. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "temporal aesthetic bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "white studio background, clean conceptual",
    "lighting": "warm sepia left, natural center, cool chrome right",
    "style": "Vogue Italia high-fashion editorial, philosophical time concept",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_dawn_noon_dusk_bodypaint": {
    "name": "trio_dawn_noon_dusk_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: dawn bodypaint — soft pink and lavender gradient morning mist rising sun glow on skin dew drops gentle awakening light patterns. Center model: noon bodypaint — brilliant golden yellow and white harsh direct sunlight patterns strong shadows peak intensity zenith sun. Right model: dusk bodypaint — deep orange crimson purple gradient last light of day the sun disappearing below horizon across body. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "sky light bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "continuous sky background from pink dawn to orange dusk",
    "lighting": "gradient from cool pink left to blazing golden center to deep purple right",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_birth_life_death_bodypaint": {
    "name": "trio_birth_life_death_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: birth bodypaint — embryonic cellular forms spiral of beginning soft pink and gold new life energy patterns spring buds. Center model: peak life bodypaint — vibrant full bloom flowers across entire body maximum vitality summer abundance roses and sunflowers. Right model: death and transformation bodypaint — autumn leaves falling skeletal forms beneath flower petals seeds forming from dying matter eternal return. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "life cycle bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "natural garden from spring to autumn and winter",
    "lighting": "warm pink left, bright golden center, amber and shadow right",
    "style": "Vogue Italia high-fashion editorial, vanitas tradition",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_seed_tree_ash_bodypaint": {
    "name": "trio_seed_tree_ash_bodypaint",
    "subject": "Three female models — left crouching small, center standing tall arms raised, right kneeling collapsed",
    "body": "ultra-slim high fashion model",
    "outfit": "Crouching model: seed bodypaint — brown seed husk texture potential energy coiled within root tendrils just beginning. Tall standing model: ancient tree bodypaint — bark texture green canopy leaves on raised arms tree rings on torso full life in bloom. Kneeling collapsed model: ash and ember bodypaint — grey ash texture orange ember glow dissolution into elements returning to earth. Complete cycle of organic life. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "organic life cycle bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "forest floor with ash and new growth shoots emerging",
    "lighting": "dramatic cinematic each model differently lit, seed dim, tree bright, ash glowing",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

# ── 원소/자연 ──

"trio_lightning_ocean_earthquake_bodypaint": {
    "name": "trio_lightning_ocean_earthquake_bodypaint",
    "subject": "Three female models in dynamic power poses",
    "body": "ultra-slim high fashion model, athletic toned",
    "outfit": "Left model: lightning bodypaint — electric white and blue fractal lightning bolts covering entire body storm charge crackling from fingertips electromagnetic energy. Center model: ocean bodypaint — deep blue wave patterns white foam ocean current swirls the full power of the sea across body. Right model: earthquake bodypaint — cracked earth texture tectonic plate shift fault line fractures across skin seismic wave patterns. Three forces of natural destruction. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "natural disaster force bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dramatic stormy disaster composite background",
    "lighting": "electric blue left, deep ocean blue center, earth brown cracked right",
    "style": "Vogue Italia high-fashion editorial, elemental power",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_sand_ice_magma_bodypaint": {
    "name": "trio_sand_ice_magma_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: desert sand bodypaint — golden sand grain texture sand dune ripple patterns heat shimmer effect Sahara amber and beige. Center model: glacier ice bodypaint — crystal clear ice blue frozen crevasse patterns ice crystal formations sub-zero clarity. Right model: flowing magma bodypaint — orange and red molten lava texture glowing cracks cooling basalt edges volcanic heat. Earth's three extreme solid surface states. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "geological extreme bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "three-zone background matching each extreme state",
    "lighting": "warm amber left, cool blue center, orange volcanic glow right",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_sky_earth_underground_bodypaint": {
    "name": "trio_sky_earth_underground_bodypaint",
    "subject": "Three female models at different heights — one elevated on platform, one standing, one lower",
    "body": "ultra-slim high fashion model",
    "outfit": "Elevated model: sky bodypaint — cloud formations blue atmosphere lightning birds in flight weather systems across body. Standing model: earth surface bodypaint — forests rivers cities topographic map of land surface civilization. Lower model: underground bodypaint — cave systems geological strata fossil record magma core glowing root systems. Three layers of our world. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "vertical world layer bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "vertical cross-section of earth aesthetic background",
    "lighting": "bright sky light above, warm earth tone center, deep cave glow below",
    "style": "National Geographic meets Vogue Italia editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_micro_human_macro_bodypaint": {
    "name": "trio_micro_human_macro_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: microscale bodypaint — DNA double helix cells atoms quantum particles the invisible world of matter across body. Center model: human scale bodypaint — naturalistic world perspective human landscape city street scale naturalistic body with human scale detail. Right model: cosmic scale bodypaint — galaxies nebulae superclusters the observable universe vast cosmic scale. Micro human macro — all scales of existence. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "scale spectrum bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "white studio, clean scientific conceptual background",
    "lighting": "even studio lighting showing equal importance of each scale",
    "style": "Vogue Italia high-fashion editorial, scientific philosophy",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_fog_rain_snow_bodypaint": {
    "name": "trio_fog_rain_snow_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: fog bodypaint — misty grey-white vapour patterns soft diffused texture moisture in the air made visible mysterious obscuring mist. Center model: rain bodypaint — blue rain streaks cascading down entire body puddle ripple patterns storm rain intensity each drop rendered. Right model: snow bodypaint — white crystalline snowflake patterns covering body each flake unique winter blanket texture frost crystal formations. Water's three weather states. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "atmospheric water state bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "grey atmospheric background, weather studio",
    "lighting": "soft diffused grey lighting throughout, cool tones",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_jungle_desert_tundra_bodypaint": {
    "name": "trio_jungle_desert_tundra_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Amazon rainforest bodypaint — lush green tropical foliage exotic birds butterflies rainforest canopy on shoulders jungle floor on legs maximum biodiversity indigenous patterns. Center model: Sahara desert bodypaint — golden sand ripple texture sand dune patterns desert survival Tuareg geometric patterns extreme heat. Right model: Arctic tundra bodypaint — frozen white landscape polar bear aurora borealis hints Inuit geometric patterns crystalline cold. Earth's three extreme biomes. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "biome bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "three-biome composite background",
    "lighting": "green humid left, golden dry center, cool arctic right",
    "style": "National Geographic meets Vogue Italia editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

# ── 색/빛 ──

"trio_primary_colors_bodypaint": {
    "name": "trio_primary_colors_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: pure red bodypaint — every shade and value of red patterns and textures red is the only color maximum saturation. Center model: pure yellow bodypaint — golden yellow patterns sunburst designs all values of yellow only. Right model: pure blue bodypaint — deep to light blue patterns ocean and sky references blue only. The three primary colors as living beings. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "primary color bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "pure white background to maximize color impact and contrast",
    "lighting": "even bright lighting to show full color saturation, no shadows",
    "style": "Vogue Italia high-fashion editorial, Mondrian meets body art",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_black_white_gray_bodypaint": {
    "name": "trio_black_white_gray_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: pure black bodypaint — matte black covering entire body absorbing all light subtle geometric black-on-black patterns visible only in raking light. Center model: medium grey bodypaint — perfect mid-tone grey between light and dark subtle marble or fabric textures in grey. Right model: pure white bodypaint — brilliant white covering entire body reflecting all light subtle raised texture patterns in white. The complete achromatic spectrum. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "achromatic bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "middle grey studio background, calibrated neutral",
    "lighting": "perfectly calibrated even lighting across all three models",
    "style": "Vogue Italia high-fashion editorial, Ansel Adams meets body art",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_gold_silver_bronze_bodypaint": {
    "name": "trio_gold_silver_bronze_bodypaint",
    "subject": "Three female models on tiered podium levels — highest left, middle center, lower right",
    "body": "ultra-slim high fashion model",
    "outfit": "Highest podium model: gold bodypaint — Olympic gold metallic paint laurel wreath motifs champion victory energy gleaming gold. Middle podium model: silver bodypaint — Olympic silver metallic paint flowing silver patterns second place grace. Lower podium model: bronze bodypaint — warm bronze metallic paint ancient athlete motifs honorable third. The three medals of achievement as living women on podium. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "Olympic medal metallic bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "Olympic ceremony aesthetic, podium, stadium atmosphere",
    "lighting": "triumphant golden ceremonial lighting, victory spotlight",
    "style": "Vogue Italia high-fashion editorial, Olympic glory meets fashion",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_neon_pastel_dark_bodypaint": {
    "name": "trio_neon_pastel_dark_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: maximum neon bodypaint — electric neon pink green yellow at full saturation UV reactive quality rave energy blacklight aesthetics. Center model: soft pastel bodypaint — gentle lavender baby pink soft mint green watercolor softness delicate and dreamy palette. Right model: deep dark color bodypaint — midnight navy forest green deep burgundy moody dark saturated gothic richness. Three completely different color worlds. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "color world bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "neutral black background allowing all three color worlds to shine",
    "lighting": "UV blacklight left, soft natural center, dramatic moody right",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_sunrise_sunset_moonrise_bodypaint": {
    "name": "trio_sunrise_sunset_moonrise_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: sunrise bodypaint — pink and gold dawn light patterns sun emerging over horizon across torso morning birds dew fresh beginning energy. Center model: sunset bodypaint — deep orange amber crimson the sun descending dramatic silhouette landscape across body. Right model: moonrise bodypaint — deep blue night sky full moon rising silver lunar light stars appearing nocturnal serenity. Three celestial transitions in one day. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "celestial transition bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "continuous sky background across all three models",
    "lighting": "warm pink left, deep orange center, silver blue right",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_infrared_visible_uv_bodypaint": {
    "name": "trio_infrared_visible_uv_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: infrared spectrum bodypaint — false color infrared photography style red hot body heat visualization thermal imaging color palette. Center model: natural visible light — normal natural human skin tones the world as human eyes see it. Right model: ultraviolet spectrum bodypaint — UV reactive paint patterns blacklight visible designs the hidden world beyond visible light. Three ways of seeing the same body. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "light spectrum bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "scientific laboratory aesthetic background",
    "lighting": "warm infrared left, natural center, UV blacklight right",
    "style": "Vogue Italia high-fashion editorial, science meets art",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

# ── 신화/종교 ──

"trio_heaven_earth_hell_bodypaint": {
    "name": "trio_heaven_earth_hell_bodypaint",
    "subject": "Three female models at different vertical levels — one elevated, one standing, one lower",
    "body": "ultra-slim high fashion model",
    "outfit": "Elevated model: Heaven bodypaint — white and gold divine light angel wing motifs halo glow cloud formations celestial beauty radiating. Standing model: Earth bodypaint — green continents blue oceans human civilization surface world balance natural beauty. Lower model: Hell bodypaint — red and black flames demonic motifs lava cracks dark infernal energy powerful dark beauty. The three realms of existence. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "three realms bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dramatic vertical three-zone background heaven above earth center infernal below",
    "lighting": "golden divine above, natural center, red infernal below",
    "style": "Vogue Italia high-fashion editorial, Dante's cosmos meets fashion",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_creator_preserver_destroyer_bodypaint": {
    "name": "trio_creator_preserver_destroyer_bodypaint",
    "subject": "Three female models in Hindu goddess poses",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model (creative gesture): Brahma the Creator bodypaint — golden creation energy lotus flower motifs Sanskrit calligraphy cosmic egg four-armed iconography elements. Center model (balanced pose): Vishnu the Preserver bodypaint — deep blue skin paint four lotus symbols cosmic ocean preserving balance Vishnu's eternal rest. Right model (dynamic fierce pose): Shiva the Destroyer bodypaint — ash grey skin crescent moon head third eye trishul trident motif cosmic destruction regeneration. Hindu divine trinity. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "Hindu divine bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "cosmic Hindu temple celestial background",
    "lighting": "golden creative left, deep blue preserving center, silver powerful right",
    "style": "Vogue Italia high-fashion editorial, Hindu philosophy meets art",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_fate_three_bodypaint": {
    "name": "trio_fate_three_bodypaint",
    "subject": "Three female models — left spinning thread, center measuring, right with cutting gesture",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model (spinning): Clotho the Spinner bodypaint — thread and spindle motifs spiraling across body life thread emerging fate being created. Center model (measuring): Lachesis the Allotter bodypaint — ruler and measuring motifs life span calculation destiny patterns. Right model (cutting gesture): Atropos the Inevitable bodypaint — scissors motifs the final cut inevitability of fate. The three Greek Moirai controlling human destiny. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "Greek Fate goddess bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "ancient Greek dramatic classical background",
    "lighting": "dramatic theatrical goddess lighting, timeless",
    "style": "Vogue Italia high-fashion editorial, Greek mythology meets fashion",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_medusa_sphinx_hydra_bodypaint": {
    "name": "trio_medusa_sphinx_hydra_bodypaint",
    "subject": "Three female models in powerful mythological monster goddess poses",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Medusa bodypaint — snake hair painted as head art green scale skin texture petrifying gaze serpent coils across body Greek monster beauty. Center model: Sphinx bodypaint — Egyptian Sphinx headdress body art riddle-keeper energy leonine elements ancient Egypt gold and blue. Right model: Hydra bodypaint — multiple snake head motifs hydra scales regenerating wound motifs swamp green and dark water. Greece's three greatest female monsters. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "Greek monster goddess bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "ancient Greek ruins mythological drama background",
    "lighting": "dramatic hero myth low lighting, green for Medusa, gold for Sphinx, swamp for Hydra",
    "style": "Vogue Italia high-fashion editorial, Greek mythology meets fashion",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_valkyrie_siren_medea_bodypaint": {
    "name": "trio_valkyrie_siren_medea_bodypaint",
    "subject": "Three female models in powerful mythological woman poses",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Valkyrie bodypaint — Norse battle silver and gold armor body art raven motifs Odin's chooser of the slain Viking rune patterns warrior power. Center model: Siren bodypaint — oceanic blue and green fish scale texture merging with skin ship motifs the deadly beautiful oceanic call Greek island aesthetic. Right model: Medea bodypaint — dark sorceress golden fleece motifs Greek pottery imagery powerful witch energy dark magic. Three mythological women of lethal power. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "mythological woman bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dramatic mythological composite landscape background",
    "lighting": "silver battle light left, blue oceanic center, dark sorcery right",
    "style": "Vogue Italia high-fashion editorial, mythological feminine power",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

# ── 문명/지역 ──

"trio_amazon_sahara_arctic_bodypaint": {
    "name": "trio_amazon_sahara_arctic_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Amazon rainforest bodypaint — dense tropical green exotic wildlife waterfall patterns indigenous Amazon body art motifs integrated. Center model: Sahara desert bodypaint — golden sand desert survival motifs Tuareg geometric patterns extreme heat sun. Right model: Arctic bodypaint — ice white polar bear aurora borealis Inuit geometric patterns crystalline cold extreme. Earth's three most extreme environments. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "extreme biome bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "three extreme environment composite background",
    "lighting": "green humid left, golden harsh center, cool arctic right",
    "style": "National Geographic meets Vogue Italia editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_east_west_south_bodypaint": {
    "name": "trio_east_west_south_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Eastern civilization bodypaint — Chinese dragon Japanese kamon Korean dancheong patterns silk road gold and crimson Eastern philosophy calligraphy. Center model: Western civilization bodypaint — Greek columns Roman eagle Renaissance art motifs Western classical heritage marble white and blue. Right model: Southern civilizations bodypaint — African kente geometry Aztec sun calendar Indian mandala Global South heritage. Three great traditions of humanity. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "world civilization bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "world heritage site composite background",
    "lighting": "warm Eastern light, classical Western light, vibrant Southern light",
    "style": "Vogue Italia high-fashion editorial, world culture celebration",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_viking_samurai_spartan_bodypaint": {
    "name": "trio_viking_samurai_spartan_bodypaint",
    "subject": "Three female models in warrior poses",
    "body": "ultra-slim high fashion model, athletic toned",
    "outfit": "Left model: Viking shield-maiden bodypaint — Norse runes covering body Yggdrasil tree shield and axe motifs Viking blue-grey cold sea aesthetic. Center model: Onna-bugeisha samurai bodypaint — Japanese family mon crest cherry blossom samurai armor naginata motifs red and black lacquer. Right model: Spartan warrior woman bodypaint — Greek meander patterns Spartan shield lambda olive wreath red cape motif classical Greek warrior. Three greatest warrior traditions female perspective. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "warrior civilization bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "ancient battlefield dramatic three-civilization background",
    "lighting": "dramatic warrior battle lighting each differently lit",
    "style": "Vogue Italia high-fashion editorial, warrior mythology meets fashion",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_geisha_odalisque_gisaeng_bodypaint": {
    "name": "trio_geisha_odalisque_gisaeng_bodypaint",
    "subject": "Three female models in elegant traditional poses",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Japanese Geisha bodypaint — white geisha makeup elements kimono pattern across body kanzashi hairpin motifs cherry blossom tea ceremony elegance. Center model: Ottoman Odalisque bodypaint — Turkish tile patterns harem beauty Orientalist aesthetic jewel tones and gold. Right model: Korean Gisaeng bodypaint — Joseon court patterns hanji motifs gisaeng fan dance elements literary and musical accomplishment. Three great traditions of female artistic culture. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "East artistic tradition bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "elegant East-meets-East interior lantern light background",
    "lighting": "warm lantern light aesthetic across all three",
    "style": "Vogue Italia high-fashion editorial, cultural arts celebration",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_nile_amazon_yangtze_bodypaint": {
    "name": "trio_nile_amazon_yangtze_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Nile River civilization bodypaint — Egyptian hieroglyphs papyrus plants lotus flowers Nile delta map pharaonic gold and lapis lazuli. Center model: Amazon River bodypaint — indigenous Amazon patterns tropical biodiversity piranha anaconda pink dolphin motifs green abundance. Right model: Yangtze River bodypaint — Chinese ink wash mountains dragon motifs rice terraces Three Gorges landscape Chinese civilization map. Three rivers that gave birth to civilization. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "river civilization bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "world river civilization map background",
    "lighting": "golden Egyptian left, green jungle center, misty mountain Chinese right",
    "style": "National Geographic meets Vogue editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_rome_babylon_aztec_bodypaint": {
    "name": "trio_rome_babylon_aztec_bodypaint",
    "subject": "Three female models in imperial goddess poses",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Roman Empire bodypaint — Roman mosaic patterns SPQR eagle motifs toga patterns Colosseum architecture across torso laurel wreath. Center model: Babylon bodypaint — Hanging Gardens plants Ishtar Gate blue and gold tiles cuneiform script lion of Babylon ancient Mesopotamia. Right model: Aztec Empire bodypaint — Aztec sun calendar on torso feathered serpent Quetzalcoatl Teotihuacan pyramid jade green and gold. Three great empires three continents one humanity. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "ancient empire bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "composite imperial architecture background from three continents",
    "lighting": "golden imperial ceremonial lighting",
    "style": "Vogue Italia high-fashion editorial, imperial grandeur meets fashion",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

# ── 감정/철학 ──

"trio_love_war_peace_bodypaint": {
    "name": "trio_love_war_peace_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Love bodypaint — roses and hearts covering body Aphrodite Venus motifs soft pink and red doves universal human emotion. Center model: War bodypaint — battle wounds healed into art warrior symbols red and black dramatic power Mars energy swords and shields as body art. Right model: Peace bodypaint — white dove patterns olive branch motifs clear sky blue earth from space UN blue aesthetic. Humanity's eternal triangle. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "universal concept bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "dramatic sky background",
    "lighting": "warm pink left, dramatic red center, cool peace blue right",
    "style": "Vogue Italia high-fashion editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_fear_anger_joy_bodypaint": {
    "name": "trio_fear_anger_joy_bodypaint",
    "subject": "Three female models in emotionally expressive poses — contracted left, explosive center, expansive right",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model (contracted protective pose): Fear bodypaint — cold blue and dark purple goosebump texture shadow motifs hiding protective energy in the paint. Center model (explosive power pose): Anger bodypaint — volcanic red and orange fire crackling from body thunder energy maximum intensity. Right model (expansive open arms pose): Joy bodypaint — warm golden yellow sunburst patterns flowers blooming from skin light radiating outward. Three primary human emotions as living art. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "emotion bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "pure black studio background",
    "lighting": "cool blue left, explosive red center, warm golden right",
    "style": "Vogue Italia high-fashion editorial, emotional psychology as art",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_order_chaos_void_bodypaint": {
    "name": "trio_order_chaos_void_bodypaint",
    "subject": "Three female models standing side by side",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Order bodypaint — perfect geometric grid patterns mathematical precision sacred geometry crystalline structure control and pattern across body. Center model: Chaos bodypaint — explosive random fractal patterns paint splatter and drips maximum entropy beautiful disorder. Right model: Void bodypaint — pure deep black nothing the absence of all only the model's form visible as negative space emptiness itself. The three states of existence. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "philosophical state bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "pure black studio background",
    "lighting": "precise geometric light left, chaotic multi-directional center, barely visible void right",
    "style": "Vogue Italia high-fashion editorial, cosmological philosophy",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_predator_prey_scavenger_bodypaint": {
    "name": "trio_predator_prey_scavenger_bodypaint",
    "subject": "Three female models in nature relationship poses",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: apex predator bodypaint — lion or wolf fur texture and markings hunting focused eyes power and aggression in pattern. Center model: prey bodypaint — soft dappled deer or gazelle skin pattern alert wide eyes grace and vulnerability. Right model: scavenger bodypaint — vulture feather patterns hyena spot texture necessary ecosystem cleanup crew. The complete food chain. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "food chain animal bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "African savanna background, golden grass, nature documentary aesthetic",
    "lighting": "dramatic golden nature documentary lighting",
    "style": "National Geographic meets Vogue editorial",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_id_ego_superego_bodypaint": {
    "name": "trio_id_ego_superego_bodypaint",
    "subject": "Three female models — similar looking, different expressions and poses",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Id bodypaint — raw primal patterns animal instinct motifs red and black passion unconscious desire made visible. Center model: Ego bodypaint — balanced realistic patterns grey and neutral tones the conscious rational self mirror of reality. Right model: Superego bodypaint — gold and white moral authority patterns societal ideals rule and conscience made visible. Freud's three-part psyche as three living women. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "psychological concept bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "white clinical studio, psychological aesthetic",
    "lighting": "dramatic psychological contrast each figure differently lit",
    "style": "Vogue Italia high-fashion editorial, psychological philosophy as art",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

"trio_thesis_antithesis_synthesis_bodypaint": {
    "name": "trio_thesis_antithesis_synthesis_bodypaint",
    "subject": "Three female models — two flanking facing each other, one between them facing forward",
    "body": "ultra-slim high fashion model",
    "outfit": "Left model: Thesis bodypaint — structured geometric golden patterns the initial proposition classical beauty and order. Right model: Antithesis bodypaint — opposing silver chaotic mirror patterns the contradiction challenging the thesis. Center model: Synthesis bodypaint — gold AND silver patterns merging both geometric and free the resolution transcending the opposition. Hegel's dialectic method as living body art. Body fully painted directly on bare skin NOT clothing barefoot.",
    "material": "dialectic philosophy bodypaint pigment directly on bare skin, NOT clothing",
    "environment": "minimalist philosophical studio, clean and contemplative",
    "lighting": "golden left, silver right, harmonious blend center",
    "style": "Vogue Italia high-fashion editorial, Hegelian philosophy as art",
    "quality": "ultra-sharp 8K, professional body paint photography",
},

}  # end PRESETS dict


def main():
    PRESETS_DIR.mkdir(exist_ok=True)
    created = 0
    skipped = 0

    for preset_name, data in PRESETS.items():
        filepath = PRESETS_DIR / f"{preset_name}.json"
        if filepath.exists():
            print(f"  [SKIP] {preset_name}.json 이미 존재")
            skipped += 1
            continue
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  [OK] {preset_name}.json")
        created += 1

    print(f"\n완료: 생성 {created}개 / 스킵 {skipped}개 / 총 {len(PRESETS)}개")
    print(f"저장위치: {PRESETS_DIR}")


if __name__ == '__main__':
    main()
