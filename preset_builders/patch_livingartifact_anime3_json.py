# -*- coding: utf-8 -*-
"""
Living Artifact · Anime Blueprint 51-70 (20)
- 01-50과 겹치지 않는 체형 × 재질 × 자세 조합, 헤어스타일 20종 · 신발 20종을 모두 다르게 배정
- 규칙(v5.2): 2D 고정 / near-black 피부 + 얼굴 톤 일치 / 세로 2:3 앞뒤 반복 /
  가슴 커버리지 문장 필수 / 팔레흐는 롤 계열 체형 제외 / apron·옷 단어 금지
- output: presets/la_anime_{51..70}_*.json
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

from importlib.machinery import SourceFileLoader
_base = SourceFileLoader("anime2", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                "patch_livingartifact_anime2_json.py")).load_module()
BODY, MAT, ROLL_BODIES = _base.BODY, _base.MAT, _base.ROLL_BODIES
DARK_BG, BRIGHT_BG, POSE_LABEL = _base.DARK_BG, _base.BRIGHT_BG, _base.POSE_LABEL

# 헤어 20종
HAIR = [
"waist-length straight black hair with a center part",
"a sharp blunt bob with straight bangs",
"a high swinging ponytail tied with a gold cord",
"long box braids gathered over one shoulder",
"a large round afro",
"tight cornrows swept into a high bun",
"glossy finger waves close to the head",
"a short cropped pixie cut",
"waist-length locs with gold cuffs",
"two high space buns",
"a sleek low ponytail tied at the nape",
"shoulder-length loose curls",
"a braided crown wrapped around her head",
"long micro braids falling to her hips",
"an asymmetric bob, one side shaved",
"a voluminous curly half-up half-down style",
"a sleek chignon with a pearl pin",
"long straight hair with blunt bangs",
"a high top knot with loose strands framing her face",
"thick twin braids falling in front of her shoulders",
]
# 신발 20종 (desc, platform 여부)
SHOE = [
("platform stiletto mules", "plat"),
("knee-high stiletto boots", "stil"),
("thigh-high stretch stiletto boots", "stil"),
("ankle-strap stiletto sandals on a thick platform", "plat"),
("transparent clear platform heels", "plat"),
("lace-up platform heels ribboned to mid-calf", "plat"),
("pointed-toe stiletto pumps", "stil"),
("chunky platform ankle boots", "thick"),
("strappy gladiator heels laced to the knee", "stil"),
("mary-jane platform pumps with a thick strap", "plat"),
("peep-toe platform slingbacks", "plat"),
("square-toe platform mules", "plat"),
("wedge platform sandals", "thick"),
("ankle boots with a curved stiletto heel", "stil"),
("T-strap platform sandals", "plat"),
("open-toe platform booties", "plat"),
("crisscross strap platform heels", "plat"),
("stiletto sandals with a wide ankle cuff", "stil"),
("platform sandals with toe rings", "plat"),
("pointed knee-high boots on a platform sole", "plat"),
]

# (body, material, pose) — 01-50과 중복 없음
ENTRIES = [
("ussbbw","celadoninlay","front"), ("ussbbw","eunipsa","front"),
("ussbbw","alebrije","34"), ("ussbbw","cloisonne","front"),
("hgssbbw","sonmai","34"), ("hgssbbw","makie","34"),
("hgssbbw","palekh","34"), ("hgssbbw","malachite","34"),
("heavymuscle","najeon","front"), ("heavymuscle","sonmai","34"),
("heavymuscle","fordite","front"),
("musclehg","najeon","34"), ("musclehg","kintsugi","front"), ("musclehg","sonmai","front"),
("massmonster","jajuyo","front"), ("massmonster","kintsugi","front"), ("massmonster","palekh","front"),
("muscleussbbw","makie","front"), ("muscleussbbw","malachite","front"), ("muscleussbbw","alebrije","front"),
]

def build(i, body, mat, pose, hair, shoe):
    B, M = BODY[body], MAT[mat]
    bright = M[1]
    bg = (DARK_BG if bright else BRIGHT_BG)[i % (4 if bright else 5)]
    light = ("a single strong warm light from one side" if bright
             else "lighter than her body, warm light from one side")
    desc, plat = shoe
    color = {"red lacquer with gold trim": "red lacquer",
             "pearl-white with iridescent shimmer": "iridescent pearl-white"}.get(M[3], M[3])
    tail = {"plat": "the platform soles as tall as her ankle bones, the ultra-thin stiletto heels so high her insteps stand nearly vertical",
            "stil": "towering ultra-thin stiletto heels so high her insteps stand nearly vertical",
            "thick": "towering soles as tall as her ankle bones, so high her insteps stand steeply angled"}[plat]
    return P(VFRONT, STYLE,
        f"Subject: ONE mature adult Black woman in her {B[1]} with clearly adult facial features, {hair}, {B[3]}.",
        f"Physique: {SKIN} {B[4]}",
        f"Body Art: {M[2]} {COVER}",
        B[5][pose],
        f"Footwear: Extreme {color} {desc}, {tail}.",
        f"Background & Lighting: {bg}, {light}, {B[6]}, {M[4]}, glossy anime highlights on every curve.",
        VEND)

def validate():
    assert len(ENTRIES) == 20 and len(HAIR) == 20 and len(SHOE) == 20
    assert len(set(HAIR)) == 20 and len(set(s[0] for s in SHOE)) == 20
    assert all(k in ("plat","stil","thick") for _, k in SHOE)
    seen = set()
    for body, mat, pose in ENTRIES:
        assert body in BODY and mat in MAT and pose in BODY[body][5], (body, mat, pose)
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
        i = 51 + j
        key = f"la_anime_{i}_{body}_{mat}_{pose}"
        title = f"Anime {i} · {BODY[body][0]} · {MAT[mat][0]} · {POSE_LABEL[pose]}"
        prompt = build(j, body, mat, pose, HAIR[j], SHOE[j])
        assert prompt.startswith("Image format") and prompt.rstrip().endswith("taller than it is wide."), key
        data = {"title": title, "category": CATEGORY, "platform": "gemini", "aspect_ratio": "2:3", "prompt": prompt}
        md.append(f"## {i}. {title}\n`{key}` · 헤어: {HAIR[j]} · 신발: {SHOE[j][0]}\n\n```\n{prompt}\n```\n")
        path = os.path.join(PRESETS, key + ".json")
        if os.path.exists(path) and not a.force:
            skipped += 1; continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        made += 1
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Anime Blueprint 51-70 (20) — 헤어·신발 다양화\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")

if __name__ == "__main__":
    main()
