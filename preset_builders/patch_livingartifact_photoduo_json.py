# -*- coding: utf-8 -*-
"""
Living Artifact · Photo Duo 001-168  (실사 직접 생성 · 2인)
- 7체형에서 2개씩 고른 21쌍 × 8자세 = 168
- 자세 8종
  가로 3:2 (6) 나란히 기대기 / 기대기+앉기 / 눕기+기대기(머리 반대) /
               눕기+걸터앉기 / 둘 다 눕기(머리 반대) / (예비) — 아래 POSE 참조
  세로 2:3 (2) 둘 다 정면 / 정면+3/4  ※ 둘 다 걸터앉기는 세로
- 압축 템플릿(약 430단어). 듀오는 인물이 둘이라 솔로 템플릿을 그대로 쓰면 800단어를 넘김
- 확정 규칙(v5.6)
  * `the camera set close ... so the two of them fill the frame edge to edge` 필수 (빼면 멀어짐)
  * 화면 어디에 누가 오는지(좌/우, 앞/뒤, 머리 방향) 반드시 명시
  * 몸끼리 눌려 살이 밀리는 표현 — 듀오에서만 가능한 부피 수단
  * 팔은 자기 몸도 상대 몸도 가리지 않음
  * 안 보일 부위는 "자르라"고 지시하지 말고 아예 언급하지 않는다 (신발·발끝 묘사가 카메라를 물러나게 함)
  * 둘 다 누울 때는 머리 방향 반대 / 마주 보며 기대기는 불채택
- output: presets/la_photoduo_{001..168}_*.json   options: --force, --md review.md
"""
import json, os, argparse
from itertools import combinations

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Photo Duo"
V_HEAD = "Image format: a vertical portrait-orientation photograph, 2:3 aspect ratio, taller than it is wide."
V_END = "Vertical 2:3 portrait-orientation photograph, taller than it is wide."
H_HEAD = "Image format: a horizontal landscape-orientation photograph, 3:2 aspect ratio, wider than it is tall."
H_END = "Horizontal 3:2 landscape-orientation photograph, wider than it is tall."
CAM = ("50mm lens at f/8, a single hard key light raking in from one side — a real photograph, not an illustration, "
       "not CGI, not a render.")
ONBOTH = ("On both: real photographic skin with visible pores, creases where the flesh folds and faint stretch marks, no "
          "illustration finish, no CG sheen. The paint is pigment on living skin, distorting over every bulge and cracking "
          "where it folds, covering everything below the jaw with no bare skin left; their faces unpainted, the pattern "
          "fading out at the neck. Neither arm crosses in front of her own body or the other woman's, both faces toward the "
          "camera. Every fold keeps its own rounded outline with a deep crease between them, never one shapeless mass; arms, "
          "hands and legs in correct proportion. Both wear extreme platform stiletto heels with soles as tall as their ankle bones.")

# ---------- 체형 (압축판) ----------
BELLY = {
 "stand": ("{mass} sits on her middle, so much of it that it hangs far lower than it projects — sagging down toward her knees "
           "under its own weight rather than pushing forward, gathering into {n} heavy rounded folds stacked one above the "
           "other, deep creases between them, never taut, never smooth, never round like a drum, merging seamlessly into her "
           "sides, hips and thighs with no boundary anywhere, not pregnant"),
 "sit":   ("{mass} sits on her middle and settles down over her thighs as she sits, spreading forward and outward under its "
           "own weight in {n} heavy rounded folds with deep creases between them, never taut, never smooth, never round like "
           "a drum, merging seamlessly into her sides, hips and thighs with no boundary anywhere, not pregnant"),
 "recline": ("{mass} sits on her middle and spills forward down the slope of her raised torso under its own weight, piling "
           "over her thighs and reaching toward her knees in {n} heavy rounded folds with deep creases between them, never "
           "taut, never smooth, never round like a drum, merging seamlessly into her sides, hips and thighs with no boundary "
           "anywhere, not pregnant"),
 "lie":   ("{mass} sits on her middle and, even as she lies on her side, spills forward away from her body and hangs over the "
           "front edge of her torso, the lowest part sagging onto the platform in {n} heavy rounded folds with deep creases "
           "between them, never taut, never smooth, never round like a drum, merging seamlessly into her sides, hips and "
           "thighs with no boundary anywhere, not pregnant"),
}
def low(t): return t[0].lower() + t[1:]

def belly(mode, big):
    return BELLY[mode].format(mass="An immense mass of soft heavy fat" if big else "A great mass of soft heavy fat",
                              n="three or four" if big else "two or three")
LIE_HIP = " Her upper hip rises as a great rounded mound higher than her own shoulder, the underside hip and thigh flattening wide against the platform."
SIT_EDGE = " Her hips spread wide and flatten against the seat, the flesh of her thighs bulging out above and below where the hard front edge presses into them."

def ussbbw(m):
    return (f"{belly(m, True)}. A gigantic bust above it, no waist at all, colossal hips more than three times the width of her "
            f"shoulders and an enormous rounded rear, each thigh thicker than a normal woman's waist, very thick upper arms.")
def hg_ussbbw(m):
    return (f"A colossal heavy bust far wider than her shoulders, and below it a waistline that still draws in clearly even at "
            f"this size — the one place on her body where the outline pulls inward. Below it {low(belly(m, True))}. Colossal hips "
            f"more than three times the width of that waistline and a gigantic rear, each thigh thicker than a normal woman's waist.")
def hg_ssbbw(m):
    return (f"A colossal heavy bust far wider than her shoulders, and below it a waistline that still draws in clearly even at "
            f"this size — the one place on her body where the outline pulls inward. Below it {low(belly(m, False))}. Enormous round "
            f"hips more than three times the width of that waistline, a gigantic rear, gigantic soft thighs, very thick soft arms.")
def muscle_hg(m):
    return (f"Huge rounded shoulders and massive arms with the swell of the biceps showing through a soft layer of fat, a "
            f"colossal bust far wider than her shoulders, and below it a waistline that still draws in clearly, the muscle of "
            f"her core firm beneath it. Below it {low(belly(m, False))}. Enormous round hips, a gigantic powerful rear, colossal "
            f"thighs with the sweep of the quads visible under a soft layer, no bodybuilder leanness.")
def athletic(m):
    return (f"The body of a world's strongest woman pushed far past real limits: enormously broad thick shoulders, massive "
            f"heavy arms so thick they cannot lie flat against her sides, a colossal bust, a huge barrel torso, no waist at "
            f"all. {belly(m, False)}. Colossal wide hips and a huge rounded powerful rear, tree-trunk thighs. The muscle is "
            f"huge but rounded and buried under a thick layer of soft fat, broad blunt swells with no sharp separation.")
def colossal(m):
    return ("A giantess built on a completely even scale, every part enlarged by the same amount: massive rounded shoulders, "
            "huge thick arms, a colossal full bust, a broad heavy torso with a large smooth rounded belly, wide solid hips, "
            "enormous columnar thighs. Her shoulders span more than four head-widths and each hand is as wide as a normal "
            "woman's torso. No single part stands out more than another, no hanging folds, not pregnant.")
def tentpole(m):
    return (f"A giant hourglass frame flaring out at both ends: enormous flaring lats spreading to shoulders twice the width "
            f"of a normal woman's, huge thick arms pushed far out by the width of her back, a colossal bust projecting past "
            f"the line of her shoulders, no waist at all. {belly(m, False)}. Below it colossal wide hips just as broad as her "
            f"shoulders and a huge rounded rear; the muscle is rounded and soft-edged under a thick layer of fat.")

BODY = {
 "ussbbw": ("USSBBW", ussbbw), "hgussbbw": ("아워글래스 USSBBW", hg_ussbbw), "hgssbbw": ("아워글래스 SSBBW", hg_ssbbw),
 "musclehg": ("머슬 아워글래스 BBW", muscle_hg), "athletic": ("애슬리트 USSBBW", athletic),
 "colossal": ("콜로설", colossal), "tentpole": ("텐트폴 USSBBW", tentpole),
}
PAIRS = list(combinations(BODY.keys(), 2))   # 21

# ---------- 자세 ----------
# key: (라벨, 프레임, 배경문장, subjects 문장, A역할, B역할, A모드, B모드, 자세문장)
POSE = {
"recline_pair": ("나란히 기대기", "h",
 "reclining side by side against the same padded backrest on a low platform, a plain seamless {bg} backdrop, nothing else in the frame, the camera set close at platform level so the two of them fill the frame edge to edge",
 "propped at about 45 degrees with their legs stretched out in front of them, their two bodies together filling the frame from edge to edge and top to bottom with almost no empty backdrop left, their hips and sides pressed against each other and the flesh bulging out where they touch",
 "Left woman", "Right woman", "recline", "recline",
 "Their outer arms rest back on the platform with the elbows out, their inner hands on their own thighs."),
"bench_pair": ("둘 다 걸터앉기", "v",
 "seated side by side on one short backless bench carved from a solid block of pale grey stone, just long enough for the two of them and no longer, in a bare gallery space with a plain smooth {bg} wall behind them, the camera set close at bench level so the two of them fill the frame edge to edge",
 "seated with their knees apart and their feet flat on the floor, their two bodies together overflowing the stone on both sides and filling the frame from edge to edge, their hips and sides pressed against each other and the flesh bulging out where they touch",
 "Left woman", "Right woman", "sit", "sit",
 "Their outer hands rest on the stone beside their hips, their inner hands on their own thighs."),
"recline_sit": ("기대기 + 앉기", "h",
 "on a low platform with a padded backrest at its left end and a short stone bench at its right end, a plain seamless {bg} backdrop, nothing else in the frame, the camera set close at platform level so the two of them fill the frame edge to edge",
 "one reclining against the backrest at the left of the frame with her legs stretched out toward the right, the other sitting upright on the stone bench at the right and rising to fill the full height of the picture, their two bodies together filling the frame from edge to edge and top to bottom with almost no empty backdrop left, and where they meet in the middle the flesh presses together and bulges out",
 "Reclining woman at the left", "Seated woman at the right", "recline", "sit",
 "The reclining woman's arms rest back on the platform behind her hips with the elbows out; the seated woman's hands rest on the stone beside her hips."),
"lie_recline": ("눕기 + 기대기 (머리 반대)", "h",
 "on a low platform with a padded backrest at its right end, a plain seamless {bg} backdrop, nothing else in the frame, the camera set close at platform level so the two of them fill the frame edge to edge",
 "lying head to toe in opposite directions — one reclining against the backrest at the right with her head at the right edge and rising to fill the full height of the picture, the other lying on her side along the front of the platform with her head at the left edge and her legs stretching back beneath the reclining woman's raised torso, their two bodies together filling the frame from edge to edge and top to bottom with almost no empty backdrop left",
 "Reclining woman, head at the right", "Lying woman, head at the left", "recline", "lie",
 "The reclining woman's arms rest back on the platform behind her hips with the elbows out; the lying woman rests her head on her raised hand with that elbow planted behind her body, her other arm lifted clear on the top of her hip with the elbow raised."),
"lie_bench": ("눕기 + 걸터앉기", "h",
 "in a bare gallery space with a plain smooth {bg} wall behind them, nothing in the frame but one short backless bench carved from a solid block of pale grey stone, just long enough for the two of them and no longer, the camera set close at bench level so the two of them fill the frame edge to edge",
 "one lying on her side along the near length of the stone with her head at the left edge, the other sitting upright on the right end of the same bench with her hips overhanging the narrow stone on both sides and rising to fill the full height of the picture, their two bodies together filling the frame from edge to edge and top to bottom with almost no empty backdrop left",
 "Lying woman, head at the left", "Seated woman at the right", "lie", "sit",
 "The lying woman rests her head on her raised hand with that elbow planted behind her body, her other arm lifted clear on the top of her hip with the elbow raised; the seated woman's hands rest on the stone beside her hips."),
"lie_pair": ("둘 다 눕기 (머리 반대)", "h",
 "lying on one low flat platform, a plain seamless {bg} backdrop, nothing else in the frame, the camera set close at platform level so the two of them fill the frame edge to edge",
 "lying on their sides one behind the other and both facing the camera but head to toe in opposite directions — the nearer woman's head at the left edge and the farther woman's head at the right edge, so that each one's shoulders sit behind the other one's legs and their bulk fills the frame evenly from edge to edge and top to bottom",
 "Nearer woman, head at the left", "Farther woman, head at the right", "lie", "lie",
 "Each rests her head on her raised hand with that elbow planted behind her body, her other arm lifted clear on the top of her hip with the elbow raised, a visible gap of background between that arm and her side."),
"stand_pair": ("둘 다 정면", "v",
 "standing side by side on a plain seamless {bg} backdrop, nothing else in the frame, the camera set close so the two of them fill the frame edge to edge",
 "standing square to the camera with their feet planted far apart, their two bodies together so wide that they overflow the full width of the frame and are cut off by the left and right edges, pressed shoulder to shoulder with their sides squeezed against each other and the flesh bulging out where they touch",
 "Left woman", "Right woman", "stand", "stand",
 "Their outer arms are held away from their bodies with a visible gap of background at each side."),
"stand_mixed": ("정면 + 3/4", "v",
 "standing side by side on a plain seamless {bg} backdrop, nothing else in the frame, the camera set close so the two of them fill the frame edge to edge",
 "the left one standing square to the camera and the right one turned about 45 degrees toward her with the front of her body still mostly toward the lens and the great curve of her hips and rear projecting behind her, their two bodies together so wide that they overflow the full width of the frame and are cut off by the left and right edges, their sides pressed against each other and the flesh bulging out where they touch",
 "Left woman, square to the camera", "Right woman, turned 45 degrees", "stand", "stand",
 "Both hold their arms clear of their bodies with a visible gap of background at each side."),
}
POSES = list(POSE.keys())

ETHNIC = [
 ("흑인", "a Black woman", "deep near-black skin tone, THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, not brown, not lightened, her face exactly as dark as her body", False),
 ("한국", "a Korean woman", "warm ivory skin with a golden undertone, her face exactly the same tone as her body", True),
 ("라틴", "a Latina woman", "warm golden-tan skin with olive undertones, her face exactly the same tone as her body", True),
 ("북유럽", "a Scandinavian woman", "very fair skin with cool pink undertones and faint freckling, her face exactly the same tone as her body", True),
 ("남아시아", "a South Asian woman", "rich warm brown skin with golden undertones, her face exactly the same tone as her body", True),
 ("동아프리카", "an East African woman", "deep umber skin with a warm sheen, her face exactly the same tone as her body", False),
]
AGE = [("20대 후반", "in her late 20s"), ("30대 후반", "in her late 30s"),
       ("40대 후반", "in her late 40s"), ("50대 후반", "in her late 50s")]
MAT = [
 ("나전칠기", "Korean najeon mother-of-pearl lacquer — glossy black lacquer with iridescent mother-of-pearl vines, peonies and cranes in pink, aqua and silver, wide bands following every deep crease and curving around the hips and thighs like contour lines"),
 ("자주요 흑유 척화", "Chinese Cizhou sgraffito — a glossy jet-black glaze carved away to bold cream-white peony scrolls and leafy vines, carved cream bands following every deep crease and curve"),
 ("마키에", "Japanese maki-e lacquer — glossy black lacquer with sprinkled gold powder shading into autumn grasses, chrysanthemums and full moons, bold gold bands following every curve"),
 ("은입사", "Korean eunipsa silver inlay — a deep black ground with thick bright silver linework and fine lattice fills, a bold silver band following every deep crease, catching the light the way paint on skin does rather than like real metal"),
 ("라이롯남", "Thai lai rot nam — brilliant gold leaf over black lacquer, continuous kranok flame scrolls covering every surface, a gold border band following every curve"),
 ("포다이트", "polished fordite — thin layered strata of candy red, teal, mustard yellow, cobalt, white and orange in tight concentric bands following every deep crease and curve"),
 ("알레브리헤", "Oaxacan alebrije — her own skin tone as the base, densely painted with neon magenta, yellow, lime green, turquoise and orange dots, stripes and zigzags, a bright striped band following every curve, no animal figures"),
 ("청자 상감", "Korean celadon inlay — a pale jade-green glaze ground inlaid with indigo and black cranes, clouds and chrysanthemum medallions, fine dark bands following every curve, the glaze staying pale"),
 ("팔레흐", "Russian Palekh miniature — a deep black ground with fine gold linework and jewel-toned firebirds, horses and winter forests in crimson, emerald and ultramarine, a gold border band following every curve"),
 ("말라카이트", "polished malachite — vivid emerald and deep forest green in concentric swirling bands following every curve like contour lines on a map, a thin gold line between them"),
 ("탈라베라", "Mexican Talavera — a glossy white tin glaze painted with cobalt blue, marigold yellow, terracotta orange and green rosettes, star medallions and scalloped borders, a thick cobalt border following every curve"),
 ("마욜리카", "Italian maiolica tin-glaze — a warm cream glaze painted with cobalt, ochre, copper green and manganese purple scrolls and medallions, a bold cobalt band following every curve"),
 ("호홀로마", "Russian Khokhloma — a glossy black lacquer ground with scarlet berries, curling golden vines and flame-gold leaves, a thick gold vine band following every curve, the black ground reading clearly as paint on skin rather than as fabric"),
 ("스테인드글라스", "stained glass — glowing panes of ruby, sapphire, emerald, amber and violet fitted together by thick black lead lines, rose-window medallions on the bust and torso, the lead lines following every deep crease"),
]
HAIR = ["a high bun with a jewelled pin", "waist-length straight hair", "a wide round afro with a gold headband",
 "long box braids gathered high", "a high ponytail tied with a cord", "tight cornrows in a thick low bun",
 "waist-length locs with gold cuffs", "a blunt bob with straight bangs", "a braided crown around her head",
 "shoulder-length glossy curls", "a sleek chignon with a carved pin", "long micro braids to her hips",
 "a high top knot with loose strands", "thick twin braids over her shoulders", "a short cropped pixie cut",
 "a sleek low ponytail at the nape", "long finger waves past her shoulders", "two thick braided buns",
 "a voluminous curly half-up style", "a neat low bun with a lacquered pin"]

def P(*p): return "\n\n".join(p)

def person(role, eth_i, age_i, mat_i, hair_i, body_key, mode):
    eth_l, eth_en, skin, bright = ETHNIC[eth_i % 6]
    age_l, age_s = AGE[age_i % 4]
    m_l, art = MAT[mat_i % 14]
    extra = LIE_HIP if mode == "lie" else (SIT_EDGE if mode == "sit" else "")
    return (f"{role}: {eth_en} {age_s}, {skin}, {HAIR[hair_i % 20]}. {BODY[body_key][1](mode)}{extra} "
            f"Painted in {art}.")

def build(n, a_body, b_body, pose_key):
    pl, frame, setting, subj, a_role, b_role, a_mode, b_mode, arms = POSE[pose_key]
    i = n
    a_eth, b_eth = i % 6, (i + 3) % 6
    a_age, b_age = i % 4, (i + 2) % 4
    a_mat, b_mat = i % 14, (i + 7) % 14
    a_hair, b_hair = i % 20, (i + 10) % 20
    bright = ETHNIC[a_eth][3] or ETHNIC[b_eth][3]
    bg = "deep-charcoal" if bright else "mid-grey"
    return P(V_HEAD if frame == "v" else H_HEAD,
      f"A photograph of TWO women {setting.format(bg=bg)}, {CAM}",
      f"Subjects: TWO real adult women, both far beyond any real person in size, {subj}.",
      person(a_role, a_eth, a_age, a_mat, a_hair, a_body, a_mode),
      person(b_role, b_eth, b_age, b_mat, b_hair, b_body, b_mode),
      f"{arms} {ONBOTH}",
      V_END if frame == "v" else H_END)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--force", action="store_true"); ap.add_argument("--md")
    a = ap.parse_args(); os.makedirs(PRESETS, exist_ok=True)
    made = skipped = 0; md = []; n = 1
    assert len(PAIRS) == 21 and len(POSES) == 8
    for ai, bi in PAIRS:
        for pose_key in POSES:
            key = f"la_photoduo_{n:03d}_{ai}-{bi}_{pose_key}"
            title = f"Photo Duo {n:03d} · {BODY[ai][0]} × {BODY[bi][0]} · {POSE[pose_key][0]}"
            prompt = build(n, ai, bi, pose_key)
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
    assert n == 169, n
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Photo Duo 001-168 (실사 2인 · 21쌍 × 8자세)\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} -> {CATEGORY}")

if __name__ == "__main__":
    main()
