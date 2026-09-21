# -*- coding: utf-8 -*-
r"""
patch_livingartifact_colossal_jpcn_1_json.py
Living Artifact · Colossal — 24 solo presets
(Japan/China 4 materials: Kintsugi, Maki-e, Cloisonné, Ru-Guan x 3 standing + 3 seated)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_colossal_jpcn_1_json.py
    python preset_builders\patch_livingartifact_colossal_jpcn_1_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · Colossal"
PLATFORM = "gemini"
ASPECT = "2:3"

STAND = ("Physique: The most colossal SuperBBW physique physically possible — gigantic soft belly hanging in multiple "
         "deep overlapping rolls down toward the thighs, not pregnant, overwhelmingly massive heavy bust resting on the "
         "upper belly, extremely wide hips far wider than the shoulders, enormous thick thighs, very broad soft arms, "
         "profound physical volume filling the entire frame width.")


def seat(spread):
    return ("Physique: The most colossal SuperBBW physique physically possible — gigantic soft belly resting in multiple "
            "deep overlapping rolls over the thighs, not pregnant, overwhelmingly massive heavy bust resting on the upper "
            f"belly, extremely wide hips {spread}, enormous thick thighs, very broad soft arms, profound physical volume "
            "filling the entire frame width.")


ARMS = "Arms kept away from the torso so the painted bust and belly are fully visible."
END = "Emphasis on the extremely large SuperBBW body volume. 2:3 vertical 8K portrait."


def cover(extra=""):
    return ("The body painting is the only covering on the body — no garments, no fabric,"
            f"{extra} no robes, no bodysuit, no leggings, no stockings.")


def build(subject, physique, art, pose, foot, nails, bg):
    return "\n\n".join([
        f"Fine art body painting photography. Subject: {subject}",
        physique,
        f"Body Art: {art}",
        f"Pose: {pose} Full body head to toe visible.",
        f"Footwear: {foot}\nNails: {nails}",
        f"Background & Lighting: {bg} ONE woman only. Figure fills 90% of the frame. {END}",
    ])


KS = "Full body Kintsugi body painting from neck to ankle, painted directly on bare skin, one continuous surface."
MK = "Full body maki-e lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex."
CL = "Full body cloisonné enamel body painting in jingtailan style, from neck to ankle, painted directly on bare skin, one continuous surface, no collar band."
RG = "painted directly on bare skin, one continuous surface."
COV = "Pelvis, inner thighs, and both arms fully covered."
PAT = "Pelvis, inner thighs, and both arms fully patterned."
GLZ = "Pelvis, inner thighs, and both arms fully glazed and crackled."

P = []


def add(key, title, *args):
    P.append((key, title, build(*args)))


# ── Kintsugi ─────────────────────────────────────────────
add("la_colossal_kintsugi_01", "LA Colossal – Kintsugi 01 (Standing)",
    "ONE extremely large SuperBBW Japanese woman in her early 30s, glossy black blunt bob with razor-cut bangs, natural face with a confident smile.",
    STAND, f"{KS} {cover(' no kimono,')} High-gloss obsidian-black ceramic glaze with a dense network of many fine raised 24-karat gold repair seams catching the light across bust, belly rolls, hips, and legs. {COV}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Towering 9-inch gold mirror-chrome peep-toe platform stilettos with crossed ankle straps.",
    "Extra long stiletto nails, black with gold tips.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm gold key with raking side light making the gold seams glow.")
add("la_colossal_kintsugi_02", "LA Colossal – Kintsugi 02 (Standing)",
    "ONE extremely large SuperBBW Black woman in her late 20s, long knotless braids gathered to one side, natural face with a bright smile.",
    STAND, f"{KS} {cover()} High-gloss celadon-green ceramic glaze with a dense network of many fine raised gold repair seams. {COV}",
    f"Standing in a three-quarter front view, one arm extended gracefully out to the side at shoulder height, the other hand on her hip, chest open. {ARMS}",
    "Towering 9-inch caged celadon-glazed platform stiletto sandals with gold seams along each strap.",
    "Extra long coffin nails, celadon with gold crack lines.",
    "Contemporary ceramics gallery with mended vessels on white plinths, softly blurred. Low camera angle, 85mm lens. Soft gallery light with warm raking side light.")
add("la_colossal_kintsugi_03", "LA Colossal – Kintsugi 03 (Standing)",
    "ONE extremely large SuperBBW Norwegian woman in her early 40s, long pale blonde hair loose over the shoulders, natural face with a calm smile.",
    STAND, f"{KS} {cover()} High-gloss deep indigo-blue ceramic glaze with a dense network of many fine raised gold and silver repair seams. {COV}",
    "Standing in a three-quarter front view, both hands clasped loosely behind her lower back, shoulders drawn back, chest and belly facing the camera.",
    "Very high 8-inch indigo-glazed platform stiletto sandals with spiral straps coiling up the calf, gold-edged.",
    "Extra long almond nails, indigo with silver seam lines.",
    "Nordic rocky seashore under a soft overcast sky, softly blurred. Low camera angle, 135mm lens. Soft overcast light with warm raking side light, no direct sun.")
add("la_colossal_kintsugi_04", "LA Colossal – Kintsugi 04 (Seated)",
    "ONE extremely large SuperBBW Japanese woman in her mid-20s, long black hair in a high ponytail, natural face with a playful smile.",
    seat("spreading across the bench"), f"{KS} {cover(' no kimono,')} High-gloss milky ivory porcelain glaze clearly covering all skin, visibly different from natural skin tone, with a dense network of many fine raised gold repair lines. {COV}",
    f"Seated on a low wooden bench, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Very high 8-inch ivory-glazed platform stiletto thong sandals with a gold toe ring and a slim ankle strap.",
    "Extra long oval nails, ivory with gold tips.",
    "Kyoto tea house engawa with shoji screens and a moss garden, softly blurred. Low camera angle, 85mm lens. Soft window light with warm raking side light.")
add("la_colossal_kintsugi_05", "LA Colossal – Kintsugi 05 (Seated)",
    "ONE extremely large SuperBBW Mexican woman in her late 30s, long dark wavy hair with a side part, natural face with a warm smile.",
    seat("spreading across the stool"), f"{KS} {cover()} High-gloss deep rust-red raku ceramic glaze with smoky black patches and a dense network of many fine raised gold repair seams. {COV}",
    f"Seated upright on a round wooden stool, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Very high 8-inch rust-red glazed platform Mary Jane stilettos with gold buckles.",
    "Extra long coffin nails, rust red with gold crack line.",
    "Potter's studio with a wood kiln and shelves of raku bowls, softly blurred. Low camera angle, 85mm lens. Warm kiln glow with raking side light.")
add("la_colossal_kintsugi_06", "LA Colossal – Kintsugi 06 (Seated)",
    "ONE extremely large SuperBBW Korean woman in her late 40s, black shoulder-length hair tucked behind the ears, natural face with a composed smile.",
    seat("filling the armchair"), f"{KS} {cover()} Satin charcoal-grey stoneware glaze with a subtle sheen and a dense network of many fine raised gold repair seams. {COV}",
    f"Seated in a minimalist wooden armchair, torso turned open toward the camera, one forearm on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Towering 9-inch charcoal-glazed platform stiletto d'Orsay pumps with gold heels.",
    "Extra long almond nails, charcoal with gold seam.",
    "Minimal concrete gallery with a single spotlit mended vase, softly blurred. Low camera angle, 85mm lens. Warm spotlight with raking side light making the gold seams glow.")

# ── Maki-e ───────────────────────────────────────────────
add("la_colossal_makie_01", "LA Colossal – Maki-e 01 (Standing)",
    "ONE extremely large SuperBBW Japanese woman in her early 40s, glossy black hair in a soft chignon with a gold hairpin, natural face with a calm smile.",
    STAND, f"{MK} {cover(' no kimono,')} Deep glossy black urushi with natural highlights and subtle brush texture, fine sprinkled gold dust with individual particles visible forming a full moon, autumn grasses, and flying geese, crisp raised gold relief. {PAT}",
    f"Standing in a three-quarter front view, one hand lightly touching her hairpin at shoulder height, the other on her outer hip, torso turned open to the camera. {ARMS}",
    "Very high 8-inch knee-high lace-up black lacquer platform stiletto boots with gold-dust detailing and gold eyelets, visible boot edge.",
    "Extra long almond nails, black with gold powder tips.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm key with raking side light making the gold dust glitter.")
add("la_colossal_makie_02", "LA Colossal – Maki-e 02 (Standing)",
    "ONE extremely large SuperBBW Korean woman in her late 20s, straight black hair falling past the shoulders, natural face with a soft smile.",
    STAND, f"{MK} {cover()} Deep glossy black urushi with fine sprinkled gold dust forming sweeping waves, plovers, and chrysanthemums, crisp raised gold relief, minimal plain black areas. {PAT}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Extreme 10-inch black lacquer barely-there platform stilettos with two hairline gold straps.",
    "Extra long coffin nails, black with gold flakes.",
    "Snow-covered cedar forest with falling snow, softly blurred. Low camera angle, 135mm lens. Soft cool daylight bounced off the snow with warm raking side light.")
add("la_colossal_makie_03", "LA Colossal – Maki-e 03 (Standing)",
    "ONE extremely large SuperBBW Native Hawaiian woman in her mid-30s, long dark waves with a small gold flower pin, natural face with a warm smile.",
    STAND, f"{MK} {cover()} Deep glossy black urushi with fine sprinkled gold dust forming ocean waves, sea birds, and cherry blossoms, crisp raised gold relief. {PAT}",
    f"Standing in a three-quarter front view, one arm extended gracefully out to the side at shoulder height, the other hand on her hip, chest open. {ARMS}",
    "Towering 9-inch black lacquer platform gladiator stiletto sandals laced to mid-calf with gold-dust straps.",
    "Extra long stiletto nails, black with gold wave.",
    "Black volcanic sand beach at sunset, simple horizon, softly blurred. Low camera angle, 135mm lens. Warm low backlight with raking side light making the gold dust sparkle.")
add("la_colossal_makie_04", "LA Colossal – Maki-e 04 (Seated)",
    "ONE extremely large SuperBBW Japanese woman in her late 30s, black hair in a low bun with a lacquer comb, natural face with a knowing smile.",
    seat("filling the armchair"), f"{MK} {cover(' no kimono,')} Deep glossy black urushi with fine sprinkled gold dust forming irises, a wooden bridge, and flowing water, crisp raised gold relief. {PAT}",
    f"Seated in a low black lacquer armchair, torso turned open toward the camera, one forearm on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Towering 9-inch black lacquer peep-toe platform stilettos with a single gold ankle strap.",
    "Extra long oval nails, black with gold powder tips.",
    "Lacquer artist's studio with half-finished boxes and brushes, softly blurred. Low camera angle, 85mm lens. Warm window light with raking side light.")
add("la_colossal_makie_05", "LA Colossal – Maki-e 05 (Seated)",
    "ONE extremely large SuperBBW German woman in her early 20s, platinum chin-length bob, natural face with a playful smile.",
    seat("spreading across the block"), f"{MK} {cover()} Deep glossy black urushi with fine sprinkled gold dust forming maple leaves, deer, and a crescent moon, crisp raised gold relief. {PAT}",
    f"Seated on a low black block, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Towering 9-inch caged black lacquer platform stiletto sandals with gold-dust accents at each junction.",
    "Extra long coffin nails, black with gold glitter.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm key with raking side light and soft rim light.")
add("la_colossal_makie_06", "LA Colossal – Maki-e 06 (Seated)",
    "ONE extremely large SuperBBW Filipino woman in her late 40s, silver-streaked black bob, natural face with a gentle smile.",
    seat("spreading across the bench"), f"{MK} {cover()} Deep glossy black urushi with fine sprinkled gold dust forming wisteria clusters and butterflies, crisp raised gold relief. {PAT}",
    f"Seated upright on a low wooden bench, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Very high 8-inch black lacquer platform stiletto sandals with gold ribbon laces tied in a bow below the knee.",
    "Extra long almond nails, lavender with gold tips.",
    "Japanese garden with hanging wisteria at dusk, softly blurred. Low camera angle, 85mm lens. Warm lantern light with raking side light.")

# ── Cloisonné ────────────────────────────────────────────
add("la_colossal_cloisonne_01", "LA Colossal – Cloisonné 01 (Standing)",
    "ONE extremely large SuperBBW Chinese woman in her late 30s, black hair in a high sleek bun with a gold hairpin, natural face with a composed smile.",
    STAND, f"{CL} {cover(' no qipao,')} Glossy turquoise-blue enamel base divided by raised gold wire outlines, filled with lotus scrolls, peonies, and cloud bands in coral red, cobalt, and white. {PAT}",
    "Standing in a three-quarter front view, both hands clasped loosely behind her lower back, shoulders drawn back, chest and belly facing the camera.",
    "Very high 8-inch turquoise enamel platform T-strap stiletto sandals with raised gold wire on every strap.",
    "Extra long stiletto nails, turquoise with gold tips.",
    "Museum gallery of Ming cloisonné vessels in glass cases, softly blurred. Low camera angle, 85mm lens. Warm museum key with raking side light making the gold wires glow.")
add("la_colossal_cloisonne_02", "LA Colossal – Cloisonné 02 (Standing)",
    "ONE extremely large SuperBBW Latina woman in her late 20s, long dark voluminous curls, natural face with a bright smile.",
    STAND, f"{CL} {cover()} Glossy turquoise enamel base with raised gold wire cells filled with chrysanthemums, butterflies, and scrolling vines in coral, cobalt, green, and white. {PAT}",
    f"Standing in a three-quarter front view, one hand lifting her curls at shoulder height, the other on her outer hip, torso turned open to the camera. {ARMS}",
    "Very high 8-inch turquoise enamel platform stiletto sandals with multiple thin gold-edged straps across the instep.",
    "Extra long coffin nails, coral with gold tips.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Warm key with raking side light and soft rim light.")
add("la_colossal_cloisonne_03", "LA Colossal – Cloisonné 03 (Standing)",
    "ONE extremely large SuperBBW Russian woman in her early 40s, sleek black chin-length bob, natural face with a confident smile.",
    STAND, f"{CL} {cover()} Glossy deep cobalt enamel base with raised gold wire cells filled with dragons among clouds and waves in turquoise, coral, and white. {PAT}",
    f"Standing in a three-quarter front view, both hands on her wide hips with elbows out, shoulders back and chest open. {ARMS}",
    "Very high 8-inch cobalt enamel pointed platform stiletto ankle booties with gold wire detailing.",
    "Extra long almond nails, cobalt with gold line.",
    "Huangshan cliff terrace above a sea of clouds, softly blurred. Low camera angle, 135mm lens. Soft morning light through mist with raking side light.")
add("la_colossal_cloisonne_04", "LA Colossal – Cloisonné 04 (Seated)",
    "ONE extremely large SuperBBW Chinese woman in her early 20s, long straight black hair with a jade clip, natural face with a sweet smile.",
    seat("spreading across the stool"), f"{CL} {cover(' no qipao,')} Glossy turquoise enamel base with raised gold wire cells filled with lotus, goldfish, and water ripples. {PAT}",
    f"Seated upright on a carved stone garden stool, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Very high 8-inch turquoise enamel platform Mary Jane stilettos with gold wire buckles.",
    "Extra long oval nails, turquoise with coral dots.",
    "Classical Suzhou garden with a lotus pond and moon gate, softly blurred. Low camera angle, 85mm lens. Soft daylight with warm raking side light.")
add("la_colossal_cloisonne_05", "LA Colossal – Cloisonné 05 (Seated)",
    "ONE extremely large SuperBBW Korean woman in her late 40s, black hair in a low chignon with a gold pin, natural face with a gentle smile.",
    seat("filling the armchair"), f"{CL} {cover()} Glossy turquoise enamel base with raised gold wire cells filled with peonies, magpies, and plum branches. {PAT}",
    f"Seated in a rosewood armchair, torso turned open toward the camera, one forearm on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Very high 8-inch turquoise enamel platform stiletto sandals with gold spiral straps coiling up the calf.",
    "Extra long coffin nails, turquoise with gold.",
    "Ming scholar's study with rosewood furniture and scroll paintings, softly blurred. Low camera angle, 85mm lens. Warm window light with raking side light.")
add("la_colossal_cloisonne_06", "LA Colossal – Cloisonné 06 (Seated)",
    "ONE extremely large SuperBBW Black woman in her mid-30s, short natural afro with gold rings, natural face with a radiant smile.",
    seat("spreading across the block"), f"{CL} {cover()} Glossy turquoise enamel base with raised gold wire cells filled with phoenixes, lotus, and cloud bands in coral, cobalt, and white. {PAT}",
    f"Seated on a low white block, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Towering 9-inch turquoise enamel peep-toe platform stilettos with crossed gold ankle straps.",
    "Extra long stiletto nails, gold chrome.",
    "Minimal white gallery with pale plinths, softly blurred. Low camera angle, 85mm lens. Soft high-key light with raking side light, strong color contrast against white.")

# ── Ru-Guan ──────────────────────────────────────────────
NK = "no painted motifs, not kintsugi."
add("la_colossal_ru_guan_01", "LA Colossal – Ru-Guan 01 (Standing)",
    "ONE extremely large SuperBBW Chinese woman in her early 40s, black hair in a soft low chignon with a pale jade pin, natural face with a serene smile.",
    STAND, f"Full body Song dynasty Ru-Guan celadon body painting from neck to ankle, {RG} {cover()} High-gloss deep saturated sky-blue-grey glaze clearly different from skin, with a fine dense crackle of thin dark lines and finer golden secondary crackle, soft uneven reflections, {NK} {GLZ}",
    f"Standing in a three-quarter front view, one arm extended gracefully out to the side at shoulder height, the other hand on her hip, chest open. {ARMS}",
    "Towering 9-inch caged sky-blue crackle-glazed platform stiletto sandals.",
    "Extra long almond nails, pale blue with fine crackle.",
    "Quiet Song ceramics gallery with pale celadon bowls in glass cases, softly blurred. Low camera angle, 85mm lens. Soft cool museum light with warm raking side light.")
add("la_colossal_ru_guan_02", "LA Colossal – Ru-Guan 02 (Standing)",
    "ONE extremely large SuperBBW Finnish woman in her late 20s, silvery ash-blonde hair in a low bun, natural face with a calm smile.",
    STAND, f"Full body Guan ware celadon body painting from neck to ankle, {RG} {cover()} High-gloss deep grey-green glaze clearly different from skin, with a bold network of dark crackle lines and fine secondary crackle, {NK} {GLZ}",
    "Standing in a three-quarter front view, both hands clasped loosely behind her lower back, shoulders drawn back, chest and belly facing the camera.",
    "Towering 9-inch grey-green crackle-glazed platform stiletto d'Orsay pumps.",
    "Extra long oval nails, grey-green.",
    "Frozen lake shore under a pale winter sky, softly blurred. Low camera angle, 135mm lens. Soft overcast light with warm raking side light.")
add("la_colossal_ru_guan_03", "LA Colossal – Ru-Guan 03 (Standing)",
    "ONE extremely large SuperBBW Indonesian woman in her mid-30s, long dark waves, natural face with a warm smile.",
    STAND, f"Full body Ru ware celadon body painting from neck to ankle, {RG} {cover()} High-gloss deep saturated duck-egg blue glaze clearly different from skin, with a fine dense crackle of thin dark lines, {NK} {GLZ}",
    f"Standing in a three-quarter front view, one hand lifting her hair at shoulder height, the other on her outer hip, torso turned open to the camera. {ARMS}",
    "Very high 8-inch duck-egg blue glazed platform stiletto sandals with multiple thin straps across the instep.",
    "Extra long coffin nails, pale blue.",
    "MANDATORY seamless matte black studio background. Low camera angle, 85mm lens. Cool key with warm raking side light and soft rim light.")
add("la_colossal_ru_guan_04", "LA Colossal – Ru-Guan 04 (Seated)",
    "ONE extremely large SuperBBW Chinese woman in her early 50s, silver-streaked black bob, natural face with gentle smile lines.",
    seat("filling the armchair"), f"Full body Guan ware celadon body painting from neck to ankle, {RG} {cover()} High-gloss deep pale grey-green glaze clearly different from skin, with a fine dense crackle of thin dark lines, {NK} {GLZ}",
    f"Seated in a rosewood armchair, torso turned open toward the camera, one forearm on the armrest, the other hand on her thigh, legs crossed at the knee. {ARMS}",
    "Towering 9-inch grey-green crackle-glazed peep-toe platform stilettos with a single ankle strap.",
    "Extra long almond nails, pale celadon.",
    "Hangzhou garden pavilion with a misty lake, softly blurred. Low camera angle, 85mm lens. Soft diffused daylight with warm raking side light.")
add("la_colossal_ru_guan_05", "LA Colossal – Ru-Guan 05 (Seated)",
    "ONE extremely large SuperBBW Japanese woman in her early 20s, black hair in two low braids, natural face with a playful smile.",
    seat("spreading across the bench"), f"Full body Ru-Guan celadon body painting from neck to ankle, {RG} {cover()} High-gloss deep saturated sky-blue glaze clearly different from skin, with a fine dense crackle of thin dark lines and golden secondary crackle, {NK} {GLZ}",
    f"Seated on a low wooden bench, leaning back slightly with both hands planted behind her, chest open and belly relaxed forward, legs crossed at the knee. {ARMS}",
    "Very high 8-inch sky-blue crackle-glazed platform stiletto thong sandals with a slim ankle strap.",
    "Extra long oval nails, sky blue.",
    "Minimal white gallery with pale plinths, softly blurred. Low camera angle, 85mm lens. Soft high-key light with raking side light, strong contrast against white.")
add("la_colossal_ru_guan_06", "LA Colossal – Ru-Guan 06 (Seated)",
    "ONE extremely large SuperBBW Lebanese woman in her late 30s, voluminous black waves, natural face with kohl-lined eyes and a warm smile.",
    seat("spreading across the stool"), f"Full body Ru ware celadon body painting from neck to ankle, {RG} {cover()} High-gloss deep saturated blue-green glaze clearly different from skin, with a bold network of dark crackle lines and fine secondary crackle, {NK} {GLZ}",
    f"Seated upright on a round stone stool, torso facing the camera, legs crossed at the knee, both hands resting lightly on her upper knee with elbows relaxed out. {ARMS}",
    "Very high 8-inch blue-green crackle-glazed platform stiletto sandals with ribbon laces tied in a bow below the knee.",
    "Extra long coffin nails, blue-green.",
    "Contemporary ceramics museum hall with celadon vessels on plinths, softly blurred. Low camera angle, 85mm lens. Soft museum light with warm raking side light.")

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
