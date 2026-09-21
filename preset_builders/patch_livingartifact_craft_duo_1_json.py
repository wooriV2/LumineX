# -*- coding: utf-8 -*-
"""
patch_livingartifact_craft_duo_1_json.py
Living Artifact · Craft Duo — 12 presets (complete-text format)

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_craft_duo_1_json.py
    python preset_builders\patch_livingartifact_craft_duo_1_json.py --force   (overwrite existing)

- Writes presets/{key}.json  (utf-8, ensure_ascii=False)
- Duo aspect ratio fixed to 3:4 (field + prompt text normalized)
- Existing files are skipped unless --force
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

CATEGORY = "🏺 Living Artifact · Craft Duo"
PLATFORM = "gemini"
ASPECT = "3:4"

PRESETS = [
    # ── 같은 권역 6 (검증 자세판) ──────────────────────────────
    {
        "key": "la_craft_duo_najeon_black_celadon",
        "title": "LA Craft Duo – Black Najeon × Celadon Sanggam",
        "prompt": """Subject: TWO extremely large SuperBBW Korean women standing in three-quarter front view facing the camera, no touching, clear space between them. LEFT: ONE extremely large SuperBBW woman in her early 60s, silver-white hair in a low bun with a mother-of-pearl binyeo. RIGHT: ONE extremely large SuperBBW woman in her late 30s, long black hair in a low braid with a jade pin. Two clearly distinct faces, bright smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies with soft rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, paint fades softly at the neck, no collar, no waistband, no horizontal bands. Pelvis, inner thighs, sides of hips, and both arms fully patterned, dense pattern on hips and thighs, minimal plain base areas. LEFT: deep glossy black najeon lacquer with subtle brush texture and iridescent pink-green-blue mother-of-pearl moon, cranes, pine, and clouds. RIGHT: high-gloss jade-green celadon glaze with fine crackle and dense black-and-white sanggam cranes, clouds, and chrysanthemums. Each material strictly separate. Authentic Korean style.

Pose: LEFT with feet together and hips shifted outward, both hands gently framing her face, elbows out. RIGHT in a wide stance with one arm extended gracefully out to the side, the other hand on her hip, chin lifted. Full bodies head to toe visible.

Footwear: LEFT 8-inch black lacquer platform stilettos with pearl inlay. RIGHT 8-inch celadon platform stilettos with crane details.
Nails: LEFT black with pearl tips. RIGHT celadon with white tips.

Background & Lighting: Hanok daecheong hall with paper lattice doors and a white moon jar, softly blurred. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm window light with raking side light. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_gamji_najeon_vermilion",
        "title": "LA Craft Duo – Gamji-geumni × Vermilion Najeon",
        "prompt": """Subject: TWO extremely large SuperBBW Korean women standing in three-quarter front view facing the camera, no touching, clear space between them. LEFT: ONE extremely large SuperBBW woman in her late 50s, silver-white hair in a low jjok-meori bun with a gold binyeo. RIGHT: ONE extremely large SuperBBW woman in her mid-40s, black hair in a tall eonjeun-meori updo with mother-of-pearl tteoljam. Two clearly distinct faces, regal smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies with soft rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, no collar, no waistband, no horizontal bands. Pelvis, inner thighs, sides of hips, and both arms fully patterned, dense pattern on hips and thighs. LEFT: glossy deep navy-indigo gamji-geumni base, not purple, with bold dense gold ink lotus medallions, vine scrolls, and cloud bands, no religious figures. RIGHT: deep glossy vermilion lacquer clearly different from skin, with dense iridescent mother-of-pearl phoenixes, bamboo, and clouds covering both legs. Each material strictly separate. Authentic Korean Joseon style.

Pose: LEFT in frontal contrapposto with both arms raised overhead, wrists lightly crossed, torso lengthened. RIGHT leaning one shoulder against a red lacquered palace column, ankles crossed, one hand on her hip. Full bodies head to toe visible.

Footwear: LEFT 8-inch indigo lacquer platform stilettos with fine gold lines. RIGHT 8-inch vermilion lacquer platform Mary Jane stilettos with pearl buckles.
Nails: LEFT indigo with gold tips. RIGHT vermilion with pearl tips.

Background & Lighting: Joseon palace hall with red columns, dancheong beams, and an Irworobongdo screen, softly blurred. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm golden key with raking side light. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_makie_kintsugi_celadon",
        "title": "LA Craft Duo – Maki-e × Kintsugi (Celadon)",
        "prompt": """Subject: TWO extremely large SuperBBW Japanese women walking side by side toward the camera, no touching, clear space between them. LEFT: ONE extremely large SuperBBW woman in her early 40s, glossy black hair in a high chignon with gold kanzashi. RIGHT: ONE extremely large SuperBBW woman in her late 60s, short silver-white hair neatly set. Two clearly distinct faces, joyful smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies with soft rolling folds swaying as they walk, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, no collar, no horizontal bands. Pelvis, inner thighs, sides of hips, and both arms fully patterned. LEFT: deep glossy black urushi maki-e with fine sprinkled gold dust, visible particles, forming a full moon, autumn grasses, and flying geese, dense pattern on hips and thighs, minimal plain black areas. RIGHT: high-gloss celadon-green ceramic Kintsugi glaze with a dense network of many fine raised gold repair lines. Each material strictly separate.

Pose: Both mid-stride facing the camera in three-quarter front view. LEFT holding an open folding fan at chest height, other arm swinging. RIGHT laughing, one hand lightly lifted, the other arm swinging. Full bodies head to toe visible.

Footwear: LEFT 8-inch black lacquer platform stilettos with gold maki-e. RIGHT 8-inch celadon glazed platform pumps with gold heels.
Nails: LEFT black with gold powder tips. RIGHT celadon with gold tips.

Background & Lighting: Kyoto tea house engawa with shoji screens and a moss garden, softly blurred. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Soft warm daylight with raking side light. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_cloisonne_ru_guan",
        "title": "LA Craft Duo – Cloisonné × Ru-Guan Celadon",
        "prompt": """Subject: TWO extremely large SuperBBW Chinese women standing in three-quarter front view facing the camera, no touching, clear space between them. LEFT: ONE extremely large SuperBBW woman in her early 50s, black hair in a high sleek bun with a gold hairpin. RIGHT: ONE extremely large SuperBBW woman in her late 60s, silver-white hair in a low bun with a pale jade pin. Two clearly distinct faces, composed smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies with soft rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, no collar, no neckline band, no horizontal bands. Pelvis, inner thighs, sides of hips, and both arms fully patterned. LEFT: glossy turquoise jingtailan cloisonné enamel with raised gold wire cells densely filled with lotus scrolls and peonies in coral, cobalt, and white. RIGHT: high-gloss sky-blue-grey Ru-Guan celadon glaze with a fine dense crackle of thin dark lines, not kintsugi, no painted motifs. Each material strictly separate. Authentic Chinese style.

Pose: LEFT leaning one shoulder against a red lacquered column, ankles crossed, arms folded loosely under her bust. RIGHT facing the camera with feet together and hips shifted outward, both hands gently framing her face. Full bodies head to toe visible.

Footwear: LEFT 8-inch turquoise enamel platform stilettos with gold wire. RIGHT 7-inch sky-blue crackle-glazed platform pumps.
Nails: LEFT turquoise with gold tips. RIGHT pale blue with crackle tips.

Background & Lighting: Ming palace hall with red columns, rosewood furniture, and celadon vessels, softly blurred. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm window light with raking side light. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_palekh_zhostovo",
        "title": "LA Craft Duo – Palekh × Zhostovo",
        "prompt": """Subject: TWO extremely large SuperBBW Russian women standing in three-quarter front view facing the camera, no touching, clear space between them. LEFT: ONE extremely large SuperBBW woman in her late 30s, dark auburn hair in a thick braid. RIGHT: ONE extremely large SuperBBW woman in her early 60s, honey-blonde braided crown with silver streaks. Two clearly distinct faces, bright smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies with soft rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, not latex, subtle brush texture, no collar, no horizontal bands. Pelvis, inner thighs, sides of hips, back of thighs, and both arms fully painted, minimal plain black areas. LEFT: glossy black Palekh lacquer densely filled with fine gold-line firebird, troika horses, onion domes, and filigree. RIGHT: glossy black Zhostovo lacquer densely covered with lush painted rose and peony bouquets and gold scroll borders. Each material strictly separate. Authentic Russian style.

Pose: LEFT with one foot raised on a low gilded footstool, knee bent, one hand resting on the raised knee, the other on her hip. RIGHT in frontal contrapposto with both arms raised overhead, wrists lightly crossed. Full bodies head to toe visible.

Footwear: LEFT 8-inch black lacquer platform stilettos with gold firebird. RIGHT 8-inch black lacquer platform stilettos with painted roses.
Nails: LEFT black with gold line tips. RIGHT black with rose tips.

Background & Lighting: Russian imperial ballroom with gilded mouldings and chandeliers, softly blurred. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm chandelier key with raking side light. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_lairodnam_sonmai",
        "title": "LA Craft Duo – Lai Rod Nam × Son Mai",
        "prompt": """Subject: TWO extremely large SuperBBW women standing in three-quarter front view facing the camera, no touching, clear space between them. LEFT: ONE extremely large SuperBBW Thai woman in her late 30s, glossy black hair in a high topknot with a small gold ornament. RIGHT: ONE extremely large SuperBBW Vietnamese woman in her mid-50s, black hair in a low bun with a gold lotus hairpin. Two clearly distinct faces, warm smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies with soft rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, not latex, no collar, no horizontal bands. Pelvis, inner thighs, sides of hips, and both arms fully patterned, dense pattern on hips and thighs. LEFT: deep glossy black lai rod nam lacquer with bright gold-leaf kranok flames, lotus buds, and naga serpents, no religious figures. RIGHT: crackled white eggshell inlay clearly visible as mosaic clouds, set in deep lacquer-black son mai with vermilion accents, gold-leaf lotus, and silver-leaf cranes. Each material strictly separate.

Pose: LEFT in a wide stance with one arm extended gracefully out to the side in a Thai dance gesture, the other hand on her hip. RIGHT with one foot raised on a low black block, knee bent, one hand resting on the raised knee, body and face toward the camera. Full bodies head to toe visible.

Footwear: LEFT 9-inch black lacquer platform stilettos with gold kranok. RIGHT 8-inch black lacquer platform stilettos with gold-leaf lotus.
Nails: LEFT black with gold tips. RIGHT black with eggshell-white tips.

Background & Lighting: MANDATORY seamless matte black studio background with a low black block. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm gold key with raking side light and soft rim light separating the figures. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    # ── 교차 6 (7~9 재작성판) ──────────────────────────────────
    {
        "key": "la_craft_duo_najeon_vermilion_cloisonne",
        "title": "LA Craft Duo – Vermilion Najeon × Cloisonné",
        "prompt": """Subject: TWO extremely large SuperBBW women in three-quarter front view facing the camera, no touching, wide clear space between them. LEFT: ONE extremely large SuperBBW Korean woman in her late 40s, black hair in a sleek high bun with a coral binyeo. RIGHT: ONE extremely large SuperBBW Chinese woman in her mid-30s, the most colossal body in the frame, long black hair in a low ponytail with a jade clasp. Two clearly distinct faces, bright smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies hanging in deep rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. The RIGHT woman is equally colossal, belly hanging in deep rolls and hips far wider than her shoulders. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, paint fades softly at the neck, no collar, no neckline band, no waistband, no horizontal bands. Upper arms, underarms, and forearms fully painted and patterned down to the wrists; pelvis, inner thighs, and sides of hips fully patterned, dense pattern on hips and thighs. No ribbons, no fabric, no accessories on the body. LEFT: deep glossy vermilion najeon lacquer clearly different from skin, with dense iridescent mother-of-pearl peonies, vines, and butterflies. RIGHT: glossy turquoise jingtailan cloisonné enamel with raised gold wire cells densely filled with lotus scrolls in coral, cobalt, and white. Each material strictly separate.

Pose: LEFT in a wide stance with one arm extended gracefully out to the side at shoulder height, the other hand on her own hip. RIGHT with weight on one leg, one hand lifted to shoulder height lightly touching her jade hair clasp, the other hand resting on her own hip. Both hands on their own bodies. Full bodies head to toe visible.

Footwear: LEFT 8-inch vermilion lacquer platform stilettos with mother-of-pearl heels. RIGHT 8-inch turquoise enamel platform stilettos with gold wire.
Nails: LEFT vermilion with pearl tips. RIGHT turquoise with gold tips.

Background & Lighting: East Asian decorative arts museum gallery with lacquerware and cloisonné vessels in glass cases, softly blurred. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm museum key with raking side light. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_gamji_makie",
        "title": "LA Craft Duo – Gamji-geumni × Maki-e",
        "prompt": """Subject: TWO extremely large SuperBBW women in three-quarter front view facing the camera, no touching, wide clear space between them. LEFT: ONE extremely large SuperBBW Korean woman in her late 20s, long black hair in a single low braid falling behind her shoulder, no ribbon. RIGHT: ONE extremely large SuperBBW Japanese woman in her mid-60s, silver-grey hair in a low sculpted bun with a lacquer comb. Two clearly distinct faces, gentle smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies hanging in deep rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, no collar, no horizontal bands. Upper arms, underarms, and forearms fully painted and patterned down to the wrists; pelvis, inner thighs, and sides of hips fully patterned. No ribbons, no fabric, no accessories on the body. LEFT: glossy deep navy-indigo gamji-geumni base, not purple, with bold dense gold ink peony vines, lotus medallions, and cloud bands, no plain indigo areas, no religious figures. RIGHT: deep glossy black urushi maki-e with fine sprinkled gold dust, visible particles, forming sweeping waves, plovers, and chrysanthemums densely across bust, belly, hips, and legs, minimal plain black areas. Each material strictly separate.

Pose: LEFT with feet together and hips shifted outward, both hands gently framing her own face, elbows low and close to her body. RIGHT with one foot raised on a low black block, knee bent, one hand resting on her own raised knee, the other on her own hip, body and face toward the camera. Full bodies head to toe visible.

Footwear: LEFT 8-inch indigo lacquer platform stilettos with fine gold lines. RIGHT 8-inch black lacquer platform stilettos with gold wave heels.
Nails: LEFT indigo with gold tips. RIGHT black with gold powder tips.

Background & Lighting: MANDATORY seamless matte black studio background with a low black block. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm narrow spotlights with raking side light making the gold lines and gold dust shimmer, soft rim light separating the figures. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_minakari_zhostovo",
        "title": "LA Craft Duo – Minakari × Zhostovo",
        "prompt": """Subject: TWO extremely large SuperBBW women in three-quarter front view facing the camera, no touching, wide clear space between them. LEFT: ONE extremely large SuperBBW Iranian woman in her late 40s, long dark waves with a thin gold headband. RIGHT: ONE extremely large SuperBBW Russian woman in her late 20s, long wavy chestnut hair with a small painted hair comb. Two clearly distinct faces, warm smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies hanging in deep rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, paint fades softly at the neck, no collar, no neckline band, no horizontal bands. Upper arms, underarms, and forearms fully painted and patterned down to the wrists; pelvis, inner thighs, sides of hips, and back of thighs fully patterned, dense pattern on hips and thighs. No ribbons, no fabric, no accessories on the body. LEFT: glossy cobalt and turquoise Persian minakari enamel with fine gold outlines, birds, roses, and arabesque vines. RIGHT: glossy black Zhostovo lacquer, not latex, subtle brush texture, densely covered with painted rose and forget-me-not bouquets and gold scroll borders, minimal plain black areas. Each material strictly separate.

Pose: LEFT leaning one shoulder against a white marble column, ankles crossed, both hands resting on her own belly. RIGHT standing apart in open space with weight on one leg, one hand lifted to shoulder height lightly touching her hair comb, the other hand on her own hip. Both hands on their own bodies, no reaching toward each other. Full bodies head to toe visible.

Footwear: LEFT 8-inch cobalt enamel platform stilettos with gold heels. RIGHT 7-inch black lacquer platform stilettos with painted flowers.
Nails: LEFT cobalt with gold tips. RIGHT black with pink rose tips.

Background & Lighting: Grand palace-style decorative arts gallery with marble columns and gilded display cases, softly blurred. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm chandelier key with raking side light. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_ru_guan_khokhloma",
        "title": "LA Craft Duo – Ru-Guan Celadon × Khokhloma",
        "prompt": """Subject: TWO extremely large SuperBBW women in three-quarter front view facing the camera, no touching, clear space between them. LEFT: ONE extremely large SuperBBW Chinese woman in her mid-40s, black hair in a loose low chignon with a celadon hairpin. RIGHT: ONE extremely large SuperBBW Russian woman in her early 70s, silver-white hair in a thick crown braid. Two clearly distinct faces, calm smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies with soft rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, no collar, no horizontal bands, pelvis, inner thighs, sides of hips, and both arms fully covered. LEFT: deep saturated sky-blue-grey Ru-Guan celadon glaze clearly different from skin, with a fine dense crackle of thin dark lines, not kintsugi, no painted motifs. RIGHT: deep glossy black and gold Khokhloma lacquer with dense red rowan berries, golden leaves, and curling grass scrolls. Each material strictly separate.

Pose: LEFT in frontal contrapposto with both arms raised overhead, wrists lightly crossed. RIGHT with one foot raised on a low white block, knee bent, one hand resting on the raised knee, the other on her hip. Full bodies head to toe visible.

Footwear: LEFT 7-inch sky-blue crackle-glazed platform pumps. RIGHT 8-inch black-and-gold lacquer platform stilettos with red berry details.
Nails: LEFT pale blue with crackle tips. RIGHT gold with red tips.

Background & Lighting: Minimal white gallery with pale plinths, softly blurred. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Soft high-key light with raking side light, strong color contrast against white. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_sonmai_kintsugi",
        "title": "LA Craft Duo – Son Mai × Kintsugi (Celadon)",
        "prompt": """Subject: TWO extremely large SuperBBW women walking side by side toward the camera, no touching, clear space between them. LEFT: ONE extremely large SuperBBW Vietnamese woman in her early 30s, long straight black hair past the waist. RIGHT: ONE extremely large SuperBBW Japanese woman in her early 50s, glossy black blunt bob with razor-cut bangs. Two clearly distinct faces, joyful smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies with soft rolling folds swaying as they walk, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, no collar, no horizontal bands, pelvis, inner thighs, sides of hips, and both arms fully patterned. LEFT: crackled white eggshell inlay clearly visible as mosaic clouds, set in deep lacquer-black son mai with gold-leaf lotus and silver-leaf cranes, dense coverage. RIGHT: high-gloss celadon-green ceramic Kintsugi glaze with a dense network of many fine raised gold repair lines. Each material strictly separate.

Pose: Both mid-stride facing the camera in three-quarter front view, arms swinging naturally, LEFT tossing her long hair back with one hand, RIGHT laughing with one hand lightly lifted. Full bodies head to toe visible.

Footwear: LEFT 8-inch black lacquer platform stilettos with gold-leaf lotus. RIGHT 8-inch celadon glazed platform pumps with gold heels.
Nails: LEFT black with eggshell-white tips. RIGHT celadon with gold tips.

Background & Lighting: Asian lacquer and ceramics museum corridor with glass cases, softly blurred. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm museum light with raking side light. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
    {
        "key": "la_craft_duo_celadon_palekh",
        "title": "LA Craft Duo – Celadon Sanggam × Palekh",
        "prompt": """Subject: TWO extremely large SuperBBW women in three-quarter front view facing the camera, no touching, clear space between them. LEFT: ONE extremely large SuperBBW Korean woman in her late 60s, silver-white hair in a soft side-swept bob. RIGHT: ONE extremely large SuperBBW Russian woman in her late 50s, silver-blonde braided crown. Two clearly distinct faces, warm smiles.

Physique: BOTH with IDENTICALLY EXTREME SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE — colossal soft bellies with soft rolling folds, not pregnant, overwhelmingly massive heavy busts, extremely wide hips, enormous thick thighs, very broad soft arms. Both same scale.

Body Art: Each painted directly on bare skin from neck to ankle, one continuous surface, no collar, no horizontal bands, pelvis, inner thighs, sides of hips, and both arms fully patterned, dense pattern on hips and thighs. LEFT: high-gloss jade-green Goryeo celadon glaze with fine crackle and dense black-and-white sanggam chrysanthemum and peony scrolls. RIGHT: glossy black Palekh lacquer, not latex, densely filled with fine gold-line snow maiden, birch forest, winter sleigh, and filigree vines. Each material strictly separate.

Pose: LEFT with one foot raised on a low black block, knee bent, one hand resting on the raised knee, the other on her hip. RIGHT with feet together and hips shifted outward, both hands gently framing her face. Full bodies head to toe visible.

Footwear: LEFT 7-inch celadon platform Mary Jane stilettos with white chrysanthemum buckles. RIGHT 8-inch black lacquer platform stilettos with gold snowflake details.
Nails: LEFT celadon with white tips. RIGHT black with gold tips.

Background & Lighting: MANDATORY seamless matte black studio background with a low black block. TWO women only. Both figures fill the frame equally, low camera angle, 50mm lens. Warm key with raking side light and soft rim light separating the figures. Emphasis on both extremely large SuperBBW bodies at equal scale. 3:4 vertical 8K portrait.""",
    },
]

RATIO_RE = re.compile(r"\b(?:2:3|3:4|4:5)(?= vertical)")


def normalize_prompt(text: str) -> str:
    text = text.strip()
    return RATIO_RE.sub(ASPECT, text)


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
        # round-trip validation
        check = json.loads(path.read_text(encoding="utf-8-sig"))
        assert check["prompt"] and check["aspect_ratio"] == ASPECT
        print(f"[OK]   {path.name}")
        written += 1

    print(f"\nDone. written={written} skipped={skipped} total={len(PRESETS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
