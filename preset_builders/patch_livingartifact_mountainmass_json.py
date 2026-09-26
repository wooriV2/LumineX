# -*- coding: utf-8 -*-
"""
Living Artifact · Mountain Mass (30)
- 5,000파운드 극단 부피 전용 카테고리. 기존 Idol Duo/Solo(1,000~1,500lb)와 별개.
- v6.4 13장 규칙 전면 적용:
  - Body Art는 원본 짧은 형식만 사용, 띠(band) 표현 없음
  - 허리 있는 체형(아워글래스 4종)은 듀오에서만 사용 + 허리 처방 문장 포함
  - 어깨 넓은 체형(텐트폴·애슬리트)은 어깨 처방 문장 포함
  - "흐르는" 동사(hangs/spills) 대신 "쌓인 덩어리"(stacked/resting heavy and solid) 사용
  - 무릎 꿇기는 "kneeling upright ... not squatting and not crouching"로 이중 고정
  - 듀오는 Coverage 문단으로 두 몸이 맞닿는 자리 처리, 팔이 프레임 밖으로 잘리는 건 지시하지 않음(체형이 결정)
- 솔로 20 (허리 없는 체형 5종: USSBBW·콜로설·텐트폴·애슬리트·바스트 퀸) + 듀오 10 (위 5종 + 아워글래스 4종, 총 9종에서 무작위 조합)
- 재질 14종, 인물 풀은 Idol Duo/Solo와 동일(한중일 아이돌 + 인도·중동·라틴 미인 + 실버폭스, 흑인 제외)
- output: presets/{key}.json  (title, category, platform, aspect_ratio, prompt)
- options: --force, --md review.md
"""
import json, os, argparse, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Mountain Mass"
SEED = 51117
N_SOLO = 20
N_DUO = 10

import json, os, random, itertools

# ---- 허리 없는 체형 5종 (솔로 기본, 듀오도 우선 사용) ----
BODY_NW = {
"ussbbw": ("USSBBW", "USSBBW",
 "Her body so wide that her hips are cut off far inside the left and right edges of the frame and her head nearly touches the top edge. An enormous soft belly of {rolls} massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, {lowroll}, deep shadowed creases between them, not pregnant, a gigantic bust resting on the top roll, no waist at all, colossal hips seven times the width of her shoulders, each thigh wider than a normal woman is tall and pressing hard against the other, upper arms so thick they are pushed out almost horizontally from her sides and cannot come anywhere near her body.",
 False),
"colossal": ("콜로설", "COLOSSAL",
 "Her body so wide that her shoulders are cut off far inside the left and right edges of the frame and her head nearly touches the top edge. A giantess built on a completely even scale, every part of her enlarged by the same immense amount: massive rounded shoulders, huge thick arms, a colossal full bust, a broad heavy torso with a large smooth rounded belly, wide solid hips, enormous columnar thighs and thick heavy calves. Her shoulders span more than eight head-widths and each thigh is wider than a normal woman is tall. No single part stands out more than another, no hanging rolls, not pregnant, her whole body one immense smooth silhouette.",
 False),
"tentpole": ("텐트폴 USSBBW", "TENTPOLE USSBBW",
 "Her body so wide that both her shoulders and her hips are cut off far inside the left and right edges of the frame. A giant hourglass frame that flares out at both ends: enormous flaring lats spreading to shoulders more than four times the width of a normal woman's, massive rounded deltoids stacked on top of them, a smooth rounded neck buried between the shoulders, a colossal bust projecting forward far past the line of her shoulders, a broad heavy torso with a big round belly of {rolls_small} heavy rounded rolls stacked in front of her, no waist at all, colossal wide hips just as broad as her shoulders, thighs wider than a normal woman is tall and thick heavy calves, not pregnant. {shoulder_patch}",
 True),
"athletic": ("애슬리트 USSBBW", "ATHLETIC USSBBW",
 "Her body so wide that her hips are cut off far inside the left and right edges of the frame and her head nearly touches the top edge. Enormously broad thick shoulders, massive heavy arms pushed out almost horizontally from her sides and unable to come anywhere near her body, a colossal bust, a huge barrel torso, no waist at all, a great mass of soft heavy flesh sits stacked in {rolls} heavy rounded rolls one above the other in front of her, deep shadowed creases between them, not pregnant, colossal hips seven times the width of her shoulders, each thigh wider than a normal woman is tall. {shoulder_patch}",
 True),
"bustqueen": ("바스트 퀸 BBW", "BUST QUEEN BBW",
 "Her body so wide that her hips are cut off far inside the left and right edges of the frame. A colossal bust far wider than her shoulders, each rounded half many times the volume of her torso, its weight resting heavily on a great mass of soft heavy fat stacked in {rolls_small} rolls one above the other below it, broad soft shoulders, thick heavy arms, soft wide hips and colossal soft thighs each wider than a normal woman is tall, thick heavy calves, not pregnant. The bust merges smoothly into her chest, shoulders and belly as one continuous soft body, no gap, no seam.",
 False),
}

# ---- 허리 있는 체형 4종 (듀오에서만 사용, 허리 처방 포함) ----
WAIST_PATCH = ("That inward turn is nothing but the shape of her own flesh, painted exactly as continuously as every other part of her, the pattern "
 "simply following the flesh in and out again with no interruption, no closed shape, and no separate piece of anything laid over the skin there.")
BODY_W = {
"hgussbbw": ("아워글래스 USSBBW", "HOURGLASS USSBBW",
 "A colossal heavy bust wider than her shoulders, and below it a waistline that still pulls in clearly even at this size — the one place "
 "on her whole body where the outline turns inward, now reading as a narrow throat between two mountains of flesh. " + WAIST_PATCH +
 " Below that waistline an enormous soft belly of {rolls} massive rounded rolls of heavy soft flesh stacked one above the other, each roll "
 "thicker and rounder than the one above it, deep shadowed creases between them, not pregnant, colossal hips seven times the width of that "
 "waistline, each thigh wider than a normal woman is tall."),
"hgssbbw": ("아워글래스 SSBBW", "HOURGLASS SSBBW",
 "A colossal heavy bust, and below it a waistline that still draws in even at this size — the one place her outline turns inward. " + WAIST_PATCH +
 " A great mass of soft heavy flesh stacked in {rolls} heavy rounded rolls one above the other below it, deep shadowed creases between them, "
 "not pregnant, colossal wide hips seven times the width of that waistline, each thigh wider than a normal woman is tall, very thick soft arms."),
"musclehg": ("머슬 아워글래스 BBW", "MUSCULAR HOURGLASS BBW",
 "enormously broad powerful shoulders, thick heavy arms with the swell of biceps and triceps showing through a colossal soft layer, a gigantic "
 "soft bust, and below it a waistline that still draws in even at this size — the one place her outline turns inward. " + WAIST_PATCH +
 " A great mass of soft heavy flesh stacked in {rolls} heavy rounded rolls one above the other, deep shadowed creases between them, not pregnant, "
 "colossal wide hips seven times the width of that waistline, each thigh wider than a normal woman is tall, the quads showing through the "
 "softness in broad blunt swells."),
"topheavy": ("톱헤비 아워글래스", "TOP-HEAVY HOURGLASS",
 "A colossal bust far wider than her shoulders, curving forward as one enormous rounded mass and resting with real weight against her upper "
 "body, the bust more than seven times the width of her waistline — and below that bust a waistline that still pulls in clearly even at this "
 "size, the one place on her whole body where the outline turns inward. " + WAIST_PATCH +
 " Below it enormous round hips flaring out to more than three times the width of her shoulders, colossal thick thighs each wider than a "
 "normal woman is tall, pressing together down to the knees, thick heavy calves, thick soft upper arms, not pregnant. The bust merges smoothly "
 "into her chest and shoulders as one continuous body, no gap, no seam."),
}

MAT = {
"najeon": ("나전칠기", "Korean najeon mother-of-pearl lacquer body painting", "glossy black lacquer covered with shimmering iridescent mother-of-pearl arabesque vines, peonies and cranes glowing pink, aqua and silver", "iridescent pearl-white", "the mother-of-pearl shimmering with rainbow iridescence"),
"makie": ("마키에", "Japanese maki-e lacquer body painting", "glossy black lacquer with sprinkled gold powder shading into autumn grasses, chrysanthemums, plum branches and full moons", "gold", "the gold powder glittering"),
"palekh": ("팔레흐", "Russian Palekh lacquer miniature body painting", "glossy mirror-black lacquer with ultra-fine gold filigree, firebirds, blossoms and tiny folk-tale scenes in red, gold and emerald", "red lacquer with gold trim", "the gold filigree glinting against the black"),
"khokhloma": ("호홀로마", "Russian Khokhloma body painting", "a deep black ground with brilliant gold and vermilion strawberry vines, rowan berries and curling leaves painted in confident brushstrokes", "vermilion", "the gold and vermilion glowing against the black"),
"laironam": ("라이롯남", "Thai lai rot nam body painting", "brilliant gold leaf over black lacquer, continuous kranok flame scrolls wrapping the shoulders, arms, belly and thighs", "gold", "the gold leaf blazing"),
"cloisonne": ("칠보", "cloisonné enamel body painting", "a brilliant turquoise enamel ground with lotus scrolls and peonies in coral red, cobalt and white, every colour cell outlined by raised gold wires", "turquoise", "the gold wires glinting on the turquoise enamel"),
"dancheong": ("단청", "Korean dancheong temple polychrome body painting", "brilliant cobalt blue, malachite green, vermilion red, white and gold geometric lotus and cloud motifs with crisp white outlines", "cobalt-blue", "the vivid dancheong colours blazing"),
"fordite": ("포다이트", "polished fordite body painting", "thin layered strata of candy red, teal, mustard yellow, cobalt, white and orange, glossy as polished stone", "candy-red", "the polished colour bands gleaming"),
"eunipsa": ("은입사", "Korean eunipsa silver inlay body painting", "a deep black iron ground with thick bright silver wire covering most of the surface, fine lattice fills between the lines", "silver", "the silver wire gleaming on the black"),
"imari": ("이마리", "Imari-palette body painting", "cobalt blue underglaze scrolls, lotus and cranes joined by iron-red overglaze enamel and raised gilt accents, three colours layered together", "cobalt-and-red", "the red and gilt catching warm highlights over the blue"),
"jasperware": ("웨지우드 재스퍼", "Wedgwood jasperware body painting", "a matte pale blue-white ground with crisp white applied relief scrolls, peonies and classical figures standing slightly proud of the surface", "pale blue", "the white relief standing crisp against the matte blue"),
"cheonghwa": ("청화백자", "blue-and-white porcelain body painting", "a brilliant white ground with cobalt peony scrolls, lotus, vines and cranes", "white", "the white ground reading bright with crisp cobalt"),
"celadon": ("청자 상감", "Korean celadon inlay body painting", "a soft pale jade-green glaze ground inlaid with crisp white and black slip cranes, clouds and chrysanthemum medallions", "pale jade-green", "the pale glaze glowing and the inlaid cranes reading crisp"),
"jajuyo": ("자주요 흑유", "Cizhou sgraffito ceramic body painting", "a glossy jet-black glaze carved away to bold cream-white peony scrolls and leafy vines", "cream-white", "the black glaze gleaming"),
}


MAT_ENG = {
"najeon": "najeon mother-of-pearl", "makie": "maki-e", "palekh": "Palekh", "khokhloma": "Khokhloma",
"laironam": "lai rot nam", "cloisonne": "cloisonné enamel", "dancheong": "dancheong", "fordite": "fordite",
"eunipsa": "eunipsa silver-inlay", "imari": "Imari", "jasperware": "jasperware", "cheonghwa": "blue-and-white porcelain",
"celadon": "celadon inlay", "jajuyo": "Cizhou sgraffito",
}

NATION = {
"kr_idol": ("한국 아이돌", "a Korean woman", "with the polished look of a K-pop idol, fair ivory skin with a warm golden undertone, smooth high cheekbones with a gently tapering jaw and a small delicate chin, large clear dark eyes with a soft double lid, straight softly arched brows, a slender nose and full rounded lips",
 ["long straight glossy black hair with a soft see-through fringe", "a sleek chin-length bob with a blunt cut", "long dark brown hair in soft loose curls with a centre part", "long honey-brown hair in soft beach waves with a deep side part"],
 ["a bright confident smile", "a calm composed smile", "a cool composed expression, feminine face"], ["early 20s","late 20s","early 30s"]),
"jp_idol": ("일본 아이돌", "a Japanese woman", "with the sweet look of a Japanese idol, fair skin with a soft neutral undertone, soft full cheeks with a gently tapering jaw and a small chin, very large round dark eyes with a wide gaze, softly rounded brows, a small nose and small full lips",
 ["long black hair with a straight blunt fringe and loose waves at the ends", "a blunt shoulder-length cut with a straight fringe"], ["a bright cheerful smile","a gentle cheerful smile"], ["early 20s","late 20s"]),
"cn_idol": ("중국 아이돌", "a Chinese woman", "with the polished look of a C-pop idol, fair porcelain-pale skin with a cool undertone, smooth high cheekbones with a gently tapering jaw and a small round chin, large clear almond eyes with a soft double lid, willow-leaf brows, a small nose and small full lips",
 ["long straight black hair with a centre part falling past her shoulders", "a sleek low ponytail with a straight fringe"], ["a gentle cheerful smile","a serene assured expression"], ["early 20s","late 20s","early 30s"]),
"indian": ("인도 미인", "an Indian woman", "with the refined features of a high fashion model — a flawless oval face with warm deep-golden brown skin, high sculpted cheekbones, a clean jawline, very large deep almond eyes under strong arched brows, heavy dark lashes, a straight elegant nose and full sculpted lips, thick black kohl rimming both eyes and drawn into a fine tail, a deep red lip",
 ["long jet-black hair in heavy glossy waves","long black hair swept into a low twisted chignon"], ["a calm direct gaze","a serene assured expression"], ["late 20s","early 30s"]),
"gulf": ("중동 걸프 미인", "a Gulf Arab woman", "with the refined features of a high fashion model — a flawless oval face with warm olive skin, high sculpted cheekbones, a clean jawline, very large deep-set dark eyes under strong dark brows, heavy lashes, a straight elegant nose with a fine high bridge and full well-defined lips, dense black kohl rimming both eyes and smoked outward at the corners, a warm bronze eyeshadow, a soft nude-rose lip",
 ["long jet-black hair in heavy glossy waves","long black hair swept into a low twisted chignon"], ["a calm direct gaze","a serene composed expression"], ["late 20s","early 30s"]),
"latina": ("라틴 미인", "a Latina woman", "with the refined features of a high fashion model — a flawless oval face with warm golden-bronze skin, high sculpted cheekbones, a clean jawline, large dark almond eyes under strong dark brows, heavy lashes, a straight elegant nose and full richly shaped lips, a sharp black winged liner, a warm terracotta eyeshadow, a deep berry lip",
 ["a high sleek ponytail with a few strands loose at the temples","long dark brown hair in loose waves swept over one shoulder"], ["a calm direct gaze","a calm powerful smile, feminine face"], ["late 20s","early 30s"]),
}
SILVER_NOTE = ("a striking silver-haired beauty, her hair turned early — her face still young and firm with only the faintest lines "
 "at the outer corners of her eyes, a full head of natural silver-white hair")
SILVER_HAIR = ["in a sharp shoulder-length bob with a deep side part", "swept into a sleek low chignon with a few strands loose at the temples", "in loose glossy waves"]
SILVER_AGE = ["early 40s", "mid 40s"]

CLOSING = ("Her head looks tiny on top of her massive body — no wider than a tenth of her own hips — and each hand is as wide as a normal "
 "woman's torso, each finger as thick as a normal woman's arm. Every roll keeps its own clear rounded outline with a deep shadowed crease "
 "between them, never merging into one shapeless mass; her arms, hands, legs and feet stay in correct proportion to one another.")

def shoulder_patch(mat_eng):
    return (f"The same {mat_eng} pattern lies flat and continuous across the top of each shoulder, over each deltoid and down into the chest "
            f"with no seam, no strap and no separate panel of colour anywhere at the shoulder — the paint simply follows the flesh over that "
            f"curve exactly as it does everywhere else on her.")

POSE_STANDFRONT = "Pose: Standing full frontal, feet planted very wide apart, arms held well away from her body with a visible gap of background at each side, full body head to toe."
POSE_STAND34 = "Pose: Standing turned about 45 degrees with the front of her body still mostly facing the viewer, her face toward the camera, the stacked rolls seen in side profile, the enormous curve of her hips and rear jutting out behind her, feet planted wide apart, arms held clear of her body with a gap at each side, full body head to toe."
POSE_BENCH = "Pose: Seated on a stone bench that her body completely engulfs, her hips turned about 45 degrees away from the camera so the great curve of her rear is seen from the side, her torso twisted back toward the viewer and her face turned to the camera, her near knee toward the camera and her far leg angled away, one hand resting back behind her hip and the other on her near thigh, both arms held clear of her body, full body head to toe."
POSE_KNEEL = "Pose: Kneeling upright square to the camera on a low stone plinth, her knees planted directly beneath her body and set apart, not squatting and not crouching, her calves folded flat back beneath her and her weight settled down onto her heels, her spine held straight and vertical, her face to the camera, arms held clear of her body with a gap of background at each side, full body head to toe."
POSE_LIE = "Pose: Lying on her side on a low platform facing the viewer, her head resting on her raised hand with that elbow planted behind her body so her arm never crosses in front of her torso, her other arm lifted clear and resting on the top of her upper hip with the elbow raised, her legs stacked one on the other with the knees slightly bent, her body stretching across the full width of the frame from edge to edge."

BG = ["A dark charcoal stylized background", "A dark deep-burgundy stylized background", "A dark deep-navy stylized background", "A dark plum-purple stylized background"]

def gen_face(rng, nat_key, silver):
    label, eng, face, hairs, smiles, ages = NATION[nat_key]
    if silver:
        return f"{label} 실버폭스", eng, rng.choice(SILVER_AGE), face, f"{SILVER_NOTE} {rng.choice(SILVER_HAIR)}", rng.choice(["a quiet assured expression","a serene composed expression"])
    return label, eng, rng.choice(ages), face, rng.choice(hairs), rng.choice(smiles)

def solo(rng, idx):
    bkey = rng.choice(list(BODY_NW.keys()))
    body_kr, body_caps, body_tpl, needs_shoulder = BODY_NW[bkey]
    mkey = rng.choice(list(MAT.keys()))
    mat_kr, mat_full, mat_desc, shoe, light = MAT[mkey]
    silver = rng.random() < 0.15
    nat = rng.choice(list(NATION.keys()))
    kr, eng, age, face, hair, smile = gen_face(rng, nat, silver)
    rolls = rng.choice([6,7]); rolls_small = rng.choice([4,5])
    lowroll = rng.choice(["the lowest roll resting heavy and solid on the floor in front of her feet",
                           "the lowest roll settled low and solid, its weight resting flat against the ground"])
    sp = shoulder_patch(MAT_ENG[mkey]) if needs_shoulder else ""
    body_text = body_tpl.format(rolls=rolls, rolls_small=rolls_small, lowroll=lowroll, shoulder_patch=sp)

    pose_key = rng.choices(["standfront","stand34","bench","kneel","lie"], weights=[24,24,20,20,12])[0]
    if pose_key == "lie":
        head = "Image format: a horizontal landscape-orientation illustration, 3:2 aspect ratio, wider than it is tall."
        end = "Horizontal 3:2 landscape-orientation full-body illustration, wider than it is tall."
        aspect = "3:2"
        pose = POSE_LIE
        body_text = body_text.replace("her hips are cut off far inside the left and right edges of the frame and her head nearly touches the top edge",
                                       "her head and her feet are cut off far inside the left and right edges of the frame, her body filling the full height of the picture")
    else:
        head = "Image format: a vertical portrait-orientation illustration, 2:3 aspect ratio, taller than it is wide."
        end = "Vertical 2:3 portrait-orientation full-body illustration, taller than it is wide."
        aspect = "2:3"
        pose = {"standfront": POSE_STANDFRONT, "stand34": POSE_STAND34, "bench": POSE_BENCH, "kneel": POSE_KNEEL}[pose_key]
        if pose_key in ("bench", "kneel"):
            body_text += " She is so vast that the stone bench beneath her is completely buried and invisible." if pose_key=="bench" else ""

    subject = f"Subject: ONE mature adult woman, {eng} in her {age}, with clearly adult facial features, {face}, {hair}, {smile}."
    body_art = f"Body Art: Full body {mat_full} on her bare skin from the collarbones to the ankles, {mat_desc}. The pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly and the calves, covering them as densely as the chest."
    physique = f"Physique: {body_caps} PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond any real anatomy and beyond anything a living body could be, around 5,000 pounds — a mountain of a woman. {body_text} {CLOSING}"
    footwear = f"Footwear: Extreme {shoe} platform stiletto slingbacks, the platform soles as tall as her ankle bones, the ultra-thin stiletto heels so high her insteps stand nearly vertical."
    bg = rng.choice(BG)
    background = f"Background & Lighting: {bg}, barely visible behind her, a single strong warm light from one side, deep soft shadows in every crease, {light}, glossy anime highlights on every curve."
    style = "Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant saturated colors, polished professional anime art — not a photograph."

    prompt = "\n\n".join([head, style, subject, body_art, physique, pose, footwear, background, end])
    title = f"Mountain Mass Solo {idx:02d} · {body_kr}({kr}) · {mat_kr} · {pose_key}"
    key = f"la_mountain_solo_{idx:02d}_{bkey}_{mkey}_{pose_key}"
    return {"title": title, "category": "🏺 Living Artifact · Mountain Mass", "platform": "gemini", "aspect_ratio": aspect, "prompt": prompt}, key

def duo(rng, idx):
    pool = list(BODY_NW.keys()) + list(BODY_W.keys())
    bL, bR = rng.sample(pool, 2)
    def resolve(bk, rolls, rolls_small):
        if bk in BODY_NW:
            kr, caps, tpl, needs_shoulder = BODY_NW[bk]
            lowroll = "the lowest roll resting heavy and solid on the floor in front of her feet"
            sp_placeholder = needs_shoulder
            return kr, caps, tpl, lowroll, sp_placeholder, False
        else:
            kr, caps, tpl = BODY_W[bk]
            return kr, caps, tpl, None, False, True

    mL, mR = rng.sample(list(MAT.keys()), 2)
    matL_kr, matL_full, matL_desc, shoeL, lightL = MAT[mL]
    matR_kr, matR_full, matR_desc, shoeR, lightR = MAT[mR]

    silverL = rng.random() < 0.15; silverR = rng.random() < 0.15
    natL = rng.choice(list(NATION.keys())); natR = rng.choice(list(NATION.keys()))
    krL, engL, ageL, faceL, hairL, smileL = gen_face(rng, natL, silverL)
    krR, engR, ageR, faceR, hairR, smileR = gen_face(rng, natR, silverR)

    rollsL = rng.choice([6,7]); rollsL_small = rng.choice([4,5])
    rollsR = rng.choice([6,7]); rollsR_small = rng.choice([4,5])

    kr1, caps1, tpl1, lowroll1, needs_sh1, is_waist1 = resolve(bL, rollsL, rollsL_small)
    kr2, caps2, tpl2, lowroll2, needs_sh2, is_waist2 = resolve(bR, rollsR, rollsR_small)

    sp1 = shoulder_patch(MAT_ENG[mL]) if needs_sh1 else ""
    sp2 = shoulder_patch(MAT_ENG[mR]) if needs_sh2 else ""

    bodyL_text = tpl1.format(rolls=rollsL, rolls_small=rollsL_small, lowroll=lowroll1 or "", shoulder_patch=sp1)
    bodyR_text = tpl2.format(rolls=rollsR, rolls_small=rollsR_small, lowroll=lowroll2 or "", shoulder_patch=sp2)

    left = (f"Left woman: {engL} in her {ageL}, {faceL}, {hairL}, {smileL}. {caps1} PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, "
            f"exaggerated far beyond any real anatomy and beyond anything a living body could be, around 5,000 pounds — a mountain of a "
            f"woman. {bodyL_text} {CLOSING} Full body {matL_full} on her bare skin from the collarbones to the ankles, {matL_desc}. "
            f"The pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly and the "
            f"calves, covering them as densely as the chest.")
    right = (f"Right woman: {engR} in her {ageR}, {faceR}, {hairR}, {smileR}. {caps2} PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, "
             f"exaggerated far beyond any real anatomy and beyond anything a living body could be, around 5,000 pounds — a mountain of a "
             f"woman. {bodyR_text} {CLOSING} Full body {matR_full} on her bare skin from the collarbones to the ankles, {matR_desc}. "
             f"The pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly and the "
             f"calves, covering them as densely as the chest.")

    coverage = ("Coverage: Where the two women's bodies press together at hip and side, the flesh of each bulges into the gap and presses "
                "flat against the other, each woman's own rounded outline still clearly her own on either side of that pressed seam.")
    pose = "Pose: Both standing full frontal, feet planted very wide apart, arms held clear of their bodies, neither arm crossing in front of her own body or the other woman's."
    footwear = (f"Footwear: The left woman wears extreme {shoeL} platform stiletto mules; the right woman wears extreme {shoeR} platform "
                f"stiletto mules; the platform soles as tall as their ankle bones, the ultra-thin stiletto heels so high their insteps "
                f"stand nearly vertical.")
    bg = rng.choice(BG)
    background = (f"Background & Lighting: {bg}, barely visible behind them, a single strong warm light from the left, deep soft shadows "
                  f"in every crease and where the two bodies press together, {lightL} and {lightR}, glossy anime highlights on every curve.")
    style = "Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant saturated colors, polished professional anime art — not a photograph."
    subj = ("Subject: TWO mature adult women standing side by side, both with clearly adult facial features, both full body head to toe, "
            "both faces toward the camera. The camera is set close so the two of them fill the frame edge to edge — their bodies together "
            "overflow the full width of the frame and run off both the left and right edges, their heads near the top edge and their heels "
            "near the bottom, with almost no background visible. They stand pressed shoulder to shoulder and hip to hip, the flesh bulging "
            "out where they touch.")
    head = "Image format: a vertical portrait-orientation illustration, 2:3 aspect ratio, taller than it is wide."
    end = "Vertical 2:3 portrait-orientation full-body illustration, taller than it is wide."

    prompt = "\n\n".join([head, style, subj, left, right, coverage, pose, footwear, background, end])
    title = f"Mountain Mass Duo {idx:02d} · {kr1}({krL}) × {kr2}({krR}) · {matL_kr}×{matR_kr}"
    key = f"la_mountain_duo_{idx:02d}_{bL}-{bR}_{mL}-{mR}"
    return {"title": title, "category": "🏺 Living Artifact · Mountain Mass", "platform": "gemini", "aspect_ratio": "2:3", "prompt": prompt}, key

def validate(items):
    seen = set()
    for data, key in items:
        assert data["prompt"].startswith("Image format")
        assert data["prompt"].rstrip().endswith("taller than it is wide.") or data["prompt"].rstrip().endswith("wider than it is tall.")
        assert key not in seen, key
        seen.add(key)


def build_all(rng):
    items = []
    used = set()
    i = 1
    while len([1 for d, k in items if "_solo_" in k]) < N_SOLO:
        data, key = solo(rng, i)
        if key not in used:
            used.add(key)
            items.append((data, key))
        i += 1
    i = 1
    while len([1 for d, k in items if "_duo_" in k]) < N_DUO:
        data, key = duo(rng, i)
        if key not in used:
            used.add(key)
            items.append((data, key))
        i += 1
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()

    rng = random.Random(SEED)
    items = build_all(rng)
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
            f.write(f"# Living Artifact · Mountain Mass ({N_SOLO + N_DUO})\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")


if __name__ == "__main__":
    main()
