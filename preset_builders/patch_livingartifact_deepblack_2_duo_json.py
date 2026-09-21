# -*- coding: utf-8 -*-
r"""
patch_livingartifact_deepblack_2_duo_json.py
Living Artifact · DeepBlack Ink — duos 64~83 (20 presets, 3:4)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_deepblack_2_duo_json.py
    python preset_builders\patch_livingartifact_deepblack_2_duo_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · DeepBlack Ink"
PLATFORM = "gemini"
ASPECT = "3:4"

SKIN = "deepest ebony skin with cool blue-black undertones"
X = "THE MOST EXTREME PHYSICALLY POSSIBLE"
PHYS = {
    "pear": f"pear queen physique {X} — narrow shoulders over colossal hips flaring to impossible width, enormous thighs, full bust",
    "colossal": f"colossal SuperBBW physique {X} — gigantic soft belly in deep overlapping rolls, not pregnant, overwhelmingly massive bust, extremely wide hips, enormous thighs",
    "hourglass": f"hourglass queen physique {X} — impossibly cinched waist, hips flaring beyond human proportion, enormous full bust, thick touching thighs",
    "bubble": f"bubble butt goddess physique {X} — bubble butt projecting dramatically backward, snatched waist, full high bust, powerful thighs",
    "top": f"top-heavy bombshell physique {X} — overwhelmingly colossal bust, broad soft shoulders, full belly, wide hips, thick thighs",
    "thigh": f"thick thigh temptress physique {X} — thighs massively thick pressing together, wide powerful hips, full heavy bust, snatched waist",
    "spoon": f"spoon-shape physique {X} — hips dramatically wider than the upper body, full belly, full bust, enormous thighs",
    "amazon": f"amazon physique {X} — broad powerful shoulders, enormous bust, thick strong waist, massive hips, colossal muscular thighs",
}

POSE = {
    "P1": "full frontal, both hands on hips, elbows out, shoulders back, chest and belly fully visible.",
    "P2": "three-quarter front, one hand lifting her hair at shoulder height, other hand on hip, chest and belly fully visible.",
    "P3": "three-quarter front, one arm extended to the side at shoulder height, other hand on hip, chest and belly fully visible.",
    "P4": "full frontal, hands clasped loosely behind lower back, chest forward, chest and belly fully visible.",
    "P5": "facing camera, both hands gently framing her face, elbows low, chest and belly fully visible.",
    "P6": "contrapposto, one foot on a low black block, hand on raised knee, torso upright facing camera, chest and belly fully visible.",
    "P7": "walking toward camera, arms swinging slightly away from the body, chest and belly fully visible.",
    "P8": "facing camera, both hands resting on lower belly, shoulders back, chest and belly fully visible.",
}


def fig(side, age, phys, hair, motif, details, pose, shoes, nails, outline="Bold black outlines"):
    return (f"{side}: {SKIN}, {age}, {PHYS[phys]}, {hair} — full body {motif} covering EVERY inch of skin from neck to "
            f"ankle, both legs fully covered, NO bare skin below neck. {outline} — {details}, filling every gap, NO airbrush "
            f"NO gradient wash. Pose: {POSE[pose]}\n{side}: {shoes}, {nails}.")


def duo(l, r, langs):
    return "\n\n".join([
        "Professional fashion photograph, full body shot. TWO women standing side by side, clear space between them.",
        l, r,
        "All: extreme high-gloss oil. MANDATORY pure pitch black background only, NO studio backdrop NO texture NO grey NO "
        "gradient. CRITICAL: both women's legs show FULL BODY ART coverage hip to ankle to toe. TWO completely different "
        f"body art languages — {langs} — must CLASH dramatically against the deepest ebony skin. 8K portrait 3:4 vertical.",
    ])


P = []


def add(num, slug, title, l, r, langs):
    P.append((f"la_deepblack_{num:03d}_duo_{slug}", f"LA DeepBlack {num:03d} Duo – {title}", duo(l, r, langs)))


add(64, "eagle_rose_uvneonrain", "Eagle Rose · UV Neon Rain",
    fig("LEFT", "early 40s", "colossal", "sleek black pompadour with gold pins", "American traditional eagle and rose tattoo art", "BLAZING GOLD spread-wing eagle across bust and belly, DEEP RED roses and EMERALD leaves both legs to ankle", "P1", "red gold peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long stiletto nails red with gold tips"),
    fig("RIGHT", "late 20s", "hourglass", "UV-reactive electric blue box braids", "UV neon rain body art", "ELECTRIC BLUE and MAGENTA falling rain streaks across torso and both legs, VIVID CYAN splash rings at hips and knees, STARK WHITE reflections", "P2", "blue magenta caged platform stiletto sandals 8 inch", "extra long almond nails neon rain tips"),
    "American traditional eagle rose, UV neon rain")
add(65, "swallow_anchor_kente", "Swallow Anchor · Kente",
    fig("LEFT", "mid 30s", "top", "victory-roll updo with navy scarf pin", "sailor traditional swallow and anchor tattoo art", "NAVY BLUE swallows in flight across the bust, GOLD anchors and RED rope coils on belly and both legs to ankle, WHITE stars", "P3", "navy red platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long coffin nails navy with white star"),
    fig("RIGHT", "late 40s", "amazon", "high gele-style wrapped updo in gold", "Kente weave pattern body art", "BLAZING GOLD, EMERALD, and CRIMSON woven strip blocks across torso and both legs to ankle", "P4", "gold emerald knee-high platform stiletto boots 8 inch", "extra long almond nails kente stripe tips"),
    "sailor swallow anchor, Kente weave")
add(66, "panther_jasmine_uvplasma", "Panther Jasmine · UV Plasma",
    fig("LEFT", "early 30s", "pear", "long sleek black ponytail", "panther and jasmine tattoo art", "SILVER-GREY prowling panther across belly and hip, PURE WHITE jasmine blossoms and JADE vines both legs to ankle", "P8", "silver white multi-strap platform stiletto sandals 8 inch", "extra long stiletto nails white jasmine tips"),
    fig("RIGHT", "early 20s", "colossal", "UV-reactive violet afro puffs", "UV plasma globe body art", "ELECTRIC VIOLET plasma tendrils branching from a core on the belly across torso and both legs, VIVID PINK filament tips, STARK WHITE sparks", "P1", "violet chrome mirror platform stilettos 8 inch", "extra long coffin nails plasma violet"),
    "panther jasmine, UV plasma")
add(67, "heron_reeds_adinkra", "Heron Reeds · Adinkra",
    fig("LEFT", "early 50s", "hourglass", "silver close-cropped curls", "heron and reed irezumi", "PURE WHITE herons wading across belly and thighs, OLIVE GOLD reeds rising both legs to ankle, PALE BLUE water rings", "P5", "white gold d'Orsay platform stilettos 8 inch", "extra long oval nails white with gold line", outline="Bold black ink outlines"),
    fig("RIGHT", "mid 30s", "thigh", "long twists with cowrie shells", "Adinkra symbol body art", "BLAZING GOLD Adinkra symbols in a grid across torso, TERRACOTTA and IVORY bands both legs to ankle", "P6", "gold terracotta platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails gold symbol tips"),
    "heron reed irezumi, Adinkra symbols")
add(68, "owl_oak_uvfiberoptic", "Owl Oak · UV Fiber-optic",
    fig("LEFT", "late 30s", "spoon", "copper-tinted locs in a high bun", "owl and oak tattoo art", "AMBER-EYED great horned owl across bust and belly, BRONZE oak branches and GOLD acorns both legs to ankle", "P4", "bronze amber knee-high lace-up platform stiletto boots 8 inch", "extra long almond nails bronze acorn tips"),
    fig("RIGHT", "mid 20s", "top", "UV-reactive white platinum pixie", "UV fiber-optic starburst body art", "ELECTRIC WHITE and CYAN fiber-optic bursts radiating across torso and both legs, VIVID AMBER glowing fiber tips", "P3", "white cyan caged platform stiletto sandals 8 inch", "extra long stiletto nails glowing fiber tips"),
    "owl oak, UV fiber-optic")
add(69, "bamboo_sparrow_ndebele", "Bamboo Sparrow · Ndebele",
    fig("LEFT", "late 20s", "bubble", "sleek black low bun with jade pin", "bamboo and sparrow irezumi", "JADE GREEN bamboo stalks rising both legs to ankle, WARM BROWN sparrows across bust and belly, PALE GOLD wind lines", "P2", "jade gold peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails jade tips", outline="Bold black ink outlines"),
    fig("RIGHT", "early 50s", "colossal", "silver short afro with beaded band", "Ndebele geometric body art", "BRIGHT YELLOW, COBALT, RED, and WHITE stepped geometric panels across torso and both legs to ankle", "P1", "yellow cobalt multi-strap platform stiletto sandals 8 inch", "extra long almond nails geometric color blocks"),
    "bamboo sparrow irezumi, Ndebele geometric")
add(70, "camellia_rain_uvwireframe", "Camellia Rain · UV Wireframe",
    fig("LEFT", "mid 40s", "pear", "glossy black bob with red camellia pin", "camellia and rain irezumi", "CRIMSON camellias across bust and hips, SILVER rain lines falling both legs to ankle, DARK GREEN glossy leaves", "P5", "crimson silver caged platform stiletto sandals 8 inch", "extra long stiletto nails crimson petal tips", outline="Bold black ink outlines"),
    fig("RIGHT", "early 30s", "hourglass", "UV-reactive lime sleek high ponytail", "UV hologram wireframe body art", "ELECTRIC LIME triangle mesh wireframe following every curve of torso and both legs, VIVID CYAN vertex points, STARK WHITE scan lines", "P7", "lime chrome mirror platform stilettos 8 inch", "extra long almond nails lime wireframe tips"),
    "camellia rain irezumi, UV hologram wireframe")
add(71, "moth_moon_bogolan", "Moth Moon · Bogolan",
    fig("LEFT", "late 20s", "thigh", "black finger waves", "moth and moon tattoo art", "DUSTY GOLD and CREAM large moth with patterned wings across the bust, PALE SILVER moon phases down the belly, VIOLET night flowers both legs to ankle", "P4", "gold cream d'Orsay platform stilettos 8 inch", "extra long stiletto nails moon phase tips"),
    fig("RIGHT", "early 40s", "amazon", "long braids wrapped in ochre thread", "bogolan mudcloth pattern body art", "CREAM and OCHRE mudcloth dots, crosses, and zigzag blocks across torso and both legs to ankle, RUST accents", "P3", "ochre rust platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails cream dot tips"),
    "moth moon, bogolan mudcloth")
add(72, "scorpion_desertrose_uvlava", "Scorpion Desert Rose · UV Lava",
    fig("LEFT", "mid 30s", "hourglass", "long sleek black hair with a gold chain headpiece", "scorpion and desert rose tattoo art", "BLAZING GOLD scorpion across the belly, DUSTY PINK desert roses and SAND ochre dunes both legs to ankle", "P2", "gold pink multi-strap platform stiletto sandals 8 inch", "extra long stiletto nails gold scorpion tips"),
    fig("RIGHT", "late 40s", "colossal", "UV-reactive flame-orange tapered afro", "UV molten lava crack body art", "ELECTRIC ORANGE and RED glowing lava fissures across torso and both legs, VIVID YELLOW molten cores at hips and knees", "P8", "orange red knee-high platform stiletto boots 8 inch", "extra long coffin nails lava glow tips"),
    "scorpion desert rose, UV molten lava")
add(73, "peacock_artdeco", "Peacock · Art Deco",
    fig("LEFT", "early 30s", "top", "voluminous black curls with a peacock feather clip", "peacock feather tattoo art", "IRIDESCENT TEAL and COBALT peacock eyes fanning across torso and both legs to ankle, GOLD feather barbs", "P1", "teal gold peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails peacock eye tips"),
    fig("RIGHT", "early 50s", "pear", "sleek silver finger-wave bob", "Art Deco fan geometry body art", "BLAZING GOLD sunburst fans and chevrons across torso, SILVER stepped zigzags and IVORY arcs both legs to ankle", "P5", "gold silver mirror platform stilettos 8 inch", "extra long coffin nails gold deco stripes"),
    "peacock feathers, Art Deco fans")
add(74, "hummingbird_hibiscus_uveel", "Hummingbird Hibiscus · UV Electric Eel",
    fig("LEFT", "late 30s", "spoon", "long loose curls with a red hibiscus", "hummingbird and hibiscus tattoo art", "EMERALD and RUBY hummingbirds across bust and belly, HOT RED hibiscus blooms both legs to ankle, GOLD pollen dots", "P7", "ruby emerald platform stiletto sandals with spiral straps coiling up the calf 8 inch", "extra long stiletto nails hibiscus red"),
    fig("RIGHT", "mid 20s", "thigh", "UV-reactive electric yellow twist-out", "UV electric eel body art", "ELECTRIC YELLOW eel ribbons wrapping torso and spiraling both legs, VIVID BLUE discharge arcs, STARK WHITE sparks", "P6", "yellow blue caged platform stiletto sandals 8 inch", "extra long coffin nails electric yellow"),
    "hummingbird hibiscus, UV electric eel")
add(75, "seahorse_anemone_seigaiha", "Seahorse Anemone · Seigaiha",
    fig("LEFT", "early 20s", "hourglass", "aqua-tipped long braids", "seahorse and anemone tattoo art", "CORAL ORANGE seahorses across bust and belly, VIOLET and PINK anemones both legs to ankle, AQUA bubbles", "P3", "coral aqua multi-strap platform stiletto sandals 8 inch", "extra long almond nails coral with aqua dots"),
    fig("RIGHT", "mid 40s", "colossal", "sleek black low bun with a lacquer comb", "seigaiha and asanoha Japanese pattern body art", "INDIGO and WHITE seigaiha wave scales across torso, GOLD asanoha hemp-leaf lattice both legs to ankle", "P4", "indigo gold peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails indigo wave tips"),
    "seahorse anemone, seigaiha asanoha")
add(76, "jaguar_monstera_uvfractal", "Jaguar Monstera · UV Fractal Fern",
    fig("LEFT", "early 40s", "amazon", "long locs with gold cuffs", "jaguar and monstera tattoo art", "BLAZING GOLD jaguar rosettes across torso and hips, DEEP GREEN monstera leaves both legs to ankle, AMBER eyes on the belly", "P1", "gold green knee-high lace-up platform stiletto boots 8 inch", "extra long stiletto nails jaguar spot tips"),
    fig("RIGHT", "late 20s", "pear", "UV-reactive neon green sleek bob", "UV fractal fern body art", "ELECTRIC GREEN self-similar fern fronds unfurling across torso and both legs, VIVID CYAN spiral tips, STARK WHITE micro fronds", "P2", "green cyan barely-there platform stilettos 8 inch", "extra long almond nails fractal green"),
    "jaguar monstera, UV fractal fern")
add(77, "elephant_jasmine_iznik", "Ornamental Elephant · Iznik",
    fig("LEFT", "late 40s", "colossal", "long braid wrapped in gold", "ornamental elephant tattoo art", "ROYAL PURPLE and GOLD adorned elephant across the belly, SAFFRON tassels and jewels on bust, TEAL paisley vines both legs to ankle", "P8", "purple gold caged platform stiletto sandals 8 inch", "extra long coffin nails gold jewel tips"),
    fig("RIGHT", "early 30s", "bubble", "sleek black high bun with a turquoise pin", "Iznik tulip body art", "COBALT and TURQUOISE saz leaves, BRIGHT TOMATO RED tulips and carnations across torso and both legs to ankle", "P3", "cobalt red d'Orsay platform stilettos 8 inch", "extra long almond nails tulip red"),
    "ornamental elephant, Iznik tulips")
add(78, "stag_fern_uvcymatics", "Stag Fern · UV Cymatics",
    fig("LEFT", "mid 30s", "thigh", "loose natural coils with small gold leaves", "stag and fern tattoo art", "BRONZE stag with branching antlers across bust and belly, FOREST GREEN ferns both legs to ankle, GOLD forest light", "P6", "bronze green platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long stiletto nails bronze antler tips"),
    fig("RIGHT", "early 20s", "hourglass", "UV-reactive ice-blue high puff", "UV cymatics body art", "ELECTRIC ICE BLUE and VIOLET concentric sound-vibration patterns blooming on the bust and belly, VIVID WHITE nodal lines rippling both legs to ankle", "P5", "ice blue chrome mirror platform stilettos 8 inch", "extra long almond nails glowing ice tips"),
    "stag fern, UV cymatics")
add(79, "bee_honeycomb_memphis", "Bee Honeycomb · Memphis",
    fig("LEFT", "early 50s", "top", "honey-blonde short tapered afro", "bee and honeycomb tattoo art", "BLAZING AMBER honeycomb cells across torso, GOLD and BLACK bees in flight, DRIPPING HONEY both legs to ankle", "P4", "amber gold multi-strap platform stiletto sandals 8 inch", "extra long coffin nails honeycomb tips"),
    fig("RIGHT", "late 20s", "spoon", "bubblegum-pink high ponytail", "Memphis design body art", "BRIGHT PINK, TEAL, and YELLOW squiggles, triangles, and dots across torso and both legs to ankle", "P7", "pink teal peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails Memphis squiggle tips"),
    "bee honeycomb, Memphis design")
add(80, "swan_lilypad_uvorigami", "Swan Lily Pad · UV Origami",
    fig("LEFT", "early 30s", "pear", "sleek black ballerina bun with pearl pins", "swan and lily pad tattoo art", "PURE WHITE swans with curved necks across bust and belly, JADE lily pads and BLUSH water lilies both legs to ankle, SILVER ripples", "P8", "white silver d'Orsay platform stilettos 8 inch", "extra long oval nails pearl white"),
    fig("RIGHT", "mid 40s", "colossal", "UV-reactive orange sculpted Bantu knots", "UV neon origami body art", "ELECTRIC ORANGE and CYAN folded paper facets, cranes and fold lines tessellating torso and both legs, VIVID MAGENTA crease highlights", "P1", "orange cyan caged platform stiletto sandals 8 inch", "extra long coffin nails origami fold tips"),
    "swan lily pad, UV neon origami")
add(81, "manta_tide_batik", "Manta Tide · Batik",
    fig("LEFT", "late 30s", "hourglass", "long wavy black hair swept to one side", "manta ray and tide tattoo art", "DEEP TEAL manta ray with wings spanning the bust, OCEAN BLUE tidal swirls down the belly and both legs to ankle, WHITE foam", "P2", "teal blue platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long stiletto nails ocean blue"),
    fig("RIGHT", "early 20s", "amazon", "high wrapped updo in brown batik-toned band", "Javanese batik parang body art", "SOGA BROWN, INDIGO, and CREAM diagonal parang blades across torso and both legs to ankle", "P6", "brown indigo platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails batik line tips"),
    "manta tide, batik parang")
add(82, "whale_starsea_uvgeode", "Whale Starry Sea · UV Crystal Geode",
    fig("LEFT", "mid 50s", "colossal", "silver locs in a high crown", "whale and starry sea tattoo art", "MIDNIGHT BLUE humpback whale across the belly, SILVER star field on the bust, TEAL waves both legs to ankle", "P8", "midnight silver knee-high platform stiletto boots 8 inch", "extra long almond nails starry blue"),
    fig("RIGHT", "early 30s", "thigh", "UV-reactive amethyst purple coils", "UV crystal geode body art", "ELECTRIC AMETHYST and CITRINE crystal facets clustered across bust and belly, VIVID AQUA quartz points both legs to ankle", "P3", "amethyst chrome mirror platform stilettos 8 inch", "extra long stiletto nails crystal facet tips"),
    "whale starry sea, UV crystal geode")
add(83, "flamingo_palm_opart", "Flamingo Palm · Op-art",
    fig("LEFT", "late 20s", "spoon", "big curly hair with a pink flower", "flamingo and palm tattoo art", "HOT PINK flamingos across bust and belly, EMERALD palm fronds both legs to ankle, SUNSET ORANGE sky bands", "P7", "pink emerald platform stiletto sandals with spiral straps coiling up the calf 8 inch", "extra long coffin nails flamingo pink"),
    fig("RIGHT", "early 40s", "top", "sleek white-platinum buzz cut", "op-art moiré body art", "STARK WHITE warped concentric stripes bending around bust and belly, BLACK-AND-WHITE optical wave bands both legs to ankle", "P1", "black white striped peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails op-art stripe tips"),
    "flamingo palm, op-art moiré")

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
