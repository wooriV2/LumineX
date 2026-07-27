# -*- coding: utf-8 -*-
"""
patch_bp_hof_3_trio.py
Bodypaint HOF - TRIO 10종 presets/*.json 생성

실행:
    $env:PYTHONUTF8 = "1"
    cd C:\\Dev\\LumineX
    python preset_builders\\patch_bp_hof_3_trio.py
"""
import json
import os

PRESETS_DIR = "presets"
CATEGORY = "🎨 Bodypaint"

TAIL_MATTE = (
    "SURFACE — MANDATORY: bone-dry chalky matte finish, NO wet sheen, NO gloss, NO specular "
    "highlight. Shapes stay flat and graphic, never bulging off the skin.\n"
    "Pigment applied directly on bare skin, pores and skin texture visible.\n"
    "Motifs tightly repeated so each pattern reads as continuous texture at full-body scale.\n"
    "No panel, no band, no skirt or bodice shape.\n"
    "The paint ends at the wrist and ankle in ONE thin crisp border no thicker than a fingerwidth; "
    "hands and feet bare. No second band anywhere.\n"
    "ALL SIX hands fully visible, five separated fingers each, correct anatomy.\n"
)

TAIL_INK = (
    "SURFACE — MANDATORY: bone-dry chalky matte finish, NO wet sheen, NO gloss. Ink lines sit flat "
    "in the skin, slightly soft at the edges as printed ink would be.\n"
    "Pigment applied directly on bare skin, pores and skin texture visible.\n"
    "Line work dense enough that the hatching reads as continuous tone at full-body scale.\n"
    "No panel, no band, no skirt or bodice shape.\n"
    "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
    "ALL SIX hands fully visible, five separated fingers each.\n"
)

PRESETS = {
    "bp_trio_indigo_resist_mature": {
        "label": "🌀 인디고 방염 삼기법 — 30·40·60대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women in a row, evenly spaced with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: early forties. RIGHT: early sixties.\n"
            "All three hourglass figures, defined waists and rounded hips.\n"
            "LEFT hair: black, high tight bun. CENTER hair: dark brown, two low braids. "
            "RIGHT hair: grey-white, wrapped in a cotton band.\n\n"
            "POSE — THREE DIFFERENT STANCES, NOT mirror images, staggered heights:\n"
            "LEFT is angled away at 45 degrees with hips turned back, torso twisting forward so the "
            "chest rotates toward the lens, head turned over the shoulder.\n"
            "CENTER sits on a low bench, hips angled to one side, torso twisting toward the camera, one "
            "hand planted on the bench behind her.\n"
            "RIGHT stands in near-profile at 70 degrees, chest opening toward the lens, one arm lifted "
            "to shoulder height.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's forearm.\n\n"
            "Body fully painted with: indigo resist-dye patterns, no unpainted ground anywhere.\n"
            "LEFT — Japanese shibori: tight kumo spiderweb rings over the shoulders, itajime folded "
            "triangles down the torso, fine kanoko dots covering arms and legs, deep indigo and undyed "
            "white.\n"
            "CENTER — Indian bandhani: thousands of tiny tied-dot circles in dense concentric rings and "
            "diamond fields, the same deep indigo and white at the same small scale.\n"
            "RIGHT — Yoruba adire eleko: pale cassava-paste resist patterns on indigo — olokun "
            "concentric rings across the torso, ibadandun grid squares each filled with a different "
            "small symbol, comb-drawn line bands down the limbs, same indigo and white.\n"
            "All three share one indigo register so the group reads as a single dye study. No transition "
            "or blending between figures is needed.\n\n"
            + TAIL_MATTE +
            "Nails long coffin-shaped, all three lacquered matte indigo.\n\n"
            "Footwear: all three wear matte white platform stiletto sandals, 3cm platform, open toe with "
            "painted toenails visible.\n"
            "Environment: a whitewashed studio wall, three indigo cloth panels mounted behind, one per "
            "figure.\n"
            "LIGHTING: a single hard key from the front right at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind left. NOT symmetrical multi-sided lighting.\n"
            "Style: high fashion editorial meeting textile craft. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
    "bp_trio_mineral_section_mature": {
        "label": "💎 광물 박편 삼종 — 30·40·50대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women in a row, evenly spaced with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: mid forties. RIGHT: early fifties.\n"
            "All three dramatic hourglass figures, narrow waists flaring to full hips.\n"
            "LEFT hair: dark copper, long and straight. CENTER hair: black, sleek low knot. "
            "RIGHT hair: silver-grey, cropped short.\n\n"
            "POSE — THREE DIFFERENT STANCES, NOT mirror images, staggered heights:\n"
            "LEFT stands in deep contrapposto facing the camera, outer hip pushed far to the side, one "
            "hand on that hip.\n"
            "CENTER sits cross-legged on a low platform, torso upright and squared to the camera, hands "
            "resting on her knees.\n"
            "RIGHT is mid-turn, one foot crossing behind the other, torso rotating so one shoulder "
            "leads, head turned to the lens.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's opposite shoulder.\n\n"
            "Body fully painted with: mineral cross-section texture, no unpainted ground anywhere.\n"
            "LEFT — banded agate: concentric bands of translucent grey, white and pale blue following "
            "one another in tight parallel curves, each band edged with a fine crystalline line, the "
            "bands wrapping around the body's contours.\n"
            "CENTER — malachite: tight concentric botryoidal rings in graded deep green to pale mint, "
            "each ring cluster nested against its neighbours, at the same small scale.\n"
            "RIGHT — mica schist: overlapping platy flakes in silver-grey and pale green aligned in "
            "continuous wavy foliation streams, tiny garnet spots set into the flow, same scale.\n"
            "All three share one cool mineral register so the group reads as a single specimen study. "
            "No transition or blending between figures is needed.\n\n"
            + TAIL_MATTE +
            "Nails long coffin-shaped — LEFT matte pale grey, CENTER matte deep green, RIGHT matte "
            "silver.\n\n"
            "Footwear: all three wear matte charcoal platform stiletto sandals, 3cm platform, open toe "
            "with painted toenails visible.\n"
            "Environment: a deep charcoal seamless studio void.\n"
            "LIGHTING: a single hard key from the front left at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind right. NOT symmetrical multi-sided lighting.\n"
            "Style: scientific fashion editorial. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
    "bp_trio_islamic_geometry_mature": {
        "label": "✴️ 기리 × 젤리주 × 무카르나스 — 30·40·50대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women in a row, evenly spaced with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: early forties. RIGHT: early fifties.\n"
            "All three dramatic hourglass figures, sharply defined waists and broad rounded hips.\n"
            "LEFT hair: black, long and straight, centre-parted. CENTER hair: dark brown, wrapped in a "
            "smooth turban twist. RIGHT hair: silver-grey, long single braid over one shoulder.\n\n"
            "POSE — THREE DIFFERENT STANCES, NOT mirror images, staggered heights:\n"
            "LEFT stands in full profile at 90 degrees, spine long, chest rotating toward the lens, one "
            "arm extended down the thigh, head turned to the camera.\n"
            "CENTER sits on a low stone ledge, hips angled to one side, torso twisting back toward the "
            "camera, one hand planted on the ledge behind her.\n"
            "RIGHT is mid-turn, one foot crossing behind the other, torso rotating so one shoulder "
            "leads and the waist twists, one arm raised to the collarbone.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's forearm.\n\n"
            "Body fully painted with: Islamic geometric tilework, no unpainted ground anywhere.\n"
            "LEFT — girih strapwork: interlocking ten- and twelve-point stars linked by continuous "
            "ribbon bands, every enclosed cell filled with a smaller rosette, in lapis blue, turquoise "
            "and bone white.\n"
            "CENTER — zellige mosaic: thousands of small hand-cut tile shapes — stars, crosses, "
            "chevrons, sabres — fitted edge to edge with fine white grout lines, in the SAME lapis, "
            "turquoise and bone white palette at the same small scale.\n"
            "RIGHT — muqarnas cell projection: tiers of nested niche cells drawn as a flat tessellation, "
            "each cell outlined and filled with tiny arabesque scrollwork, same palette, same scale.\n"
            "All three share one palette and grout register so the group reads as a single tile study. "
            "No transition or blending between figures is needed.\n\n"
            + TAIL_MATTE +
            "Nails long almond-shaped, all three lacquered matte lapis blue.\n\n"
            "Footwear: all three wear bone-white platform stiletto sandals, 3cm platform, open toe with "
            "painted toenails visible.\n"
            "Environment: a pale limestone courtyard, one carved plaster panel mounted behind each "
            "figure.\n"
            "LIGHTING: a single hard key from the front right at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind left. NOT symmetrical multi-sided lighting.\n"
            "Style: high fashion editorial meeting architectural craft. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
    "bp_trio_ceramic_glaze_mature": {
        "label": "🏺 청자 빙렬 × 청화 × 라쿠 — 30·40·60대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women in a row, evenly spaced with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: early forties. RIGHT: early sixties.\n"
            "All three dramatic hourglass figures, narrow waists flaring to full hips.\n"
            "LEFT hair: black, blunt bob cut at the jaw. CENTER hair: black, high sculpted bun with a "
            "single lacquer pin. RIGHT hair: white-grey, pulled into a low smooth knot.\n\n"
            "POSE — THREE DIFFERENT STANCES, NOT mirror images, staggered heights:\n"
            "LEFT stands in deep contrapposto facing the camera, weight on one leg, outer hip pushed far "
            "to the side, one hand resting on that hip.\n"
            "CENTER sits cross-legged on a low dark plinth, torso upright and squared to the camera, "
            "hands resting on her knees.\n"
            "RIGHT stands in near-profile at 70 degrees, spine long, chest opening toward the lens, one "
            "arm lifted to shoulder height.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's opposite shoulder.\n\n"
            "Body fully painted with: ceramic glaze surface, no unpainted ground anywhere.\n"
            "LEFT — Goryeo celadon: pale jade-green glaze covered by a DENSE network of fine crackle "
            "lines, and inlaid sanggam cranes and clouds in white and black slip scattered across the "
            "field, the crackle tight and continuous everywhere.\n"
            "CENTER — blue-and-white porcelain: cobalt underglaze painting on white — peony scrolls, "
            "wave bands and lotus panels covering every surface in tightly packed registers, brushwork "
            "edges soft where the cobalt bled.\n"
            "RIGHT — raku ware: crawling matte glaze in charcoal and bone white, dense crazing and "
            "irregular pooling across the whole surface, small iron speckles throughout.\n"
            "All three share one ceramic register so the group reads as a single kiln study. No "
            "transition or blending between figures is needed.\n\n"
            "SURFACE — MANDATORY: matte glaze finish, no mirror gloss, no wet sheen. Skin pores and "
            "texture visible beneath the glaze so it reads as pigment on skin, not as porcelain plating.\n"
            "Pigment applied directly on bare skin. Motifs small and tightly repeated so each pattern "
            "reads as continuous texture. No panel, no band, no skirt or bodice shape.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "ALL SIX hands fully visible, five separated fingers each.\n"
            "Nails long coffin-shaped — LEFT matte celadon green, CENTER matte cobalt blue, RIGHT matte "
            "charcoal.\n\n"
            "Footwear: LEFT celadon-green platform stiletto sandals, CENTER cobalt-blue platform "
            "stiletto mules, RIGHT matte black platform stiletto sandals — all 3cm platform, open toe "
            "with painted toenails visible.\n"
            "Environment: a dark studio, three ceramic vessels on plinths behind, one per figure.\n"
            "LIGHTING: a single hard key from the front left at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind right. NOT symmetrical multi-sided lighting.\n"
            "Style: high fashion editorial meeting ceramic craft. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
    "bp_trio_frost_crystal_mature": {
        "label": "❄️ 성에 × 수지상망간 × 눈결정 — 30·40·50대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women standing in a row with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: mid forties. RIGHT: early fifties.\n"
            "All three dramatic hourglass figures, narrow waists flaring to broad rounded hips.\n"
            "LEFT hair: icy platinum, long and glass-straight. CENTER hair: jet black, slicked back "
            "tight against the skull. RIGHT hair: silver-grey, blunt bob cut at the jaw.\n\n"
            "POSE — ALL STANDING, three different stances, staggered in DEPTH:\n"
            "LEFT stands half a step FORWARD, in full profile at 90 degrees, chest rotating toward the "
            "lens, one arm extended down the thigh, head turned to the camera.\n"
            "CENTER stands square to the camera in deep contrapposto, outer hip pushed far to one side, "
            "both arms held slightly away from the ribs so the waist pinch is unobstructed.\n"
            "RIGHT stands half a step BACK, angled away at 45 degrees with hips turned back, weight on "
            "one leg, head turned back over the shoulder toward the lens.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's opposite shoulder.\n\n"
            "Body fully painted with: crystal growth structure, no unpainted ground anywhere.\n"
            "LEFT — window hoarfrost: feathered fern-like ice fronds branching in overlapping fans, each "
            "frond edged with fine barbs, in pale ice blue, white and shadow grey.\n"
            "CENTER — dendritic manganese: black tree-like mineral dendrites branching endlessly at "
            "sharp angles across a pale stone ground, in the SAME ice blue, white and grey palette.\n"
            "RIGHT — snow crystal plates: hexagonal stellar dendrites packed edge to edge, each with six "
            "symmetrical arms and internal plate structure, same palette.\n"
            "SCALE — MANDATORY: on all three figures the individual crystal units are the SAME size, "
            "none wider than a thumbnail, so the three read as one crystallography study.\n"
            "No transition or blending between figures is needed.\n\n"
            "SURFACE — MANDATORY: bone-dry chalky matte finish, NO wet sheen, NO gloss, NO glitter, NO "
            "specular sparkle. Shapes stay flat and graphic, never raised off the skin.\n"
            "Pigment applied directly on bare skin, pores and skin texture visible.\n"
            "Motifs tightly repeated so each pattern reads as continuous texture.\n"
            "No panel, no band, no skirt or bodice shape.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "ALL SIX hands fully visible, five separated fingers each.\n"
            "Nails long coffin-shaped, all three lacquered matte ice blue.\n\n"
            "Footwear: all three wear matte pale-grey platform stiletto sandals, 3cm platform, open toe "
            "with painted toenails visible.\n"
            "Environment: a deep near-black seamless studio void.\n"
            "LIGHTING: a single hard key from the front left at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind right. NOT symmetrical multi-sided lighting.\n"
            "Style: scientific fashion editorial. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
    "bp_trio_interlace_manuscript_mature": {
        "label": "࿊ 켈스 × 켈틱노트 × 우르네스 — 30·40·50대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women in a row, evenly spaced with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: early forties. RIGHT: early fifties.\n"
            "All three dramatic hourglass figures, narrow waists flaring to full rounded hips.\n"
            "LEFT hair: deep copper red, long and straight. CENTER hair: black, tight high bun. "
            "RIGHT hair: silver-white, cropped short and swept back.\n\n"
            "POSE — THREE DIFFERENT STANCES, NOT mirror images, staggered heights:\n"
            "LEFT stands in deep contrapposto facing the camera, outer hip pushed far to the side, one "
            "arm raised overhead so the ribcage lengthens.\n"
            "CENTER kneels on one knee, torso upright and rotating slightly toward the lens, one hand on "
            "the raised knee.\n"
            "RIGHT is angled away at 45 degrees with hips turned back, torso twisting forward so the "
            "chest rotates toward the lens, head turned over the shoulder.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's opposite shoulder.\n\n"
            "Body fully painted with: insular and Norse interlace, no unpainted ground anywhere.\n"
            "LEFT — Book of Kells carpet page: dense ribbon interlace weaving over and under without "
            "end, tiny spiral triskele bosses set into the knotwork, fine red dot borders outlining "
            "every band, in vellum cream, iron-gall black, orpiment gold and vermilion.\n"
            "CENTER — Celtic knotwork: continuous broad-band plaitwork in tight symmetrical panels, each "
            "panel bordered by key-fret step patterns, in the SAME cream, black, gold and vermilion "
            "palette at the same small scale.\n"
            "RIGHT — Urnes style Norse carving: slender elongated beasts with almond eyes, their bodies "
            "looping into thin tendril interlace that never closes, same palette, same scale.\n"
            "All three share one palette and line weight so the group reads as a single manuscript "
            "study. No transition or blending between figures is needed.\n\n"
            "SURFACE — MANDATORY: bone-dry chalky matte finish, no wet sheen, no gloss, no metallic "
            "flare even in the gold areas. Skin pores and texture visible beneath the pigment.\n"
            "Pigment applied directly on bare skin. Motifs small and tightly repeated so each pattern "
            "reads as continuous texture. No panel, no band, no skirt or bodice shape.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "ALL SIX hands fully visible, five separated fingers each.\n"
            "Nails long almond-shaped — LEFT matte vermilion, CENTER matte antique gold, RIGHT matte "
            "iron black.\n\n"
            "Footwear: LEFT oxblood platform stiletto sandals, CENTER antique-gold platform stiletto "
            "mules, RIGHT matte black platform stiletto sandals — all 3cm platform, open toe with "
            "painted toenails visible.\n"
            "Environment: a dim stone hall, one illuminated manuscript page mounted behind each figure.\n"
            "LIGHTING: a single hard key from the front left at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind right. NOT symmetrical multi-sided lighting.\n"
            "Style: high fashion editorial meeting manuscript craft. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
    "bp_trio_cartography_mature": {
        "label": "🗺️ 등고선 × 성도 × 식물동판화 — 30·40·50대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women standing in a row with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: mid forties. RIGHT: early fifties.\n"
            "All three dramatic hourglass figures, narrow waists flaring to full hips.\n"
            "LEFT hair: dark copper, long and straight. CENTER hair: black, high sculpted bun. "
            "RIGHT hair: silver-grey, long single braid over one shoulder.\n\n"
            "POSE — ALL STANDING, three different stances, staggered in DEPTH:\n"
            "LEFT stands half a step FORWARD, in deep contrapposto facing the camera, outer hip pushed "
            "far to the side, one hand resting on that hip.\n"
            "CENTER stands half a step BACK, angled away at 45 degrees with hips turned back, torso "
            "twisting forward so the chest rotates toward the lens, head turned over the shoulder.\n"
            "RIGHT stands in full profile at 90 degrees, spine long, chest rotating toward the lens, one "
            "arm lifted overhead, head turned to the camera.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's opposite shoulder.\n\n"
            "Body fully painted with: engraved paper illustration, no unpainted ground anywhere.\n"
            "LEFT — topographic survey map: dense concentric contour lines following the body's own "
            "relief, tightening where the form steepens, hatched cliff marks and fine stream lines "
            "between them, in sepia ink on aged paper cream.\n"
            "CENTER — antique star chart: constellation figures drawn in fine line, joined by ruled "
            "lines between stars of graded size, a grid of ecliptic circles crossing beneath, in the "
            "SAME sepia and cream palette at the same line weight.\n"
            "RIGHT — botanical copperplate engraving: leaves, seed heads and root systems rendered in "
            "tight parallel hatching and cross-hatching, each specimen labelled in small italic script, "
            "same palette, same line weight.\n"
            "SCALE — MANDATORY: on all three figures the line spacing is the SAME, fine enough that the "
            "hatching reads as continuous tone at full-body scale.\n"
            "No transition or blending between figures is needed.\n\n"
            + TAIL_INK +
            "Nails long almond-shaped, all three lacquered matte sepia.\n\n"
            "Footwear: all three wear matte parchment-cream platform stiletto sandals, 3cm platform, "
            "open toe with painted toenails visible.\n"
            "Environment: a dim archive room, three framed engravings mounted behind, one per figure.\n"
            "LIGHTING: a single hard key from the front right at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind left. NOT symmetrical multi-sided lighting.\n"
            "Style: high fashion editorial meeting print study. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
    "bp_trio_architectural_section_mature": {
        "label": "🏛️ 고딕 단면 × 돔 투영 × 목조 이음 — 30·40·60대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women standing in a row with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: early forties. RIGHT: early sixties.\n"
            "All three full hourglass figures, sharply defined waists and broad hips.\n"
            "LEFT hair: platinum blonde, sharp asymmetric bob. CENTER hair: black, high sculpted bun. "
            "RIGHT hair: white-grey, cropped short and swept back.\n\n"
            "POSE — ALL STANDING, three different stances, staggered in DEPTH:\n"
            "LEFT stands half a step BACK, in mid-turn with one foot crossing behind the other, torso "
            "rotating so one shoulder leads, one arm raised to the collarbone.\n"
            "CENTER stands half a step FORWARD, square to the camera in deep contrapposto, outer hip "
            "pushed far to one side, both arms held slightly away from the ribs.\n"
            "RIGHT stands in near-profile at 70 degrees, spine long, chest opening toward the lens, one "
            "arm lifted to shoulder height.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's opposite shoulder.\n\n"
            "Body fully painted with: architectural drafting, no unpainted ground anywhere.\n"
            "LEFT — Gothic cathedral section: ribbed vaults, flying buttresses and clustered piers drawn "
            "in elevation, every stone course ruled in, tracery windows detailed to the mullion, fine "
            "dimension lines with tick marks running the full height.\n"
            "CENTER — dome projection: nested plan and section of a hemispherical dome, coffered ceiling "
            "laid out in radiating perspective, oculus at the centre, construction arcs and compass "
            "marks left visible on the drawing.\n"
            "RIGHT — Japanese timber joinery: exploded axonometric of mortise, tenon and dovetail "
            "joints, wood grain indicated by fine parallel strokes on every member, assembly arrows and "
            "small kanji annotations between parts.\n"
            "SCALE — MANDATORY: on all three figures the line spacing is the SAME and the smallest drawn "
            "elements are no wider than a fingernail, so the three read as one drawing set.\n"
            "No transition or blending between figures is needed.\n\n"
            "SURFACE — MANDATORY: bone-dry chalky matte finish, NO wet sheen, NO gloss. Ink lines sit "
            "flat in the skin, slightly soft at the edges, in graphite grey and blue-black on bone white "
            "ground.\n"
            "Pigment applied directly on bare skin, pores and skin texture visible.\n"
            "Line work dense enough that the hatching reads as continuous tone at full-body scale.\n"
            "No panel, no band, no skirt or bodice shape.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "ALL SIX hands fully visible, five separated fingers each.\n"
            "Nails long almond-shaped, all three lacquered matte graphite.\n\n"
            "Footwear: all three wear matte bone-white platform stiletto sandals, 3cm platform, open toe "
            "with painted toenails visible.\n"
            "Environment: a drafting studio, three large drawings pinned to the wall behind, one per "
            "figure.\n"
            "LIGHTING: a single hard key from the front right at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind left. NOT symmetrical multi-sided lighting.\n"
            "Style: high fashion editorial meeting drafting study. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
    "bp_trio_natural_history_plate_mature": {
        "label": "🪶 조류 × 곤충 × 패류 도판 — 30·40·60대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women standing in a row with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: early forties. RIGHT: early sixties.\n"
            "All three dramatic hourglass figures, defined waists and full rounded hips.\n"
            "LEFT hair: dark brown, long and straight. CENTER hair: black, low twisted chignon. "
            "RIGHT hair: grey-white, high tight bun.\n\n"
            "POSE — ALL STANDING, three different stances, staggered in DEPTH:\n"
            "LEFT stands half a step BACK, in deep contrapposto facing the camera, outer hip pushed far "
            "to the side, one arm raised overhead so the ribcage lengthens.\n"
            "CENTER stands half a step FORWARD, in mid-turn with one foot crossing behind the other, "
            "torso rotating so one shoulder leads and the waist twists.\n"
            "RIGHT stands in full profile at 90 degrees, spine long, chest rotating toward the lens, one "
            "arm extended down the thigh, head turned to the camera.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's opposite shoulder.\n\n"
            "Body fully painted with: hand-coloured natural history engraving, no unpainted ground "
            "anywhere.\n"
            "LEFT — ornithological plate: birds in profile at varied scales, every barb of every feather "
            "drawn in fine hatching, perched on stippled branch fragments, small italic binomial names "
            "beneath each specimen.\n"
            "CENTER — entomological plate: beetles, moths and wasps arranged in ordered rows, wing "
            "venation and elytra punctation rendered in fine line, each specimen with a numbered pin "
            "label and a scale bar.\n"
            "RIGHT — conchological plate: gastropod and bivalve shells drawn from three aspects each, "
            "spiral whorls and ribbing built from tight parallel hatching, cast shadow stippled beneath "
            "each shell, italic names below.\n"
            "SCALE — MANDATORY: on all three figures the hatching spacing is the SAME and no single "
            "specimen is wider than a palm, so the three read as consecutive plates from one volume.\n"
            "No transition or blending between figures is needed.\n\n"
            "SURFACE — MANDATORY: bone-dry chalky matte finish, NO wet sheen, NO gloss. Ink lines sit "
            "flat in the skin, slightly soft at the edges, in sepia line with muted hand-applied "
            "watercolour washes on aged paper cream.\n"
            "Pigment applied directly on bare skin, pores and skin texture visible.\n"
            "Specimens tiled densely enough to fill every surface with no broad blank paper.\n"
            "No panel, no band, no skirt or bodice shape.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "ALL SIX hands fully visible, five separated fingers each.\n"
            "Nails long almond-shaped, all three lacquered matte sepia.\n\n"
            "Footwear: all three wear matte parchment-cream platform stiletto sandals, 3cm platform, "
            "open toe with painted toenails visible.\n"
            "Environment: a natural history library, three framed hand-coloured plates behind, one per "
            "figure.\n"
            "LIGHTING: a single hard key from the front right at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind left. NOT symmetrical multi-sided lighting.\n"
            "Style: high fashion editorial meeting print study. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
    "bp_trio_woodblock_line_mature": {
        "label": "🌊 우키요에 × 목판화 × 은선세공 — 30·40·50대",
        "aspect_ratio": "3:4",
        "prompt": (
            "Professional fashion photograph, full body group shot.\n"
            "Three women standing in a row with NO GAP between them, arranged left to right.\n"
            "LEFT: mid thirties. CENTER: mid forties. RIGHT: early fifties.\n"
            "All three dramatic hourglass figures, narrow waists flaring to broad rounded hips.\n"
            "LEFT hair: black, blunt bob cut at the jaw. CENTER hair: dark auburn, sculpted finger-wave. "
            "RIGHT hair: silver-white, long and glass-straight.\n\n"
            "POSE — ALL STANDING, three different stances, staggered in DEPTH:\n"
            "LEFT stands half a step FORWARD, angled away at 45 degrees with hips turned back, torso "
            "twisting forward so the chest rotates toward the lens, head turned over the shoulder.\n"
            "CENTER stands half a step BACK, in near-profile at 70 degrees, spine long, chest opening "
            "toward the lens, one arm lifted to shoulder height.\n"
            "RIGHT stands square to the camera in deep contrapposto, outer hip pushed far to one side, "
            "one hand on that hip.\n"
            "CONTACT: LEFT's inner hand rests on CENTER's shoulder; RIGHT's inner hand rests on "
            "CENTER's opposite shoulder.\n\n"
            "Body fully painted with: printed line illustration, no unpainted ground anywhere.\n"
            "LEFT — ukiyo-e woodblock key-block: bold outline drawing of wave crests, pine boughs and "
            "drifting cloud bands, filled with the flat colour blocks of a limited palette, the "
            "registration slightly offset at some edges as in a real print, fine bokashi gradation at "
            "the horizon lines.\n"
            "CENTER — Victorian wood engraving: dense white-line engraving on black, foliage, drapery "
            "and architectural fragments built entirely from fine parallel and cross-hatched strokes, "
            "tonal gradation achieved by line spacing alone.\n"
            "RIGHT — silverpoint drawing: extremely fine grey metal lines on prepared ground, delicate "
            "contour studies of hands, leaves and folded cloth layered over one another, the lines "
            "building tone through repetition only.\n"
            "SCALE — MANDATORY: on all three figures the line spacing is the SAME and the smallest drawn "
            "elements are no wider than a fingernail, so the three read as one printer's study.\n"
            "No transition or blending between figures is needed.\n\n"
            "SURFACE — MANDATORY: bone-dry chalky matte finish, NO wet sheen, NO gloss. Lines sit flat "
            "in the skin, slightly soft at the edges as printed ink would be.\n"
            "Pigment applied directly on bare skin, pores and skin texture visible.\n"
            "Line work dense enough that it reads as continuous tone at full-body scale.\n"
            "No panel, no band, no skirt or bodice shape.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "ALL SIX hands fully visible, five separated fingers each.\n"
            "Nails long almond-shaped — LEFT matte indigo, CENTER matte iron black, RIGHT matte "
            "silver-grey.\n\n"
            "Footwear: all three wear matte bone-white platform stiletto sandals, 3cm platform, open toe "
            "with painted toenails visible.\n"
            "Environment: a print workshop, three framed prints mounted behind, one per figure.\n"
            "LIGHTING: a single hard key from the front left at 45 degrees, raking across ALL THREE "
            "bodies from the same side. Weak rim from behind right. NOT symmetrical multi-sided lighting.\n"
            "Style: high fashion editorial meeting print study. ultra-sharp 8K. portrait 3:4 vertical."
        ),
    },
}


def main():
    os.makedirs(PRESETS_DIR, exist_ok=True)
    created, skipped = 0, 0

    for key, body in PRESETS.items():
        path = os.path.join(PRESETS_DIR, f"{key}.json")
        if os.path.exists(path):
            print(f"⏭ 이미 존재: {key}.json")
            skipped += 1
            continue

        payload = {
            "key": key,
            "label": body["label"],
            "category": CATEGORY,
            "prompt": body["prompt"],
            "aspect_ratio": body["aspect_ratio"],
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print(f"✅ 생성: {key}.json")
        created += 1

    print(f"\n[TRIO] 총 {created}개 생성 / {skipped}개 스킵")


if __name__ == "__main__":
    main()
