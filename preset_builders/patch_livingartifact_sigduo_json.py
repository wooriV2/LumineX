# -*- coding: utf-8 -*-
"""
Living Artifact · Signature Duo (중간 길이 템플릿 v4, 듀오) — 50 presets
- 재질/체형/장면/자세 블록은 patch_livingartifact_sigsolo_json.py 에서 가져옴 (같은 폴더에 있어야 함)
- 듀오 규칙(메모 v4 8장·0장): 두 윤곽 분리, 헤비 머슬은 글래머와만, 근육 체형끼리 금지(앞/뒤 구성 제외),
  USSBBW는 롤 강조 재질만, 어두운 장면은 두 사람 모두 밝은 재질일 때만
- output: presets/la_sig_duo_{nn}_{bodyL}-{bodyR}_{matL}-{matR}_{scene}.json
- options: --force, --md out.md
"""
import json, os, sys, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_livingartifact_sigsolo_json import BODY, SHAPE, CARVE, MAT, SCENE, POSE, BACK_ART

COVER_DUO = "Densely filled, covering the arms and legs completely."
BACK_ART_DUO = "A large continuous design spreads across the whole back and over the hips."

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Signature Duo"

SKIN_DUO = ("Both women have THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, blue-black void complexion darker than night sky, "
            "not brown, their faces the same deep tone with natural highlights and clearly defined features, not flat.")

BRIGHT_MATS = {"kintsugi", "sanggam", "jingtailan"}

HAIR = {
 "najeon": "sleek low bun with a mother-of-pearl binyeo", "kintsugi": "sleek high bun with gold pins",
 "tenmoku": "long voluminous curls with gold combs", "palekh": "long voluminous curls with a delicate gold tiara",
 "lairotnam": "long glossy black waves down her back", "sonmai": "sleek high bun with gold pins",
 "irezumi_cherry": "long glossy waves with gold kanzashi combs", "irezumi_waves": "sleek high bun with red lacquer kanzashi",
 "irezumi_peony": "long glossy black waves", "khokhloma": "long curls with a red silk ribbon",
 "minakari": "sleek center-parted low bun with gold hairpins", "jingtailan": "sleek high chignon with gold hairpins",
 "sanggam": "sleek high chignon with a jade binyeo", "dancheong": "sleek center-parted low bun with a gold binyeo",
 "gamji": "sleek low bun with a gold binyeo",
}
AGE = {"glamour": "mid 30s", "musclehg": "late 30s", "hgssbbw": "early 40s", "heavy": "mid 30s", "ussbbw": "late 30s"}
AGE_ALT = {"glamour": "early 30s", "musclehg": "mid 30s", "hgssbbw": "mid 40s", "heavy": "late 30s", "ussbbw": "early 40s"}

CONTRAST = {
 ("glamour","ussbbw"):   "a dramatic contrast of an impossibly tiny waist and extreme soft volume",
 ("glamour","heavy"):    "a contrast of an impossibly tiny waist and a straight powerful column",
 ("glamour","hgssbbw"):  "two hourglass figures at two very different sizes",
 ("hgssbbw","ussbbw"):   "two enormous women contrasting a deep hourglass waist with no waist at all",
 ("musclehg","ussbbw"):  "a dramatic contrast of a strong muscular hourglass and extreme soft volume",
 ("musclehg","hgssbbw"): "a strong muscular hourglass beside an enormous soft hourglass",
 ("musclehg","musclehg"):"one facing the camera and one turned away, showing the same strong hourglass figure from the front and from behind",
 ("glamour","glamour"):  "one facing the camera and one turned away, showing the same extreme hourglass from the front and from behind",
 ("hgssbbw","hgssbbw"):  "two matching enormous hourglass figures",
}

# (bodyL, bodyR, matL, matR, scene, poseL, poseR)
ENTRIES = [
 # Glamour x USSBBW 01-12
 ("glamour","ussbbw","najeon","sonmai","atrium","hip","front"),
 ("glamour","ussbbw","najeon","sonmai","cream","cross","contra"),
 ("glamour","ussbbw","jingtailan","kintsugi","gallery","cross","front"),
 ("glamour","ussbbw","sanggam","kintsugi","greenhouse","contra","front"),
 ("glamour","ussbbw","irezumi_cherry","irezumi_waves","cream","hip","front"),
 ("glamour","ussbbw","palekh","khokhloma","birch","contra","front"),
 ("glamour","ussbbw","gamji","sonmai","saltflat","hip","front"),
 ("glamour","ussbbw","kintsugi","sanggam","greenhouse","hip","contra"),
 ("glamour","ussbbw","najeon","najeon","bamboo","cross","front"),
 ("glamour","ussbbw","jingtailan","jingtailan","gallery","contra","front"),
 ("glamour","ussbbw","dancheong","sanggam","palace","hip","front"),
 ("glamour","ussbbw","minakari","kintsugi","cream","hip","front"),
 # Glamour x Heavy Muscle 13-20
 ("glamour","heavy","irezumi_cherry","lairotnam","desert","hip","v1"),
 ("glamour","heavy","najeon","lairotnam","lotus","cross","v2"),
 ("glamour","heavy","jingtailan","palekh","atrium","contra","v1"),
 ("glamour","heavy","kintsugi","tenmoku","stone","hip","v1"),
 ("glamour","heavy","minakari","khokhloma","saltflat","cross","v2"),
 ("glamour","heavy","sanggam","najeon","bamboo","contra","v1"),
 ("glamour","heavy","irezumi_waves","sonmai","cream","hip","v2"),
 ("glamour","heavy","gamji","kintsugi","cream","cross","v1"),
 # Hourglass SSBBW x USSBBW 21-28
 ("hgssbbw","ussbbw","minakari","kintsugi","cream","contra","front"),
 ("hgssbbw","ussbbw","sanggam","kintsugi","greenhouse","contra","front"),
 ("hgssbbw","ussbbw","kintsugi","sanggam","gallery","front","front"),
 ("hgssbbw","ussbbw","dancheong","sonmai","palace","front","contra"),
 ("hgssbbw","ussbbw","khokhloma","khokhloma","birch","contra","front"),
 ("hgssbbw","ussbbw","najeon","sonmai","atrium","front","front"),
 ("hgssbbw","ussbbw","jingtailan","kintsugi","nightgarden","contra","front"),
 ("hgssbbw","ussbbw","gamji","irezumi_waves","cream","front","contra"),
 # Muscle Hourglass x USSBBW 29-33
 ("musclehg","ussbbw","tenmoku","sonmai","stone","hip","front"),
 ("musclehg","ussbbw","palekh","kintsugi","birch","hip","front"),
 ("musclehg","ussbbw","kintsugi","jingtailan","greenhouse","hip","front"),
 ("musclehg","ussbbw","lairotnam","najeon","lotus","contra","front"),
 ("musclehg","ussbbw","irezumi_cherry","irezumi_waves","cream","hip","contra"),
 # Glamour x Hourglass SSBBW 34-38
 ("glamour","hgssbbw","najeon","kintsugi","bamboo","cross","contra"),
 ("glamour","hgssbbw","jingtailan","gamji","atrium","hip","front"),
 ("glamour","hgssbbw","irezumi_cherry","minakari","desert","hip","contra"),
 ("glamour","hgssbbw","palekh","khokhloma","birch","contra","contra"),
 ("glamour","hgssbbw","kintsugi","sanggam","greenhouse","cross","front"),
 # Muscle Hourglass x Hourglass SSBBW 39-42
 ("musclehg","hgssbbw","tenmoku","kintsugi","stone","hip","contra"),
 ("musclehg","hgssbbw","palekh","minakari","cream","contra","front"),
 ("musclehg","hgssbbw","lairotnam","dancheong","lotus","hip","contra"),
 ("musclehg","hgssbbw","kintsugi","jingtailan","gallery","hip","contra"),
 # Muscle Hourglass front x back 43-46
 ("musclehg","musclehg","palekh","irezumi_cherry","cream","hip","back"),
 ("musclehg","musclehg","tenmoku","irezumi_peony","atrium","hip","back"),
 ("musclehg","musclehg","lairotnam","najeon","desert","contra","back"),
 ("musclehg","musclehg","kintsugi","sonmai","stone","hip","back"),
 # Glamour front x back 47-48
 ("glamour","glamour","najeon","irezumi_waves","cream","hip","back"),
 ("glamour","glamour","jingtailan","palekh","atrium","cross","back"),
 # Hourglass SSBBW x Hourglass SSBBW 49-50
 ("hgssbbw","hgssbbw","dancheong","sanggam","palace","front","contra"),
 ("hgssbbw","hgssbbw","minakari","kintsugi","cream","contra","front"),
]

def body_block(body):
    return BODY[body][1].replace(", dominating the frame", "")

def art_block(body, mat, pose):
    m = MAT[mat]
    parts = [f"Full body {m['name']} painted directly on bare skin from neck to ankle.", m["ground"],
             SHAPE[body].format(m=m["motif"], roll=m["roll"], dark=m["dark"])]
    if pose == "back": parts.append(BACK_ART_DUO)
    if m["bans"]: parts.append(m["bans"])
    parts.append(COVER_DUO)
    return " ".join(parts)

def lc(s):
    return s[0].lower() + s[1:]

def figure(side, body, mat, pose, age):
    hair = HAIR[mat] + (", pulled over one shoulder so the back is uncovered" if pose == "back" else "")
    return f"{side} woman — {age}, {hair}. {body_block(body)} Body Art: {art_block(body, mat, pose)}"

def build(bL, bR, mL, mR, scene, pL, pR):
    s = SCENE[scene]
    same = (bL == bR)
    ageL, ageR = AGE[bL], (AGE_ALT[bR] if same else AGE[bR])
    contrast = CONTRAST[(bL, bR)]
    bg = s[1] + (", the background much lighter than their bodies" if s[3] else "")
    if same:
        carve = CARVE[bL]
        shine = f"{MAT[mL]['shine']} on the left and {MAT[mR]['shine']} on the right"
    else:
        carve = f"{CARVE[bL]} on the left and {CARVE[bR].replace('carving ', '', 1)} on the right"
        shine = "making the materials gleam"
    return "\n\n".join([
        f"Subject: TWO Black women standing side by side, clearly separated with no overlap, {contrast}.",
        f"Skin: {SKIN_DUO}",
        figure("Left", bL, mL, pL, ageL),
        figure("Right", bR, mR, pR, ageR),
        f"Pose: The left woman — {lc(POSE[bL][pL])} The right woman — {lc(POSE[bR][pR])}",
        f"Footwear & Nails: The left woman wears extremely high {MAT[mL]['shoes']}; the right woman wears extremely high {MAT[mR]['shoes']}. Extra long nails.",
        f"Background & Lighting: {bg}, {s[2]} {carve}, {shine}, bright highlights on every glossy curve. 3:4 vertical 8K portrait, camera at waist height, 35mm lens.",
    ])

def validate():
    assert len(ENTRIES) == 50, len(ENTRIES)
    for e in ENTRIES:
        bL, bR, mL, mR, scene, pL, pR = e
        assert (bL, bR) in CONTRAST, e
        assert mL in MAT and mR in MAT and scene in SCENE, e
        assert pL in POSE[bL] and pR in POSE[bR], e
        assert "float" not in (pL, pR), e
        if "heavy" in (bL, bR): assert {bL, bR} == {"glamour", "heavy"}, f"heavy muscle partner must be glamour: {e}"
        if bL == "ussbbw" or bR == "ussbbw":
            for b, m in ((bL, mL), (bR, mR)):
                if b == "ussbbw": assert MAT[m]["roll"], f"USSBBW needs roll material: {e}"
        if not SCENE[scene][3]:
            assert mL in BRIGHT_MATS and mR in BRIGHT_MATS, f"dark scene needs two bright materials: {e}"
        if bL == bR and bL in ("musclehg", "glamour"): assert pR == "back", e

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()
    validate()
    os.makedirs(PRESETS, exist_ok=True)
    made = skipped = 0; md = []
    for i, e in enumerate(ENTRIES, 1):
        bL, bR, mL, mR, scene, pL, pR = e
        key = f"la_sig_duo_{i:02d}_{bL}-{bR}_{mL}-{mR}_{scene}"
        title = f"Signature Duo {i:02d} · {BODY[bL][0]} × {BODY[bR][0]} · {MAT[mL]['label']} × {MAT[mR]['label']} · {SCENE[scene][0]}"
        prompt = build(*e)
        data = {"title": title, "category": CATEGORY, "platform": "gemini", "aspect_ratio": "3:4", "prompt": prompt}
        path = os.path.join(PRESETS, key + ".json")
        md.append(f"## {i:02d}. {title}\n`{key}`\n\n```\n{prompt}\n```\n")
        if os.path.exists(path) and not a.force:
            skipped += 1; continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        made += 1
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Signature Duo (50)\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")

if __name__ == "__main__":
    main()
