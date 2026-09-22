# -*- coding: utf-8 -*-
"""
Living Artifact · Signature Solo (중간 길이 템플릿 v4) — 55 presets
- 5 body types x 10 (01-50) + Muscle Hourglass · Alebrije 3 (51-53) + Alebrije dark-scene 2 (54-55), validated materials/scenes only (handoff memo v4)
- output: presets/la_sig_solo_{nn}_{body}_{material}_{scene}.json
- options: --force (overwrite), --md out.md (dump all prompts as markdown)
"""
import json, os, sys, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESETS = os.path.join(ROOT, "presets")
CATEGORY = "🏺 Living Artifact · Signature Solo"

SKIN = ("THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, blue-black void complexion darker than night sky, "
        "not brown, her face the same deep tone with natural highlights and clearly defined features, not flat.")

BODY = {
 "glamour": ("Glamour Hourglass",
  "Glamour hourglass bombshell physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — an overwhelmingly enormous full bust, a waist cinched so impossibly tiny it is barely a third of the width of her hips, hips flaring to nearly twice the width of her shoulders, thighs thicker than her waist pressing together, soft full voluptuous curves everywhere. Not skinny, not a runway model, dominating the frame."),
 "musclehg": ("Muscle Hourglass",
  "Muscular hourglass BBW physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits, around 300 pounds — a gigantic heavy bust, broad rounded strong shoulders, enormous thick arms with big defined biceps, a clearly cinched waist that is narrow only in contrast to the enormous bust and the very wide heavy hips, a firm flat stomach with no visible abs, colossal thighs with powerful defined quads, massive calves. Feminine face, warm smile, not masculine, no bodybuilder look, dominating the frame."),
 "hgssbbw": ("Hourglass SSBBW",
  "Hourglass SSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits, around 500 pounds — an overwhelmingly colossal bust, enormous round hips wider than a normal woman's whole torso and flaring far beyond the shoulders, gigantic soft thighs, very thick soft arms, and a sharply cinched waist that stays clearly visible between them, with a soft rounded belly below the waistline that does not hide the waist. Huge, heavy, soft, unmistakably hourglass, not a plus-size model, not a shapeless round body, dominating the frame."),
 "heavy": ("Heavy Muscle",
  "Heavy muscular physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits, around 500 pounds — enormously broad muscular shoulders as wide as her hips, massive arms with big defined biceps, colossal thighs with powerful defined quads, a gigantic bust, no waist at all, the torso a thick straight column, and only the belly soft and round, projecting forward past the chest line, no visible abs, dominating the frame. Feminine face, warm expression, not masculine, no bodybuilder look."),
 "ussbbw": ("USSBBW",
  "USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits, around 800 pounds — an enormous soft apron belly hanging in several heavy overlapping rolls down to mid-thigh, deep creases between each roll, not pregnant, a gigantic bust resting on the belly, no waist at all, deep side rolls, hips wider than a normal woman's whole torso, huge thighs pressed together, enormous soft upper arms, dominating the frame."),
}

SHAPE = {
 "glamour":  "{m} spread wide across the bust and hips and narrow across the tiny waistline.",
 "musclehg": "{m} wrap the swell of the biceps and quads and narrow across the cinched waistline.",
 "hgssbbw":  "{m} spread wide across the colossal bust and hips and narrow across the cinched waistline.",
 "heavy":    "{m} wrap the swell of the shoulders and biceps, curve around the round belly, and sweep along the quads.",
 "ussbbw":   "{m} cover the whole body, {roll}, darker {dark} settling into each deep crease.",
}

CARVE = {
 "glamour":  "carving the impossibly tiny waist",
 "musclehg": "carving the inward curve of the waist and the swell of the biceps and quads",
 "hgssbbw":  "carving the deep inward curve of the waist and the huge curves of the bust and hips",
 "heavy":    "carving the round forward curve of the soft belly and the swell of the shoulders, biceps, and quads",
 "ussbbw":   "carving deep shadows between each belly roll",
}

# name, label, ground, motif, roll, dark, bans, shine, finish, shoes, nails
MAT = {
 "najeon": dict(label="Najeon", name="najeon-chilgi",
   ground="Deep glossy black lacquer densely inlaid with thick cut mother-of-pearl shell pieces with visible sharp cut edges, flashing pink, green, and blue iridescent sheen, not painted, real inlaid shell.",
   motif="Large peony blossoms and continuous vines", roll="a line of mother-of-pearl shell running along each belly roll", dark="lacquer",
   bans="", shine="making every shell piece flash rainbow", finish="lacquer",
   shoes="black lacquer platform stiletto mules with mother-of-pearl studs", nails="extra long stiletto, black with pearl tips"),
 "kintsugi": dict(label="Celadon Kintsugi", name="kintsugi",
   ground="Pale celadon ceramic glaze with fine crackle and blazing raised gold repair seams.",
   motif="The gold seams", roll="a thick gold seam running beneath every single belly roll so each heavy roll is outlined in gold, more gold seams tracing the deep side rolls and the folds of the thighs", dark="glaze",
   bans="", shine="making every gold seam glow", finish="ceramic",
   shoes="platform stiletto mules in translucent iridescent pearl", nails="extra long stiletto, gold mirror tips"),
 "tenmoku": dict(label="Tenmoku", name="tenmoku black glaze",
   ground="Deep glossy black glaze scattered with dense silvery oil-spot flecks and streaks of iridescent blue hare's-fur lines.",
   motif="The silver flecks and blue streaks", roll="", dark="glaze",
   bans="", shine="making every silver fleck sparkle", finish="glaze",
   shoes="gold mirror-chrome platform stiletto mules", nails="extra long almond, black with gold tips"),
 "palekh": dict(label="Palekh", name="Russian Palekh lacquer painting",
   ground="Deep glossy black lacquer densely covered with fine gold-leaf vine scrolls, firebird feather ornaments, and jewel-tone red, blue, and green flowers.",
   motif="The gold scrolls", roll="", dark="lacquer",
   bans="No borders, no bands, not a corset.", shine="making the gold leaf glow", finish="lacquer",
   shoes="red lacquer platform stiletto mules with gold straps", nails="extra long almond, red with gold tips"),
 "lairotnam": dict(label="Lai Rot Nam", name="Thai lai rot nam",
   ground="Brilliant gold leaf covers most of the surface over black lacquer, continuous kranok flame scrolls and flower vines, purely ornamental, no religious figures.",
   motif="The kranok scrolls", roll="", dark="lacquer",
   bans="No bikini-shaped panels.", shine="making the gold leaf blaze", finish="",
   shoes="gold mirror-chrome platform stiletto mules", nails="extra long stiletto, black with gold tips"),
 "sonmai": dict(label="Son Mai", name="Vietnamese son mai lacquer",
   ground="Glossy black and cinnabar-red lacquer with gold-leaf lotus vines and dense crushed white eggshell mosaic of tiny white fragments, not kintsugi.",
   motif="The lotus vines and eggshell mosaic", roll="a line of white eggshell mosaic following each belly roll", dark="lacquer",
   bans="", shine="making the gold leaf and eggshell glint", finish="lacquer",
   shoes="cinnabar-red platform stiletto mules", nails="extra long almond, red with gold-leaf tips"),
 "irezumi_cherry": dict(label="Irezumi Cherry", name="Japanese irezumi body painting",
   ground="A bright indigo and white swirling wave ground with vivid pink, vermilion, and gold cherry blossom branches, one continuous design flowing diagonally across the torso.",
   motif="The waves and blossoms", roll="each belly roll carrying its own curling white-crested wave", dark="pigment",
   bans="Not black shading, no dragons, no koi.", shine="making the glossy colors gleam", finish="",
   shoes="pink lacquer platform stiletto mules", nails="extra long stiletto, pink"),
 "irezumi_waves": dict(label="Irezumi Waves", name="Japanese irezumi body painting",
   ground="A bright indigo and white ground of continuous curling white-crested waves with vermilion and gold wind bars and scattered cherry petals.",
   motif="The waves", roll="each belly roll carrying its own curling white-crested wave", dark="pigment",
   bans="Not black shading, no dragons, no koi.", shine="making the glossy colors gleam", finish="",
   shoes="vermilion lacquer platform stiletto mules", nails="extra long almond, vermilion with gold tips"),
 "irezumi_peony": dict(label="Irezumi Peony", name="Japanese irezumi body painting",
   ground="A bright indigo and white swirling wave ground with vivid vermilion, pink, gold, and jade green botan peony vines, one continuous design flowing diagonally across the torso.",
   motif="The peony vines", roll="", dark="pigment",
   bans="Not black shading, no dragons, no koi.", shine="making the glossy colors gleam", finish="",
   shoes="pink lacquer platform stiletto mules", nails="extra long stiletto, vermilion with pink tips"),
 "khokhloma": dict(label="Khokhloma", name="Russian Khokhloma painting",
   ground="A high-gloss gold ground densely painted with swirling black and red grass curls, red rowan berries, and strawberries.",
   motif="The swirls", roll="a band of black and red swirls along each belly roll", dark="gold",
   bans="No borders, no bands.", shine="making the gold ground gleam", finish="",
   shoes="red lacquer platform stiletto mules", nails="extra long almond, red with gold tips"),
 "minakari": dict(label="Minakari", name="Persian minakari enamel",
   ground="A high-gloss cobalt blue enamel ground with dense turquoise, white, and red arabesques outlined in fine raised gold wire.",
   motif="The arabesques", roll="a fine gold wire line along each belly roll", dark="cobalt",
   bans="No panels, no collar band.", shine="making the gold wire glint", finish="enamel",
   shoes="turquoise enamel platform stiletto mules", nails="extra long almond, cobalt with gold tips"),
 "jingtailan": dict(label="Jingtailan", name="Chinese jingtailan cloisonne enamel",
   ground="A high-gloss turquoise enamel ground divided into small cells by fine raised gold wire, filled with continuous lotus scrolls in red, cobalt, yellow, and white.",
   motif="The lotus scrolls", roll="a fine gold wire line along each belly roll", dark="turquoise",
   bans="No panels, no collar band.", shine="making the gold wire glint", finish="enamel",
   shoes="turquoise enamel platform stiletto mules", nails="extra long stiletto, turquoise with gold tips"),
 "sanggam": dict(label="Celadon Sanggam", name="Goryeo celadon",
   ground="High-gloss jade-green celadon glaze with fine crackle, densely inlaid with black-and-white sanggam lotus arabesques and flying cranes.",
   motif="The lotus arabesques", roll="a black-and-white inlaid ribbon along each belly roll", dark="glaze",
   bans="", shine="making the jade glaze glow", finish="ceramic",
   shoes="celadon platform stiletto mules", nails="extra long almond, celadon with white tips"),
 "dancheong": dict(label="Dancheong", name="Korean dancheong body painting",
   ground="Glossy celadon green, vermilion, cobalt blue, and golden yellow in the style of palace eave painting, large layered lotus medallions and continuous cloud scrolls.",
   motif="The lotus medallions", roll="", dark="green",
   bans="", shine="making the glossy colors gleam", finish="",
   shoes="vermilion lacquer platform stiletto mules", nails="extra long almond, vermilion with celadon tips"),
 "alebrije": dict(label="Alebrije", name="Oaxacan alebrije painting",
   ground="A glossy deep cobalt blue base densely painted in vivid hand-painted patterns of magenta, sunflower yellow, lime green, turquoise, and orange — tiny dots, fine stripes, zigzags, and small flowers packed edge to edge, the patterns fading softly at the wrists and ankles.",
   motif="The flowing bands of pattern", roll="a bright dotted band running along every single belly roll so each heavy roll is outlined in color", dark="cobalt",
   bans="Purely decorative patterns, no animal figures.", shine="making the vivid colors pop", finish="painted",
   shoes="magenta lacquer platform stiletto mules", nails="extra long almond, turquoise with yellow dots"),
 "gamji": dict(label="Gamji Geumni", name="Korean gamji geumni painting",
   ground="A deep indigo-blue ground like dyed indigo paper, not purple, painted in fine shimmering gold ink with continuous lotus scrolls and cloud patterns, purely ornamental, no religious figures.",
   motif="The gold lotus scrolls", roll="", dark="indigo",
   bans="", shine="making the gold ink shimmer", finish="",
   shoes="deep indigo lacquer platform stiletto mules", nails="extra long almond, indigo with gold tips"),
}

# label, text, light, bright?
SCENE = {
 "bamboo":   ("Bamboo Dawn", "A pale misty bamboo grove at dawn, soft white light filtering through tall green stalks", "low sunlight", True),
 "birch":    ("Snowy Birch", "A snowy birch forest on a bright winter morning, white snow and pale trunks", "soft low sunlight", True),
 "desert":   ("Desert Dawn", "Pale golden desert dunes at dawn under a soft white sky, no buildings, no temples", "warm low sunlight", True),
 "atrium":   ("Marble Atrium", "A vast bright white marble atrium with a glass skylight", "soft daylight from above", True),
 "stone":    ("Stone Garden", "A pale misty stone garden at dawn with raked white gravel", "warm low sunlight", True),
 "lotus":    ("Lotus Pond", "A pale misty dawn over a lotus pond under a soft white sky, no buildings, no temples", "warm low sunlight", True),
 "saltflat": ("Salt Flat", "A vast white salt flat at sunrise under a pale sky", "warm low sunlight", True),
 "cream":    ("Cream Studio", "A seamless warm cream studio backdrop with no props", "soft warm light from one side", True),
 "palace":   ("Palace Eaves", "Beneath the eaves of a Korean royal palace hall, painted dancheong rafters and red columns softly out of focus, warm daylight glowing beyond", "warm bounce light", True),
 "greenhouse": ("Rainy Greenhouse", "Inside a dark Victorian glass greenhouse on a rainy night, raindrops streaking the dark glass, lush dark leaves in shadow", "warm lantern light", False),
 "dome":     ("Underwater Dome", "Inside a giant transparent underwater observation dome, the deep dark ocean outside the glass, glowing bioluminescent jellyfish drifting past", "cool light", False),
 "gallery":  ("Dark Gallery", "A dark museum gallery at night with charcoal walls and no objects", "a single warm spotlight from above", False),
 "stage":    ("Dark Stage", "A dark empty stage with a black floor and no props", "a single strong warm spotlight from one side", False),
 "nightgarden": ("Lantern Night Garden", "A dark night garden with paper lanterns glowing softly among black pines", "warm lantern light", False),
}

POSE = {
 "glamour": {
  "hip":   "Standing in a wide stance with a strong hip shift, one hand resting lightly on her outer thigh, the other arm hanging relaxed away from the body.",
  "cross": "A runway cross-step toward the camera, one leg crossing in front of the other with a strong hip shift, her hips still flaring to nearly twice the width of her shoulders, arms relaxed slightly away from the body.",
  "contra":"Standing facing the camera in a relaxed contrapposto, her weight on one leg so that hip juts far outward, the other heel lifted, arms relaxed away from the body.",
  "back":  "Standing with her back three-quarters to the camera, looking back over her shoulder with a smile, one arm hanging away from the body, the painted back, tiny waist, and flaring hips fully visible.",
  "float": "Floating weightlessly inside the dome, legs apart, arms drifting away from the body.",
 },
 "musclehg": {
  "hip":   "Standing in a glamour pose, wide stance with a strong hip shift, arms hanging relaxed slightly away from the body, no flexing.",
  "contra":"Standing facing the camera in a relaxed contrapposto, her weight on one leg so that hip juts outward, the other heel lifted, arms relaxed away from the body, no flexing.",
  "back":  "Standing with her back three-quarters to the camera, looking back over her shoulder with a warm smile, one arm hanging away from the body, the painted broad back, cinched waist, and wide hips fully visible.",
 },
 "hgssbbw": {
  "contra":"Standing facing the camera in a relaxed contrapposto, her weight on one leg so that enormous hip juts far outward, the other heel lifted, arms hanging relaxed slightly away from the body.",
  "front": "Standing full frontal in a wide stance, arms relaxed slightly away from the body.",
  "float": "Floating weightlessly inside the dome, legs apart, arms drifting away from the body.",
 },
 "heavy": {
  "v1": "Standing full frontal in a wide stance with shoulders squared, arms hanging relaxed slightly away from the body.",
  "v2": "Standing full frontal in a wide stance, one arm hanging relaxed away from the body, the other hand resting lightly on her outer thigh.",
 },
 "ussbbw": {
  "front": "Standing full frontal with her feet planted far apart, arms relaxed slightly away from the body, never covering the belly, so every roll is fully visible.",
  "contra":"Standing full frontal in a relaxed contrapposto with her feet planted apart, her weight on one leg so that huge hip juts outward, arms held away from the body, never covering the belly.",
 },
}

BACK_ART = "A large continuous design spreads across the whole back and down over the hips and the backs of the thighs."
COVER = "Densely filled with no plain skin, covering the shoulders and arms completely down to the wrists and the legs down to the ankles."

# (body, material, scene, pose, age, hair)
ENTRIES = [
 # Glamour Hourglass 01-10
 ("glamour","najeon","bamboo","hip","mid 30s","sleek center-parted low bun with a mother-of-pearl binyeo"),
 ("glamour","najeon","atrium","cross","early 30s","sleek high chignon with pearl pins"),
 ("glamour","irezumi_cherry","desert","hip","mid 30s","long glossy waves with gold kanzashi combs"),
 ("glamour","irezumi_waves","cream","back","late 20s","long glossy black waves"),
 ("glamour","jingtailan","gallery","cross","mid 30s","sleek high chignon with gold hairpins"),
 ("glamour","kintsugi","dome","float","early 30s","long black hair floating loosely as if underwater"),
 ("glamour","palekh","birch","contra","late 30s","long voluminous curls with a delicate gold tiara"),
 ("glamour","gamji","saltflat","hip","mid 30s","sleek low bun with a gold binyeo"),
 ("glamour","sanggam","greenhouse","contra","early 40s","sleek high chignon with a jade binyeo"),
 ("glamour","sonmai","stone","back","early 30s","long glossy black waves"),
 # Muscle Hourglass 11-20
 ("musclehg","tenmoku","stone","hip","late 30s","long voluminous curls with gold combs"),
 ("musclehg","palekh","birch","hip","late 30s","long voluminous curls with a delicate gold tiara"),
 ("musclehg","khokhloma","cream","back","mid 30s","long voluminous curls"),
 ("musclehg","irezumi_cherry","desert","back","mid 30s","long glossy black waves"),
 ("musclehg","lairotnam","lotus","hip","mid 30s","long glossy black waves down her back"),
 ("musclehg","najeon","bamboo","contra","late 30s","sleek low bun with a mother-of-pearl binyeo"),
 ("musclehg","kintsugi","greenhouse","hip","early 40s","long black waves down her back"),
 ("musclehg","dancheong","palace","contra","mid 30s","sleek center-parted low bun with a gold binyeo"),
 ("musclehg","minakari","saltflat","hip","late 30s","long knotless box braids piled high with gold cuffs"),
 ("musclehg","tenmoku","atrium","back","mid 30s","long glossy black waves"),
 # Hourglass SSBBW 21-30
 ("hgssbbw","kintsugi","greenhouse","contra","early 40s","long black waves down her back"),
 ("hgssbbw","kintsugi","dome","float","early 40s","long black hair floating loosely as if underwater"),
 ("hgssbbw","minakari","cream","contra","early 40s","sleek center-parted low bun with gold hairpins"),
 ("hgssbbw","dancheong","palace","front","early 40s","sleek center-parted low bun with a gold binyeo"),
 ("hgssbbw","sanggam","gallery","front","mid 30s","sleek high chignon with a jade binyeo"),
 ("hgssbbw","khokhloma","birch","contra","early 40s","long curls with a delicate gold tiara"),
 ("hgssbbw","jingtailan","nightgarden","contra","late 30s","sleek high chignon with gold hairpins"),
 ("hgssbbw","najeon","bamboo","front","mid 40s","silver-streaked low bun with a mother-of-pearl binyeo"),
 ("hgssbbw","irezumi_waves","desert","contra","late 30s","long glossy black waves"),
 ("hgssbbw","gamji","atrium","front","early 40s","sleek low bun with a gold binyeo"),
 # Heavy Muscle 31-40
 ("heavy","lairotnam","desert","v1","mid 30s","long glossy black waves down her back"),
 ("heavy","lairotnam","lotus","v2","late 30s","sleek high bun with gold pins"),
 ("heavy","irezumi_peony","cream","v1","mid 30s","long glossy black waves"),
 ("heavy","palekh","birch","v1","late 30s","long voluminous curls with a delicate gold tiara"),
 ("heavy","tenmoku","stone","v1","mid 30s","long voluminous curls with gold combs"),
 ("heavy","khokhloma","saltflat","v2","early 40s","long curls with a red silk ribbon"),
 ("heavy","najeon","atrium","v1","mid 30s","sleek low bun with a mother-of-pearl binyeo"),
 ("heavy","sonmai","bamboo","v2","late 30s","sleek high bun with gold pins"),
 ("heavy","kintsugi","greenhouse","v1","early 40s","long black waves down her back"),
 ("heavy","gamji","cream","v2","mid 30s","sleek low bun with a gold binyeo"),
 # USSBBW 41-50
 ("ussbbw","kintsugi","greenhouse","front","early 40s","sleek high bun with gold pins"),
 ("ussbbw","kintsugi","dome","front","late 30s","long black hair floating loosely as if underwater"),
 ("ussbbw","kintsugi","gallery","contra","late 30s","short sculpted natural curls"),
 ("ussbbw","sanggam","greenhouse","front","early 40s","sleek high chignon with a jade binyeo"),
 ("ussbbw","jingtailan","gallery","front","late 30s","sleek high bun with gold hairpins"),
 ("ussbbw","sonmai","atrium","front","late 30s","sleek high bun with gold pins"),
 ("ussbbw","sonmai","cream","contra","early 40s","long glossy black waves"),
 ("ussbbw","irezumi_waves","cream","front","late 30s","sleek high bun with red lacquer kanzashi"),
 ("ussbbw","najeon","bamboo","front","mid 40s","silver-streaked low bun with a mother-of-pearl binyeo"),
 ("ussbbw","khokhloma","birch","front","early 40s","long curls with a delicate gold tiara"),
 # Muscle Hourglass · Alebrije 51-53 (added after verification)
 ("musclehg","alebrije","cream","hip","late 30s","long voluminous curls with colorful beaded combs"),
 ("musclehg","alebrije","saltflat","contra","mid 30s","long voluminous curls with colorful beaded combs"),
 ("musclehg","alebrije","atrium","back","late 30s","long voluminous curls with colorful beaded combs"),
 # Alebrije x dark background + spotlight 54-55 (bright material on dark scene, verified)
 ("glamour","alebrije","stage","cross","early 30s","long glossy waves with colorful beaded combs"),
 ("ussbbw","alebrije","gallery","front","late 30s","sleek high bun with colorful beaded combs"),
]

def build(body, mat, scene, pose, age, hair):
    m = MAT[mat]; s = SCENE[scene]
    is_back = (pose == "back")
    if is_back:
        hair = hair + ", pulled over one shoulder so the back is uncovered"
    shape = SHAPE[body].format(m=m["motif"], roll=m["roll"], dark=m["dark"])
    art = [f"Full body {m['name']} painted directly on bare skin, covering every inch from neck to ankle without exception.",
           m["ground"], shape]
    if is_back: art.append(BACK_ART)
    if m["bans"]: art.append(m["bans"])
    art.append(COVER)
    bg = s[1] + (", the background much lighter than her body" if s[3] else "")
    light = f"{s[2]} {CARVE[body]}, {m['shine']}, bright highlights on every glossy curve"
    finish = f"Extreme high-gloss {m['finish']} finish. " if m["finish"] else "Extreme high-gloss finish. "
    return "\n\n".join([
        f"Subject: ONE Black woman in her {age}, {hair}.",
        f"Physique: {SKIN} {BODY[body][1]}",
        "Body Art: " + " ".join(art),
        f"Pose: {POSE[body][pose]}",
        f"Footwear: Extremely high {m['shoes']}. Nails: {m['nails']}.",
        f"Background & Lighting: {bg}, {light}. {finish}2:3 vertical 8K portrait.",
    ])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()
    assert len(ENTRIES) == 55, len(ENTRIES)
    for body, mat, scene, pose, *_ in ENTRIES:
        assert body in BODY and mat in MAT and scene in SCENE and pose in POSE[body], (body, mat, scene, pose)
        if body == "ussbbw": assert MAT[mat]["roll"], f"USSBBW needs roll element: {mat}"
    os.makedirs(PRESETS, exist_ok=True)
    made = skipped = 0; md = []
    for i, e in enumerate(ENTRIES, 1):
        body, mat, scene, pose, age, hair = e
        key = f"la_sig_solo_{i:02d}_{body}_{mat}_{scene}"
        title = f"Signature {i:02d} · {BODY[body][0]} · {MAT[mat]['label']} · {SCENE[scene][0]}"
        prompt = build(*e)
        data = {"title": title, "category": CATEGORY, "platform": "gemini", "aspect_ratio": "2:3", "prompt": prompt}
        path = os.path.join(PRESETS, key + ".json")
        md.append(f"## {i:02d}. {title}\n`{key}`\n\n```\n{prompt}\n```\n")
        if os.path.exists(path) and not a.force:
            skipped += 1; continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        made += 1
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Signature Solo (55)\n\n" + "\n".join(md))
    print(f"[OK] created {made}, skipped {skipped} (existing) -> {CATEGORY}")

if __name__ == "__main__":
    main()
