# -*- coding: utf-8 -*-
r"""
patch_livingartifact_colossal_600_1_json.py
Living Artifact · Colossal — 14 solo presets (true extreme SuperBBW ~600 lb, S-tier materials)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_colossal_600_1_json.py
    python preset_builders\patch_livingartifact_colossal_600_1_json.py --force   (overwrite)
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

PHYSIQUE = ("Physique: true extreme SuperBBW, around 600 pounds, the largest body physically possible. Enormous apron "
            "belly hanging in several heavy overlapping rolls down to mid-thigh, belly wider than the chest, not pregnant. "
            "Gigantic heavy bust resting on top of the belly. Hips and thighs extremely wide, thighs pressed together "
            "with deep soft folds, dimpled knees, thick calves. Massive soft upper arms as thick as thighs. Soft side "
            "rolls visible at the waist. Full round face with a soft double chin. Not curvy, not hourglass, not a "
            "plus-size fashion model — a true extreme SuperBBW body filling the entire frame width.")

ENDING = "Emphasis on the true extreme SuperBBW body volume. 2:3 vertical 8K portrait."


def build(subject, body_art, pose, foot, bg):
    return "\n\n".join([
        f"Fine art body painting photography. Subject: {subject}",
        PHYSIQUE,
        f"Body Art: {body_art}",
        f"Pose: {pose} Full body head to toe visible.",
        f"Footwear: {foot}",
        f"Background & Lighting: {bg} {ENDING}",
    ])


def cover(extra=""):
    return f"The body painting is the only covering — no garments, no fabric,{extra} no bodysuit."


PRESETS = [
    ("la_colossal_600_sonmai", "LA Colossal 600 – Son Mai", build(
        "ONE true extreme SuperBBW Vietnamese woman in her early 30s, straight black hair falling to her waist, full round face with a warm smile.",
        f"Full body Vietnamese son mai lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {cover()} Deep glossy black and vermilion lacquer with gold-leaf lotus, silver-leaf cranes, and crackled white eggshell mosaic clouds.",
        "Standing full frontal, both hands on her hips, elbows out, chest and belly fully visible.",
        "8-inch black lacquer caged platform stiletto sandals with gold-leaf lotus. Nails: extra long almond, black with eggshell-white tips.",
        "Hue imperial citadel hall with red lacquered columns, softly blurred. ONE woman only. Low camera angle, 50mm lens. Warm key with raking side light making the gold leaf and eggshell glow.")),
    ("la_colossal_600_lairodnam", "LA Colossal 600 – Lai Rod Nam", build(
        "ONE true extreme SuperBBW Thai woman in her late 20s, glossy black hair in a high topknot with a small gold ornament, full round face with a bright smile.",
        f"Full body Thai lai rod nam lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {cover()} Deep glossy black lacquer with bright gold-leaf kranok flames, lotus buds, and naga scrolls, no religious figures.",
        "Standing in three-quarter front view, one arm extended gracefully to the side at shoulder height in a Thai dance gesture, the other hand on her hip, chest and belly fully visible.",
        "9-inch black lacquer peep-toe platform stilettos with crossed gold ankle straps. Nails: extra long curved stiletto, black with gold tips.",
        "MANDATORY seamless matte black studio background. ONE woman only. Low camera angle, 50mm lens. Warm gold key with raking side light and soft rim light outlining the body silhouette.")),
    ("la_colossal_600_minakari", "LA Colossal 600 – Minakari", build(
        "ONE true extreme SuperBBW Iranian woman in her late 30s, long dark waves with a thin gold headband, full round face with kohl-lined eyes and a confident smile.",
        f"Full body Persian minakari enamel painted directly on bare skin from neck to ankle, one continuous surface, no collar band. {cover()} Glossy cobalt and turquoise enamel with fine gold outlines, birds, roses, and arabesque vines.",
        "Standing full frontal, hands clasped loosely behind her lower back, shoulders drawn back, chest and belly fully visible.",
        "8-inch cobalt enamel multi-strap platform stiletto sandals outlined in gold. Nails: extra long stiletto, cobalt with gold tips.",
        "Isfahan palace hall with mirror mosaic and arched niches, softly blurred. ONE woman only. Low camera angle, 50mm lens. Warm lantern key with raking side light making the enamel shine.")),
    ("la_colossal_600_khokhloma", "LA Colossal 600 – Khokhloma", build(
        "ONE true extreme SuperBBW Russian woman in her late 20s, long honey-blonde side braid, full round face with a sweet smile.",
        f"Full body Khokhloma lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {cover()} Deep glossy black and gold lacquer with dense red rowan berries, golden leaves, and curling grass scrolls.",
        "Standing in three-quarter front view, one hand lifting her braid at shoulder height, the other on her hip, chest and belly fully visible.",
        "9-inch black-and-gold lacquer platform gladiator stiletto sandals laced to mid-calf with red berry motifs. Nails: extra long almond, gold with red tips.",
        "Russian imperial hall with gilded mouldings and chandeliers, softly blurred. ONE woman only. Low camera angle, 50mm lens. Warm chandelier key with raking side light.")),
    ("la_colossal_600_celadon", "LA Colossal 600 – Celadon Sanggam", build(
        "ONE true extreme SuperBBW Korean woman in her early 30s, long black hair in a low braid with a jade binyeo, full round face with a serene smile.",
        f"Full body Goryeo celadon painted directly on bare skin from neck to ankle, one continuous surface. {cover(' no hanbok,')} High-gloss jade-green celadon glaze clearly covering all skin, fine crackle, black-and-white sanggam cranes and clouds.",
        "Standing full frontal, both hands on her hips, elbows out, chest and belly fully visible.",
        "8-inch celadon-glazed platform stiletto sandals with ribbon laces tied below the knee. Nails: extra long almond, celadon with white tips.",
        "Korean ceramics gallery with celadon maebyeong vases, softly blurred. ONE woman only. Low camera angle, 50mm lens. Cool museum light with warm raking side light across the glaze.")),
    ("la_colossal_600_najeon_vermilion", "LA Colossal 600 – Vermilion Najeon", build(
        "ONE true extreme SuperBBW Korean woman in her early 40s, black hair in a sleek high bun with a coral binyeo, full round face with a bright smile.",
        f"Full body najeon-chilgi painted directly on bare skin from neck to ankle, one continuous surface, not latex. {cover(' no hanbok,')} Deep glossy vermilion lacquer clearly different from skin, inlaid with thick cut mother-of-pearl in pink, green, and blue rainbow sheen — peonies, vines, and butterflies.",
        "Standing in three-quarter front view, one hand lightly touching her binyeo at shoulder height, the other on her hip, chest and belly fully visible.",
        "9-inch vermilion lacquer peep-toe platform stilettos with crossed ankle straps and mother-of-pearl heels. Nails: extra long coffin, vermilion with pearl tips.",
        "MANDATORY seamless matte black studio background. ONE woman only. Low camera angle, 50mm lens. Warm key with strong raking side light so the mother-of-pearl flashes rainbow, soft rim light.")),
    ("la_colossal_600_najeon_black", "LA Colossal 600 – Black Najeon", build(
        "ONE true extreme SuperBBW Korean woman in her late 40s, silver-streaked black hair in a sleek low bun with a mother-of-pearl binyeo, full round face with a calm smile.",
        f"Full body najeon-chilgi painted directly on bare skin from neck to ankle, one continuous surface, not latex, subtle brush texture beneath the shine. {cover(' no hanbok,')} Deep glossy black lacquer inlaid with iridescent pink-green-blue mother-of-pearl — full moon on the belly, cranes on the bust, pine and waves on the legs.",
        "Standing full frontal, hands clasped loosely behind her lower back, chest and belly fully visible.",
        "9-inch black lacquer caged platform stiletto sandals with mother-of-pearl accents. Nails: extra long almond, black with pearl tips.",
        "Hanok daecheong hall with paper lattice doors and a white moon jar, softly blurred. ONE woman only. Low camera angle, 50mm lens. Warm window light with strong raking side light.")),
    ("la_colossal_600_gamji", "LA Colossal 600 – Gamji-geumni", build(
        "ONE true extreme SuperBBW Korean woman in her late 20s, long black hair in a single low braid, full round face with a gentle smile.",
        f"Full body gamji-geumni painted directly on bare skin from neck to ankle, one continuous surface. {cover(' no hanbok,')} Glossy deep navy-indigo base, not purple, with bold dense gold ink lotus medallion on the belly, vine scrolls on the bust, cloud bands and lotus-petal borders on the legs, no religious figures.",
        "Standing in three-quarter front view, one arm extended gracefully to the side at shoulder height, the other hand on her hip, chest and belly fully visible.",
        "8-inch indigo lacquer T-strap platform stiletto sandals with fine gold lines. Nails: extra long almond, indigo with gold tips.",
        "MANDATORY seamless matte black studio background. ONE woman only. Low camera angle, 50mm lens. Warm narrow spotlight with raking side light making the gold lines shimmer, soft rim light.")),
    ("la_colossal_600_kintsugi", "LA Colossal 600 – Kintsugi", build(
        "ONE true extreme SuperBBW Japanese woman in her early 30s, glossy black blunt bob with bangs, full round face with a confident smile.",
        f"Full body Kintsugi painted directly on bare skin from neck to ankle, one continuous surface. {cover(' no kimono,')} High-gloss celadon-green ceramic glaze with a dense network of many fine raised 24-karat gold repair seams following every roll and curve.",
        "Standing full frontal, both hands resting softly on her lower belly, shoulders back, chest and belly fully visible.",
        "9-inch gold mirror-chrome peep-toe platform stilettos with crossed ankle straps. Nails: extra long stiletto, celadon with gold crack lines.",
        "Contemporary ceramics gallery with mended vessels on white plinths, softly blurred. ONE woman only. Low camera angle, 50mm lens. Warm gold key with raking side light making the gold seams glow.")),
    ("la_colossal_600_makie", "LA Colossal 600 – Maki-e", build(
        "ONE true extreme SuperBBW Japanese woman in her late 30s, glossy black hair in a soft chignon with a gold hairpin, full round face with a calm smile.",
        f"Full body maki-e lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {cover(' no kimono,')} Deep glossy black urushi with fine sprinkled gold dust, visible particles, forming a full moon, autumn grasses, and flying geese, crisp raised gold relief.",
        "Standing in three-quarter front view, one hand touching her hairpin at shoulder height, the other on her hip, chest and belly fully visible.",
        "8-inch knee-high lace-up black lacquer platform stiletto boots with gold-dust detailing, visible boot edge. Nails: extra long almond, black with gold powder tips.",
        "Kyoto tea house engawa with shoji screens and a moss garden, softly blurred. ONE woman only. Low camera angle, 50mm lens. Soft window light with warm raking side light making the gold dust glitter.")),
    ("la_colossal_600_cloisonne", "LA Colossal 600 – Cloisonné", build(
        "ONE true extreme SuperBBW Chinese woman in her late 30s, black hair in a high sleek bun with a gold hairpin, full round face with a composed smile.",
        f"Full body jingtailan cloisonné enamel painted directly on bare skin from neck to ankle, one continuous surface, no collar band. {cover(' no qipao,')} Glossy turquoise enamel divided by raised gold wire cells filled with lotus scrolls and peonies in coral, cobalt, and white.",
        "Standing full frontal, both hands on her hips, elbows out, chest and belly fully visible.",
        "8-inch turquoise enamel multi-strap platform stiletto sandals with raised gold wire. Nails: extra long stiletto, turquoise with gold tips.",
        "Museum gallery of Ming cloisonné vessels in glass cases, softly blurred. ONE woman only. Low camera angle, 50mm lens. Warm museum key with raking side light making the gold wires glow.")),
    ("la_colossal_600_ru_guan", "LA Colossal 600 – Ru-Guan", build(
        "ONE true extreme SuperBBW Chinese woman in her early 40s, black hair in a soft low chignon with a pale jade pin, full round face with a serene smile.",
        f"Full body Song dynasty Ru-Guan celadon painted directly on bare skin from neck to ankle, one continuous surface. {cover()} High-gloss deep saturated sky-blue-grey glaze clearly different from skin, with a fine dense crackle of thin dark lines and golden secondary crackle, no painted motifs, not kintsugi.",
        "Standing in three-quarter front view, one hand lifting a loose strand of hair at shoulder height, the other on her hip, chest and belly fully visible.",
        "9-inch sky-blue crackle-glazed caged platform stiletto sandals. Nails: extra long almond, pale blue with fine crackle.",
        "Quiet Song ceramics gallery with pale celadon bowls in glass cases, softly blurred. ONE woman only. Low camera angle, 50mm lens. Soft cool museum light with warm raking side light.")),
    ("la_colossal_600_palekh", "LA Colossal 600 – Palekh", build(
        "ONE true extreme SuperBBW Russian woman in her late 30s, dark auburn hair in a thick braid over one shoulder, full round face with a confident smile.",
        f"Full body Palekh miniature lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {cover()} Deep glossy black lacquer densely filled with fine gold-line firebird on the bust, troika horses and onion domes across the belly, gold filigree vines on the legs, minimal plain black.",
        "Standing in a wide stance, one arm extended gracefully to the side at shoulder height, the other hand on her hip, chest and belly fully visible.",
        "8-inch black lacquer platform stiletto sandals with spiral straps coiling up the calf and gold firebird heels. Nails: extra long stiletto, black with fine gold line tips.",
        "Russian imperial ballroom with gilded mouldings and chandeliers, softly blurred. ONE woman only. Low camera angle, 50mm lens. Warm chandelier key with raking side light.")),
    ("la_colossal_600_zhostovo", "LA Colossal 600 – Zhostovo", build(
        "ONE true extreme SuperBBW Russian woman in her early 30s, honey-blonde braided crown with a small gold pin, full round face with a warm smile.",
        f"Full body Zhostovo lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {cover()} Deep glossy black lacquer covered in lush painted bouquets of roses, peonies, and daisies in crimson, pink, cream, and green, fine gold scroll borders at wrists and ankles. Underarms, sides, and inner thighs fully painted.",
        "Standing full frontal, feet together with a soft hip shift, both hands gently framing her face with elbows low, chest and belly fully visible.",
        "8-inch black lacquer d'Orsay platform stilettos with painted roses and gold trim. Nails: extra long almond, black with painted rose tips.",
        "Russian imperial drawing room with silk walls and a brass samovar, softly blurred. ONE woman only. Low camera angle, 50mm lens. Warm chandelier key with raking side light.")),
]

RATIO_RE = re.compile(r"\b(?:2:3|3:4|4:5)(?= vertical)")


def main() -> int:
    force = "--force" in sys.argv
    if not PRESETS_DIR.is_dir():
        print(f"[ERROR] presets dir not found: {PRESETS_DIR}")
        return 1
    keys = [k for k, _, _ in PRESETS]
    if len(keys) != len(set(keys)):
        print("[ERROR] duplicate keys in PRESETS")
        return 1

    written, skipped = 0, 0
    for key, title, prompt in PRESETS:
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

    print(f"\nDone. written={written} skipped={skipped} total={len(PRESETS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
