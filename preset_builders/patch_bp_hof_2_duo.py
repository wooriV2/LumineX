# -*- coding: utf-8 -*-
"""
patch_bp_hof_2_duo.py
Bodypaint HOF - DUO 5종 presets/*.json 생성

실행:
    $env:PYTHONUTF8 = "1"
    cd C:\\Dev\\LumineX
    python preset_builders\\patch_bp_hof_2_duo.py
"""
import json
import os

PRESETS_DIR = "presets"
CATEGORY = "🎨 Bodypaint"

COMMON_TAIL = (
    "SURFACE — MANDATORY: bone-dry chalky matte finish, no wet sheen, no gloss, no specular "
    "highlight. Shapes stay flat and graphic, never bulging off the skin.\n"
    "Pigment applied directly on bare skin, pores and skin texture visible.\n"
    "Motifs small and tightly repeated so each pattern reads as continuous texture at full-body "
    "scale. No panel, no band, no skirt or bodice shape.\n"
    "The paint ends at the wrist and ankle in ONE thin crisp border no thicker than a fingerwidth; "
    "hands and feet bare. No second band anywhere.\n"
    "All four hands fully visible, five separated fingers each, correct anatomy.\n"
)

PRESETS = {
    "bp_duo_diatom_radiolaria_mature": {
        "label": "🔬 규조류 × 방산충 — 30·40대",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Two women standing shoulder to shoulder, arms lightly touching, NO GAP between them, "
            "matched height. LEFT: early thirties. RIGHT: early forties.\n"
            "Both hourglass figures, defined waists and full hips.\n"
            "LEFT hair: long black, slicked back wet. RIGHT hair: shaved close, geometric line cut.\n\n"
            "POSE: LEFT stands in contrapposto with the outer hip pushed away, torso twisting so the "
            "chest rotates toward the camera. RIGHT mirrors it in reverse. The two inner hips press "
            "together at the center. Inner arms hang between them, outer hands rest on the outer hips. "
            "Both look directly into the lens.\n\n"
            "Body fully painted with: a single continuous darkfield microscopy plankton field spanning "
            "BOTH bodies, no unpainted ground anywhere.\n"
            "LEFT — centric diatoms: hundreds of small radial silica frustules, each a perfect disc of "
            "concentric pore rings, in luminous amber, cream and pale gold against near-black, packed "
            "edge to edge at a small uniform scale.\n"
            "RIGHT — radiolarians: intricate spherical silica lattices with radiating spines, nested "
            "inner shells visible through the outer mesh, in cool ivory and glassy blue-white against "
            "near-black, same small uniform scale.\n\n"
            + COMMON_TAIL +
            "Nails long coffin-shaped — LEFT lacquered warm amber, RIGHT lacquered glassy pale blue.\n\n"
            "Footwear: both wear black patent platform stiletto sandals, 3cm platform, open toe with "
            "painted toenails visible.\n"
            "Environment: a deep black seamless studio void.\n"
            "Lighting: two hard rim lights behind at 45 degrees left and right carving the outer "
            "silhouettes, frontal bounce at 20% only. No light source visible in frame.\n"
            "Style: scientific fashion editorial. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_duo_pollen_wingscale_mature": {
        "label": "🦋 화분 SEM × 나비 비늘 SEM — 30대",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Two women standing shoulder to shoulder, arms lightly touching, NO GAP between them, "
            "matched height, both mid thirties. Both athletic hourglass builds, defined waists and "
            "shoulders.\n"
            "LEFT hair: dark brown in a high tight bun. RIGHT hair: copper-red, long and loose over "
            "one shoulder.\n\n"
            "POSE: LEFT is angled away at 45 degrees with hips turned back, torso twisting forward so "
            "the chest rotates toward the lens, head turned over the shoulder. RIGHT stands in "
            "contrapposto facing the camera, one hand raised to the collarbone. Their inner shoulders "
            "press together.\n\n"
            "Body fully painted with: one continuous false-color scanning electron micrograph spanning "
            "BOTH bodies, no ground left unfilled.\n"
            "LEFT — pollen grains: hundreds of spherical echinate grains densely heaped, each studded "
            "with sharp conical spines and pitted between them, in false-color magenta, violet and lime "
            "against charcoal, packed at a small uniform scale.\n"
            "RIGHT — butterfly wing scales: overlapping flat scales laid like roof tiles in perfect "
            "rows, each scale ridged with fine parallel longitudinal ribs, in false-color teal, gold "
            "and bronze against charcoal, same small uniform scale.\n\n"
            "SEAM: where their shoulders meet, loose pollen grains scatter ONTO the right figure's "
            "tiled scale surface and lodge between the rows. The transition happens ON the bodies, not "
            "in the air between them. Grain scale and charcoal ground match across it.\n\n"
            + COMMON_TAIL +
            "Nails long coffin-shaped — LEFT lacquered saturated magenta, RIGHT lacquered metallic teal.\n\n"
            "Footwear: both wear charcoal matte platform stiletto sandals, 3cm platform, open toe with "
            "painted toenails visible.\n"
            "Environment: a dark grey seamless studio cyclorama.\n"
            "Lighting: key from the front right at 45 degrees raking across both torsos to carve the "
            "waists, secondary rim from behind left separating the shoulders.\n"
            "Style: scientific fashion editorial. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_duo_stomata_rootsection_mature": {
        "label": "🌿 잎 기공 × 뿌리 횡단면 — 30대",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Two women standing shoulder to shoulder, arms lightly touching, NO GAP between them, "
            "matched height, both mid thirties. Both athletic hourglass builds, defined waists and "
            "shoulders.\n"
            "LEFT hair: platinum blonde, cropped short and textured. RIGHT hair: dark brown, in a high "
            "sculpted bun.\n\n"
            "POSE — MIRRORED: LEFT stands in near-profile at 70 degrees with the torso rotating forward "
            "so the chest opens toward the lens. RIGHT holds the exact mirror of that stance. Their "
            "inner shoulders overlap.\n"
            "CONTACT: their inner forearms cross and rest against one another at waist height. Outer "
            "hands rest on the outer hips. Both face the camera directly.\n\n"
            "Body fully painted with: false-color plant micrograph texture, no unpainted ground "
            "anywhere.\n"
            "LEFT — leaf epidermis: a dense mosaic of interlocking jigsaw-edged pavement cells outlined "
            "in fine dark line, with hundreds of small lens-shaped stomata scattered evenly between "
            "them, each flanked by a pair of kidney-shaped guard cells, in false-color jade green, teal "
            "and pale mint.\n"
            "RIGHT — root cross section: concentric rings of tightly packed cortical cells radiating "
            "outward from a central stele, the xylem arms forming a star at the core, each cell wall "
            "picked out in fine line, in the SAME jade green, teal and pale mint palette at the same "
            "small scale, the rings wrapping around the torso and limbs as if the body were the "
            "specimen itself.\n\n"
            "Both patterns share one color temperature and one ground tone so the pair reads as a "
            "single specimen plate. No transition or blending between the figures is needed.\n\n"
            + COMMON_TAIL +
            "Nails long coffin-shaped, both lacquered saturated jade green.\n\n"
            "Footwear: both wear pale mint patent platform stiletto sandals, 3cm platform, open toe "
            "with painted toenails visible.\n"
            "Environment: a deep near-black seamless studio void.\n"
            "Lighting: key from the front left at 45 degrees modeling both busts and waists, secondary "
            "rim from behind right separating the shoulders.\n"
            "Style: scientific fashion editorial. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_duo_peristome_sporeridge_mature": {
        "label": "✳ 선태류 삭치 × 포자 융선 — 30·40대",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Two women standing shoulder to shoulder, arms lightly touching, NO GAP between them, "
            "matched height. LEFT: late thirties. RIGHT: mid forties.\n"
            "Both hourglass figures, narrow waists and broad rounded hips.\n"
            "LEFT hair: dark brown in two low braids. RIGHT hair: black, long and loose over one "
            "shoulder.\n\n"
            "POSE — ASYMMETRIC PAIR, NOT mirror images:\n"
            "LEFT stands with her back mostly to the camera at 45 degrees, weight on one leg, hip "
            "pushed out, head turned back over the shoulder toward the lens.\n"
            "RIGHT faces the camera squarely in mid-turn, one foot crossing behind the other, torso "
            "rotating so one shoulder leads, one arm raised to the collarbone.\n"
            "CONTACT: LEFT's inner hand rests on RIGHT's forearm.\n\n"
            "Body fully painted with: false-color bryophyte micrograph texture, no unpainted ground "
            "anywhere.\n"
            "LEFT — moss peristome teeth: rings of slender tapered teeth radiating outward from "
            "repeated circular centers, each tooth cross-barred with fine horizontal ridges and hinged "
            "at its base, the rings tiled densely across the body, in false-color burnt sienna, ochre "
            "and pale bone.\n"
            "RIGHT — fern spore ornamentation: hundreds of rounded trilete spores, each marked with a "
            "Y-shaped scar and wrapped in low winding surface ridges, packed tightly with fine granular "
            "texture filling the gaps, in the SAME burnt sienna, ochre and pale bone palette at the "
            "same small scale. Ridges only, no spines, no projections.\n\n"
            "Both share one color temperature and ground tone so the pair reads as a single specimen "
            "plate. No transition or blending between the figures is needed.\n\n"
            + COMMON_TAIL +
            "Nails long coffin-shaped, both lacquered matte burnt sienna.\n\n"
            "Footwear: both wear matte ochre platform stiletto sandals, 3cm platform, open toe with "
            "painted toenails visible.\n"
            "Environment: a deep near-black seamless studio void.\n"
            "LIGHTING: a single hard key from the front right at 45 degrees, raking across BOTH bodies "
            "from the same side to carve the turned hip and the rotating torso. Weak rim from behind "
            "left. NOT symmetrical two-sided lighting.\n"
            "Style: scientific fashion editorial. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_duo_leafskeleton_ginkgovein_mature": {
        "label": "🍃 잎맥 골격 × 은행 이차맥 — 30대",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Two women standing shoulder to shoulder, arms lightly touching, NO GAP between them, "
            "matched height, both early thirties. Both dramatic hourglass figures, narrow waists "
            "flaring to full hips.\n"
            "LEFT hair: black, high sleek ponytail. RIGHT hair: dark copper, long and straight.\n\n"
            "POSE — ASYMMETRIC PAIR, NOT mirror images:\n"
            "LEFT stands in near-profile at 70 degrees, spine long, chest opening toward the lens, one "
            "arm lifted to shoulder height, the other at the small of the back.\n"
            "RIGHT kneels on one knee beside her, torso upright and squared to the camera, one hand "
            "resting on the raised knee, chin level.\n"
            "CONTACT: LEFT's inner hand rests on RIGHT's shoulder.\n\n"
            "Body fully painted with: false-color cleared-leaf micrograph texture, no unpainted ground "
            "anywhere.\n"
            "LEFT — angiosperm vein skeleton: a branching hierarchy of thick primary veins dividing into "
            "secondaries and then into an extremely fine reticulate mesh, every enclosed areole filled "
            "with still finer veinlets ending in blind tips, in false-color deep jade, moss green and "
            "pale chartreuse.\n"
            "RIGHT — ginkgo dichotomous venation: parallel veins running in fanned bundles, each vein "
            "splitting cleanly into two equal branches again and again without ever reconnecting, the "
            "fans sweeping around the body's curves, in the SAME deep jade, moss green and pale "
            "chartreuse palette at the same small scale.\n\n"
            "Both share one color temperature and ground tone so the pair reads as a single specimen "
            "plate. No transition or blending between the figures is needed.\n\n"
            + COMMON_TAIL +
            "Vein density stays high everywhere — no broad empty areas between branches.\n"
            "Nails long coffin-shaped, both lacquered matte jade.\n\n"
            "Footwear: both wear matte moss-green platform stiletto sandals, 3cm platform, open toe "
            "with painted toenails visible.\n"
            "Environment: a deep black seamless studio void.\n"
            "LIGHTING: a single hard key from the front left at 45 degrees, raking across BOTH bodies "
            "from the same side to carve the standing waist and the kneeling thigh. Weak rim from "
            "behind right. NOT symmetrical two-sided lighting.\n"
            "Style: scientific fashion editorial. ultra-sharp 8K. portrait 2:3 vertical."
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

    print(f"\n[DUO] 총 {created}개 생성 / {skipped}개 스킵")


if __name__ == "__main__":
    main()
