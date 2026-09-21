# -*- coding: utf-8 -*-
r"""
patch_livingartifact_muscle_solo_1_json.py
Living Artifact · Muscle — 17 solo presets
(bodybuilder 5 + strongwoman 5 + muscle BBW 4 + extreme bodybuilder + mass monster + extreme muscle BBW)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_muscle_solo_1_json.py
    python preset_builders\patch_livingartifact_muscle_solo_1_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · Muscle"
PLATFORM = "gemini"
ASPECT = "2:3"

BB = ("Physique: extreme female bodybuilder, the most muscular physique physically possible — massive rounded "
      "shoulders with visible striations, huge biceps and triceps with prominent veins, broad flaring lats, deeply "
      "carved eight-pack abs, thick serratus, enormous quadriceps with a deep teardrop above the knee, sweeping "
      "hamstrings, diamond-shaped calves, full muscular chest. Shredded, every muscle separation visible. Not slim, "
      "not a fitness model — true competition bodybuilder mass.")

SW = ("Physique: extreme strongwoman physique, massively thick and powerful — huge trapezius rising toward the ears, "
      "broad thick shoulders, enormous arms, thick strong waist with a solid belly, massive powerful thighs and "
      "glutes, heavy muscle under a layer of softness, a body built for lifting stones and pulling trucks. Not lean, "
      "not a fitness model.")

MB = ("Physique: muscular SuperBBW, around 400 pounds — enormous frame with massive muscle under soft volume: huge "
      "rounded shoulders and thick muscular arms, heavy full bust, big round belly with soft rolls over a strong "
      "core, not pregnant, extremely wide hips, colossal muscular thighs and calves. Both huge and strong. Not slim, "
      "not a fitness model.")

NO_CLOTH = "The body painting is the only covering — no garments, no fabric, no bodysuit."

PRESETS = [
    # ── Bodybuilder ─────────────────────────────────────────
    {
        "key": "la_muscle_solo_bodybuilder_kintsugi",
        "title": "LA Muscle Solo – Bodybuilder · Kintsugi",
        "prompt": f"""Fine art body painting photography. Subject: ONE Japanese woman in her mid-30s, glossy black blunt bob, focused confident expression.

{BB}

Body Art: Full body Kintsugi painted directly on bare skin from neck to ankle, one continuous surface. {NO_CLOTH} High-gloss obsidian-black ceramic glaze with raised 24-karat gold repair seams tracing each muscle separation, like a shattered statue mended with gold. Underarms, inner arms, pelvis, and inner thighs fully painted.

Pose: Front lat spread — standing full frontal, fists on the waist, lats flared wide, chest lifted, abs tight. Chest and abs fully visible. Full body head to toe visible.

Footwear: 9-inch gold mirror-chrome peep-toe platform stilettos with crossed ankle straps. Nails: extra long stiletto, black with gold tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Low camera angle, 50mm lens. Hard raking side light carving every muscle, warm gold key making the seams glow. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_bodybuilder_palekh",
        "title": "LA Muscle Solo – Bodybuilder · Palekh",
        "prompt": f"""Fine art body painting photography. Subject: ONE Russian woman in her late 20s, dark auburn hair in a tight high braid, fierce smile.

{BB}

Body Art: Full body Palekh miniature lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {NO_CLOTH} Deep glossy black lacquer with fine gold-line firebird across the chest, troika horses over the abs, onion domes and gold filigree following the contours of shoulders, arms, and legs. Underarms, inner arms, pelvis, and inner thighs fully painted.

Pose: Front double biceps — standing full frontal, both arms raised to shoulder height and bent, biceps peaked, elbows level, chest open. Chest and abs fully visible. Full body head to toe visible.

Footwear: 8-inch black lacquer platform stiletto sandals with spiral straps coiling up the calf and gold firebird heels. Nails: extra long coffin, black with gold line.

Background & Lighting: Russian imperial hall with gilded mouldings, softly blurred. ONE woman only. Low camera angle, 50mm lens. Hard raking side light carving every muscle, warm chandelier key. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_bodybuilder_gamji",
        "title": "LA Muscle Solo – Bodybuilder · Gamji-geumni",
        "prompt": f"""Fine art body painting photography. Subject: ONE Korean woman in her late 30s, black hair in a sleek low bun with a gold binyeo, calm focused expression.

{BB}

Body Art: Full body gamji-geumni painted directly on bare skin from neck to ankle, one continuous surface. {NO_CLOTH} Glossy deep navy-indigo base, not purple, with bold gold ink lotus scrolls and cloud bands, fine gold lines tracing each muscle separation, no religious figures. Underarms, inner arms, pelvis, and inner thighs fully painted.

Pose: Side chest — body turned three-quarters, front arm bent across below the chest gripping the other wrist, chest expanded and turned toward the camera, front leg bent on the toes to show the calf. Chest and abs visible. Full body head to toe visible.

Footwear: 8-inch indigo lacquer T-strap platform stiletto sandals with fine gold lines. Nails: extra long almond, indigo with gold tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Low camera angle, 50mm lens. Hard raking side light carving every muscle, warm narrow spotlight making the gold lines shimmer. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_bodybuilder_celadon",
        "title": "LA Muscle Solo – Bodybuilder · Celadon Sanggam",
        "prompt": f"""Fine art body painting photography. Subject: ONE Korean woman in her late 20s, long black hair in a low braid with a jade pin, serene confident expression.

{BB}

Body Art: Full body Goryeo celadon painted directly on bare skin from neck to ankle, one continuous surface. {NO_CLOTH} High-gloss jade-green celadon glaze clearly covering all skin, fine crackle, black-and-white sanggam cranes and clouds, making her look like a living celadon statue. Underarms, inner arms, pelvis, and inner thighs fully painted.

Pose: Front relaxed pose — standing full frontal, arms slightly away from the sides, lats flared, quads tensed, abs tight, chin lifted. Chest and abs fully visible. Full body head to toe visible.

Footwear: 8-inch celadon-glazed platform stiletto sandals with ribbon laces tied below the knee. Nails: extra long almond, celadon with white tips.

Background & Lighting: Korean ceramics gallery with celadon vases on plinths, softly blurred. ONE woman only. Low camera angle, 50mm lens. Hard raking side light carving every muscle across the glaze, cool museum fill. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_bodybuilder_najeon_black",
        "title": "LA Muscle Solo – Bodybuilder · Black Najeon",
        "prompt": f"""Fine art body painting photography. Subject: ONE Korean woman in her early 40s, black hair in a tight low bun with a mother-of-pearl binyeo, composed strong expression.

{BB}

Body Art: Full body najeon-chilgi painted directly on bare skin from neck to ankle, one continuous surface, not latex. {NO_CLOTH} Deep glossy black lacquer inlaid with iridescent pink-green-blue mother-of-pearl cranes, pine, and waves, the inlay flashing on every muscle peak. Underarms, inner arms, pelvis, and inner thighs fully painted.

Pose: Side triceps — body turned three-quarters toward the camera, front arm straight down and locked to show the triceps, other hand holding the wrist behind, chest turned open to the camera, front leg bent. Chest and abs visible. Full body head to toe visible.

Footwear: 9-inch black lacquer caged platform stiletto sandals with pearl accents. Nails: extra long almond, black with pearl tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Low camera angle, 50mm lens. Hard raking side light carving every muscle so the mother-of-pearl flashes rainbow. 2:3 vertical 8K portrait.""",
    },
    # ── Strongwoman ─────────────────────────────────────────
    {
        "key": "la_muscle_solo_strongwoman_khokhloma",
        "title": "LA Muscle Solo – Strongwoman · Khokhloma",
        "prompt": f"""Fine art body painting photography. Subject: ONE Russian woman in her mid-30s, platinum-blonde hair in a thick side braid, broad face with a proud grin.

{SW}

Body Art: Full body Khokhloma lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {NO_CLOTH} Deep glossy black and gold lacquer with bold red rowan berries, golden leaves, and curling grass scrolls wrapping the thick arms and legs. Underarms, pelvis, and inner thighs fully painted.

Pose: Standing full frontal in a wide powerful stance, both fists on her hips, shoulders back, chest and belly fully visible. Full body head to toe visible.

Footwear: 9-inch black-and-gold lacquer platform gladiator stiletto sandals laced to mid-calf. Nails: extra long coffin, gold with red tips.

Background & Lighting: Rustic Russian wooden hall with carved beams, softly blurred. ONE woman only. Low camera angle, 50mm lens. Hard raking side light, warm firelight key. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_strongwoman_cloisonne",
        "title": "LA Muscle Solo – Strongwoman · Cloisonné",
        "prompt": f"""Fine art body painting photography. Subject: ONE Chinese woman in her early 40s, black hair in a high sleek bun with a gold hairpin, strong composed expression.

{SW}

Body Art: Full body jingtailan cloisonné enamel painted directly on bare skin from neck to ankle, one continuous surface, no collar band. {NO_CLOTH} Glossy turquoise enamel divided by raised gold wire cells filled with lotus scrolls and cloud bands in coral, cobalt, and white. Underarms, pelvis, and inner thighs fully painted.

Pose: Standing three-quarter front, one arm bent at shoulder height flexing a huge biceps, the other hand on her hip, chest and belly fully visible. Full body head to toe visible.

Footwear: 8-inch turquoise enamel multi-strap platform stiletto sandals with raised gold wire. Nails: extra long stiletto, turquoise with gold tips.

Background & Lighting: Museum gallery of Ming cloisonné, softly blurred. ONE woman only. Low camera angle, 50mm lens. Hard raking side light making the gold wires glint on every muscle. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_strongwoman_lairodnam",
        "title": "LA Muscle Solo – Strongwoman · Lai Rod Nam",
        "prompt": f"""Fine art body painting photography. Subject: ONE Thai woman in her late 20s, glossy black hair in a high topknot with a small gold ornament, bold smile.

{SW}

Body Art: Full body lai rod nam lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {NO_CLOTH} Deep glossy black lacquer with bright gold-leaf kranok flames and naga scrolls wrapping the thick limbs, no religious figures. Underarms, pelvis, and inner thighs fully painted.

Pose: Standing with one foot raised on a low black stone block, knee bent, one forearm resting on the raised knee, the other hand on her hip, torso upright facing camera, chest and belly fully visible. Full body head to toe visible.

Footwear: 9-inch black lacquer peep-toe platform stilettos with crossed gold ankle straps. Nails: extra long curved stiletto, black with gold tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Low camera angle, 50mm lens. Hard raking side light, warm gold key and rim light. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_strongwoman_makie",
        "title": "LA Muscle Solo – Strongwoman · Maki-e",
        "prompt": f"""Fine art body painting photography. Subject: ONE Japanese woman in her mid-40s, glossy black hair in a low chignon with a lacquer comb, calm powerful expression.

{SW}

Body Art: Full body maki-e lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. The body painting is the only covering — no garments, no fabric, no kimono, no bodysuit. Deep glossy black urushi with fine sprinkled gold dust forming sweeping waves and chrysanthemums, minimal plain black. Underarms, pelvis, and inner thighs fully painted.

Pose: Front lat spread — standing full frontal, fists on the waist, lats and traps flared wide, chest lifted. Chest and belly fully visible. Full body head to toe visible.

Footwear: 8-inch knee-high lace-up black lacquer platform stiletto boots with gold-dust detailing, visible boot edge. Nails: extra long almond, black with gold powder tips.

Background & Lighting: Traditional Japanese wooden dojo with polished floor, softly blurred. ONE woman only. Low camera angle, 50mm lens. Hard raking side light making the gold dust glitter on every muscle. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_strongwoman_ru_guan",
        "title": "LA Muscle Solo – Strongwoman · Ru-Guan",
        "prompt": f"""Fine art body painting photography. Subject: ONE Chinese woman in her early 30s, long straight black hair tied low, steady confident expression.

{SW}

Body Art: Full body Ru-Guan celadon painted directly on bare skin from neck to ankle, one continuous surface. {NO_CLOTH} High-gloss deep saturated sky-blue-grey glaze clearly different from skin, fine dense crackle of thin dark lines, no painted motifs, not kintsugi — like a monumental glazed statue. Underarms, pelvis, and inner thighs fully glazed.

Pose: Standing full frontal, hands clasped behind her lower back, shoulders and traps squared, chest and belly fully visible. Full body head to toe visible.

Footwear: 8-inch sky-blue crackle-glazed caged platform stiletto sandals. Nails: extra long almond, pale blue.

Background & Lighting: Quiet Song ceramics gallery, softly blurred. ONE woman only. Low camera angle, 50mm lens. Hard raking side light across the glaze, cool museum fill. 2:3 vertical 8K portrait.""",
    },
    # ── Muscle BBW ──────────────────────────────────────────
    {
        "key": "la_muscle_solo_musclebbw_zhostovo",
        "title": "LA Muscle Solo – Muscle BBW · Zhostovo",
        "prompt": f"""Fine art body painting photography. Subject: ONE Russian woman in her late 30s, honey-blonde braided crown, full round face with a bright grin.

{MB}

Body Art: Full body Zhostovo lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {NO_CLOTH} Deep glossy black lacquer with lush painted rose and peony bouquets and gold scroll borders. Underarms, inner arms, pelvis, and inner thighs fully painted.

Pose: Front double biceps — standing full frontal, both arms raised to shoulder height and bent, huge biceps flexed, chest open. Chest and belly fully visible. Full body head to toe visible.

Footwear: 8-inch black lacquer d'Orsay platform stilettos with painted roses. Nails: extra long almond, black with rose tips.

Background & Lighting: Russian imperial drawing room with a brass samovar, softly blurred. ONE woman only. Low camera angle, 50mm lens. Hard raking side light, warm chandelier key. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_musclebbw_najeon_vermilion",
        "title": "LA Muscle Solo – Muscle BBW · Vermilion Najeon",
        "prompt": f"""Fine art body painting photography. Subject: ONE Korean woman in her late 40s, black hair in a sleek high bun with a coral binyeo, full round face with a confident smile.

{MB}

Body Art: Full body najeon-chilgi painted directly on bare skin from neck to ankle, one continuous surface, not latex. The body painting is the only covering — no garments, no fabric, no hanbok, no bodysuit. Deep glossy vermilion lacquer clearly different from skin, inlaid with iridescent mother-of-pearl phoenixes and peonies. Underarms, pelvis, and inner thighs fully painted.

Pose: Standing full frontal, both fists on her hips, elbows out, shoulders squared, chest and belly fully visible. Full body head to toe visible.

Footwear: 9-inch vermilion lacquer peep-toe platform stilettos with crossed ankle straps. Nails: extra long coffin, vermilion with pearl tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Low camera angle, 50mm lens. Hard raking side light so the mother-of-pearl flashes, soft rim light. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_musclebbw_sonmai",
        "title": "LA Muscle Solo – Muscle BBW · Son Mai",
        "prompt": f"""Fine art body painting photography. Subject: ONE Vietnamese woman in her late 20s, straight black hair falling to her waist, full round face with a warm smile.

{MB}

Body Art: Full body son mai lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {NO_CLOTH} Crackled white eggshell inlay clearly visible as mosaic clouds, set in deep glossy black and vermilion lacquer with gold-leaf lotus and silver-leaf cranes. Underarms, pelvis, and inner thighs fully painted.

Pose: Standing three-quarter front, one arm extended to the side at shoulder height showing the thick muscular arm, the other hand on her hip, chest and belly fully visible. Full body head to toe visible.

Footwear: 8-inch black lacquer caged platform stiletto sandals with gold-leaf lotus. Nails: extra long almond, black with eggshell-white tips.

Background & Lighting: Hue imperial citadel hall with red lacquered columns, softly blurred. ONE woman only. Low camera angle, 50mm lens. Hard raking side light making the gold leaf and eggshell glow. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_musclebbw_minakari",
        "title": "LA Muscle Solo – Muscle BBW · Minakari",
        "prompt": f"""Fine art body painting photography. Subject: ONE Iranian woman in her mid-30s, long dark waves with a thin gold headband, full round face with kohl-lined eyes and a strong smile.

{MB}

Body Art: Full body Persian minakari enamel painted directly on bare skin from neck to ankle, one continuous surface, no collar band. {NO_CLOTH} Glossy cobalt and turquoise enamel with fine gold outlines, birds, roses, and arabesque vines. Underarms, pelvis, and inner thighs fully painted.

Pose: Standing full frontal, feet planted wide, both hands resting on top of her belly, shoulders back, chest and belly fully visible. Full body head to toe visible.

Footwear: 8-inch cobalt enamel multi-strap platform stiletto sandals outlined in gold. Nails: extra long stiletto, cobalt with gold tips.

Background & Lighting: Isfahan palace hall with mirror mosaic and arched niches, softly blurred. ONE woman only. Low camera angle, 50mm lens. Hard raking side light, warm lantern key making the enamel shine. 2:3 vertical 8K portrait.""",
    },
    # ── Extreme variants ────────────────────────────────────
    {
        "key": "la_muscle_solo_extreme_bodybuilder_kintsugi",
        "title": "LA Muscle Solo – Extreme Bodybuilder · Kintsugi",
        "prompt": f"""Fine art body painting photography. Subject: ONE Japanese woman in her early 30s, glossy black hair slicked back into a tight low bun, intense focused expression.

Physique: the most extreme female bodybuilder physique physically possible, beyond professional open-class mass. Gigantic boulder shoulders with deep striations, traps rising steeply to the ears, colossal biceps with a high peak and thick veins running over them, horseshoe triceps, forearms like a man's calves. Massive thick chest plates, lats flaring so wide the torso forms a sharp V. Deeply carved eight-pack abs with thick serratus and intercostals visible. Enormous quadriceps with separated vastus heads and a huge teardrop above the knee, cross-striated thighs, sweeping hamstrings, diamond calves. Paper-thin skin, shredded to competition condition, every fiber and vein visible. Not slim, not a fitness or figure model — the most muscular woman imaginable.

Body Art: Full body Kintsugi painted directly on bare skin from neck to ankle, one continuous surface. {NO_CLOTH} High-gloss obsidian-black ceramic glaze with raised 24-karat gold repair seams running precisely along every muscle separation — between the delts, down the center of the abs, around each quad head — like a shattered bronze statue mended with gold. Underarms, inner arms, pelvis, and inner thighs fully painted.

Pose: Front lat spread — standing full frontal, fists pressed into the waist, lats flared to maximum width, chest lifted high, abs tight, quads flexed. Chest and abs fully visible. Full body head to toe visible.

Footwear: Towering 9-inch gold mirror-chrome peep-toe platform stilettos with crossed ankle straps.
Nails: Extra long stiletto nails, black with gold tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Low camera angle, 50mm lens. Hard raking side light from one direction carving every muscle into deep shadow and bright highlight, warm gold key making the seams glow, thin rim light tracing the silhouette. Emphasis on the extreme muscular mass. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_massmonster_kintsugi",
        "title": "LA Muscle Solo – Mass Monster · Kintsugi",
        "prompt": f"""Fine art body painting photography. Subject: ONE Japanese woman in her early 30s, glossy black hair slicked back into a tight low bun, intense focused expression.

Physique: a colossal female mass monster in offseason bulk — 6 feet 4 inches tall and around 330 pounds of dense muscle, the biggest and heaviest muscular woman physically possible. Shoulders wider than a doorway, gigantic round boulder delts, traps swelling up into the neck, a thick powerful neck. Enormous swollen arms thicker than a normal woman's thighs, huge biceps and horseshoe triceps. Massive barrel chest and a thick, wide ribcage, lats spreading like wings. Thick powerful waist with blocky abs under a thin layer of fullness. Gigantic tree-trunk quadriceps wider than her hips, huge sweeping hamstrings, massive calves. Full, thick, dense, and swollen everywhere — not shredded and small, not slim, not a fitness or figure model. Her body fills the entire width of the frame.

Body Art: Full body Kintsugi painted directly on bare skin from neck to ankle, one continuous surface. {NO_CLOTH} High-gloss obsidian-black ceramic glaze with raised 24-karat gold repair seams running along the major muscle borders — around the delts, down the center of the torso, around each quad — like a giant shattered bronze statue mended with gold. Underarms, inner arms, pelvis, and inner thighs fully painted.

Pose: Front lat spread — standing full frontal in a wide planted stance, fists pressed into the waist, lats flared to maximum width, chest lifted, quads flexed. Chest and abs fully visible. Full body head to toe visible.

Footwear: Towering 9-inch gold mirror-chrome peep-toe platform stilettos with crossed ankle straps.
Nails: Extra long stiletto nails, black with gold tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Camera straight-on at waist height, 35mm lens, her body filling the frame edge to edge. Hard raking side light carving the muscle masses, warm gold key making the seams glow, thin rim light tracing the enormous silhouette. Emphasis on the colossal size and mass of her body. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_muscle_solo_extreme_musclebbw_khokhloma",
        "title": "LA Muscle Solo – Extreme Muscle BBW · Khokhloma",
        "prompt": f"""Fine art body painting photography. Subject: ONE Russian woman in her mid-30s, platinum-blonde hair in a thick side braid, full round face with a proud grin.

Physique: extreme muscular SuperBBW, around 550 pounds, built like a super heavyweight strongwoman crossed with a sumo wrestler. Enormous thick trapezius rising to the ears, colossal rounded shoulders, gigantic arms with huge biceps and triceps visible under heavy softness. Massive heavy bust over a huge round belly with deep soft rolls hanging over a powerful thick core, not pregnant. Extremely wide hips, gigantic tree-trunk thighs with visible quad sweep under the fat, massive muscular calves. Thick powerful neck, full round face. The biggest and strongest body physically possible — both colossal fat volume and colossal muscle at once. Not a fitness model, not lean, not merely curvy.

Body Art: Full body Khokhloma lacquer painted directly on bare skin from neck to ankle, one continuous surface, not latex. {NO_CLOTH} Deep glossy black and gold lacquer with bold red rowan berries and golden leaves. Underarms, inner arms, pelvis, and inner thighs fully painted.

Pose: Standing full frontal in a wide powerful stance, one arm bent at shoulder height flexing a gigantic biceps, the other fist on her hip, chest and belly fully visible. Full body head to toe visible.

Footwear: 9-inch black-and-gold lacquer platform gladiator stiletto sandals laced to mid-calf. Nails: extra long coffin, gold with red tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Straight-on at waist height, 35mm lens. Hard raking side light revealing muscle shape beneath the volume, warm gold key. Emphasis on the colossal muscular SuperBBW body. 2:3 vertical 8K portrait.""",
    },
]

RATIO_RE = re.compile(r"\b(?:2:3|3:4|4:5)(?= vertical)")


def normalize_prompt(text: str) -> str:
    return RATIO_RE.sub(ASPECT, text.strip())


def main() -> int:
    force = "--force" in sys.argv
    if not PRESETS_DIR.is_dir():
        print(f"[ERROR] presets dir not found: {PRESETS_DIR}")
        return 1
    keys = [p["key"] for p in PRESETS]
    if len(keys) != len(set(keys)):
        print("[ERROR] duplicate keys in PRESETS")
        return 1

    written, skipped = 0, 0
    for p in PRESETS:
        path = PRESETS_DIR / f"{p['key']}.json"
        if path.exists() and not force:
            print(f"[SKIP] exists: {path.name}")
            skipped += 1
            continue
        data = {
            "title": p["title"],
            "category": CATEGORY,
            "platform": PLATFORM,
            "aspect_ratio": ASPECT,
            "prompt": normalize_prompt(p["prompt"]),
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
