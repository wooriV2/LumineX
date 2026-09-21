# -*- coding: utf-8 -*-
r"""
patch_livingartifact_deepblack_4_sbbw_group_json.py
Living Artifact · DeepBlack Ink — SuperBBW trios 104~113 (4:5) + duos 114~133 (3:4)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_deepblack_4_sbbw_group_json.py
    python preset_builders\patch_livingartifact_deepblack_4_sbbw_group_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · DeepBlack Ink"
PLATFORM = "gemini"

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


def fig(side, age, hair, motif, details, pose, shoes, nails, outline="Bold black outlines"):
    return (f"{side}: {SKIN}, {age}, {SBBW}, {hair} — full body {motif} from neck to ankle, EVERY inch covered, NO bare "
            f"skin below neck. {outline} — {details}, filling every gap, NO airbrush NO gradient wash. Pose: {POSE[pose]} "
            f"{shoes}, {nails}.")


def trio(l, c, r, langs):
    return "\n".join([
        "Professional fashion photograph, full body shot. THREE women standing side by side, clear space between them.",
        l, c, r,
        "All: extreme high-gloss oil. MANDATORY pure pitch black background only, NO backdrop NO texture NO grey NO gradient. "
        "All three same scale, CENTER exactly as colossal as LEFT and RIGHT. CRITICAL: all legs show FULL BODY ART hip to "
        f"ankle to toe. THREE different body art languages — {langs} — CLASH against the deepest ebony skin. 8K portrait 4:5 vertical.",
    ])


def duo(l, r, langs):
    return "\n".join([
        "Professional fashion photograph, full body shot. TWO women standing side by side, clear space between them.",
        l, r,
        "All: extreme high-gloss oil. MANDATORY pure pitch black background only, NO backdrop NO texture NO grey NO gradient. "
        "Both same scale, equally colossal. CRITICAL: both women's legs show FULL BODY ART hip to ankle to toe. TWO body art "
        f"languages — {langs} — CLASH against the deepest ebony skin. 8K portrait 3:4 vertical.",
    ])


P = []  # (key, title, prompt, aspect)


def add_trio(num, slug, title, l, c, r, langs):
    P.append((f"la_deepblack_{num:03d}_trio_{slug}", f"LA DeepBlack {num:03d} Trio SBBW – {title}", trio(l, c, r, langs), "4:5"))


def add_duo(num, slug, title, l, r, langs):
    P.append((f"la_deepblack_{num:03d}_duo_{slug}", f"LA DeepBlack {num:03d} Duo SBBW – {title}", duo(l, r, langs), "3:4"))


# ══ Trios 104~113 ═══════════════════════════════════════
add_trio(104, "shishi_namazu_uvsacredgeo", "Shishi · Namazu · UV Sacred Geometry",
    fig("LEFT", "late 30s", "sleek black high bun with gold pin", "shishi guardian lion and peony irezumi", "BLAZING GOLD shishi lion with curled mane across belly, CRIMSON peonies on bust and both legs to ankle", "P1", "Gold crimson caged platform stiletto sandals 8 inch", "extra long stiletto nails gold", outline="Bold black ink outlines"),
    fig("CENTER", "early 50s", "silver close-cropped curls", "namazu giant catfish and wave irezumi", "SLATE BLUE giant catfish with long whiskers across the belly, WHITE crashing waves both legs to ankle, GOLD rocks", "P8", "Slate white knee-high platform stiletto boots 8 inch", "extra long coffin nails wave white", outline="Bold black ink outlines"),
    fig("RIGHT", "mid 20s", "UV-reactive electric gold afro puff", "UV sacred geometry body art", "ELECTRIC GOLD flower-of-life circles centered on the belly, VIVID CYAN interlocking polygons across bust and both legs to ankle", "P2", "Gold chrome mirror platform stilettos 8 inch", "extra long almond nails glowing gold"),
    "shishi peony irezumi, namazu wave irezumi, UV sacred geometry")
add_trio(105, "qilin_ume_uvmycelium", "Qilin · Ume Nightingale · UV Mycelium",
    fig("LEFT", "early 40s", "long braids wrapped in jade thread", "qilin and cloud irezumi", "JADE GREEN scaled qilin across belly, GOLD flame mane on bust, TURQUOISE ruyi clouds both legs to ankle", "P3", "Jade gold peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails jade", outline="Bold black ink outlines"),
    fig("CENTER", "late 20s", "sleek black bob", "ume plum blossom and nightingale irezumi", "BLUSH PINK plum blossoms on dark branches across bust and belly, OLIVE nightingales perched on hips, SILVER snow dots both legs to ankle", "P1", "Blush silver d'Orsay platform stilettos 8 inch", "extra long oval nails plum pink", outline="Bold black ink outlines"),
    fig("RIGHT", "mid 30s", "UV-reactive lime twists", "UV mycelium network body art", "ELECTRIC LIME branching fungal threads across torso and both legs, VIVID VIOLET spore nodes at hips and knees, STARK WHITE micro filaments", "P5", "Lime violet multi-strap platform stiletto sandals 8 inch", "extra long almond nails glowing lime"),
    "qilin cloud irezumi, ume nightingale irezumi, UV mycelium")
add_trio(106, "iris_barong_uvspirograph", "Iris Dragonfly · Barong · UV Spirograph",
    fig("LEFT", "mid 20s", "long straight black hair with a violet pin", "iris and dragonfly irezumi", "DEEP VIOLET irises across bust and belly, IRIDESCENT BLUE dragonflies on hips, GREEN blade leaves both legs to ankle", "P8", "Violet blue platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long almond nails iris violet", outline="Bold black ink outlines"),
    fig("CENTER", "late 40s", "high wrapped gold headwrap", "Balinese barong mask body art", "CRIMSON and GOLD barong mask with mirror-studded mane across the belly, WHITE fringe and GOLD carved floral bands on bust and both legs to ankle", "P4", "Crimson gold knee-high lace-up platform stiletto boots 8 inch", "extra long coffin nails gold carved"),
    fig("RIGHT", "early 30s", "UV-reactive magenta high ponytail", "UV spirograph body art", "ELECTRIC MAGENTA and CYAN looping hypotrochoid curves layered across bust, belly, and both legs to ankle, STARK WHITE center points", "P3", "Magenta cyan caged platform stiletto sandals 8 inch", "extra long stiletto nails neon loop"),
    "iris dragonfly irezumi, Balinese barong, UV spirograph")
add_trio(107, "morningglory_wayang_uvlissajous", "Morning Glory · Wayang · UV Lissajous",
    fig("LEFT", "early 50s", "silver twist-out", "morning glory vine irezumi", "COBALT and MAGENTA morning glory trumpets across bust and belly, BRIGHT GREEN twisting vines spiraling both legs to ankle", "P2", "Cobalt magenta multi-strap platform stiletto sandals 8 inch", "extra long oval nails cobalt", outline="Bold black ink outlines"),
    fig("CENTER", "mid 30s", "sleek black chignon with gold filigree", "Javanese wayang shadow puppet body art", "GOLD and CRIMSON intricately perforated puppet silhouettes and gunungan tree on the belly, TEAL carved lace patterns both legs to ankle", "P1", "Gold teal d'Orsay platform stilettos 8 inch", "extra long stiletto nails gold lace"),
    fig("RIGHT", "early 20s", "UV-reactive electric green bob", "UV oscilloscope Lissajous body art", "ELECTRIC GREEN glowing Lissajous figure-eight and knot curves across torso and both legs, VIVID AMBER grid ticks", "P7", "Green amber barely-there platform stilettos 8 inch", "extra long coffin nails oscilloscope green"),
    "morning glory irezumi, wayang shadow puppet, UV Lissajous")
add_trio(108, "ginkgo_scarab_uvneural", "Ginkgo · Egyptian Scarab · UV Neural",
    fig("LEFT", "late 20s", "golden-tinted locs", "ginkgo and autumn wind irezumi", "BLAZING YELLOW fan-shaped ginkgo leaves swirling across bust, belly, and both legs to ankle, GOLD wind bars", "P5", "Yellow gold peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails ginkgo yellow", outline="Bold black ink outlines"),
    fig("CENTER", "mid 40s", "sleek black blunt bob with gold beads", "ancient Egyptian lotus and scarab body art", "LAPIS BLUE winged scarab across the bust, GOLD and TURQUOISE lotus friezes down the belly and both legs to ankle, CARNELIAN accents", "P4", "Lapis gold caged platform stiletto sandals 8 inch", "extra long coffin nails lapis blue"),
    fig("RIGHT", "early 30s", "UV-reactive white-blue high puff", "UV neural network body art", "ELECTRIC BLUE glowing neurons with branching dendrites across torso and both legs, VIVID PINK synapse flashes, STARK WHITE signal pulses", "P3", "Blue pink chrome mirror platform stilettos 8 inch", "extra long stiletto nails glowing neuron"),
    "ginkgo irezumi, Egyptian lotus scarab, UV neural network")
add_trio(109, "oni_maasai_uvsplatter", "Oni Flame · Maasai · UV Splatter",
    fig("LEFT", "mid 30s", "sleek black high ponytail with red cord", "oni mask and flame irezumi", "VERMILION oni mask with gold horns across the belly, ORANGE flame scrolls on bust and both legs to ankle, BLACK smoke curls", "P1", "Vermilion black knee-high lace-up platform stiletto boots 8 inch", "extra long stiletto nails flame orange", outline="Bold black ink outlines"),
    fig("CENTER", "early 50s", "short shaved silver hair", "Maasai beadwork pattern body art", "BRIGHT RED, WHITE, COBALT, and YELLOW concentric beaded collar rings across bust, beaded band patterns down belly and both legs to ankle", "P8", "Red white multi-strap platform stiletto sandals 8 inch", "extra long coffin nails bead stripe"),
    fig("RIGHT", "late 20s", "UV-reactive rainbow box braids", "UV blacklight paint splatter body art", "ELECTRIC PINK, YELLOW, GREEN, and ORANGE splashes, drips, and speckles covering torso and both legs to ankle", "P6", "Neon multicolor platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long almond nails splatter neon"),
    "oni flame irezumi, Maasai beadwork, UV blacklight splatter")
add_trio(110, "fuji_mosaic_uvstringart", "Fuji Cloud · Roman Mosaic · UV String Art",
    fig("LEFT", "early 40s", "black low bun with lacquer comb", "Mount Fuji and cloud irezumi", "INDIGO and WHITE snowcapped Fuji across the belly, CRIMSON rising sun on the bust, GOLD cloud bands both legs to ankle", "P2", "Indigo crimson peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails rising sun", outline="Bold black ink outlines"),
    fig("CENTER", "late 20s", "voluminous black curls with a laurel pin", "Roman floor mosaic body art", "TERRACOTTA, OCHRE, and CREAM tesserae forming dolphins, laurels, and guilloche borders across torso and both legs to ankle", "P1", "Terracotta cream caged platform stiletto sandals 8 inch", "extra long almond nails mosaic ochre"),
    fig("RIGHT", "mid 40s", "UV-reactive turquoise sculpted crown braid", "UV neon string art body art", "ELECTRIC TURQUOISE and PINK taut string lines forming parabolic curves and star webs across torso and both legs to ankle, STARK WHITE pin points", "P8", "Turquoise pink multi-strap platform stiletto sandals 8 inch", "extra long stiletto nails neon string"),
    "Fuji cloud irezumi, Roman mosaic, UV string art")
add_trio(111, "lantern_azulejo_uvtesseract", "Lantern Festival · Azulejo · UV Tesseract",
    fig("LEFT", "early 30s", "twin high buns with red tassels", "night lantern festival irezumi", "GLOWING RED and ORANGE paper lanterns across bust and belly, GOLD firework bursts, INDIGO night swirls both legs to ankle", "P7", "Red gold platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long coffin nails lantern red", outline="Bold black ink outlines"),
    fig("CENTER", "late 40s", "silver-streaked sleek chignon", "Portuguese azulejo tile body art", "COBALT BLUE and WHITE glazed tile panels with scrolls, birds, and ships across torso and both legs to ankle, YELLOW border tiles", "P4", "Cobalt white d'Orsay platform stilettos 8 inch", "extra long oval nails azulejo blue"),
    fig("RIGHT", "mid 20s", "UV-reactive violet buzz cut", "UV tesseract hypercube body art", "ELECTRIC VIOLET and CYAN nested rotating cube wireframes across bust and belly, VIVID YELLOW vertex points both legs to ankle", "P3", "Violet chrome mirror platform stilettos 8 inch", "extra long almond nails glowing cube"),
    "lantern festival irezumi, Portuguese azulejo, UV tesseract")
add_trio(112, "kozane_urnes_uvquasar", "Kozane Armor · Urnes Beasts · UV Quasar",
    fig("LEFT", "late 30s", "sleek black topknot", "kozane lamellar armor scale body art", "LACQUERED CRIMSON and GOLD overlapping armor plates laced with NAVY cords across torso and both legs to ankle", "P1", "Crimson navy knee-high lace-up platform stiletto boots 8 inch", "extra long stiletto nails lacquer red"),
    fig("CENTER", "mid 20s", "long braided crown with silver rings", "Viking Urnes-style interlaced beast body art", "SILVER and BRONZE elongated serpent beasts interlacing across bust, belly, and both legs to ankle, DEEP GREEN fills", "P2", "Silver bronze caged platform stiletto sandals 8 inch", "extra long coffin nails silver knot"),
    fig("RIGHT", "early 50s", "UV-reactive white silver afro", "UV quasar body art", "ELECTRIC WHITE-BLUE blazing core on the belly with twin relativistic jets beaming up the torso and down both legs, VIVID MAGENTA accretion rings", "P8", "White blue chrome mirror platform stilettos 8 inch", "extra long almond nails quasar white"),
    "kozane armor, Urnes beasts, UV quasar")
add_trio(113, "goldfish_greekmeander_uvplankton", "Goldfish · Greek Black-figure · UV Plankton",
    fig("LEFT", "early 20s", "orange-tipped curls", "fancy goldfish and water plant irezumi", "ORANGE and WHITE fantail goldfish with flowing fins across bust and belly, GREEN water weeds both legs to ankle, PALE BLUE bubbles", "P5", "Orange white peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long almond nails goldfish orange", outline="Bold black ink outlines"),
    fig("CENTER", "early 40s", "high braided bun with gold laurel", "Greek black-figure and meander body art", "TERRACOTTA ORANGE panels with black-figure dancers and horses across bust and belly, GOLD meander key bands wrapping both legs to ankle", "P1", "Terracotta gold platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails meander gold"),
    fig("RIGHT", "mid 30s", "UV-reactive aqua waist-length locs", "UV bioluminescent plankton wave body art", "ELECTRIC AQUA glowing breaking-wave crests across bust and belly, VIVID BLUE sparkle trails both legs to ankle, STARK WHITE spray dots", "P7", "Aqua blue barely-there platform stilettos 8 inch", "extra long stiletto nails glowing aqua"),
    "goldfish irezumi, Greek black-figure meander, UV plankton wave")

# ══ Duos 114~133 ════════════════════════════════════════
D = [
    (114, "qinghua_uvbutterfly", "Blue-and-White · UV Butterfly Swarm",
     ("early 40s", "sleek black high bun with a porcelain pin", "blue-and-white porcelain pattern body art", "COBALT BLUE lotus scrolls and waves on a PORCELAIN WHITE painted base across torso and both legs to ankle", "P1", "Cobalt white d'Orsay platform stilettos 8 inch", "extra long oval nails porcelain blue"),
     ("late 20s", "UV-reactive orange twist-out", "UV neon butterfly swarm body art", "ELECTRIC ORANGE and VIOLET glowing butterflies swirling in a spiral across bust, belly, and both legs to ankle, STARK WHITE wing sparkles", "P3", "Orange violet caged platform stiletto sandals 8 inch", "extra long almond nails glowing wing"),
     "blue-and-white porcelain, UV butterfly swarm"),
    (115, "dancheong_kuba", "Dancheong · Kuba",
     ("mid 30s", "long black braid with a jade binyeo", "Korean dancheong pattern body art", "CELADON GREEN, VERMILION, COBALT, and YELLOW lotus medallions and banded geometric borders across torso and both legs to ankle", "P2", "Green vermilion multi-strap platform stiletto sandals 8 inch", "extra long coffin nails dancheong green"),
     ("early 50s", "silver short afro with cowrie band", "Kuba cloth pattern body art", "RAFFIA TAN, RUST, and DARK BROWN interlocking maze-like geometric blocks across torso and both legs to ankle", "P4", "Tan rust knee-high platform stiletto boots 8 inch", "extra long almond nails raffia tan"),
     "Korean dancheong, Kuba cloth"),
    (116, "bojagi_uvpulsar", "Bojagi · UV Pulsar",
     ("late 40s", "sleek black low chignon", "Korean bojagi patchwork body art", "JEWEL-TONE PINK, JADE, SAFFRON, and INDIGO translucent patchwork squares with fine stitched seams across torso and both legs to ankle", "P8", "Pink jade peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long oval nails patchwork"),
     ("early 20s", "UV-reactive ice blue high ponytail", "UV pulsar radio wave body art", "ELECTRIC ICE BLUE pulse lines stacked like a radio signal chart across bust and belly, VIVID WHITE beam cones sweeping both legs to ankle", "P7", "Ice blue chrome mirror platform stilettos 8 inch", "extra long stiletto nails pulse white"),
     "bojagi patchwork, UV pulsar"),
    (117, "hwajodo_amazigh", "Hwajodo · Amazigh",
     ("early 30s", "long straight black hair with a coral pin", "Korean hwajodo flower-and-bird body art", "CORAL peonies, PLUM blossoms, and pairs of MANDARIN DUCKS and MAGPIES across bust and belly, JADE rocks and branches both legs to ankle", "P5", "Coral jade platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long almond nails coral"),
     ("mid 40s", "long braids with silver coins", "Amazigh Berber geometric body art", "SAFFRON, INDIGO, and SILVER diamonds, chevrons, and cross-hatched lozenges across torso and both legs to ankle", "P1", "Saffron silver platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails indigo diamond"),
     "hwajodo flower and bird, Amazigh geometric"),
    (118, "rangoli_uvpaisley", "Rangoli · UV Paisley",
     ("late 30s", "long thick braid with marigold beads", "rangoli pattern body art", "MAGENTA, SAFFRON, LEAF GREEN, and WHITE radial floral rangoli rosettes centered on bust and belly, petal borders both legs to ankle", "P3", "Magenta saffron caged platform stiletto sandals 8 inch", "extra long stiletto nails rangoli petal"),
     ("early 30s", "UV-reactive hot pink sleek bob", "UV neon paisley body art", "ELECTRIC PINK and TEAL glowing paisley teardrops nested across torso and both legs, VIVID YELLOW dot trims", "P6", "Pink teal barely-there platform stilettos 8 inch", "extra long coffin nails neon paisley"),
     "rangoli, UV paisley"),
    (119, "madhubani_shweshwe", "Madhubani · Shweshwe",
     ("mid 20s", "center-parted long black hair", "Madhubani folk painting body art", "RED, YELLOW, and GREEN paired fish, peacocks, and sun faces across bust and belly, dense line-filled borders both legs to ankle", "P1", "Red yellow multi-strap platform stiletto sandals 8 inch", "extra long almond nails folk red"),
     ("early 50s", "high indigo headwrap", "shweshwe print body art", "INDIGO BLUE base with fine WHITE discharge-print circles, stars, and geometric lattices across torso and both legs to ankle", "P8", "Indigo white knee-high platform stiletto boots 8 inch", "extra long coffin nails indigo dot"),
     "Madhubani folk, shweshwe print"),
    (120, "kalamkari_uvmushroom", "Kalamkari · UV Mushroom",
     ("early 40s", "low bun with jasmine strings", "kalamkari tree-of-life body art", "MADDER RED, INDIGO, and MUSTARD tree of life rising from belly to bust with birds and blossoms, vine borders both legs to ankle", "P4", "Madder red mustard d'Orsay platform stilettos 8 inch", "extra long oval nails madder red"),
     ("late 20s", "UV-reactive teal coils", "UV bioluminescent mushroom body art", "ELECTRIC TEAL and GREEN glowing mushroom clusters rising both legs, VIVID BLUE caps across belly and hips, STARK WHITE spores drifting over bust", "P2", "Teal green caged platform stiletto sandals 8 inch", "extra long almond nails glowing teal"),
     "kalamkari tree of life, UV mushrooms"),
    (121, "girih_tuareg", "Girih · Tuareg Silver",
     ("mid 30s", "long black waves with a gold chain", "girih arabesque geometry body art", "TURQUOISE and GOLD ten-point star girih strapwork across torso and both legs to ankle, LAPIS fills", "P3", "Turquoise gold peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long stiletto nails lapis gold"),
     ("late 40s", "braids with silver cross pendants", "Tuareg engraved silver body art", "BRIGHT SILVER engraved triangles, lozenges, and pendant shapes over INDIGO base across torso and both legs to ankle", "P6", "Silver indigo platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails engraved silver"),
     "girih arabesque, Tuareg silver"),
    (122, "uli_uvrosethorn", "Uli · UV Rose Thorn",
     ("early 50s", "silver cornrows into a crown", "Igbo uli line art body art", "delicate IVORY and OCHRE spirals, crescents, and stylized plant forms across torso and both legs to ankle", "P8", "Ivory ochre d'Orsay platform stilettos 8 inch", "extra long oval nails ivory line"),
     ("mid 20s", "UV-reactive red high puff", "UV neon rose and thorn body art", "ELECTRIC RED glowing roses on bust and belly, VIVID GREEN thorny stems spiraling both legs to ankle, STARK WHITE dew sparks", "P1", "Red green caged platform stiletto sandals 8 inch", "extra long stiletto nails neon rose"),
     "uli line art, UV neon rose"),
    (123, "delft_gzhel", "Delft · Gzhel",
     ("late 20s", "black finger waves", "Delft tile body art", "DELFT BLUE windmills, tulips, and sailing ships in square tile frames on a WHITE glaze base across torso and both legs to ankle", "P2", "Delft blue white multi-strap platform stiletto sandals 8 inch", "extra long almond nails delft blue"),
     ("early 40s", "braided crown with blue ribbon", "Gzhel painted porcelain body art", "ROYAL BLUE single-stroke roses and swirling leaves shaded from deep to pale blue on a WHITE glaze base across torso and both legs to ankle", "P7", "Royal blue white peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails blue rose"),
     "Delft tile, Gzhel porcelain"),
    (124, "victoriantextile_acanthus", "Victorian Textile · Baroque Acanthus",
     ("mid 40s", "loose coily updo with a velvet band", "Victorian textile strawberry-and-thrush body art", "INDIGO base with RED strawberries, CREAM-SPECKLED thrushes, and GREEN leafy vines in symmetrical repeat across torso and both legs to ankle", "P4", "Indigo red knee-high lace-up platform stiletto boots 8 inch", "extra long oval nails strawberry red"),
     ("early 30s", "voluminous side-swept curls", "Baroque acanthus scroll body art", "BURNISHED GOLD curling acanthus leaves and C-scrolls across bust, belly, and both legs to ankle, DEEP BURGUNDY fills", "P3", "Gold burgundy d'Orsay platform stilettos 8 inch", "extra long stiletto nails burnished gold"),
     "Victorian strawberry textile, Baroque acanthus"),
    (125, "rococo_uvlaserharp", "Rococo · UV Laser Harp",
     ("late 30s", "powder-pink tinted high curls", "Rococo shell-and-scroll body art", "PASTEL PINK, MINT, and GOLD asymmetric rocaille shells, ribbons, and floral garlands across torso and both legs to ankle", "P5", "Pink mint platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long almond nails pastel gold"),
     ("early 20s", "UV-reactive green high ponytail", "UV laser harp beam body art", "ELECTRIC GREEN vertical laser beams fanning up from the ankles over legs and torso, VIVID RED beam-break flares at hips and bust, STARK WHITE haze points", "P1", "Green chrome mirror platform stilettos 8 inch", "extra long coffin nails laser green"),
     "Rococo shells, UV laser harp"),
    (126, "heraldic_tudorrose", "Heraldic Lion · Tudor Rose",
     ("early 50s", "silver sleek bob", "heraldic lion and fleur-de-lis body art", "GOLD rampant lions on a ROYAL BLUE field across bust and belly, SILVER fleur-de-lis and quartered shield bands both legs to ankle", "P1", "Royal blue gold caged platform stiletto sandals 8 inch", "extra long stiletto nails heraldic gold"),
     ("late 20s", "long braids with red ribbon", "Tudor rose body art", "CRIMSON and WHITE double-layered Tudor roses across bust and belly, GREEN leaves and GOLD crowns both legs to ankle", "P2", "Crimson white peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails rose crimson"),
     "heraldic lions, Tudor roses"),
    (127, "matyo_otomi", "Matyó · Otomi",
     ("early 30s", "braided crown with flower pins", "Hungarian Matyó embroidery body art", "CRIMSON, SUNFLOWER YELLOW, and ROYAL BLUE dense satin-stitch roses and tulips across torso and both legs to ankle", "P8", "Crimson blue multi-strap platform stiletto sandals 8 inch", "extra long almond nails embroidered rose"),
     ("mid 40s", "long black waves with a woven band", "Otomi embroidery body art", "BRIGHT PINK, ORANGE, TEAL, and PURPLE stylized deer, birds, rabbits, and flowers across torso and both legs to ankle", "P6", "Pink orange platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails otomi bird"),
     "Matyó embroidery, Otomi embroidery"),
    (128, "huichol_mola", "Huichol · Mola",
     ("late 20s", "beaded high puff", "Huichol yarn art body art", "CONCENTRIC YELLOW, MAGENTA, TURQUOISE, and ORANGE yarn-line deer, suns, and corn motifs across torso and both legs to ankle", "P3", "Yellow turquoise caged platform stiletto sandals 8 inch", "extra long stiletto nails yarn stripe"),
     ("early 50s", "silver braids with red cloth wraps", "Kuna mola reverse-appliqué body art", "layered RED, ORANGE, and BLACK cut-channel maze patterns with stylized birds and turtles across torso and both legs to ankle", "P4", "Red orange knee-high platform stiletto boots 8 inch", "extra long coffin nails mola red"),
     "Huichol yarn art, Kuna mola"),
    (129, "andean_uvlighttrail", "Andean Nazca · UV Light Trail",
     ("mid 30s", "two long braids with woven tassels", "Andean textile and Nazca line body art", "CRIMSON, MUSTARD, and EMERALD stepped woven bands on the torso, GOLD single-line hummingbird and spider geoglyphs on the belly and both legs to ankle", "P1", "Crimson mustard platform stiletto sandals with ribbon laces tied below the knee 8 inch", "extra long almond nails woven stripe"),
     ("late 40s", "UV-reactive red-orange tapered afro", "UV long-exposure light trail body art", "ELECTRIC RED and BLUE streaking light trails curving around bust, belly, and both legs like night traffic, VIVID WHITE headlight flares", "P7", "Red blue chrome mirror platform stilettos 8 inch", "extra long coffin nails light streak"),
     "Andean textile Nazca, UV light trails"),
    (130, "flytrap_reeffish", "Carnivorous Plants · Reef Fish",
     ("early 40s", "sleek black high bun with green pin", "carnivorous plant body art", "LIME and CRIMSON Venus flytraps, pitcher plants, and sundews across bust, belly, and both legs to ankle, GLISTENING dew dots", "P2", "Lime crimson peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long stiletto nails flytrap green"),
     ("mid 20s", "long aqua-tipped braids", "tropical reef fish body art", "ELECTRIC YELLOW tangs, ORANGE clownfish, and BLUE angelfish schooling across bust, belly, and both legs to ankle, AQUA water swirls", "P5", "Yellow aqua multi-strap platform stiletto sandals 8 inch", "extra long almond nails reef stripe"),
     "carnivorous plants, tropical reef fish"),
    (131, "cactusbloom_poppy", "Cactus Bloom · Poppy Field",
     ("late 30s", "voluminous curls with a pink flower", "desert cactus bloom body art", "SAGE GREEN saguaro and prickly pear with HOT PINK and YELLOW blooms across bust, belly, and both legs to ankle, SAND dune lines", "P1", "Sage pink platform gladiator stiletto sandals laced to mid-calf 8 inch", "extra long coffin nails cactus pink"),
     ("early 50s", "silver low bun with a red pin", "poppy field body art", "SCARLET poppies with black centers across bust and belly, GREEN wheat and BLUE cornflowers both legs to ankle", "P8", "Scarlet black d'Orsay platform stilettos 8 inch", "extra long oval nails poppy red"),
     "cactus bloom, poppy field"),
    (132, "sunflower_lavenderolive", "Sunflower Finch · Lavender Olive",
     ("early 20s", "golden-blonde afro", "sunflower and finch body art", "BLAZING YELLOW sunflowers with brown seed centers across bust and belly, GOLDFINCHES and GREEN leaves both legs to ankle", "P7", "Yellow brown caged platform stiletto sandals 8 inch", "extra long almond nails sunflower yellow"),
     ("mid 40s", "sleek black chignon with an olive sprig", "lavender and olive branch body art", "LAVENDER PURPLE flower spikes in rows up both legs, SILVER-GREEN olive branches with dark olives across bust and belly", "P3", "Lavender silver peep-toe platform stilettos with crossed ankle straps 8 inch", "extra long coffin nails lavender"),
     "sunflower finch, lavender olive"),
    (133, "redwood_orca", "Redwood Fog · Orca Glacier",
     ("late 40s", "long locs in a high crown", "redwood forest and fog body art", "RUST RED towering redwood trunks rising up both legs, DEEP GREEN canopy across bust, PALE GREY fog bands on the belly", "P4", "Rust green knee-high lace-up platform stiletto boots 8 inch", "extra long stiletto nails rust bark"),
     ("early 30s", "platinum-white sleek bob", "orca and glacier body art", "STARK WHITE and BLACK orca breaching across the belly, ICE BLUE glacier facets on bust and both legs to ankle, SILVER water", "P6", "Ice blue white chrome mirror platform stilettos 8 inch", "extra long coffin nails glacier blue"),
     "redwood fog, orca glacier"),
]

for num, slug, title, L, R, langs in D:
    add_duo(num, slug, title, fig("LEFT", *L), fig("RIGHT", *R), langs)

RATIO_RE = re.compile(r"\b(?:2:3|3:4|4:5)(?= vertical)")


def main() -> int:
    force = "--force" in sys.argv
    if not PRESETS_DIR.is_dir():
        print(f"[ERROR] presets dir not found: {PRESETS_DIR}")
        return 1
    keys = [k for k, _, _, _ in P]
    if len(keys) != len(set(keys)):
        print("[ERROR] duplicate keys")
        return 1

    written, skipped = 0, 0
    for key, title, prompt, aspect in P:
        path = PRESETS_DIR / f"{key}.json"
        if path.exists() and not force:
            print(f"[SKIP] exists: {path.name}")
            skipped += 1
            continue
        data = {
            "title": title,
            "category": CATEGORY,
            "platform": PLATFORM,
            "aspect_ratio": aspect,
            "prompt": RATIO_RE.sub(aspect, prompt.strip()),
        }
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        check = json.loads(path.read_text(encoding="utf-8-sig"))
        assert check["prompt"] and check["aspect_ratio"] == aspect
        print(f"[OK]   {path.name}")
        written += 1

    print(f"\nDone. written={written} skipped={skipped} total={len(P)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
