# -*- coding: utf-8 -*-
r"""
patch_livingartifact_ceramic_1_json.py
Living Artifact · Ceramic Collection — 10 duo presets
(same glaze x4, different glaze x6; muscular x extreme SuperBBW)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_ceramic_1_json.py
    python preset_builders\patch_livingartifact_ceramic_1_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · Ceramic Collection"
PLATFORM = "gemini"
ASPECT = "3:4"

SBBW = ("Around 800 pounds, body almost as wide as it is tall below the chest. Massive apron belly hanging "
        "in two stacked heavy aprons down to her knees, not pregnant, gigantic heavy bust resting on the upper "
        "belly, hips each wider than a normal woman's whole torso, huge thighs pressed together with deep folds, "
        "enormous soft upper arms, deep side rolls. Not curvy, not a plus-size model.")

PRESETS = [
    # ── Same glaze ────────────────────────────────────────────
    {
        "key": "la_ceramic_duo_same_celadon",
        "title": "LA Ceramic Duo – Celadon × Celadon (Bodybuilder / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO Korean women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them. The same Goryeo celadon glaze on both bodies, like two celadon statues from the same kiln.

LEFT — shredded professional bodybuilder: early 30s, black hair in a tight low bun with a jade binyeo, intense expression. Boulder delts with striations, peaked biceps with veins, horseshoe triceps, huge chest plates, flaring lats, deeply carved eight-pack abs, separated quad heads, diamond calves. Not slim, not a fitness model. Pose: front lat spread, fists on the waist, chest lifted, chest and abs fully visible. 8-inch celadon caged platform stiletto sandals. Extra long almond nails, celadon with white tips.

RIGHT — true extreme SuperBBW: early 40s, long black hair in a low braid with a jade pin, very full round face with a double chin and a serene smile. {SBBW} Pose: full frontal, both hands resting on top of her belly, chest and belly fully visible. 8-inch celadon platform stiletto sandals with ribbon laces tied below the knee. Extra long coffin nails, celadon.

Both: high-gloss jade-green celadon glaze clearly covering all skin from neck to ankle, fine crackle and soft uneven reflections, black-and-white sanggam cranes and clouds in round medallions. Painted directly on bare skin, one continuous surface, the only covering — no garments, no fabric, no hanbok, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed.

Background & Lighting: Korean ceramics gallery with celadon maebyeong vases, softly blurred. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light across the glaze — carving muscles on the left, catching every roll on the right. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_ceramic_duo_same_kintsugi_black",
        "title": "LA Ceramic Duo – Kintsugi Black × Kintsugi Black (Mass Monster / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO Japanese women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them. The same Kintsugi glaze on both bodies, like two broken vessels mended by the same hand.

LEFT — colossal offseason mass monster: early 30s, glossy black hair slicked into a tight low bun, intense expression. 6 feet 4 inches and around 330 pounds of dense muscle — shoulders wider than a doorway, boulder delts, traps swelling into a thick neck, arms thicker than a normal woman's thighs, barrel chest, lats like wings, blocky abs, tree-trunk quads. Full, thick, swollen — not shredded, not slim. Gold seams follow the muscle borders. Pose: one arm raised to shoulder height flexing a gigantic biceps, other fist on hip, chest and abs fully visible. 9-inch gold mirror-chrome peep-toe platform stilettos with crossed ankle straps. Extra long stiletto nails, black with gold tips.

RIGHT — true extreme SuperBBW: late 30s, glossy black blunt bob with bangs, very full round face with a double chin and a calm smile. {SBBW} Gold seams follow every roll and fold. Pose: feet together with a soft hip shift, both hands gently framing her face with elbows low, chest and belly fully visible. 8-inch black lacquer caged platform stiletto sandals with gold accents. Extra long almond nails, black with gold crack line.

Both: high-gloss obsidian-black ceramic glaze with a dense network of raised 24-karat gold Kintsugi repair seams. Painted directly on bare skin from neck to ankle, one continuous surface, the only covering — no garments, no fabric, no kimono, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed.

Background & Lighting: MANDATORY seamless matte black studio background. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light, warm gold key making the seams glow, thin rim light tracing both silhouettes. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_ceramic_duo_same_ru_guan",
        "title": "LA Ceramic Duo – Ru-Guan × Ru-Guan (Strongwoman / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO Chinese women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them. The same Song dynasty Ru-Guan glaze on both bodies.

LEFT — extreme strongwoman: mid 30s, black hair in a tight high bun, proud grin. Massively thick and powerful — huge trapezius rising toward the ears, broad thick shoulders, enormous arms, thick strong waist with a solid belly, massive powerful thighs and glutes, heavy muscle under a layer of softness. Not lean, not a fitness model. Pose: full frontal in a wide powerful stance, both fists on her hips, chest and belly fully visible. 8-inch sky-blue crackle-glazed platform gladiator stiletto sandals laced to mid-calf. Extra long coffin nails, pale blue.

RIGHT — true extreme SuperBBW: late 20s, long straight black hair with a jade clip, very full round face with a double chin and a soft smile. {SBBW} Pose: full frontal, hands clasped loosely behind her lower back, chest and belly fully visible. 9-inch sky-blue crackle-glazed caged platform stiletto sandals. Extra long almond nails, pale blue with fine crackle.

Both: high-gloss deep saturated sky-blue-grey glaze clearly different from skin, fine dense crackle of thin dark lines with golden secondary crackle, soft uneven reflections, no painted motifs, not kintsugi. Painted directly on bare skin from neck to ankle, one continuous surface, the only covering — no garments, no fabric, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed.

Background & Lighting: Quiet Song ceramics gallery with pale celadon bowls in glass cases, softly blurred. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light across the crackled glaze, cool museum fill. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_ceramic_duo_same_qinghua",
        "title": "LA Ceramic Duo – Blue-and-White × Blue-and-White (Physique / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO Chinese women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them. The same blue-and-white porcelain on both bodies.

LEFT — women's physique competitor: late 20s, black hair in a sleek high ponytail, confident expression. Aesthetic V-taper — very wide rounded shoulders, broad sweeping lats, tight waist, sharp six-pack, capped arms, full muscular chest, sweeping quads. Muscular and dramatic, not slim, not a bikini model. Pose: front double biceps, both arms raised to shoulder height and bent, chest open, chest and abs fully visible. 8-inch white porcelain platform stiletto sandals with cobalt-painted T-straps. Extra long almond nails, white with cobalt tips.

RIGHT — true extreme SuperBBW: mid 40s, black hair in a low chignon with a porcelain pin, very full round face with a double chin and a gentle smile. {SBBW} Pose: full frontal, both hands resting on top of her belly, chest and belly fully visible. 8-inch white porcelain d'Orsay platform stilettos with cobalt lotus. Extra long coffin nails, cobalt blue.

Both: high-gloss milky white porcelain glaze clearly covering all skin, visibly different from natural skin tone, with deep cobalt-blue lotus scrolls, waves, and cloud bands densely painted from neck to ankle. Painted directly on bare skin, one continuous surface, the only covering — no garments, no fabric, no qipao, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed.

Background & Lighting: MANDATORY seamless matte black studio background for strong contrast with the white glaze. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light across the porcelain, thin rim light. 3:4 vertical 8K portrait.""",
    },
    # ── Different glaze ───────────────────────────────────────
    {
        "key": "la_ceramic_duo_celadon_kintsugi_celadon",
        "title": "LA Ceramic Duo – Celadon × Kintsugi Celadon (Powerlifter / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them.

LEFT — super heavyweight powerlifter: Korean woman in her late 30s, black hair in a low bun with a jade binyeo, determined expression. Around 350 pounds of raw power — colossal thick back and traps, huge dense shoulders, enormous arms, thick solid waist with a powerful belly, gigantic glutes, massive tree-trunk thighs. Not lean, not a fitness model. Body art: high-gloss jade-green Goryeo celadon glaze clearly covering all skin, fine crackle, black-and-white sanggam cranes and chrysanthemums. Pose: full frontal in a wide planted stance, both fists on her hips, chest and belly fully visible. 8-inch celadon platform gladiator stiletto sandals laced to mid-calf. Extra long almond nails, celadon.

RIGHT — true extreme SuperBBW: Japanese woman in her early 30s, glossy black blunt bob, very full round face with a double chin and a warm smile. {SBBW} Body art: high-gloss celadon-green ceramic glaze with a dense network of raised gold Kintsugi repair seams following every roll, no painted motifs. Pose: feet together with a soft hip shift, both hands gently framing her face, chest and belly fully visible. 9-inch gold mirror-chrome peep-toe platform stilettos. Extra long coffin nails, celadon with gold crack line.

Both: painted directly on bare skin from neck to ankle, one continuous surface, the only covering — no garments, no fabric, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed. Two green glazes clearly distinct — inlaid motifs on the left, gold seams only on the right.

Background & Lighting: Contemporary ceramics gallery with celadon and mended vessels on plinths, softly blurred. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light, warm gold key. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_ceramic_duo_ru_guan_qinghua",
        "title": "LA Ceramic Duo – Ru-Guan × Blue-and-White (Amazon / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO Chinese women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them.

LEFT — towering amazon: late 20s, long straight black hair loose, fierce calm expression. 6 feet 8 inches tall, a giant athletic warrior build — long powerful limbs, broad square shoulders, sculpted arms, wide back, strong abs, long muscular thighs and calves. Muscular and statuesque, not a runway model. Body art: high-gloss deep saturated sky-blue-grey Ru-Guan glaze clearly different from skin, fine dense crackle of thin dark lines, no painted motifs. Pose: standing tall, one arm extended to the side at shoulder height, the other hand on her hip, chest and abs fully visible. 9-inch sky-blue crackle-glazed platform stiletto sandals with spiral straps up the calf. Extra long stiletto nails, pale blue.

RIGHT — true extreme SuperBBW: late 30s, black hair in a low chignon with a porcelain pin, very full round face with a double chin and a gentle smile. {SBBW} Body art: high-gloss milky white porcelain glaze clearly covering all skin, deep cobalt-blue peony scrolls and dragons among clouds densely painted. Pose: full frontal, hands clasped loosely behind her lower back, chest and belly fully visible. 8-inch white porcelain d'Orsay platform stilettos with cobalt trim. Extra long coffin nails, cobalt.

Both: painted directly on bare skin from neck to ankle, one continuous surface, the only covering — no garments, no fabric, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed. Each glaze strictly separate.

Background & Lighting: Ming palace ceramics hall with dark rosewood shelves, softly blurred. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light, warm museum key. Emphasis on the towering height on the left and the colossal width on the right. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_ceramic_duo_tenmoku_celadon",
        "title": "LA Ceramic Duo – Jian Tenmoku × Celadon (Bodybuilder / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them.

LEFT — shredded professional bodybuilder: Chinese woman in her early 30s, black hair in a tight low bun, intense expression. Boulder delts with striations, peaked biceps with veins, horseshoe triceps, huge chest plates, flaring lats, deeply carved eight-pack abs, separated quad heads, diamond calves. Not slim, not a fitness model. Body art: high-gloss deep black-brown Jian ware tenmoku glaze with silvery oil-spot droplets and iridescent blue halos scattered across every muscle, like a living Song tea bowl. Pose: front lat spread, fists on the waist, chest lifted, chest and abs fully visible. 8-inch black-brown glazed caged platform stiletto sandals with silver-spot accents. Extra long stiletto nails, black with silver dots.

RIGHT — true extreme SuperBBW: Korean woman in her early 40s, long black hair in a low braid with a jade pin, very full round face with a double chin and a serene smile. {SBBW} Body art: high-gloss jade-green Goryeo celadon glaze clearly covering all skin, fine crackle, black-and-white sanggam cranes and clouds. Pose: full frontal, both hands resting on top of her belly, chest and belly fully visible. 8-inch celadon platform stiletto sandals with ribbon laces tied below the knee. Extra long almond nails, celadon.

Both: painted directly on bare skin from neck to ankle, one continuous surface, the only covering — no garments, no fabric, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed. Each glaze strictly separate.

Background & Lighting: East Asian ceramics gallery with tea bowls and celadon vases, softly blurred. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light making the oil spots shimmer and the celadon glow. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_ceramic_duo_kintsugi_black_famille_rose",
        "title": "LA Ceramic Duo – Kintsugi Black × Famille Rose (Sumo / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them.

LEFT — sumo wrestler build: Japanese woman in her early 40s, black hair in a tight topknot, calm powerful expression. Around 500 pounds, a sumo champion's body — a huge firm round belly over a powerful core, massive thick thighs and a low heavy center of gravity, broad dense shoulders, heavy arms, thick neck. Solid and strong rather than soft, not pregnant. Body art: high-gloss obsidian-black ceramic glaze with bold raised 24-karat gold Kintsugi seams crossing the round belly and thick limbs. Pose: full frontal in a wide low stance, knees slightly bent, both hands resting on her thighs, torso upright, chest and belly fully visible. 8-inch black lacquer platform gladiator stiletto sandals laced to mid-calf with gold seams. Extra long coffin nails, black with gold crack line.

RIGHT — true extreme SuperBBW: Chinese woman in her late 20s, black hair in a soft low bun with a pink peony pin, very full round face with a double chin and a sweet smile. {SBBW} Body art: glossy milky white famille rose porcelain glaze clearly covering all skin, with soft pastel enamel peonies, butterflies, and flowering branches in pink, lavender, and green. Pose: feet together with a soft hip shift, both hands gently framing her face, chest and belly fully visible. 8-inch white porcelain platform stiletto sandals with pastel peony straps. Extra long almond nails, soft pink.

Both: painted directly on bare skin from neck to ankle, one continuous surface, the only covering — no garments, no fabric, no mawashi, no belt, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed. Each glaze strictly separate.

Background & Lighting: MANDATORY seamless matte black studio background. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light, warm gold key making the seams glow and the porcelain gleam, thin rim light. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_ceramic_duo_celadon_moonjar_kintsugi",
        "title": "LA Ceramic Duo – Celadon × Moon Jar Kintsugi (CrossFit / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO Korean women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them.

LEFT — thick CrossFit athlete: late 20s, black hair in a high ponytail with a jade clasp, energetic smile. A dense functional build — thick rounded shoulders, strong capped arms, powerful back, visible abs with a solid core, huge muscular glutes and quads, thick calves. Powerful and thick, not slim. Body art: high-gloss jade-green Goryeo celadon glaze clearly covering all skin, fine crackle, black-and-white sanggam willows, reeds, and waterfowl. Pose: three-quarter front, one hand touching her ponytail at shoulder height, the other on her hip, chest and abs fully visible. 8-inch celadon T-strap platform stiletto sandals. Extra long almond nails, celadon.

RIGHT — true extreme SuperBBW: late 40s, black hair in a low jjok-meori bun with a silver binyeo, very full round face with a double chin and a calm smile — her round body echoing a Joseon moon jar. {SBBW} Body art: high-gloss milky ivory Joseon white porcelain glaze clearly covering all skin, visibly different from natural skin tone, with a dense network of fine raised gold Kintsugi repair lines. Pose: full frontal, both hands resting on top of her belly, chest and belly fully visible. 8-inch ivory porcelain d'Orsay platform stilettos with gold heels. Extra long coffin nails, ivory with gold line.

Both: painted directly on bare skin from neck to ankle, one continuous surface, the only covering — no garments, no fabric, no hanbok, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed. Each glaze strictly separate.

Background & Lighting: Hanok gallery room with a white moon jar and celadon vases on low tables, softly blurred. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light, warm window fill making the gold lines glow. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_ceramic_duo_kintsugi_black_ru_guan",
        "title": "LA Ceramic Duo – Kintsugi Black × Ru-Guan (Muscle BBW / SuperBBW)",
        "prompt": f"""Fine art body painting photography. TWO women standing side by side in three-quarter front view, clear space between them, no touching. Two completely different body types — do not average them.

LEFT — extreme muscular SuperBBW: Japanese woman in her mid-30s, glossy black hair in a high topknot, bold grin. Around 550 pounds, built like a super heavyweight strongwoman crossed with a sumo wrestler — enormous thick trapezius, colossal shoulders, gigantic arms with huge biceps visible under heavy softness, massive bust over a huge round belly on a powerful core, not pregnant, tree-trunk thighs with visible quad sweep under the fat. Firm and hard, clearly more muscular than the soft woman beside her. Body art: high-gloss obsidian-black ceramic glaze with bold raised 24-karat gold Kintsugi seams tracing the muscle masses. Pose: full frontal in a wide stance, one arm raised to shoulder height flexing a gigantic biceps, the other fist on her hip, chest and belly fully visible. 9-inch gold mirror-chrome peep-toe platform stilettos. Extra long stiletto nails, black with gold tips.

RIGHT — true extreme SuperBBW: Chinese woman in her early 30s, long straight black hair with a jade clip, very full round face with a double chin and a serene smile. {SBBW} Body art: high-gloss deep saturated sky-blue-grey Ru-Guan glaze clearly different from skin, fine dense crackle of thin dark lines, no painted motifs, not kintsugi. Pose: full frontal, hands clasped loosely behind her lower back, chest and belly fully visible. 9-inch sky-blue crackle-glazed caged platform stiletto sandals. Extra long almond nails, pale blue.

Both: painted directly on bare skin from neck to ankle, one continuous surface, the only covering — no garments, no fabric, no bodysuit. Underarms, inner arms, pelvis, and inner thighs fully glazed. Each glaze strictly separate.

Background & Lighting: Minimal concrete gallery with a single spotlit mended vase and a Song celadon bowl, softly blurred. TWO women only. Camera straight-on at waist height, 35mm lens, both bodies filling the frame edge to edge. Hard raking side light, warm gold key making the seams glow, cool fill on the blue glaze. 3:4 vertical 8K portrait.""",
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
