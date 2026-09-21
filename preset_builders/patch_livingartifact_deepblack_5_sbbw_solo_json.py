# -*- coding: utf-8 -*-
r"""
patch_livingartifact_deepblack_5_sbbw_solo_json.py
Living Artifact · DeepBlack Ink — SuperBBW solos 134~163 (30 presets, 2:3)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_deepblack_5_sbbw_solo_json.py
    python preset_builders\patch_livingartifact_deepblack_5_sbbw_solo_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · DeepBlack Ink"
PLATFORM = "gemini"
ASPECT = "2:3"

SKIN = "deepest ebony skin with cool blue-black undertones"
SBBW = ("colossal SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — gigantic soft belly hanging in deep overlapping "
        "rolls, not pregnant, overwhelmingly massive heavy bust, extremely wide hips, enormous thighs, very broad soft arms")

POSE = {
    "P1": "full frontal, both hands on hips, elbows out, chest and belly fully visible.",
    "P2": "three-quarter front, one hand lifting hair at shoulder height, other hand on hip, chest and belly fully visible.",
    "P3": "three-quarter front, one arm extended to the side at shoulder height, other hand on hip, chest and belly fully visible.",
    "P4": "full frontal, hands clasped loosely behind lower back, chest forward, chest and belly fully visible.",
    "P5": "facing camera, both hands gently framing her face, elbows low, chest and belly fully visible.",
    "P6": "contrapposto, one foot on a low black block, hand on raised knee, torso upright facing camera, chest and belly fully visible.",
    "P7": "walking toward camera, arms swinging slightly away from the body, chest and belly fully visible.",
    "P8": "facing camera, both hands resting on lower belly, shoulders back, chest and belly fully visible.",
}


def solo(age, hair, motif, details, pose, shoes, nails, outline="Bold black outlines"):
    return (f"Professional fashion photograph, full body shot. ONE woman standing, {SKIN}, {age}, {SBBW}, {hair} — full "
            f"body {motif} from neck to ankle, EVERY inch covered, NO bare skin below neck. {outline} — {details}, filling "
            f"every gap, NO airbrush NO gradient wash. Pose: {POSE[pose]} {shoes}, {nails}. Extreme high-gloss oil. "
            "MANDATORY pure pitch black background only, NO backdrop NO texture NO grey NO gradient. CRITICAL: legs show "
            "FULL BODY ART hip to ankle to toe. Emphasis on the extreme SuperBBW body volume. 8K portrait 2:3 vertical.")


IREZUMI = "Bold black ink outlines"

S = [
    (134, "bear_salmon", "Grizzly Bear Salmon", "early 40s", "short tapered natural hair", "grizzly bear and salmon body art", "AMBER BROWN bear across the belly, SILVER-PINK leaping salmon on bust and both legs, TEAL river currents", "P1", "Amber teal knee-high platform stiletto boots 8 inch", "extra long coffin nails salmon pink", None),
    (135, "lynx_snowpine", "Lynx Snowy Pine", "late 20s", "silver-dyed braids", "lynx and snowy pine body art", "FROST GREY lynx with tufted ears across the bust, DEEP GREEN snow-laden pines both legs to ankle, WHITE snowflakes", "P2", "Grey white d'Orsay platform stilettos 8 inch", "extra long almond nails frost white", None),
    (136, "chameleon_jungle", "Chameleon Jungle", "mid 30s", "long rainbow-tipped braids", "chameleon and jungle body art", "SHIFTING GREEN-TURQUOISE-ORANGE chameleon curled across the belly, TROPICAL leaves and vines both legs to ankle", "P3", "Green orange caged platform stiletto sandals 8 inch", "extra long stiletto nails chameleon color-shift", None),
    (137, "macaw_rainforest", "Scarlet Macaw Rainforest", "early 20s", "big curly afro with a red feather", "scarlet macaw and rainforest body art", "SCARLET, YELLOW, and BLUE macaws across bust and belly, EMERALD rainforest leaves both legs to ankle", "P5", "Scarlet blue multi-strap platform stiletto sandals 8 inch", "extra long coffin nails macaw feather", None),
    (138, "toucan_bromeliad", "Toucan Bromeliad", "late 30s", "high puff with orange wrap", "toucan and bromeliad body art", "BLAZING ORANGE-billed toucans across the bust, HOT PINK and LIME bromeliads on belly and both legs to ankle", "P4", "Orange lime peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails toucan orange", None),
    (139, "treefrog_heliconia", "Tree Frog Heliconia", "mid 20s", "lime-green tipped twists", "red-eyed tree frog and heliconia body art", "VIVID GREEN tree frogs with RED eyes across bust and belly, CRIMSON and YELLOW heliconia claws both legs to ankle", "P6", "Green red platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long stiletto nails frog green", None),
    (140, "zebra", "Zebra Stripe", "early 50s", "platinum-white buzz cut", "zebra stripe body art", "STARK WHITE sweeping zebra stripes flowing with every curve of bust, belly rolls, hips, and both legs to ankle", "P8", "Black white striped d'Orsay platform stilettos 8 inch", "extra long coffin nails zebra stripe", None),
    (141, "giraffe", "Giraffe Patch", "late 20s", "honey-brown locs", "giraffe patch body art", "CARAMEL and CHESTNUT irregular giraffe patches separated by CREAM lines across torso and both legs to ankle", "P7", "Caramel cream caged platform stiletto sandals 8 inch", "extra long almond nails caramel patch", None),
    (142, "snowleopard", "Snow Leopard Mountain", "mid 40s", "silver sleek high bun", "snow leopard and mountain body art", "SMOKY WHITE snow leopard with charcoal rosettes across bust and belly, ICE BLUE peaks both legs to ankle", "P1", "Smoky white knee-high lace-up platform stiletto boots 8 inch", "extra long stiletto nails rosette grey", None),
    (143, "rooster_cockscomb", "Rooster Cockscomb Irezumi", "early 30s", "sleek black topknot with red cord", "rooster and cockscomb flower irezumi", "IRIDESCENT GREEN, GOLD, and CRIMSON rooster with flowing tail across bust and belly, VELVET RED cockscomb flowers both legs to ankle", "P3", "Crimson gold peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails rooster green", IREZUMI),
    (144, "nautilus", "Nautilus Golden Ratio", "late 40s", "pearl-pinned silver curls", "nautilus and golden ratio body art", "PEARL WHITE and RUST striped nautilus shell spiraling on the belly, GOLD golden-ratio arcs and rectangles across bust and both legs to ankle", "P5", "Pearl gold multi-strap platform stiletto sandals 8 inch", "extra long oval nails pearl", None),
    (145, "ammonite", "Opal Ammonite", "early 20s", "copper-tinted high puff", "opalized ammonite fossil body art", "IRIDESCENT RED-GREEN opal ammonite spirals across bust and belly, SANDSTONE fossil fern imprints both legs to ankle", "P4", "Copper opal caged platform stiletto sandals 8 inch", "extra long almond nails opal shimmer", None),
    (146, "gothicfiligree", "Gothic Filigree", "mid 30s", "sleek black long hair with a silver circlet", "gothic tracery filigree body art", "BRIGHT SILVER pointed arches, trefoils, and rose-window tracery across bust and belly, WINE RED fills and silver lattice both legs to ankle", "P2", "Silver wine knee-high platform stiletto boots 8 inch", "extra long stiletto nails silver filigree", None),
    (147, "clockwork", "Antique Clockwork", "early 40s", "brass-cuffed locs", "antique clock face body art", "CREAM enamel clock dials with ROMAN numerals and BRASS hands on bust and belly, COPPER gears and pocket-watch chains both legs to ankle", "P1", "Brass copper platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails brass", None),
    (148, "alchemy", "Alchemy Symbols", "late 20s", "violet-tinted twist-out", "alchemy symbol body art", "ANTIQUE GOLD alchemical circles, triangles, and element glyphs (no letters) across bust and belly, DEEP VIOLET star charts and CRIMSON flask diagrams both legs to ankle", "P8", "Gold violet d'Orsay platform stilettos 8 inch", "extra long almond nails alchemy gold", None),
    (149, "zodiacanimals", "Chinese Zodiac Wheel", "mid 40s", "sleek black high bun with red tassel", "Chinese zodiac animal wheel body art", "CINNABAR RED and GOLD zodiac wheel on the belly with twelve stylized animals, JADE cloud scrolls on bust and both legs to ankle", "P3", "Red gold peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long stiletto nails cinnabar", None),
    (150, "cardsuits", "Playing Card Suits", "early 30s", "red finger-wave bob", "playing card suit body art", "CRIMSON hearts and diamonds with IVORY spades and clubs in a harlequin checker across torso and both legs to ankle, GOLD card borders", "P5", "Crimson ivory caged platform stiletto sandals 8 inch", "extra long coffin nails card suits", None),
    (151, "carnivalmask", "Venetian Carnival", "late 30s", "voluminous curls with a gold feather", "Venetian carnival mask body art", "GOLD and TEAL ornate masks with feathers across bust and belly, PLUM damask and DIAMOND harlequin bands both legs to ankle", "P4", "Gold teal multi-strap platform stiletto sandals 8 inch", "extra long almond nails harlequin", None),
    (152, "popart", "Pop Art Halftone", "mid 20s", "bright yellow high puff", "pop art halftone body art", "PRIMARY RED, YELLOW, and CYAN halftone dot fields and starburst panels across torso and both legs to ankle", "P7", "Red yellow peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails halftone dot", None),
    (153, "streetart", "Street Art Bubbles", "early 20s", "magenta box braids", "street art bubble mural body art", "ELECTRIC PURPLE, LIME, and ORANGE bubble shapes, arrows, and drips (no letters) across torso and both legs to ankle, WHITE highlight dashes", "P6", "Purple lime platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long stiletto nails drip lime", None),
    (154, "goldmosaicspiral", "Gold Leaf Mosaic Spiral", "early 50s", "silver coils with gold leaf", "gold leaf mosaic spiral body art", "BLAZING GOLD leaf spirals, eyes, and rectangles with JEWEL-TONE squares of teal, coral, and violet across torso and both legs to ankle", "P1", "Gold chrome mirror platform stilettos 8 inch", "extra long almond nails gold leaf", None),
    (155, "impastonight", "Impasto Night Sky", "late 40s", "sleek black low bun", "impasto swirling night sky body art", "THICK COBALT and ULTRAMARINE swirling brushstroke sky, BLAZING YELLOW star halos across bust and belly, DARK CYPRESS flames rising both legs to ankle", "P8", "Cobalt yellow knee-high platform stiletto boots 8 inch", "extra long coffin nails swirling blue", None),
    (156, "pointillism", "Pointillist Garden", "early 30s", "long straight hair with a parasol pin", "pointillist garden body art", "thousands of tiny dots in CORAL, MINT, LAVENDER, and SUNLIT YELLOW forming flowers and dappled light across torso and both legs to ankle", "P2", "Coral mint caged platform stiletto sandals 8 inch", "extra long oval nails dotted pastel", None),
    (157, "cubist", "Cubist Facets", "mid 40s", "geometric-shaved short hair", "cubist facet body art", "OCHRE, SLATE BLUE, OLIVE, and BRICK RED fractured angular planes and overlapping guitar and bottle shapes across torso and both legs to ankle", "P4", "Ochre slate multi-strap platform stiletto sandals 8 inch", "extra long coffin nails faceted ochre", None),
    (158, "destijl", "De Stijl Grid", "late 20s", "sleek white-platinum bob", "De Stijl grid body art", "rectangles of PRIMARY RED, BLUE, YELLOW, and WHITE wrapping around torso and both legs to ankle", "P3", "Red blue d'Orsay platform stilettos 8 inch", "extra long squoval nails primary blocks", "Bold thick black grid lines"),
    (159, "circusposter", "Vintage Circus Poster", "early 40s", "pin-curled updo with a red bow clip", "vintage circus poster body art", "CIRCUS RED and CREAM tent stripes on the torso, GOLD stars and sunburst on the belly, TEAL and RED diamond borders both legs to ankle", "P5", "Red cream peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails circus stripe", None),
    (160, "uvneontube", "UV Neon Tube Sign", "mid 30s", "UV-reactive pink sleek ponytail", "UV neon tube sign body art", "ELECTRIC PINK, BLUE, and YELLOW bent glass-tube shapes — hearts, stars, palm outlines, cocktail glasses (no letters) — across torso and both legs to ankle, STARK WHITE glow halos", "P7", "Pink blue barely-there platform stilettos 8 inch", "extra long coffin nails neon tube pink", None),
    (161, "uvanglerfish", "UV Deep-Sea Anglerfish", "early 50s", "UV-reactive teal close-cropped curls", "UV deep-sea creature body art", "ELECTRIC TEAL anglerfish lure glowing on the belly, VIVID BLUE lanternfish and siphonophore chains across bust and both legs to ankle, STARK WHITE photophore dots", "P1", "Teal blue caged platform stiletto sandals 8 inch", "extra long stiletto nails glowing teal", None),
    (162, "uvhypnospiral", "UV Hypnotic Spiral", "late 20s", "UV-reactive white-violet afro", "UV hypnotic spiral body art", "ELECTRIC VIOLET and WHITE concentric spirals centered on the belly and bust, VIVID CYAN spiral arms winding down both legs to ankle", "P8", "Violet white chrome mirror platform stilettos 8 inch", "extra long almond nails spiral violet", None),
    (163, "uvjunglevine", "UV Neon Jungle Vine", "mid 40s", "UV-reactive green long locs", "UV neon jungle vine body art", "ELECTRIC GREEN and YELLOW glowing vines and monstera outlines wrapping torso and both legs, VIVID MAGENTA tropical flower blooms at bust and hips, STARK WHITE sparkle dots", "P6", "Green magenta platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails neon green", None),
]

P = []
for num, slug, title, age, hair, motif, details, pose, shoes, nails, outline in S:
    kw = {"outline": outline} if outline else {}
    P.append((f"la_deepblack_{num:03d}_solo_{slug}", f"LA DeepBlack {num:03d} Solo SBBW – {title}",
              solo(age, hair, motif, details, pose, shoes, nails, **kw)))

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
