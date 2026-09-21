# -*- coding: utf-8 -*-
r"""
patch_livingartifact_hg_ussbbw_duo_2_json.py
Living Artifact · Hourglass × USSBBW Duo — duos 11~30 (20 presets, 3:4)
LEFT = glamour hourglass standard, RIGHT = USSBBW standard, both darkest skin.
Material library: each material has an hourglass version (even whole-body flow) and a USSBBW version (roll-following).

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_hg_ussbbw_duo_2_json.py
    python preset_builders\patch_livingartifact_hg_ussbbw_duo_2_json.py --force   (overwrite)
    python preset_builders\patch_livingartifact_hg_ussbbw_duo_2_json.py --md out.md   (also dump prompts)
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

EVEN = "flowing evenly over the whole body, no single motif centered on the chest."
ROLL = "following each belly roll, with {dark} settling into each deep crease so the overlapping folds read clearly."
IREZ = "Bold black sumi outlines with soft bokashi shading, colors bright enough to stand out against the darkest skin."
PAINT = "painted directly on bare skin from neck to ankle"


def hg_shoe(desc):
    return f"8-inch {desc}."


def sb_shoe(color, detail):
    return f"7-inch {color} platform stilettos with a thick wide platform, a sturdy heel, and a broad ankle strap {detail}."


# ── material library ─────────────────────────────────────
# each: name, hg art, sb art, hg shoe, sb shoe, nails
def irez(motif_hg, motif_sb):
    return (f"Traditional Japanese irezumi full bodysuit {PAINT} — {motif_hg}, {EVEN} {IREZ}",
            f"Traditional Japanese irezumi full bodysuit {PAINT} — {motif_sb}, the design wrapping along each belly roll with dark sumi shading settling into each deep crease. {IREZ}")


def ks(glaze):
    base = f"Full body Kintsugi {PAINT} — {glaze} with a dense web of raised 24-karat gold repair seams branching over the whole body"
    return (base + ", thicker seams sweeping along the curves of the bust, the tiny waist, and the wide hips.",
            base + ", the largest seams running along the crease beneath each belly roll so every fold is outlined in gold.")


NJ_SHELL = "densely inlaid with thick cut mother-of-pearl shell pieces with visible sharp edges flashing pink, green, and blue rainbow sheen"

M = {
    "najeon_black_peony": ("Black Najeon Peony",
        f"Full body najeon-chilgi {PAINT}, not latex — deep glossy black lacquer {NJ_SHELL}, continuous peony scrolls with cranes and butterflies {EVEN}",
        f"Full body najeon-chilgi {PAINT}, not latex — deep glossy black lacquer {NJ_SHELL}, continuous peony scrolls and cranes {ROLL.format(dark='darker lacquer')}",
        hg_shoe("black lacquer multi-strap platform stiletto sandals with mother-of-pearl studs"),
        sb_shoe("black lacquer", "with mother-of-pearl studs"), "black with pearl tips"),
    "najeon_black_chrys": ("Black Najeon Chrysanthemum",
        f"Full body najeon-chilgi {PAINT}, not latex — deep glossy black lacquer {NJ_SHELL}, continuous chrysanthemum scrolls with butterflies {EVEN}",
        f"Full body najeon-chilgi {PAINT}, not latex — deep glossy black lacquer {NJ_SHELL}, continuous chrysanthemum scrolls and small birds {ROLL.format(dark='darker lacquer')}",
        hg_shoe("black lacquer caged platform stiletto sandals with mother-of-pearl accents"),
        sb_shoe("black lacquer", "inlaid with shell"), "black with pearl tips"),
    "najeon_vermilion": ("Vermilion Najeon",
        f"Full body najeon-chilgi {PAINT}, not latex — deep glossy vermilion lacquer clearly different from skin, {NJ_SHELL}, peonies, scrolling vines, and butterflies {EVEN}",
        f"Full body najeon-chilgi {PAINT}, not latex — deep glossy vermilion lacquer clearly different from skin, {NJ_SHELL}, peonies and vines {ROLL.format(dark='deeper red lacquer')}",
        hg_shoe("vermilion lacquer peep-toe platform stilettos with crossed ankle straps and mother-of-pearl heels"),
        sb_shoe("vermilion lacquer", "with mother-of-pearl studs"), "vermilion with pearl tips"),
    "kintsugi_celadon": ("Kintsugi Celadon",
        *ks("high-gloss celadon-green ceramic glaze with fine crackle"),
        hg_shoe("gold mirror-chrome platform stiletto sandals with gold ribbon laces tied below the knee"),
        sb_shoe("gold mirror-chrome", "shaped as a broad gold cuff"), "celadon with gold tips"),
    "kintsugi_obsidian": ("Kintsugi Obsidian",
        *ks("high-gloss obsidian-black ceramic glaze"),
        hg_shoe("gold mirror-chrome peep-toe platform stilettos with crossed ankle straps"),
        sb_shoe("gold mirror-chrome", "with wide crossed gold straps"), "black with gold tips"),
    "kintsugi_ivory": ("Kintsugi Ivory",
        *ks("high-gloss milky ivory porcelain glaze clearly different from skin"),
        hg_shoe("ivory glazed platform stilettos with gold heels and a gold ankle strap"),
        sb_shoe("ivory glazed", "in gold"), "ivory with gold tips"),
    "celadon": ("Celadon Sanggam",
        f"Full body Goryeo celadon {PAINT} — high-gloss jade-green celadon glaze with fine crackle, densely covered in black-and-white sanggam cranes weaving through continuous scrolling clouds and chrysanthemum sprays, no isolated circles, {EVEN}",
        f"Full body Goryeo celadon {PAINT} — high-gloss jade-green celadon glaze with fine crackle, densely covered in black-and-white sanggam cranes and continuous clouds, {ROLL.format(dark='deeper pools of green glaze')}",
        hg_shoe("celadon platform stiletto sandals with ribbon laces tied below the knee"),
        sb_shoe("celadon", "wrapped in celadon ribbon"), "celadon with white tips"),
    "ruguan": ("Ru-Guan Celadon",
        f"Full body Song dynasty Ru-Guan celadon {PAINT} — high-gloss deep saturated sky-blue-grey glaze clearly different from skin, fine dense crackle of thin dark lines and golden secondary crackle, no painted motifs, not kintsugi, the crackle spreading evenly over the whole body.",
        f"Full body Song dynasty Ru-Guan celadon {PAINT} — high-gloss deep saturated sky-blue-grey glaze clearly different from skin, fine dense crackle of thin dark lines, no painted motifs, not kintsugi, the glaze pooling thicker and darker in each crease between the belly rolls so the overlapping folds read clearly.",
        hg_shoe("sky-blue crackle-glazed caged platform stiletto sandals"),
        sb_shoe("sky-blue crackle-glazed", "in pale blue"), "pale blue with fine crackle"),
    "gamji": ("Gamji-geumni",
        f"Full body gamji-geumni {PAINT} — glossy deep navy-indigo base, not purple, with bold dense shimmering gold ink lotus-vine scrolls and cloud bands, no plain indigo areas, no religious figures, {EVEN}",
        f"Full body gamji-geumni {PAINT} — glossy deep navy-indigo base, not purple, with bold dense gold ink lotus-vine scrolls, no religious figures, a gold lotus-petal border {ROLL.format(dark='the deep indigo')}",
        hg_shoe("indigo lacquer T-strap platform stiletto sandals with fine gold lines"),
        sb_shoe("indigo lacquer", "with fine gold lines"), "indigo with gold tips"),
    "makie": ("Maki-e",
        f"Full body maki-e lacquer {PAINT}, not latex — deep glossy black urushi with fine sprinkled gold dust forming continuous autumn grasses, flowing water, and flying geese in crisp raised gold relief, {EVEN}",
        f"Full body maki-e lacquer {PAINT}, not latex — deep glossy black urushi with fine sprinkled gold dust forming continuous waves and plovers in crisp raised gold relief, gold-dust waves {ROLL.format(dark='the black urushi')}",
        hg_shoe("black lacquer platform stiletto sandals with gold maki-e detailing and ribbon laces tied below the knee"),
        sb_shoe("black lacquer", "with gold maki-e detailing"), "black with gold powder tips"),
    "cloisonne": ("Cloisonné",
        f"Full body jingtailan cloisonné enamel {PAINT}, no collar band — glossy bright turquoise enamel divided by raised gold wire cells filled with continuous lotus scrolls in coral red, cobalt, and white, {EVEN}",
        f"Full body jingtailan cloisonné enamel {PAINT}, no collar band — glossy bright turquoise enamel with raised gold wire cells and continuous lotus scrolls, a raised gold wire border {ROLL.format(dark='deeper turquoise')}",
        hg_shoe("turquoise enamel T-strap platform stiletto sandals with raised gold wire on every strap"),
        sb_shoe("turquoise enamel", "outlined in gold wire"), "turquoise with gold tips"),
    "minakari": ("Minakari",
        f"Persian minakari enamel {PAINT}, no collar band — glossy bright cobalt and turquoise enamel with fine raised gold wire outlines, continuous arabesque vines, white birds, and crimson roses {EVEN}",
        f"Persian minakari enamel {PAINT}, no collar band — glossy bright cobalt and turquoise enamel with fine gold wire outlines and continuous arabesque vines, a gold arabesque band {ROLL.format(dark='deeper cobalt')}",
        hg_shoe("cobalt enamel multi-strap platform stiletto sandals outlined in gold"),
        sb_shoe("cobalt enamel", "outlined in gold"), "cobalt with gold tips"),
    "palekh": ("Palekh",
        f"Full body Palekh miniature lacquer {PAINT}, not latex — deep glossy black lacquer densely filled with bright fine gold-line firebirds, troika horses, and onion domes woven together by continuous gold filigree vines, little plain black remaining, {EVEN}",
        f"Full body Palekh miniature lacquer {PAINT}, not latex — deep glossy black lacquer densely filled with bright fine gold-line folk-tale scenes, each belly roll carrying its own gold band of scenes, {ROLL.format(dark='the black lacquer')}",
        hg_shoe("black lacquer platform stilettos with gold firebird heels and crossed ankle straps"),
        sb_shoe("black lacquer", "with gold firebird detailing"), "black with fine gold line"),
    "zhostovo": ("Zhostovo",
        f"Full body Zhostovo lacquer {PAINT}, not latex — deep glossy black lacquer covered in lush continuous garlands of hand-painted roses, peonies, and daisies in crimson, pink, cream, and green, minimal plain black, {EVEN}",
        f"Full body Zhostovo lacquer {PAINT}, not latex — deep glossy black lacquer with lush hand-painted rose and peony garlands, a garland {ROLL.format(dark='the black lacquer')}",
        hg_shoe("black lacquer d'Orsay platform stilettos with painted roses and gold trim"),
        sb_shoe("black lacquer", "painted with roses"), "black with rose tips"),
    "khokhloma": ("Khokhloma",
        f"Full body Khokhloma lacquer {PAINT}, not latex — glossy gold lacquer base densely painted with bold black and red rowan berries, strawberries, and flowing kudrina leaf swirls {EVEN}",
        f"Full body Khokhloma lacquer {PAINT}, not latex — glossy gold lacquer base with bold black and red berries and kudrina swirls curling {ROLL.format(dark='dark lacquer')}",
        hg_shoe("gold lacquer platform stiletto sandals with red berry buckles and spiral straps coiling up the calf"),
        sb_shoe("gold lacquer", "with red berry buckles"), "gold with red tips"),
    "lairodnam": ("Lai Rod Nam",
        f"Full body Thai lai rod nam lacquer {PAINT}, not latex — deep glossy black lacquer with dense bright gold-leaf kranok flame scrolls, lotus buds, and naga vines woven continuously together, no religious figures, {EVEN}",
        f"Full body Thai lai rod nam lacquer {PAINT}, not latex — deep glossy black lacquer with dense gold-leaf kranok scrolls, no religious figures, a gold kranok border {ROLL.format(dark='the black lacquer')}",
        hg_shoe("black lacquer peep-toe platform stilettos with crossed gold ankle straps and gold-leaf kranok patterns"),
        sb_shoe("black lacquer", "with gold-leaf kranok patterns"), "black with gold tips"),
    "sonmai": ("Son Mai",
        f"Full body Vietnamese son mai lacquer {PAINT}, not latex — deep glossy vermilion and black lacquer with continuous gold-leaf lotus, silver-leaf cranes, and crackled white eggshell mosaic clouds {EVEN}",
        f"Full body Vietnamese son mai lacquer {PAINT}, not latex — deep glossy vermilion and black lacquer with gold-leaf lotus, a band of crackled white eggshell {ROLL.format(dark='the lacquer')}",
        hg_shoe("vermilion lacquer caged platform stiletto sandals with gold-leaf lotus accents"),
        sb_shoe("vermilion lacquer", "with gold-leaf lotus"), "vermilion with eggshell-white tips"),
    "irez_tiger": ("Irezumi Tiger Bamboo",
        *irez("a blazing amber and orange striped tiger stalking across the shoulders with its tail curling around the tiny waist, vivid jade bamboo groves rising along both legs, bold white wind bars",
              "a blazing amber and orange striped tiger stalking across the bust and belly, vivid jade bamboo along both legs, bold white wind bars"),
        hg_shoe("black lacquer peep-toe platform stilettos with amber-striped crossed ankle straps"),
        sb_shoe("black lacquer", "striped in amber"), "amber with black stripe"),
    "irez_crane_plum": ("Irezumi Crane Plum",
        *irez("a storm of crimson plum blossoms on deep indigo branches, a pair of golden cranes soaring from the shoulders down both legs, white petals scattering",
              "crimson plum blossoms on deep indigo branches and a pair of golden cranes soaring across the belly, white petals scattering"),
        hg_shoe("crimson gold multi-strap platform stiletto sandals"),
        sb_shoe("crimson lacquer", "in gold"), "crimson plum tips"),
    "irez_koi": ("Irezumi Koi Waves",
        *irez("blazing crimson and gold koi swimming in a continuous spiral around the whole body through white waves, vivid pink sakura petals drifting everywhere",
              "blazing crimson and gold koi swimming through white waves, a curling wave crest along each belly roll, vivid pink sakura petals drifting"),
        hg_shoe("crimson gold caged platform stiletto sandals"),
        sb_shoe("crimson lacquer", "caged in gold"), "crimson with gold koi-scale tips"),
    "irez_phoenix": ("Irezumi Phoenix Peony",
        *irez("a blazing crimson and gold phoenix whose long tail feathers sweep around the tiny waist and down both legs, vivid pink giant peonies and bright white wind bars",
              "a blazing crimson and gold phoenix with a sweeping tail feather along each belly roll, vivid pink giant peonies and bright white wind bars"),
        hg_shoe("crimson gold platform stiletto sandals with spiral straps coiling up the calf"),
        sb_shoe("crimson gold", "with gold feather detailing"), "crimson with gold feather tips"),
    "irez_chrys_water": ("Irezumi Chrysanthemum Water",
        *irez("giant golden chrysanthemums floating on continuous flowing indigo water from the shoulders around the tiny waist and down both legs, bold white wind bars",
              "giant golden chrysanthemums floating on flowing indigo water, a water current along each belly roll, bold white wind bars"),
        hg_shoe("gold emerald caged platform stiletto sandals"),
        sb_shoe("gold lacquer", "with emerald accents"), "gold chrysanthemum tips"),
    "irez_hannya": ("Irezumi Hannya Maple",
        *irez("a white hannya mask with crimson horns on the shoulder, swirling scarlet maple leaves flowing around the tiny waist and down both legs, dark clouds and bold wind bars",
              "a white hannya mask on the upper belly, swirling scarlet maple leaves across every roll, dark clouds and bold wind bars"),
        hg_shoe("black lacquer multi-strap platform stiletto sandals with scarlet maple details"),
        sb_shoe("black lacquer", "with scarlet maple details"), "scarlet with gold tips"),
}


def warm_bg(place):
    return f"Background & Lighting: {place}, softly blurred, the wall directly behind them much lighter than their bodies."


BG = {
    "hanok": warm_bg("Warm hanok daecheong hall with glowing golden paper lattice doors and a pale cream wall"),
    "palace_kr": warm_bg("Warm Joseon palace hall with red lacquered columns and glowing golden paper windows, a pale cream wall"),
    "library": warm_bg("Warm Joseon royal library with indigo-and-gold manuscripts and glowing paper lattice windows, a pale cream wall"),
    "kyoto": warm_bg("Warm Kyoto wooden tea room with glowing shoji screens and a pale cream wall"),
    "gallery": warm_bg("Warm cream ceramics gallery with pale plinths and a light cream wall"),
    "ballroom": warm_bg("Warm gilded Russian imperial ballroom with cream and gold panels and a crystal chandelier"),
    "drawing": warm_bg("Warm Russian imperial drawing room with cream silk walls and gilded frames"),
    "isfahan": warm_bg("Warm Isfahan palace hall with cream plaster arches and golden mirror mosaic, a pale warm wall"),
    "forbidden": warm_bg("Warm Forbidden City palace hall with red lacquered columns and golden beams, a pale warm wall"),
    "teak": warm_bg("Warm traditional Thai teak house interior with golden light and a pale warm wall"),
    "hue": warm_bg("Warm Hue imperial citadel hall with red lacquered columns and golden light, a pale warm wall"),
}

# (num, hg_mat, hg_age, hg_hair, hg_pose, sb_mat, sb_age, sb_hair, bg)
PAIRS = [
    (11, "najeon_vermilion", "Early 30s", "Black hair in a sleek high bun with a coral binyeo, bright smile.", "hips",
         "kintsugi_obsidian", "Mid 40s", "Sleek black low bun with a gold pin, confident smile.", "hanok"),
    (12, "irez_tiger", "Mid 30s", "Long black hair in a high ponytail, fierce smile.", "arm",
         "zhostovo", "Early 40s", "Braided crown with a small gold pin, warm smile.", "drawing"),
    (13, "ruguan", "Early 40s", "Short silver natural curls with a pale jade pin, serene smile.", "hips",
         "lairodnam", "Late 30s", "Glossy black hair in a high topknot with a small gold ornament, warm smile.", "teak"),
    (14, "gamji", "Late 30s", "Black hair in a low jjok-meori bun with a gold binyeo, gentle smile.", "arm",
         "kintsugi_ivory", "Early 50s", "Short silver tapered afro with a gold band, gentle smile.", "library"),
    (15, "makie", "Early 30s", "Glossy black hair in a high chignon with gold kanzashi, calm smile.", "hips",
         "celadon", "Late 40s", "Sleek high chignon with a jade binyeo, serene smile.", "kyoto"),
    (16, "khokhloma", "Late 30s", "Silver-streaked crown braid with red ribbon, bright smile.", "arm",
         "minakari", "Mid 40s", "Long dark waves with a thin gold headband, regal smile.", "isfahan"),
    (17, "sonmai", "Early 40s", "Long straight black hair falling past the waist, gentle smile.", "hips",
         "cloisonne", "Late 40s", "Sleek black high bun with a gold hairpin, composed smile.", "hue"),
    (18, "irez_crane_plum", "Early 30s", "Long knotless box braids piled high with gold cuffs, confident smile.", "arm",
         "palekh", "Late 30s", "Long locs crowned with a gold filigree circlet, bright smile.", "ballroom"),
    (19, "kintsugi_ivory", "Mid 30s", "Sleek high bun with a gold pin, calm smile.", "hips",
         "irez_koi", "Early 40s", "Sleek black high chignon with a red lacquer comb, warm smile.", "kyoto"),
    (20, "zhostovo", "Early 40s", "Honey-toned braided crown with a small gold pin, warm smile.", "arm",
         "ruguan", "Early 50s", "Short silver natural curls with a pale jade pin, serene smile.", "gallery"),
    (21, "minakari", "Late 30s", "Long dark waves with a thin gold headband, regal smile.", "hips",
         "najeon_black_chrys", "Late 40s", "Silver-streaked low bun with a mother-of-pearl binyeo, calm smile.", "hanok"),
    (22, "celadon", "Mid 30s", "Sleek high chignon with a jade binyeo, serene smile.", "arm",
         "irez_phoenix", "Early 40s", "Long box braids piled high with gold cuffs, bright smile.", "hanok"),
    (23, "palekh", "Early 30s", "Long locs crowned with a gold filigree circlet, bright smile.", "hips",
         "cloisonne", "Mid 40s", "Sleek black high bun with a gold hairpin, composed smile.", "ballroom"),
    (24, "lairodnam", "Late 30s", "Glossy black hair in a high topknot with a small gold ornament, warm smile.", "arm",
         "kintsugi_celadon", "Late 40s", "Short sculpted silver natural curls, calm smile.", "teak"),
    (25, "irez_chrys_water", "Early 40s", "Glossy black blunt collarbone-length bob, confident smile.", "hips",
         "gamji", "Late 40s", "Black hair in a low jjok-meori bun with a gold binyeo, gentle smile.", "library"),
    (26, "cloisonne", "Late 30s", "Sleek black high bun with a gold hairpin, composed smile.", "arm",
         "khokhloma", "Mid 40s", "Silver-streaked crown braid with red ribbon, bright smile.", "forbidden"),
    (27, "najeon_black_peony", "Early 30s", "Sleek center-parted low bun with a mother-of-pearl binyeo, confident smile.", "hips",
         "minakari", "Late 40s", "Long silver-streaked waves with a thin gold headband, dignified smile.", "palace_kr"),
    (28, "kintsugi_celadon", "Mid 30s", "Sleek high bun with a jade pin, confident smile.", "arm",
         "sonmai", "Early 40s", "Long straight black hair falling past the waist, gentle smile.", "hue"),
    (29, "irez_hannya", "Late 30s", "Glossy black hair in a sleek chignon with a gold hairpin, composed smile.", "hips",
         "ruguan", "Mid 40s", "Short silver natural curls with a pale jade pin, serene smile.", "kyoto"),
    (30, "makie", "Early 40s", "Glossy black hair in a high chignon with gold kanzashi, calm smile.", "arm",
         "cloisonne", "Late 40s", "Sleek black high bun with a gold hairpin, composed smile.", "forbidden"),
]


def build(hg, hg_age, hg_hair, hg_pose, sb, sb_age, sb_hair, bg):
    hn, hg_art, _, hg_shoe_, _, hg_nails = M[hg]
    sn, _, sb_art, _, sb_shoe_, sb_nails = M[sb]
    L = (f"LEFT: {SKIN} {hg_age}, {HOURGLASS} {hg_hair} {hg_art} Pose: {POSE_HG[hg_pose]} "
         f"{hg_shoe_} Extra long stiletto nails, {hg_nails}.")
    R = (f"RIGHT: {SKIN} {sb_age}, {USSBBW} {sb_hair} {sb_art} Pose: {POSE_SB} "
         f"{sb_shoe_} Extra long almond nails, {sb_nails}.")
    return "\n\n".join([HEADER, L, R, BOTH, f"{BG[bg]} Warm indoor key making both materials shine. {TAIL}"]), hn, sn


def slug(s):
    return s.replace("_", "")


P = []
for num, hg, ha, hh, hp, sb, sa, sh, bg in PAIRS:
    prompt, hn, sn = build(hg, ha, hh, hp, sb, sa, sh, bg)
    P.append((f"la_hgussbbw_duo_{num:02d}_{slug(hg)}_{slug(sb)}",
              f"LA Hourglass × USSBBW Duo {num:02d} – {hn} × {sn}", prompt))


def main() -> int:
    force = "--force" in sys.argv
    md_path = Path(sys.argv[sys.argv.index("--md") + 1]) if "--md" in sys.argv else None
    keys = [k for k, _, _ in P]
    if len(keys) != len(set(keys)):
        print("[ERROR] duplicate keys")
        return 1

    if md_path:
        lines = ["# Glamour Hourglass × USSBBW Duo — 11~30\n"]
        for key, title, prompt in P:
            lines += [f"## {title}", f"`{key}`", "", "```", prompt.strip(), "```", ""]
        md_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"[MD]   {md_path}")

    if not PRESETS_DIR.is_dir():
        if md_path:
            return 0
        print(f"[ERROR] presets dir not found: {PRESETS_DIR}")
        return 1

    written, skipped = 0, 0
    for key, title, prompt in P:
        path = PRESETS_DIR / f"{key}.json"
        if path.exists() and not force:
            print(f"[SKIP] exists: {path.name}")
            skipped += 1
            continue
        data = {"title": title, "category": CATEGORY, "platform": PLATFORM,
                "aspect_ratio": ASPECT, "prompt": prompt.strip()}
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        check = json.loads(path.read_text(encoding="utf-8-sig"))
        assert check["prompt"] and check["aspect_ratio"] == ASPECT
        print(f"[OK]   {path.name}")
        written += 1

    print(f"\nDone. written={written} skipped={skipped} total={len(P)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
