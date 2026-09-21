# -*- coding: utf-8 -*-
r"""
patch_livingartifact_deepblack_3_solo_json.py
Living Artifact · DeepBlack Ink — solos 84~103 (20 presets, 2:3)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_deepblack_3_solo_json.py
    python preset_builders\patch_livingartifact_deepblack_3_solo_json.py --force   (overwrite)
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


def solo(age, phys, hair, motif, details, pose, shoes, nails, name, outline="Bold black outlines"):
    return "\n".join([
        f"Professional fashion photograph, full body shot. ONE woman standing, {SKIN}, {age}, {PHYS[phys]}, {hair} — "
        f"full body {motif} from neck to ankle, EVERY inch covered, NO bare skin below neck. {outline} — {details}, "
        f"filling every gap, NO airbrush NO gradient wash. Pose: {POSE[pose]}",
        f"Footwear: {shoes}. Nails: {nails}.",
        "Extreme high-gloss oil. MANDATORY pure pitch black background only, NO studio backdrop NO texture NO grey NO "
        f"gradient. CRITICAL: legs show FULL BODY ART coverage hip to ankle to toe. {name} must BLAZE against the deepest "
        "ebony skin. Emphasis on the extreme body volume. 8K portrait 2:3 vertical.",
    ])


P = []


def add(num, slug, title, *args, **kw):
    P.append((f"la_deepblack_{num:03d}_solo_{slug}", f"LA DeepBlack {num:03d} Solo – {title}", solo(*args, **kw)))


add(84, "hawk_cherry", "Hawk Cherry Irezumi", "early 30s", "colossal", "sleek black high bun with gold pin", "hawk and cherry blossom irezumi",
    "BRONZE hawk diving across bust and belly, SOFT PINK cherry blossoms both legs to ankle, GOLD wind bars", "P1",
    "bronze pink caged platform stiletto sandals 8 inch", "extra long stiletto nails, pink with gold tips", "Hawk cherry irezumi", outline="Bold black ink outlines")
add(85, "fortunebat_moon", "Fortune Bat Moon", "late 40s", "hourglass", "silver-streaked sleek bob", "fortune bat and crescent moon body art",
    "CINNABAR RED fortune bats circling the bust, PALE GOLD crescent moons down the belly, JADE cloud scrolls both legs to ankle", "P2",
    "red jade peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails, cinnabar red with gold moon", "Fortune bat moon art")
add(86, "horse_wildflower", "Horse Wildflower", "mid 20s", "pear", "long flowing curls", "wild horse and wildflower tattoo art",
    "CHESTNUT and WHITE galloping horses across the belly, VIOLET, YELLOW, and CORAL wildflowers both legs to ankle, GOLD grass", "P7",
    "chestnut gold platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails, wildflower multicolor", "Horse wildflower art")
add(87, "cheetah_savanna", "Cheetah Savanna", "early 40s", "amazon", "golden-brown locs in a high crown", "cheetah and savanna tattoo art",
    "BLAZING GOLD cheetah spots flowing across torso and hips, AMBER sunset acacia silhouettes on the belly, OCHRE grass both legs to ankle", "P3",
    "gold ochre knee-high lace-up platform stiletto boots 8 inch", "extra long stiletto nails, cheetah spot gold", "Cheetah savanna art")
add(88, "hydrangea_rain", "Hydrangea Rain Irezumi", "late 30s", "colossal", "black finger-wave bob", "hydrangea and rain irezumi",
    "PERIWINKLE and LILAC hydrangea clusters across bust and belly, SILVER raindrops and small snails both legs to ankle, SAGE leaves", "P5",
    "lilac silver d'Orsay platform stilettos 8 inch", "extra long oval nails, periwinkle", "Hydrangea rain irezumi", outline="Bold black ink outlines")
add(89, "thistle_songbird", "Thistle Songbird", "early 20s", "top", "auburn-tinted twist-out", "thistle and songbird tattoo art",
    "DEEP PURPLE thistles across bust and hips, GOLDFINCH YELLOW and ROBIN RED songbirds on the belly, SILVER-GREEN thorny stems both legs to ankle", "P4",
    "purple gold multi-strap platform stiletto sandals 8 inch", "extra long coffin nails, purple with yellow bird", "Thistle songbird art")
add(90, "ikat", "Ikat", "mid 30s", "spoon", "long box braids tied high", "Central Asian ikat body art",
    "FUCHSIA, SAFFRON, and TEAL blurred-edge ikat diamonds and pomegranate shapes across torso and both legs to ankle", "P6",
    "fuchsia teal platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long almond nails, ikat pattern", "Ikat art")
add(91, "hmong_embroidery", "Hmong Embroidery", "early 50s", "thigh", "silver high bun with a beaded pin", "Hmong embroidery pattern body art",
    "HOT PINK, EMERALD, and INDIGO cross-stitch spirals, snail-shell and star motifs across torso and both legs to ankle, SILVER dots", "P8",
    "pink indigo caged platform stiletto sandals 8 inch", "extra long stiletto nails, cross-stitch pink", "Hmong embroidery art")
add(92, "zellige_star", "Zellige Star", "late 20s", "hourglass", "long sleek hair with a gold chain headpiece", "Moroccan zellige star body art",
    "EMERALD, COBALT, and SAFFRON eight-point star tessellations across torso and both legs to ankle, WHITE interlace bands", "P2",
    "emerald cobalt peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails, emerald with gold star", "Zellige star art")
add(93, "bauhaus", "Bauhaus", "mid 40s", "colossal", "sharp platinum buzz cut", "Bauhaus geometric body art",
    "PRIMARY RED circles, BLUE squares, and YELLOW triangles composed across torso and both legs to ankle, WHITE grid bars", "P1",
    "red yellow chrome mirror platform stilettos 8 inch", "extra long squoval nails, primary color blocks", "Bauhaus art")
add(94, "kaleidoscope", "Kaleidoscope", "early 30s", "bubble", "big voluminous afro", "kaleidoscope body art",
    "JEWEL-TONE RUBY, SAPPHIRE, and TOPAZ mirrored kaleidoscope rosettes centered on bust and belly, radiating symmetric shards both legs to ankle", "P3",
    "ruby sapphire multi-strap platform stiletto sandals 8 inch", "extra long almond nails, jewel mosaic", "Kaleidoscope art")
add(95, "celestial_sunmoon", "Celestial Sun Moon", "late 30s", "top", "long locs with gold star cuffs", "celestial sun and moon body art",
    "BLAZING GOLD sun face on the belly, SILVER crescent moon on the bust, DEEP BLUE and GOLD stars and orbit lines both legs to ankle", "P5",
    "gold navy knee-high platform stiletto boots 8 inch", "extra long stiletto nails, gold sun and silver moon", "Celestial sun moon art")
add(96, "botanical_mushroom", "Botanical Engraving Mushroom", "late 40s", "pear", "silver-grey twists in a side bun", "vintage botanical engraving body art",
    "CREAM and RUST fine-line engraved mushrooms, MOSS GREEN moss and ferns across torso and both legs to ankle, crosshatched shading", "P4",
    "rust cream d'Orsay platform stilettos 8 inch", "extra long oval nails, moss green", "Botanical engraving art")
add(97, "uvsonar", "UV Sonar", "early 20s", "colossal", "UV-reactive neon green high puffs", "UV radar sonar body art",
    "ELECTRIC GREEN concentric sonar rings pulsing from the belly, VIVID CYAN sweep lines across bust, STARK WHITE target blips both legs to ankle", "P8",
    "green chrome mirror platform stilettos 8 inch", "extra long coffin nails, glowing green", "UV sonar art")
add(98, "uvorchid", "UV Orchid", "mid 30s", "hourglass", "UV-reactive hot pink sleek ponytail", "UV bioluminescent orchid body art",
    "ELECTRIC PINK and VIOLET glowing orchids across bust and belly, VIVID LIME stems and aerial roots both legs to ankle, STARK WHITE pollen sparks", "P2",
    "pink lime barely-there platform stilettos 8 inch", "extra long stiletto nails, glowing orchid pink", "UV orchid art")
add(99, "uvfirefly", "UV Firefly", "late 20s", "thigh", "UV-reactive amber waist-length braids", "UV firefly swarm body art",
    "ELECTRIC AMBER and YELLOW-GREEN firefly glows swirling in spirals across torso and both legs to ankle, VIVID WHITE light trails", "P7",
    "amber gold platform stiletto sandals with spiral straps coiling up the calf 8 inch", "extra long almond nails, glowing amber", "UV firefly art")
add(100, "uvfrost", "UV Frost", "early 40s", "amazon", "UV-reactive ice-white sculpted crown braid", "UV frost fractal body art",
    "ELECTRIC ICE BLUE branching frost crystals spreading across torso and both legs, STARK WHITE snowflake nodes, VIVID VIOLET edges", "P1",
    "ice blue knee-high lace-up platform stiletto boots 8 inch", "extra long coffin nails, frosted ice blue", "UV frost art")
add(101, "uvbrushstroke", "UV Brushstroke", "mid 40s", "spoon", "UV-reactive red sleek low bun", "UV neon ink brushstroke body art",
    "ELECTRIC RED and ORANGE sweeping calligraphic brush strokes (abstract, no letters) across torso and both legs to ankle, VIVID GOLD splatter dots", "P6",
    "red gold platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long stiletto nails, neon red brushstroke", "UV brushstroke art")
add(102, "uvwormhole", "UV Wormhole", "early 30s", "pear", "UV-reactive ultraviolet coily fro", "UV cosmic wormhole body art",
    "ELECTRIC VIOLET and CYAN spiral vortex centered on the belly, VIVID MAGENTA gravity-bent grid lines across bust and both legs to ankle, STARK WHITE stars", "P5",
    "violet cyan caged platform stiletto sandals 8 inch", "extra long almond nails, cosmic violet", "UV wormhole art")
add(103, "uvcaustics", "UV Caustics", "late 20s", "colossal", "UV-reactive aqua bob with bangs", "UV water caustics body art",
    "ELECTRIC AQUA and TURQUOISE rippling pool-light caustic networks across torso and both legs to ankle, STARK WHITE bright light knots", "P3",
    "aqua chrome mirror platform stilettos 8 inch", "extra long coffin nails, aqua shimmer", "UV caustics art")

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
