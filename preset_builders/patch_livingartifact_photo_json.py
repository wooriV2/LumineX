# -*- coding: utf-8 -*-
"""
Living Artifact · Photo Direct 001-252  (실사 직접 생성, 애니 경유 없음)
- 7체형 × (세로 24 + 가로 12) = 252
- 자세 11종
  세로 2:3 (8) 선 정면 / 선 3/4 / 걸터앉기 3/4 / 쪼그려 정면 / 쪼그려 3/4 /
               무릎 정면(한쪽 무릎) / 무릎 3/4(양 무릎) / 무릎 옆(양 무릎)
  가로 3:2 (3) 옆으로 누운 자세 / 엎드린 자세 / 비스듬히 기대앉기
- 다양성: 인종 6 · 연령 4 · 재질 14 · 헤어 20 · 신발 20 · 네일 20 · 귀걸이 20
- 규칙(v5.5)
  * 배경: 무지(대부분) / 갤러리 돌 벤치(걸터앉기). 외부 기준물·광각 앙각 불채택
  * 화면 점유 문구, Skin 문단 독립, 문양은 살 위 물감, 깨짐 방지 2줄, 팔이 몸 앞을 가리지 않음
  * 복부: 겹 + 지방량·무게 절충안, 자세별로 중력 방향을 바꿔 서술
  * 각도 체계는 정면 / 3/4 / 옆 세 가지만 사용 (22도·67도 불채택)
- output: presets/la_photo_{001..252}_*.json   options: --force, --md review.md
"""
import json, os, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Photo Direct"
CAM = ("shot on a medium format camera with an 85mm lens at f/8, a single hard key light raking in from one side so the "
       "texture of the skin stands out, sharp focus from head to toe, realistic photographic grain — a real photograph, "
       "not an illustration, not CGI, not a render.")
V_HEAD = "Image format: a vertical portrait-orientation photograph, 2:3 aspect ratio, taller than it is wide."
V_END = "Vertical 2:3 portrait-orientation full-body photograph, taller than it is wide."
H_HEAD = "Image format: a horizontal landscape-orientation photograph, 3:2 aspect ratio, wider than it is tall."
H_END = "Horizontal 3:2 landscape-orientation full-body photograph, wider than it is tall."
SET = {
 "studio": "A full-body photograph on a plain seamless {bg} backdrop, nothing else in the frame, " + CAM,
 "gallery": ("A full-body photograph in a bare gallery space with a plain smooth {bg} wall behind her, nothing in the frame "
             "but a single backless bench carved from a solid block of pale grey stone, " + CAM),
 "platform": ("A full-body photograph on a plain seamless {bg} backdrop, nothing in the frame but a low flat platform, " + CAM),
 "recline": ("A full-body photograph on a plain seamless {bg} backdrop, nothing in the frame but a low flat platform with a "
             "plain padded backrest at one end, " + CAM),
}
GUARD = ("Every fold and curve keeps its own clear rounded outline with a deep shadowed crease between them, never merging "
         "into one shapeless mass. Her arms, hands, legs and feet stay in correct proportion to each other.")
SCALE = "Her head looks small on top of her massive body and her hands look small against her thighs."
PAINT = ("The paint is pigment sitting on living skin, so it distorts slightly over every bulge and cracks a little where "
         "the skin folds.")
COVER = ("The paint covers her whole body with no bare skin left anywhere below the jaw: her shoulders, her upper arms, her "
         "forearms and the backs of her hands are painted as densely as her torso, and so are the sides of her body, her back, "
         "her rear, the lower belly, the knees, the calves and the tops of her feet. Her face is left unpainted and the "
         "pattern fades out at the neck with no hard line.")
SOFT = ("the surface soft and uneven, never taut, never smooth, never round like a drum. It merges seamlessly into her sides, "
        "her hips and her thighs with no boundary anywhere, one continuous body rather than a separate mass, not pregnant.")

def cap(t): return t[0].upper() + t[1:]

def belly(mode, big):
    n = "three or four" if big else "two or three"
    mass = "an immense mass of soft heavy fat" if big else "a great mass of soft heavy fat"
    low = "toward the knees" if big else "over the tops of her thighs"
    return {
 "stand": f"{mass} sits on her middle, so much of it that it hangs far lower than it projects — sagging down {low} under its own "
          f"weight rather than pushing forward, gathering into {n} heavy rounded folds stacked one above the other as it falls, "
          f"each fold thicker than the one above it, deep shadowed creases between them, {SOFT}",
 "sit":   f"{mass} sits on her middle and settles down over her thighs as she sits, spreading forward and outward under its own "
          f"weight and reaching down between her knees, gathering into {n} heavy rounded folds as it falls, deep shadowed "
          f"creases between them, {SOFT}",
 "squat": f"{mass} sits on her middle and drops straight down between her parted knees under its own weight, settling onto the "
          f"tops of her thighs and spreading down toward the floor, gathering into {n} heavy rounded folds as it compresses, "
          f"deep shadowed creases between them, {SOFT}",
 "kneel": f"{mass} sits on her middle and drops straight down from it under its own weight, projecting far forward past the line "
          f"of her own knees before it falls, settling onto the tops of her thighs and piling over them, gathering into {n} heavy "
          f"rounded folds as it falls, deep shadowed creases between them, {SOFT}",
 "side":  f"{mass} sits on her middle and, even as she lies on her side, spills forward away from her body and hangs over the "
          f"front edge of her torso under its own weight, the lowest part sagging down onto the platform, gathering into {n} "
          f"heavy rounded folds stacked one in front of the other, deep shadowed creases between them, {SOFT}",
 "prone": f"{mass} on her middle is squeezed out past her body on both sides where her weight presses it against the platform, "
          f"spreading sideways into {n} heavy rounded folds with deep shadowed creases between them, {SOFT}",
 "recl":  f"{mass} sits on her middle and spills forward down the slope of her own raised torso under its own weight, piling up "
          f"over the tops of her thighs and reaching toward her knees, gathering into {n} heavy rounded folds stacked one in "
          f"front of the other, deep shadowed creases between them, {SOFT}",
    }[mode]

WAIST = ("a waistline that still draws in clearly even at this size — a shadowed groove running around her middle, the one place "
         "on her body where the outline pulls inward")
HG = "Wide at the bust, drawn in at the waistline, wide again below: the silhouette reads as a great hourglass at the most extreme size."

def ussbbw(m):
    return (f"{cap(belly(m, True))} A gigantic bust resting on the top fold, no waist at all, colossal hips more than "
            f"three times the width of her shoulders and an enormous rounded rear, each thigh thicker than a normal woman's "
            f"waist, thick heavy calves, very thick upper arms, a full round face. {SCALE} {GUARD}")
def hg_ussbbw(m):
    return (f"A colossal heavy bust far wider than her shoulders, and below it {WAIST}. Below that waistline {belly(m, True)} "
            f"Colossal hips more than three times the width of that waistline and a gigantic rounded rear, each thigh thicker "
            f"than a normal woman's waist, thick heavy calves, very thick upper arms, a full round face. {SCALE} {HG} {GUARD}")
def hg_ssbbw(m):
    return (f"A colossal heavy bust far wider than her shoulders, and below it {WAIST}. Below that waistline {belly(m, False)} "
            f"Enormous round hips more than three times the width of that waistline and far wider than her shoulders, a gigantic "
            f"rounded rear, gigantic soft thighs pressing together down to the knees, huge soft calves, very thick soft arms, a "
            f"full round face. {SCALE} {HG} {GUARD}")
def muscle_hg(m):
    return (f"Huge rounded shoulders and massive thick arms with the swell of the biceps and triceps showing through a soft layer "
            f"of fat, a colossal heavy bust far wider than her shoulders, and below it {WAIST}, the muscle of her core firm "
            f"beneath it. Below that waistline {belly(m, False)} Enormous round hips more than three times the width of that "
            f"waistline, a gigantic powerful rear, colossal thighs with the great sweep of the quads visible under a soft layer, "
            f"thick heavy calves with a diamond shape showing through, a full round face. {SCALE} {HG} Powerful and heavy at once, "
            f"no bodybuilder leanness, the weight of the flesh visible in how it hangs over the muscle beneath. {GUARD}")
def athletic(m):
    return (f"The body of a world's strongest woman pushed far past real limits: enormously broad thick shoulders, massive heavy "
            f"arms so thick they cannot hang flat against her sides, a colossal bust, a huge barrel torso, no waist at all. On her "
            f"middle. {cap(belly(m, False))} Colossal wide hips and a huge rounded powerful rear, tree-trunk thighs pressing together "
            f"down to the knees, thick heavy calves. Immense power under a thick layer of soft fat: the muscle is huge but rounded "
            f"and buried, only broad blunt swells at the shoulders, upper arms and thighs, no sharp muscle separation anywhere, no "
            f"carved abs. {SCALE} {GUARD}")
def colossal(m):
    return ("A giantess built on a completely even scale, every part of her enlarged by the same amount: massive rounded shoulders, "
            "huge thick arms, a colossal full bust, a broad heavy torso with a large smooth rounded belly, wide solid hips, "
            "enormous columnar thighs and thick heavy calves, a full round face. Her head looks small on top of her massive body, "
            "her shoulders span more than four head-widths, each hand is as wide as a normal woman's torso and each thigh thicker "
            "than a normal woman's waist. No single part stands out more than another, no hanging folds, not pregnant, her whole "
            f"body scaled up together into one immense smooth silhouette that towers over the viewer. {GUARD}")
def tentpole(m):
    return (f"A giant hourglass frame that flares out at both ends: enormous flaring lats spreading to shoulders twice the width of "
            f"a normal woman's, massive rounded deltoids stacked on top of them, huge thick arms pushed far out from her sides by "
            f"the width of her back, a smooth rounded neck, a colossal bust projecting forward past the line of her shoulders, no "
            f"waist at all. {cap(belly(m, False))} Below it colossal wide hips just as broad as her shoulders, a huge "
            f"rounded rear, colossal thighs pressing together down to the knees and thick heavy calves. Her head looks small on top "
            f"of her massive frame and her shoulders span more than five head-widths. Wide above and wide below; the muscle is huge "
            f"but rounded and soft-edged under a thick layer of fat, no bodybuilder look. {GUARD}")

BODY = {
 "ussbbw": ("USSBBW", ussbbw), "hourglassussbbw": ("아워글래스 USSBBW", hg_ussbbw),
 "hourglassssbbw": ("아워글래스 SSBBW", hg_ssbbw), "musclehourglass": ("머슬 아워글래스 BBW", muscle_hg),
 "athleticussbbw": ("애슬리트 USSBBW", athletic), "colossal": ("콜로설", colossal),
 "tentpole": ("텐트폴 USSBBW", tentpole),
}

W_HANG = "The sheer weight of the flesh is visible in how every part hangs, settles and presses against the part below it."
W_SIT = "The sheer weight of the flesh is visible in how it settles, spreads and presses down against the hard stone beneath her."
W_SQUAT = "The sheer weight of the flesh is visible in how it drops, compresses and presses out to the sides wherever two parts of her body meet."
W_KNEEL = "The sheer weight of the flesh is visible in how it drops, settles and presses down onto the thighs beneath it."
W_LIE = "The sheer weight of the flesh is visible in how it spills forward, sags downward and presses flat against the platform beneath her."
W_PRONE = "The sheer weight of the flesh is visible in how it spreads sideways and presses flat against the platform beneath her."
W_RECL = "The sheer weight of the flesh is visible in how it spills forward down her body, settles and presses flat against the platform beneath her."
OCC_V = "her body so wide that her hips are cut off by the left and right edges of the frame"
OCC_DEEP = "her body so deep from front to back that her belly reaches beyond one edge of the frame and her rear beyond the other"
OCC_BENCH = "her body so wide that it overflows the stone bench on both sides and is cut off by the left and right edges of the frame"
OCC_H = "her body so long and vast that her head and her feet are cut off by the left and right edges of the frame"

POSE = {
"stand_front": ("선 자세 정면", "v", "studio", "stand", OCC_V, W_HANG,
 "Pose: Standing square to the camera, full frontal, feet planted far apart, the heavy mass of her middle resting down on her "
 "thighs, arms held clear of her body with a visible gap of background between each arm and her side so her whole outline reads "
 "unbroken, full body head to toe."),
"stand_34": ("선 자세 3/4", "v", "studio", "stand", OCC_V, W_HANG,
 "Pose: Standing turned about 45 degrees from the camera with the front of her body still mostly toward the lens, her face toward "
 "the camera, the great mass of her middle seen in side profile and the enormous curve of her hips and rear projecting behind her, "
 "feet planted apart, arms held clear of her body with a visible gap of background between each arm and her side, full body head to toe."),
"bench_34": ("걸터앉기 3/4", "v", "gallery", "sit", OCC_BENCH, W_SIT,
 "Pose: Seated on the backless stone bench with her hips turned about 45 degrees away from the camera so the great curve of her "
 "rear and one hip spreading out on the stone is seen from the side, her torso twisted back toward the lens and her face turned to "
 "the camera, the great mass of her middle settling forward over her thighs seen at an angle, her near knee toward the camera and "
 "her far leg angled away, one hand resting back on the bench behind her hip and the other resting on her near thigh, both arms "
 "held clear of her body so nothing crosses in front of her torso, her feet flat on the floor, the flesh of her thighs bulging out "
 "above and below where the hard front edge of the bench presses into them, full body head to toe."),
"squat_front": ("쪼그려 앉기 정면", "v", "studio", "squat", OCC_V, W_SQUAT,
 "Pose: Squatting low facing the camera, balanced on the balls of her feet with the heels of her shoes lifted clear of the floor, "
 "her knees pushed wide apart by the bulk of her own thighs, her back straight and her torso upright, her calves squeezed flat "
 "beneath her thighs with the flesh of both bulging out where they meet, her hands resting on her knees with her arms held clear of "
 "her body so nothing crosses in front of her torso, her head level and facing the lens, full body head to feet filling the frame."),
"squat_34": ("쪼그려 앉기 3/4", "v", "studio", "squat", OCC_V, W_SQUAT,
 "Pose: Squatting low and turned about 45 degrees from the camera with the front of her body still mostly toward the lens, her face "
 "toward the camera, balanced on the balls of her feet with the heels of her shoes lifted clear of the floor, her knees pushed wide "
 "apart by the bulk of her own thighs, her back straight, the enormous rear settling down low behind her seen in partial profile, "
 "her hands resting on her knees with her arms held clear of her body, full body head to feet filling the frame."),
"kneel_front": ("무릎 꿇기 정면 (한쪽 무릎)", "v", "platform", "kneel", OCC_V, W_KNEEL,
 "Pose: Kneeling on one knee on the platform facing the camera, one shin and foot folded back beneath her with that thigh lying "
 "flat, the other knee raised in front of her with the foot planted flat on the platform, the great mass of her middle settling "
 "down over the flat thigh on one side and pressing against the raised thigh on the other, her back straight, her hands resting on "
 "her thighs with her arms held clear of her body so nothing crosses in front of her torso, her head level and facing the lens, "
 "full body head to feet filling the frame."),
"kneel_34": ("무릎 꿇기 3/4 (양 무릎)", "v", "platform", "kneel", OCC_V, W_KNEEL,
 "Pose: Kneeling upright on the platform and turned about 45 degrees from the camera with the front of her body still mostly toward "
 "the lens, her face toward the camera, both shins and feet folded back beneath her and her weight settled onto her heels, her knees "
 "wide apart, her back straight, her near hand resting on her thigh and her far arm held back so nothing crosses in front of her "
 "torso, the enormous rounded rear settling back onto her heels seen in partial profile, full body head to knees filling the frame."),
"kneel_side": ("무릎 꿇기 옆 (양 무릎)", "v", "platform", "kneel", OCC_DEEP, W_KNEEL,
 "Pose: Kneeling upright on the platform seen from directly to her side, both calves folded beneath her thighs and her rear settled "
 "back onto her heels, her back straight, her near hand resting on her thigh and her far arm held back so nothing crosses in front "
 "of her torso, her head turned toward the camera, the whole depth of her body read from the side, full body head to knees filling the frame."),
"lying_side": ("옆으로 누운 자세", "h", "platform", "side", OCC_H, W_LIE,
 "Pose: Lying on her side on the platform facing the camera, her head resting on her raised hand with that elbow planted on the "
 "platform behind her body so her arm never crosses in front of her torso, her other arm lifted clear of her body and resting "
 "lightly on the top of her hip with the elbow raised, a visible gap of background between that arm and her side so the whole curve "
 "of her waist, hip and belly reads unbroken, her legs stacked one on the other with the knees slightly bent, her upper hip rising "
 "as a great rounded mound higher than her own shoulder and the underside hip and thigh flattening wide where they press against "
 "the platform, her body stretching across the full width of the frame from edge to edge."),
"prone": ("엎드린 자세", "h", "platform", "prone", OCC_H, W_PRONE,
 "Pose: Lying face down on the platform, her upper body propped up on both forearms with her elbows planted wide apart and her head "
 "raised and turned toward the camera, her legs straight and slightly apart, a colossal rear rising as two enormous rounded mounds "
 "far above the line of her back with a deep shadowed cleft between them, her broad heavy back built from massive horizontal rolls "
 "of soft flesh, her thighs flattening wide where they meet the platform, her body stretching across the full width of the frame "
 "from edge to edge."),
"recline": ("비스듬히 기대앉기", "h", "recline", "recl", OCC_H, W_RECL,
 "Pose: Reclining on the platform propped up against the backrest at about 45 degrees, her legs stretched out straight in front of "
 "her and slightly apart, her arms resting back on the platform behind her hips with the elbows out so nothing crosses in front of "
 "her torso, her head turned toward the camera, her colossal hips and rear spreading wide and flattening against the platform, her "
 "body stretching across the full width of the frame from edge to edge."),
}
V_POSES = ["stand_front", "stand_34", "bench_34", "squat_front", "squat_34", "kneel_front", "kneel_34", "kneel_side"]
H_POSES = ["lying_side", "prone", "recline"]
PLAN = [p for p in V_POSES for _ in range(3)] + [p for p in H_POSES for _ in range(4)]

ETHNIC = [
 ("흑인", "Black", "deep near-black skin tone, THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, void complexion, not brown, not lightened, her face exactly as dark as her body", False),
 ("한국", "Korean", "warm ivory skin tone with a soft golden undertone, her face exactly the same tone as her body", True),
 ("라틴", "Latina", "warm golden-tan skin tone with olive undertones, her face exactly the same tone as her body", True),
 ("북유럽", "Scandinavian", "very fair skin tone with cool pink undertones and faint freckling across the shoulders, her face exactly the same tone as her body", True),
 ("남아시아", "South Asian", "rich warm brown skin tone with golden undertones, her face exactly the same tone as her body", True),
 ("동아프리카", "East African", "deep umber skin tone with a warm sheen, her face exactly the same tone as her body", False),
]
AGE = [
 ("20대 후반", "in her late 20s", " The flesh is young and firm for its size, each fold holding a taut rounded shape.",
  "a smooth taut surface with natural creases and shadow only where the flesh folds"),
 ("30대 후반", "in her late 30s", "", "natural creases and shadow where the flesh folds"),
 ("40대 후반", "in her late 40s, faint lines at the eyes and mouth", " The flesh is softer and looser at this age, each fold hanging lower and settling further over the one below it.",
  "a coarser surface grain, natural creases and shadow where the flesh folds, crepey texture in the deepest folds"),
 ("50대 후반", "in her late 50s, lines at the eyes, mouth and neck", " The flesh is soft and loose at this age, every fold hanging low and settling deep over the one below it.",
  "coarse surface grain and fine crepey texture across the softest areas, natural creases and shadow where the flesh folds"),
]
MAT = [
 ("나전칠기", "Korean najeon mother-of-pearl lacquer — glossy black lacquer covered with shimmering iridescent mother-of-pearl arabesque vines, peonies and cranes glowing pink, aqua and silver, wide mother-of-pearl bands following every deep crease and curving around the hips and thighs like contour lines, dense scrolls filling the space between every band", "iridescent pearl-white", "the mother-of-pearl shimmering with rainbow iridescence"),
 ("자주요 흑유 척화", "Chinese Cizhou sgraffito ceramic style — a glossy jet-black glaze carved away to reveal bold cream-white peony scrolls and leafy vines, carved cream bands following every deep crease and curving around the hips and thighs like contour lines, dense leaf scrolls filling the space between every band", "cream-white", "the black glaze gleaming"),
 ("마키에", "Japanese maki-e lacquer style — glossy black lacquer with sprinkled gold powder shading into flowing autumn grasses, chrysanthemums, plum branches and full moons, bold gold bands following every deep crease and curving around the hips and thighs, a scattered gold-flake ground filling the space between every motif", "gold", "the gold powder glittering"),
 ("은입사", "Korean eunipsa silver inlay style — a deep black ground with thick bright silver linework covering most of the surface, fine lattice fills between the lines, a bold silver band following every deep crease and curving around the hips and thighs like contour lines", "silver", "the silver linework catching the light unevenly the way paint on skin does rather than like real metal"),
 ("라이롯남", "Thai lai rot nam style — brilliant gold leaf over a black lacquer ground, continuous kranok flame scrolls covering every surface, a gold border band following every deep crease and curving around the hips and thighs, kranok scrolls filling the space between every band", "gold", "the gold leaf blazing, catching the light the way gold paint on skin does rather than like solid metal"),
 ("포다이트", "polished fordite style — thin layered strata of candy red, teal, mustard yellow, cobalt, white and orange stacked in tight concentric bands that follow every deep crease and curve around the hips and thighs like contour lines", "candy-red", "the layered colour bands gleaming"),
 ("알레브리헤", "Oaxacan alebrije style — her own skin tone as the base colour, densely painted with vivid neon magenta, yellow, lime green, turquoise and orange dots, stripes, zigzags and small flowers, a bright striped band following every deep crease and curving around the hips and thighs, no animal figures", "magenta", "the neon colours blazing"),
 ("청자 상감", "Korean celadon inlay style — a soft pale jade-green glaze ground inlaid with deep indigo and black slip cranes, clouds and chrysanthemum medallions, a fine dark double-line band following every deep crease and curving around the hips and thighs like contour lines, inlaid medallions filling the space between every band", "pale jade-green", "the pale glaze staying pale and the inlaid motifs crisp"),
 ("팔레흐", "Russian Palekh miniature style — a deep black ground with fine gold linework and small jewel-toned scenes of firebirds, horses and winter forests in crimson, emerald and ultramarine, a gold border band following every deep crease and curving around the hips and thighs, gold filigree filling the space between every band", "gold", "the gold filigree glinting, the black ground reading clearly as paint on skin rather than as fabric"),
 ("말라카이트", "polished malachite style — vivid emerald and deep forest green in concentric swirling bands that follow every deep crease and curve around the hips and thighs like contour lines on a map, a thin gold line between the bands", "emerald-green", "the polished green bands gleaming"),
 ("탈라베라", "Mexican Talavera ceramic style — a glossy white tin glaze ground painted with bold cobalt blue, marigold yellow, terracotta orange and green floral rosettes, star medallions and scalloped borders, a thick cobalt border following every deep crease and curving around the hips and thighs", "cobalt-blue", "the cobalt and marigold blazing on the white glaze"),
 ("마욜리카", "Italian maiolica tin-glaze style — a glossy warm cream glaze ground painted with cobalt blue, ochre yellow, copper green and manganese purple grotesque scrolls, acanthus leaves and medallions, a bold cobalt band following every deep crease and curving around the hips and thighs", "cobalt-blue", "the cobalt and ochre glowing on the cream glaze"),
 ("호홀로마", "Russian Khokhloma style — a glossy black lacquer ground covered with brilliant scarlet berries, curling golden strawberry vines and flame-gold leaves, a thick gold vine band following every deep crease and curving around the hips and thighs, dense berry scrolls filling the space between every band", "scarlet", "the scarlet and gold blazing, the black ground reading clearly as paint on skin rather than as fabric"),
 ("스테인드글라스", "stained glass style — glowing panes of ruby red, sapphire blue, emerald green, amber and violet fitted together by thick black lead lines, rose-window medallions on the bust and the torso, the lead lines following every deep crease and curving around the hips and thighs, dense small panes filling the space between every medallion", "ruby-red", "the glass panes glowing as if lit from within"),
]
HAIR = ["a high bun with a jewelled pin", "waist-length straight hair swept behind her shoulders", "a wide round afro with a gold headband",
 "long box braids gathered high on her head", "a high swinging ponytail tied with a cord", "tight cornrows swept into a thick low bun",
 "waist-length locs with gold cuffs", "a blunt bob with straight bangs", "a braided crown wrapped around her head",
 "shoulder-length glossy curls", "a sleek chignon with a carved pin", "long micro braids falling to her hips",
 "a high top knot with loose strands framing her face", "thick twin braids over her shoulders", "a short cropped pixie cut",
 "a sleek low ponytail tied at the nape", "long finger waves falling past her shoulders", "two thick braided buns",
 "a voluminous curly half-up half-down style", "a neat low bun with a lacquered pin"]
SHOE = ["platform stiletto mules", "platform stiletto sandals with a single ankle strap", "peep-toe platform stiletto pumps",
 "platform stiletto slingbacks", "square-toe platform stiletto mules", "platform stiletto sandals with a wide ankle cuff",
 "crisscross strap platform stiletto sandals", "platform stiletto ankle-strap pumps", "T-strap platform stiletto sandals",
 "platform stiletto mules with a rounded toe", "platform stiletto sandals with twin instep straps", "platform stiletto slides with a thick toe band",
 "platform stiletto sandals with a braided strap", "platform stiletto mules with a scalloped edge", "platform stiletto sandals with toe rings",
 "platform stiletto pumps with an open back", "platform stiletto sandals with double ankle straps", "platform stiletto mules with a squared toe band",
 "platform stiletto sandals laced around the ankle", "platform stiletto mules with a mirror-finish sole"]
NAILS = ["long glossy almond nails", "sharp stiletto nails", "squared-off coffin nails", "short rounded nails with a high gloss",
 "long oval nails with a mirror finish", "tapered almond nails with metallic tips", "long square nails", "pointed nails with a pearl sheen",
 "glossy ballerina-shaped nails", "long nails with a chrome finish", "almond nails with a matte finish", "extra-long stiletto nails",
 "short squoval nails with a lacquered shine", "long coffin nails with an iridescent glaze", "rounded nails with a deep gloss",
 "long almond nails with gilded tips", "square nails with a glass-like shine", "sharp talon-shaped nails", "oval nails with a satin finish",
 "long nails lacquered to match her body art"]
EAR = ["large hoop earrings", "long teardrop earrings", "heavy chandelier earrings", "wide disc earrings", "thick gold cuff earrings",
 "long linear drop earrings", "oversized round studs", "layered hoop earrings", "long tassel earrings", "crescent-shaped earrings",
 "large square earrings", "spiral drop earrings", "wide fan-shaped earrings", "heavy ball-drop earrings", "long chain earrings",
 "thick twisted hoops", "large teardrop studs", "double-hoop earrings", "long geometric drop earrings", "wide crescent hoops"]

def P(*p): return "\n\n".join(p)

def build(j, body, pose_key):
    label, fn = BODY[body]
    pl, frame, setting, mode, occ, weight, pose_s = POSE[pose_key]
    eth_l, eth_en, skin, bright = ETHNIC[j % 6]
    age_l, age_s, flesh, tex = AGE[j % 4]
    m_l, art, shoe_c, shine = MAT[j % 14]
    bg = "deep-charcoal" if bright else "mid-grey"
    head = SET[setting].format(bg=bg)
    return P(V_HEAD if frame == "v" else H_HEAD, head,
      f"Subject: ONE real adult {eth_en} woman {age_s}, {skin}, real skin texture with visible pores and fine grain, "
      f"{HAIR[j % 20]}, a calm confident expression, real living eyes. She wears {EAR[j % 20]} and has {NAILS[j % 20]}.",
      f"Physique: An extraordinarily large woman, far beyond any real person, {occ}. {fn(mode)}{flesh} {weight}",
      f"Skin: Real photographic skin — visible pores and fine grain, {tex}, faint stretch marks where the great curves have "
      f"expanded, the raking light picking out every ridge and hollow of the surface. No smooth illustration finish, no plastic CG sheen.",
      f"Body Art: Her bare skin is painted in {art}. {PAINT} {COVER}",
      pose_s,
      f"Footwear: Extreme {shoe_c} {SHOE[j % 20]}, the platform soles as tall as her ankle bones, the ultra-thin stiletto heels "
      f"so high her insteps stand nearly vertical.",
      f"Background & Lighting: {shine}, the hard raking light carving every fold and curve.",
      V_END if frame == "v" else H_END)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--force", action="store_true"); ap.add_argument("--md")
    a = ap.parse_args(); os.makedirs(PRESETS, exist_ok=True)
    made = skipped = 0; md = []; n = 1
    assert len(PLAN) == 36
    for body in BODY:
        for j, pose_key in enumerate(PLAN):
            key = f"la_photo_{n:03d}_{body}_{pose_key}"
            title = (f"Photo {n:03d} · {BODY[body][0]} · {MAT[j % 14][0]} · {POSE[pose_key][0]} · "
                     f"{ETHNIC[j % 6][0]} {AGE[j % 4][0]}")
            prompt = build(j, body, pose_key)
            assert prompt.startswith("Image format")
            data = {"title": title, "category": CATEGORY, "platform": "gemini",
                    "aspect_ratio": "2:3" if POSE[pose_key][1] == "v" else "3:2", "prompt": prompt}
            md.append(f"## {n:03d}. {title}\n`{key}`\n\n```\n{prompt}\n```\n")
            path = os.path.join(PRESETS, key + ".json")
            if os.path.exists(path) and not a.force: skipped += 1
            else:
                with open(path, "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=2)
                made += 1
            n += 1
    assert n == 253, n
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Photo Direct 001-252 (실사 직접 생성 · 자세 11종)\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} -> {CATEGORY}")

if __name__ == "__main__":
    main()
