# -*- coding: utf-8 -*-
r"""
patch_livingartifact_ussbbw_1_json.py
Living Artifact · USSBBW — 20 solo presets (2:3)
Confirmed extreme SuperBBW standard: USSBBW single label, several overlapping belly rolls to mid-thigh,
arms away from torso, roll-following pattern, raking light, thick platform heels, darkest skin first.

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_ussbbw_1_json.py
    python preset_builders\patch_livingartifact_ussbbw_1_json.py --force   (overwrite)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · USSBBW"
PLATFORM = "gemini"
ASPECT = "2:3"

SKIN = ("Her face, neck, hands, and all skin are THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, blue-black void "
        "complexion darker than night sky, not brown, even under warm light.")

BODY = ("USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits, around 800 pounds — an "
        "enormous soft apron belly hanging in several heavy overlapping rolls down to mid-thigh, the belly wider than "
        "the chest and projecting far forward, deep shadowed creases between each roll, not pregnant, a gigantic heavy "
        "bust resting on top of the belly, no waist at all, deep side rolls visible past the silhouette, hips wider "
        "than a normal woman's whole torso, huge thighs pressed together with deep folds, enormous soft upper arms, a "
        "very full round face with a double chin. Not curvy, not hourglass, not a plus-size model.")

COVER = "painted directly on bare skin from neck to ankle, the only covering — no garments, no fabric, no bodysuit"

POSE = {
    "hips": ("Standing full frontal in a wide stance, arms held slightly away from the torso with hands resting on "
             "the outer hips, so the painted belly and every roll are fully visible, shoulders back, full body head to toe."),
    "arm": ("Standing full frontal in a wide stance, one arm extended to the side at shoulder height, the other arm "
            "held away from the torso with the hand on the outer hip, so the painted belly and every roll are fully "
            "visible, shoulders back, full body head to toe."),
}

VOID = "pure pitch black void background."
TAIL = ("Low camera angle, 50mm lens, her body filling the frame edge to edge. Emphasis on the most extreme body "
        "volume ever displayed. 2:3 vertical 8K portrait.")


def warm_bg(place):
    return f"{place}, softly blurred, the wall directly behind her much lighter than her body."


def build(age, hair, art, pose, shoes, nails, bg, light):
    return "\n\n".join([
        "Fine art body painting photography, full body shot of ONE woman.",
        f"Physique: {SKIN} {age}, {BODY} {hair}",
        f"Body Art: {art}",
        f"Pose: {POSE[pose]}",
        f"Footwear: {shoes} Nails: {nails}",
        f"Background & Lighting: {bg} {light} Raking side light carving deep shadows between each belly roll, "
        f"strong warm rim light tracing the enormous silhouette. {TAIL}",
    ])


P = []  # (key, title, prompt)


def add(num, slug, title, *args):
    P.append((f"la_ussbbw_{num:02d}_{slug}", f"LA USSBBW {num:02d} – {title}", build(*args)))


NJ_SHELL = ("Deep glossy black lacquer densely inlaid with thick cut mother-of-pearl shell pieces with visible sharp cut "
            "edges, each piece flashing strong pink, green, and blue iridescent rainbow sheen — not painted, real inlaid shell.")
NJ_ROLL = "The pattern follows every belly roll, with darker lacquer settling into each deep crease so the overlapping folds read clearly."
HANOK = warm_bg("warm hanok daecheong hall with glowing golden paper lattice doors on both sides and a pale cream wall")
IREZ = "Bold black sumi outlines with soft bokashi shading, colors bright enough to stand out against the darkest skin."

# 1–3 Najeon
add(1, "najeon_black_peony", "Black Najeon Peony", "Early 40s",
    "Sleek center-parted low bun with a mother-of-pearl binyeo, warm smile.",
    f"Full body najeon-chilgi {COVER}, not latex. {NJ_SHELL} Continuous peony scrolls with cranes and butterflies flowing evenly across the shoulders, arms, torso, hips, thighs, and calves. {NJ_ROLL}",
    "hips", "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap with mother-of-pearl studs.",
    "extra long stiletto, black with pearl tips.", HANOK, "Warm indoor key making every shell piece flash rainbow.")
add(2, "najeon_black_chrysanthemum", "Black Najeon Chrysanthemum Scroll", "Late 40s",
    "Silver-streaked black hair in a low jjok-meori bun with a mother-of-pearl binyeo, calm smile.",
    f"Full body najeon-chilgi {COVER}, not latex. {NJ_SHELL} Continuous chrysanthemum scrolls with small birds and butterflies flowing evenly across the shoulders, arms, torso, hips, thighs, and calves. {NJ_ROLL}",
    "arm", "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad padded ankle cuff inlaid with shell.",
    "extra long almond, black with pearl tips.",
    warm_bg("warm Joseon palace hall with red lacquered columns and glowing golden paper windows, a pale cream wall"),
    "Warm indoor key making every shell piece flash rainbow.")
add(3, "najeon_vermilion", "Vermilion Najeon", "Early 40s",
    "Black hair in a sleek high bun with a coral binyeo, bright smile.",
    f"Full body najeon-chilgi {COVER}, not latex. Deep glossy vermilion lacquer clearly different from skin, densely inlaid with thick cut mother-of-pearl shell pieces with visible sharp cut edges flashing pink, green, and blue rainbow sheen — peonies, scrolling vines, and butterflies flowing evenly over the whole body. The pattern follows every belly roll, with deeper red lacquer settling into each crease so the overlapping folds read clearly.",
    "hips", "7-inch vermilion lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap with mother-of-pearl studs.",
    "extra long coffin, vermilion with pearl tips.", HANOK, "Warm indoor key making every shell piece flash rainbow.")

# 4–6 Kintsugi
KS = "Full body Kintsugi {cover}. {glaze} with a dense web of raised 24-karat gold repair seams branching over the whole body. The largest gold seams run along the deep crease beneath each belly roll and around the side rolls, like a colossal round vessel mended with gold, so every overlapping fold is outlined in gold."
add(4, "kintsugi_celadon", "Kintsugi Celadon", "Late 40s",
    "Short sculpted silver natural curls, calm smile.",
    KS.format(cover=COVER, glaze="High-gloss celadon-green ceramic glaze with fine crackle"),
    "hips", "7-inch gold mirror-chrome platform stilettos with a thick wide platform, a sturdy heel, and a broad gold ankle cuff.",
    "extra long almond, celadon with gold tips.", VOID, "Warm gold key making every seam glow.")
add(5, "kintsugi_obsidian", "Kintsugi Obsidian", "Mid 40s",
    "Sleek black low bun with a gold pin, confident smile.",
    KS.format(cover=COVER, glaze="High-gloss obsidian-black ceramic glaze"),
    "arm", "7-inch gold mirror-chrome peep-toe platform stilettos with a thick wide platform, a sturdy heel, and wide crossed ankle straps.",
    "extra long stiletto, black with gold tips.",
    warm_bg("warm cream ceramics gallery with mended vessels on pale plinths, a light cream wall"),
    "Warm gold key making every seam glow.")
add(6, "kintsugi_ivory", "Kintsugi Ivory Porcelain", "Early 50s",
    "Short silver tapered afro with a gold band, gentle smile.",
    KS.format(cover=COVER, glaze="High-gloss milky ivory porcelain glaze clearly different from skin"),
    "hips", "7-inch ivory glazed platform stilettos with a thick wide platform, a sturdy gold heel, and a broad gold ankle strap.",
    "extra long oval, ivory with gold tips.", VOID, "Warm gold key making every seam glow.")

# 7–9 Russian lacquer
add(7, "palekh", "Palekh", "Late 30s",
    "Long locs crowned with a gold filigree circlet, bright smile.",
    f"Full body Palekh miniature lacquer {COVER}, not latex. Deep glossy black lacquer densely filled with bright fine gold-line folk-tale scenes — firebirds, galloping troika horses, and onion-dome towers woven together by continuous gold filigree vines, the gold so dense that little plain black remains. Each belly roll carries its own gold band of scenes, with the black lacquer settling into each deep crease so the overlapping folds read clearly.",
    "arm", "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel with gold firebird detailing, and a broad ankle strap.",
    "extra long coffin, black with fine gold line.",
    warm_bg("warm gilded Russian imperial ballroom with cream and gold panels and a crystal chandelier"),
    "Warm chandelier key making the gold lines shimmer.")
add(8, "zhostovo", "Zhostovo", "Early 40s",
    "Braided crown with a small gold pin, warm smile.",
    f"Full body Zhostovo lacquer {COVER}, not latex. Deep glossy black lacquer covered in lush continuous garlands of hand-painted roses, peonies, and daisies in crimson, pink, cream, and green with luminous shaded petals, minimal plain black. A garland wraps along each belly roll, with the black lacquer settling into each deep crease so the overlapping folds read clearly. Fine gold scroll borders at the wrists and ankles.",
    "hips", "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap painted with roses.",
    "extra long almond, black with rose tips.",
    warm_bg("warm Russian imperial drawing room with cream silk walls and gilded frames, a pale cream wall"),
    "Warm chandelier key making the lacquer gleam.")
add(9, "khokhloma", "Khokhloma", "Mid 40s",
    "Silver-streaked crown braid with red ribbon, bright smile.",
    f"Full body Khokhloma lacquer {COVER}, not latex. Glossy gold lacquer base densely painted with bold black and red rowan berries, strawberries, and flowing kudrina leaf swirls. The swirls curl along each belly roll, with dark lacquer settling into each deep crease so the overlapping folds read clearly.",
    "arm", "7-inch gold lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap with red berry buckles.",
    "extra long coffin, gold with red tips.",
    warm_bg("warm Russian palace hall with cream walls, gilded mouldings, and chandeliers"),
    "Warm chandelier key making the gold lacquer glow.")

# 10–14 East Asian ceramic / lacquer
add(10, "celadon_sanggam", "Celadon Sanggam Cloud-Crane", "Mid 30s",
    "Sleek high chignon with a jade binyeo, serene smile.",
    f"Full body Goryeo celadon {COVER}, no hanbok. High-gloss jade-green celadon glaze with fine crackle, densely covered in black-and-white sanggam inlay — many cranes in flight weaving through continuous scrolling clouds, chrysanthemum sprays filling the spaces between, lotus-petal borders at the wrists and ankles. Deeper pools of green glaze collect in each crease between the belly rolls so the overlapping folds read clearly.",
    "hips", "7-inch celadon platform stilettos with a thick wide platform, a sturdy heel, and a broad ribbon-wrapped ankle strap.",
    "extra long almond, celadon with white tips.", VOID, "Cool key with warm raking light across the glaze.")
add(11, "gamji_geumni", "Gamji-geumni", "Late 40s",
    "Black hair in a low jjok-meori bun with a gold binyeo, gentle smile.",
    f"Full body gamji-geumni {COVER}, no hanbok. Glossy deep navy-indigo base, not purple, with bold dense shimmering gold ink line work — lotus-vine scrolls, cloud bands, and stacked lotus-petal borders, no plain indigo areas, no religious figures. A gold lotus-petal border runs along each belly roll, with the deep indigo settling into each crease so the overlapping folds read clearly.",
    "arm", "7-inch indigo lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap with fine gold lines.",
    "extra long almond, indigo with gold tips.",
    warm_bg("warm Joseon royal library with indigo-and-gold manuscripts and glowing paper lattice windows, a pale cream wall"),
    "Warm lamp key making the gold lines shimmer.")
add(12, "makie", "Maki-e", "Early 40s",
    "Glossy black hair in a high chignon with gold kanzashi, calm smile.",
    f"Full body maki-e lacquer {COVER}, no kimono, not latex. Deep glossy black urushi with fine sprinkled gold dust with individual particles visible, forming continuous autumn grasses, flowing water, and flying geese with crisp raised gold relief, minimal plain black. Gold-dust waves follow each belly roll, with the black urushi settling into each deep crease so the overlapping folds read clearly.",
    "hips", "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel with gold maki-e detailing, and a broad ankle strap.",
    "extra long almond, black with gold powder tips.",
    warm_bg("warm Kyoto tatami room with glowing shoji screens and a pale cream wall"),
    "Warm indoor key making the gold dust glitter.")
add(13, "cloisonne", "Cloisonné Lotus Scroll", "Late 40s",
    "Sleek black high bun with a gold hairpin, composed smile.",
    f"Full body jingtailan cloisonné enamel {COVER}, no collar band. Glossy bright turquoise enamel divided by raised gold wire cells filled with continuous lotus scrolls and twining vines in coral red, cobalt, and white. A raised gold wire border runs along each belly roll, with deeper turquoise pooling in each crease so the overlapping folds read clearly.",
    "arm", "7-inch turquoise enamel platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap outlined in gold wire.",
    "extra long stiletto, turquoise with gold tips.",
    warm_bg("warm Forbidden City palace hall with red lacquered columns and golden beams, a pale warm wall"),
    "Warm key making the gold wires glint.")
add(14, "ru_guan", "Ru-Guan Celadon", "Early 50s",
    "Short silver natural curls with a pale jade pin, serene smile.",
    f"Full body Song dynasty Ru-Guan celadon {COVER}. High-gloss deep saturated sky-blue-grey glaze clearly different from skin, with a fine dense crackle of thin dark lines and finer golden secondary crackle, soft uneven reflections, no painted motifs, not kintsugi. The glaze pools thicker and darker in each crease between the belly rolls so the overlapping folds read clearly.",
    "hips", "7-inch sky-blue crackle-glazed platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap.",
    "extra long oval, pale blue with fine crackle.", VOID, "Cool key with warm raking light across the crackle.")

# 15–17 Persian / Southeast Asian
add(15, "minakari", "Minakari Arabesque", "Late 30s",
    "Long dark waves with a thin gold headband, regal smile.",
    f"Persian minakari enamel {COVER}, no collar band. Glossy bright cobalt and turquoise enamel with fine raised gold wire outlines, filled with continuous arabesque vines, white birds, and crimson roses flowing evenly over the whole body. A gold arabesque band runs along each belly roll, with deeper cobalt pooling in each crease so the overlapping folds read clearly.",
    "arm", "7-inch cobalt enamel platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap outlined in gold.",
    "extra long stiletto, cobalt with gold tips.",
    warm_bg("warm Isfahan palace hall with cream plaster arches and golden mirror mosaic, a pale warm wall"),
    "Warm lantern key making the enamel shine.")
add(16, "sonmai", "Son Mai Lotus", "Early 40s",
    "Long straight black hair falling past the waist, gentle smile.",
    f"Full body Vietnamese son mai lacquer {COVER}, not latex. Deep glossy black and vermilion lacquer with continuous gold-leaf lotus stems and blooms, silver-leaf cranes, and crackled white eggshell mosaic clouds. A band of crackled eggshell runs along each belly roll, with the black lacquer settling into each deep crease so the overlapping folds read clearly.",
    "hips", "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap with gold-leaf lotus.",
    "extra long almond, black with eggshell-white tips.",
    warm_bg("warm Hue imperial citadel hall with red lacquered columns and golden light, a pale warm wall"),
    "Warm key making the gold leaf and eggshell glow.")
add(17, "lairodnam", "Lai Rod Nam", "Late 30s",
    "Glossy black hair in a high topknot with a small gold ornament, warm smile.",
    f"Full body Thai lai rod nam lacquer {COVER}, not latex. Deep glossy black lacquer with bright gold-leaf stencil kranok flame scrolls, lotus buds, and naga vines woven continuously together, minimal plain black, no religious figures. A gold kranok border runs along each belly roll, with the black lacquer settling into each deep crease so the overlapping folds read clearly.",
    "arm", "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel with gold-leaf kranok patterns, and a broad ankle strap.",
    "extra long curved stiletto, black with gold tips.",
    warm_bg("warm traditional Thai teak house interior with golden light and a pale warm wall"),
    "Warm key making the gold leaf blaze.")

# 18–20 Irezumi
add(18, "irezumi_phoenix_peony", "Irezumi Phoenix Peony", "Early 30s",
    "Long knotless box braids piled high with gold cuffs, confident smile.",
    f"Traditional Japanese irezumi full bodysuit {COVER}, no kimono. A blazing crimson and gold phoenix whose long tail feathers sweep across the shoulders and down both legs, vivid pink giant peonies and bright white wind bars flowing between them. A sweeping tail feather follows each belly roll, with dark sumi shading settling into each deep crease so the overlapping folds read clearly. {IREZ}",
    "hips", "7-inch crimson gold platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap.",
    "extra long stiletto, crimson with gold feather tips.", VOID, "Warm key making the colors blaze.")
add(19, "irezumi_koi_waves", "Irezumi Koi Waves", "Early 40s",
    "Sleek black high chignon with a red lacquer comb, warm smile.",
    f"Traditional Japanese irezumi full bodysuit {COVER}, no kimono. Blazing crimson and gold koi swimming in a continuous spiral around the whole body through indigo and bright white waves, vivid pink sakura petals drifting everywhere. A curling wave crest runs along each belly roll, with dark sumi shading settling into each deep crease so the overlapping folds read clearly. {IREZ}",
    "arm", "7-inch crimson gold platform stilettos with a thick wide platform, a sturdy heel, and a broad caged ankle strap.",
    "extra long coffin, crimson with gold koi-scale tips.",
    warm_bg("warm Kyoto wooden tea room with glowing shoji screens and a pale cream wall"),
    "Warm indoor key making the colors glow.")
add(20, "irezumi_dragon_clouds", "Irezumi Dragon Clouds", "Mid 40s",
    "Black hair slicked into a tight topknot, bold grin.",
    f"Traditional Japanese irezumi full bodysuit {COVER}, no kimono. A great vivid emerald and gold dragon coiling from one shoulder around the whole body and spiraling down both legs, swirling indigo storm clouds, crimson maple leaves, and bold wind bars filling every gap. The dragon's body wraps along the belly rolls, with dark sumi shading settling into each deep crease so the overlapping folds read clearly. {IREZ}",
    "hips", "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel with gold scale detailing, and a broad ankle strap.",
    "extra long coffin, emerald with gold tips.", VOID, "Warm key making the dragon scales shine.")


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
            "prompt": prompt.strip(),
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
