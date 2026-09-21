# -*- coding: utf-8 -*-
r"""
patch_livingartifact_colossal_priority_1_json.py
Living Artifact · Colossal — 24 solo presets
(priority 4 materials: Son Mai, Lai Rod Nam, Minakari, Khokhloma x 3 standing + 3 seated)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_colossal_priority_1_json.py
    python preset_builders\patch_livingartifact_colossal_priority_1_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · Colossal"
PLATFORM = "gemini"
ASPECT = "2:3"

STAND = ("Physique: The most colossal SuperBBW physique physically possible — gigantic soft belly hanging in multiple "
         "deep overlapping rolls down toward the thighs, not pregnant, overwhelmingly massive heavy bust resting on the "
         "upper belly, extremely wide hips far wider than the shoulders, enormous thick thighs, very broad soft arms, "
         "profound physical volume filling the entire frame width.")


def seat(spread):
    return ("Physique: The most colossal SuperBBW physique physically possible — gigantic soft belly resting in multiple "
            "deep overlapping rolls over the thighs, not pregnant, overwhelmingly massive heavy bust resting on the upper "
            f"belly, extremely wide hips {spread}, enormous thick thighs, very broad soft arms, profound physical volume "
            "filling the entire frame width.")


ARMS = "Arms kept away from the torso so the painted bust and belly are fully visible."
END = "Emphasis on the extremely large SuperBBW body volume. 2:3 vertical 8K portrait."


def build(subject, physique, art, pose, foot, nails, bg):
    return "\n\n".join([
        f"Subject: {subject}",
        physique,
        f"Body Art: {art}",
        f"Pose: {pose} Full body head to toe visible.",
        f"Footwear: {foot}\nNails: {nails}",
        f"Background & Lighting: {bg} ONE woman only. Figure fills 90% of the frame. {END}",
    ])


SM = "Full body Vietnamese son mai lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex."
LR = "Full body Thai lai rod nam lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex."
MN = "Full body Persian minakari enamel body painting from neck to ankle, painted directly on bare skin, one continuous surface, no collar band."
KH = "Full body Khokhloma lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex."
PAT = "Pelvis, inner thighs, and both arms fully patterned."

P = []  # (key, title, prompt)


def add(key, title, *args):
    P.append((key, title, build(*args)))


# ── Son Mai ──────────────────────────────────────────────
add("la_colossal_sonmai_01", "LA Colossal – Son Mai 01 (Standing)",
    "ONE extremely large SuperBBW Vietnamese woman in her early 30s, straight black hair falling to her waist, natural face with a warm smile.",
    STAND, f"{SM} Deep glossy black and vermilion lacquer with gold-leaf lotus, silver-leaf cranes, and crackled white eggshell mosaic clouds clearly visible across bust, belly rolls, hips, and legs. {PAT}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Towering 9-inch caged black lacquer platform stiletto sandals, a lattice of fine straps with gold-leaf lotus at each junction.",
    "Extra long almond nails, black with eggshell-white tips.",
    "Hue imperial citadel hall with red lacquered columns, softly blurred. Low camera angle, 85mm lens. Warm key with raking side light making the gold leaf and eggshell glow.")
add("la_colossal_sonmai_02", "LA Colossal – Son Mai 02 (Standing)",
    "ONE extremely large SuperBBW Black woman in her late 20s, long knotless box braids with small gold cuffs, natural face with a bright smile.",
    STAND, f"{SM} Deep glossy black lacquer with gold-leaf bamboo and areca palms, silver-leaf koi, and crackled white eggshell water ripples. {PAT}",
    f"Standing in a three-quarter front view, one hand lifting her braids at shoulder height, the other hand resting on her outer hip, torso turned open toward the camera. {ARMS}",
    "Very high 8-inch black lacquer platform stiletto sandals with spiral straps coiling up the calf like a vine, gold-leaf accents.",
    "Extra long coffin nails, gold leaf over black.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm gold key with raking side light and soft rim light.")
add("la_colossal_sonmai_03", "LA Colossal – Son Mai 03 (Standing)",
    "ONE extremely large SuperBBW Latina woman in her early 40s, voluminous dark brown waves past the shoulders, natural face with a confident smile.",
    STAND, f"{SM} Deep glossy vermilion-red lacquer with black borders, gold-leaf phoenixes, and large crackled white eggshell clouds. {PAT}",
    "Standing in a three-quarter front view, both hands clasped loosely behind her lower back, shoulders drawn back, chest and belly facing the camera.",
    "Towering 9-inch vermilion lacquer peep-toe platform stilettos with crossed ankle straps.",
    "Extra long stiletto nails, vermilion with gold tips.",
    "Hoi An old house courtyard with hanging lanterns, softly blurred. Low camera angle, 85mm lens. Warm lantern light with raking side light.")
add("la_colossal_sonmai_04", "LA Colossal – Son Mai 04 (Seated)",
    "ONE extremely large SuperBBW Vietnamese woman in her early 20s, sleek high ponytail, natural face with a playful smile.",
    seat("spreading across the bench"), f"{SM} Deep glossy black lacquer with gold-leaf lotus ponds, silver-leaf dragonflies, and crackled white eggshell clouds. {PAT}",
    f"Seated on a low wooden bench, leaning back slightly with both hands planted on the bench behind her, chest open and belly relaxed forward, legs crossed at the knee, torso facing the camera. {ARMS}",
    "Very high 8-inch black lacquer platform stiletto thong sandals with a gold-leaf lotus toe ring and a slim ankle strap.",
    "Extra long almond nails, black with gold-leaf dots.",
    "Vietnamese lacquer workshop with half-finished panels on the walls, softly blurred. Low camera angle, 85mm lens. Warm window light with raking side light.")
add("la_colossal_sonmai_05", "LA Colossal – Son Mai 05 (Seated)",
    "ONE extremely large SuperBBW Chinese woman in her late 40s, black hair in a low polished bun with a gold pin, natural face with a gentle smile.",
    seat("spreading across the stool"), f"{SM} Deep glossy black and red-brown lacquer with gold-leaf chrysanthemums, silver-leaf herons, and crackled white eggshell mountains. {PAT}",
    f"Seated upright on a round lacquer stool, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee, elbows relaxed out to the sides. {ARMS}",
    "Very high 8-inch red-brown lacquer platform Mary Jane stilettos with a gold buckle strap.",
    "Extra long oval nails, red-brown with eggshell-white tips.",
    "Vintage Hanoi parlor with lacquer screens, softly blurred. Low camera angle, 85mm lens. Warm lamp key with raking side light.")
add("la_colossal_sonmai_06", "LA Colossal – Son Mai 06 (Seated)",
    "ONE extremely large SuperBBW Indian woman in her mid-30s, long thick braid over one shoulder with small gold beads, natural face with a warm smile.",
    seat("filling the armchair"), f"{SM} Deep glossy black lacquer with gold-leaf peacocks, silver-leaf palms, and crackled white eggshell moon and clouds. {PAT}",
    f"Seated in a carved armchair, torso turned open toward the camera, one forearm resting on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Very high 8-inch black lacquer platform stiletto sandals with ribbon laces wrapping up the calf and tied in a bow below the knee.",
    "Extra long coffin nails, black with gold tips.",
    "Colonial-era Saigon villa interior with tiled floor and shutters, softly blurred. Low camera angle, 85mm lens. Warm afternoon window light with raking side light.")

# ── Lai Rod Nam ──────────────────────────────────────────
LRN = "no religious figures."
add("la_colossal_lairodnam_01", "LA Colossal – Lai Rod Nam 01 (Standing)",
    "ONE extremely large SuperBBW Thai woman in her late 20s, glossy black hair in a high topknot with a small gold ornament, natural face with a bright smile.",
    STAND, f"{LR} Deep glossy black lacquer with bright gold-leaf kranok flame scrolls, lotus buds, and naga serpents densely covering bust, belly rolls, hips, and legs, {LRN} {PAT}",
    f"Standing in a three-quarter front view, one arm extended gracefully out to the side at shoulder height in a Thai dance gesture, the other hand on her hip, chest open. {ARMS}",
    "Towering 9-inch black lacquer barely-there platform stilettos with two hairline gold straps.",
    "Extra long curved stiletto nails, black with gold tips.",
    "Grand Palace gallery with gilded red walls and mirrored mosaic pillars, softly blurred. Low camera angle, 85mm lens. Warm golden key with raking side light.")
add("la_colossal_lairodnam_02", "LA Colossal – Lai Rod Nam 02 (Standing)",
    "ONE extremely large SuperBBW Korean woman in her late 30s, sleek jaw-length black bob, natural face with a composed smile.",
    STAND, f"{LR} Deep glossy black lacquer with bright gold-leaf stencil mythical birds, flowering vines, and kranok borders, {LRN} {PAT}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Towering 9-inch caged black lacquer platform stiletto sandals with gold kranok straps.",
    "Extra long squoval nails, glossy black.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm gold key with raking side light and soft rim light.")
add("la_colossal_lairodnam_03", "LA Colossal – Lai Rod Nam 03 (Standing)",
    "ONE extremely large SuperBBW Samoan woman in her early 40s, long dark wavy hair with a gold flower pin, natural face with a warm smile.",
    STAND, f"{LR} Deep glossy black lacquer with bright gold-leaf lotus ponds, swans, and kranok flames, {LRN} {PAT}",
    f"Standing in a three-quarter front view, one hand touching her hair at shoulder height, the other resting on her outer hip, torso turned open to the camera. {ARMS}",
    "Towering 9-inch black lacquer platform stiletto d'Orsay pumps with gold-leaf trim.",
    "Extra long almond nails, gold chrome.",
    "Tropical teak pavilion with a lotus pond, softly blurred. Low camera angle, 85mm lens. Soft shaded daylight with warm raking side light.")
add("la_colossal_lairodnam_04", "LA Colossal – Lai Rod Nam 04 (Seated)",
    "ONE extremely large SuperBBW Thai woman in her early 50s, silver-streaked black hair in a low bun with a jasmine garland, natural face with a gentle smile.",
    seat("filling the chair"), f"{LR} Deep glossy black lacquer with bright gold-leaf kranok scrolls and naga serpents coiling around the belly and thighs, {LRN} {PAT}",
    f"Seated in a gilded teak armchair, torso facing the camera, both forearms resting on the armrests, legs crossed at the knee. {ARMS}",
    "Towering 9-inch black lacquer peep-toe platform stilettos with crossed gold ankle straps.",
    "Extra long oval nails, black with gold tips.",
    "Traditional Thai house interior with gilded lacquer cabinets, softly blurred. Low camera angle, 85mm lens. Warm window light with raking side light.")
add("la_colossal_lairodnam_05", "LA Colossal – Lai Rod Nam 05 (Seated)",
    "ONE extremely large SuperBBW Black woman in her early 30s, short natural afro with gold hair rings, natural face with a radiant smile.",
    seat("spreading across the block"), f"{LR} Deep glossy black lacquer with bright gold-leaf kinnari birds, lotus scrolls, and flame borders, {LRN} {PAT}",
    f"Seated on a low black block, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Towering 9-inch black lacquer platform gladiator stiletto sandals laced to mid-calf with gold kranok along each strap.",
    "Extra long coffin nails, black with gold foil.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm gold key with raking side light and soft rim light.")
add("la_colossal_lairodnam_06", "LA Colossal – Lai Rod Nam 06 (Seated)",
    "ONE extremely large SuperBBW Filipino woman in her mid-20s, long black side braid with gold thread, natural face with a sweet smile.",
    seat("spreading across the bench"), f"{LR} Deep glossy black lacquer with bright gold-leaf elephants, lotus, and kranok vines, {LRN} {PAT}",
    f"Seated upright on a gilded bench, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Extreme 10-inch black lacquer platform stilettos with a thick mirrored gold platform and a chrome stiletto heel.",
    "Extra long almond nails, mirror gold.",
    "Riverside Bangkok temple courtyard wall with gold mosaic (no religious images), softly blurred. Low camera angle, 85mm lens. Warm late-afternoon light with raking side light.")

# ── Minakari ─────────────────────────────────────────────
add("la_colossal_minakari_01", "LA Colossal – Minakari 01 (Standing)",
    "ONE extremely large SuperBBW Iranian woman in her late 30s, long dark waves with a thin gold headband, natural face with kohl-lined eyes and a confident smile.",
    STAND, f"{MN} Glossy deep cobalt and turquoise enamel base with fine gold outlines, filled with birds, roses, and arabesque vines in white, red, and green. {PAT}",
    "Standing in a three-quarter front view, both hands clasped loosely behind her lower back, shoulders drawn back, chest and belly facing the camera.",
    "Very high 8-inch cobalt enamel platform stiletto sandals with multiple thin straps across the instep outlined in gold.",
    "Extra long stiletto nails, cobalt with gold tips.",
    "Isfahan palace hall with mirror mosaic and arched niches, softly blurred. Low camera angle, 85mm lens. Warm lantern key with raking side light making the enamel shine.")
add("la_colossal_minakari_02", "LA Colossal – Minakari 02 (Standing)",
    "ONE extremely large SuperBBW Turkish woman in her late 20s, auburn hair in a high messy bun, natural face with a bright smile.",
    STAND, f"{MN} Glossy sky-blue and cobalt enamel base with fine gold outlines, filled with nightingales, pomegranates, and paisley vines in white, crimson, and emerald. {PAT}",
    f"Standing in a three-quarter front view, one arm extended gracefully out to the side at shoulder height, the other hand on her hip, chest open. {ARMS}",
    "Very high 8-inch cobalt enamel platform stiletto sandals with spiral straps coiling up the calf, gold-edged.",
    "Extra long almond nails, turquoise with gold swirl.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm key with raking side light and soft rim light.")
add("la_colossal_minakari_03", "LA Colossal – Minakari 03 (Standing)",
    "ONE extremely large SuperBBW Arab woman in her mid-40s, long straight black hair past the shoulders, natural face with kohl-lined eyes and a regal smile.",
    STAND, f"{MN} Glossy deep cobalt enamel base with fine gold outlines, filled with large rosette medallions, cypress trees, and birds in turquoise, red, and white. {PAT}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Very high 8-inch cobalt enamel pointed platform stiletto ankle booties with gold arabesque detailing.",
    "Extra long coffin nails, deep cobalt.",
    "Empty desert dunes at golden hour, smooth sand curves and a clean sky. Low camera angle, 135mm lens. Warm low sun with strong raking side light across the enamel.")
add("la_colossal_minakari_04", "LA Colossal – Minakari 04 (Seated)",
    "ONE extremely large SuperBBW Iranian woman in her mid-50s, silver-streaked dark hair in a low bun with a small gold comb, natural face with a dignified smile.",
    seat("spreading across the divan"), f"{MN} Glossy turquoise and cobalt enamel base with fine gold outlines, filled with lotus, tulips, and peacocks. {PAT}",
    f"Seated upright on a low tiled divan, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Towering 9-inch cobalt enamel peep-toe platform stilettos with a single gold ankle strap.",
    "Extra long oval nails, cobalt with gold tips.",
    "Shiraz garden pavilion with stained glass casting colored light, softly blurred. Low camera angle, 85mm lens. Warm key with raking side light.")
add("la_colossal_minakari_05", "LA Colossal – Minakari 05 (Seated)",
    "ONE extremely large SuperBBW Uzbek woman in her early 30s, long black hair in many thin braids with a small embroidered cap, natural face with a warm smile.",
    seat("filling the chair"), f"{MN} Glossy cobalt and turquoise enamel base with fine gold outlines, filled with pomegranates, birds, and arabesque vines. {PAT}",
    f"Seated in a carved wooden armchair, torso turned open toward the camera, one forearm on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Towering 9-inch caged cobalt enamel platform stiletto sandals with gold-tipped straps.",
    "Extra long almond nails, turquoise with gold dots.",
    "Bukhara courtyard with blue-tiled walls, softly blurred. Low camera angle, 85mm lens. Warm afternoon light with raking side light.")
add("la_colossal_minakari_06", "LA Colossal – Minakari 06 (Seated)",
    "ONE extremely large SuperBBW Pakistani woman in her late 20s, long dark side-swept waves, natural face with a soft smile.",
    seat("spreading across the bench"), f"{MN} Glossy sky-blue enamel base with fine gold outlines, filled with roses, irises, and hummingbirds in pink, cobalt, and white. {PAT}",
    f"Seated on a low marble bench, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Towering 9-inch sky-blue enamel platform stiletto d'Orsay pumps with gold trim.",
    "Extra long coffin nails, sky blue with gold tips.",
    "Mughal-style garden pavilion with marble arches, softly blurred. Low camera angle, 85mm lens. Soft daylight with warm raking side light.")

# ── Khokhloma ────────────────────────────────────────────
add("la_colossal_khokhloma_01", "LA Colossal – Khokhloma 01 (Standing)",
    "ONE extremely large SuperBBW Russian woman in her late 20s, long honey-blonde side braid, natural face with a sweet smile.",
    STAND, f"{KH} Deep glossy black and gold lacquer with dense hand-painted red rowan berries, golden leaves, and curling grass scrolls. {PAT}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Towering 9-inch black-and-gold lacquer platform gladiator stiletto sandals laced to mid-calf with red berry motifs.",
    "Extra long almond nails, gold with red tips.",
    "Russian imperial hall with gilded mouldings and chandeliers, softly blurred. Low camera angle, 85mm lens. Warm chandelier key with raking side light.")
add("la_colossal_khokhloma_02", "LA Colossal – Khokhloma 02 (Standing)",
    "ONE extremely large SuperBBW Ukrainian woman in her early 40s, long copper-red waves, natural face with a warm smile.",
    STAND, f"{KH} Glossy gold base with bold black and red strawberries, currants, and flowing kudrina leaf swirls. {PAT}",
    f"Standing in a three-quarter front view, one hand lifting her hair at shoulder height, the other on her outer hip, torso turned open toward the camera. {ARMS}",
    "Towering 9-inch gold lacquer peep-toe platform stilettos with crossed red ankle straps.",
    "Extra long coffin nails, red with gold tips.",
    "Russian birch grove in autumn, white trunks and golden leaves. Low camera angle, 135mm lens. Low warm afternoon sun with raking side light.")
add("la_colossal_khokhloma_03", "LA Colossal – Khokhloma 03 (Standing)",
    "ONE extremely large SuperBBW Kazakh woman in her mid-30s, glossy black hair in a sleek high ponytail, natural face with a confident smile.",
    STAND, f"{KH} Deep glossy black and gold lacquer with red rowan berries, golden leaves, and firebird feather scrolls. {PAT}",
    f"Standing in a three-quarter front view, one arm extended gracefully out to the side at shoulder height, the other hand on her hip, chest open. {ARMS}",
    "Very high 8-inch knee-high lace-up black lacquer platform stiletto boots with gold eyelets and painted berries, visible boot edge.",
    "Extra long stiletto nails, black with red berry dots.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm key with raking side light and soft rim light.")
add("la_colossal_khokhloma_04", "LA Colossal – Khokhloma 04 (Seated)",
    "ONE extremely large SuperBBW Russian woman in her early 50s, silver-blonde braided crown, natural face with warm smile lines.",
    seat("spreading across the bench"), f"{KH} Deep glossy black and gold lacquer with dense red rowan berries and golden leaves. {PAT}",
    f"Seated on a carved wooden bench, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Very high 8-inch black-and-gold lacquer platform Mary Jane stilettos with red berry buckles.",
    "Extra long oval nails, gold with red tips.",
    "Rustic Russian izba with a painted tiled stove and wooden utensils, softly blurred. Low camera angle, 85mm lens. Warm firelight key with raking side light.")
add("la_colossal_khokhloma_05", "LA Colossal – Khokhloma 05 (Seated)",
    "ONE extremely large SuperBBW Polish woman in her early 20s, platinum-blonde chin-length bob, natural face with a playful smile.",
    seat("spreading across the stool"), f"{KH} Glossy gold base with bold black and red strawberries, currants, and kudrina swirls. {PAT}",
    f"Seated upright on a painted wooden stool, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Very high 8-inch gold lacquer platform stiletto sandals with red ribbon laces wrapping up the calf and tied in a bow below the knee.",
    "Extra long almond nails, red with gold leaf.",
    "Russian dacha parlor with lace curtains and a samovar, softly blurred. Low camera angle, 85mm lens. Soft window light with raking side light.")
add("la_colossal_khokhloma_06", "LA Colossal – Khokhloma 06 (Seated)",
    "ONE extremely large SuperBBW Black woman in her late 40s, long locs gathered over one shoulder with gold cuffs, natural face with a regal smile.",
    seat("filling the chair"), f"{KH} Deep glossy black and gold lacquer with dense red rowan berries, golden leaves, and curling grass scrolls. {PAT}",
    f"Seated in a gilded palace armchair, torso turned open toward the camera, one forearm on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Towering 9-inch caged black-and-gold lacquer platform stiletto sandals with red berry accents at each junction.",
    "Extra long coffin nails, black with gold and red.",
    "Russian palace salon with gilded panels and a chandelier, softly blurred. Low camera angle, 85mm lens. Warm chandelier key with raking side light.")

RATIO_RE = re.compile(r"\b(?:2:3|3:4|4:5)(?= vertical)")


def main() -> int:
    force = "--force" in sys.argv
    if not PRESETS_DIR.is_dir():
        print(f"[ERROR] presets dir not found: {PRESETS_DIR}")
        return 1
    keys = [k for k, _, _ in P]
    if len(keys) != len(set(keys)):
        print("[ERROR] duplicate keys")
        return 1

    written, skipped = 0, 0
    for key, title, prompt in P:
        path = PRESETS_DIR / f"{key}.json"
        if path.exists() and not force:
            print(f"[SKIP] exists: {path.name}")
            skipped += 1
            continue
        data = {
            "title": title,
            "category": CATEGORY,
            "platform": PLATFORM,
            "aspect_ratio": ASPECT,
            "prompt": RATIO_RE.sub(ASPECT, prompt.strip()),
        }
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        check = json.loads(path.read_text(encoding="utf-8-sig"))
        assert check["prompt"] and check["aspect_ratio"] == ASPECT
        print(f"[OK]   {path.name}")
        written += 1

    print(f"\nDone. written={written} skipped={skipped} total={len(P)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
