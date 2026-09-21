# -*- coding: utf-8 -*-
r"""
patch_livingartifact_deepblack_1_trio_json.py
Living Artifact · DeepBlack Ink — trios 54~63 (10 presets, 4:5)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_deepblack_1_trio_json.py
    python preset_builders\patch_livingartifact_deepblack_1_trio_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · DeepBlack Ink"
PLATFORM = "gemini"
ASPECT = "4:5"

SKIN = "deepest ebony skin with cool blue-black undertones"
X = "THE MOST EXTREME PHYSICALLY POSSIBLE"
PHYS = {
    "pear": f"pear queen physique {X} — narrow shoulders over colossal hips flaring to impossible width, enormous thick thighs, full bust",
    "colossal": f"colossal SuperBBW physique {X} — gigantic soft belly in deep overlapping rolls, not pregnant, overwhelmingly massive heavy bust, extremely wide hips, enormous thighs",
    "hourglass": f"hourglass queen physique {X} — impossibly cinched waist, hips flaring beyond human proportion, enormous full bust, thick touching thighs",
    "bubble": f"bubble butt goddess physique {X} — bubble butt projecting dramatically backward, snatched waist, full high bust, powerful thick thighs",
    "top": f"top-heavy bombshell physique {X} — overwhelmingly colossal bust beyond anatomy, broad soft shoulders, full belly, wide hips, thick thighs",
    "thigh": f"thick thigh temptress physique {X} — thighs massively thick pressing together, wide powerful hips, full heavy bust, snatched waist",
    "spoon": f"spoon-shape physique {X} — hips and seat dramatically wider than the upper body, full belly, full bust, enormous thighs",
    "amazon": f"amazon physique {X} — broad powerful shoulders, enormous bust, thick strong waist, massive hips, colossal muscular thighs",
}


def fig(side, age, phys, hair, motif, details, pose, shoes, nails, outline="Bold black ink outlines"):
    return (f"{side}: {SKIN}, {age}, {PHYS[phys]}, {hair} — full body {motif} covering EVERY inch of skin from neck to "
            f"ankle, both legs fully covered, NO bare skin below neck. {outline} — {details}, filling every gap, NO airbrush "
            f"NO gradient wash. Pose: {pose}\n{side}: {shoes}, {nails}.")


def trio(l, c, r, langs):
    return "\n\n".join([
        "Professional fashion photograph, full body shot. THREE women standing side by side, clear space between them.",
        l, c, r,
        "All: extreme high-gloss oil. MANDATORY pure pitch black background only, absolutely NO studio backdrop NO texture "
        "NO grey NO gradient. CRITICAL: all three women legs show FULL BODY ART coverage hip to ankle to toe, NO bare skin "
        f"on any leg. THREE completely different body art languages — {langs} — must CLASH dramatically against the "
        "deepest ebony skin. 8K portrait 4:5 vertical.",
    ])


P = []

P.append(("la_deepblack_054_trio_hannya_crane_holoprism", "LA DeepBlack 054 Trio – Hannya · Crane · UV Holoprism", trio(
    fig("LEFT", "late 30s", "pear", "jet black sleek chignon with red lacquer comb", "hannya mask and maple irezumi",
        "BLAZING WHITE hannya mask with crimson horns across the belly, VIVID SCARLET maple leaves swirling both legs hip to ankle, GOLD wind bars",
        "side profile, one hand resting on the small of her back, the other on her outer thigh, face turned to camera — extreme pear silhouette fully displayed.",
        "scarlet black knee-high platform stiletto boots 8 inch", "extra long stiletto nails scarlet maple tips"),
    fig("CENTER", "early 50s", "colossal", "silver-streaked high bun with white crane pin", "crane and pine irezumi",
        "PURE WHITE red-crowned cranes in flight across bust and belly, DEEP EMERALD pine boughs winding both legs, GOLD sun disc on the belly",
        "full frontal, both hands on wide hips, elbows out, chest open — colossal physique fully commanding.",
        "white gold caged platform stiletto sandals 8 inch", "extra long coffin nails white with red crane tips"),
    fig("RIGHT", "early 20s", "hourglass", "UV-reactive iridescent silver bob with blunt bangs", "UV holographic prism body art",
        "ELECTRIC CYAN and MAGENTA refracting prism shards tessellating full torso both legs to ankle, VIVID VIOLET light-split rainbow bands at hips thighs knees, STARK WHITE glints",
        "strong hip pop, one hand lifting hair at shoulder height, other hand on waist — impossible hourglass fully displayed.",
        "holographic peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails holographic prism tips", outline="Bold black outlines"),
    "hannya maple irezumi, crane pine irezumi, UV holographic prism")))

P.append(("la_deepblack_055_trio_kitsune_octopus_uvjellyfish", "LA DeepBlack 055 Trio – Kitsune · Octopus · UV Jellyfish", trio(
    fig("LEFT", "early 30s", "bubble", "long straight black hair with gold fox-ear ornaments", "kitsune and wisteria irezumi",
        "BLAZING ORANGE nine-tailed fox curling full torso to thighs, VIVID LAVENDER wisteria cascades both legs hip to ankle, GOLD foxfire flames",
        "three-quarter side view, walking one step forward, looking back toward camera, one hand trailing along her hip — bubble butt silhouette in motion.",
        "orange lavender platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long stiletto nails orange foxfire tips"),
    fig("CENTER", "mid 40s", "top", "short silver-white tapered afro", "octopus and wave irezumi",
        "DEEP CRIMSON giant octopus tentacles wrapping torso and both legs to ankle, VIVID COBALT Hokusai-style waves, PURE WHITE sea foam",
        "full frontal, one hand at collarbone, other hand resting on belly, chin lifted — top-heavy physique fully commanding.",
        "crimson cobalt knee-high lace-up platform stiletto boots 8 inch", "extra long coffin nails cobalt wave tips"),
    fig("RIGHT", "early 20s", "thigh", "UV-reactive glowing aqua locs piled high", "UV bioluminescent jellyfish body art",
        "ELECTRIC AQUA jellyfish bells across bust and belly, VIVID PINK trailing tentacle lines flowing both legs hip to toe, STARK WHITE plankton sparkle dots",
        "contrapposto, one foot raised on a low black block, hand resting on raised knee — extreme thick thighs fully displayed.",
        "aqua pink barely-there platform stilettos 8 inch", "extra long almond nails glowing aqua tips", outline="Bold black outlines"),
    "kitsune wisteria irezumi, octopus wave irezumi, UV bioluminescent jellyfish")))

P.append(("la_deepblack_056_trio_chrysanthemum_tortoise_uvaurora", "LA DeepBlack 056 Trio – Chrysanthemum · Tortoise · UV Aurora", trio(
    fig("LEFT", "late 20s", "hourglass", "glossy black finger waves with gold chrysanthemum pin", "chrysanthemum and cherry blossom waterfall irezumi",
        "BLAZING GOLD chrysanthemums across bust and hips, SOFT PINK cherry petals falling both legs to ankle, VIVID TEAL waterfall streams",
        "facing camera, both hands gently framing her face, elbows low, hip shifted — hourglass fully displayed.",
        "gold teal peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long stiletto nails gold petal tips"),
    fig("CENTER", "mid 50s", "colossal", "short silver natural curls", "sea tortoise and kelp irezumi",
        "JADE GREEN ancient tortoise with gold shell plates across the belly, DEEP OLIVE kelp forests rising both legs, WHITE bubble trails",
        "full frontal, hands clasped loosely behind lower back, shoulders drawn back, chest and belly forward — colossal physique fully commanding.",
        "jade olive knee-high platform stiletto boots 8 inch", "extra long coffin nails jade shell tips"),
    fig("RIGHT", "early 20s", "spoon", "UV-reactive glowing mint high ponytail", "UV aurora borealis body art",
        "ELECTRIC GREEN and VIOLET aurora ribbons flowing diagonally across torso and spiraling both legs to ankle, STARK WHITE star points, VIVID PINK shimmer edges",
        "three-quarter view, one arm extended to the side at shoulder height, other hand on hip — extreme spoon silhouette fully displayed.",
        "green violet spiral-strap platform stiletto sandals 8 inch", "extra long almond nails aurora gradient tips", outline="Bold black outlines"),
    "chrysanthemum waterfall irezumi, tortoise kelp irezumi, UV aurora")))

P.append(("la_deepblack_057_trio_mehndi_aztec_uvglitch", "LA DeepBlack 057 Trio – Mehndi · Aztec · UV Glitch", trio(
    fig("LEFT", "mid 30s", "colossal", "long braid wrapped with gold thread", "mehndi mandala body art",
        "BLAZING GOLD paisley and mandala medallions across bust and belly, VIVID COPPER lace filigree bands both legs to ankle, ROSE GOLD dot work",
        "facing camera, both hands resting softly on her belly, gentle hip shift — colossal physique fully displayed.",
        "gold copper caged platform stiletto sandals 8 inch", "extra long stiletto nails gold filigree tips", outline="Bold black outlines"),
    fig("CENTER", "early 40s", "amazon", "gold-cuffed high puff", "Aztec sun stone body art",
        "BLAZING TURQUOISE and GOLD sun stone calendar disc on the belly, VIVID RED stepped glyph bands both legs to ankle, JADE feathered serpent borders",
        "full frontal wide stance, both hands on hips, chin lifted — amazon physique fully commanding.",
        "turquoise gold platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails turquoise glyph tips", outline="Bold black outlines"),
    fig("RIGHT", "early 20s", "bubble", "UV-reactive neon green buzz cut", "UV glitch pixel body art",
        "ELECTRIC MAGENTA and CYAN displaced pixel blocks shearing across torso and both legs, VIVID YELLOW scanline stripes at hips thighs knees, STARK WHITE static noise",
        "side profile, one hand resting on the small of her back, face turned to camera — bubble butt silhouette fully displayed.",
        "magenta cyan mirror platform stilettos with chrome heels 8 inch", "extra long almond nails pixel glitch tips", outline="Bold black outlines"),
    "gold mehndi mandala, Aztec sun stone, UV glitch pixel")))

P.append(("la_deepblack_058_trio_celtic_artnouveau_uvconstellation", "LA DeepBlack 058 Trio – Celtic · Art Nouveau · UV Constellation", trio(
    fig("LEFT", "late 40s", "thigh", "silver-tipped locs in a high crown", "Celtic knotwork body art",
        "BLAZING SILVER interlaced knot panels across torso, EMERALD triskele spirals at hips and knees, BRONZE zoomorphic beasts winding both legs to ankle",
        "contrapposto, one hand at collarbone, other hand on outer thigh — thick thighs fully displayed.",
        "silver emerald knee-high lace-up platform stiletto boots 8 inch", "extra long stiletto nails silver knot tips", outline="Bold black outlines"),
    fig("CENTER", "early 30s", "hourglass", "glossy black sculpted updo with gold lily pin", "Art Nouveau lily body art",
        "PURE WHITE lilies and irises across bust and belly, VIVID GOLD whiplash stems curving both legs to ankle, SOFT PEACH and SAGE fills",
        "three-quarter view, one hand lifting a lock of hair at shoulder height, other hand resting on hip — hourglass fully displayed.",
        "gold ivory d'Orsay platform stilettos 8 inch", "extra long coffin nails ivory lily tips", outline="Bold black whiplash outlines"),
    fig("RIGHT", "mid 20s", "pear", "UV-reactive glowing indigo afro halo", "UV constellation star map body art",
        "ELECTRIC WHITE star points connected by CYAN constellation lines across torso, VIVID VIOLET zodiac rings at hips and knees, GOLD celestial grid lines both legs to toe",
        "full frontal, one arm extended gracefully to the side at shoulder height, other hand on hip — pear silhouette fully displayed.",
        "indigo white multi-strap platform stiletto sandals 8 inch", "extra long almond nails glowing star tips", outline="Bold black outlines"),
    "Celtic knotwork, Art Nouveau lilies, UV constellation map")))

P.append(("la_deepblack_059_trio_stainedglass_nebula_uvlaser", "LA DeepBlack 059 Trio – Stained Glass · Nebula · UV Laser", trio(
    fig("LEFT", "early 30s", "top", "sleek black high ponytail with gold cuff", "stained glass body art",
        "RUBY, SAPPHIRE, and AMBER glass panels in a rose window across bust and belly, EMERALD vine panels both legs to ankle, GOLD lead highlights",
        "facing camera, both hands on hips, elbows out, chest open — top-heavy physique fully displayed.",
        "ruby sapphire caged platform stiletto sandals 8 inch", "extra long stiletto nails ruby glass tips", outline="Bold black leaded outlines"),
    fig("CENTER", "late 40s", "colossal", "silver-streaked twist-out", "galaxy nebula body art",
        "DEEP MAGENTA and TEAL nebula clouds swirling across belly and bust, GOLD spiral galaxy on the belly, WHITE star clusters both legs to ankle",
        "full frontal, hands clasped loosely behind lower back, chest and belly forward — colossal physique fully commanding.",
        "magenta teal knee-high platform stiletto boots 8 inch", "extra long coffin nails galaxy swirl tips", outline="Bold black outlines"),
    fig("RIGHT", "early 20s", "bubble", "UV-reactive glowing red micro braids", "UV laser topographic body art",
        "ELECTRIC RED contour lines wrapping torso and both legs like a terrain map, VIVID LIME grid crosshairs at hips thighs knees, STARK WHITE elevation numbers",
        "three-quarter view walking forward, looking over her shoulder toward camera, one hand trailing on hip — bubble butt silhouette in motion.",
        "red lime mirror platform stilettos with chrome heels 8 inch", "extra long almond nails red laser tips", outline="Bold black outlines"),
    "stained glass rose window, galaxy nebula, UV laser topography")))

P.append(("la_deepblack_060_trio_sugarskull_petrykivka_uvsynthwave", "LA DeepBlack 060 Trio – Día de Muertos · Petrykivka · UV Synthwave", trio(
    fig("LEFT", "early 40s", "hourglass", "black curls crowned with orange marigolds", "Día de los Muertos floral body art",
        "BLAZING ORANGE marigolds and HOT PINK roses across bust and hips, WHITE sugar skull motifs on the thighs, TURQUOISE filigree both legs to ankle",
        "facing camera, both hands gently framing her face, elbows low, hip shifted — hourglass fully displayed.",
        "orange pink platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long stiletto nails marigold tips", outline="Bold black outlines"),
    fig("CENTER", "mid 30s", "colossal", "gold-beaded crown braid", "Petrykivka folk flower body art",
        "VIVID RED and SUNFLOWER YELLOW brushstroke blossoms, EMERALD feathered leaves, COBALT berries across torso and both legs to ankle",
        "full frontal, one hand at collarbone, other hand on belly — colossal physique fully commanding.",
        "red yellow peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails folk flower tips", outline="Bold black outlines"),
    fig("RIGHT", "early 20s", "thigh", "UV-reactive hot pink blunt bob", "UV synthwave body art",
        "ELECTRIC PINK and ORANGE striped retro sun on the belly, VIVID CYAN perspective grid wrapping both legs to ankle, VIOLET palm silhouettes at hips",
        "contrapposto, one foot raised on a low black block, hand resting on raised knee — thick thighs fully displayed.",
        "pink cyan barely-there platform stilettos 8 inch", "extra long almond nails neon sunset tips", outline="Bold black outlines"),
    "Día de los Muertos florals, Petrykivka folk flowers, UV synthwave")))

P.append(("la_deepblack_061_trio_biomech_raven_uvdna", "LA DeepBlack 061 Trio – Biomech · Raven Woodcut · UV DNA", trio(
    fig("LEFT", "late 20s", "amazon", "shaved sides with long top braid", "biomechanical body art",
        "GUNMETAL pistons and gears revealed under torn-skin illusion across torso, BRASS hydraulic tubes running both legs to ankle, ELECTRIC BLUE power cores at hips and knees",
        "three-quarter view, one arm extended to the side at shoulder height, other hand on hip — amazon physique fully displayed.",
        "gunmetal brass knee-high lace-up platform stiletto boots 8 inch", "extra long stiletto nails chrome gear tips", outline="Bold black outlines"),
    fig("CENTER", "early 50s", "pear", "silver close-cropped curls", "monochrome woodcut raven body art",
        "STARK WHITE woodcut-engraved ravens and feathers across bust and belly, PALE GREY moon and branch linework both legs to ankle, crosshatched shading",
        "full frontal, hands clasped loosely behind lower back, chest and hips forward — pear silhouette fully commanding.",
        "white grey d'Orsay platform stilettos 8 inch", "extra long coffin nails white feather tips", outline="Bold black outlines"),
    fig("RIGHT", "mid 20s", "colossal", "UV-reactive glowing violet bantu knots", "UV DNA helix body art",
        "ELECTRIC VIOLET and LIME double helix strands spiraling torso and both legs to ankle, VIVID CYAN base-pair rungs, STARK WHITE molecule nodes",
        "facing camera, both hands resting softly on her belly, gentle hip shift — colossal physique fully displayed.",
        "violet lime caged platform stiletto sandals 8 inch", "extra long almond nails glowing helix tips", outline="Bold black outlines"),
    "biomechanical, monochrome woodcut raven, UV DNA helix")))

P.append(("la_deepblack_062_trio_peony_polynesian_uvequalizer", "LA DeepBlack 062 Trio – Peony Butterfly · Ocean Pattern · UV Equalizer", trio(
    fig("LEFT", "mid 30s", "spoon", "sleek black low bun with pink peony pin", "peony and butterfly irezumi",
        "HOT PINK and CORAL peonies across bust and hips, GOLD swallowtail butterflies both legs to ankle, DEEP TEAL wind bars",
        "side profile, one hand resting on the small of her back, face turned to camera — spoon silhouette fully displayed.",
        "pink gold multi-strap platform stiletto sandals 8 inch", "extra long stiletto nails peony pink tips"),
    fig("CENTER", "early 40s", "thigh", "long wavy black hair with a shell ornament", "Polynesian-inspired ocean pattern body art",
        "STARK WHITE wave, shark-tooth, and turtle-shell band patterns wrapping torso and both legs to ankle, OCEAN BLUE fills and GOLD sun rays",
        "contrapposto, one foot raised on a low black block, hand resting on raised knee — thick thighs fully displayed.",
        "white blue platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails wave pattern tips", outline="Bold black outlines"),
    fig("RIGHT", "early 20s", "hourglass", "UV-reactive electric yellow high puff", "UV sound wave equalizer body art",
        "ELECTRIC YELLOW and CYAN equalizer bars pulsing across torso, VIVID MAGENTA waveform lines both legs to ankle, STARK WHITE frequency markers",
        "facing camera, one hand lifting hair at shoulder height, other hand on hip — hourglass fully displayed.",
        "yellow cyan peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails neon waveform tips", outline="Bold black outlines"),
    "peony butterfly irezumi, Polynesian-inspired ocean pattern, UV sound equalizer")))

P.append(("la_deepblack_063_trio_mermaid_lion_uvchrome", "LA DeepBlack 063 Trio – Mermaid · Lion Sun · UV Liquid Chrome", trio(
    fig("LEFT", "late 20s", "bubble", "long sea-green ombré waves with pearl pins", "mermaid and coral irezumi",
        "IRIDESCENT TEAL fish scales covering both legs to ankle, CORAL RED coral branches across hips and torso, PEARL WHITE bubbles",
        "three-quarter view walking forward, looking over her shoulder toward camera, one hand trailing on hip — bubble butt silhouette in motion.",
        "teal pearl caged platform stiletto sandals 8 inch", "extra long stiletto nails iridescent scale tips"),
    fig("CENTER", "late 40s", "colossal", "voluminous golden-brown afro like a mane", "lion and sun body art",
        "BLAZING AMBER lion head across the belly, GOLD sunburst rays radiating across bust and hips, DEEP OCHRE savanna grass both legs to ankle",
        "full frontal wide stance, both hands on hips, chin lifted — colossal physique fully commanding.",
        "amber gold knee-high platform stiletto boots 8 inch", "extra long coffin nails gold sunburst tips"),
    fig("RIGHT", "mid 30s", "top", "UV-reactive silver sleek bun", "UV liquid chrome body art",
        "MIRROR SILVER liquid metal ripples flowing torso and both legs to ankle, ELECTRIC BLUE reflection streaks, VIVID VIOLET molten droplets",
        "contrapposto, one hand at collarbone, other hand resting on her belly — top-heavy physique fully displayed.",
        "chrome mirror platform stilettos with thick mirrored platform 8 inch", "extra long almond nails liquid chrome tips", outline="Bold black outlines"),
    "mermaid coral irezumi, lion sun, UV liquid chrome")))

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
