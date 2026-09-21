# -*- coding: utf-8 -*-
r"""
patch_livingartifact_craft_solo_c_outdoor_json.py
Living Artifact — Craft Solo (C) 5 presets + Craft Outdoor 8 presets

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_craft_solo_c_outdoor_json.py
    python preset_builders\patch_livingartifact_craft_solo_c_outdoor_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CAT_SOLO = "🏺 Living Artifact · Craft Solo"
CAT_OUT = "🏺 Living Artifact · Craft Outdoor"
PLATFORM = "gemini"
ASPECT = "2:3"

P1 = ("Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly hanging "
      "in deep overlapping rolls, overwhelmingly massive heavy bust, extremely wide hips, enormous thick thighs, very broad "
      "soft arms, profound physical volume filling the entire frame width.")
P1_NP = P1.replace("very broad soft arms,", "very broad soft arms, not pregnant,")


def p1_seat(spread):
    return ("Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly "
            f"resting in deep rolls above the thighs, overwhelmingly massive heavy bust, extremely wide hips {spread}, "
            "enormous thick thighs, very broad soft arms, profound physical volume filling the frame.")


OUT_P = ("Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly hanging "
         "in deep rolling folds, not pregnant, overwhelmingly massive heavy bust, extremely wide hips, enormous thick "
         "thighs, very broad soft arms")
OUT_BIG = OUT_P + ", belly and hips dominating the frame."
OUT_STD = OUT_P + "."


def build(subject, physique, art, pose, foot, bg, light, lens="85mm lens"):
    return "\n\n".join([
        f"Subject: {subject}",
        physique,
        f"Body Art: {art}",
        f"Pose: {pose} Full body head to toe visible.",
        f"Footwear: {foot}",
        f"Background & Lighting: {bg} ONE woman only. Figure fills 90% of the frame, low camera angle, {lens}. "
        f"{light} Emphasis on the extremely large SuperBBW body volume. 2:3 vertical 8K portrait.",
    ])


def build_out(subject, physique, art, pose, foot, bg, light):
    return "\n\n".join([
        f"Subject: {subject}",
        physique,
        f"Body Art: {art}",
        f"Pose: {pose} Full body head to toe visible.",
        f"Footwear: {foot}",
        f"Background & Lighting: {bg} ONE woman only. Figure fills 90% of the frame, low camera angle, 135mm lens. "
        f"{light} 2:3 vertical 8K portrait.",
    ])


P = []  # (key, title, category, prompt)

# ── Craft Solo C ─────────────────────────────────────────
P.append(("la_craft_solo_zhostovo_palace", "LA Craft Solo – Zhostovo (Palace Drawing Room)", CAT_SOLO, build(
    "ONE extremely large SuperBBW Russian woman in her early 50s, honey-blonde hair in a braided crown with a small gold pin, natural face with a warm smile.",
    P1,
    "Full body Zhostovo lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer with natural highlights and subtle brush texture, covered in lush hand-painted bouquets of roses, peonies, and daisies in crimson, pink, cream, and green with luminous shaded petals, framed by fine gold scroll borders at wrists and ankles. Pelvis, inner thighs, and both arms fully painted and patterned, no bare skin gaps. Authentic Russian Zhostovo style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly over the back leg, one hand on her wide hip, the other at her collarbone.",
    "8-inch black lacquer platform stilettos with painted rose details and gold trim.\nNails: Extra long almond nails, black with painted rose tips.",
    "Russian imperial drawing room with silk walls and a samovar on a side table, softly blurred.",
    "Warm chandelier key with raking side light making the lacquer gleam.")))
P.append(("la_craft_solo_palekh_studio", "LA Craft Solo – Palekh (Studio Seated)", CAT_SOLO, build(
    "ONE extremely large SuperBBW Russian woman in her late 30s, long dark auburn hair in a single thick braid over one shoulder, natural face with a calm smile.",
    p1_seat("spreading across the seat"),
    "Full body Palekh miniature lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer with natural highlights, densely filled with fine gold-line folk-tale scenes — a blazing firebird with fiery red and gold feathers across the bust, galloping white horses and onion-dome towers across the belly, and gold filigree vines and flowers wrapping the hips and legs. Pelvis, inner thighs, and both arms fully painted and patterned. Authentic Russian Palekh style.",
    "Seated on a tall black cube with hips angled slightly to the right, torso turned back toward the camera, legs crossed at the knee, far hand on the cube behind her, near hand resting on her knee.",
    "8-inch black lacquer platform ankle-strap stilettos with gold firebird details.\nNails: Extra long stiletto nails, black with fine gold line tips.",
    "MANDATORY seamless matte black studio background.",
    "Warm narrow spotlight with raking side light making the gold lines shimmer.")))
P.append(("la_craft_solo_olinala", "LA Craft Solo – Olinalá Rayado Lacquer", CAT_SOLO, build(
    "ONE extremely large SuperBBW Mexican woman in her mid-40s, long black hair in two braids woven with red ribbons, natural face with a joyful smile.",
    P1,
    "Full body Olinalá rayado lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Glossy two-layer lacquer: a deep black top coat carved away to reveal vivid vermilion beneath, forming stylized birds, rabbits, deer, flowers, and scrolling leaves with crisp etched edges, densely covering bust, belly rolls, hips, and legs. Pelvis, inner thighs, and both arms fully patterned, no bare skin gaps. Authentic Mexican Guerrero style.",
    "Standing with hips turned slightly to the right and chest angled toward the camera, front leg crossed slightly in front, one hand on her waist, the other touching a braid.",
    "8-inch black-and-vermilion lacquer platform stilettos with etched bird details.\nNails: Extra long coffin nails, black with vermilion etched tips.",
    "Rustic Olinalá artisan workshop with carved lacquered chests and adobe walls, softly blurred.",
    "Warm window light with raking side light across the carved lacquer.")))
P.append(("la_craft_solo_kashmiri", "LA Craft Solo – Kashmiri Papier-mâché", CAT_SOLO, build(
    "ONE extremely large SuperBBW Kashmiri woman in her early 60s, silver-streaked black hair in a low bun with a small gold ornament, natural face with a gentle smile.",
    p1_seat("spreading across the cushions"),
    "Full body Kashmiri papier-mâché painting from neck to ankle, painted directly on bare skin, one continuous surface. High-gloss varnished finish with a deep indigo base densely covered in brightly painted chinar leaves, roses, irises, and small birds in crimson, emerald, and saffron, outlined with raised gold leaf. Pelvis, inner thighs, and both arms fully painted and patterned, no bare skin gaps. No religious figures. Authentic Kashmiri style.",
    "Seated on a low carved walnut divan with hips angled slightly to the left, torso turned back toward the camera, legs crossed at the knee, far hand on a cushion behind her, near hand resting on her knee.",
    "7-inch indigo lacquer platform Mary Jane stilettos with gold chinar leaf details.\nNails: Extra long almond nails, indigo with gold tips.",
    "Carved walnut interior of a Srinagar houseboat with lake views, softly blurred.",
    "Soft lake daylight with warm raking side light making the gold leaf glow.")))
P.append(("la_craft_solo_rishtan", "LA Craft Solo – Rishtan Ceramics", CAT_SOLO, build(
    "ONE extremely large SuperBBW Uzbek woman in her late 20s, long black hair in many thin braids with a small embroidered cap ornament, natural face with a bright smile.",
    P1_NP,
    "Full body Rishtan ceramic body painting from neck to ankle, painted directly on bare skin, one continuous surface. High-gloss deep turquoise ishkor glaze base with dense cobalt, white, and ochre pomegranates, almond shapes, and swirling floral medallions, fine glaze crackle and soft uneven reflections. Pelvis, inner thighs, and both arms fully painted and patterned, no bare skin gaps. Authentic Uzbek style.",
    "Standing with hips turned slightly to the left and shoulders angled toward the camera, front leg crossed slightly over the back leg, one hand on her wide hip, the other lifting a braid.",
    "8-inch turquoise glazed platform stilettos with cobalt pomegranate details.\nNails: Extra long almond nails, turquoise with cobalt tips.",
    "Registan square in Samarkand with blue-tiled madrasa portals at golden hour, softly blurred.",
    "Warm late-afternoon sun with raking side light across the glaze.", lens="135mm lens")))

# ── Craft Outdoor ────────────────────────────────────────
P.append(("la_craft_outdoor_najeon_black_beach", "LA Craft Outdoor – Black Najeon · Sunset Beach", CAT_OUT, build_out(
    "ONE extremely large SuperBBW Korean woman in her mid-30s, long black hair loose in the sea breeze with a mother-of-pearl binyeo, natural face with a calm smile.",
    OUT_BIG,
    "Full body najeon-chilgi body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex, subtle brush texture and skin creases beneath the shine. Deep glossy black lacquer with iridescent pink-green-blue mother-of-pearl moon, cranes, waves, and clouds. Pelvis, inner thighs, and both arms fully patterned.",
    "Standing on wet sand in a soft three-quarter front view, gentle weight shift, one hand holding her hair against the breeze, the other relaxed at her side.",
    "Caged black lacquer platform stiletto sandals, a lattice of thin glossy straps over the foot and ankle with mother-of-pearl accents at each junction, 8-inch platform stilettos. Nails: black with pearl tips.",
    "Empty East Sea beach at sunset, wet sand mirroring the sky, simple horizon, no other people.",
    "Warm low backlight with soft bounce from the wet sand, raking side light making the mother-of-pearl flash rainbow.")))
P.append(("la_craft_outdoor_celadon_bamboo", "LA Craft Outdoor – Celadon Sanggam · Misty Bamboo Forest", CAT_OUT, build_out(
    "ONE extremely large SuperBBW Korean woman in her late 20s, black hair in a low braid with a jade pin, natural face with a serene smile.",
    OUT_STD,
    "Full body Goryeo celadon body painting from neck to ankle, painted directly on bare skin, one continuous surface. High-gloss jade-green celadon glaze with fine crackle and soft uneven reflections, black-and-white sanggam cranes and chrysanthemums. Pelvis, inner thighs, and both arms fully patterned.",
    "Standing on a stone path in a soft three-quarter front view, head tilted slightly, one hand resting on her belly, the other lightly touching a bamboo stalk.",
    "Celadon-glazed platform stiletto sandals with ribbon laces wrapping up the calf and tied in a soft bow below the knee, fine crackle finish, 8-inch platform stilettos. Nails: celadon with white tips.",
    "Misty Damyang bamboo forest, tall green stalks receding into fog, no other people.",
    "Soft overcast diffused light with gentle raking side light across the glaze, no harsh highlights.")))
P.append(("la_craft_outdoor_makie_snow", "LA Craft Outdoor – Maki-e · Snowy Cedar Forest", CAT_OUT, build_out(
    "ONE extremely large SuperBBW Japanese woman in her late 30s, glossy black hair in a soft chignon with a gold kanzashi, natural face with a quiet smile, warm breath visible in the cold air.",
    OUT_BIG,
    "Full body maki-e lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black urushi with fine sprinkled gold dust with individual particles visible, forming a full moon, snow-laden pines, and flying cranes, crisp raised gold relief. Pelvis, inner thighs, and both arms fully patterned.",
    "Standing in fresh snow in a soft three-quarter front view, one knee gently bent, holding a closed folding fan at her side, the other hand at her collarbone.",
    "Knee-high lace-up black lacquer platform stiletto boots with gold-dust maki-e detailing and gold eyelets laced from ankle to knee, boots clearly distinct from the painted legs with a visible boot edge. Nails: black with gold powder tips.",
    "Snow-covered cedar forest in Japan, white ground and dark trunks, falling snow, no other people.",
    "Soft cool daylight bounced off the snow with warm raking side light making the gold dust sparkle against the black.")))
P.append(("la_craft_outdoor_cloisonne_huangshan", "LA Craft Outdoor – Cloisonné · Huangshan Sea of Clouds", CAT_OUT, build_out(
    "ONE extremely large SuperBBW Chinese woman in her early 40s, black hair in a high sleek bun with a gold hairpin, natural face with a composed smile.",
    OUT_STD,
    "Full body cloisonné enamel body painting in Ming jingtailan style, from neck to ankle, painted directly on bare skin, one continuous surface, no collar band. Glossy turquoise enamel base divided by raised gold wire outlines, filled with lotus scrolls, peonies, and cloud bands in coral red, cobalt, and white. Pelvis, inner thighs, and both arms fully patterned.",
    "Standing on a stone terrace in a soft three-quarter front view, gentle weight shift, both hands resting lightly on her belly, gazing toward the camera.",
    "Turquoise enamel platform T-strap stiletto sandals with raised gold wire outlining every strap and a gold ankle buckle, 8-inch platform stilettos. Nails: turquoise with gold tips.",
    "Huangshan cliff terrace above a sea of clouds, pine silhouettes and pale mist, no other people.",
    "Soft morning light through mist with gentle raking side light making the gold wires glint.")))
P.append(("la_craft_outdoor_khokhloma_birch", "LA Craft Outdoor – Khokhloma · Autumn Birch Grove", CAT_OUT, build_out(
    "ONE extremely large SuperBBW Russian woman in her late 20s, long honey-blonde hair in a loose side braid, natural face with a sweet smile.",
    OUT_BIG,
    "Full body Khokhloma lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Glossy black and gold lacquer with dense hand-painted red rowan berries, golden leaves, and curling grass scrolls. Pelvis, inner thighs, and both arms fully painted.",
    "Walking slowly through fallen leaves toward the camera in three-quarter front view, a relaxed gentle step, arms swaying softly.",
    "Black-and-gold lacquer platform gladiator stiletto sandals laced to mid-calf with painted red rowan berries along each strap, painted legs visible between the straps. Nails: gold with red tips.",
    "Russian birch grove in autumn, white trunks and golden leaves, no other people.",
    "Low warm afternoon sun filtering through the trees with raking side light making the gold lacquer glow.")))
P.append(("la_craft_outdoor_minakari_dunes", "LA Craft Outdoor – Minakari · Desert Dunes", CAT_OUT, build_out(
    "ONE extremely large SuperBBW Iranian woman in her mid-40s, long dark waves with a thin gold headband, natural face with kohl-lined eyes and a gentle smile.",
    OUT_STD,
    "Full body Persian minakari enamel body painting from neck to ankle, painted directly on bare skin, one continuous surface, no collar band. Glossy deep cobalt and turquoise enamel base with fine gold outlines, filled with birds, roses, and arabesque vines in white, red, and green. Pelvis, inner thighs, and both arms fully patterned.",
    "Standing on a sand ridge in a soft three-quarter front view, weight on one leg, one hand lifting her hair from her shoulder, the other resting on her hip.",
    "Cobalt enamel platform stiletto sandals with multiple thin straps across the instep, fine gold arabesque outlines on every strap and a gold ankle strap, 8-inch platform stilettos. Nails: cobalt with gold tips.",
    "Empty desert dunes at golden hour, smooth sand curves and a clean sky, no other people.",
    "Warm low sun with strong raking side light across the enamel, cool shadow fill from the sky.")))
P.append(("la_craft_outdoor_lairodnam_waterfall", "LA Craft Outdoor – Lai Rod Nam · Tropical Waterfall", CAT_OUT, build_out(
    "ONE extremely large SuperBBW Thai woman in her early 30s, glossy black hair in a high topknot with a small gold ornament, natural face with a warm smile.",
    OUT_BIG,
    "Full body Thai lai rod nam lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black lacquer with bright gold-leaf kranok flame scrolls, lotus buds, and naga serpents densely covering the body, no religious figures. Pelvis, inner thighs, and both arms fully patterned.",
    "Standing on a flat wet rock in a graceful three-quarter front view, gentle weight shift, one hand held softly beside her shoulder in a slow Thai dance gesture, the other on her hip.",
    "Black lacquer peep-toe platform stiletto sandals with gold-leaf kranok patterns and crossed ankle straps, 9-inch platform stilettos. Nails: black with gold tips.",
    "Tropical waterfall in deep jungle shade, white water and dark wet rock, fine mist in the air, no other people.",
    "Soft shaded daylight with a warm raking side light making the gold leaf glow against the black lacquer.")))
P.append(("la_craft_outdoor_sonmai_terraces", "LA Craft Outdoor – Son Mai · Rice Terraces", CAT_OUT, build_out(
    "ONE extremely large SuperBBW Vietnamese woman in her mid-30s, long straight black hair past the waist, natural face with a bright smile.",
    OUT_STD,
    "Full body Vietnamese son mai lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Deep glossy black and vermilion lacquer with gold-leaf lotus, silver-leaf cranes, and crackled white eggshell mosaic clouds clearly visible. Pelvis, inner thighs, and both arms fully patterned.",
    "Standing on a narrow earth ridge in a soft three-quarter front view, one hand sweeping her long hair back, the other resting on her hip, head slightly tilted.",
    "Black lacquer platform stiletto thong sandals with a gold-leaf lotus at the toe ring and a thin slingback strap, 8-inch platform stilettos. Nails: black with eggshell-white tips.",
    "Sapa terraced rice fields at sunset, curved green terraces and flooded paddies reflecting the sky, no other people.",
    "Warm low sun with soft bounce from the flooded fields, raking side light.")))

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
    for key, title, cat, prompt in P:
        path = PRESETS_DIR / f"{key}.json"
        if path.exists() and not force:
            print(f"[SKIP] exists: {path.name}")
            skipped += 1
            continue
        data = {
            "title": title,
            "category": cat,
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
