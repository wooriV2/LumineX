# -*- coding: utf-8 -*-
r"""
patch_livingartifact_craft_solo_a_json.py
Living Artifact · Craft Solo (A) — 12 presets
Korea/Japan 6 S-tier materials x standing/seated
(Celadon Sanggam, Vermilion Najeon, Black Najeon, Gamji-geumni, Kintsugi, Maki-e)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_craft_solo_a_json.py
    python preset_builders\patch_livingartifact_craft_solo_a_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · Craft Solo"
PLATFORM = "gemini"
ASPECT = "2:3"

STAND = ("Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly in "
         "deep overlapping rolls, overwhelmingly massive heavy bust, extremely wide hips, enormous thick thighs, very "
         "broad soft arms, not pregnant, profound physical volume filling the frame.")


def seat(spread):
    return ("Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly "
            "resting in deep rolls over the thighs, overwhelmingly massive heavy bust, extremely wide hips "
            f"{spread}, enormous thick thighs, very broad soft arms, profound physical volume filling the frame.")


def build(subject, physique, art, pose, foot, bg, light, lens="85mm lens"):
    return "\n\n".join([
        f"Subject: {subject}",
        physique,
        f"Body Art: {art}",
        f"Pose: {pose} Full body head to toe visible.",
        f"Footwear: {foot}",
        f"Background & Lighting: {bg} ONE woman only. Figure fills 90% of the frame, low camera angle, {lens}. "
        f"{light} Emphasis on the extremely large SuperBBW body volume. 2:3 vertical 8K portrait.",
    ])


P = []


def add(key, title, *args, **kw):
    P.append((key, title, build(*args, **kw)))


# 1. Celadon Sanggam
add("la_craft_solo_celadon_stand", "LA Craft Solo – Celadon Sanggam (Standing)",
    "ONE extremely large SuperBBW Korean woman in her late 30s, long black hair in a sleek low ponytail with a jade binyeo, natural face with a calm smile.",
    STAND,
    "Full body Goryeo celadon body painting from neck to ankle, painted directly on bare skin, one continuous surface. High-gloss jade-green celadon glaze with fine crackle and soft uneven reflections, black-and-white sanggam cranes and clouds in round medallions. Pelvis, inner thighs, and both arms fully patterned, no bare skin gaps. Authentic Korean Goryeo style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly over the back leg, one hand on her wide hip, the other at her collarbone.",
    "8-inch celadon platform stiletto pumps with white crane details. Nails: extra long almond nails, celadon with white tips.",
    "Dim Korean ceramics gallery with celadon maebyeong vases, softly blurred.",
    "Cool museum light with warm raking side light.")
add("la_craft_solo_celadon_seat", "LA Craft Solo – Celadon Sanggam (Seated)",
    "ONE extremely large SuperBBW Korean woman in her late 60s, silver-white hair in a soft side-swept bob, natural face with gentle smile lines.",
    seat("spreading across the maru"),
    "Full body Goryeo celadon body painting from neck to ankle, painted directly on bare skin, one continuous surface. High-gloss jade-green celadon glaze with fine crackle, black-and-white sanggam chrysanthemum sprays and peony scrolls. Pelvis, inner thighs, and both arms fully patterned, no bare skin gaps. Authentic Korean style.",
    "Seated on the edge of a wooden maru with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, far hand planted behind her, near hand on her knee.",
    "7-inch celadon platform Mary Jane stilettos with white chrysanthemum buckles. Nails: extra long oval nails, celadon with white tips.",
    "Hanok room with paper lattice doors and a white moon jar, softly blurred.",
    "Soft window light with raking side light across the glaze.")

# 2. Vermilion Najeon
add("la_craft_solo_najeon_vermilion_stand", "LA Craft Solo – Vermilion Najeon (Standing)",
    "ONE extremely large SuperBBW Korean woman in her late 40s, black hair in a sleek high bun with a coral binyeo, natural face with a bright smile.",
    STAND,
    "Full body najeon-chilgi body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy vermilion lacquer with natural highlights and subtle brush texture, inlaid with thick cut mother-of-pearl in pink-green-blue rainbow sheen — peonies, scrolling vines, and butterflies. Pelvis, inner thighs, and both arms fully patterned. Authentic Korean Joseon style.",
    "Standing with hips turned slightly to the right and chest angled toward the camera, front leg crossed slightly in front, one hand on her waist, the other lightly touching her binyeo.",
    "9-inch vermilion lacquer platform ankle-strap stilettos with mother-of-pearl heels. Nails: extra long coffin nails, vermilion with pearl tips.",
    "Gyeongbokgung courtyard at golden hour, softly blurred.",
    "Warm sunlight with raking side light.")
add("la_craft_solo_najeon_vermilion_seat", "LA Craft Solo – Vermilion Najeon (Seated)",
    "ONE extremely large SuperBBW Korean woman in her mid-50s, black hair in a tall eonjeun-meori updo with mother-of-pearl tteoljam, natural face with a regal gaze.",
    seat("filling the throne seat"),
    "Full body najeon-chilgi body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy vermilion lacquer with natural highlights, inlaid with iridescent mother-of-pearl ten longevity symbols — sun, clouds, cranes, pine, deer, turtles, waves. Pelvis, inner thighs, and both arms fully patterned. Authentic Korean Joseon style.",
    "Seated on a carved wooden throne with body turned 30 degrees to the left, legs crossed at the knee, forearms on the armrests, torso upright and open.",
    "8-inch vermilion lacquer platform Mary Jane stilettos with pearl buckles. Nails: extra long stiletto nails, vermilion with pearl tips.",
    "Joseon throne hall with dancheong beams and an Irworobongdo screen, softly blurred.",
    "Warm golden key with raking side light.")

# 3. Black Najeon
add("la_craft_solo_najeon_black_stand", "LA Craft Solo – Black Najeon (Standing)",
    "ONE extremely large SuperBBW Korean woman in her early 60s, silver-white hair in a sleek low bun with a mother-of-pearl binyeo, natural face with a serene smile.",
    STAND,
    "Full body najeon-chilgi body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex, not a bodysuit. Deep glossy black lacquer with natural highlights and subtle brush texture, inlaid with iridescent pink-green-blue mother-of-pearl — full moon on the belly, cranes on the bust, pine on the hips, clouds and waves on the legs. Pelvis, inner thighs, and both arms fully patterned. Authentic Korean style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly over the back leg, one hand on her wide hip, the other at her collarbone.",
    "8-inch black lacquer platform stiletto pumps with pearl crane inlay. Nails: extra long almond nails, black with pearl tips.",
    "MANDATORY seamless matte black studio background.",
    "Warm key with strong raking side light so the mother-of-pearl flashes rainbow.")
add("la_craft_solo_najeon_black_seat", "LA Craft Solo – Black Najeon (Seated)",
    "ONE extremely large SuperBBW Korean woman in her early 30s, long black hair in a high ponytail with a pearl band, natural face with a quiet smile.",
    seat("spreading across the ledge"),
    "Full body najeon-chilgi body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer with natural highlights, inlaid with iridescent mother-of-pearl lotus flowers, mandarin ducks, reeds, and Korean ripple patterns. Pelvis, inner thighs, and both arms fully patterned. Authentic Korean style.",
    "Seated on a wooden pavilion ledge with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, leaning back on the far hand.",
    "8-inch black lacquer platform Mary Jane stilettos with pearl lotus buckles. Nails: extra long stiletto nails, black with pearl tips.",
    "Korean lotus pond pavilion at blue hour with warm lanterns reflected in the water, softly blurred.",
    "Warm lantern key with cool ambient and raking side light.")

# 4. Gamji-geumni
add("la_craft_solo_gamji_stand", "LA Craft Solo – Gamji-geumni (Standing)",
    "ONE extremely large SuperBBW Korean woman in her late 50s, silver-white hair in a low jjok-meori bun with a gold binyeo, natural face with a serene smile.",
    STAND,
    "Full body gamji-geumni body painting in the style of Goryeo illuminated sutra covers, from neck to ankle, painted directly on bare skin, one continuous surface. Glossy deep navy-indigo gamji paper color, not purple, not violet, with bold dense shimmering gold ink line work — bosang-hwa lotus medallion on the belly, lotus-vine scrolls across the bust, cloud bands on the arms, stacked lotus-petal borders on the legs. Hips and upper thighs densely filled with gold scrollwork, no plain indigo areas. No religious figures. Authentic Korean Goryeo style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly in front, one hand on her wide hip, the other at her collarbone.",
    "8-inch indigo lacquer platform stilettos with fine gold line details. Nails: extra long almond nails, indigo with gold tips.",
    "MANDATORY seamless matte black studio background.",
    "Warm narrow spotlight with raking side light making the gold lines shimmer.")
add("la_craft_solo_gamji_seat", "LA Craft Solo – Gamji-geumni (Seated)",
    "ONE extremely large SuperBBW Korean woman in her late 20s, long straight black hair in a single low braid with a gold-embroidered daenggi ribbon, natural face with a gentle smile.",
    seat("spreading across the bench"),
    "Full body gamji-geumni body painting from neck to ankle, painted directly on bare skin, one continuous surface. Glossy deep navy-indigo base, not purple, with bold dense gold ink peony and arabesque vines across bust and belly, cloud-and-crane bands on the arms, and lotus-petal and diamond borders stacked on the legs, with fine silver accent lines. No religious figures. Pelvis, inner thighs, and both arms fully patterned, no plain indigo areas. Authentic Korean Goryeo style.",
    "Seated on a low wooden bench with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, far hand on the bench behind her, near hand on her knee.",
    "7-inch indigo velvet platform Mary Jane stilettos with gold buckles. Nails: extra long stiletto nails, indigo with gold tips.",
    "Joseon royal library with shelves of folded indigo-and-gold manuscripts and paper lattice windows, softly blurred.",
    "Warm lamp key with raking side light.")

# 5. Kintsugi
add("la_craft_solo_kintsugi_stand", "LA Craft Solo – Kintsugi (Standing)",
    "ONE extremely large SuperBBW Japanese woman in her early 50s, glossy black blunt bob with razor-cut bangs, natural face with a confident smile.",
    STAND,
    "Full body Kintsugi body painting from neck to ankle, painted directly on bare skin, one continuous surface. High-gloss obsidian-black ceramic glaze with a dense network of raised 24-karat gold crack lines catching the light. Pelvis, inner thighs, and both arms fully glazed and cracked, no bare skin gaps.",
    "Standing with hips turned slightly to the right and chest angled toward the camera, front leg crossed slightly in front, one hand on her waist, the other at her collarbone.",
    "9-inch gold mirror-chrome platform stiletto pumps. Nails: extra long stiletto nails, black with gold tips.",
    "MANDATORY seamless matte black studio background.",
    "Warm gold key with raking side light making the gold seams glow.")
add("la_craft_solo_kintsugi_seat", "LA Craft Solo – Kintsugi (Seated)",
    "ONE extremely large SuperBBW Japanese woman in her early 70s, short silver-white hair neatly set, natural face with warm smile lines.",
    seat("spreading across the bench"),
    "Full body Kintsugi body painting from neck to ankle, painted directly on bare skin, one continuous surface. High-gloss milky ivory porcelain glaze with a dense network of raised gold and silver repair lines catching the light. Pelvis, inner thighs, and both arms fully glazed and cracked, no bare skin gaps.",
    "Seated on a low wooden engawa bench with hips angled slightly to the left, torso turned back toward the camera, legs crossed at the knee, far hand behind her, near hand on her knee.",
    "7-inch ivory glazed platform pumps with gold heels. Nails: extra long almond nails, ivory with gold tips.",
    "Traditional Kyoto tea house with shoji screens and a moss garden, softly blurred.",
    "Soft window light with warm raking side light.")

# 6. Maki-e
add("la_craft_solo_makie_stand", "LA Craft Solo – Maki-e (Standing)",
    "ONE extremely large SuperBBW Japanese woman in her early 40s, glossy black hair in a high chignon with gold kanzashi, natural face with a calm smile.",
    STAND,
    "Full body maki-e lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black urushi with natural highlights and subtle brush texture, fine sprinkled gold dust with individual particles visible — a full moon on the belly, autumn grasses up the legs, flying geese across the bust, crisp raised gold relief. Pelvis, inner thighs, and both arms fully patterned.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly in front, one hand holding a folding fan at her shoulder, the other on her hip.",
    "8-inch black lacquer platform stilettos with gold maki-e details. Nails: extra long almond nails, black with gold powder tips.",
    "Kyoto temple veranda at dusk with lanterns, softly blurred.",
    "Warm lantern key with raking side light making the gold glitter.")
add("la_craft_solo_makie_seat", "LA Craft Solo – Maki-e (Seated)",
    "ONE extremely large SuperBBW Japanese woman in her mid-60s, silver-grey hair in a low sculpted bun with a lacquer comb, natural face with a knowing smile.",
    seat("spreading across the bench"),
    "Full body maki-e lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black urushi with fine sprinkled gold dust forming sweeping waves, plovers, and chrysanthemums across bust, belly rolls, hips, and legs, crisp raised gold relief. Pelvis, inner thighs, and both arms fully patterned.",
    "Seated on a low black lacquer bench with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, far hand behind her, near hand on her knee.",
    "8-inch black lacquer platform ankle-strap stilettos with gold wave heels. Nails: extra long coffin nails, black with gold wave tips.",
    "Traditional tatami room with shoji screens and a lacquered chest, softly blurred.",
    "Soft window light with raking side light making the gold dust sparkle.")

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
