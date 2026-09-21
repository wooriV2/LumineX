# -*- coding: utf-8 -*-
r"""
patch_livingartifact_colossal_korea_1_json.py
Living Artifact · Colossal — 24 solo presets
(Korean 4 materials: Celadon Sanggam, Vermilion Najeon, Black Najeon, Gamji-geumni x 3 standing + 3 seated)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_colossal_korea_1_json.py
    python preset_builders\patch_livingartifact_colossal_korea_1_json.py --force   (overwrite)
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


CEL = ("Full body Goryeo celadon body painting from neck to ankle, painted directly on bare skin, one continuous surface. "
       "High-gloss jade-green celadon glaze clearly covering all skin, fine crackle and soft uneven reflections,")
NJ = "Full body najeon-chilgi body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex."
GJ = ("Full body gamji-geumni body painting in the style of Goryeo illuminated sutra covers, from neck to ankle, painted "
      "directly on bare skin, one continuous surface. Glossy deep navy-indigo base, not purple, with bold dense shimmering gold ink line work —")
PAT = "Pelvis, inner thighs, and both arms fully patterned."
KR = "Authentic Korean Goryeo style."

P = []


def add(key, title, *args):
    P.append((key, title, build(*args)))


# ── Celadon Sanggam ──────────────────────────────────────
add("la_colossal_celadon_01", "LA Colossal – Celadon Sanggam 01 (Standing)",
    "ONE extremely large SuperBBW Korean woman in her early 30s, long black hair in a low braid with a jade binyeo, natural face with a serene smile.",
    STAND, f"{CEL} black-and-white sanggam cranes and clouds in round medallions across bust, belly rolls, hips, and legs. {PAT} {KR}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Very high 8-inch celadon-glazed platform stiletto sandals with ribbon laces wrapping up the calf and tied in a bow below the knee.",
    "Extra long almond nails, celadon with white tips.",
    "Korean ceramics gallery with celadon maebyeong vases, softly blurred. Low camera angle, 85mm lens. Cool museum light with warm raking side light across the glaze.")
add("la_colossal_celadon_02", "LA Colossal – Celadon Sanggam 02 (Standing)",
    "ONE extremely large SuperBBW Japanese woman in her early 40s, glossy black blunt bob with bangs, natural face with a calm smile.",
    STAND, f"{CEL} black-and-white sanggam willow trees, reeds, and waterfowl. {PAT} {KR}",
    f"Standing in a three-quarter front view, one arm extended gracefully out to the side at shoulder height, the other hand on her hip, chest open. {ARMS}",
    "Towering 9-inch caged celadon-glazed platform stiletto sandals, a lattice of fine crackle-finish straps.",
    "Extra long squoval nails, pale celadon.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Cool key with warm raking side light and soft rim light.")
add("la_colossal_celadon_03", "LA Colossal – Celadon Sanggam 03 (Standing)",
    "ONE extremely large SuperBBW Brazilian woman in her late 20s, long dark voluminous curls, natural face with a bright smile.",
    STAND, f"{CEL} black-and-white sanggam peony scrolls and chrysanthemum sprays. {PAT} {KR}",
    "Standing in a three-quarter front view, both hands clasped loosely behind her lower back, shoulders drawn back, chest and belly facing the camera.",
    "Towering 9-inch celadon-glazed peep-toe platform stilettos with crossed ankle straps.",
    "Extra long coffin nails, celadon with black sanggam dots.",
    "Misty Damyang bamboo forest, softly blurred. Low camera angle, 135mm lens. Soft overcast light with gentle raking side light, no harsh highlights.")
add("la_colossal_celadon_04", "LA Colossal – Celadon Sanggam 04 (Seated)",
    "ONE extremely large SuperBBW Korean woman in her mid-20s, sleek high ponytail with a jade clasp, natural face with a playful smile.",
    seat("spreading across the maru"), f"{CEL} black-and-white sanggam cranes, clouds, and ripples. {PAT} {KR}",
    f"Seated on the edge of a wooden maru, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Very high 8-inch celadon-glazed platform stiletto thong sandals with a white crane toe ring and a slim ankle strap.",
    "Extra long almond nails, celadon with white crane tips.",
    "Hanok room with paper lattice doors and a white moon jar, softly blurred. Low camera angle, 85mm lens. Soft window light with warm raking side light.")
add("la_colossal_celadon_05", "LA Colossal – Celadon Sanggam 05 (Seated)",
    "ONE extremely large SuperBBW Mongolian woman in her late 40s, black hair in two long braids, natural face with a gentle smile.",
    seat("spreading across the bench"), f"{CEL} black-and-white sanggam lotus ponds and mandarin ducks. {PAT} {KR}",
    f"Seated upright on a low wooden bench, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Very high 8-inch celadon-glazed platform Mary Jane stilettos with white chrysanthemum buckles.",
    "Extra long oval nails, celadon with white tips.",
    "Korean temple courtyard wall with pine trees (no religious images), softly blurred. Low camera angle, 85mm lens. Soft daylight with warm raking side light.")
add("la_colossal_celadon_06", "LA Colossal – Celadon Sanggam 06 (Seated)",
    "ONE extremely large SuperBBW British woman in her late 30s, long ivory-blonde waves, natural face with a warm smile.",
    seat("filling the armchair"), f"{CEL} black-and-white sanggam cranes and cloud medallions. {PAT} {KR}",
    f"Seated in a museum-style upholstered armchair, torso turned open toward the camera, one forearm on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Towering 9-inch celadon-glazed platform stiletto d'Orsay pumps with white trim.",
    "Extra long coffin nails, soft jade green.",
    "Western museum gallery displaying Korean celadon in glass cases, softly blurred. Low camera angle, 85mm lens. Cool museum light with warm raking side light.")

# ── Vermilion Najeon ─────────────────────────────────────
VJ = f"{NJ} Deep glossy vermilion lacquer clearly different from skin,"
add("la_colossal_najeon_vermilion_01", "LA Colossal – Vermilion Najeon 01 (Standing)",
    "ONE extremely large SuperBBW Korean woman in her early 40s, black hair in a sleek high bun with a coral binyeo, natural face with a bright smile.",
    STAND, f"{VJ} subtle brush texture beneath the shine, inlaid with thick cut mother-of-pearl in pink, green, and blue rainbow sheen — peonies, scrolling vines, and butterflies. {PAT} Authentic Korean Joseon style.",
    f"Standing in a three-quarter front view, one hand lightly touching her binyeo at shoulder height, the other on her outer hip, torso turned open to the camera. {ARMS}",
    "Towering 9-inch vermilion lacquer peep-toe platform stilettos with crossed ankle straps and mother-of-pearl heels.",
    "Extra long coffin nails, vermilion with pearl tips.",
    "Gyeongbokgung courtyard at golden hour, softly blurred. Low camera angle, 85mm lens. Warm sunlight with raking side light so the mother-of-pearl flashes rainbow.")
add("la_colossal_najeon_vermilion_02", "LA Colossal – Vermilion Najeon 02 (Standing)",
    "ONE extremely large SuperBBW Black woman in her early 30s, long locs gathered high with a coral clasp, natural face with a radiant smile.",
    STAND, f"{VJ} inlaid with iridescent mother-of-pearl phoenixes, bamboo, and cloud bands. {PAT}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Very high 8-inch vermilion lacquer platform stiletto sandals with spiral straps coiling up the calf, pearl-tipped.",
    "Extra long stiletto nails, vermilion with iridescent pearl.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm key with strong raking side light and soft rim light.")
add("la_colossal_najeon_vermilion_03", "LA Colossal – Vermilion Najeon 03 (Standing)",
    "ONE extremely large SuperBBW Spanish woman in her late 40s, black hair in a low chignon with a carved comb, natural face with a confident smile.",
    STAND, f"{VJ} inlaid with iridescent mother-of-pearl ten longevity symbols — sun, clouds, cranes, pine, deer, turtles, and waves. {PAT}",
    f"Standing in a three-quarter front view, one arm extended gracefully out to the side at shoulder height, the other hand on her hip, chest open. {ARMS}",
    "Very high 8-inch vermilion lacquer platform stiletto sandals with multiple thin straps across the instep and pearl studs.",
    "Extra long almond nails, deep red.",
    "Grand museum hall of Asian lacquerware with red walls, softly blurred. Low camera angle, 85mm lens. Warm museum key with raking side light.")
add("la_colossal_najeon_vermilion_04", "LA Colossal – Vermilion Najeon 04 (Seated)",
    "ONE extremely large SuperBBW Korean woman in her early 50s, black hair in a tall eonjeun-meori updo with mother-of-pearl tteoljam, natural face with a confident smile.",
    seat("filling the throne seat"), f"{VJ} inlaid with iridescent mother-of-pearl phoenixes and peonies. {PAT} Authentic Korean Joseon style.",
    f"Seated on a carved wooden throne, torso facing the camera, both forearms resting on the armrests, legs crossed at the knee. {ARMS}",
    "Very high 8-inch vermilion lacquer platform Mary Jane stilettos with pearl buckles.",
    "Extra long stiletto nails, vermilion with pearl tips.",
    "Joseon throne hall with dancheong beams and an Irworobongdo screen, softly blurred. Low camera angle, 85mm lens. Warm golden key with raking side light.")
add("la_colossal_najeon_vermilion_05", "LA Colossal – Vermilion Najeon 05 (Seated)",
    "ONE extremely large SuperBBW Chinese woman in her late 20s, long straight black hair falling over both shoulders, natural face with a soft smile.",
    seat("spreading across the bench"), f"{VJ} inlaid with iridescent mother-of-pearl grapevines and squirrels. {PAT}",
    f"Seated on a low lacquered bench, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Towering 9-inch caged vermilion lacquer platform stiletto sandals with pearl accents at each junction.",
    "Extra long almond nails, pearl white.",
    "Traditional Korean lacquer craftsman's workshop with finished boxes on shelves, softly blurred. Low camera angle, 85mm lens. Warm window light with raking side light.")
add("la_colossal_najeon_vermilion_06", "LA Colossal – Vermilion Najeon 06 (Seated)",
    "ONE extremely large SuperBBW Indian woman in her late 30s, long thick braid with a coral ornament, natural face with a warm smile.",
    seat("spreading across the stool"), f"{VJ} inlaid with iridescent mother-of-pearl lotus and mandarin ducks. {PAT}",
    f"Seated upright on a round lacquer stool, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Towering 9-inch vermilion lacquer platform gladiator stiletto sandals laced to mid-calf with pearl eyelets.",
    "Extra long coffin nails, coral red.",
    "Palace corridor with red columns and hanging silk lanterns, softly blurred. Low camera angle, 85mm lens. Warm lantern light with raking side light.")

# ── Black Najeon ─────────────────────────────────────────
BJ = f"{NJ} Deep glossy black lacquer"
add("la_colossal_najeon_black_01", "LA Colossal – Black Najeon 01 (Standing)",
    "ONE extremely large SuperBBW Korean woman in her early 50s, silver-white hair in a sleek low bun with a mother-of-pearl binyeo, natural face with a serene smile.",
    STAND, f"{BJ} with subtle brush texture, not a bodysuit, inlaid with thick cut mother-of-pearl in pink, green, and blue rainbow sheen — full moon on the belly, cranes on the bust, pine on the hips, clouds and waves on the legs. {PAT}",
    "Standing in a three-quarter front view, both hands clasped loosely behind her lower back, shoulders drawn back, chest and belly facing the camera.",
    "Towering 9-inch caged black lacquer platform stiletto sandals with mother-of-pearl accents at each junction.",
    "Extra long almond nails, black with pearl tips.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm key with strong raking side light so the mother-of-pearl flashes rainbow.")
add("la_colossal_najeon_black_02", "LA Colossal – Black Najeon 02 (Standing)",
    "ONE extremely large SuperBBW Vietnamese woman in her late 20s, straight black hair falling past the waist, natural face with a sweet smile.",
    STAND, f"{BJ} inlaid with iridescent mother-of-pearl plum blossoms, bamboo, and small birds. {PAT}",
    f"Standing in a three-quarter front view, one hand sweeping her hair back at shoulder height, the other on her outer hip, torso turned open to the camera. {ARMS}",
    "Extreme 10-inch black lacquer barely-there platform stilettos with two hairline straps and pearl heel caps.",
    "Extra long coffin nails, iridescent pearl.",
    "Korean lotus pond pavilion at blue hour with warm lanterns, softly blurred. Low camera angle, 85mm lens. Warm lantern key with cool ambient and raking side light.")
add("la_colossal_najeon_black_03", "LA Colossal – Black Najeon 03 (Standing)",
    "ONE extremely large SuperBBW Italian woman in her late 30s, voluminous black waves, natural face with a confident smile.",
    STAND, f"{BJ} inlaid with iridescent mother-of-pearl chrysanthemum scrolls and arabesque vines. {PAT}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Very high 8-inch knee-high lace-up black lacquer platform stiletto boots with pearl eyelets, visible boot edge.",
    "Extra long stiletto nails, glossy black.",
    "Dark wood-paneled gallery with spotlit lacquer boxes, softly blurred. Low camera angle, 85mm lens. Warm spotlight with raking side light.")
add("la_colossal_najeon_black_04", "LA Colossal – Black Najeon 04 (Seated)",
    "ONE extremely large SuperBBW Korean woman in her early 30s, high ponytail with a pearl band, natural face with a quiet smile.",
    seat("spreading across the ledge"), f"{BJ} inlaid with iridescent mother-of-pearl lotus flowers, mandarin ducks, and Korean ripple patterns. {PAT}",
    f"Seated upright on a wooden pavilion ledge, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Towering 9-inch black lacquer peep-toe platform stilettos with a single pearl ankle strap.",
    "Extra long oval nails, black with pearl tips.",
    "Korean lotus pond pavilion at dusk, softly blurred. Low camera angle, 85mm lens. Warm lantern key with raking side light.")
add("la_colossal_najeon_black_05", "LA Colossal – Black Najeon 05 (Seated)",
    "ONE extremely large SuperBBW Black woman in her mid-40s, short platinum pixie cut, natural face with a bold smile.",
    seat("filling the armchair"), f"{BJ} inlaid with iridescent mother-of-pearl tigers, pine trees, and magpies. {PAT}",
    f"Seated in a carved wooden armchair, torso turned open toward the camera, one forearm on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Towering 9-inch black lacquer platform stiletto d'Orsay pumps with pearl inlay.",
    "Extra long coffin nails, black with pearl flakes.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm key with strong raking side light and soft rim light.")
add("la_colossal_najeon_black_06", "LA Colossal – Black Najeon 06 (Seated)",
    "ONE extremely large SuperBBW Taiwanese woman in her early 20s, black hair in two high buns, natural face with a playful smile.",
    seat("spreading across the bench"), f"{BJ} inlaid with iridescent mother-of-pearl butterflies, peonies, and scattered stars. {PAT}",
    f"Seated on a low black bench, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Very high 8-inch black lacquer platform stiletto thong sandals with a pearl toe ring and a slim ankle strap.",
    "Extra long almond nails, pastel pearl.",
    "Night garden with paper lanterns and a stone path, softly blurred. Low camera angle, 85mm lens. Warm lantern light with raking side light.")

# ── Gamji-geumni ─────────────────────────────────────────
NOREL = "No plain indigo areas, no religious figures."
add("la_colossal_gamji_01", "LA Colossal – Gamji-geumni 01 (Standing)",
    "ONE extremely large SuperBBW Korean woman in her late 40s, black hair in a low jjok-meori bun with a gold binyeo, natural face with a confident smile.",
    STAND, f"{GJ} bosang-hwa lotus medallion on the belly, lotus-vine scrolls across the bust, cloud bands on the arms, stacked lotus-petal borders on the legs. {NOREL} {PAT} {KR}",
    f"Standing in a three-quarter front view, one arm extended gracefully out to the side at shoulder height, the other hand on her hip, chest open. {ARMS}",
    "Very high 8-inch indigo lacquer platform T-strap stiletto sandals with fine gold line straps.",
    "Extra long almond nails, indigo with gold tips.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm narrow spotlight with raking side light making the gold lines shimmer.")
add("la_colossal_gamji_02", "LA Colossal – Gamji-geumni 02 (Standing)",
    "ONE extremely large SuperBBW Japanese woman in her early 30s, glossy black hair in a sleek chignon, natural face with a calm smile.",
    STAND, f"{GJ} peony and arabesque vines across bust and belly, cloud-and-crane bands on the arms, lotus-petal and diamond borders on the legs. {NOREL} {PAT}",
    "Standing in a three-quarter front view, both hands clasped loosely behind her lower back, shoulders drawn back, chest and belly facing the camera.",
    "Towering 9-inch indigo lacquer peep-toe platform stilettos with crossed gold ankle straps.",
    "Extra long squoval nails, indigo with fine gold line.",
    "Joseon royal library with indigo-and-gold manuscripts and paper windows, softly blurred. Low camera angle, 85mm lens. Warm lamp key with raking side light.")
add("la_colossal_gamji_03", "LA Colossal – Gamji-geumni 03 (Standing)",
    "ONE extremely large SuperBBW French woman in her late 20s, long strawberry-blonde waves, natural face with a bright smile.",
    STAND, f"{GJ} lotus medallions, scrolling vines, and cloud bands. {NOREL} {PAT}",
    f"Standing in a three-quarter front view, one hand lifting her hair at shoulder height, the other on her outer hip, torso turned open to the camera. {ARMS}",
    "Towering 9-inch caged indigo lacquer platform stiletto sandals with gold-tipped straps.",
    "Extra long coffin nails, gold chrome.",
    "Paris museum gallery of Asian manuscripts with dim display cases, softly blurred. Low camera angle, 85mm lens. Warm spotlight with raking side light.")
add("la_colossal_gamji_04", "LA Colossal – Gamji-geumni 04 (Seated)",
    "ONE extremely large SuperBBW Korean woman in her late 20s, long black hair in a single low braid with a gold-embroidered daenggi ribbon, natural face with a gentle smile.",
    seat("spreading across the bench"), f"{GJ} peony vines, lotus medallions, and cloud bands, fine silver accent lines. {NOREL} {PAT}",
    f"Seated on a low wooden bench, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Very high 8-inch indigo velvet platform Mary Jane stilettos with gold buckles.",
    "Extra long stiletto nails, indigo with gold tips.",
    "Joseon royal library with folded manuscripts and paper lattice windows, softly blurred. Low camera angle, 85mm lens. Warm lamp key with raking side light.")
add("la_colossal_gamji_05", "LA Colossal – Gamji-geumni 05 (Seated)",
    "ONE extremely large SuperBBW Thai woman in her early 40s, black hair in a low bun with a small gold pin, natural face with a warm smile.",
    seat("spreading across the stool"), f"{GJ} chrysanthemums, phoenix tail scrolls, and cloud bands. {NOREL} {PAT}",
    f"Seated upright on a round indigo stool, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Very high 8-inch indigo lacquer platform stiletto sandals with gold spiral straps coiling up the calf.",
    "Extra long almond nails, midnight blue with gold leaf.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm narrow spotlight with raking side light and soft rim light.")
add("la_colossal_gamji_06", "LA Colossal – Gamji-geumni 06 (Seated)",
    "ONE extremely large SuperBBW Black British woman in her late 30s, natural hair in a high sculpted bun with a gold pin, natural face with a confident smile.",
    seat("filling the armchair"), f"{GJ} lotus medallions, vine scrolls, and stacked lotus-petal borders. {NOREL} {PAT}",
    f"Seated in a carved rosewood armchair, torso turned open toward the camera, one forearm on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Very high 8-inch indigo lacquer pointed platform stiletto ankle booties with gold line detailing.",
    "Extra long coffin nails, indigo with gold stripe.",
    "Scholar's study with bookcases of indigo-bound volumes and a brass lamp, softly blurred. Low camera angle, 85mm lens. Warm lamp light with raking side light.")

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
