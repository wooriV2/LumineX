# -*- coding: utf-8 -*-
"""
Living Artifact · Idol Duo (50)
- 흑인 여성 전용 Anime Duo(la_anime_duo_01~50, 4:5)와 별개의 신규 카테고리.
- 인물 풀: 한국/일본/중국 아이돌 + 인도/중동 걸프/라틴 미인 + 실버폭스(국적 무작위, 40대) — 흑인 제외, 무작위 혼합.
- 체형 9종(USSBBW·아워글래스 USSBBW·아워글래스 SSBBW·머슬 아워글래스 BBW·애슬리트 USSBBW·콜로설·텐트폴 USSBBW·
  톱헤비 아워글래스·바스트 퀸 BBW) + 일부 임산부 변형.
- 재질 14종(najeon·makie·palekh·khokhloma·laironam·cloisonne·dancheong·fordite·eunipsa·imari·jasperware·
  cheonghwa·celadon·jajuyo), 체형에 영향 없는 피어싱/귀걸이 등 액세서리 무작위 추가.
- 비율: 서기/앉기/무릎꿇기 = 세로 2:3, 옆으로 눕기(듀오는 눕기+걸터앉기 혼합)만 가로 3:2.
- 조합은 seed 고정(4271)으로 재현 가능, 체형×재질 쌍 중복 없음.
- output: presets/{key}.json  (title, category, platform, aspect_ratio, prompt)
- options: --force, --md review.md
"""
import json, os, argparse, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Idol Duo"
SEED = 4271
N = 50

# ---------------- body blocks ----------------
BODY = {
"ussbbw": ("USSBBW",
 "USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — an enormous soft belly made of four massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, deep creases between each roll, not pregnant, a gigantic bust resting on the top roll, no waist at all, colossal wide hips, colossal thick thighs, thick heavy calves."),
"hgussbbw": ("아워글래스 USSBBW",
 "EXTREME HOURGLASS USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — a colossal heavy bust wider than her shoulders, and below it a waistline that still pulls in clearly even at this size, then an enormous soft belly of four massive rounded rolls of heavy soft flesh spilling out below the waistline, the lowest roll hanging heavily down to mid-thigh, deep creases between each roll, not pregnant, colossal wide hips more than three times the width of that waistline, colossal thick thighs."),
"hgssbbw": ("아워글래스 SSBBW",
 "Hourglass SSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, not a plus-size model, around 700 pounds — a colossal heavy bust, a still-visible cinched waist indentation, a big soft rounded belly below the waistline hanging heavily over the top of her thighs, enormous round hips nearly three times the width of a normal woman's, gigantic soft thighs pressing together down to the knees, huge soft calves, very thick soft arms, a full round face."),
"musclehg": ("머슬 아워글래스 BBW",
 "Muscular hourglass BBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 450 pounds — a thick soft layer of fat over huge muscle everywhere, enormously broad powerful shoulders, thick heavy arms with rounded biceps under the softness, a colossal soft bust, a cinched waist far narrower than her hips with a soft rounded belly folding slightly over the waistline, gigantic wide hips more than twice the width of her waist, colossal thick thighs with strong quads showing through the softness, thick strong calves. More soft than hard, unmistakably hourglass."),
"athletic": ("애슬리트 USSBBW",
 "EXTREME ATHLETIC USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — the body of a world's strongest woman pushed far past real limits: enormously broad thick shoulders, massive heavy arms so thick they cannot hang flat against her sides, a colossal bust, a huge barrel torso with a big round heavy belly hanging over the tops of her thighs, no waist at all, colossal wide hips, a huge rounded powerful rear, tree-trunk thighs, thick heavy calves, not pregnant. Immense power under a thick layer of soft fat: the muscle is huge but rounded and buried, broad blunt swells with no sharp separation."),
"colossal": ("콜로설",
 "EXTREME COLOSSAL physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — a giantess built on a completely even scale, every part of her enlarged by the same amount: massive rounded shoulders, huge thick arms, a colossal full bust, a broad heavy torso with a large smooth rounded belly, wide solid hips, enormous columnar thighs and thick heavy calves, her shoulders spanning more than four head-widths. No single part stands out more than another, no hanging rolls, not pregnant."),
"tentpole": ("텐트폴 USSBBW",
 "EXTREME TENTPOLE USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — a giant hourglass frame that flares out at both ends: enormous flaring lats spreading to shoulders twice the width of a normal woman's, massive rounded deltoids stacked on top of them, huge thick arms pushed far out from her sides by the width of her back, a colossal bust projecting forward past the line of her shoulders, a broad heavy torso with a big round belly hanging over the tops of her thighs, no waist at all, colossal wide hips just as broad as her shoulders, a huge rounded rear, colossal thighs and thick heavy calves, not pregnant."),
"topheavy": ("톱헤비 아워글래스",
 "EXTREME TOP-HEAVY HOURGLASS physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 350 pounds — a colossal heavy bust far wider than her shoulders, curving forward as one enormous rounded mass and resting with real weight against her upper body, the bust nearly five times the width of her waistline, and below it enormous round hips flaring out to more than twice the width of her shoulders, a gigantic rounded rear, colossal thick thighs pressing together down to the knees, thick heavy calves, thick soft upper arms, not pregnant. The bust merges smoothly into her chest and shoulders as one continuous body, no gap, no seam."),
"bustqueen": ("바스트 퀸 BBW",
 "EXTREME BUST QUEEN BBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 500 pounds — a colossal bust far wider than her shoulders, each rounded half reaching past the outer line of her arms and hanging down to her waistline, several times the volume of her torso, its weight resting heavily on the big soft rounded belly below it, broad soft shoulders, thick heavy arms, soft wide hips and colossal soft thighs, thick heavy calves, not pregnant. The bust merges smoothly into her chest, shoulders and belly as one continuous soft body, no gap, no seam."),
}

PREG = {
"ussbbw": "EXTREME PREGNANT USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds and heavily pregnant — at the front of her body a great taut rounded belly of late pregnancy stands high and firm, the skin drawn tight and smooth over it, projecting far forward past everything else. Around it and beneath it the immense mass of soft heavy fat is still there and still hanging: thick rolls gather above the firm curve and press down onto it, soft flesh banks up at her sides and folds over its edges, and the lowest roll hangs heavily below it down to mid-thigh, so the soft flesh and the taut curve meet in deep shadowed creases all around. A gigantic bust resting on the topmost roll, no waist at all, colossal hips, colossal thick thighs, upper arms too thick to hang flat against her sides.",
"hgussbbw": "EXTREME PREGNANT HOURGLASS USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds and heavily pregnant — a colossal heavy bust wider than her shoulders, and below it a waistline that still pulls in clearly even at this size. Below that waistline a great taut rounded belly of late pregnancy stands high and firm, the skin drawn tight and smooth over it, projecting far forward past everything else, and around and beneath it the enormous soft belly still hangs in massive rounded rolls, thick rolls gathering above the firm curve and pressing down onto it and soft flesh banking up at her sides, so the soft flesh and the taut curve meet in deep shadowed creases all around. Colossal hips more than three times the width of that waistline, colossal thick thighs.",
"colossal": "EXTREME PREGNANT COLOSSAL physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds and heavily pregnant — a giantess built on a completely even scale, every part of her enlarged by the same amount: massive rounded shoulders, huge thick arms, a colossal full bust, a broad heavy torso, wide solid hips, enormous columnar thighs and thick heavy calves, her shoulders spanning more than four head-widths. At the front of her broad torso a great taut rounded belly of late pregnancy stands high and firm, the skin drawn tight and smooth over it, projecting far forward past everything else, the soft flesh of her sides banking up against its edges in a deep shadowed crease all the way around.",
"athletic": "EXTREME PREGNANT ATHLETIC USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds and heavily pregnant — enormously broad thick shoulders, massive heavy arms so thick they cannot hang flat against her sides, a colossal bust, a huge barrel torso, no waist at all, colossal wide hips, a huge rounded powerful rear, tree-trunk thighs. At the front of the barrel torso a great taut rounded belly of late pregnancy stands high and firm, the skin drawn tight and smooth over it, projecting far forward past everything else, with thick rolls of soft flesh gathering above it and a heavy fold hanging below it, the soft flesh and the taut curve meeting in deep shadowed creases all around. Immense power under a thick layer of soft fat.",
"tentpole": "EXTREME PREGNANT TENTPOLE USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds and heavily pregnant — enormous flaring lats spreading to shoulders twice the width of a normal woman's, huge thick arms pushed far out by the width of her back, a colossal bust projecting past the line of her shoulders, no waist at all, colossal wide hips just as broad as her shoulders, a huge rounded rear and colossal thighs. At the front a great taut rounded belly of late pregnancy stands high and firm, the skin drawn tight and smooth over it, projecting far forward past everything else, with thick rolls of soft flesh gathering above it and a heavy fold hanging below it, the soft flesh and the taut curve meeting in deep shadowed creases all around.",
}

# ---------------- material blocks: (kr_name, body_text) ----------------
MAT = {
"najeon": ("나전칠기", "painted as Korean najeon mother-of-pearl lacquer — glossy black lacquer covered with shimmering iridescent mother-of-pearl arabesque vines, peonies and cranes glowing pink, aqua and silver, wide bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines, dense scrolls filling the space between every band"),
"makie": ("마키에", "painted as Japanese maki-e lacquer — glossy black lacquer with sprinkled gold powder shading into autumn grasses, chrysanthemums, plum branches and full moons, bold gold bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines, a scattered gold-flake ground filling the space between every motif"),
"palekh": ("팔레흐", "painted as a Russian Palekh lacquer miniature — glossy mirror-black lacquer with ultra-fine gold filigree, firebirds, blossoms and tiny folk-tale scenes in red, gold and emerald, gold filigree filling all the space between the scenes so the shoulders, arms, knees and calves are covered as densely as the torso"),
"khokhloma": ("호홀로마", "painted in Russian Khokhloma style — a deep black ground with brilliant gold and vermilion strawberry vines, rowan berries and curling leaves painted in confident brushstrokes, gold bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines, dense berry vines filling the space between every band"),
"laironam": ("라이롯남", "painted in Thai lai rot nam — brilliant gold leaf over black lacquer, continuous kranok flame scrolls wrapping the shoulders, arms, belly and thighs, gold border bands following the deep crease beneath every roll and circling the arms and thighs"),
"cloisonne": ("칠보", "painted in cloisonné enamel — a brilliant turquoise enamel ground with lotus scrolls and peonies in coral red, cobalt and white, every colour cell outlined by raised gold wires, bold gold bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines"),
"dancheong": ("단청", "painted in Korean dancheong temple polychrome — brilliant cobalt blue, malachite green, vermilion red, white and gold geometric lotus and cloud motifs in tight symmetrical bands with crisp white outlines, banded borders following every deep crease and circling the arms and thighs, dense scrollwork filling the space between every band"),
"fordite": ("포다이트", "painted as polished fordite — thin layered strata of candy red, teal, mustard yellow, cobalt, white and orange stacked in tight concentric bands that follow every deep crease and curve around the hips and thighs like contour lines, glossy as polished stone"),
"eunipsa": ("은입사", "painted as Korean eunipsa silver inlay — a deep black iron ground with thick bright silver wire covering most of the surface, fine lattice fills between the lines, a bold silver band curving along the deep crease beneath every roll and around the hips and thighs"),
"imari": ("이마리", "painted in the Imari palette — cobalt blue underglaze scrolls, lotus and cranes joined by iron-red overglaze enamel and raised gilt accents, three colours layered together, bold bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines"),
"jasperware": ("웨지우드 재스퍼", "painted in Wedgwood jasperware style — a matte pale blue-white ground with crisp white applied relief scrolls, peonies and classical figures standing slightly proud of the surface, the white relief following the deep crease beneath every roll and curving around the hips and thighs like contour lines"),
"cheonghwa": ("청화백자", "painted as blue-and-white porcelain — a brilliant white ground with cobalt peony scrolls, lotus, vines and cranes, broad cobalt bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines, dense scrollwork filling the space between every band"),
"celadon": ("청자 상감", "painted in Korean celadon inlay — a soft pale jade-green glaze ground inlaid with crisp white and black slip cranes, clouds and chrysanthemum medallions, fine double-line bands following the deep crease beneath every roll and circling the arms and thighs"),
"jajuyo": ("자주요 흑유", "painted as Cizhou sgraffito ceramic — a glossy jet-black glaze carved away to bold cream-white peony scrolls and leafy vines, carved cream bands following the deep crease beneath every roll and curving around the hips and thighs like contour lines"),
}
MAT_SHOE = {
"najeon": "iridescent pearl-white", "makie": "gold", "palekh": "red lacquer with gold trim",
"khokhloma": "vermilion", "laironam": "gold", "cloisonne": "turquoise", "dancheong": "cobalt-blue",
"fordite": "candy-red", "eunipsa": "silver", "imari": "cobalt-and-red", "jasperware": "pale blue",
"cheonghwa": "white", "celadon": "pale jade-green", "jajuyo": "cream-white",
}
MAT_LIGHT = {
"najeon": "the mother-of-pearl shimmering with rainbow iridescence", "makie": "the gold powder glittering",
"palekh": "the gold filigree glinting against the black", "khokhloma": "the gold and vermilion glowing against the black",
"laironam": "the gold leaf blazing", "cloisonne": "the gold wires glinting on the turquoise enamel",
"dancheong": "the vivid dancheong colours blazing", "fordite": "the polished colour bands gleaming",
"eunipsa": "the silver wire gleaming on the black", "imari": "the red and gilt catching warm highlights over the blue",
"jasperware": "the white relief standing crisp against the matte blue", "cheonghwa": "the white ground reading bright with crisp cobalt",
"celadon": "the pale glaze glowing and the inlaid cranes reading crisp", "jajuyo": "the black glaze gleaming",
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

# accessories that never affect body shape — includes empty entries for "no accessory" cases
ACCESSORIES = [
 "small diamond studs in each earlobe", "a delicate pair of gold hoop earrings", "a single small nose stud catching the light",
 "a stack of two fine gold ear cuffs on one ear", "a pair of long dangling drop earrings", "a small silver septum ring",
 "a fine gold chain choker at her throat", "a pair of pearl stud earrings", "a small diamond nose stud and matching stud earrings",
 "delicate gold huggie hoops climbing one ear", "", "", "",
]

POSE_STAND = ("Pose: Both standing full frontal, feet planted very wide apart, their outer arms held away from their bodies, "
 "neither arm crossing in front of her own body or the other woman's.")
POSE_STAND_MIXED = ("Pose: The left woman stands full frontal with her feet planted wide. The right woman stands beside her turned "
 "about 45 degrees with the front of her body still mostly toward the camera and her face to the lens, the great mass of her middle "
 "seen in side profile and the curve of her hips and rear jutting out behind her. Both hold their arms away from their bodies, "
 "neither arm crossing in front of her own body or the other woman's.")
POSE_BENCH = ("Pose: Both seated on a short backless bench carved from a solid block of pale grey stone, facing the camera with "
 "their knees apart and their feet flat on the floor, their outer hands resting on the stone beside their hips and their inner "
 "hands on their own thighs, neither arm crossing in front of her own body or the other woman's.")
POSE_RECLINE = ("Pose: Both propped against the same padded backrest on a low platform at about 45 degrees with their legs "
 "stretched out in front of them and slightly apart, their outer arms resting back on the platform behind their hips with the "
 "elbows out and their inner hands on their own thighs, neither arm crossing in front of her own body or the other woman's.")
POSE_KNEEL = ("Pose: Both kneeling square to the camera on a low stone plinth with both knees down and set wide apart, their "
 "calves folded back beneath them and their weight settled down onto their heels, backs straight and faces to the camera, arms "
 "held clear of their bodies with a gap of background at each side.")
POSE_LIE = ("Pose: The left woman lies on her side facing the camera along the near length of a low platform, her head on her "
 "raised hand with that elbow planted behind her body, her other arm lifted clear and resting on the top of her hip with the "
 "elbow raised, her legs stacked with the knees slightly bent. The right woman sits upright on a short stone bench at the right "
 "with her knees apart and her feet on the floor, her hips turned about 45 degrees away from the camera so the curve of her rear "
 "spreading on the stone is seen from the side, her torso twisted back toward the lens and her face turned to the camera, her "
 "hands resting on the bench beside her hip and on her own thigh. Neither woman's arms cross in front of her own body or the other's.")

POSES = {
 "stand": ("나란히 서기", "v", POSE_STAND, ""),
 "stand_mixed": ("정면+3/4", "v", POSE_STAND_MIXED, ""),
 "bench": ("걸터앉기", "v", POSE_BENCH,
   " On both of them the mass of the middle settles down over the thighs and spreads forward as they sit, and the flesh of the "
   "thighs bulges out above and below where the hard front edge of the bench presses into them."),
 "recline": ("기대고 앉기", "v", POSE_RECLINE,
   " On both of them the mass of the middle spills forward down the slope of the raised torso and piles over the tops of the "
   "thighs, and the rear spreads wide and flattens against the platform."),
 "kneel": ("무릎 꿇기", "v", POSE_KNEEL,
   " On both of them the belly hangs straight down and the lowest roll rests on the plinth and spreads where it meets the stone."),
 "lie": ("눕기+걸터앉기", "h", POSE_LIE,
   " Lying on her side the left woman's middle spills forward away from her body and hangs over the front edge of her torso while "
   "her upper hip rises as a great rounded mound higher than her own shoulder; the seated woman's flesh bulges out above and below "
   "where the hard front edge of the bench presses into her thighs."),
}
POSE_WEIGHTS = [26, 18, 18, 14, 14, 10]  # stand, stand_mixed, bench, recline, kneel, lie

BG = ["A dark charcoal stylized background", "A dark deep-burgundy stylized background", "A dark midnight-blue stylized background",
      "A dark deep-navy stylized background", "A dark plum-purple stylized background"]

BODY_KEYS = list(BODY.keys())
MAT_KEYS = list(MAT.keys())
NATION_KEYS = list(NATION.keys())
POSE_KEYS = list(POSES.keys())


def gen_figure_face(rng, nation_key, silver):
    label, eng_noun, face_desc, hair_pool, smile_pool, age_pool = NATION[nation_key]
    if silver:
        age = rng.choice(SILVER_AGE)
        hair = f"{SILVER_NOTE} {rng.choice(SILVER_HAIR)}"
        smile = rng.choice(["a quiet assured expression", "a serene composed expression", "a calm assured smile"])
        kr_label = f"{label} 실버폭스"
        return kr_label, eng_noun, age, face_desc, hair, smile
    age = rng.choice(age_pool)
    hair = rng.choice(hair_pool)
    smile = rng.choice(smile_pool)
    return label, eng_noun, age, face_desc, hair, smile


def acc_clause(rng):
    a = rng.choice(ACCESSORIES)
    return f", {a}" if a else ""


def build_one(rng, idx, used):
    for _ in range(200):
        bL, bR = rng.sample(BODY_KEYS, 2)
        mL, mR = rng.sample(MAT_KEYS, 2)
        key = (bL, bR, mL, mR)
        if key not in used:
            used.add(key)
            break
    pregL = rng.random() < 0.12 and bL in PREG
    pregR = (rng.random() < 0.12 and bR in PREG) and not pregL
    pose_key = rng.choices(POSE_KEYS, weights=POSE_WEIGHTS)[0]
    pose_label, frame, pose_text, pose_extra = POSES[pose_key]

    silverL = rng.random() < 0.18
    silverR = rng.random() < 0.18
    natL = rng.choice(NATION_KEYS)
    natR = rng.choice(NATION_KEYS)

    krL, engL, ageL, faceL, hairL, smileL = gen_figure_face(rng, natL, silverL)
    krR, engR, ageR, faceR, hairR, smileR = gen_figure_face(rng, natR, silverR)

    physL = PREG[bL] if pregL else BODY[bL][1]
    physR = PREG[bR] if pregR else BODY[bR][1]
    matL_name, matL_text = MAT[mL]
    matR_name, matR_text = MAT[mR]
    accL = acc_clause(rng)
    accR = acc_clause(rng)

    left = (f"Left woman: {engL} in her {ageL}, {faceL}{accL}, {hairL}, {smileL}. "
            f"{physL} Her body is {matL_text}, covering her from the collarbones to the ankles.")
    right = (f"Right woman: {engR} in her {ageR}, {faceR}{accR}, {hairR}, {smileR}. "
             f"{physR} Her body is {matR_text}, covering her from the collarbones to the ankles.")

    cover = ("Coverage: On both women the pattern covers the entire bust densely with no open gaps, and wraps fully around the "
             "rear, the lower belly, the knees and the calves, covering them as densely as the chest. Every fold and roll keeps "
             "its own clear rounded outline with a deep shadowed crease between them, never merging into one shapeless mass.")

    pose = pose_text + pose_extra
    shoes = (f"Footwear: The left woman wears extreme {MAT_SHOE[mL]} platform stiletto slingbacks; the right woman wears extreme "
             f"{MAT_SHOE[mR]} platform stiletto mules, the platform soles as tall as their ankle bones, the ultra-thin stiletto "
             f"heels so high their insteps stand nearly vertical.")
    bg = rng.choice(BG)
    back = (f"Background & Lighting: {bg}, a single strong warm light from the left, deep soft shadows in every crease and "
            f"beneath every hanging roll, {MAT_LIGHT[mL]} and {MAT_LIGHT[mR]}, glossy anime highlights on every curve.")

    if frame == "v":
        head = "Image format: a vertical portrait-orientation illustration, 2:3 aspect ratio, taller than it is wide."
        end = "Vertical 2:3 portrait-orientation full-body illustration, taller than it is wide."
        subj_frame = ("The camera is set close so the two of them fill the frame edge to edge — their bodies together overflow "
                       "the full width of the frame and run off both the left and right edges, their heads near the top edge and "
                       "their heels near the bottom, with almost no background visible. They stand close enough that their sides "
                       "press against each other and the flesh bulges out where they touch.")
        aspect = "2:3"
    else:
        head = "Image format: a horizontal landscape-orientation illustration, 3:2 aspect ratio, wider than it is tall."
        end = "Horizontal 3:2 landscape-orientation full-body illustration, wider than it is tall."
        subj_frame = ("The camera is set close so the two of them fill the frame edge to edge and top to bottom, with almost no "
                       "empty ground left.")
        aspect = "3:2"

    style = ("Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant "
             "saturated colors, polished professional anime art — not a photograph.")
    subj = (f"Subject: TWO mature adult women, both with clearly adult facial features, both full body head to toe, both faces "
            f"toward the camera, each with her own distinct nationality, face and skin tone as described below. {subj_frame}")

    prompt = "\n\n".join([head, style, subj, left, right, cover, pose, shoes, back, end])
    title = (f"Idol Duo {idx:02d} · {('임산부 ' if pregL else '')}{BODY[bL][0]}({krL}) × {('임산부 ' if pregR else '')}"
             f"{BODY[bR][0]}({krR}) · {matL_name}×{matR_name} · {pose_label}")
    key_slug = f"la_idolduo_{idx:02d}_{bL}-{bR}_{mL}-{mR}_{pose_key}"
    return {"title": title, "category": CATEGORY, "platform": "gemini", "aspect_ratio": aspect, "prompt": prompt}, key_slug


def validate(items):
    seen_keys = set()
    for data, key in items:
        assert data["prompt"].startswith("Image format")
        assert data["prompt"].rstrip().endswith("taller than it is wide.") or data["prompt"].rstrip().endswith("wider than it is tall.")
        assert key not in seen_keys, key
        seen_keys.add(key)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()

    rng = random.Random(SEED)
    used = set()
    items = [build_one(rng, i, used) for i in range(1, N + 1)]
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
            f.write(f"# Living Artifact · Idol Duo ({N})\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")


if __name__ == "__main__":
    main()
