# -*- coding: utf-8 -*-
r"""
patch_livingartifact_muscle_duo_1_json.py
Living Artifact · Muscle — 12 duo presets (muscular type x extreme SuperBBW)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_muscle_duo_1_json.py
    python preset_builders\patch_livingartifact_muscle_duo_1_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · Muscle"
PLATFORM = "gemini"
ASPECT = "3:4"

HEAD = ("Fine art body painting photography. TWO {who} standing side by side in three-quarter front view, "
        "clear space between them, no touching. Two completely different body types — do not average them, "
        "do not make them similar.")

SBBW = ("Around 800 pounds, body almost as wide as it is tall below the chest. Massive apron belly hanging in two "
        "stacked heavy aprons down to her knees, not pregnant, gigantic heavy bust resting on the upper belly, hips "
        "each wider than a normal woman's whole torso, huge thighs pressed together with deep folds, enormous soft "
        "upper arms hanging away from the body, deep side rolls past the silhouette. Not curvy, not a plus-size model.")

MASS = ("6 feet 4 inches tall and around 330 pounds of dense muscle, the biggest muscular woman physically possible. "
        "Shoulders wider than a doorway, gigantic round boulder delts, traps swelling into a thick neck, enormous "
        "swollen arms thicker than a normal woman's thighs, massive barrel chest, lats spreading like wings, blocky "
        "abs, gigantic tree-trunk quadriceps, massive calves. Full, thick, dense, swollen muscle — not shredded, not slim.")

PRO_BB = ("The most muscular competition physique possible — boulder delts with deep striations, peaked biceps with "
          "thick veins, horseshoe triceps, huge chest plates, wide flaring lats, deeply carved eight-pack abs, "
          "separated quad heads with a deep teardrop, diamond calves, paper-thin skin with every fiber visible. "
          "Not slim, not a fitness model.")


def both(extra_no=""):
    return ("Both: body painting painted directly on bare skin from neck to ankle, one continuous surface, the only "
            f"covering — no garments, no fabric,{extra_no} no bodysuit, not latex. Underarms, inner arms, pelvis, and "
            "inner thighs fully painted. Each material strictly separate.")


def cam(bg, light):
    return (f"Background & Lighting: {bg} TWO women only. Camera straight-on at waist height, 35mm lens, both bodies "
            f"filling the frame edge to edge. {light} Emphasis on both extreme bodies. 3:4 vertical 8K portrait.")


PRESETS = [
    {
        "key": "la_muscle_duo_massmonster_kintsugi_x_makie",
        "title": "LA Muscle Duo – Mass Monster Kintsugi × SuperBBW Maki-e",
        "prompt": "\n\n".join([
            HEAD.format(who="Japanese women"),
            "LEFT — colossal muscular mass monster: early 30s, glossy black hair slicked back into a tight low bun, intense focused expression. " + MASS + " Body art: high-gloss obsidian-black Kintsugi glaze with raised 24-karat gold repair seams running along the major muscle borders, like a shattered bronze statue mended with gold. Pose: front lat spread, fists pressed into the waist, lats flared, chest lifted, chest and abs fully visible. 9-inch gold mirror-chrome peep-toe platform stilettos with crossed ankle straps. Extra long stiletto nails, black with gold tips.",
            "RIGHT — true extreme SuperBBW: late 30s, glossy black hair in a soft chignon with a gold hairpin, very full round face with a double chin and a calm smile. " + SBBW + " Body art: deep glossy black urushi maki-e with fine sprinkled gold dust forming a full moon, autumn grasses, and flying geese across every roll, minimal plain black. Pose: full frontal, both hands resting on top of her belly, shoulders back, chest and belly fully visible. 8-inch black lacquer caged platform stiletto sandals with gold-dust accents. Extra long almond nails, black with gold powder tips.",
            both(" no kimono,"),
            cam("MANDATORY seamless matte black studio background.", "Hard raking side light carving the muscle masses on the left and the heavy rolls on the right, warm gold key making the seams and gold dust glow, thin rim light tracing both silhouettes."),
        ]),
    },
    {
        "key": "la_muscle_duo_massmonster_palekh_x_zhostovo",
        "title": "LA Muscle Duo – Mass Monster Palekh × SuperBBW Zhostovo",
        "prompt": "\n\n".join([
            HEAD.format(who="Russian women"),
            "LEFT — colossal muscular mass monster: late 20s, dark auburn hair in a tight high braid, fierce grin. " + MASS + " Body art: deep glossy black Palekh lacquer with fine gold-line firebird across the chest, troika horses over the abs, onion domes and gold filigree following the contours of the shoulders, arms, and legs. Pose: one arm raised to shoulder height and bent, flexing a gigantic biceps, the other fist on her hip, chest and abs fully visible. 9-inch black lacquer platform gladiator stiletto sandals laced to mid-calf with gold firebird details. Extra long coffin nails, black with gold line.",
            "RIGHT — true extreme SuperBBW: early 40s, honey-blonde braided crown, very full round face with a double chin and a warm smile. " + SBBW + " Body art: deep glossy black Zhostovo lacquer covered in lush painted rose and peony bouquets in crimson, pink, and cream, gold scroll borders at wrists and ankles. Pose: feet together with a soft hip shift, both hands gently framing her face with elbows low, chest and belly fully visible. 8-inch black lacquer d'Orsay platform stilettos with painted roses. Extra long almond nails, black with rose tips.",
            both(),
            cam("Russian imperial ballroom with gilded mouldings and chandeliers, softly blurred.", "Hard raking side light carving the muscle masses on the left and the heavy rolls on the right, warm chandelier key."),
        ]),
    },
    {
        "key": "la_muscle_duo_bodybuilder_najeon_x_celadon",
        "title": "LA Muscle Duo – Pro Bodybuilder Black Najeon × SuperBBW Celadon",
        "prompt": "\n\n".join([
            HEAD.format(who="Korean women"),
            "LEFT — shredded professional bodybuilder: early 30s, black hair in a tight low bun with a mother-of-pearl binyeo, intense expression. " + PRO_BB + " Body art: deep glossy black najeon lacquer inlaid with iridescent pink-green-blue mother-of-pearl cranes and pine, the inlay flashing on every muscle peak. Pose: front lat spread, fists pressed into the waist, lats flared, chest lifted, chest and abs fully visible. 9-inch black lacquer caged platform stiletto sandals with pearl accents. Extra long almond nails, black with pearl tips.",
            "RIGHT — true extreme SuperBBW: early 40s, long black hair in a low braid with a jade pin, very full round face with a double chin and a serene smile. " + SBBW + " Body art: high-gloss jade-green Goryeo celadon glaze clearly covering all skin, fine crackle, black-and-white sanggam cranes and chrysanthemums across every roll. Pose: full frontal, both hands resting on top of her belly, shoulders back, chest and belly fully visible. 8-inch celadon platform stiletto sandals with ribbon laces tied below the knee. Extra long coffin nails, celadon with white tips.",
            both(" no hanbok,"),
            cam("Hanok daecheong hall with paper lattice doors and a white moon jar, softly blurred.", "Hard raking side light carving the muscles on the left and the heavy rolls on the right, warm window fill."),
        ]),
    },
    {
        "key": "la_muscle_duo_physique_gamji_x_najeon_vermilion",
        "title": "LA Muscle Duo – Physique Gamji-geumni × SuperBBW Vermilion Najeon",
        "prompt": "\n\n".join([
            HEAD.format(who="Korean women"),
            "LEFT — women's physique competitor: late 20s, long black hair in a single low braid, confident expression. An aesthetic V-taper physique — very wide rounded shoulders, broad sweeping lats, tiny tight waist, sharp six-pack abs, capped arms with clear biceps and triceps separation, full muscular chest, sweeping quads and defined hamstrings, athletic calves. Muscular and dramatic, not slim, not a bikini model. Body art: glossy deep navy-indigo gamji-geumni base, not purple, with bold gold ink lotus scrolls and cloud bands, fine gold lines tracing each muscle separation, no religious figures. Pose: front double biceps, both arms raised to shoulder height and bent, biceps peaked, chest open, chest and abs fully visible. 8-inch indigo lacquer T-strap platform stiletto sandals with fine gold lines. Extra long almond nails, indigo with gold tips.",
            "RIGHT — true extreme SuperBBW: mid 40s, black hair in a sleek high bun with a coral binyeo, very full round face with a double chin and a bright smile. " + SBBW + " Body art: deep glossy vermilion lacquer clearly different from skin, inlaid with iridescent mother-of-pearl phoenixes, peonies, and clouds. Pose: full frontal, both fists on her hips, elbows out, chest and belly fully visible. 9-inch vermilion lacquer peep-toe platform stilettos with crossed ankle straps. Extra long coffin nails, vermilion with pearl tips.",
            both(" no hanbok,"),
            cam("MANDATORY seamless matte black studio background.", "Hard raking side light making the gold lines shimmer and the mother-of-pearl flash, thin rim light tracing both silhouettes."),
        ]),
    },
    {
        "key": "la_muscle_duo_massmonster_makie_x_kintsugi_celadon",
        "title": "LA Muscle Duo – Mass Monster Maki-e × SuperBBW Kintsugi Celadon",
        "prompt": "\n\n".join([
            HEAD.format(who="Japanese women"),
            "LEFT — colossal offseason mass monster: early 30s, glossy black hair slicked into a tight low bun, intense expression. " + MASS + " Body art: deep glossy black urushi maki-e with fine sprinkled gold dust forming sweeping waves and chrysanthemums that wrap the huge muscles, minimal plain black. Pose: one arm raised to shoulder height and bent, flexing a gigantic biceps, the other fist on her hip, chest and abs fully visible. 8-inch knee-high lace-up black lacquer platform stiletto boots with gold-dust detailing, visible boot edge. Extra long stiletto nails, black with gold powder tips.",
            "RIGHT — true extreme SuperBBW: late 30s, short silver-streaked black bob, very full round face with a double chin and a warm smile. " + SBBW + " Body art: high-gloss celadon-green ceramic glaze with a dense network of many fine raised gold Kintsugi repair seams following every roll and fold. Pose: feet together with a soft hip shift, both hands gently framing her face with elbows low, chest and belly fully visible. 9-inch gold mirror-chrome peep-toe platform stilettos with crossed ankle straps. Extra long almond nails, celadon with gold crack lines.",
            both(" no kimono,"),
            cam("Kyoto tea house with shoji screens and a moss garden, softly blurred.", "Hard raking side light carving the muscle masses on the left and the heavy rolls on the right, warm gold key making the gold dust and seams glow."),
        ]),
    },
    {
        "key": "la_muscle_duo_powerlifter_cloisonne_x_ru_guan",
        "title": "LA Muscle Duo – Powerlifter Cloisonné × SuperBBW Ru-Guan",
        "prompt": "\n\n".join([
            HEAD.format(who="Chinese women"),
            "LEFT — super heavyweight powerlifter: late 30s, black hair in a high sleek bun with a gold hairpin, determined expression. Around 350 pounds of raw power — a colossal thick back and traps, huge dense shoulders, enormous forearms and arms, a thick solid waist with a powerful belly, gigantic glutes and hips, massive tree-trunk thighs built for squatting, thick powerful calves. Enormous strength with some softness over dense muscle. Not lean, not a fitness model. Body art: glossy turquoise jingtailan cloisonné enamel divided by raised gold wire cells filled with lotus scrolls and cloud bands in coral, cobalt, and white, no collar band. Pose: full frontal in a wide planted squat-ready stance, both fists on her hips, shoulders squared, chest and belly fully visible. 8-inch turquoise enamel multi-strap platform stiletto sandals with raised gold wire. Extra long stiletto nails, turquoise with gold tips.",
            "RIGHT — true extreme SuperBBW: early 30s, long straight black hair with a jade clip, very full round face with a double chin and a soft smile. " + SBBW + " Body art: high-gloss deep saturated sky-blue-grey Ru-Guan celadon glaze clearly different from skin, fine dense crackle of thin dark lines, no painted motifs, not kintsugi. Pose: full frontal, hands clasped loosely behind her lower back, chest and belly fully visible. 9-inch sky-blue crackle-glazed caged platform stiletto sandals. Extra long almond nails, pale blue.",
            both(" no qipao,"),
            cam("Museum gallery of Ming cloisonné and Song celadon in glass cases, softly blurred.", "Hard raking side light carving the power on the left and the heavy rolls on the right, warm museum key."),
        ]),
    },
    {
        "key": "la_muscle_duo_strongwoman_khokhloma_x_palekh",
        "title": "LA Muscle Duo – Strongwoman Khokhloma × SuperBBW Palekh",
        "prompt": "\n\n".join([
            HEAD.format(who="Russian women"),
            "LEFT — extreme strongwoman: mid 30s, platinum-blonde hair in a thick side braid, proud grin. Massively thick and powerful — huge trapezius rising toward the ears, broad thick shoulders, enormous arms, thick strong waist with a solid belly, massive powerful thighs and glutes, heavy muscle under a layer of softness, a body built for lifting stones and pulling trucks. Not lean, not a fitness model. Body art: deep glossy black and gold Khokhloma lacquer with bold red rowan berries, golden leaves, and curling grass scrolls wrapping the thick limbs. Pose: full frontal in a wide powerful stance, one arm raised to shoulder height and bent flexing the biceps, the other fist on her hip, chest and belly fully visible. 9-inch black-and-gold lacquer platform gladiator stiletto sandals laced to mid-calf. Extra long coffin nails, gold with red tips.",
            "RIGHT — true extreme SuperBBW: late 20s, dark auburn hair in a thick braid over one shoulder, very full round face with a double chin and a bright smile. " + SBBW + " Body art: deep glossy black Palekh lacquer with fine gold-line firebird on the bust, troika horses and onion domes across the belly rolls, gold filigree on the legs. Pose: full frontal, both hands resting on top of her belly, shoulders back, chest and belly fully visible. 8-inch black lacquer spiral-strap platform stiletto sandals with gold firebird heels. Extra long stiletto nails, black with gold line.",
            both(),
            cam("Russian imperial hall with gilded mouldings and chandeliers, softly blurred.", "Hard raking side light carving the muscles on the left and the heavy rolls on the right, warm chandelier key."),
        ]),
    },
    {
        "key": "la_muscle_duo_amazon_minakari_x_zhostovo",
        "title": "LA Muscle Duo – Amazon Minakari × SuperBBW Zhostovo",
        "prompt": "\n\n".join([
            HEAD.format(who="women"),
            "LEFT — towering amazon: Iranian woman in her late 20s, long dark waves with a thin gold headband, regal fierce expression. 6 feet 8 inches tall, a giant athletic warrior build — long powerful limbs, broad square shoulders, sculpted muscular arms, wide back, strong defined abs, long muscular thighs and calves, towering over the frame. Muscular and statuesque, not slim, not a runway model. Body art: glossy cobalt and turquoise Persian minakari enamel with fine gold outlines, birds, roses, and arabesque vines tracing the long muscles, no collar band. Pose: standing tall, one arm extended to the side at shoulder height, the other hand on her hip, chest and abs fully visible. 9-inch cobalt enamel platform stiletto sandals with spiral straps coiling up the calf. Extra long stiletto nails, cobalt with gold tips.",
            "RIGHT — true extreme SuperBBW: Russian woman in her late 30s, honey-blonde braided crown, very full round face with a double chin and a warm smile. " + SBBW + " Body art: deep glossy black Zhostovo lacquer covered in lush painted rose and peony bouquets with gold scroll borders. Pose: feet together with a soft hip shift, both hands gently framing her face with elbows low, chest and belly fully visible. 8-inch black lacquer d'Orsay platform stilettos with painted roses. Extra long almond nails, black with rose tips.",
            both(),
            "Background & Lighting: Grand palace-style decorative arts gallery with marble columns and gilded display cases, softly blurred. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light, warm chandelier key. Emphasis on the towering height on the left and the colossal width on the right. 3:4 vertical 8K portrait.",
        ]),
    },
    {
        "key": "la_muscle_duo_musclebbw_lairodnam_x_sonmai",
        "title": "LA Muscle Duo – Extreme Muscle BBW Lai Rod Nam × SuperBBW Son Mai",
        "prompt": "\n\n".join([
            HEAD.format(who="women"),
            "LEFT — extreme muscular SuperBBW: Thai woman in her mid-30s, glossy black hair in a high topknot with a small gold ornament, bold grin. Around 550 pounds, built like a super heavyweight strongwoman crossed with a sumo wrestler — enormous thick trapezius, colossal rounded shoulders, gigantic arms with huge biceps visible under heavy softness, massive bust over a huge round belly with soft rolls on a powerful thick core, not pregnant, gigantic tree-trunk thighs with visible quad sweep under the fat. Both colossal fat volume and colossal muscle at once. Firm and hard, clearly more muscular than the soft woman beside her. Body art: deep glossy black lai rod nam lacquer with bright gold-leaf kranok flames and naga scrolls wrapping the huge limbs, no religious figures. Pose: full frontal in a wide stance, one arm raised to shoulder height flexing a gigantic biceps, the other fist on her hip, chest and belly fully visible. 9-inch black lacquer peep-toe platform stilettos with crossed gold ankle straps. Extra long curved stiletto nails, black with gold tips.",
            "RIGHT — true extreme SuperBBW: Vietnamese woman in her late 20s, straight black hair falling to her waist, very full round face with a double chin and a warm smile. " + SBBW + " Body art: crackled white eggshell inlay clearly visible as mosaic clouds, set in deep glossy black son mai lacquer with vermilion accents, gold-leaf lotus, and silver-leaf cranes. Pose: full frontal, both hands resting on top of her belly, shoulders back, chest and belly fully visible. 8-inch black lacquer caged platform stiletto sandals with gold-leaf lotus. Extra long almond nails, black with eggshell-white tips.",
            both(),
            cam("MANDATORY seamless matte black studio background.", "Hard raking side light revealing muscle beneath the volume on the left and the soft rolls on the right, warm gold key and thin rim light."),
        ]),
    },
    {
        "key": "la_muscle_duo_sumo_kintsugi_x_najeon",
        "title": "LA Muscle Duo – Sumo Kintsugi × SuperBBW Black Najeon",
        "prompt": "\n\n".join([
            HEAD.format(who="women"),
            "LEFT — sumo wrestler build: Japanese woman in her early 40s, black hair in a tight topknot, calm powerful expression. Around 500 pounds, a sumo champion's body — a huge firm round belly over a powerful core, massive thick thighs and a low heavy center of gravity, broad dense shoulders and heavy arms, thick powerful neck. Solid, heavy, and strong rather than soft, not pregnant. Firm and hard, clearly more muscular than the soft woman beside her. Body art: high-gloss obsidian-black ceramic glaze with bold raised 24-karat gold Kintsugi repair seams crossing the round belly and thick limbs. Pose: full frontal in a wide low stance, knees slightly bent, both hands resting on her thighs, torso upright, chest and belly fully visible. 8-inch black lacquer platform gladiator stiletto sandals laced to mid-calf with gold seams. Extra long coffin nails, black with gold crack line.",
            "RIGHT — true extreme SuperBBW: Korean woman in her late 30s, silver-streaked black hair in a low bun with a mother-of-pearl binyeo, very full round face with a double chin and a calm smile. " + SBBW + " Body art: deep glossy black najeon lacquer inlaid with iridescent pink-green-blue mother-of-pearl full moon, cranes, and waves across every roll. Pose: full frontal, hands clasped loosely behind her lower back, chest and belly fully visible. 9-inch black lacquer caged platform stiletto sandals with pearl accents. Extra long almond nails, black with pearl tips.",
            both(" no mawashi, no belt,"),
            cam("MANDATORY seamless matte black studio background.", "Hard raking side light, warm gold key making the seams glow and the mother-of-pearl flash, thin rim light."),
        ]),
    },
    {
        "key": "la_muscle_duo_crossfit_celadon_x_gamji",
        "title": "LA Muscle Duo – CrossFit Celadon × SuperBBW Gamji-geumni",
        "prompt": "\n\n".join([
            HEAD.format(who="Korean women"),
            "LEFT — thick CrossFit athlete: late 20s, black hair in a high ponytail with a jade clasp, energetic smile. A dense functional athlete build — thick rounded shoulders, strong capped arms, powerful back, visible abs with a solid core, huge muscular glutes and quads, thick strong calves. Powerful and thick, not lean, not slim. Body art: high-gloss jade-green Goryeo celadon glaze clearly covering all skin, fine crackle, black-and-white sanggam cranes and clouds wrapping the muscles. Pose: three-quarter front, one hand touching her ponytail at shoulder height, the other hand on her hip, chest and abs fully visible. 8-inch celadon platform stiletto sandals with ribbon laces tied below the knee. Extra long almond nails, celadon with white tips.",
            "RIGHT — true extreme SuperBBW: late 40s, black hair in a low jjok-meori bun with a gold binyeo, very full round face with a double chin and a gentle smile. " + SBBW + " Body art: glossy deep navy-indigo gamji-geumni, not purple, with bold dense gold ink lotus medallion on the belly, vine scrolls on the bust, cloud bands on the legs, no religious figures. Pose: full frontal, both hands resting on top of her belly, shoulders back, chest and belly fully visible. 8-inch indigo lacquer T-strap platform stiletto sandals with gold lines. Extra long coffin nails, indigo with gold tips.",
            both(" no hanbok,"),
            cam("Joseon royal library with indigo-and-gold manuscripts and paper lattice windows, softly blurred.", "Hard raking side light, warm lamp key making the gold lines shimmer."),
        ]),
    },
    {
        "key": "la_muscle_duo_thrower_ru_guan_x_cloisonne",
        "title": "LA Muscle Duo – Shot Put Thrower Ru-Guan × SuperBBW Cloisonné",
        "prompt": "\n\n".join([
            HEAD.format(who="Chinese women"),
            "LEFT — elite shot put thrower: early 30s, black hair in a tight high bun, focused expression. Around 280 pounds, an explosive thrower's build — massive round shoulders, a thick powerful chest, huge throwing arm and forearms, a thick solid waist, enormous explosive thighs and glutes, powerful calves. Big, dense, and athletic, not lean, not a fitness model. Body art: high-gloss deep saturated sky-blue-grey Ru-Guan celadon glaze clearly different from skin, fine dense crackle of thin dark lines, no painted motifs, not kintsugi — like a monumental glazed statue of an athlete. Pose: full frontal, one arm raised to shoulder height and bent showing the huge biceps, the other fist on her hip, chest and belly fully visible. 8-inch sky-blue crackle-glazed caged platform stiletto sandals. Extra long almond nails, pale blue.",
            "RIGHT — true extreme SuperBBW: early 40s, black hair in a high sleek bun with a gold hairpin, very full round face with a double chin and a composed smile. " + SBBW + " Body art: glossy turquoise jingtailan cloisonné enamel divided by raised gold wire cells filled with lotus scrolls and peonies in coral, cobalt, and white, no collar band. Pose: full frontal, hands clasped loosely behind her lower back, chest and belly fully visible. 8-inch turquoise enamel multi-strap platform stiletto sandals with raised gold wire. Extra long stiletto nails, turquoise with gold tips.",
            both(" no qipao,"),
            cam("Ming scholar's study with rosewood furniture and scroll paintings, softly blurred.", "Hard raking side light, warm window key making the gold wires glint."),
        ]),
    },
]

RATIO_RE = re.compile(r"\b(?:2:3|3:4|4:5)(?= vertical)")


def normalize_prompt(text: str) -> str:
    return RATIO_RE.sub(ASPECT, text.strip())


def main() -> int:
    force = "--force" in sys.argv
    if not PRESETS_DIR.is_dir():
        print(f"[ERROR] presets dir not found: {PRESETS_DIR}")
        return 1
    keys = [p["key"] for p in PRESETS]
    if len(keys) != len(set(keys)):
        print("[ERROR] duplicate keys in PRESETS")
        return 1

    written, skipped = 0, 0
    for p in PRESETS:
        path = PRESETS_DIR / f"{p['key']}.json"
        if path.exists() and not force:
            print(f"[SKIP] exists: {path.name}")
            skipped += 1
            continue
        data = {
            "title": p["title"],
            "category": CATEGORY,
            "platform": PLATFORM,
            "aspect_ratio": ASPECT,
            "prompt": normalize_prompt(p["prompt"]),
        }
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        check = json.loads(path.read_text(encoding="utf-8-sig"))
        assert check["prompt"] and check["aspect_ratio"] == ASPECT
        print(f"[OK]   {path.name}")
        written += 1

    print(f"\nDone. written={written} skipped={skipped} total={len(PRESETS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
