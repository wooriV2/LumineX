# -*- coding: utf-8 -*-
r"""
patch_livingartifact_craft_fusion_1_json.py
Living Artifact · Craft Fusion — 12 presets (6 fusion lines x standing/seated)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_craft_fusion_1_json.py
    python preset_builders\patch_livingartifact_craft_fusion_1_json.py --force   (overwrite)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · Craft Fusion"
PLATFORM = "gemini"
ASPECT = "2:3"

PRESETS = [
    # 1. Celadon Sanggam + Kintsugi
    {
        "key": "la_craft_fusion_celadon_kintsugi_stand",
        "title": "LA Craft Fusion – Celadon Sanggam + Kintsugi (Standing)",
        "prompt": """Subject: ONE extremely large SuperBBW Korean woman in her mid-30s, black hair in a soft low bun with a jade binyeo, natural face with a serene smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly hanging in deep rolling folds, not pregnant, overwhelmingly massive heavy bust, extremely wide hips, enormous thick thighs, very broad soft arms, belly and hips dominating the frame.

Body Art: Full body fusion body painting from neck to ankle, painted directly on bare skin, one continuous surface. Base: high-gloss jade-green Goryeo celadon glaze with fine crackle and black-and-white sanggam cranes and clouds. Accent: raised 24-karat gold Kintsugi repair seams running through the celadon as if the vessel had been broken and mended with gold, crossing bust, belly rolls, hips, and legs. Upper arms, pelvis, and inner thighs fully covered.

Pose: Standing in a soft three-quarter front view, gentle weight shift to one hip, fingertips lightly touching her binyeo, the other hand relaxed at her side. Full body head to toe visible.

Footwear: 8-inch celadon platform stilettos with gold heels. Nails: celadon with gold tips.

Background & Lighting: Korean ceramics gallery with mended celadon vessels in glass cases, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Cool museum light with warm raking side light making the gold seams glow. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_fusion_celadon_kintsugi_seat",
        "title": "LA Craft Fusion – Celadon Sanggam + Kintsugi (Seated)",
        "prompt": """Subject: ONE extremely large SuperBBW Korean woman in her early 40s, long black hair in a low braid with a jade pin, natural face with a gentle smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly resting in deep rolling folds over the thighs, not pregnant, overwhelmingly massive heavy bust, extremely wide hips spreading across the maru, enormous thick thighs, very broad soft arms.

Body Art: Full body fusion body painting from neck to ankle, painted directly on bare skin, one continuous surface. Base: high-gloss jade-green Goryeo celadon glaze with fine crackle and black-and-white sanggam chrysanthemums and peony scrolls. Accent: raised gold Kintsugi repair seams running across the glaze. Upper arms, pelvis, and inner thighs fully covered.

Pose: Seated on the edge of a wooden maru, hips angled slightly to the side, torso turned softly back toward the camera, legs crossed at the knee, one hand resting on her knee, the other lightly on the maru beside her. Full body head to toe visible.

Footwear: 7-inch celadon platform Mary Jane stilettos with gold buckles. Nails: celadon with gold tips.

Background & Lighting: Hanok room with paper lattice doors and a white moon jar, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Soft window light with warm raking side light. 2:3 vertical 8K portrait.""",
    },
    # 2. Ru-Guan + Kintsugi
    {
        "key": "la_craft_fusion_ru_guan_kintsugi_stand",
        "title": "LA Craft Fusion – Ru-Guan + Kintsugi (Standing)",
        "prompt": """Subject: ONE extremely large SuperBBW Chinese woman in her early 40s, black hair in a soft low chignon with a pale jade pin, natural face with a serene smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly hanging in deep rolling folds, not pregnant, overwhelmingly massive heavy bust, extremely wide hips, enormous thick thighs, very broad soft arms, belly and hips dominating the frame.

Body Art: Full body fusion body painting from neck to ankle, painted directly on bare skin, one continuous surface. Base: high-gloss sky-blue-grey Song dynasty Ru-Guan celadon glaze with a fine dense crackle of thin dark lines, no painted motifs. Accent: raised 24-karat gold Kintsugi repair seams running through the crackled glaze. Upper arms, pelvis, and inner thighs fully covered.

Pose: Standing in a gentle three-quarter front view, head tilted slightly, fingertips lightly touching her hairpin, the other hand resting relaxed at her side. Full body head to toe visible.

Footwear: 7-inch sky-blue crackle-glazed platform pumps with gold heels. Nails: pale blue with gold tips.

Background & Lighting: Song dynasty ceramics gallery with mended celadon bowls in glass cases, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Soft museum light with warm raking side light. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_fusion_ru_guan_kintsugi_seat",
        "title": "LA Craft Fusion – Ru-Guan + Kintsugi (Seated)",
        "prompt": """Subject: ONE extremely large SuperBBW Chinese woman in her late 20s, long straight black hair loose over one shoulder, natural face with a soft smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly resting in deep rolling folds over the thighs, not pregnant, overwhelmingly massive heavy bust, extremely wide hips spreading across the stool, enormous thick thighs, very broad soft arms.

Body Art: Full body fusion body painting from neck to ankle, painted directly on bare skin, one continuous surface. Base: high-gloss pale grey-green Guan ware celadon glaze with a fine dense crackle of thin dark lines, no painted motifs. Accent: raised gold Kintsugi repair seams crossing the glaze. Upper arms, pelvis, and inner thighs fully covered.

Pose: Seated on a carved stone garden stool, hips angled slightly to the side, torso turned softly toward the camera, legs crossed at the knee, one hand on her knee, the other resting gently on her belly. Full body head to toe visible.

Footwear: 7-inch grey-green crackle-glazed platform Mary Jane stilettos with gold buckles. Nails: pale celadon with gold tips.

Background & Lighting: Classical Hangzhou garden pavilion with a misty lake, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Soft diffused daylight with warm raking side light. 2:3 vertical 8K portrait.""",
    },
    # 3. Minakari + Kintsugi
    {
        "key": "la_craft_fusion_minakari_kintsugi_stand",
        "title": "LA Craft Fusion – Minakari + Kintsugi (Standing)",
        "prompt": """Subject: ONE extremely large SuperBBW Iranian woman in her late 40s, long dark waves with a thin gold headband, natural face with kohl-lined eyes and a gentle smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly hanging in deep rolling folds, not pregnant, overwhelmingly massive heavy bust, extremely wide hips, enormous thick thighs, very broad soft arms, belly and hips dominating the frame.

Body Art: Full body fusion enamel body painting from neck to ankle, painted directly on bare skin, one continuous surface, no collar band. Base: glossy cobalt and turquoise Persian minakari enamel with fine gold outlines, birds, roses, and arabesque vines. Accent: raised gold Kintsugi-style repair seams cutting across the enamel as if it had been shattered and rejoined with gold. Upper arms, pelvis, and inner thighs fully covered.

Pose: Standing in a relaxed three-quarter front view, weight on one leg, both hands resting softly on her belly, calm gaze toward the camera. Full body head to toe visible.

Footwear: 8-inch cobalt enamel platform stilettos with gold heels. Nails: cobalt with gold tips.

Background & Lighting: Isfahan palace hall with mirror mosaic and arched niches, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Warm lantern light with raking side light. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_fusion_minakari_kintsugi_seat",
        "title": "LA Craft Fusion – Minakari + Kintsugi (Seated)",
        "prompt": """Subject: ONE extremely large SuperBBW Iranian woman in her early 30s, long dark waves swept over one shoulder, natural face with kohl-lined eyes and a soft smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly resting in deep rolling folds over the thighs, not pregnant, overwhelmingly massive heavy bust, extremely wide hips spreading across the divan, enormous thick thighs, very broad soft arms.

Body Art: Full body fusion enamel body painting from neck to ankle, painted directly on bare skin, one continuous surface, no collar band. Base: glossy sky-blue and cobalt Persian minakari enamel with fine gold outlines, nightingales, pomegranates, and paisley vines. Accent: raised gold Kintsugi-style repair seams crossing the enamel. Upper arms, pelvis, and inner thighs fully covered.

Pose: Seated on a low tiled divan, hips angled slightly to the side, torso turned softly toward the camera, legs crossed at the knee, one hand on her knee, the other resting on a cushion beside her. Full body head to toe visible.

Footwear: 7-inch cobalt enamel platform ankle booties with gold heels. Nails: sky blue with gold tips.

Background & Lighting: Shiraz garden pavilion with stained glass casting colored light, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Warm key with raking side light. 2:3 vertical 8K portrait.""",
    },
    # 4. Black Najeon + Maki-e
    {
        "key": "la_craft_fusion_najeon_makie_stand",
        "title": "LA Craft Fusion – Black Najeon + Maki-e (Standing)",
        "prompt": """Subject: ONE extremely large SuperBBW Korean woman in her mid-30s, long black hair in a sleek low bun with a mother-of-pearl binyeo, natural face with a calm smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly hanging in deep rolling folds, not pregnant, overwhelmingly massive heavy bust, extremely wide hips, enormous thick thighs, very broad soft arms, belly and hips dominating the frame.

Body Art: Full body fusion lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex, subtle brush texture beneath the shine. Base: deep glossy black lacquer with iridescent pink-green-blue mother-of-pearl cranes, pine, and plum blossoms. Accent: fine gold dust with individual particles visible drifting like a night sky between the inlays and gathering into soft gold clouds. Upper arms, pelvis, and inner thighs fully covered.

Pose: Standing in a soft three-quarter front view, one knee gently bent, fingertips resting lightly on her collarbone, the other hand loosely at her hip. Full body head to toe visible.

Footwear: 8-inch black lacquer platform stilettos with pearl inlay and gold dust. Nails: black with pearl and gold tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Warm soft key with strong raking side light making the pearl flash rainbow and the gold dust sparkle. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_fusion_najeon_makie_seat",
        "title": "LA Craft Fusion – Black Najeon + Maki-e (Seated)",
        "prompt": """Subject: ONE extremely large SuperBBW Korean woman in her mid-40s, black hair in a low chignon with a mother-of-pearl comb, natural face with a gentle smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly resting in deep rolling folds over the thighs, not pregnant, overwhelmingly massive heavy bust, extremely wide hips spreading across the bench, enormous thick thighs, very broad soft arms.

Body Art: Full body fusion lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Base: deep glossy black lacquer with iridescent mother-of-pearl lotus, mandarin ducks, and ripple patterns. Accent: fine sprinkled gold dust with visible particles drifting between the inlays like moonlight on water. Upper arms, pelvis, and inner thighs fully covered.

Pose: Seated on a low black lacquer bench, hips angled slightly to the side, torso turned softly toward the camera, legs crossed at the knee, one hand on her knee, the other resting lightly on the bench. Full body head to toe visible.

Footwear: 8-inch black lacquer platform Mary Jane stilettos with pearl buckles. Nails: black with pearl and gold tips.

Background & Lighting: Korean lotus pond pavilion at blue hour with warm lanterns reflected in the water, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Warm lantern key with cool ambient and raking side light. 2:3 vertical 8K portrait.""",
    },
    # 5. Khokhloma + Palekh
    {
        "key": "la_craft_fusion_khokhloma_palekh_stand",
        "title": "LA Craft Fusion – Khokhloma + Palekh (Standing)",
        "prompt": """Subject: ONE extremely large SuperBBW Russian woman in her late 20s, long honey-blonde hair in a loose side braid, natural face with a sweet smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly hanging in deep rolling folds, not pregnant, overwhelmingly massive heavy bust, extremely wide hips, enormous thick thighs, very broad soft arms, belly and hips dominating the frame.

Body Art: Full body fusion lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Base: glossy black and gold Khokhloma lacquer with dense red rowan berries, golden leaves, and curling grass scrolls. Accent: fine Palekh-style gold hairline filigree and small firebird silhouettes woven between the berry clusters. Upper arms, pelvis, and inner thighs fully covered.

Pose: Walking slowly toward the camera in three-quarter front view, a relaxed gentle step, arms swaying softly. Full body head to toe visible.

Footwear: 8-inch black-and-gold lacquer platform stilettos with red berry details. Nails: gold with red tips.

Background & Lighting: Russian palace hall with gilded mouldings and chandeliers, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Warm chandelier key with raking side light. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_fusion_khokhloma_palekh_seat",
        "title": "LA Craft Fusion – Khokhloma + Palekh (Seated)",
        "prompt": """Subject: ONE extremely large SuperBBW Russian woman in her early 40s, auburn hair in a soft braided crown, natural face with a warm smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly resting in deep rolling folds over the thighs, not pregnant, overwhelmingly massive heavy bust, extremely wide hips spreading across the bench, enormous thick thighs, very broad soft arms.

Body Art: Full body fusion lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Base: glossy gold and black Khokhloma lacquer with strawberries, currants, and flowing kudrina leaf swirls. Accent: fine Palekh-style gold filigree and small troika horse silhouettes woven between the fruit clusters. Upper arms, pelvis, and inner thighs fully covered.

Pose: Seated on a carved wooden bench, hips angled slightly to the side, torso turned softly toward the camera, legs crossed at the knee, one hand on her knee, the other resting gently on the bench. Full body head to toe visible.

Footwear: 8-inch gold lacquer platform Mary Jane stilettos with red berry buckles. Nails: gold with red tips.

Background & Lighting: Rustic Russian izba interior with a painted tiled stove and wooden utensils, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Warm firelight key with raking side light. 2:3 vertical 8K portrait.""",
    },
    # 6. Lai Rod Nam + Son Mai
    {
        "key": "la_craft_fusion_lairodnam_sonmai_stand",
        "title": "LA Craft Fusion – Lai Rod Nam + Son Mai (Standing)",
        "prompt": """Subject: ONE extremely large SuperBBW Thai woman in her late 30s, glossy black hair in a high topknot with a small gold ornament, natural face with a warm smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly hanging in deep rolling folds, not pregnant, overwhelmingly massive heavy bust, extremely wide hips, enormous thick thighs, very broad soft arms, belly and hips dominating the frame.

Body Art: Full body fusion lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Base: deep glossy black lacquer with bright gold-leaf kranok flame scrolls, lotus buds, and naga serpents in Thai lai rod nam style, no religious figures. Accent: crackled white eggshell inlay clearly visible forming drifting cloud bands across the bust, belly, and thighs in Vietnamese son mai technique, with silver-leaf cranes among them. Upper arms, pelvis, and inner thighs fully covered.

Pose: Standing in a graceful three-quarter front view, gentle weight shift, one hand held softly beside her shoulder in a slow Thai dance gesture with curved fingers, the other resting lightly on her hip. Full body head to toe visible.

Footwear: 9-inch black lacquer platform stilettos with gold kranok and eggshell details. Nails: black with gold and eggshell-white tips.

Background & Lighting: MANDATORY seamless matte black studio background. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Warm soft gold key with raking side light making the gold leaf glow and the eggshell catch the light. 2:3 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_fusion_lairodnam_sonmai_seat",
        "title": "LA Craft Fusion – Lai Rod Nam + Son Mai (Seated)",
        "prompt": """Subject: ONE extremely large SuperBBW Thai woman in her late 20s, long black hair in a low bun with a jasmine garland, natural face with a gentle smile.

Physique: Heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft belly resting in deep rolling folds over the thighs, not pregnant, overwhelmingly massive heavy bust, extremely wide hips spreading across the bench, enormous thick thighs, very broad soft arms.

Body Art: Full body fusion lacquer body painting from neck to ankle, painted directly on bare skin, one continuous surface, not latex. Base: deep glossy black lacquer with gold-leaf kranok borders, flowering vines, and mythical birds in Thai lai rod nam style, no religious figures. Accent: crackled white eggshell inlay clearly visible as cloud bands and lotus petals in Vietnamese son mai technique, with silver-leaf details. Upper arms, pelvis, and inner thighs fully covered.

Pose: Seated on a low gilded teak bench, hips angled slightly to the side, torso turned softly toward the camera, legs crossed at the knee, one hand on her knee, the other resting lightly on the bench. Full body head to toe visible.

Footwear: 8-inch black lacquer platform Mary Jane stilettos with gold kranok buckles. Nails: black with gold tips.

Background & Lighting: Traditional Thai teak house interior with gilded lacquer cabinets and a river view, softly blurred. ONE woman only. Figure fills 90% of the frame, low camera angle, 85mm lens. Warm window light with raking side light. 2:3 vertical 8K portrait.""",
    },
]

RATIO_RE = re.compile(r"\b(?:2:3|3:4|4:5)(?= vertical)")


def normalize_prompt(text: str) -> str:
    return RATIO_RE.sub(ASPECT, text.strip())


def main() -> int:
    force = "--force" in sys.argv
    if not PRESETS_DIR.is_dir():
        print(f"[ERROR] presets dir not found: {PRESETS_DIR}")
        return 1
    keys = [p["key"] for p in PRESETS]
    if len(keys) != len(set(keys)):
        print("[ERROR] duplicate keys in PRESETS")
        return 1

    written, skipped = 0, 0
    for p in PRESETS:
        path = PRESETS_DIR / f"{p['key']}.json"
        if path.exists() and not force:
            print(f"[SKIP] exists: {path.name}")
            skipped += 1
            continue
        data = {
            "title": p["title"],
            "category": CATEGORY,
            "platform": PLATFORM,
            "aspect_ratio": ASPECT,
            "prompt": normalize_prompt(p["prompt"]),
        }
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        check = json.loads(path.read_text(encoding="utf-8-sig"))
        assert check["prompt"] and check["aspect_ratio"] == ASPECT
        print(f"[OK]   {path.name}")
        written += 1

    print(f"\nDone. written={written} skipped={skipped} total={len(PRESETS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
