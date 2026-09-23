# -*- coding: utf-8 -*-
"""
Living Artifact · Anime Blueprint 96-215 (120)
- 2026-09-22 세션 후반에 확정한 신규 6개 체형 × 20개
  애슬리트 USSBBW / 콜로설 / 텐트폴 USSBBW / 아워글래스 USSBBW / 톱헤비 아워글래스 / 바스트 퀸 BBW
  (바스트 퀸 슬림은 불채택 — 생성 거부 잦음)
- 재질 23종(검증 13 + 신규 컬러 10), 헤어 20 · 신발 20(플랫폼 스틸레토 변형) · 네일 20 · 귀걸이 20
- 규칙(v5.3): 2D / near-black 피부 + 얼굴 톤 일치 / 세로 2:3 앞뒤 반복 / 가슴 커버리지 필수 /
  배 길이 상한 허벅지 중간 / 노출 강조 문구 금지 / 팔레흐는 롤 계열 체형 제외 / apron·옷 단어 금지
- output: presets/la_anime_{96..215}_*.json
- options: --force, --md review.md
"""
import json, os, argparse
from importlib.machinery import SourceFileLoader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Anime Blueprint"
VFRONT = "Image format: a vertical portrait-orientation illustration, 2:3 aspect ratio, taller than it is wide."
VEND = "Vertical 2:3 portrait-orientation full-body illustration, taller than it is wide."
STYLE = "Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant saturated colors, polished professional anime art — not a photograph."
SKIN = "Deep near-black skin tone, THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, void complexion, not brown, not blue, not lightened, her face exactly as dark as her body."
COVER = "The pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly, the knees and the calves, covering them as densely as the chest."

def P(*p): return "\n\n".join(p)

_b = SourceFileLoader("anime2", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                             "patch_livingartifact_anime2_json.py")).load_module()
MAT = dict(_b.MAT)
DARK_BG, BRIGHT_BG = _b.DARK_BG, _b.BRIGHT_BG

# ---------------- 신규 컬러 재질 10종 ----------------
MAT.update({
"dancheong": ("단청", True, "Full body Korean dancheong temple polychrome body painting on her bare skin from the collarbones to the ankles, brilliant cobalt blue, malachite green, vermilion red, white and gold geometric lotus and cloud motifs in tight symmetrical bands with crisp white outlines, a bold banded border following every deep crease and curve, dense scrollwork filling the space between every band.", "cobalt-blue", "the vivid dancheong colours blazing"),
"minakari": ("미나카리", True, "Full body Persian minakari enamel body painting on her bare skin from the collarbones to the ankles, a brilliant cobalt blue enamel ground covering her entire body, dense arabesque vines, turquoise medallions, crimson blossoms and white filigree in saturated jewel colours, fine gold outlines around every motif, a gold enamel band following every deep crease and curve.", "turquoise", "the jewel-toned enamel glowing"),
"jingtailan": ("경태람", True, "Full body Chinese jingtailan cloisonné enamel body painting on her bare skin from the collarbones to the ankles, a brilliant lapis blue enamel ground covering her entire body, dense peony scrolls, phoenix feathers and cloud bands in coral red, emerald green, turquoise and white, every colour cell outlined by raised gold wires, bold gold wire bands circling every curve.", "gold", "the gold wires glinting on the brilliant enamel"),
"khokhloma": ("호홀로마", False, "Full body Russian Khokhloma body painting on her bare skin from the collarbones to the ankles, a glossy black lacquer ground covered with brilliant scarlet berries, curling golden strawberry vines and flame-gold leaves, a thick gold vine band following every deep crease and curve, dense berry scrolls filling the space between every band.", "scarlet", "the scarlet and gold blazing"),
"maiolica": ("마욜리카", True, "Full body Italian maiolica tin-glaze body painting on her bare skin from the collarbones to the ankles, a glossy warm cream glaze covering her entire body, painted with cobalt blue, ochre yellow, copper green and manganese purple grotesque scrolls, acanthus leaves and medallions, a bold cobalt band following every deep crease and curve.", "cobalt-blue", "the cobalt and ochre glowing on the cream glaze"),
"talavera": ("탈라베라", True, "Full body Mexican Talavera ceramic body painting on her bare skin from the collarbones to the ankles, a glossy white tin glaze covering her entire body, painted with bold cobalt blue, marigold yellow, terracotta orange and green floral rosettes, star medallions and scalloped borders, a thick cobalt border following every deep crease and curve.", "marigold-yellow", "the cobalt and marigold blazing on the white glaze"),
"stainedglass": ("스테인드글라스", True, "Full body stained glass body painting on her bare skin from the collarbones to the ankles, glowing panes of ruby red, sapphire blue, emerald green, amber and violet fitted together by thick black lead lines, rose-window medallions on the bust and the torso, the lead lines following every deep crease and curve, dense small panes filling the space between every medallion.", "ruby-red", "the glass panes glowing as if lit from within"),
"oribe": ("오리베", True, "Full body Japanese Oribe ware body painting on her bare skin from the collarbones to the ankles, deep copper-green glaze flowing across half of every surface against a warm cream ground, bold geometric grids, bridges and plum blossoms painted in iron brown, the copper-green glaze pooling along every deep crease and curve.", "copper-green", "the copper-green glaze glowing against the cream ground"),
"millefiori": ("무라노 밀레피오리", True, "Full body Murano millefiori glass body painting on her bare skin from the collarbones to the ankles, hundreds of tiny glass flower canes in ruby, cobalt, emerald, yellow and white packed edge to edge like a glossy mosaic, gold leaf ribbons winding between them, a band of larger canes following every deep crease and curve.", "ruby-red", "the glass canes glittering with jewel colours"),
"shippo": ("칠보 화조", False, "Full body Japanese shippo cloisonné body painting on her bare skin from the collarbones to the ankles, a deep emerald enamel ground covering her entire body, flower-and-bird panels of peonies, irises and flying cranes in coral, sky blue, gold and white, every colour cell outlined by fine silver wires, a silver wire band following every deep crease and curve.", "emerald-green", "the silver wires glinting on the emerald enamel"),
})

# ---------------- 신규 6개 체형 ----------------
# body: (label, age, expression, physique, {pose: sentence}, shadow)
BODY = {
"athleticussbbw": ("애슬리트 USSBBW", "late 30s", "a warm confident smile, feminine face",
 "EXTREME ATHLETIC USSBBW PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — the body of a world's strongest woman pushed far past real limits: enormously broad thick shoulders, massive heavy arms so thick they cannot hang flat against her sides, a colossal bust, a huge barrel torso with a big round heavy belly hanging over the tops of her thighs, no waist at all, colossal wide hips and a huge rounded powerful rear, tree-trunk thighs pressing together down to the knees, thick heavy calves. Immense power under a thick layer of soft fat: the muscle is huge but rounded and buried, only broad blunt swells at the shoulders, upper arms and thighs, no sharp muscle separation anywhere, no carved abs. Solid, heavy and powerful rather than sculpted.",
 {"front": "Pose: Standing full frontal in a wide powerful stance, feet planted far apart, arms held away from the body because of their thickness, the heavy belly resting over her thighs, full body head to toe.",
  "34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the massive shoulder and arm in the foreground, the heavy belly seen in partial profile hanging forward, the powerful rear and thighs behind, feet planted wide, arms held away from the body, full body head to toe."},
 "deep cel-shaded shadows under the heavy belly and along the broad swells of the shoulders, arms and thighs"),
"colossal": ("콜로설", "early 40s", "a serene regal expression",
 "EXTREME COLOSSAL PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — a giantess built on a completely even scale, every part of her enlarged by the same amount: massive rounded shoulders, huge thick arms, a colossal full bust, a broad heavy torso with a large smooth rounded belly, wide solid hips, enormous columnar thighs and thick heavy calves, a full round face. Her head looks small on top of her massive body and her shoulders span more than four head-widths. No single part stands out more than another, no hanging rolls and no folds, not pregnant, her whole body scaled up together into one immense smooth silhouette that towers over the viewer.",
 {"front": "Pose: Standing upright full frontal with her feet planted apart, arms hanging relaxed away from the body, her full immense silhouette clear against the background, full body head to toe.",
  "34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the great curve of the torso seen in partial profile and the enormous rounded curve of her hips and rear jutting out behind her, feet planted apart, arms hanging away from the body, full body head to toe."},
 "broad sweeping shadows across the great curves of the torso, hips and thighs showing their scale"),
"tentpole": ("텐트폴 USSBBW", "late 30s", "a calm powerful smile, feminine face",
 "EXTREME TENTPOLE USSBBW PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — a giant hourglass frame that flares out at both ends: enormous flaring lats spreading to shoulders twice the width of a normal woman's, massive rounded deltoids stacked on top of them, huge thick arms pushed far out from her sides by the width of her back, a smooth rounded neck, a colossal bust projecting forward past the line of her shoulders, a broad heavy torso with a big round belly hanging over the tops of her thighs, and below it colossal wide hips just as broad as her shoulders, a huge rounded rear, colossal thighs pressing together down to the knees and thick heavy calves. Her head looks small on top of her massive frame and her shoulders span more than five head-widths. Wide above and wide below, the silhouette flaring out at the shoulders and the hips alike; the muscle is huge but rounded and soft-edged under a thick layer of fat, broad blunt swells with no sharp separation, no bodybuilder look.",
 {"front": "Pose: Standing full frontal in a wide stance with her shoulders squared and pulled back, feet planted far apart, arms held well away from the body so the full spread of her shoulders and hips is visible, the heavy belly resting over her thighs, full body head to toe.",
  "open": "Pose: Standing full frontal with her feet planted far apart, both arms raised out to the sides at shoulder height with the elbows slightly bent, the full spread of her shoulders and hips opened toward the viewer, the heavy belly resting over her thighs, full body head to toe.",
  "34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the great sweep of the back and the massive shoulder seen from an angle, the heavy belly in partial profile and the rear behind, feet planted wide, arms held well away from the body, full body head to toe."},
 "deep cel-shaded shadows fanning across the shoulders and the chest, under the heavy belly and along the curve of the hips"),
"hourglassussbbw": ("아워글래스 USSBBW", "early 40s", "a serene warm smile",
 "EXTREME HOURGLASS USSBBW PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — a colossal heavy bust wider than her shoulders, and below it a waistline that still pulls in clearly even at this size, the hips more than three times the width of that waistline, then an enormous soft belly of three or four massive rounded rolls of heavy soft flesh spilling out below the waistline, the lowest roll hanging heavily down to mid-thigh, deep creases between each roll, not pregnant, colossal wide hips and a gigantic rounded rear jutting far out behind her, colossal thick thighs pressing together down to the knees, huge soft upper arms, thick heavy calves. Huge above, drawn in at the waistline, huge again below: the hourglass shape survives at the most extreme size.",
 {"34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the waistline indentation and the heavy rolls spilling out below it seen in partial profile, the enormous curve of her hips and rear jutting out behind her, feet planted apart, arms relaxed away from the body, never covering the belly, full body head to toe.",
  "front": "Pose: Standing full frontal with her feet planted apart, the heavy rolls resting over her thighs, arms relaxed away from the body, never covering the belly, the silhouette narrowing sharply at the waistline and flaring wide above and below it, full body head to toe."},
 "deep soft shadows in the creases where each heavy roll of flesh folds over the next and along the curve of the waistline, hips and rear"),
"topheavyhg": ("톱헤비 아워글래스", "mid 30s", "a calm confident expression",
 "EXTREME TOP-HEAVY HOURGLASS PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 350 pounds — a colossal heavy bust far wider than her shoulders, curving forward as one enormous rounded mass and resting with real weight against her upper body, the bust nearly five times the width of her waistline, and below it enormous round hips flaring out to more than twice the width of her shoulders, a gigantic rounded rear jutting far out behind her, colossal thick thighs pressing together down to the knees, thick heavy calves, thick soft upper arms. Huge above and huge below, with a deep waistline between them. The bust merges smoothly into her chest and shoulders as one continuous body, no gap, no seam.",
 {"34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the colossal bust seen in partial profile projecting far forward and the enormous curve of her hips and rear jutting out behind her, feet planted apart, arms hanging relaxed at her sides, full body head to toe.",
  "front": "Pose: Standing full frontal with her feet planted apart, arms hanging relaxed at her sides, the full width of the bust, waistline and hips visible as one silhouette, full body head to toe."},
 "a strong curved highlight and deep shadow under the bust and along the curve of the waistline, hips and rear"),
"bustqueenbbw": ("바스트 퀸 BBW", "late 30s", "a warm confident smile",
 "EXTREME BUST QUEEN BBW PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 500 pounds — a colossal bust spanning the full width of the frame, far wider than her shoulders, each rounded half reaching past the outer line of her arms and hanging down to her waistline, several times the volume of her torso, its weight resting heavily on the big soft rounded belly below it. Broad soft shoulders, thick heavy arms, soft wide hips and colossal soft thighs, thick heavy calves, a full round face. The bust merges smoothly into her chest, shoulders and belly as one continuous soft body, no gap, no seam.",
 {"front": "Pose: Standing full frontal with her feet planted apart, arms hanging relaxed at her sides, full body head to toe.",
  "34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the colossal bust seen in partial profile projecting far forward over the soft belly, the curve of her hips and rear behind, feet planted apart, arms hanging relaxed at her sides, full body head to toe."},
 "a strong curved highlight and deep shadow under the bust where it rests on the belly"),
}
ROLL_BODIES = {"hourglassussbbw"}
POSE_LABEL = {"front": "정면", "34": "3/4", "open": "정면 팔 벌림"}

HAIR = [
"a sleek high bun with gold pins", "waist-length straight hair with a center part",
"a wide round afro with a gold headband", "long box braids gathered high on her head",
"a high swinging ponytail tied with a gold cord", "tight cornrows swept into a thick low bun",
"waist-length locs with gold cuffs", "a blunt bob with straight bangs",
"a braided crown wrapped around her head", "shoulder-length glossy curls",
"a sleek chignon with a jade pin", "long micro braids falling to her hips",
"a high top knot with loose strands framing her face", "thick twin braids over her shoulders",
"a short cropped pixie cut", "a sleek low ponytail tied at the nape",
"long finger waves falling past her shoulders", "two thick braided buns",
"a voluminous curly half-up half-down style", "a high topknot bun with a carved pin",
]
SHOE = [
"platform stiletto mules", "platform stiletto sandals with a single ankle strap",
"peep-toe platform stiletto pumps", "platform stiletto slingbacks",
"square-toe platform stiletto mules", "platform stiletto sandals with a wide ankle cuff",
"crisscross strap platform stiletto sandals", "platform stiletto ankle-strap pumps",
"T-strap platform stiletto sandals", "platform stiletto mules with a rounded toe",
"platform stiletto sandals with twin instep straps", "platform stiletto slides with a thick toe band",
"platform stiletto sandals with a braided strap", "platform stiletto mules with a scalloped edge",
"platform stiletto sandals with toe rings", "platform stiletto pumps with an open back",
"platform stiletto sandals with double ankle straps", "platform stiletto mules with a squared toe band",
"platform stiletto sandals laced around the ankle", "platform stiletto mules with a mirror-finish sole",
]
NAILS = [
"long glossy almond nails", "sharp stiletto nails", "squared-off coffin nails",
"short rounded nails with a high gloss", "long oval nails with a mirror finish",
"tapered almond nails with metallic tips", "long square nails", "pointed nails with a pearl sheen",
"glossy ballerina-shaped nails", "long nails with a chrome finish",
"almond nails with a matte finish", "extra-long stiletto nails",
"short squoval nails with a lacquered shine", "long coffin nails with an iridescent glaze",
"rounded nails with a deep gloss", "long almond nails with gilded tips",
"square nails with a glass-like shine", "sharp talon-shaped nails",
"oval nails with a satin finish", "long nails lacquered to match her body art",
]
EARRINGS = [
"large hoop earrings", "long teardrop earrings", "heavy chandelier earrings",
"wide disc earrings", "thick gold cuff earrings", "long linear drop earrings",
"oversized round studs", "layered hoop earrings", "long tassel earrings",
"crescent-shaped earrings", "large square earrings", "spiral drop earrings",
"wide fan-shaped earrings", "heavy ball-drop earrings", "long chain earrings",
"thick twisted hoops", "large teardrop studs", "double-hoop earrings",
"long geometric drop earrings", "wide crescent hoops",
]

# ---------------- 체형별 20개 (재질, 자세) ----------------
MATS_ALL = ["najeon","jajuyo","makie","eunipsa","laironam","sonmai","alebrije","malachite","fordite",
            "kintsugi","celadoninlay","cloisonne","palekh","dancheong","minakari","jingtailan",
            "khokhloma","maiolica","talavera","stainedglass","oribe","millefiori","shippo"]

def pick(body, poses):
    """해당 체형에 쓸 재질 20종 + 자세를 번갈아 배정"""
    mats = [m for m in MATS_ALL if not (body in ROLL_BODIES and m == "palekh")]
    mats = mats[:20] if len(mats) >= 20 else mats
    return [(m, poses[i % len(poses)]) for i, m in enumerate(mats)]

PLAN = [
("athleticussbbw", ["front", "34"]),
("colossal", ["front", "34"]),
("tentpole", ["front", "34", "open"]),
("hourglassussbbw", ["34", "front"]),
("topheavyhg", ["34", "front"]),
("bustqueenbbw", ["34", "front"]),
]

def build(i, body, mat, pose, hair, shoe, nails, ear):
    B, M = BODY[body], MAT[mat]
    bright = M[1]
    bg = (DARK_BG if bright else BRIGHT_BG)[i % (4 if bright else 5)]
    light = ("a single strong warm light from one side" if bright
             else "lighter than her body, warm light from one side")
    color = {"red lacquer with gold trim": "red lacquer",
             "pearl-white with iridescent shimmer": "iridescent pearl-white"}.get(M[3], M[3])
    return P(VFRONT, STYLE,
        f"Subject: ONE mature adult Black woman in her {B[1]} with clearly adult facial features, {hair}, {B[2]}. "
        f"She wears {ear} and has {nails}.",
        f"Physique: {SKIN} {B[3]} Her body fills the full width of the frame.",
        f"Body Art: {M[2]} {COVER}",
        B[4][pose],
        f"Footwear: Extreme {color} {shoe}, the platform soles as tall as her ankle bones, the ultra-thin stiletto heels so high her insteps stand nearly vertical.",
        f"Background & Lighting: {bg}, {light}, {B[5]}, {M[4]}, glossy anime highlights on every curve.",
        VEND)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()
    assert len(HAIR) == len(SHOE) == len(NAILS) == len(EARRINGS) == 20
    os.makedirs(PRESETS, exist_ok=True)
    made = skipped = 0; md = []; n = 96; seen = set()
    for body, poses in PLAN:
        combos = pick(body, poses)
        assert len(combos) == 20, (body, len(combos))
        for j, (mat, pose) in enumerate(combos):
            assert (body, mat, pose) not in seen
            seen.add((body, mat, pose))
            key = f"la_anime_{n}_{body}_{mat}_{pose}"
            title = f"Anime {n} · {BODY[body][0]} · {MAT[mat][0]} · {POSE_LABEL[pose]}"
            prompt = build(j, body, mat, pose, HAIR[j], SHOE[j], NAILS[j], EARRINGS[j])
            assert prompt.startswith("Image format") and prompt.rstrip().endswith("taller than it is wide.")
            data = {"title": title, "category": CATEGORY, "platform": "gemini",
                    "aspect_ratio": "2:3", "prompt": prompt}
            md.append(f"## {n}. {title}\n`{key}` · 헤어: {HAIR[j]} · 신발: {SHOE[j]} · 네일: {NAILS[j]} · 귀걸이: {EARRINGS[j]}\n\n```\n{prompt}\n```\n")
            path = os.path.join(PRESETS, key + ".json")
            if os.path.exists(path) and not a.force:
                skipped += 1
            else:
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                made += 1
            n += 1
    assert n == 216, n
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Anime Blueprint 96-215 (120) — 신규 6개 체형\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")

if __name__ == "__main__":
    main()
