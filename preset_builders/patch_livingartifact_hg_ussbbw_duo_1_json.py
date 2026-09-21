# -*- coding: utf-8 -*-
r"""
patch_livingartifact_hg_ussbbw_duo_1_json.py
Living Artifact · Hourglass × USSBBW Duo — 10 duo presets (3:4)
LEFT = glamour hourglass standard, RIGHT = USSBBW standard, both darkest skin.

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_hg_ussbbw_duo_1_json.py
    python preset_builders\patch_livingartifact_hg_ussbbw_duo_1_json.py --force   (overwrite)
    python preset_builders\patch_livingartifact_hg_ussbbw_duo_1_json.py --md out.md   (also dump prompts to markdown)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · Hourglass × USSBBW Duo"
PLATFORM = "gemini"
ASPECT = "3:4"

SKIN = ("Her face, neck, hands, and all skin are THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, blue-black void "
        "complexion darker than night sky, not brown.")

HOURGLASS = ("glamour hourglass bombshell physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — an "
             "overwhelmingly enormous full bust, a waist cinched so impossibly tiny it is barely a third of the width of "
             "her hips, hips flaring to nearly twice the width of her shoulders, thighs thicker than her waist pressing "
             "together, soft full voluptuous curves everywhere. Voluptuous and curvy, not skinny, not a runway model, "
             "not a fitness model.")

USSBBW = ("USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits, around 800 pounds — an "
          "enormous soft apron belly hanging in several heavy overlapping rolls down to mid-thigh, the belly wider than "
          "the chest and projecting far forward, deep shadowed creases between each roll, not pregnant, a gigantic heavy "
          "bust resting on top of the belly, no waist at all, deep side rolls visible past the silhouette, hips wider "
          "than a normal woman's whole torso, huge thighs pressed together with deep folds, enormous soft upper arms, a "
          "very full round face with a double chin. Not curvy, not hourglass, not a plus-size model.")

POSE_HG = {
    "hips": "wide stance with a strong hip shift, both hands resting on her outer hips pushing them outward, chest and belly fully visible.",
    "arm": "wide stance with a strong hip shift, one arm extended to the side at shoulder height, the other hand on her outer hip, chest and belly fully visible.",
}
POSE_SB = "wide stance, arms held away from the torso with hands on the outer hips, so the painted belly and every roll are fully visible."

HEADER = ("Fine art body painting photography, full body shot. TWO women standing side by side facing the camera, clear "
          "space between them, no touching. Two completely different extreme body types — a glamour hourglass with an "
          "impossibly tiny waist on the left, an ultra colossal body with no waist at all on the right — do not average "
          "them, do not make them similar. Each body art strictly separate.")

BOTH = ("Both: the body painting is the only covering — no garments, no fabric, no kimono, no hanbok, no bodysuit. "
        "Underarms, inner arms, pelvis, and inner thighs fully painted.")

TAIL = ("TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. "
        "Raking side light carving the hourglass curves on the left and deep shadows between the belly rolls on the "
        "right, strong warm rim light tracing both silhouettes. 3:4 vertical 8K portrait.")


def warm_bg(place):
    return f"{place}, softly blurred, the wall directly behind them much lighter than their bodies."


def left(age, hair, art, pose, shoes, nails):
    return (f"LEFT: {SKIN} {age}, {HOURGLASS} {hair} {art} Pose: {POSE_HG[pose]} {shoes} {nails}")


def right(age, hair, art, shoes, nails):
    return (f"RIGHT: {SKIN} {age}, {USSBBW} {hair} {art} Pose: {POSE_SB} {shoes} {nails}")


def build(L, R, bg, light):
    return "\n\n".join([HEADER, L, R, BOTH, f"Background & Lighting: {bg} {light} {TAIL}"])


P = []


def add(num, slug, title, L, R, bg, light):
    P.append((f"la_hgussbbw_duo_{num:02d}_{slug}", f"LA Hourglass × USSBBW Duo {num:02d} – {title}", build(L, R, bg, light)))


# ── art snippets ─────────────────────────────────────────
def ks(glaze, roll):
    base = (f"Full body Kintsugi painted directly on bare skin from neck to ankle — {glaze} with a dense web of raised "
            "24-karat gold repair seams branching over the whole body")
    if roll:
        return base + ", the largest seams running along the crease beneath each belly roll so every fold is outlined in gold."
    return base + ", thicker seams sweeping along the curves of the bust, the tiny waist, and the wide hips."


NJ = ("Full body najeon-chilgi painted directly on bare skin from neck to ankle, not latex — deep glossy black lacquer "
      "densely inlaid with thick cut mother-of-pearl shell pieces with visible sharp edges flashing pink, green, and "
      "blue rainbow sheen, {motif}")
PALEKH = ("Full body Palekh miniature lacquer painted directly on bare skin from neck to ankle, not latex — deep glossy "
          "black lacquer densely filled with bright fine gold-line firebirds, troika horses, and onion domes woven "
          "together by continuous gold filigree vines, little plain black remaining{extra}")
IREZ = "Bold black sumi outlines with soft bokashi shading, colors bright enough to stand out against the darkest skin."

# 1
add(1, "palekh_kintsugi_celadon", "Palekh × Kintsugi Celadon",
    left("Early 30s", "Long locs crowned with a gold filigree circlet, bright smile.", PALEKH.format(extra="."),
         "hips", "8-inch black lacquer platform stilettos with gold firebird heels and crossed ankle straps.",
         "Extra long coffin nails, black with fine gold line."),
    right("Late 40s", "Short sculpted silver natural curls, calm smile.",
          ks("high-gloss celadon-green ceramic glaze with fine crackle", True),
          "7-inch gold mirror-chrome platform stilettos with a thick wide platform, a sturdy heel, and a broad gold ankle cuff.",
          "Extra long almond nails, celadon with gold tips."),
    warm_bg("Warm gilded Russian imperial ballroom with cream and gold panels and a crystal chandelier"),
    "Warm chandelier key making the gold lines shimmer and the seams glow.")
# 2
add(2, "najeon_chrysanthemum_kintsugi_ivory", "Black Najeon Chrysanthemum × Kintsugi Ivory",
    left("Late 30s", "Sleek center-parted low bun with a mother-of-pearl binyeo, confident smile.",
         NJ.format(motif="continuous chrysanthemum scrolls with butterflies flowing evenly over the whole body, no single flower centered on the chest."),
         "hips", "8-inch black lacquer multi-strap platform stiletto sandals with mother-of-pearl studs.",
         "Extra long stiletto nails, black with pearl tips."),
    right("Early 50s", "Short silver tapered afro with a gold band, gentle smile.",
          ks("high-gloss milky ivory porcelain glaze clearly different from skin", True),
          "7-inch ivory glazed platform stilettos with a thick wide platform, a sturdy gold heel, and a broad gold ankle strap.",
          "Extra long oval nails, ivory with gold tips."),
    warm_bg("Warm hanok daecheong hall with glowing golden paper lattice doors and a pale cream wall"),
    "Warm indoor key making every shell piece flash rainbow and every seam glow.")
# 3
add(3, "irezumi_phoenix_najeon_peony", "Irezumi Phoenix Peony × Black Najeon Peony",
    left("Early 30s", "Long knotless box braids piled high with gold cuffs, confident smile.",
         f"Traditional Japanese irezumi full bodysuit painted directly on bare skin from neck to ankle — a blazing crimson and gold phoenix whose long tail feathers sweep around the tiny waist and down both legs, vivid pink giant peonies and bright white wind bars flowing between them, no single motif centered on the chest. {IREZ}",
         "arm", "8-inch crimson gold platform stiletto sandals with spiral straps coiling up the calf.",
         "Extra long stiletto nails, crimson with gold feather tips."),
    right("Early 40s", "Sleek high bun with a mother-of-pearl pin, warm smile.",
          NJ.format(motif="continuous peony scrolls and cranes, darker lacquer settling into each deep crease between the belly rolls."),
          "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap with mother-of-pearl studs.",
          "Extra long almond nails, black with pearl tips."),
    warm_bg("Warm hanok daecheong hall with glowing golden paper lattice doors and a pale cream wall"),
    "Warm indoor key making the phoenix blaze and every shell piece flash rainbow.")
# 4
add(4, "celadon_sanggam_palekh", "Celadon Sanggam × Palekh",
    left("Mid 30s", "Sleek high chignon with a jade binyeo, serene smile.",
         "Full body Goryeo celadon painted directly on bare skin from neck to ankle — high-gloss jade-green celadon glaze with fine crackle, densely covered in black-and-white sanggam cranes weaving through continuous scrolling clouds and chrysanthemum sprays, no isolated circles, no single motif centered on the chest.",
         "hips", "8-inch celadon platform stiletto sandals with ribbon laces tied below the knee.",
         "Extra long almond nails, celadon with white tips."),
    right("Late 30s", "Long locs gathered high with gold cuffs, bright smile.",
          PALEKH.format(extra=", each belly roll carrying its own gold band of scenes with the black lacquer settling into each deep crease."),
          "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel with gold firebird detailing, and a broad ankle strap.",
          "Extra long coffin nails, black with fine gold line."),
    warm_bg("Warm cream ceramics gallery with pale plinths and a light cream wall"),
    "Warm key with cool fill across the glaze, making the gold lines shimmer.")
# 5
add(5, "minakari_kintsugi_obsidian", "Minakari × Kintsugi Obsidian",
    left("Late 30s", "Long dark waves with a thin gold headband, regal smile.",
         "Persian minakari enamel painted directly on bare skin from neck to ankle, no collar band — glossy bright cobalt and turquoise enamel with fine raised gold wire outlines, continuous arabesque vines, white birds, and crimson roses flowing evenly over the whole body, no single motif centered on the chest.",
         "arm", "8-inch cobalt enamel multi-strap platform stiletto sandals outlined in gold.",
         "Extra long stiletto nails, cobalt with gold tips."),
    right("Mid 40s", "Sleek black low bun with a gold pin, confident smile.",
          ks("high-gloss obsidian-black ceramic glaze", True),
          "7-inch gold mirror-chrome peep-toe platform stilettos with a thick wide platform, a sturdy heel, and wide crossed ankle straps.",
          "Extra long stiletto nails, black with gold tips."),
    warm_bg("Warm Isfahan palace hall with cream plaster arches and golden mirror mosaic, a pale warm wall"),
    "Warm lantern key making the enamel shine and every seam glow.")
# 6
add(6, "cloisonne_makie", "Cloisonné × Maki-e",
    left("Late 40s", "Sleek black high bun with a gold hairpin, composed smile.",
         "Full body jingtailan cloisonné enamel painted directly on bare skin from neck to ankle, no collar band — glossy bright turquoise enamel divided by raised gold wire cells filled with continuous lotus scrolls in coral red, cobalt, and white, no single motif centered on the chest.",
         "hips", "8-inch turquoise enamel T-strap platform stiletto sandals with raised gold wire on every strap.",
         "Extra long stiletto nails, turquoise with gold tips."),
    right("Early 40s", "Glossy black hair in a high chignon with gold kanzashi, calm smile.",
          "Full body maki-e lacquer painted directly on bare skin from neck to ankle, not latex — deep glossy black urushi with fine sprinkled gold dust forming continuous autumn grasses, flowing water, and flying geese in crisp raised gold relief, gold-dust waves following each belly roll with the black urushi settling into each deep crease.",
          "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel with gold maki-e detailing, and a broad ankle strap.",
          "Extra long almond nails, black with gold powder tips."),
    warm_bg("Warm East Asian palace hall with red lacquered columns and golden beams, a pale warm wall"),
    "Warm key making the gold wires glint and the gold dust glitter.")
# 7
add(7, "zhostovo_khokhloma", "Zhostovo × Khokhloma",
    left("Early 40s", "Braided crown with a small gold pin, warm smile.",
         "Full body Zhostovo lacquer painted directly on bare skin from neck to ankle, not latex — deep glossy black lacquer covered in lush continuous garlands of hand-painted roses, peonies, and daisies in crimson, pink, cream, and green, minimal plain black, no single flower centered on the chest.",
         "arm", "8-inch black lacquer d'Orsay platform stilettos with painted roses and gold trim.",
         "Extra long almond nails, black with rose tips."),
    right("Mid 40s", "Silver-streaked crown braid with red ribbon, bright smile.",
          "Full body Khokhloma lacquer painted directly on bare skin from neck to ankle, not latex — glossy gold lacquer base densely painted with bold black and red rowan berries, strawberries, and flowing kudrina leaf swirls curling along each belly roll, dark lacquer settling into each deep crease.",
          "7-inch gold lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap with red berry buckles.",
          "Extra long coffin nails, gold with red tips."),
    warm_bg("Warm Russian imperial drawing room with cream silk walls and gilded frames"),
    "Warm chandelier key making the lacquer gleam and the gold glow.")
# 8
add(8, "lairodnam_sonmai", "Lai Rod Nam × Son Mai",
    left("Late 30s", "Glossy black hair in a high topknot with a small gold ornament, warm smile.",
         "Full body Thai lai rod nam lacquer painted directly on bare skin from neck to ankle, not latex — deep glossy black lacquer with dense bright gold-leaf kranok flame scrolls, lotus buds, and naga vines woven continuously together, minimal plain black, no religious figures, no single motif centered on the chest.",
         "hips", "8-inch black lacquer peep-toe platform stilettos with crossed gold ankle straps and gold-leaf kranok patterns.",
         "Extra long curved stiletto nails, black with gold tips."),
    right("Early 40s", "Long straight black hair falling past the waist, gentle smile.",
          "Full body Vietnamese son mai lacquer painted directly on bare skin from neck to ankle, not latex — deep glossy vermilion and black lacquer with continuous gold-leaf lotus and silver-leaf cranes, a band of crackled white eggshell running along each belly roll with the lacquer settling into each deep crease.",
          "7-inch vermilion lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap with gold-leaf lotus.",
          "Extra long almond nails, vermilion with eggshell-white tips."),
    warm_bg("Warm traditional Thai teak house interior with golden light and a pale warm wall"),
    "Warm key making the gold leaf blaze and the eggshell glow.")
# 9
add(9, "irezumi_koi_gamji", "Irezumi Koi Waves × Gamji-geumni",
    left("Early 30s", "Sleek black high ponytail with a red cord, bright smile.",
         f"Traditional Japanese irezumi full bodysuit painted directly on bare skin from neck to ankle — blazing crimson and gold koi swimming in a continuous spiral around the whole body through white waves, vivid pink sakura petals drifting everywhere, no single motif centered on the chest. {IREZ}",
         "arm", "8-inch crimson gold caged platform stiletto sandals.",
         "Extra long coffin nails, crimson with gold koi-scale tips."),
    right("Late 40s", "Black hair in a low jjok-meori bun with a gold binyeo, gentle smile.",
          "Full body gamji-geumni painted directly on bare skin from neck to ankle — glossy deep navy-indigo base, not purple, with bold dense shimmering gold ink lotus-vine scrolls and cloud bands, no plain indigo areas, no religious figures, a gold lotus-petal border running along each belly roll with the deep indigo settling into each crease.",
          "7-inch indigo lacquer platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap with fine gold lines.",
          "Extra long almond nails, indigo with gold tips."),
    warm_bg("Warm Kyoto wooden tea room with glowing shoji screens and a pale cream wall"),
    "Warm indoor key making the koi blaze and the gold lines shimmer.")
# 10
add(10, "kintsugi_celadon_irezumi_dragon", "Kintsugi Celadon × Irezumi Dragon",
    left("Late 30s", "Sleek high bun with a jade pin, confident smile.",
         ks("high-gloss celadon-green ceramic glaze with fine crackle", False),
         "hips", "8-inch gold mirror-chrome platform stiletto sandals with gold ribbon laces tied below the knee.",
         "Extra long almond nails, celadon with gold tips."),
    right("Mid 40s", "Black hair slicked into a tight topknot, bold grin.",
          f"Traditional Japanese irezumi full bodysuit painted directly on bare skin from neck to ankle — a great vivid emerald and gold dragon coiling from one shoulder around the whole body and spiraling down both legs, indigo storm clouds and bold wind bars filling every gap, the dragon's body wrapping along the belly rolls with dark sumi shading settling into each deep crease. {IREZ}",
          "7-inch black lacquer platform stilettos with a thick wide platform, a sturdy heel with gold scale detailing, and a broad ankle strap.",
          "Extra long coffin nails, emerald with gold tips."),
    warm_bg("Warm cream ceramics gallery with mended vessels on pale plinths and a light cream wall"),
    "Warm gold key making every seam glow and the dragon scales shine.")


def main() -> int:
    force = "--force" in sys.argv
    md_path = None
    if "--md" in sys.argv:
        md_path = Path(sys.argv[sys.argv.index("--md") + 1])
    if md_path is None and not PRESETS_DIR.is_dir():
        print(f"[ERROR] presets dir not found: {PRESETS_DIR}")
        return 1
    keys = [k for k, _, _ in P]
    if len(keys) != len(set(keys)):
        print("[ERROR] duplicate keys")
        return 1

    if md_path:
        lines = ["# Glamour Hourglass × USSBBW Duo — 10 prompts\n"]
        for key, title, prompt in P:
            lines += [f"## {title}", f"`{key}`", "", "```", prompt.strip(), "```", ""]
        md_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"[MD]   {md_path}")

    if not PRESETS_DIR.is_dir():
        return 0

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
