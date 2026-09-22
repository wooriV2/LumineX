# -*- coding: utf-8 -*-
"""
Living Artifact · Anime Blueprint 71-95 (25)
- 검증된 5개 체형(USSBBW / 아워글래스 SSBBW / 헤비 머슬 / 머슬 USSBBW / 스모)의
  **강화판 체형 블록**으로 체형당 5개씩 25개
- 신발은 전부 플랫폼 스틸레토 계열에서 형태만 조금씩 변형 (25종)
- 헤어 25종 모두 다르게 배정
- 규칙(v5.2): 2D 고정 / near-black 피부 + 얼굴 톤 일치 / 세로 2:3 앞뒤 반복 /
  가슴 커버리지 문장 필수 / 배 길이 상한은 허벅지 중간 / apron·옷 단어 금지
- output: presets/la_anime_{71..95}_*_max.json
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

_base = SourceFileLoader("anime2", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                "patch_livingartifact_anime2_json.py")).load_module()
MAT, DARK_BG, BRIGHT_BG = _base.MAT, _base.DARK_BG, _base.BRIGHT_BG

# ---------------- 강화판 체형 블록 ----------------
# body: (label, age, expression, physique(강화), {pose: sentence}, shadow)
AMP = {
"ussbbw": ("USSBBW", "early 40s", "a calm confident expression",
 "USSBBW physique PUSHED TO THE ABSOLUTE MAXIMUM, THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,200 pounds — an enormous soft belly built from four massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, the lowest roll hanging heavily down to mid-thigh, every roll wider than her own shoulders, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, deep creases between each roll, not pregnant, a gigantic bust resting on the top roll, no waist at all, colossal hips more than three times the width of her shoulders and an enormous rounded rear, colossal thick thighs pressing together, thick heavy calves. Her hips span nearly the full width of the frame and she towers over the viewer.",
 {"34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the stacked belly rolls seen in side profile hanging forward and the enormous rounded curve of her hips and rear jutting out behind her, feet planted apart, arms relaxed away from the body, never covering the belly, full body head to toe.",
  "front": "Pose: Standing full frontal with her feet planted far apart, the heavy belly resting on her thighs, arms relaxed away from the body, never covering the belly, full body head to toe."},
 "deep soft shadows in the creases where each heavy roll of flesh folds over the next"),
"hgssbbw": ("아워글래스 SSBBW", "early 40s", "a serene warm smile",
 "Hourglass SSBBW physique PUSHED TO THE ABSOLUTE MAXIMUM, THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, not a plus-size model, around 750 pounds — a colossal heavy bust wider than her shoulders, a waist indentation still clearly visible even at this size, a huge soft rounded belly below the waistline hanging heavily over the tops of her thighs, enormous round hips nearly four times the width of a normal woman's and far wider than her shoulders, a gigantic rounded rear jutting far out behind her, gigantic soft thighs pressing together down to the knees, huge soft calves, very thick soft arms, a full round face. The contrast between the cinched waist and the colossal hips is extreme.",
 {"34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the waist indentation and the heavy belly below it seen in partial profile, the enormous curve of her hips and rear jutting out behind her, feet planted apart, arms relaxed away from the body, never covering the belly, full body head to toe.",
  "front": "Pose: Standing full frontal with her feet planted apart, the soft belly resting low over her thighs, arms relaxed away from the body, never covering the belly, full body head to toe."},
 "deep cel-shaded shadows under the belly and along the curve of her hips and rear"),
"heavymuscle": ("헤비 머슬", "mid 30s", "a warm confident smile, feminine face",
 "Heavy muscular physique PUSHED TO THE ABSOLUTE MAXIMUM, THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 700 pounds — gigantic boulder shoulders nearly twice the width of her hips, massive arms with huge peaked biceps, thick horseshoe triceps and enormous forearms, a colossal bust, a thick powerful neck and a broad flaring back, no waist at all, the torso one massive column, colossal thighs with enormous defined quads each wider than her own waistline, a huge rounded powerful rear, thick defined calves, and only the belly soft and round, no visible abs. A feminine face with a warm expression, no bodybuilder look. Her shoulders fill the full width of the frame.",
 {"34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the massive shoulder and arm in the foreground, the soft round belly seen in partial profile, the powerful rear and quads behind, feet planted wide, arms hanging relaxed away from the body, full body head to toe.",
  "front": "Pose: Standing full frontal in a wide stance with shoulders squared, arms held slightly away from the body so the full width of the shoulders and arms is visible, full body head to toe."},
 "deep cel-shaded shadows carving the shoulders, arms and quads and under the round belly"),
"muscleussbbw": ("머슬 USSBBW", "early 40s", "a calm powerful smile, feminine face",
 "MUSCULAR USSBBW physique PUSHED TO THE ABSOLUTE MAXIMUM, THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,250 pounds of colossal muscle and heavy soft flesh — gigantic cannonball shoulders far wider than her hips, massive arms with huge peaked biceps and thick horseshoe triceps showing through a soft layer, enormous forearms, a gigantic bust resting on the top roll, an enormous soft belly built from four massive rounded rolls of heavy soft flesh, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, not pregnant, no waist at all, colossal wide hips, colossal thighs with enormous defined quads bulging out on both sides of the belly, diamond-shaped calves. The muscle is defined only on the shoulders, arms, thighs and calves; the belly and rolls stay soft and round. A feminine face with a warm expression, no bodybuilder look. Her shoulders and hips together fill the full width of the frame.",
 {"front": "Pose: Standing full frontal with her feet planted wide, the heavy belly resting on her thighs, both arms held slightly away from the body with the biceps flexed, full body head to toe.",
  "34": "Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, the massive shoulder and arm in the foreground, the stacked belly rolls seen in side profile hanging forward, the enormous curve of her rear and quads behind, feet planted wide, arms held slightly away from the body, full body head to toe."},
 "deep soft shadows in the creases where each heavy roll of flesh folds over the next and in every muscle separation"),
"sumo": ("스모", "early 40s", "a calm powerful expression",
 "EXTREME SUMO PHYSIQUE PUSHED TO THE ABSOLUTE MAXIMUM, THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 900 pounds of dense solid mass — a colossal round firm belly forming one single smooth taut dome, half again as wide as her shoulders, the belly broader than it is tall, filling the whole torso from just under the bust down to the hips and merging smoothly into her sides, one solid mass with her chest and hips, with no hanging rolls and no folds, not pregnant, massive rounded shoulders, thick powerful arms, a full heavy bust resting on top of the great dome, broad solid hips, pillar-like colossal thighs each as thick as a normal woman's waist, thick solid calves. Firm and solid rather than soft, smooth rounded surfaces with no visible muscle definition. Her body fills the full width of the frame.",
 {"low": "Pose: A low powerful stance facing the camera, feet planted very wide, knees bent outward, hands resting on her thighs, the great round dome of her belly centered and projecting toward the viewer, full body head to toe.",
  "upright": "Pose: Standing upright full frontal with her feet planted apart, arms hanging relaxed away from the body, the great round dome of her belly centered and projecting toward the viewer, full body head to toe."},
 "a strong curved highlight and deep shadow across the great dome of the belly showing its roundness"),
}

# 헤어 25종
HAIR = [
"a sleek high bun with gold pins", "waist-length straight hair with a center part",
"a wide round afro with a gold headband", "long box braids gathered high on her head",
"a high swinging ponytail tied with a gold cord",
"tight cornrows swept into a thick low bun", "waist-length locs with gold cuffs",
"a blunt bob with straight bangs", "a braided crown wrapped around her head",
"shoulder-length glossy curls",
"a sleek chignon with a jade pin", "long micro braids falling to her hips",
"a high top knot with loose strands framing her face", "thick twin braids over her shoulders",
"a short cropped pixie cut",
"a sleek low ponytail tied at the nape", "long finger waves falling past her shoulders",
"two thick braided buns", "a voluminous curly half-up half-down style",
"long straight hair swept over one shoulder",
"a high topknot bun with a carved bone pin", "a sleek center-parted low bun",
"an asymmetric bob, one side tucked behind her ear", "coiled flat twists gathered at the crown",
"a thick fishtail braid falling to her waist",
]
# 신발 25종 — 전부 플랫폼 스틸레토 계열 변형
SHOE = [
"platform stiletto mules", "open-toe platform stiletto mules with a wide instep band",
"platform stiletto sandals with a single ankle strap", "platform stiletto slingbacks",
"peep-toe platform stiletto pumps",
"platform stiletto sandals with double ankle straps", "square-toe platform stiletto mules",
"platform stiletto sandals with a thin toe strap", "platform stiletto pumps with a closed pointed toe",
"platform stiletto sandals with a wide ankle cuff",
"crisscross strap platform stiletto sandals", "platform stiletto mules with a rounded toe",
"platform stiletto sandals laced around the ankle", "T-strap platform stiletto sandals",
"platform stiletto ankle-strap pumps",
"platform stiletto mules with a scalloped edge", "platform stiletto sandals with a buckled cuff",
"platform stiletto slides with a thick toe band", "platform stiletto sandals with toe rings",
"platform stiletto mules with a mirror-finish sole",
"platform stiletto sandals with a braided strap", "platform stiletto pumps with an open back",
"platform stiletto mules with a squared toe band", "platform stiletto sandals with twin instep straps",
"platform stiletto mules with a curved cutout vamp",
]

# (body, material, pose) — 체형당 5개
ENTRIES = [
("ussbbw","najeon","34"), ("ussbbw","jajuyo","front"), ("ussbbw","kintsugi","34"),
("ussbbw","malachite","front"), ("ussbbw","fordite","34"),
("hgssbbw","jajuyo","34"), ("hgssbbw","najeon","front"), ("hgssbbw","alebrije","34"),
("hgssbbw","kintsugi","front"), ("hgssbbw","cloisonne","34"),
("heavymuscle","laironam","34"), ("heavymuscle","eunipsa","front"), ("heavymuscle","jajuyo","front"),
("heavymuscle","makie","34"), ("heavymuscle","najeon","34"),
("muscleussbbw","eunipsa","front"), ("muscleussbbw","laironam","34"), ("muscleussbbw","jajuyo","front"),
("muscleussbbw","najeon","34"), ("muscleussbbw","fordite","front"),
("sumo","jajuyo","low"), ("sumo","najeon","upright"), ("sumo","kintsugi","low"),
("sumo","malachite","upright"), ("sumo","cloisonne","low"),
]
POSE_LABEL = {"34": "3/4 강화", "front": "정면 강화", "low": "정면 낮은 자세 강화", "upright": "정면 직립 강화"}

def build(i, body, mat, pose, hair, shoe):
    B, M = AMP[body], MAT[mat]
    bright = M[1]
    bg = (DARK_BG if bright else BRIGHT_BG)[i % (4 if bright else 5)]
    light = ("a single strong warm light from one side" if bright
             else "lighter than her body, warm light from one side")
    color = {"red lacquer with gold trim": "red lacquer",
             "pearl-white with iridescent shimmer": "iridescent pearl-white"}.get(M[3], M[3])
    return P(VFRONT, STYLE,
        f"Subject: ONE mature adult Black woman in her {B[1]} with clearly adult facial features, {hair}, {B[2]}.",
        f"Physique: {SKIN} {B[3]}",
        f"Body Art: {M[2]} {COVER}",
        B[4][pose],
        f"Footwear: Extreme {color} {shoe}, the platform soles as tall as her ankle bones, the ultra-thin stiletto heels so high her insteps stand nearly vertical.",
        f"Background & Lighting: {bg}, {light}, {B[5]}, {M[4]}, glossy anime highlights on every curve.",
        VEND)

def validate():
    assert len(ENTRIES) == 25 and len(HAIR) == 25 and len(SHOE) == 25
    assert len(set(HAIR)) == 25 and len(set(SHOE)) == 25
    assert all("platform stiletto" in s for s in SHOE)
    from collections import Counter
    c = Counter(b for b, _, _ in ENTRIES)
    assert set(c) == set(AMP) and all(v == 5 for v in c.values()), c
    seen = set()
    for body, mat, pose in ENTRIES:
        assert mat in MAT and pose in AMP[body][4], (body, mat, pose)
        assert mat != "palekh", mat
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
        i = 71 + j
        key = f"la_anime_{i}_{body}_{mat}_{pose}_max"
        title = f"Anime {i} · {AMP[body][0]} (강화) · {MAT[mat][0]} · {POSE_LABEL[pose]}"
        prompt = build(j, body, mat, pose, HAIR[j], SHOE[j])
        assert prompt.startswith("Image format") and prompt.rstrip().endswith("taller than it is wide."), key
        data = {"title": title, "category": CATEGORY, "platform": "gemini", "aspect_ratio": "2:3", "prompt": prompt}
        md.append(f"## {i}. {title}\n`{key}` · 헤어: {HAIR[j]} · 신발: {SHOE[j]}\n\n```\n{prompt}\n```\n")
        path = os.path.join(PRESETS, key + ".json")
        if os.path.exists(path) and not a.force:
            skipped += 1; continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        made += 1
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Anime Blueprint 71-95 (25) — 체형 강화판\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")

if __name__ == "__main__":
    main()
