# -*- coding: utf-8 -*-
"""
patch_bp_hof_5_schema_fix.py
Bodypaint HOF 28종 JSON을 기존 9필드 스키마로 재작성 (덮어쓰기)

스키마: tag / subject / body / outfit / material / environment / lighting / style / quality
※ outfit 은 반드시 "body fully painted with:" 로 시작 (_is_bodypaint 감지용)

실행:
    $env:PYTHONUTF8 = "1"
    cd C:\\Dev\\LumineX
    python preset_builders\\patch_bp_hof_5_schema_fix.py
"""
import json
import os

PRESETS_DIR = "presets"

MAT_MATTE = (
    "fine art body paint — bone-dry chalky matte pigment on bare skin, no wet sheen no gloss, "
    "skin pores and texture visible through the pigment, paint ends at wrist and ankle in one thin "
    "crisp border with hands and feet bare, NO clothing NO fabric NO garment shape"
)
MAT_INK = (
    "fine art body paint — matte ink line work sitting flat in the skin, edges slightly soft as "
    "printed ink, skin pores visible beneath, paint ends at wrist and ankle in one thin crisp "
    "border with hands and feet bare, NO clothing NO fabric NO garment shape"
)

Q23 = "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography, portrait 2:3 vertical"
Q34 = "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography, portrait 3:4 vertical"

PRESETS = {
    # ───────────────────────── SOLO 13 ─────────────────────────
    "bp_solo_shibori_indigo_mature": {
        "tag": "Shibori Indigo Body Paint",
        "subject": "a fine art female model with Japanese shibori indigo body paint",
        "body": "petite compact build, dark brown hair in a high tight bun, seated on the floor with legs folded to one side, one hand on the mat, torso turned in three-quarter view",
        "outfit": "body fully painted with: Japanese shibori indigo resist-dye — tight kumo spiderweb rings over the shoulders, itajime folded triangles down the torso, fine kanoko dots covering arms and legs, deep indigo and undyed white, every surface filled with no blank ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE,
        "environment": "a quiet tatami room, shoji screen partly open to a garden, barefoot on tatami",
        "lighting": "broad soft daylight through the shoji from the left at a low raking angle, pattern reading clearly on the lit side, natural falloff into shadow on the right",
        "style": "quiet documentary fine art photography, Japanese textile craft sensibility",
        "quality": Q23,
    },
    "bp_solo_katazome_crane_pine_mature": {
        "tag": "Katazome Crane and Pine Body Paint",
        "subject": "a fine art female model in her forties with Japanese katazome stencil body paint",
        "body": "athletic build with defined shoulders, black hair cropped short, standing squarely with arms held slightly out from the body, chin level, direct gaze",
        "outfit": "body fully painted with: katazome paper-stencil dyeing — deep indigo ground with white reserved shapes, flying cranes across the chest, pine needle clusters over the shoulders, tortoiseshell hexagons down the arms, karakusa vine scrolls covering the legs, every motif hard-edged and precisely repeated tiled edge to edge with no blank ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE,
        "environment": "a dyeing workshop, long indigo vats sunk in the floor, lengths of dyed cloth hanging to dry, barefoot on wet stone",
        "lighting": "high diffuse daylight from a roof skylight directly above, soft downward modeling, gentle shadow under the brow and chin",
        "style": "documentary photography of traditional textile craft",
        "quality": Q23,
    },
    "bp_solo_hwarot_phoenix_gold_elder": {
        "tag": "Hwarot Phoenix Gold Thread Body Paint",
        "subject": "a fine art female model in her sixties with Korean hwarot bridal embroidery body paint",
        "body": "full dignified build, grey hair in a traditional low chignon with a binyeo pin, seated on a low wooden chest with back straight, hands folded in the lap, facing the camera",
        "outfit": "body fully painted with: Korean hwarot bridal embroidery — dense silk thread work in vermilion cobalt jade and gold on deep red ground, paired phoenixes across the chest, peony blooms over the shoulders, lotus and pomegranate down the torso, stylized wave and rock bands around the legs, couched gold outline and satin-stitch fill packed everywhere with visible thread direction, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", natural age lines visible through the color",
        "environment": "a dim hanok room at night, lacquered chest, folding screen behind, barefoot on a woven mat",
        "lighting": "warm candlelight from two low candles at the front left, flickering soft key, deep falloff into shadow, gold thread catching small specular glints",
        "style": "quiet documentary fine art photography, Korean court craft sensibility",
        "quality": Q23,
    },
    "bp_solo_adire_eleko_indigo_mature": {
        "tag": "Adire Eleko Indigo Body Paint",
        "subject": "a fine art female model in her forties with Yoruba adire eleko body paint",
        "body": "full curvy figure with broad hips and defined waist, strong shoulders, hair in tight cornrows gathered back, standing with weight on one leg and one hand resting on the outward hip, torso turned three-quarter, chin lifted",
        "outfit": "body fully painted with: Yoruba adire eleko cassava-paste resist on deep indigo — olokun concentric ring motifs across the torso, ibadandun grid squares each filled with a different tiny hand-drawn symbol over hips and thighs, fine comb-drawn line bands down the arms, soft irregular bleed where the resist lifted, no blank ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE,
        "environment": "a compound courtyard, indigo dye pots, cloth drying on a line, barefoot on packed earth",
        "lighting": "late afternoon sun from the side at a low angle raking hard across the body to model hip and waist, warm bounce off the earth on the shadow side",
        "style": "documentary photography of traditional textile craft",
        "quality": Q23,
    },
    "bp_solo_abrbandi_ikat_young": {
        "tag": "Abr-bandi Ikat Body Paint",
        "subject": "a fine art female model in her twenties with Uzbek abr-bandi ikat body paint",
        "body": "athletic hourglass build with defined waist and shoulders, long dark hair in a single thick braid over one shoulder, mid-turn with one foot crossing behind the other, torso twisting toward the camera while hips stay angled away, one arm lifted holding a hanging silk skein",
        "outfit": "body fully painted with: Uzbek abr-bandi ikat — bold cloud-blurred flame and pomegranate forms across the torso, ram's-horn hooks down the legs, narrow rainbow warp stripes along the arms, crimson saffron emerald and white on black, every edge feathered and bleeding in the characteristic ikat blur, colors packed with no black ground exposed, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE,
        "environment": "a silk workshop, skeins of dyed thread hanging in rows, barefoot on a woven rug",
        "lighting": "hard daylight from a high side window raking down across the twist of the torso, strong shadow in the small of the back, weak fill opposite",
        "style": "documentary photography of traditional textile craft",
        "quality": Q23,
    },
    "bp_solo_andean_pallay_mature": {
        "tag": "Andean Pallay Weaving Body Paint",
        "subject": "a fine art female model in her thirties with Andean pallay weaving body paint",
        "body": "curvy strong build with full hips and thighs and defined waist, black hair in two long braids, photographed from behind at three-quarter angle with weight on one leg and hip pushed out, head turned back over the shoulder toward the camera, one hand at the waist",
        "outfit": "body fully painted with: Andean pallay pickup-weave bands running horizontally across the body — rows of inti sun figures, ch'unchu zigzag mountains, kinsa cruz stepped crosses, tiny stylized llamas and birds, crimson ochre black and white, each band tightly packed with narrow striped dividers between and no undyed ground anywhere, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE,
        "environment": "a high altiplano slope, stone wall, distant peaks, barefoot on dry grass",
        "lighting": "hard low-angle mountain sun from the side carving the curve of the back and hip, deep shadow on the far side, thin cold sky fill",
        "style": "documentary photography of traditional textile craft",
        "quality": Q23,
    },
    "bp_solo_kente_adweneasa_mature": {
        "tag": "Kente Adweneasa Body Paint",
        "subject": "a fine art female model in her thirties with Ashanti kente strip-weave body paint",
        "body": "curvy hourglass build with narrow waist and broad hips, hair in a high sculpted updo, standing frontally with chest and shoulders square to the camera, one leg crossed slightly in front of the other, hands relaxed away from the waist",
        "outfit": "body fully painted with: Ashanti kente strip-weaving — a tight grid of woven blocks in saffron gold emerald crimson and black, alternating warp-stripe and weft-float blocks in checkerboard rotation, each block filled with its own adinkra symbol or zigzag comb or double-headed lozenge, strip seams reading as fine vertical lines, no empty ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE,
        "environment": "a bright courtyard, folded kente cloth stacked on a low bench, modern polished gold metallic stiletto sandals with thin ankle strap and open toe",
        "lighting": "hard equatorial sun from the front right at 45 degrees, crisp shadow under the jaw and bust, white wall bouncing light back onto the shadow side",
        "style": "high fashion editorial meeting traditional textile craft",
        "quality": Q23,
    },
    "bp_solo_miao_batik_silver_mature": {
        "tag": "Miao Wax-Resist Batik Body Paint",
        "subject": "a fine art female model in her thirties with Guizhou Miao batik body paint",
        "body": "hourglass figure with defined waist and rounded hips, long black hair coiled high with a silver comb, standing frontally with chest and shoulders square to the camera, both arms held slightly out with palms forward and open",
        "outfit": "body fully painted with: Guizhou Miao wax-resist batik — deep indigo ground with fine white resist linework, large spiral whorls across the chest, butterfly-mother figures with outspread wings over the shoulders, dragon-and-fish forms down the torso, dense concentric coils and comb-tooth bands filling the legs, every line hand-drawn and slightly irregular with wax crackle as hairline fractures, no empty indigo ground remaining, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE,
        "environment": "the interior of a wooden stilt house, batik cloth drying on a rack, open doorway to a green valley, hand-embroidered indigo cloth shoes with red and green floral stitching",
        "lighting": "daylight from the open doorway at the front left at 45 degrees modeling the frontal form, dim wooden interior falling away behind",
        "style": "documentary photography of traditional textile craft",
        "quality": Q23,
    },
    "bp_solo_ndebele_geometric_mature": {
        "tag": "Ndebele Geometric Body Paint",
        "subject": "a fine art female model in her thirties with Ndebele geometric body paint",
        "body": "curvy hourglass build with broad hips and narrow waist, hair in a high sculpted crown of coiled braids, mid-stride walking directly toward the camera with one leg forward and crossing slightly, torso squared and chest frontal, arms swinging naturally",
        "outfit": "body fully painted with: Ndebele geometric design — bold flat blocks of cobalt blue chrome yellow crimson emerald and white each outlined in heavy black, stepped gable and staircase forms across the chest and torso, razor-edge chevrons down the legs, small aeroplane and lightbulb motifs set into the larger fields, narrow black banding separating every shape, blocks tiled edge to edge with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped lacquered cobalt blue with fine black outline",
        "environment": "a painted courtyard wall in matching Ndebele geometry out of focus, white leather platform stiletto sandals with chunky 4cm platform and open toe showing painted toenails",
        "lighting": "bright frontal-left key at 45 degrees with hard African midday sun quality, crisp shadow under the jaw and bust, white wall bounce filling the shadow side",
        "style": "high fashion editorial meeting traditional craft",
        "quality": Q23,
    },
    "bp_solo_kuba_raffia_mature": {
        "tag": "Kuba Raffia Cloth Body Paint",
        "subject": "a fine art female model in her thirties with Kuba raffia cloth body paint",
        "body": "athletic hourglass build with defined waist and shoulders, hair shaved close with a geometric line pattern cut into it, body angled away at 45 degrees with hips turned back and torso twisting forward so the chest rotates toward the lens, one arm crossing the body to rest on the opposite hip, head turned over the shoulder",
        "outfit": "body fully painted with: Kuba raffia cloth — irregular interlocking geometry in natural raffia beige rust brown charcoal and black, meandering key-fret bands that break and restart out of alignment, cut-pile velvet blocks with visible plush texture, appliqué patch shapes with hand-stitched edges, small knot rows between fields, deliberately asymmetric with every field filled and no repeating grid, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", cut-pile areas reading as raised velvet nap, nails short almond lacquered matte charcoal",
        "environment": "a concrete gallery space, one large Kuba panel mounted behind, sculptural bronze metallic heels with an architectural curved wedge and open toe",
        "lighting": "key from the front right at 45 degrees raking across the twisted torso to carve the waist, secondary rim from behind left separating the shoulder",
        "style": "high fashion editorial meeting textile craft",
        "quality": Q23,
    },
    "bp_solo_paj_ntaub_hmong_mature": {
        "tag": "Hmong Paj Ntaub Body Paint",
        "subject": "a fine art female model in her thirties with Hmong paj ntaub body paint",
        "body": "curvy hourglass build with defined waist and broad hips, hair coiled high in a sculpted turban-style wrap, mid-stride walking directly toward the camera with one leg crossing forward, torso squared and chest frontal, shoulders open, arms swinging naturally",
        "outfit": "body fully painted with: Hmong paj ntaub reverse appliqué and cross-stitch — snail-shell spiral coils, elephant-foot squares, ram's-horn hooks and stepped maze frets all outlined in crisp black and filled with magenta chartreuse turquoise orange and white, motifs sized small and repeated tightly so the pattern reads as continuous texture, uniform density everywhere with zero blank ground and no separate panels, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped lacquered bright turquoise with fine black outline",
        "environment": "a plain concrete courtyard, one paj ntaub panel hung out of focus behind, white patent platform stiletto sandals with 4cm platform and open toe showing painted toenails",
        "lighting": "bright frontal-left key at 45 degrees with hard midday quality, crisp shadow under the jaw and bust, white wall bounce on the shadow side",
        "style": "high fashion editorial meeting textile craft",
        "quality": Q23,
    },
    "bp_solo_termeh_boteh_mature": {
        "tag": "Persian Termeh Boteh Body Paint",
        "subject": "a fine art female model in her forties with Persian termeh boteh body paint",
        "body": "full hourglass figure with soft strong build and sharply defined waist, black hair in a low chignon, seated on a low bench with hips angled to one side and torso twisting back so the chest turns toward the camera, one hand planted on the bench behind her",
        "outfit": "body fully painted with: Persian termeh weaving — a continuous allover boteh paisley field with no plain ground, curved teardrop boteh forms in garnet lapis emerald and saffron each outlined in fine gold and filled with dense interior floral scrollwork nested so every boteh touches its neighbours, tiny stem-and-leaf fillers in any remaining space, uniform scale across chest torso arms and legs with no panels or borders, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails medium almond lacquered deep garnet",
        "environment": "a dark studio, one antique termeh panel mounted behind, garnet-red satin platform stiletto sandals with 3cm platform and open toe",
        "lighting": "warm key from the front left at 45 degrees, low and directional so the gold outlines flare along the chest and thigh, deep falloff behind",
        "style": "high fashion editorial meeting textile craft",
        "quality": Q23,
    },
    "bp_solo_ainu_moreu_mature": {
        "tag": "Ainu Moreu Scroll Body Paint",
        "subject": "a fine art female model in her thirties with Ainu attus moreu body paint",
        "body": "hourglass figure with narrow waist and rounded hips, long dark hair loose over one shoulder, hips in full profile at 90 degrees with torso rotating forward so the chest opens toward the lens, shoulders squared to camera, one arm extended down the thigh and the other lifted to the collarbone",
        "outfit": "body fully painted with: Ainu attus appliqué and embroidery — interlocking moreu spiral scrolls and ayus thorn-hook barbs in indigo navy and off-white, each band edged with fine chain-stitch outlines, the scrolls looping and branching without repeating and dense enough that navy and white share the surface evenly, uniform density from collarbone to ankle with no band structure, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped lacquered deep indigo navy",
        "environment": "a pale wood gallery interior, one attus robe mounted flat behind, pale birch-wood platform wedge sandals with sculptural block form and open toe",
        "lighting": "cool key from the front left at 45 degrees raking across the rotated torso to define the bust and waist, soft rim from behind right",
        "style": "high fashion editorial meeting textile craft",
        "quality": Q23,
    },

    # ───────────────────────── DUO 5 ─────────────────────────
    "bp_duo_diatom_radiolaria_mature": {
        "tag": "Diatom and Radiolaria Duo Body Paint",
        "subject": "two fine art female models with darkfield microscopy plankton body paint, one in her early thirties and one in her early forties, standing shoulder to shoulder with no gap between them",
        "body": "both hourglass figures with defined waists and full hips, LEFT long black hair slicked back wet and RIGHT hair shaved close with a geometric line cut, LEFT in contrapposto with outer hip pushed away and torso twisting so the chest rotates toward camera, RIGHT mirroring in reverse, inner hips pressed together, outer hands on outer hips, both looking into the lens",
        "outfit": "body fully painted with: a single continuous darkfield microscopy plankton field spanning both bodies — LEFT centric diatoms as hundreds of small radial silica discs each a ring of concentric pores in luminous amber cream and pale gold against near-black, RIGHT radiolarians as intricate spherical silica lattices with radiating spines and nested inner shells in cool ivory and glassy blue-white, both packed edge to edge at the same small uniform scale with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped LEFT amber RIGHT glassy pale blue",
        "environment": "a deep black seamless studio void, both wearing black patent platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "two hard rim lights behind at 45 degrees left and right carving the outer silhouettes, frontal bounce at 20 percent only, no light source visible in frame",
        "style": "scientific fashion editorial",
        "quality": Q23,
    },
    "bp_duo_pollen_wingscale_mature": {
        "tag": "Pollen and Wing Scale SEM Duo Body Paint",
        "subject": "two fine art female models in their mid thirties with false-color scanning electron micrograph body paint, standing shoulder to shoulder with no gap between them",
        "body": "both athletic hourglass builds with defined waists and shoulders, LEFT dark brown hair in a high tight bun and RIGHT copper-red hair long and loose, LEFT angled away at 45 degrees with hips turned back and torso twisting forward so the chest rotates toward the lens with head turned over the shoulder, RIGHT in contrapposto facing camera with one hand raised to the collarbone, inner shoulders pressed together",
        "outfit": "body fully painted with: one continuous false-color SEM field spanning both bodies — LEFT pollen grains as hundreds of spherical echinate grains studded with conical spines in magenta violet and lime against charcoal, RIGHT butterfly wing scales as overlapping flat scales laid like roof tiles in perfect rows each ridged with fine parallel ribs in teal gold and bronze against charcoal, at the seam loose pollen grains scattering onto the right figure's tiled surface and lodging between the rows, same small uniform scale throughout with no ground unfilled, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped LEFT saturated magenta RIGHT metallic teal",
        "environment": "a dark grey seamless studio cyclorama, both wearing charcoal matte platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "key from the front right at 45 degrees raking across both torsos to carve the waists, secondary rim from behind left separating the shoulders",
        "style": "scientific fashion editorial",
        "quality": Q23,
    },
    "bp_duo_stomata_rootsection_mature": {
        "tag": "Stomata and Root Section Duo Body Paint",
        "subject": "two fine art female models in their mid thirties with false-color plant micrograph body paint, standing shoulder to shoulder with no gap between them",
        "body": "both athletic hourglass builds with defined waists and shoulders, LEFT platinum blonde cropped short and RIGHT dark brown in a high sculpted bun, LEFT in near-profile at 70 degrees with torso rotating forward so the chest opens toward the lens, RIGHT holding the exact mirror, inner shoulders overlapping and inner forearms crossed at waist height, outer hands on outer hips, both facing camera",
        "outfit": "body fully painted with: false-color plant micrograph texture — LEFT leaf epidermis as a dense mosaic of interlocking jigsaw-edged pavement cells with hundreds of small lens-shaped stomata flanked by kidney-shaped guard cells, RIGHT root cross section as concentric rings of tightly packed cortical cells radiating from a central stele with xylem arms forming a star at the core, both in jade green teal and pale mint at the same small scale with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped lacquered saturated jade green",
        "environment": "a deep near-black seamless studio void, both wearing pale mint patent platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "key from the front left at 45 degrees modeling both busts and waists, secondary rim from behind right separating the shoulders",
        "style": "scientific fashion editorial",
        "quality": Q23,
    },
    "bp_duo_peristome_sporeridge_mature": {
        "tag": "Peristome and Spore Ridge Duo Body Paint",
        "subject": "two fine art female models with false-color bryophyte micrograph body paint, one in her late thirties and one in her mid forties, standing shoulder to shoulder with no gap between them",
        "body": "both hourglass figures with narrow waists and broad rounded hips, LEFT dark brown hair in two low braids and RIGHT black hair long and loose, LEFT with her back mostly to camera at 45 degrees and weight on one leg with hip pushed out and head turned back over the shoulder, RIGHT facing camera in mid-turn with one foot crossing behind the other and torso rotating so one shoulder leads, LEFT's inner hand resting on RIGHT's forearm",
        "outfit": "body fully painted with: false-color bryophyte micrograph texture — LEFT moss peristome teeth as rings of slender tapered teeth radiating from repeated circular centers each cross-barred with fine horizontal ridges, RIGHT fern spore ornamentation as hundreds of rounded trilete spores each marked with a Y-shaped scar and wrapped in low winding surface ridges with fine granular texture filling the gaps and no spines or projections, both in burnt sienna ochre and pale bone at the same small scale with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped lacquered matte burnt sienna",
        "environment": "a deep near-black seamless studio void, both wearing matte ochre platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front right at 45 degrees raking across both bodies from the same side to carve the turned hip and the rotating torso, weak rim from behind left, not symmetrical two-sided lighting",
        "style": "scientific fashion editorial",
        "quality": Q23,
    },
    "bp_duo_leafskeleton_ginkgovein_mature": {
        "tag": "Leaf Skeleton and Ginkgo Vein Duo Body Paint",
        "subject": "two fine art female models in their early thirties with false-color cleared-leaf micrograph body paint, standing shoulder to shoulder with no gap between them",
        "body": "both dramatic hourglass figures with narrow waists flaring to full hips, LEFT black hair in a high sleek ponytail and RIGHT dark copper long and straight, LEFT in near-profile at 70 degrees with spine long and chest opening toward the lens and one arm lifted to shoulder height, RIGHT kneeling on one knee beside her with torso upright and squared to camera and one hand on the raised knee, LEFT's inner hand resting on RIGHT's shoulder",
        "outfit": "body fully painted with: false-color cleared-leaf micrograph texture — LEFT angiosperm vein skeleton as a branching hierarchy of thick primary veins dividing into secondaries then into an extremely fine reticulate mesh with every areole filled by still finer veinlets, RIGHT ginkgo dichotomous venation as parallel veins in fanned bundles each splitting cleanly into two equal branches again and again without reconnecting and sweeping around the body's curves, both in deep jade moss green and pale chartreuse at the same small scale with vein density high everywhere and no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped lacquered matte jade",
        "environment": "a deep black seamless studio void, both wearing matte moss-green platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front left at 45 degrees raking across both bodies from the same side to carve the standing waist and the kneeling thigh, weak rim from behind right, not symmetrical two-sided lighting",
        "style": "scientific fashion editorial",
        "quality": Q23,
    },

    # ───────────────────────── TRIO 10 ─────────────────────────
    "bp_trio_indigo_resist_mature": {
        "tag": "Indigo Resist Three Techniques Trio Body Paint",
        "subject": "three fine art female models with indigo resist-dye body paint, aged mid thirties early forties and early sixties, in a row with no gap between them",
        "body": "all three hourglass figures with defined waists and rounded hips, LEFT black hair in a high tight bun CENTER dark brown in two low braids RIGHT grey-white wrapped in a cotton band, LEFT angled away at 45 degrees with hips turned back and torso twisting forward and head turned over the shoulder, CENTER seated on a low bench with hips angled to one side and torso twisting toward camera, RIGHT standing in near-profile at 70 degrees with chest opening toward the lens and one arm lifted, LEFT and RIGHT hands resting on CENTER's shoulder and forearm",
        "outfit": "body fully painted with: indigo resist-dye patterns — LEFT Japanese shibori with kumo spiderweb rings itajime folded triangles and fine kanoko dots, CENTER Indian bandhani as thousands of tiny tied-dot circles in dense concentric rings and diamond fields, RIGHT Yoruba adire eleko with olokun concentric rings and ibadandun grid squares each holding a different small symbol and comb-drawn line bands, all three in the same deep indigo and undyed white register with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped lacquered matte indigo",
        "environment": "a whitewashed studio wall with three indigo cloth panels mounted behind one per figure, all three in matte white platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front right at 45 degrees raking across all three bodies from the same side, weak rim from behind left, not symmetrical multi-sided lighting",
        "style": "high fashion editorial meeting textile craft",
        "quality": Q34,
    },
    "bp_trio_mineral_section_mature": {
        "tag": "Mineral Cross-Section Trio Body Paint",
        "subject": "three fine art female models with mineral cross-section body paint, aged mid thirties mid forties and early fifties, in a row with no gap between them",
        "body": "all three dramatic hourglass figures with narrow waists flaring to full hips, LEFT dark copper long and straight CENTER black sleek low knot RIGHT silver-grey cropped short, LEFT in deep contrapposto facing camera with outer hip pushed far to the side, CENTER seated cross-legged on a low platform with torso upright and squared to camera, RIGHT in mid-turn with one foot crossing behind the other and torso rotating so one shoulder leads, LEFT and RIGHT hands resting on CENTER's shoulders",
        "outfit": "body fully painted with: mineral cross-section texture — LEFT banded agate as concentric bands of translucent grey white and pale blue in tight parallel curves each edged with a fine crystalline line wrapping the body's contours, CENTER malachite as tight concentric botryoidal rings graded deep green to pale mint nested against one another, RIGHT mica schist as overlapping platy flakes in silver-grey and pale green aligned in continuous wavy foliation streams with tiny garnet spots, all at the same small scale in one cool mineral register with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long coffin-shaped LEFT pale grey CENTER deep green RIGHT silver",
        "environment": "a deep charcoal seamless studio void, all three in matte charcoal platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front left at 45 degrees raking across all three bodies from the same side, weak rim from behind right, not symmetrical multi-sided lighting",
        "style": "scientific fashion editorial",
        "quality": Q34,
    },
    "bp_trio_islamic_geometry_mature": {
        "tag": "Islamic Geometry Trio Body Paint",
        "subject": "three fine art female models with Islamic geometric tilework body paint, aged mid thirties early forties and early fifties, in a row with no gap between them",
        "body": "all three dramatic hourglass figures with sharply defined waists and broad rounded hips, LEFT black long and straight centre-parted CENTER dark brown in a smooth turban twist RIGHT silver-grey in a long single braid, LEFT in full profile at 90 degrees with chest rotating toward the lens and one arm extended down the thigh, CENTER seated on a low stone ledge with hips angled to one side and torso twisting back toward camera, RIGHT in mid-turn with one foot crossing behind the other and the waist twisting and one arm raised to the collarbone, LEFT and RIGHT hands on CENTER's shoulder and forearm",
        "outfit": "body fully painted with: Islamic geometric tilework — LEFT girih strapwork as interlocking ten and twelve point stars linked by continuous ribbon bands with every enclosed cell filled by a smaller rosette, CENTER zellige mosaic as thousands of small hand-cut tile shapes fitted edge to edge with fine white grout lines, RIGHT muqarnas cell projection as tiers of nested niche cells drawn as flat tessellation each filled with tiny arabesque scrollwork, all in lapis blue turquoise and bone white at the same small scale with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", nails long almond-shaped lacquered matte lapis blue",
        "environment": "a pale limestone courtyard with one carved plaster panel mounted behind each figure, all three in bone-white platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front right at 45 degrees raking across all three bodies from the same side, weak rim from behind left, not symmetrical multi-sided lighting",
        "style": "high fashion editorial meeting architectural craft",
        "quality": Q34,
    },
    "bp_trio_ceramic_glaze_mature": {
        "tag": "Ceramic Glaze Trio Body Paint",
        "subject": "three fine art female models with ceramic glaze body paint, aged mid thirties early forties and early sixties, in a row with no gap between them",
        "body": "all three dramatic hourglass figures with narrow waists flaring to full hips, LEFT black blunt bob at the jaw CENTER black high sculpted bun with a lacquer pin RIGHT white-grey in a low smooth knot, LEFT in deep contrapposto facing camera with outer hip pushed far to the side and one hand on that hip, CENTER seated cross-legged on a low dark plinth with hands on her knees, RIGHT in near-profile at 70 degrees with chest opening toward the lens and one arm lifted, LEFT and RIGHT hands resting on CENTER's shoulders",
        "outfit": "body fully painted with: ceramic glaze surface — LEFT Goryeo celadon as pale jade-green glaze under a dense network of fine crackle with inlaid sanggam cranes and clouds in white and black slip, CENTER blue-and-white porcelain as cobalt underglaze peony scrolls wave bands and lotus panels in tightly packed registers with soft bled brushwork edges, RIGHT raku ware as crawling matte glaze in charcoal and bone white with dense crazing irregular pooling and small iron speckles, all in one ceramic register with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": "fine art body paint — matte glaze finish with no mirror gloss and no wet sheen, skin pores and texture visible beneath the glaze so it reads as pigment on skin not porcelain plating, paint ends at wrist and ankle in one thin crisp border with hands and feet bare, nails long coffin-shaped LEFT celadon green CENTER cobalt blue RIGHT charcoal, NO clothing NO fabric",
        "environment": "a dark studio with three ceramic vessels on plinths behind one per figure, LEFT celadon-green CENTER cobalt-blue RIGHT matte black platform stiletto sandals all 3cm platform with open toe showing painted toenails",
        "lighting": "a single hard key from the front left at 45 degrees raking across all three bodies from the same side, weak rim from behind right, not symmetrical multi-sided lighting",
        "style": "high fashion editorial meeting ceramic craft",
        "quality": Q34,
    },
    "bp_trio_frost_crystal_mature": {
        "tag": "Frost and Crystal Growth Trio Body Paint",
        "subject": "three fine art female models with crystal growth structure body paint, aged mid thirties mid forties and early fifties, standing in a row with no gap between them",
        "body": "all three dramatic hourglass figures with narrow waists flaring to broad rounded hips, LEFT icy platinum long and glass-straight CENTER jet black slicked back tight RIGHT silver-grey blunt bob at the jaw, LEFT half a step forward in full profile at 90 degrees with chest rotating toward the lens, CENTER square to camera in deep contrapposto with outer hip pushed far to one side and arms held away from the ribs, RIGHT half a step back angled away at 45 degrees with hips turned back and head turned back over the shoulder, LEFT and RIGHT hands resting on CENTER's shoulders",
        "outfit": "body fully painted with: crystal growth structure — LEFT window hoarfrost as feathered fern-like ice fronds branching in overlapping fans each edged with fine barbs, CENTER dendritic manganese as black tree-like mineral dendrites branching endlessly at sharp angles across a pale stone ground, RIGHT snow crystal plates as hexagonal stellar dendrites packed edge to edge each with six symmetrical arms and internal plate structure, all in pale ice blue white and shadow grey with every crystal unit the same size no wider than a thumbnail and no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", no glitter and no specular sparkle, shapes flat and graphic never raised off the skin, nails long coffin-shaped lacquered matte ice blue",
        "environment": "a deep near-black seamless studio void, all three in matte pale-grey platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front left at 45 degrees raking across all three bodies from the same side, weak rim from behind right, not symmetrical multi-sided lighting",
        "style": "scientific fashion editorial",
        "quality": Q34,
    },
    "bp_trio_interlace_manuscript_mature": {
        "tag": "Insular and Norse Interlace Trio Body Paint",
        "subject": "three fine art female models with insular and Norse interlace body paint, aged mid thirties early forties and early fifties, in a row with no gap between them",
        "body": "all three dramatic hourglass figures with narrow waists flaring to full rounded hips, LEFT deep copper red long and straight CENTER black tight high bun RIGHT silver-white cropped short and swept back, LEFT in deep contrapposto facing camera with outer hip pushed far to the side and one arm raised overhead lengthening the ribcage, CENTER kneeling on one knee with torso upright and rotating slightly toward the lens, RIGHT angled away at 45 degrees with hips turned back and torso twisting forward and head turned over the shoulder, LEFT and RIGHT hands resting on CENTER's shoulders",
        "outfit": "body fully painted with: insular and Norse interlace — LEFT Book of Kells carpet page as dense ribbon interlace weaving over and under without end with tiny spiral triskele bosses and fine red dot borders, CENTER Celtic knotwork as continuous broad-band plaitwork in tight symmetrical panels bordered by key-fret step patterns, RIGHT Urnes style Norse carving as slender elongated beasts with almond eyes looping into thin tendril interlace that never closes, all in vellum cream iron-gall black orpiment gold and vermilion at the same small scale and line weight with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_MATTE + ", no metallic flare even in the gold areas, nails long almond-shaped LEFT vermilion CENTER antique gold RIGHT iron black",
        "environment": "a dim stone hall with one illuminated manuscript page mounted behind each figure, LEFT oxblood CENTER antique-gold RIGHT matte black platform stiletto sandals all 3cm platform with open toe showing painted toenails",
        "lighting": "a single hard key from the front left at 45 degrees raking across all three bodies from the same side, weak rim from behind right, not symmetrical multi-sided lighting",
        "style": "high fashion editorial meeting manuscript craft",
        "quality": Q34,
    },
    "bp_trio_cartography_mature": {
        "tag": "Cartography and Engraving Trio Body Paint",
        "subject": "three fine art female models with engraved paper illustration body paint, aged mid thirties mid forties and early fifties, standing in a row with no gap between them",
        "body": "all three dramatic hourglass figures with narrow waists flaring to full hips, LEFT dark copper long and straight CENTER black high sculpted bun RIGHT silver-grey in a long single braid, LEFT half a step forward in deep contrapposto facing camera with outer hip pushed far to the side, CENTER half a step back angled away at 45 degrees with hips turned back and torso twisting forward and head turned over the shoulder, RIGHT in full profile at 90 degrees with chest rotating toward the lens and one arm lifted overhead, LEFT and RIGHT hands resting on CENTER's shoulders",
        "outfit": "body fully painted with: engraved paper illustration — LEFT topographic survey map as dense concentric contour lines following the body's own relief and tightening where the form steepens with hatched cliff marks and fine stream lines between, CENTER antique star chart as constellation figures in fine line joined by ruled lines between stars of graded size over a grid of ecliptic circles, RIGHT botanical copperplate engraving as leaves seed heads and root systems in tight parallel and cross hatching each labelled in small italic script, all in sepia ink on aged paper cream at the same line spacing with no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_INK + ", nails long almond-shaped lacquered matte sepia",
        "environment": "a dim archive room with three framed engravings mounted behind one per figure, all three in matte parchment-cream platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front right at 45 degrees raking across all three bodies from the same side, weak rim from behind left, not symmetrical multi-sided lighting",
        "style": "high fashion editorial meeting print study",
        "quality": Q34,
    },
    "bp_trio_architectural_section_mature": {
        "tag": "Architectural Drafting Trio Body Paint",
        "subject": "three fine art female models with architectural drafting body paint, aged mid thirties early forties and early sixties, standing in a row with no gap between them",
        "body": "all three full hourglass figures with sharply defined waists and broad hips, LEFT platinum blonde sharp asymmetric bob CENTER black high sculpted bun RIGHT white-grey cropped short and swept back, LEFT half a step back in mid-turn with one foot crossing behind the other and one arm raised to the collarbone, CENTER half a step forward square to camera in deep contrapposto with outer hip pushed far to one side, RIGHT in near-profile at 70 degrees with chest opening toward the lens and one arm lifted to shoulder height, LEFT and RIGHT hands resting on CENTER's shoulders",
        "outfit": "body fully painted with: architectural drafting — LEFT Gothic cathedral section as ribbed vaults flying buttresses and clustered piers in elevation with every stone course ruled in and tracery windows detailed to the mullion and fine dimension lines running the full height, CENTER dome projection as nested plan and section of a hemispherical dome with coffered ceiling in radiating perspective and construction arcs left visible, RIGHT Japanese timber joinery as exploded axonometric of mortise tenon and dovetail joints with wood grain in fine parallel strokes and assembly arrows and small kanji annotations, all in graphite grey and blue-black on bone white at the same line spacing with the smallest elements no wider than a fingernail and no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_INK + ", nails long almond-shaped lacquered matte graphite",
        "environment": "a drafting studio with three large drawings pinned to the wall behind one per figure, all three in matte bone-white platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front right at 45 degrees raking across all three bodies from the same side, weak rim from behind left, not symmetrical multi-sided lighting",
        "style": "high fashion editorial meeting drafting study",
        "quality": Q34,
    },
    "bp_trio_natural_history_plate_mature": {
        "tag": "Natural History Plate Trio Body Paint",
        "subject": "three fine art female models with hand-coloured natural history engraving body paint, aged mid thirties early forties and early sixties, standing in a row with no gap between them",
        "body": "all three dramatic hourglass figures with defined waists and full rounded hips, LEFT dark brown long and straight CENTER black low twisted chignon RIGHT grey-white high tight bun, LEFT half a step back in deep contrapposto facing camera with outer hip pushed far to the side and one arm raised overhead, CENTER half a step forward in mid-turn with one foot crossing behind the other and the waist twisting, RIGHT in full profile at 90 degrees with chest rotating toward the lens and one arm extended down the thigh, LEFT and RIGHT hands resting on CENTER's shoulders",
        "outfit": "body fully painted with: hand-coloured natural history engraving — LEFT ornithological plate with birds in profile at varied scales every feather barb in fine hatching perched on stippled branch fragments and small italic binomial names beneath, CENTER entomological plate with beetles moths and wasps in ordered rows their wing venation and elytra punctation in fine line each with a numbered pin label and scale bar, RIGHT conchological plate with gastropod and bivalve shells from three aspects each their whorls and ribbing built from tight parallel hatching with stippled cast shadow, all in sepia line with muted hand-applied watercolour washes on aged paper cream tiled densely enough to fill every surface, painted on bare skin NO clothing NO fabric",
        "material": MAT_INK + ", nails long almond-shaped lacquered matte sepia",
        "environment": "a natural history library with three framed hand-coloured plates behind one per figure, all three in matte parchment-cream platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front right at 45 degrees raking across all three bodies from the same side, weak rim from behind left, not symmetrical multi-sided lighting",
        "style": "high fashion editorial meeting print study",
        "quality": Q34,
    },
    "bp_trio_woodblock_line_mature": {
        "tag": "Woodblock and Silverpoint Trio Body Paint",
        "subject": "three fine art female models with printed line illustration body paint, aged mid thirties mid forties and early fifties, standing in a row with no gap between them",
        "body": "all three dramatic hourglass figures with narrow waists flaring to broad rounded hips, LEFT black blunt bob at the jaw CENTER dark auburn sculpted finger-wave RIGHT silver-white long and glass-straight, LEFT half a step forward angled away at 45 degrees with hips turned back and torso twisting forward and head turned over the shoulder, CENTER half a step back in near-profile at 70 degrees with chest opening toward the lens and one arm lifted, RIGHT square to camera in deep contrapposto with outer hip pushed far to one side and one hand on that hip, LEFT and RIGHT hands resting on CENTER's shoulders",
        "outfit": "body fully painted with: printed line illustration — LEFT ukiyo-e woodblock key-block as bold outline drawing of wave crests pine boughs and drifting cloud bands filled with flat limited-palette colour blocks with slightly offset registration and fine bokashi gradation at the horizon, CENTER Victorian wood engraving as dense white-line engraving on black with foliage drapery and architectural fragments built entirely from parallel and cross-hatched strokes and tone achieved by line spacing alone, RIGHT silverpoint drawing as extremely fine grey metal lines on prepared ground layering contour studies of hands leaves and folded cloth building tone through repetition, all at the same line spacing with the smallest elements no wider than a fingernail and no unpainted ground, painted on bare skin NO clothing NO fabric",
        "material": MAT_INK + ", nails long almond-shaped LEFT indigo CENTER iron black RIGHT silver-grey",
        "environment": "a print workshop with three framed prints mounted behind one per figure, all three in matte bone-white platform stiletto sandals with 3cm platform and open toe showing painted toenails",
        "lighting": "a single hard key from the front left at 45 degrees raking across all three bodies from the same side, weak rim from behind right, not symmetrical multi-sided lighting",
        "style": "high fashion editorial meeting print study",
        "quality": Q34,
    },
}

FIELDS = ["tag", "subject", "body", "outfit", "material",
          "environment", "lighting", "style", "quality"]


def main():
    os.makedirs(PRESETS_DIR, exist_ok=True)
    fixed = 0

    for key, body in PRESETS.items():
        missing = [f for f in FIELDS if f not in body]
        if missing:
            raise RuntimeError(f"{key}: 필드 누락 {missing}")

        if not body["outfit"].startswith("body fully painted with:"):
            raise RuntimeError(f"{key}: outfit 이 'body fully painted with:' 로 시작하지 않음")

        payload = {f: body[f] for f in FIELDS}
        path = os.path.join(PRESETS_DIR, f"{key}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print(f"✅ 스키마 변환: {key}.json")
        fixed += 1

    print(f"\n총 {fixed}개 재작성 완료 (9필드 스키마)")
    print("※ presets_meta.py / hof_tier.py 는 이미 등록됨 — 추가 패치 불필요")


if __name__ == "__main__":
    main()
