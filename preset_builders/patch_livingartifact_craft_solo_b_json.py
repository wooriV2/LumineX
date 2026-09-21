# -*- coding: utf-8 -*-
r"""
patch_livingartifact_craft_solo_b_json.py
Living Artifact · Craft Solo (B) — 16 presets
China/Russia/SE Asia/Iran 8 S-tier materials x standing/seated
(Cloisonné, Ru-Guan, Palekh, Zhostovo, Khokhloma, Son Mai, Lai Rod Nam, Minakari)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_craft_solo_b_json.py
    python preset_builders\patch_livingartifact_craft_solo_b_json.py --force   (overwrite)
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


def build(subject, physique, art, pose, foot, bg, light):
    return "\n\n".join([
        f"Subject: {subject}",
        physique,
        f"Body Art: {art}",
        f"Pose: {pose} Full body head to toe visible.",
        f"Footwear: {foot}",
        f"Background & Lighting: {bg} ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. "
        f"{light} Emphasis on the extremely large SuperBBW body volume. 2:3 vertical 8K portrait.",
    ])


P = []


def add(key, title, *args):
    P.append((key, title, build(*args)))


# 7. Cloisonné
add("la_craft_solo_cloisonne_stand", "LA Craft Solo – Cloisonné (Standing)",
    "ONE extremely large SuperBBW Chinese woman in her early 50s, black hair in a high sleek bun with a gold hairpin, natural face with a composed smile.",
    STAND,
    "Full body cloisonné enamel body painting in Ming jingtailan style, from neck to ankle, painted directly on bare skin, one continuous surface, no collar or neckline band. Glossy turquoise-blue enamel base divided by raised gold wire outlines, filled with lotus scrolls, peonies, and cloud bands in coral red, cobalt, and white. Pelvis, inner thighs, and both arms fully patterned. Authentic Chinese style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly in front, one hand on her wide hip, the other at her collarbone.",
    "8-inch turquoise enamel platform stilettos with gold wire details. Nails: extra long stiletto nails, turquoise with gold tips.",
    "Forbidden City palace hall with red columns and golden beams, softly blurred.",
    "Warm key with raking side light making the gold wires glow.")
add("la_craft_solo_cloisonne_seat", "LA Craft Solo – Cloisonné (Seated)",
    "ONE extremely large SuperBBW Chinese woman in her late 30s, long straight black hair in a low ponytail with a jade clasp, natural face with a gentle smile.",
    seat("spreading across the chair"),
    "Full body cloisonné enamel body painting in Ming jingtailan style, from neck to ankle, painted directly on bare skin, one continuous surface, no collar band. Glossy turquoise enamel with raised gold wire cells filled with lotus, chrysanthemum, and scrolling vines in coral, cobalt, green, and white. Pelvis, inner thighs, and both arms fully patterned. Authentic Chinese style.",
    "Seated in a Ming-style rosewood armchair with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, far forearm on the armrest, near hand on her knee.",
    "8-inch turquoise enamel platform Mary Jane stilettos with gold wire details. Nails: extra long almond nails, turquoise with gold tips.",
    "Ming scholar's study with rosewood furniture, scroll paintings, and lattice windows, softly blurred.",
    "Warm window light with raking side light.")

# 8. Ru-Guan
add("la_craft_solo_ru_guan_stand", "LA Craft Solo – Ru-Guan (Standing)",
    "ONE extremely large SuperBBW Chinese woman in her late 60s, silver-white hair in a neat low bun with a pale jade pin, natural face with a serene smile.",
    STAND,
    "Full body Song dynasty Ru-Guan celadon body painting from neck to ankle, painted directly on bare skin, one continuous surface. High-gloss soft sky-blue-grey glaze with a fine dense crackle network of thin dark lines and finer golden secondary crackle, not kintsugi, not large grid lines, soft uneven reflections, no painted motifs. Pelvis, inner thighs, and both arms fully glazed and crackled. Authentic Chinese Song style.",
    "Standing with hips turned slightly to the right and chest angled toward the camera, front leg crossed slightly in front, hands clasped loosely at her side hip.",
    "7-inch sky-blue crackle-glazed platform pumps. Nails: extra long oval nails, pale blue with fine crackle tips.",
    "Quiet Song ceramics gallery with pale celadon bowls in glass cases, softly blurred.",
    "Soft cool museum light with warm raking side light.")
add("la_craft_solo_ru_guan_seat", "LA Craft Solo – Ru-Guan (Seated)",
    "ONE extremely large SuperBBW Chinese woman in her mid-40s, black hair in a loose low chignon with a celadon hairpin, natural face with a calm smile.",
    seat("spreading across the stool"),
    "Full body Guan ware celadon body painting from neck to ankle, painted directly on bare skin, one continuous surface. High-gloss pale grey-green glaze with a fine dense crackle of thin dark lines, soft uneven reflections, no painted motifs, not kintsugi. Pelvis, inner thighs, and both arms fully glazed and crackled. Authentic Chinese Song style.",
    "Seated on a carved stone garden stool with hips angled slightly to the left, torso turned back toward the camera, legs crossed at the knee, far hand behind her, near hand on her knee.",
    "7-inch grey-green crackle-glazed platform Mary Jane stilettos. Nails: extra long almond nails, pale celadon tips.",
    "Classical Hangzhou garden pavilion with a misty lake, softly blurred.",
    "Soft diffused daylight with warm raking side light.")

# 9. Palekh
add("la_craft_solo_palekh_stand", "LA Craft Solo – Palekh (Standing)",
    "ONE extremely large SuperBBW Russian woman in her late 30s, long dark auburn hair in a single thick braid over one shoulder, natural face with a confident smile.",
    STAND,
    "Full body Palekh miniature lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer densely filled with fine gold-line folk-tale scenes — a blazing firebird across the bust, galloping troika horses and onion-dome towers across the belly, gold filigree vines wrapping hips and legs. Pelvis, inner thighs, and both arms fully painted. Authentic Russian Palekh style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly over the back leg, one hand on her wide hip, the other lifting her braid.",
    "8-inch black lacquer platform stilettos with gold firebird details. Nails: extra long stiletto nails, black with fine gold line tips.",
    "MANDATORY seamless matte black studio background.",
    "Warm narrow spotlight with raking side light.")
add("la_craft_solo_palekh_seat", "LA Craft Solo – Palekh (Seated)",
    "ONE extremely large SuperBBW Russian woman in her late 50s, silver-blonde hair in a braided crown, natural face with a warm smile.",
    seat("spreading across the chair"),
    "Full body Palekh miniature lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer with fine gold-line fairy-tale scenes — a snow maiden and birch forest across the bust, a winter sleigh and white horses on the belly, gold filigree snowflakes and vines on hips and legs. Pelvis, inner thighs, and both arms fully painted. Authentic Russian Palekh style.",
    "Seated in a carved gilded armchair with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, far forearm on the armrest, near hand on her knee.",
    "7-inch black lacquer platform Mary Jane stilettos with gold snowflake buckles. Nails: extra long almond nails, black with gold tips.",
    "Russian palace study with lacquer boxes on shelves and a frosted window, softly blurred.",
    "Warm lamp key with raking side light.")

# 10. Zhostovo
add("la_craft_solo_zhostovo_stand", "LA Craft Solo – Zhostovo (Standing)",
    "ONE extremely large SuperBBW Russian woman in her early 50s, honey-blonde braided crown with a small gold pin, natural face with a warm smile.",
    STAND,
    "Full body Zhostovo lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer covered in lush hand-painted bouquets of roses, peonies, and daisies in crimson, pink, cream, and green with luminous shaded petals, fine gold scroll borders at wrists and ankles. Underarms, sides, pelvis, inner thighs, and both arms fully painted, no bare skin gaps. Authentic Russian Zhostovo style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly over the back leg, one hand on her wide hip, the other at her collarbone.",
    "8-inch black lacquer platform stilettos with painted rose details and gold trim. Nails: extra long almond nails, black with painted rose tips.",
    "Russian imperial drawing room with silk walls and a brass samovar, softly blurred.",
    "Warm chandelier key with raking side light.")
add("la_craft_solo_zhostovo_seat", "LA Craft Solo – Zhostovo (Seated)",
    "ONE extremely large SuperBBW Russian woman in her late 20s, long wavy chestnut hair with a floral ribbon, natural face with a bright smile.",
    seat("spreading across the settee"),
    "Full body Zhostovo lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer with dense painted garden roses, forget-me-nots, and golden wheat sprays in soft pink, sky blue, and cream, fine gold scroll borders. Pelvis, inner thighs, and both arms fully painted, no bare skin gaps. Authentic Russian Zhostovo style.",
    "Seated on a velvet settee with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, far arm along the backrest, near hand on her knee.",
    "7-inch black lacquer platform ankle-strap stilettos with painted forget-me-not details. Nails: extra long coffin nails, black with pink rose tips.",
    "Russian dacha parlor with lace curtains and a tea table, softly blurred.",
    "Soft window light with raking side light.")

# 11. Khokhloma
add("la_craft_solo_khokhloma_stand", "LA Craft Solo – Khokhloma (Standing)",
    "ONE extremely large SuperBBW Russian woman in her early 70s, silver-white hair in a thick crown braid, natural face with warm smile lines.",
    STAND,
    "Full body Khokhloma lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black and gold lacquer with dense hand-painted red rowan berries, golden leaves, and curling grass scrolls. Pelvis, inner thighs, and both arms fully painted, no bare skin gaps. Authentic Russian folk style.",
    "Standing with hips turned slightly to the right and chest angled toward the camera, front leg crossed slightly in front, hands clasped loosely at her side hip.",
    "8-inch black-and-gold lacquer platform stilettos with red berry details. Nails: extra long almond nails, gold with red tips.",
    "Imperial Russian palace hall with gilded mouldings and chandeliers, softly blurred.",
    "Warm chandelier key with raking side light making the gold glow.")
add("la_craft_solo_khokhloma_seat", "LA Craft Solo – Khokhloma (Seated)",
    "ONE extremely large SuperBBW Russian woman in her early 40s, long straight platinum-blonde hair loose over the shoulders, natural face with a playful smile.",
    seat("spreading across the bench"),
    "Full body Khokhloma lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Glossy gold base with bold black and red strawberries, currants, and flowing kudrina leaf swirls densely covering bust, belly rolls, hips, and legs. Pelvis, inner thighs, and both arms fully painted. Authentic Russian folk style.",
    "Seated on a carved wooden bench with hips angled slightly to the left, torso turned back toward the camera, legs crossed at the knee, far hand behind her, near hand on her knee.",
    "8-inch gold lacquer platform Mary Jane stilettos with red strawberry buckles. Nails: extra long coffin nails, black with red tips.",
    "Rustic Russian izba interior with a painted tiled stove and wooden utensils, softly blurred.",
    "Warm firelight key with raking side light.")

# 12. Son Mai
add("la_craft_solo_sonmai_stand", "LA Craft Solo – Son Mai (Standing)",
    "ONE extremely large SuperBBW Vietnamese woman in her mid-50s, long black hair in a low bun with a gold lotus hairpin, natural face with a gentle smile.",
    STAND,
    "Full body Vietnamese son mai lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black and vermilion lacquer with gold-leaf lotus flowers, silver-leaf cranes, and crackled white eggshell mosaic clouds. Pelvis, inner thighs, and both arms fully patterned. No religious figures. Authentic Vietnamese style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly in front, one hand on her wide hip, the other at her collarbone.",
    "8-inch black lacquer platform stilettos with gold-leaf lotus details. Nails: extra long almond nails, black with gold-leaf tips.",
    "Hue imperial citadel hall with red lacquered columns, softly blurred.",
    "Warm key with raking side light making the gold leaf and eggshell glow.")
add("la_craft_solo_sonmai_seat", "LA Craft Solo – Son Mai (Seated)",
    "ONE extremely large SuperBBW Vietnamese woman in her early 30s, long straight black hair past the waist, natural face with a bright smile.",
    seat("spreading across the bench"),
    "Full body Vietnamese son mai lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Glossy deep red-brown lacquer with gold-leaf bamboo and areca palms, silver-leaf koi, and crackled white eggshell water ripples. Pelvis, inner thighs, and both arms fully patterned. Authentic Vietnamese style.",
    "Seated on a wooden bench with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, far hand behind her, near hand on her knee.",
    "7-inch red-brown lacquer platform Mary Jane stilettos with gold bamboo buckles. Nails: extra long coffin nails, red-brown with eggshell-white tips.",
    "Hoi An old house interior with lanterns and a courtyard view, softly blurred.",
    "Warm lantern light with raking side light.")

# 13. Lai Rod Nam
add("la_craft_solo_lairodnam_stand", "LA Craft Solo – Lai Rod Nam (Standing)",
    "ONE extremely large SuperBBW Thai woman in her late 30s, glossy black hair in a high topknot with a small gold ornament, natural face with a warm smile.",
    STAND,
    "Full body Thai lai rod nam lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer with bright gold-leaf stencil kranok flame scrolls, lotus buds, and naga serpents densely covering bust, belly rolls, hips, and legs. Pelvis, inner thighs, and both arms fully patterned, no plain black areas. No religious figures, no Buddha images. Authentic Thai style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly in front, one hand on her wide hip, the other in a graceful Thai dance gesture beside her shoulder.",
    "9-inch black lacquer platform stilettos with gold kranok details. Nails: extra long curved stiletto nails, black with gold tips.",
    "Grand Palace gallery with gilded red walls and mirrored mosaic pillars, softly blurred.",
    "Warm golden key with raking side light.")
add("la_craft_solo_lairodnam_seat", "LA Craft Solo – Lai Rod Nam (Seated)",
    "ONE extremely large SuperBBW Thai woman in her early 60s, silver-streaked black hair in a low bun with a jasmine garland, natural face with a gentle smile.",
    seat("spreading across the bench"),
    "Full body Thai lai rod nam lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer with bright gold-leaf stencil mythical birds, flowering vines, and kranok borders densely covering bust, belly rolls, hips, and legs. Pelvis, inner thighs, and both arms fully patterned. No religious figures. Authentic Thai style.",
    "Seated on a low gilded wooden bench with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, far hand behind her, near hand on her knee.",
    "8-inch black lacquer platform Mary Jane stilettos with gold kranok buckles. Nails: extra long curved nails, black with gold tips.",
    "Traditional Thai teak house interior with gilded lacquer cabinets and river view, softly blurred.",
    "Warm window light with raking side light.")

# 14. Minakari
add("la_craft_solo_minakari_stand", "LA Craft Solo – Minakari (Standing)",
    "ONE extremely large SuperBBW Iranian woman in her late 40s, long dark waves swept back with a thin gold headband, natural face with kohl-lined eyes and a confident smile.",
    STAND,
    "Full body Persian minakari enamel body painting from neck to ankle, painted directly on bare skin, one continuous surface, no collar band. Glossy deep cobalt and turquoise enamel base with fine gold outlines, filled with birds, roses, and arabesque vines in white, red, and green. Pelvis, inner thighs, and both arms fully patterned. Authentic Persian style.",
    "Standing with hips turned slightly to the right and chest angled toward the camera, front leg crossed slightly in front, one hand on her waist, the other lightly touching her headband.",
    "8-inch cobalt enamel platform stilettos with gold heels. Nails: extra long stiletto nails, cobalt with gold tips.",
    "Isfahan palace hall with mirror mosaic and arched niches, softly blurred.",
    "Warm lantern key with raking side light making the enamel shine.")
add("la_craft_solo_minakari_seat", "LA Craft Solo – Minakari (Seated)",
    "ONE extremely large SuperBBW Iranian woman in her early 60s, silver-streaked dark waves, natural face with a dignified smile.",
    seat("spreading across the divan"),
    "Full body Persian minakari enamel body painting from neck to ankle, painted directly on bare skin, one continuous surface. Glossy sky-blue and cobalt enamel base with fine gold outlines, filled with nightingales, pomegranates, and paisley vines in white, crimson, and emerald. Pelvis, inner thighs, and both arms fully patterned. Authentic Persian style.",
    "Seated on a low tiled divan with hips angled slightly to the left, torso turned back toward the camera, legs crossed at the knee, far hand on a cushion behind her, near hand on her knee.",
    "7-inch cobalt enamel platform ankle booties with gold heels. Nails: extra long almond nails, sky blue with gold tips.",
    "Shiraz garden pavilion with stained glass windows casting colored light, softly blurred.",
    "Warm key with raking side light.")

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
