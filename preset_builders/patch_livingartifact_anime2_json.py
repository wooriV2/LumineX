# -*- coding: utf-8 -*-
"""
Living Artifact · Anime Blueprint 19-50 (32)
- 기존 01-18(검증본)에 이어 검증된 체형 블록 × 재질 블록 조합으로 32개 추가
- 규칙(v5.2): 2D 고정 / near-black 피부 + 얼굴 톤 일치 / 세로 2:3 앞뒤 반복 /
  3/4는 회전 시 보일 부위 명시, 정면은 배 롤 구조 강조 / 롤·곡면마다 재질 윤곽선 /
  가슴 커버리지 문장 필수 / 팔레흐는 롤 계열 체형 제외 / apron·옷 단어 금지
- output: presets/la_anime_{19..50}_*.json
- options: --force, --md review.md
"""
import json, os, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Anime Blueprint"
VFRONT = "Image format: a vertical portrait-orientation illustration, 2:3 aspect ratio, taller than it is wide."
VEND = "Vertical 2:3 portrait-orientation full-body illustration, taller than it is wide."
STYLE = "Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant saturated colors, polished professional anime art — not a photograph."
SKIN = "Deep near-black skin tone, THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, void complexion, not brown, not blue, not lightened, her face exactly as dark as her body."
COVER = "The pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly, the knees and the calves, covering them as densely as the chest."

def P(*p): return "\n\n".join(p)

# body: (label, age, hair, expression, physique, {pose_key: pose_sentence}, shadow_line)
BODY = {
"ussbbw": ("USSBBW", "early 40s", "a sleek high bun with gold pins", "calm confident expression",
 "USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — an enormous soft belly made of three or four massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, deep creases between each roll, not pregnant, a gigantic bust resting on the top roll, no waist at all, colossal wide hips and an enormous rounded rear, colossal thick thighs, thick heavy calves.",
 {"34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the stacked belly rolls seen in side profile hanging forward and the enormous rounded curve of her hips and rear jutting out behind her, feet planted apart, arms relaxed away from the body, never covering the belly, full body head to toe.",
  "front": "Pose: Standing full frontal with her feet planted apart, the heavy belly resting on her thighs, arms relaxed away from the body, never covering the belly, full body head to toe."},
 "deep soft shadows in the creases where each heavy roll of flesh folds over the next"),
"hgssbbw": ("아워글래스 SSBBW", "early 40s", "a high bun with a carved bone pin", "a serene warm smile",
 "Hourglass SSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, not a plus-size model, around 650 pounds — a colossal heavy bust, a still-visible cinched waist indentation, a big soft rounded belly below the waistline hanging heavily over the top of her thighs, enormous round hips nearly three times the width of a normal woman's, a gigantic rounded rear jutting far out behind her, gigantic soft thighs pressing together down to the knees, huge soft calves, very thick soft arms, a full round face.",
 {"34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the waist indentation and the heavy belly below it seen in partial profile, the enormous curve of her hips and rear jutting out behind her, feet planted apart, arms relaxed away from the body, never covering the belly, full body head to toe."},
 "deep cel-shaded shadows under the belly and along the curve of her rear"),
"heavymuscle": ("헤비 머슬", "mid 30s", "long glossy black waves", "a warm confident smile, feminine face",
 "Heavy muscular physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 600 pounds — gigantic boulder shoulders far wider than her hips, massive arms with huge defined biceps and triceps and thick forearms, a colossal bust, a thick powerful neck and back, no waist at all, the torso a massive column, colossal thighs with enormous defined quads, a huge rounded powerful rear, thick defined calves, and only the belly soft and round, no visible abs. No bodybuilder look.",
 {"34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the massive shoulder and arm in the foreground, the soft round belly seen in partial profile, the powerful rear and quads behind, feet planted wide, arms hanging relaxed away from the body, full body head to toe.",
  "front": "Pose: Standing full frontal in a wide stance with shoulders squared, arms hanging relaxed away from the body, full body head to toe."},
 "deep cel-shaded shadows carving the shoulders, arms and quads and under the round belly"),
"musclehg": ("머슬 아워글래스 BBW", "late 30s", "a high crown of thick braids with gold cuffs", "a bold confident grin",
 "Muscular hourglass BBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 450 pounds — a thick soft layer of fat over huge muscle everywhere, enormously broad powerful shoulders, thick heavy arms with rounded biceps under the softness, a colossal soft bust, a cinched waist far narrower than her hips with a soft rounded belly folding slightly over the waistline, gigantic wide hips more than twice the width of her waist, an enormous rounded rear jutting far out behind her, colossal thick thighs with strong quads showing through the softness, thick strong calves. More soft than hard, unmistakably hourglass.",
 {"34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the broad shoulders, the soft belly in partial profile and the enormous curve of her hips and rear jutting out behind her, feet planted apart, arms relaxed away from the body, full body head to toe.",
  "front": "Pose: Standing full frontal in a wide powerful stance, arms hanging relaxed away from the body, full body head to toe."},
 "deep cel-shaded shadows under the soft belly and along the curve of her hips and rear"),
"massmonster": ("매스 몬스터", "mid 30s", "a sleek low chignon with a metal pin", "a warm confident smile, feminine face",
 "EXTREME FEMALE MASS MONSTER BODYBUILDER PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 350 pounds of dense muscle with very low body fat — gigantic cannonball shoulders far wider than her hips, huge peaked biceps and thick horseshoe triceps, massive forearms, a broad flaring lat spread, deeply carved abs, enormous sweeping quads with clear separation between each muscle, diamond-shaped calves, visible veins across the arms. A full bust, no masculine facial features. Her shoulders fill the full width of the frame.",
 {"front": "Pose: Standing full frontal in a front double biceps pose, both arms raised and flexed, feet planted apart, full body head to toe."},
 "deep cel-shaded shadows in every muscle separation"),
"muscleussbbw": ("머슬 USSBBW", "early 40s", "a sleek low chignon with a metal pin", "a calm powerful smile, feminine face",
 "MUSCULAR USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,100 pounds of colossal muscle and heavy soft flesh — gigantic cannonball shoulders far wider than her hips, massive arms with huge defined biceps and horseshoe triceps showing through a soft layer, thick powerful forearms, a gigantic bust resting on the top roll, an enormous soft belly made of three or four massive rounded rolls of heavy soft flesh, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, not pregnant, no waist at all, colossal wide hips, colossal thighs with enormous defined quads, diamond-shaped calves. The muscle is defined only on the shoulders, arms, thighs and calves; the belly and rolls stay soft and round. No bodybuilder look.",
 {"front": "Pose: Standing full frontal with her feet planted wide, the heavy belly resting on her thighs, both arms held slightly away from the body with the biceps flexed, full body head to toe."},
 "deep soft shadows in the creases where each heavy roll of flesh folds over the next and in every muscle separation"),
"sumo": ("스모", "early 40s", "a high topknot bun with a carved pin", "a calm powerful expression",
 "EXTREME SUMO PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 800 pounds of dense solid mass — a colossal round firm belly forming one single smooth taut dome, wider than her shoulders, the belly broader than it is tall, filling the whole torso from just under the bust down to the hips and merging smoothly into her sides, one solid mass with her chest and hips, with no hanging rolls and no folds, not pregnant, massive rounded shoulders, thick powerful arms, a full heavy bust resting on top of the great dome, broad solid hips, pillar-like colossal thighs and thick solid calves. Firm and solid rather than soft, smooth rounded surfaces with no visible muscle definition. Her body fills the full width of the frame.",
 {"low": "Pose: A low powerful stance facing the camera, feet planted very wide, knees bent outward, hands resting on her thighs, the great round dome of her belly centered and projecting toward the viewer, full body head to toe.",
  "upright": "Pose: Standing upright full frontal with her feet planted apart, arms hanging relaxed away from the body, the great round dome of her belly centered and projecting toward the viewer, full body head to toe."},
 "a strong curved highlight and deep shadow across the great dome of the belly showing its roundness"),
}
ROLL_BODIES = {"ussbbw", "muscleussbbw", "sumo"}

# material: (label, bright, art sentence, shoes, shine)
MAT = {
"kintsugi": ("청자 킨츠기", True, "Full body kintsugi body painting drawn directly on her bare skin from the collarbones to the ankles, pale celadon glaze covering every surface, fine crackle lines and bold glowing gold seams, a thick gold seam running along every deep crease and fold.", "gold", "the gold seams glowing"),
"jajuyo": ("자주요 흑유 척화", False, "Full body Cizhou sgraffito ceramic body painting on her bare skin from the collarbones to the ankles, a glossy jet-black glaze carved away to reveal bold cream-white peony scrolls and leafy vines, carved cream bands curving around every roll, fold and curve like contour lines, dense leaf scrolls filling the space between every band.", "cream-white", "the black glaze gleaming"),
"najeon": ("나전칠기", False, "Full body Korean najeon mother-of-pearl lacquer body painting on her bare skin from the collarbones to the ankles, glossy black lacquer covered with shimmering iridescent mother-of-pearl arabesque vines, peonies and cranes glowing pink, aqua and silver, a mother-of-pearl band curving around every roll, fold and curve, dense scrolls filling the space between every band.", "pearl-white with iridescent shimmer", "the mother-of-pearl shimmering with rainbow iridescence"),
"makie": ("마키에", False, "Full body Japanese maki-e lacquer body painting on her bare skin from the collarbones to the ankles, glossy black lacquer with sprinkled gold powder shading into flowing autumn grasses, chrysanthemums, plum branches and full moons, a bold gold maki-e band along every deep crease and fold, a scattered gold-flake ground filling the space between every motif.", "gold", "the gold powder glittering"),
"eunipsa": ("은입사", False, "Full body Korean eunipsa silver inlay body painting on her bare skin from the collarbones to the ankles, a deep black iron ground with thick bright silver wire covering most of the surface, silver lotus scrolls, cloud patterns and fine lattice fills, a bold silver inlaid band curving along every deep crease, fold and muscle separation.", "silver", "the silver wire gleaming"),
"laironam": ("라이롯남", False, "Full body Thai lai rot nam body painting on her bare skin from the collarbones to the ankles, brilliant gold leaf over black lacquer, continuous kranok flame scrolls wrapping the shoulders, arms, belly and thighs along the muscle lines, a gold border band along every deep crease and fold, kranok scrolls filling the space between every band.", "gold", "the gold leaf blazing"),
"sonmai": ("썬마이", False, "Full body Vietnamese sơn mài lacquer body painting on her bare skin from the collarbones to the ankles, glossy black lacquer with cinnabar red lotus flowers, flying cranes and bamboo, crushed white eggshell inlay and bright gold leaf accents, a gold leaf band along every deep crease and fold.", "red lacquer with gold trim", "the gold leaf and eggshell glinting"),
"palekh": ("팔레흐", False, "Full body Russian Palekh lacquer miniature body painting on her bare skin from the collarbones to the ankles, glossy mirror-black lacquer with ultra-fine gold filigree, firebirds, blossoms and tiny folk-tale scenes in red, gold and emerald, gold filigree filling all the space between the scenes so the shoulders, arms, knees and calves are covered as densely as the torso.", "red lacquer with gold trim", "the gold filigree glittering"),
"alebrije": ("알레브리헤", False, "Full body Oaxacan alebrije body painting on her bare skin from the collarbones to the ankles, her near-black skin is the base color, densely painted with magenta, yellow, lime green, turquoise and orange dots, stripes, zigzags and small flowers, a bright striped band curving around every roll, fold and curve, no animal figures.", "magenta", "the vivid colors popping"),
"malachite": ("말라카이트", True, "Full body body painting on her bare skin from the collarbones to the ankles, polished malachite stone in vivid emerald and deep forest green covering her entire body, concentric swirling bands curving around every roll, fold and curve like contour lines, a thin gold line beneath every crease.", "gold", "the polished green bands gleaming"),
"fordite": ("포다이트", True, "Full body polished fordite body painting on her bare skin from the collarbones to the ankles, thin layered strata of candy red, teal, mustard yellow, cobalt, white and orange stacked in tight concentric bands curving around every roll, fold and curve like contour lines, glossy as polished stone.", "candy-red", "the polished bands gleaming"),
"celadoninlay": ("청자 상감", True, "Full body Goryeo inlaid celadon body painting on her bare skin from the collarbones to the ankles, a glossy jade-green celadon glaze covering her entire body, inlaid white cranes and clouds with fine black outlines, bold white and black inlaid bands circling every roll, fold and curve like contour lines.", "jade-green", "the glaze gleaming"),
"cloisonne": ("칠보", True, "Full body cloisonné enamel body painting on her bare skin from the collarbones to the ankles, a vivid turquoise enamel ground covering her entire body, lotus scrolls in coral red, cobalt and white, every color cell outlined by raised gold wires, bold gold wire bands circling every roll, fold and curve like contour lines.", "gold", "the gold wires glinting"),
}
DARK_BG = ["A dark charcoal stylized background", "A dark deep-navy stylized background",
           "A dark midnight-blue stylized background", "A dark deep-burgundy stylized background"]
BRIGHT_BG = ["A bright warm ivory stylized background", "A bright pale warm-sand stylized background",
             "A bright warm cream stylized background", "A bright pale grey-blue stylized background",
             "A pale stylized desert at dawn"]
POSE_LABEL = {"34": "3/4", "front": "정면", "low": "정면 낮은 자세", "upright": "정면 직립"}

# (body, material, pose) — 19번부터
ENTRIES = [
("ussbbw","laironam","34"), ("ussbbw","kintsugi","34"), ("ussbbw","sonmai","34"),
("ussbbw","malachite","front"), ("ussbbw","najeon","front"), ("ussbbw","fordite","front"),
("hgssbbw","najeon","34"), ("hgssbbw","kintsugi","34"), ("hgssbbw","alebrije","34"),
("hgssbbw","cloisonne","34"), ("hgssbbw","fordite","34"),
("heavymuscle","eunipsa","front"), ("heavymuscle","jajuyo","34"),
("heavymuscle","makie","front"), ("heavymuscle","celadoninlay","34"),
("musclehg","alebrije","34"), ("musclehg","palekh","34"), ("musclehg","jajuyo","front"),
("musclehg","laironam","front"), ("musclehg","malachite","34"),
("massmonster","laironam","front"), ("massmonster","malachite","front"),
("massmonster","cloisonne","front"), ("massmonster","makie","front"),
("muscleussbbw","laironam","front"), ("muscleussbbw","jajuyo","front"),
("muscleussbbw","najeon","front"), ("muscleussbbw","fordite","front"),
("sumo","kintsugi","low"), ("sumo","cloisonne","upright"),
("sumo","malachite","low"), ("sumo","makie","upright"),
]

def build(i, body, mat, pose):
    B, M = BODY[body], MAT[mat]
    bright = M[1]
    bg = (DARK_BG if bright else BRIGHT_BG)[i % (4 if bright else 5)]
    light = ("a single strong warm light from one side" if bright
             else "lighter than her body, warm light from one side")
    return P(VFRONT, STYLE,
        f"Subject: ONE mature adult Black woman in her {B[1]} with clearly adult facial features, {B[2]}, {B[3]}.",
        f"Physique: {SKIN} {B[4]}",
        f"Body Art: {M[2]} {COVER}",
        B[5][pose],
        f"Footwear: Extreme {M[3]} platform stiletto mules, the platform soles as tall as her ankle bones, the ultra-thin stiletto heels so high her insteps stand nearly vertical.",
        f"Background & Lighting: {bg}, {light}, {B[6]}, {M[4]}, glossy anime highlights on every curve.",
        VEND)

def validate():
    assert len(ENTRIES) == 32, len(ENTRIES)
    seen = set()
    for body, mat, pose in ENTRIES:
        assert body in BODY and mat in MAT, (body, mat)
        assert pose in BODY[body][5], (body, pose)
        if body in ROLL_BODIES: assert mat != "palekh", (body, mat)
        assert (body, mat, pose) not in seen, (body, mat, pose)
        seen.add((body, mat, pose))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()
    validate()
    os.makedirs(PRESETS, exist_ok=True)
    made = skipped = 0; md = []
    for j, (body, mat, pose) in enumerate(ENTRIES):
        i = 19 + j
        key = f"la_anime_{i:02d}_{body}_{mat}_{pose}"
        title = f"Anime {i:02d} · {BODY[body][0]} · {MAT[mat][0]} · {POSE_LABEL[pose]}"
        prompt = build(j, body, mat, pose)
        assert prompt.startswith("Image format") and prompt.rstrip().endswith("taller than it is wide."), key
        data = {"title": title, "category": CATEGORY, "platform": "gemini", "aspect_ratio": "2:3", "prompt": prompt}
        md.append(f"## {i:02d}. {title}\n`{key}`\n\n```\n{prompt}\n```\n")
        path = os.path.join(PRESETS, key + ".json")
        if os.path.exists(path) and not a.force:
            skipped += 1; continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        made += 1
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Anime Blueprint 19-50 (32)\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")

if __name__ == "__main__":
    main()
