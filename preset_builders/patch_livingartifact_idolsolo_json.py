# -*- coding: utf-8 -*-
"""
Living Artifact · Idol Solo (124)
- Idol Duo(la_idolduo_*)와 같은 인물 풀(한국/일본/중국 아이돌 + 인도/중동 걸프/라틴 미인 + 실버폭스, 흑인 제외)의 솔로 버전.
- 체형 9종 × 재질 14종 = 126 조합 중 124개 사용 (중복 없음, seed 고정으로 재현 가능).
- 자세: 3/4 서기·정면 서기·걸터앉기·기대고 앉기·무릎 꿇기·쪼그려 앉기(세로 2:3) + 옆으로 눕기(가로 3:2, 약 12%).
- 체형에 영향 없는 피어싱/귀걸이 등 액세서리 무작위 추가.
- Body Art 문단을 Physique 앞에 배치(오늘 확정 규칙).
- output: presets/{key}.json  (title, category, platform, aspect_ratio, prompt)
- options: --force, --md review.md
"""
import json, os, argparse, random, itertools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Idol Solo"
SEED = 9311
N = 124

# ---------------- body blocks: (kr_name, physique_text) ----------------
BODY = {
"ussbbw": ("USSBBW",
 "USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds, her body so wide that her hips are cut off by the left and right edges of the frame — an enormous soft belly made of four massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, deep creases between each roll, not pregnant, a gigantic bust resting on the top roll, no waist at all, colossal wide hips, colossal thick thighs, thick heavy calves, upper arms too thick to hang flat against her sides."),
"hgussbbw": ("아워글래스 USSBBW",
 "EXTREME HOURGLASS USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds, her body so wide that her hips are cut off by the left and right edges of the frame — a colossal heavy bust wider than her shoulders, and below it a waistline that still pulls in clearly even at this size, then an enormous soft belly of four massive rounded rolls of heavy soft flesh spilling out below the waistline, the lowest roll hanging heavily down to mid-thigh, deep creases between each roll, not pregnant, colossal wide hips more than three times the width of that waistline, colossal thick thighs."),
"hgssbbw": ("아워글래스 SSBBW",
 "Hourglass SSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, not a plus-size model, around 700 pounds — a colossal heavy bust, a still-visible cinched waist indentation, a big soft rounded belly below the waistline hanging heavily over the top of her thighs, enormous round hips nearly three times the width of a normal woman's, gigantic soft thighs pressing together down to the knees, huge soft calves, very thick soft arms, a full round face."),
"musclehg": ("머슬 아워글래스 BBW",
 "Muscular hourglass BBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 450 pounds — a thick soft layer of fat over huge muscle everywhere, enormously broad powerful shoulders, thick heavy arms with rounded biceps under the softness, a colossal soft bust, a cinched waist far narrower than her hips with a soft rounded belly folding slightly over the waistline, gigantic wide hips more than twice the width of her waist, colossal thick thighs with strong quads showing through the softness, thick strong calves. More soft than hard, unmistakably hourglass."),
"athletic": ("애슬리트 USSBBW",
 "EXTREME ATHLETIC USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — the body of a world's strongest woman pushed far past real limits: enormously broad thick shoulders, massive heavy arms so thick they cannot hang flat against her sides, a colossal bust, a huge barrel torso with a big round heavy belly hanging over the tops of her thighs, no waist at all, colossal wide hips, a huge rounded powerful rear, tree-trunk thighs, thick heavy calves, not pregnant. Immense power under a thick layer of soft fat: the muscle is huge but rounded and buried, broad blunt swells with no sharp separation."),
"colossal": ("콜로설",
 "EXTREME COLOSSAL physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds, her body so wide that her shoulders are cut off by the left and right edges of the frame — a giantess built on a completely even scale, every part of her enlarged by the same amount: massive rounded shoulders, huge thick arms, a colossal full bust, a broad heavy torso with a large smooth rounded belly, wide solid hips, enormous columnar thighs and thick heavy calves, her shoulders spanning more than four head-widths, each hand as wide as a normal woman's torso. No single part stands out more than another, no hanging rolls, not pregnant."),
"tentpole": ("텐트폴 USSBBW",
 "EXTREME TENTPOLE USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds, her body so wide that both her shoulders and hips are cut off by the left and right edges of the frame — a giant hourglass frame that flares out at both ends: enormous flaring lats spreading to shoulders twice the width of a normal woman's, massive rounded deltoids stacked on top of them, huge thick arms pushed far out from her sides by the width of her back, a colossal bust projecting forward past the line of her shoulders, a broad heavy torso with a big round belly hanging over the tops of her thighs, no waist at all, colossal wide hips just as broad as her shoulders, a huge rounded rear, colossal thighs and thick heavy calves, not pregnant."),
"topheavy": ("톱헤비 아워글래스",
 "EXTREME TOP-HEAVY HOURGLASS physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 350 pounds — a colossal heavy bust far wider than her shoulders, curving forward as one enormous rounded mass and resting with real weight against her upper body, the bust nearly five times the width of her waistline, and below it enormous round hips flaring out to more than twice the width of her shoulders, a gigantic rounded rear, colossal thick thighs pressing together down to the knees, thick heavy calves, thick soft upper arms, not pregnant. The bust merges smoothly into her chest and shoulders as one continuous body, no gap, no seam."),
"bustqueen": ("바스트 퀸 BBW",
 "EXTREME BUST QUEEN BBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 500 pounds — a colossal bust far wider than her shoulders, each rounded half reaching past the outer line of her arms and hanging down to her waistline, several times the volume of her torso, its weight resting heavily on the big soft rounded belly below it, broad soft shoulders, thick heavy arms, soft wide hips and colossal soft thighs, thick heavy calves, not pregnant. The bust merges smoothly into her chest, shoulders and belly as one continuous soft body, no gap, no seam."),
}

# ---------------- material blocks: (kr_name, body_art_text, shoe_color, light_text) ----------------
MAT = {
"najeon": ("나전칠기", "Full body Korean najeon mother-of-pearl lacquer body painting on her bare skin from the collarbones to the ankles, glossy black lacquer covered with shimmering iridescent mother-of-pearl arabesque vines, peonies and cranes glowing pink, aqua and silver, wide bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines, dense scrolls filling the space between every band.", "iridescent pearl-white", "the mother-of-pearl shimmering with rainbow iridescence"),
"makie": ("마키에", "Full body Japanese maki-e lacquer body painting on her bare skin from the collarbones to the ankles, glossy black lacquer with sprinkled gold powder shading into autumn grasses, chrysanthemums, plum branches and full moons, bold gold bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines, a scattered gold-flake ground filling the space between every motif.", "gold", "the gold powder glittering"),
"palekh": ("팔레흐", "Full body Russian Palekh lacquer miniature body painting on her bare skin from the collarbones to the ankles, glossy mirror-black lacquer with ultra-fine gold filigree, firebirds, blossoms and tiny folk-tale scenes in red, gold and emerald, gold filigree filling all the space between the scenes so the shoulders, arms, knees and calves are covered as densely as the torso.", "red lacquer with gold trim", "the gold filigree glinting against the black"),
"khokhloma": ("호홀로마", "Full body Russian Khokhloma body painting on her bare skin from the collarbones to the ankles, a deep black ground with brilliant gold and vermilion strawberry vines, rowan berries and curling leaves painted in confident brushstrokes, gold bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines, dense berry vines filling the space between every band.", "vermilion", "the gold and vermilion glowing against the black"),
"laironam": ("라이롯남", "Full body Thai lai rot nam body painting on her bare skin from the collarbones to the ankles, brilliant gold leaf over black lacquer, continuous kranok flame scrolls wrapping the shoulders, arms, belly and thighs, gold border bands following the deep crease beneath every roll and circling the arms and thighs.", "gold", "the gold leaf blazing"),
"cloisonne": ("칠보", "Full body cloisonné enamel body painting on her bare skin from the collarbones to the ankles, a brilliant turquoise enamel ground with lotus scrolls and peonies in coral red, cobalt and white, every colour cell outlined by raised gold wires, bold gold bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines.", "turquoise", "the gold wires glinting on the turquoise enamel"),
"dancheong": ("단청", "Full body Korean dancheong temple polychrome body painting on her bare skin from the collarbones to the ankles, brilliant cobalt blue, malachite green, vermilion red, white and gold geometric lotus and cloud motifs in tight symmetrical bands with crisp white outlines, banded borders following every deep crease and circling the arms and thighs, dense scrollwork filling the space between every band.", "cobalt-blue", "the vivid dancheong colours blazing"),
"fordite": ("포다이트", "Full body polished fordite body painting on her bare skin from the collarbones to the ankles, thin layered strata of candy red, teal, mustard yellow, cobalt, white and orange stacked in tight concentric bands that follow every deep crease and curve around the hips and thighs like contour lines, glossy as polished stone.", "candy-red", "the polished colour bands gleaming"),
"eunipsa": ("은입사", "Full body Korean eunipsa silver inlay body painting on her bare skin from the collarbones to the ankles, a deep black iron ground with thick bright silver wire covering most of the surface, fine lattice fills between the lines, a bold silver band curving along the deep crease beneath every roll and around the hips and thighs.", "silver", "the silver wire gleaming on the black"),
"imari": ("이마리", "Full body Imari-palette body painting on her bare skin from the collarbones to the ankles, cobalt blue underglaze scrolls, lotus and cranes joined by iron-red overglaze enamel and raised gilt accents, three colours layered together, bold bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines.", "cobalt-and-red", "the red and gilt catching warm highlights over the blue"),
"jasperware": ("웨지우드 재스퍼", "Full body Wedgwood jasperware body painting on her bare skin from the collarbones to the ankles, a matte pale blue-white ground with crisp white applied relief scrolls, peonies and classical figures standing slightly proud of the surface, the white relief following the deep crease beneath every roll and curving around the hips and thighs like contour lines.", "pale blue", "the white relief standing crisp against the matte blue"),
"cheonghwa": ("청화백자", "Full body blue-and-white porcelain body painting on her bare skin from the collarbones to the ankles, a brilliant white ground with cobalt peony scrolls, lotus, vines and cranes, broad cobalt bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines, dense scrollwork filling the space between every band.", "white", "the white ground reading bright with crisp cobalt"),
"celadon": ("청자 상감", "Full body Korean celadon inlay body painting on her bare skin from the collarbones to the ankles, a soft pale jade-green glaze ground inlaid with crisp white and black slip cranes, clouds and chrysanthemum medallions, fine double-line bands following the deep crease beneath every roll and circling the arms and thighs.", "pale jade-green", "the pale glaze glowing and the inlaid cranes reading crisp"),
"jajuyo": ("자주요 흑유", "Full body Cizhou sgraffito ceramic body painting on her bare skin from the collarbones to the ankles, a glossy jet-black glaze carved away to bold cream-white peony scrolls and leafy vines, carved cream bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines.", "cream-white", "the black glaze gleaming"),
}

# ---------------- nationality/face blocks: (kr_label, eng_noun, face_desc, hair_pool, smile_pool, age_pool) ----------------
NATION = {
"kr_idol": ("한국 아이돌", "a Korean woman", "with the polished look of a K-pop idol, fair ivory skin with a warm golden undertone, smooth high cheekbones with a gently tapering jaw and a small delicate chin, large clear dark eyes with a soft double lid, straight softly arched brows, a slender nose and full rounded lips",
 ["long straight glossy black hair with a soft see-through fringe", "a sleek chin-length bob with a blunt cut",
  "long dark brown hair in soft loose curls with a centre part", "long honey-brown hair in soft beach waves with a deep side part",
  "a shoulder-length layered cut with a light outward flick at the ends", "long jet-black hair pulled into a high ponytail with two loose strands framing her face"],
 ["a bright confident smile", "a calm composed smile", "a cool composed expression, feminine face", "a warm open smile"],
 ["early 20s", "late 20s", "early 30s"]),
"jp_idol": ("일본 아이돌", "a Japanese woman", "with the sweet look of a Japanese idol, fair skin with a soft neutral undertone, soft full cheeks with a gently tapering jaw and a small chin, very large round dark eyes with a wide gaze, softly rounded brows, a small nose and small full lips",
 ["long black hair with a straight blunt fringe and loose waves at the ends", "a blunt shoulder-length cut with a straight fringe just above the eyebrows",
  "long black hair with a soft curtain fringe parted in the middle", "shoulder-length black hair with a soft blunt fringe and a light outward flick"],
 ["a bright cheerful smile", "a bright gentle smile", "a gentle cheerful smile", "a calm composed expression"],
 ["early 20s", "late 20s"]),
"cn_idol": ("중국 아이돌", "a Chinese woman", "with the polished look of a C-pop idol, fair porcelain-pale skin with a cool undertone, smooth high cheekbones with a gently tapering jaw and a small round chin, large clear almond eyes with a soft double lid, willow-leaf brows, a small nose and small full lips",
 ["long straight black hair with a centre part falling past her shoulders", "a sleek low ponytail with a straight fringe",
  "long black hair in soft waves with a deep side part"],
 ["a gentle cheerful smile", "a calm composed smile", "a serene assured expression"],
 ["early 20s", "late 20s", "early 30s"]),
"indian": ("인도 미인", "an Indian woman", "with the refined features of a high fashion model — a flawless oval face with warm deep-golden brown skin, high sculpted cheekbones, a clean jawline, very large deep almond eyes under strong arched brows, heavy dark lashes, a straight elegant nose and full sculpted lips, thick black kohl rimming both eyes and drawn into a fine tail, a deep red lip",
 ["long jet-black hair in heavy glossy waves", "long black hair swept into a low twisted chignon with a few strands loose at the temples",
  "long black hair pulled into a high sleek ponytail"],
 ["a calm direct gaze", "a serene assured expression", "a bright confident smile"],
 ["late 20s", "early 30s"]),
"gulf": ("중동 걸프 미인", "a Gulf Arab woman", "with the refined features of a high fashion model — a flawless oval face with warm olive skin, high sculpted cheekbones, a clean jawline, very large deep-set dark eyes under strong dark brows, heavy lashes, a straight elegant nose with a fine high bridge and full well-defined lips, dense black kohl rimming both eyes and smoked outward at the corners, a warm bronze eyeshadow, a soft nude-rose lip",
 ["long jet-black hair in heavy glossy waves", "long black hair swept into a low twisted chignon"],
 ["a calm direct gaze", "a serene composed expression"],
 ["late 20s", "early 30s"]),
"latina": ("라틴 미인", "a Latina woman", "with the refined features of a high fashion model — a flawless oval face with warm golden-bronze skin, high sculpted cheekbones, a clean jawline, large dark almond eyes under strong dark brows, heavy lashes, a straight elegant nose and full richly shaped lips, a sharp black winged liner, a warm terracotta eyeshadow, a deep berry lip",
 ["a high sleek ponytail with a few strands loose at the temples", "long dark brown hair in loose waves swept over one shoulder"],
 ["a calm direct gaze", "a calm powerful smile, feminine face"],
 ["late 20s", "early 30s"]),
}
SILVER_NOTE = ("a striking silver-haired beauty, her hair turned early — her face still young and firm with only the faintest lines "
 "at the outer corners of her eyes, a full head of natural silver-white hair")
SILVER_HAIR = ["in a sharp shoulder-length bob with a deep side part", "swept into a sleek low chignon with a few strands loose at the temples",
               "in loose glossy waves", "in a sharp blunt bob with a straight centre part"]
SILVER_AGE = ["early 40s", "mid 40s"]

ACCESSORIES = [
 "small diamond studs in each earlobe", "a delicate pair of gold hoop earrings", "a single small nose stud catching the light",
 "a stack of two fine gold ear cuffs on one ear", "a pair of long dangling drop earrings", "a small silver septum ring",
 "a fine gold chain choker at her throat", "a pair of pearl stud earrings", "a small diamond nose stud and matching stud earrings",
 "delicate gold huggie hoops climbing one ear", "", "", "",
]

POSES_V = {
"stand34": ("3/4 서기", "Pose: Standing turned about 45 degrees with the front of her body still mostly facing the viewer, her face toward the camera, the stacked rolls and curves seen in side profile hanging forward and the enormous curve of her hips and rear jutting out behind her, feet planted wide apart, arms held clear of her body with a gap of background at each side, full body head to toe."),
"standfront": ("정면 서기", "Pose: Standing full frontal, feet planted very wide apart, arms held well away from her body with a visible gap of background at each side, full body head to toe."),
"bench": ("걸터앉기", "Pose: Seated on a short backless bench carved from a solid block of pale grey stone, her hips turned about 45 degrees away from the camera so the great curve of her rear spreading on the stone is seen from the side, her torso twisted back toward the viewer and her face turned to the camera, her near knee toward the camera and her far leg angled away, one hand resting back on the bench behind her hip and the other on her near thigh, both arms held clear of her body, full body head to toe. The flesh of her thighs bulges out above and below where the hard front edge of the bench presses into them."),
"recline": ("기대고 앉기", "Pose: Propped against a padded backrest on a low platform at about 45 degrees with her legs stretched out in front of her and slightly apart, her outer arm resting back on the platform behind her hip with the elbow out and her other hand on her own thigh, neither arm crossing in front of her torso, her face turned to the camera, full body head to toe. The mass of her middle spills forward down the slope of her raised torso and piles over the tops of her thighs."),
"kneel": ("무릎 꿇기", "Pose: Kneeling square to the camera on a low stone plinth with both knees down and set wide apart, her calves folded back beneath her and her weight settled down onto her heels, her back straight and her face to the camera, arms held clear of her body with a gap of background at each side, full body head to toe. The great mass of her middle hangs straight down in front of her and the lowest roll rests on the plinth and spreads where it meets the stone."),
"squat": ("쪼그려 앉기", "Pose: Squatting square to the camera on a low stone plinth, her feet flat and planted very wide apart with her knees pushed right out to either side, her hips lowered all the way down onto her heels, her back straight and her face to the camera, the great mass of her middle hanging down between her knees to the stone, her arms held well clear of her body and out beyond her knees with a gap of background at each side, full body head to toe."),
}
POSE_LIE = ("Pose: Lying on her side on a low platform facing the viewer, her head resting on her raised hand with that elbow "
 "planted behind her body so her arm never crosses in front of her torso, her other arm lifted clear and resting on the top of "
 "her upper hip with the elbow raised, her legs stacked one on the other with the knees slightly bent, her body stretching "
 "across the full width of the frame from edge to edge. The middle of her body spills forward away from her torso and hangs far "
 "over the front edge of it, the lowest part sagging onto the platform and spreading wide where it meets it, while her upper hip "
 "rises as a great rounded mound higher than her own shoulder.")

POSE_KEYS_V = list(POSES_V.keys())
POSE_WEIGHTS_V = [22, 18, 16, 16, 18, 10]
LIE_CHANCE = 0.12

BG = ["A dark charcoal stylized background", "A dark deep-burgundy stylized background", "A dark midnight-blue stylized background",
      "A dark deep-navy stylized background", "A dark plum-purple stylized background", "A bright pale warm-sand stylized background"]

BODY_KEYS = list(BODY.keys())
MAT_KEYS = list(MAT.keys())
NATION_KEYS = list(NATION.keys())


def gen_face(rng, nation_key, silver):
    label, eng_noun, face_desc, hair_pool, smile_pool, age_pool = NATION[nation_key]
    if silver:
        age = rng.choice(SILVER_AGE)
        hair = f"{SILVER_NOTE} {rng.choice(SILVER_HAIR)}"
        smile = rng.choice(["a quiet assured expression", "a serene composed expression", "a calm assured smile"])
        return f"{label} 실버폭스", eng_noun, age, face_desc, hair, smile
    return label, eng_noun, rng.choice(age_pool), face_desc, rng.choice(hair_pool), rng.choice(smile_pool)


def acc_clause(rng):
    a = rng.choice(ACCESSORIES)
    return f", {a}" if a else ""


def build_one(rng, idx, bL, mL):
    lie = rng.random() < LIE_CHANCE
    silver = rng.random() < 0.16
    nat = rng.choice(NATION_KEYS)
    kr, eng, age, face, hair, smile = gen_face(rng, nat, silver)
    body_label, phys = BODY[bL]
    mat_label, mat_text, shoe_color, mat_light = MAT[mL]
    acc = acc_clause(rng)

    subject = (f"Subject: ONE mature adult woman, {eng} in her {age}, with clearly adult facial features, {face}{acc}, {hair}, {smile}.")
    physique_line = f"Physique: {phys}"

    if lie:
        head = "Image format: a horizontal landscape-orientation illustration, 3:2 aspect ratio, wider than it is tall."
        end = "Horizontal 3:2 landscape-orientation full-body illustration, wider than it is tall."
        aspect = "3:2"
        pose_label = "옆으로 눕기"
        pose = POSE_LIE
    else:
        pose_key = rng.choices(POSE_KEYS_V, weights=POSE_WEIGHTS_V)[0]
        pose_label, pose = POSES_V[pose_key]
        head = "Image format: a vertical portrait-orientation illustration, 2:3 aspect ratio, taller than it is wide."
        end = "Vertical 2:3 portrait-orientation full-body illustration, taller than it is wide."
        aspect = "2:3"

    style = ("Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant "
             "saturated colors, polished professional anime art — not a photograph.")
    coverage = ("The pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly "
                "and the calves, covering them as densely as the chest. Every roll keeps its own clear rounded outline with a "
                "deep shadowed crease between them, never merging into one shapeless mass.")
    footwear = (f"Footwear: Extreme {shoe_color} platform stiletto slingbacks, the platform soles as tall as her ankle bones, "
                f"the ultra-thin stiletto heels so high her insteps stand nearly vertical.")
    bg = rng.choice(BG)
    background = (f"Background & Lighting: {bg}, a single strong warm light from one side, deep soft shadows in every crease and "
                  f"beneath every hanging roll, {mat_light}, glossy anime highlights on every curve.")

    prompt = "\n\n".join([head, style, subject, f"Body Art: {mat_text} {coverage}", physique_line, pose, footwear, background, end])
    title = f"Idol Solo {idx:03d} · {body_label}({kr}) · {mat_label} · {pose_label}"
    key = f"la_idolsolo_{idx:03d}_{bL}_{mL}"
    return {"title": title, "category": CATEGORY, "platform": "gemini", "aspect_ratio": aspect, "prompt": prompt}, key


def validate(items):
    seen = set()
    for data, key in items:
        assert data["prompt"].startswith("Image format")
        assert data["prompt"].rstrip().endswith("taller than it is wide.") or data["prompt"].rstrip().endswith("wider than it is tall.")
        assert key not in seen, key
        seen.add(key)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()

    rng = random.Random(SEED)
    combos = list(itertools.product(BODY_KEYS, MAT_KEYS))
    rng.shuffle(combos)
    combos = combos[:N]

    items = [build_one(rng, i, bL, mL) for i, (bL, mL) in enumerate(combos, 1)]
    validate(items)

    os.makedirs(PRESETS, exist_ok=True)
    made = skipped = 0
    md = []
    for data, key in items:
        md.append(f"## {key}\n**{data['title']}**\n\n```\n{data['prompt']}\n```\n")
        path = os.path.join(PRESETS, key + ".json")
        if os.path.exists(path) and not a.force:
            skipped += 1
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        made += 1
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write(f"# Living Artifact · Idol Solo ({N})\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")


if __name__ == "__main__":
    main()
