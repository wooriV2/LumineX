# -*- coding: utf-8 -*-
"""
Living Artifact · Anime Duo (50)
- 01-05: 2026-09-22 세션에서 생성·실사 변환까지 검증한 듀오 프롬프트 원문
- 06-50: 검증된 체형 블록 × 검증된 재질 블록 조합으로 생성 (4:5 세로)
- 규칙(v4/v5.2): 헤비 머슬은 글래머와만 짝 / 다인 금지 재질(칠보·청자 상감) 제외 /
  팔레흐는 롤 계열 체형(USSBBW·머슬 USSBBW·스모) 제외 / 좌우 재질 다름 / 좌우 체형 다름 /
  밝은 재질이 있으면 어두운 배경, 모두 어두운 재질이면 밝은 배경 / 팔 겹침 금지 / 세로 4:5 앞뒤 반복
- output: presets/{key}.json  (title, category, platform, aspect_ratio, prompt)
- options: --force, --md review.md
"""
import json, os, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Anime Duo"
VFRONT = "Image format: a vertical portrait-orientation illustration, 4:5 aspect ratio, taller than it is wide."
VEND = "Vertical 4:5 portrait-orientation full-body illustration, taller than it is wide."
STYLE = "Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant saturated colors, polished professional anime art — not a photograph."
SUBJ = "Subject: TWO mature adult Black women standing side by side, both with clearly adult facial features, both full body head to toe, both faces toward the camera."
SKIN = "Skin: Both women have deep near-black skin tone, THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, void complexion, not brown, not blue, not lightened, their faces exactly as dark as their bodies."
COVER = "Coverage: On both women the pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly and the calves, covering them as densely as the chest."

def P(*parts): return "\n\n".join(parts)

# ---------------- verified body blocks ----------------
BODY = {
"ussbbw": ("USSBBW", "early 40s", "a sleek high bun with gold pins", "calm confident expression",
 "USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — an enormous soft belly made of three or four massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, deep creases between each roll, not pregnant, a gigantic bust resting on the top roll, no waist at all, colossal wide hips, colossal thick thighs, thick heavy calves.",
 "stands full frontal, feet planted apart, arms relaxed away from the body, never covering the belly"),
"hgssbbw": ("아워글래스 SSBBW", "early 40s", "a high bun with a carved bone pin", "a serene warm smile",
 "Hourglass SSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, not a plus-size model, around 650 pounds — a colossal heavy bust, a still-visible cinched waist indentation, a big soft rounded belly below the waistline hanging heavily over the top of her thighs, enormous round hips nearly three times the width of a normal woman's, gigantic soft thighs pressing together down to the knees, huge soft calves, very thick soft arms, a full round face.",
 "stands full frontal, feet planted apart, arms relaxed away from the body, never covering the belly"),
"glamour": ("글래머 아워글래스", "mid 30s", "very long flowing black hair with gold combs", "a confident smile",
 "Glamour hourglass bombshell physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy — a colossal full bust wider than her shoulders, a waist cinched so impossibly tiny it is barely a quarter of the width of her hips, hips flaring out to more than twice the width of her shoulders, an enormous rounded rear, massive thick thighs pressing together down to the knees, long legs, a smooth flat belly, an extreme wasp-waisted silhouette.",
 "stands full frontal with a strong hip shift, one hand on her hip, the other arm hanging away from the body"),
"musclehg": ("머슬 아워글래스 BBW", "late 30s", "a high crown of thick braids with gold cuffs", "a bold confident grin",
 "Muscular hourglass BBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 450 pounds — a thick soft layer of fat over huge muscle everywhere, enormously broad powerful shoulders, thick heavy arms with rounded biceps under the softness, a colossal soft bust, a cinched waist far narrower than her hips with a soft rounded belly folding slightly over the waistline, gigantic wide hips more than twice the width of her waist, colossal thick thighs with strong quads showing through the softness, thick strong calves. More soft than hard, unmistakably hourglass.",
 "stands full frontal in a wide powerful stance, arms hanging relaxed away from the body"),
"heavymuscle": ("헤비 머슬", "mid 30s", "long glossy black waves with a gold headpiece", "a warm confident smile, feminine face",
 "Heavy muscular physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 600 pounds — gigantic boulder shoulders far wider than her hips, massive arms with huge defined biceps and triceps and thick forearms, a colossal bust, a thick powerful neck and back, no waist at all, the torso a massive column, colossal thighs with enormous defined quads, a huge rounded powerful rear, thick defined calves, and only the belly soft and round, no visible abs. No bodybuilder look.",
 "stands full frontal in a wide stance with shoulders squared, arms hanging relaxed away from the body"),
"massmonster": ("매스 몬스터", "mid 30s", "a sleek low chignon with a metal pin", "a bright confident smile, feminine face",
 "EXTREME FEMALE MASS MONSTER BODYBUILDER PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 350 pounds of dense muscle with very low body fat — gigantic cannonball shoulders far wider than her hips, huge peaked biceps and thick horseshoe triceps, massive forearms, a broad flaring lat spread, deeply carved abs, enormous sweeping quads with clear separation between each muscle, diamond-shaped calves, visible veins across the arms, a full bust. No masculine facial features.",
 "stands full frontal with her arms held slightly away from the body, the biceps flexed"),
"muscleussbbw": ("머슬 USSBBW", "early 40s", "a sleek low chignon with a metal pin", "a calm powerful smile, feminine face",
 "MUSCULAR USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,100 pounds of colossal muscle and heavy soft flesh — gigantic cannonball shoulders, massive arms with huge defined biceps and horseshoe triceps showing through a soft layer, a gigantic bust resting on the top roll, an enormous soft belly made of three or four massive rounded rolls of heavy soft flesh, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, not pregnant, no waist at all, colossal wide hips, colossal thighs with enormous defined quads, diamond-shaped calves. The muscle is defined only on the shoulders, arms, thighs and calves; the belly and rolls stay soft and round. No bodybuilder look.",
 "stands full frontal, feet planted wide, arms held slightly away from the body with the biceps flexed, the heavy belly resting on her thighs"),
"sumo": ("스모", "early 40s", "a sleek topknot bun with a carved pin", "a serene powerful expression",
 "EXTREME SUMO PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 800 pounds of dense solid mass — a colossal round firm belly forming one single smooth taut dome, wider than her shoulders, the belly broader than it is tall, filling the whole torso from just under the bust down to the hips and merging smoothly into her sides, one solid mass with her chest and hips, with no hanging rolls and no folds, not pregnant, massive rounded shoulders, thick powerful arms, a full heavy bust resting on top of the great dome, broad solid hips, pillar-like colossal thighs and thick solid calves. Firm and solid rather than soft, no visible muscle definition.",
 "stands in a low powerful stance facing the camera, feet planted very wide, knees bent outward, hands resting on her thighs"),
}
ROLL_BODIES = {"ussbbw", "muscleussbbw", "sumo"}

# ---------------- verified material blocks ----------------
MAT = {
"kintsugi": ("청자 킨츠기", True, "painted as a kintsugi vessel — pale celadon glaze covering every surface, fine crackle lines and bold glowing gold seams, a thick gold seam running along every deep crease and fold", "gold platform stiletto mules", "the gold seams glowing"),
"jajuyo": ("자주요 흑유 척화", False, "painted as Cizhou sgraffito ceramic — a glossy jet-black glaze carved away to reveal bold cream-white peony scrolls and leafy vines, carved cream bands curving around every roll, fold and curve, dense leaf scrolls filling the space between every band", "cream-white platform stiletto mules", "the black glaze gleaming"),
"najeon": ("나전칠기", False, "painted as Korean najeon mother-of-pearl lacquer — glossy black lacquer covered with shimmering iridescent mother-of-pearl arabesque vines, peonies and cranes glowing pink, aqua and silver, a mother-of-pearl band curving around every roll, fold and curve", "pearl-white platform stiletto mules with iridescent shimmer", "the mother-of-pearl shimmering with rainbow iridescence"),
"makie": ("마키에", False, "painted as Japanese maki-e lacquer — glossy black lacquer with sprinkled gold powder shading into autumn grasses, chrysanthemums, plum branches and full moons, a bold gold band along every deep crease, a scattered gold-flake ground filling the space between every motif", "gold platform stiletto mules", "the gold powder glittering"),
"eunipsa": ("은입사", False, "painted as Korean eunipsa silver inlay — a deep black iron ground with thick bright silver wire covering most of the surface, silver scrolls and fine lattice fills, a bold silver band curving around every roll, fold and muscle separation", "silver platform stiletto mules", "the silver wire gleaming"),
"laironam": ("라이롯남", False, "painted in Thai lai rot nam — brilliant gold leaf over black lacquer, continuous kranok flame scrolls wrapping the shoulders, arms, belly and thighs along the muscle lines, kranok scrolls filling the space between every gold band", "gold platform stiletto mules", "the gold leaf blazing"),
"sonmai": ("썬마이", False, "painted in Vietnamese sơn mài lacquer — glossy black lacquer with cinnabar red lotus flowers, flying cranes and bamboo, crushed white eggshell inlay and bright gold leaf accents, a gold leaf band along every deep crease and fold", "red lacquer platform stiletto mules with gold trim", "the gold leaf and eggshell glinting"),
"palekh": ("팔레흐", False, "painted as a Russian Palekh lacquer miniature — glossy mirror-black lacquer with ultra-fine gold filigree, firebirds, blossoms and tiny folk-tale scenes in red, gold and emerald, gold filigree filling all the space between the scenes so the shoulders, arms, knees and calves are covered as densely as the torso", "red lacquer platform stiletto mules with gold trim", "the gold filigree glittering"),
"alebrije": ("알레브리헤", False, "painted in Oaxacan alebrije style — her near-black skin is the base color, densely painted with magenta, yellow, lime green, turquoise and orange dots, stripes, zigzags and small flowers, a bright striped band curving around every roll, fold and curve, no animal figures", "magenta platform stiletto mules", "the neon colors popping"),
"malachite": ("말라카이트", True, "painted as polished malachite stone — vivid emerald and deep forest green, concentric swirling bands curving around every roll, fold and curve like contour lines", "gold platform stiletto mules", "the polished green bands gleaming"),
"fordite": ("포다이트", True, "painted as polished fordite — thin layered strata of candy red, teal, mustard yellow, cobalt, white and orange stacked in tight concentric bands curving around every roll, fold and curve, glossy as polished stone", "candy-red platform stiletto mules", "the polished color bands gleaming"),
}
DARK_BG = ["A dark charcoal stylized background", "A dark deep-navy stylized background",
           "A dark midnight-blue stylized background", "A dark deep-burgundy stylized background"]
BRIGHT_BG = ["A bright warm ivory stylized background", "A bright pale warm-sand stylized background",
             "A bright warm cream stylized background", "A bright pale grey-blue stylized background",
             "A pale stylized desert at dawn"]

# ---------------- 06-50 entries (bodyL, bodyR, matL, matR) ----------------
ENTRIES = [
("ussbbw","hgssbbw","najeon","makie"), ("ussbbw","glamour","malachite","sonmai"),
("ussbbw","musclehg","jajuyo","palekh"), ("ussbbw","massmonster","fordite","eunipsa"),
("ussbbw","muscleussbbw","makie","laironam"), ("ussbbw","sumo","alebrije","najeon"),
("hgssbbw","glamour","kintsugi","alebrije"), ("hgssbbw","musclehg","malachite","laironam"),
("hgssbbw","massmonster","najeon","eunipsa"), ("hgssbbw","muscleussbbw","sonmai","fordite"),
("hgssbbw","sumo","makie","kintsugi"), ("glamour","musclehg","fordite","jajuyo"),
("glamour","massmonster","najeon","laironam"), ("glamour","muscleussbbw","alebrije","eunipsa"),
("glamour","sumo","sonmai","malachite"), ("glamour","heavymuscle","kintsugi","makie"),
("musclehg","massmonster","palekh","laironam"), ("musclehg","muscleussbbw","alebrije","makie"),
("musclehg","sumo","jajuyo","fordite"), ("massmonster","muscleussbbw","eunipsa","malachite"),
("massmonster","sumo","laironam","najeon"), ("muscleussbbw","sumo","kintsugi","jajuyo"),
("hgssbbw","ussbbw","laironam","kintsugi"), ("glamour","ussbbw","palekh","jajuyo"),
("musclehg","ussbbw","makie","malachite"), ("massmonster","ussbbw","najeon","alebrije"),
("muscleussbbw","ussbbw","jajuyo","sonmai"), ("sumo","ussbbw","malachite","makie"),
("glamour","hgssbbw","laironam","fordite"), ("musclehg","hgssbbw","eunipsa","alebrije"),
("massmonster","hgssbbw","makie","malachite"), ("muscleussbbw","hgssbbw","najeon","kintsugi"),
("sumo","hgssbbw","fordite","sonmai"), ("musclehg","glamour","najeon","kintsugi"),
("massmonster","glamour","eunipsa","fordite"), ("muscleussbbw","glamour","laironam","malachite"),
("sumo","glamour","jajuyo","makie"), ("heavymuscle","glamour","eunipsa","fordite"),
("massmonster","musclehg","malachite","sonmai"), ("muscleussbbw","musclehg","fordite","palekh"),
("sumo","musclehg","najeon","eunipsa"), ("muscleussbbw","massmonster","sonmai","kintsugi"),
("sumo","massmonster","kintsugi","makie"), ("sumo","muscleussbbw","makie","alebrije"),
("heavymuscle","glamour","laironam","najeon"),
]

# ---------------- 01-05 verified prompts ----------------
def V(left_key, right_key, matL, matR, body):
    return (left_key, right_key, matL, matR, body)

VERIFIED = [
("ussbbw","hgssbbw","kintsugi","jajuyo", P(VFRONT,
"Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant colors, polished professional anime art — not a photograph.",
SUBJ, SKIN,
"Left woman: in her late 30s, a sleek high bun with gold pins, calm confident expression. USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — an enormous soft belly made of three or four massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, deep creases between each roll, not pregnant, a gigantic bust resting on the top roll, no waist at all, colossal wide hips, colossal thick thighs, thick heavy calves. Her body is painted as a kintsugi vessel: pale celadon glaze covering every surface from the collarbones to the ankles including every belly roll, fine crackle lines and bold glowing gold seams, a thick gold seam running along the deep crease beneath every belly roll.",
"Right woman: in her early 40s, a high bun with a carved bone pin, a serene warm smile. Hourglass SSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, not a plus-size model, around 650 pounds — a colossal heavy bust, a still-visible cinched waist indentation, a big soft rounded belly below the waistline hanging heavily over the top of her thighs, enormous round hips nearly three times the width of a normal woman's, gigantic soft thighs pressing together down to the knees, huge soft calves, very thick soft arms, a full round face. Her body is painted as Cizhou sgraffito ceramic from the collarbones to the ankles, a glossy jet-black glaze carved away to reveal bold cream-white peony scrolls and leafy vines, carved cream bands curving around the waist, belly, hips and thighs like contour lines, dense leaf scrolls filling the space between every band.",
COVER,
"Pose: Both standing full frontal, feet planted apart, arms relaxed away from the body, never covering the belly, their shoulders almost touching, together filling the full width of the frame.",
"Footwear: The left woman wears extreme gold platform stiletto mules; the right woman wears extreme cream-white platform stiletto mules, the platform soles as tall as their ankle bones, the ultra-thin stiletto heels so high their insteps stand nearly vertical.",
"Background & Lighting: A dark charcoal stylized background, a single strong warm light from the left, deep soft shadows in the creases where each heavy roll of flesh folds over the next, the pale glaze and the gold seams glowing against the darkness, glossy anime highlights on every rounded curve.",
VEND)),

("heavymuscle","glamour","laironam","sonmai", P(VFRONT, STYLE, SUBJ,
"Skin: Both women have deep near-black skin tone, THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, cool void complexion, not brown, not blue, not lightened, their faces exactly as dark as their bodies.",
"Left woman: in her mid 30s, long glossy black waves with a gold Thai-style headpiece, a warm confident smile, feminine face. Heavy muscular physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 600 pounds — gigantic boulder shoulders far wider than her hips, massive arms with huge defined biceps and triceps and thick forearms, a colossal bust, a thick powerful neck and back, no waist at all, the torso a massive column, colossal thighs with enormous defined quads, a huge rounded powerful rear, thick defined calves, and only the belly soft and round, no visible abs. No bodybuilder look. Her body is painted in Thai lai rot nam from the collarbones to the ankles, brilliant gold leaf over black lacquer, continuous kranok flame scrolls wrapping the shoulders, biceps, triceps, forearms, belly and quads along the muscle lines, kranok scrolls filling the space between every gold band.",
"Right woman: in her mid 30s, very long flowing black hair with gold kanzashi combs, confident smile. Glamour hourglass bombshell physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy — a colossal full bust wider than her shoulders, a waist cinched so impossibly tiny it is barely a quarter of the width of her hips, hips flaring out to more than twice the width of her shoulders, an enormous rounded rear, massive thick thighs pressing together down to the knees, long legs, a smooth flat belly, an extreme wasp-waisted silhouette. Her body is painted in Vietnamese sơn mài lacquer from the collarbones to the ankles, glossy black lacquer with cinnabar red lotus flowers, flying cranes and bamboo, crushed white eggshell inlay and bright gold leaf accents, curving lacquer bands following the swell of her bust, waist and hips.",
COVER,
"Pose: Both standing full frontal, feet planted apart, arms hanging relaxed away from the body, no arm crossing in front of the other woman, together filling the full width of the frame.",
"Footwear: The left woman wears extreme gold platform stiletto mules; the right woman wears extreme red lacquer platform stiletto mules with gold trim, the platform soles as tall as their ankle bones, the ultra-thin stiletto heels so high their insteps stand nearly vertical.",
"Background & Lighting: A pale stylized desert at dawn, lighter than their bodies, warm low light from the left, deep cel-shaded shadows carving the shoulders, arms and quads of the left woman and the extreme curves of the right woman, the gold leaf blazing, glossy anime highlights on every curve.",
VEND)),

("muscleussbbw","massmonster","eunipsa","laironam", P(VFRONT,
"Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant colors, polished professional anime art — not a photograph.",
"Subject: TWO mature adult Black women standing side by side, both with clearly adult facial features, both full body head to toe, both faces toward the camera, both with feminine faces and warm expressions, no bodybuilder look.",
SKIN,
"Left woman: in her early 40s, a sleek low chignon with a silver pin, a calm powerful smile. MUSCULAR USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,100 pounds of colossal muscle and heavy soft flesh — gigantic cannonball shoulders, massive arms with huge defined biceps and horseshoe triceps showing through a soft layer, a gigantic bust resting on the top roll, an enormous soft belly made of three or four massive rounded rolls of heavy soft flesh, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, not pregnant, no waist at all, colossal wide hips, colossal thighs with enormous defined quads, diamond-shaped calves. The muscle is defined only on the shoulders, arms, thighs and calves; the belly and rolls stay soft and round. Her body is painted in Korean eunipsa silver inlay from the collarbones to the ankles, a deep black iron ground with thick bright silver wire covering most of the surface, silver lines tracing along every muscle separation and a bold silver band curving along the deep crease beneath every belly roll.",
"Right woman: in her mid 30s, a sleek low chignon with a gold pin, a bright confident smile. EXTREME FEMALE MASS MONSTER BODYBUILDER PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 350 pounds of dense muscle with very low body fat — gigantic cannonball shoulders far wider than her hips, huge peaked biceps and thick horseshoe triceps, massive forearms, a broad flaring lat spread, deeply carved abs, enormous sweeping quads with clear separation between each muscle, diamond-shaped calves, visible veins across the arms, a full bust. Her body is painted in Thai lai rot nam from the collarbones to the ankles, brilliant gold leaf over black lacquer, kranok flame scrolls following every muscle separation on the shoulders, arms, abs and quads.",
COVER,
"Pose: Both standing full frontal, feet planted wide, both holding their arms slightly away from the body with the biceps flexed, no arm crossing in front of the other woman, together filling the full width of the frame.",
"Footwear: The left woman wears extreme silver platform stiletto mules; the right woman wears extreme gold platform stiletto mules, the platform soles as tall as their ankle bones, the ultra-thin stiletto heels so high their insteps stand nearly vertical.",
"Background & Lighting: A bright pale grey-blue stylized background, lighter than their bodies, strong cool light from the left carving every muscle, deep soft shadows in the creases of the left woman's belly rolls and in every muscle separation of the right woman, the silver wire and gold leaf gleaming, glossy anime highlights on every curve.",
VEND)),

("sumo","glamour","najeon","alebrije", P(VFRONT, STYLE, SUBJ, SKIN,
"Left woman: in her early 40s, a sleek topknot bun with a mother-of-pearl pin, a serene powerful expression. EXTREME SUMO PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 800 pounds of dense solid mass — a colossal round firm belly forming one single smooth taut dome, wider than her shoulders, the belly broader than it is tall, filling the whole torso from just under the bust down to the hips and merging smoothly into her sides, one solid mass with her chest and hips, with no hanging rolls and no folds, not pregnant, massive rounded shoulders, thick powerful arms, a full heavy bust resting on top of the great dome, broad solid hips, pillar-like colossal thighs and thick solid calves. Firm and solid rather than soft, no visible muscle definition. Her body is painted in Korean najeon mother-of-pearl lacquer from the collarbones to the ankles, glossy black lacquer covered with shimmering iridescent mother-of-pearl arabesque vines, peonies and cranes glowing pink, aqua and silver, horizontal mother-of-pearl bands wrapping around the great belly and continuing around her sides.",
"Right woman: in her mid 30s, long voluminous curls with colorful beaded combs, a bold confident grin. Glamour hourglass bombshell physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy — a colossal full bust wider than her shoulders, a waist cinched so impossibly tiny it is barely a quarter of the width of her hips, hips flaring out to more than twice the width of her shoulders, an enormous rounded rear, massive thick thighs pressing together down to the knees, long legs, a smooth flat belly. Her body is painted in Oaxacan alebrije style from the collarbones to the ankles, her near-black skin is the base color, densely painted with magenta, yellow, lime green, turquoise and orange dots, stripes, zigzags and small flowers, bright striped bands curving around her bust, waist, hips and thighs, no animal figures.",
COVER,
"Pose: The left woman stands in a low powerful stance facing the camera, feet planted very wide, knees bent outward, hands resting on her thighs; the right woman stands full frontal beside her with a strong hip shift, one hand on her hip, the other arm hanging away from the body. Together they fill the full width of the frame.",
"Footwear: The left woman wears extreme pearl-white platform stiletto mules with iridescent shimmer; the right woman wears extreme magenta platform stiletto mules, the platform soles as tall as their ankle bones, the ultra-thin stiletto heels so high their insteps stand nearly vertical.",
"Background & Lighting: A bright pale ivory stylized background, lighter than their bodies, warm light from the left, a strong curved highlight and deep shadow across the great dome of the left woman's belly showing its roundness, deep shadows along the right woman's tiny waist and enormous hips, the mother-of-pearl shimmering and the neon colors popping, glossy anime highlights on every curve.",
VEND)),

("ussbbw","musclehg","fordite","palekh", P(VFRONT, STYLE, SUBJ, SKIN,
"Left woman: in her early 40s, a high bun wrapped in multicolor bands, bold confident smile. USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — an enormous soft belly made of three or four massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, deep creases between each roll, not pregnant, a gigantic bust resting on the top roll, no waist at all, colossal wide hips, colossal thick thighs, thick heavy calves. Her body is painted as polished fordite from the collarbones to the ankles, thin layered strata of candy red, teal, mustard yellow, cobalt, white and orange stacked in tight concentric bands that curve around every roll, fold and curve like contour lines, glossy as polished stone.",
"Right woman: in her late 30s, a high crown of thick braids with gold cuffs, a bold confident grin. Muscular hourglass BBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 450 pounds — a thick soft layer of fat over huge muscle everywhere, enormously broad powerful shoulders, thick heavy arms with rounded biceps under the softness, a colossal soft bust, a cinched waist far narrower than her hips with a soft rounded belly folding slightly over the waistline, gigantic wide hips more than twice the width of her waist, colossal thick thighs with strong quads showing through the softness, thick strong calves. More soft than hard, unmistakably hourglass. Her body is painted as a Russian Palekh lacquer miniature from the collarbones to the ankles, glossy mirror-black lacquer with ultra-fine gold filigree, firebirds, blossoms and tiny folk-tale scenes in red, gold and emerald, gold filigree filling all the space between the scenes so the shoulders, arms, knees and calves are covered as densely as the torso.",
COVER,
"Pose: Both standing full frontal, feet planted apart, arms relaxed away from the body, never covering the belly, no arm crossing in front of the other woman, together filling the full width of the frame.",
"Footwear: The left woman wears extreme candy-red platform stiletto mules; the right woman wears extreme red lacquer platform stiletto mules with gold trim, the platform soles as tall as their ankle bones, the ultra-thin stiletto heels so high their insteps stand nearly vertical.",
"Background & Lighting: A bright warm cream stylized background, lighter than their bodies, warm light from the left, deep soft shadows in the creases of the left woman's belly rolls and along the right woman's waist and hips, the polished bands and the gold filigree gleaming, glossy anime highlights on every curve.",
VEND)),
]

def build(i, bL, bR, mL, mR):
    L, R, ML, MR = BODY[bL], BODY[bR], MAT[mL], MAT[mR]
    bright = ML[1] or MR[1]
    bg = (DARK_BG if bright else BRIGHT_BG)[i % (4 if bright else 5)]
    light = "a single strong warm light from the left" if bright else "warm light from the left, lighter than their bodies"
    left = (f"Left woman: in her {L[1]}, {L[2]}, {L[3]}. {L[4]} "
            f"Her body is {ML[2]}, covering her from the collarbones to the ankles.")
    right = (f"Right woman: in her {R[1]}, {R[2]}, {R[3]}. {R[4]} "
             f"Her body is {MR[2]}, covering her from the collarbones to the ankles.")
    pose = (f"Pose: The left woman {L[5]}; the right woman {R[5]}. No arm crossing in front of the other woman, "
            f"their shoulders almost touching, together filling the full width of the frame.")
    shoes = (f"Footwear: The left woman wears extreme {ML[3]}; the right woman wears extreme {MR[3]}, "
             f"the platform soles as tall as their ankle bones, the ultra-thin stiletto heels so high their insteps stand nearly vertical.")
    back = (f"Background & Lighting: {bg}, {light}, deep soft shadows in every crease and fold, "
            f"{ML[4]} and {MR[4]}, glossy anime highlights on every curve.")
    return P(VFRONT, STYLE, SUBJ, SKIN, left, right, COVER, pose, shoes, back, VEND)

def validate():
    assert len(VERIFIED) == 5 and len(ENTRIES) == 45
    seen = set()
    for bL, bR, mL, mR, *_ in [e[:4] for e in VERIFIED] + ENTRIES:
        assert bL in BODY and bR in BODY and mL in MAT and mR in MAT, (bL, bR, mL, mR)
        assert bL != bR, (bL, bR)
        assert mL != mR, (mL, mR)
        if "heavymuscle" in (bL, bR): assert {bL, bR} == {"heavymuscle", "glamour"}, (bL, bR)
        for b, m in ((bL, mL), (bR, mR)):
            if b in ROLL_BODIES: assert m != "palekh", f"palekh not for roll bodies: {b}"
        key = (bL, bR, mL, mR)
        assert key not in seen, key
        seen.add(key)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()
    validate()
    os.makedirs(PRESETS, exist_ok=True)
    items = []
    for i, (bL, bR, mL, mR, prompt) in enumerate(VERIFIED, 1):
        items.append((i, bL, bR, mL, mR, prompt))
    for j, (bL, bR, mL, mR) in enumerate(ENTRIES):
        items.append((6 + j, bL, bR, mL, mR, build(j, bL, bR, mL, mR)))
    made = skipped = 0; md = []
    for i, bL, bR, mL, mR, prompt in items:
        key = f"la_anime_duo_{i:02d}_{bL}-{bR}_{mL}-{mR}"
        tag = " (검증)" if i <= 5 else ""
        title = f"Anime Duo {i:02d} · {BODY[bL][0]} × {BODY[bR][0]} · {MAT[mL][0]} × {MAT[mR][0]}{tag}"
        data = {"title": title, "category": CATEGORY, "platform": "gemini", "aspect_ratio": "4:5", "prompt": prompt}
        assert prompt.startswith("Image format") and prompt.rstrip().endswith("taller than it is wide."), key
        md.append(f"## {i:02d}. {title}\n`{key}`\n\n```\n{prompt}\n```\n")
        path = os.path.join(PRESETS, key + ".json")
        if os.path.exists(path) and not a.force:
            skipped += 1; continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        made += 1
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Anime Duo (50)\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")

if __name__ == "__main__":
    main()
