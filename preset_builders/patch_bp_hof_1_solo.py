# -*- coding: utf-8 -*-
"""
patch_bp_hof_1_solo.py
Bodypaint HOF - SOLO 13종 presets/*.json 생성

실행:
    $env:PYTHONUTF8 = "1"
    cd C:\\Dev\\LumineX
    python preset_builders\\patch_bp_hof_1_solo.py
"""
import json
import os
import glob

PRESETS_DIR = "presets"
CATEGORY = "🎨 Bodypaint"

PRESETS = {
    "bp_solo_shibori_indigo_mature": {
        "label": "🌀 시보리 인디고 — 다다미 좌식",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman, petite build, compact proportions, dark brown hair in a high tight bun.\n"
            "Pose: seated on the floor, legs folded to one side, one hand on the mat, torso turned in "
            "three-quarter view.\n\n"
            "Body fully painted with: Japanese shibori indigo — dense resist-dye patterns in deep indigo "
            "and undyed white, tight kumo spiderweb rings over the shoulders, itajime folded triangles "
            "down the torso, fine kanoko dots covering the arms and legs, every surface filled.\n\n"
            "Pigment applied directly on bare skin, pores and skin texture visible, matte.\n"
            "The paint ends at the wrist and ankle in a crisp deliberate border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each.\n\n"
            "Barefoot on tatami.\n"
            "Environment: a quiet tatami room, shoji screen partly open to a garden.\n"
            "Lighting: broad soft daylight through the shoji from the left at a low raking angle, so the "
            "pattern reads clearly on the lit side and falls into natural shadow on the right.\n"
            "Style: quiet documentary fine art photography. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_katazome_crane_pine_mature": {
        "label": "🕊️ 카타조메 학과 솔 — 40대 염색장",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her forties, athletic build, defined shoulders, black hair cropped short.\n"
            "Pose: standing squarely, arms held slightly out from the body, chin level, looking directly "
            "at the camera.\n\n"
            "Body fully painted with: katazome stencil dyeing — crisp repeating motifs cut in paper stencil "
            "style, deep indigo ground with white reserved shapes: flying cranes across the chest, pine "
            "needle clusters over the shoulders, tortoiseshell hexagons down the arms, karakusa vine "
            "scrolls covering the legs. Every motif hard-edged and precisely repeated, tiled edge to edge "
            "with no blank ground anywhere.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in a crisp deliberate border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each.\n\n"
            "Barefoot on wet stone.\n"
            "Environment: a dyeing workshop, long indigo vats sunk in the floor, lengths of dyed cloth "
            "hanging to dry.\n"
            "Lighting: high diffuse daylight from a roof skylight directly above, soft downward modeling, "
            "gentle shadow under the brow and chin.\n"
            "Style: documentary photography of textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_hwarot_phoenix_gold_elder": {
        "label": "🔥 활옷 봉황 금사 — 60대 촛불",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her sixties, full build, dignified bearing, grey hair in a traditional "
            "low chignon with a binyeo pin.\n"
            "Pose: seated on a low wooden chest, back straight, hands folded in the lap, facing the "
            "camera directly.\n\n"
            "Body fully painted with: Korean hwarot bridal embroidery — dense silk thread work in "
            "vermilion, cobalt, jade and gold on a deep red ground. Paired phoenixes across the chest, "
            "peony blooms over the shoulders, lotus and pomegranate down the torso, stylized wave and "
            "rock bands around the legs, every area packed with couched gold outline and satin-stitch "
            "fill. The thread direction is visible and shifts with each shape. No empty ground anywhere.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture and natural age lines "
            "visible through the color.\n"
            "The paint ends at the wrist and ankle in a crisp deliberate border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each.\n\n"
            "Barefoot on a woven mat.\n"
            "Environment: a dim hanok room at night, lacquered chest, folding screen behind.\n"
            "Lighting: warm candlelight from two low candles at the front left, flickering soft key, deep "
            "falloff into shadow, the gold thread catching small specular glints.\n"
            "Style: quiet documentary fine art photography. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_adire_eleko_indigo_mature": {
        "label": "🌑 아디레 엘레코 — 40대 마당",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her forties, full curvy figure, broad hips and defined waist, strong "
            "shoulders, hair in tight cornrows gathered back.\n"
            "Pose: standing with weight on one leg, one hand resting on the outward hip, the other arm "
            "hanging, torso turned three-quarter, chin lifted.\n\n"
            "Body fully painted with: Yoruba adire eleko — deep indigo ground with pale cassava-paste "
            "resist patterns. Olokun concentric ring motifs across the torso, ibadandun grid squares "
            "filled with tiny hand-drawn symbols over the hips and thighs, fine comb-drawn line bands "
            "down the arms. Every square of the grid filled with a different small motif, no blank "
            "ground. Soft irregular bleed at the edges where the resist lifted.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in a thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each.\n\n"
            "Barefoot on packed earth.\n"
            "Environment: a compound courtyard, indigo dye pots, cloth drying on a line.\n"
            "Lighting: late afternoon sun from the side at a low angle, raking hard across the body to "
            "model the hip and waist, warm bounce off the earth on the shadow side.\n"
            "Style: documentary photography of textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_abrbandi_ikat_young": {
        "label": "🔶 아브르반디 이카트 — 20대 실크공방",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her twenties, athletic hourglass build, defined waist and shoulders, "
            "long dark hair in a single thick braid over one shoulder.\n"
            "Pose: mid-turn, one foot crossing behind the other, torso twisting toward the camera while "
            "the hips stay angled away, one arm lifted holding a hanging silk skein.\n\n"
            "Body fully painted with: Uzbek abr-bandi ikat — bold cloud-blurred shapes in crimson, "
            "saffron, emerald and white on black. Large flame and pomegranate forms across the torso, "
            "ram's-horn hooks down the legs, narrow rainbow warp stripes along the arms. Every edge "
            "feathered and bleeding in the characteristic ikat blur. Density high everywhere, colors "
            "packed with no black ground left exposed.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in a thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each.\n\n"
            "Barefoot on a woven rug.\n"
            "Environment: a silk workshop, skeins of dyed thread hanging in rows.\n"
            "Lighting: hard daylight from a high side window raking down across the twist of the torso, "
            "strong shadow in the small of the back, weak fill opposite.\n"
            "Style: documentary photography of textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_andean_pallay_mature": {
        "label": "⛰️ 안데스 파야이 — 30대 고원 후면",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her thirties, curvy strong build, full hips and thighs, defined waist, "
            "black hair in two long braids.\n"
            "Pose: photographed from behind at three-quarter angle, weight on one leg with the hip "
            "pushed out, head turned back over the shoulder toward the camera, one hand resting at "
            "the waist.\n\n"
            "Body fully painted with: Andean pallay weaving — dense pickup-weave bands in crimson, ochre, "
            "black and white running horizontally across the body. Rows of inti sun figures, ch'unchu "
            "zigzag mountains, kinsa cruz stepped crosses, and tiny stylized llamas and birds, each band "
            "tightly packed against the next with narrow striped dividers between. No undyed ground "
            "anywhere.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in a thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each.\n\n"
            "Barefoot on dry grass.\n"
            "Environment: a high altiplano slope, stone wall, distant peaks.\n"
            "Lighting: hard low-angle mountain sun from the side, carving the curve of the back and hip, "
            "deep shadow on the far side, thin cold sky fill.\n"
            "Style: documentary photography of textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_kente_adweneasa_mature": {
        "label": "👑 켄테 아드웨네아사 — 30대 현대 힐",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her thirties, curvy hourglass build, narrow waist and broad hips, hair "
            "in a high sculpted updo.\n"
            "Pose: standing frontally, chest and shoulders square to the camera, one leg crossed slightly "
            "in front of the other, both hands relaxed away from the waist, head level, gazing at the lens.\n\n"
            "Body fully painted with: Ashanti kente strip-weaving — a tight grid of woven blocks in "
            "saffron gold, emerald green, crimson and black. Alternating warp-stripe blocks and solid "
            "weft-float blocks in checkerboard rotation across the entire body, each block filled with "
            "its own small motif — adinkra symbols, zigzag combs, double-headed lozenges. The strip seams "
            "read as fine vertical lines every few inches. No empty ground.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each.\n\n"
            "Footwear: modern polished gold metallic stiletto sandals, thin ankle strap, open toe, "
            "deliberately contemporary against the traditional pattern.\n"
            "Environment: a bright courtyard, folded kente cloth stacked on a low bench.\n"
            "Lighting: hard equatorial sun from the front right at 45 degrees, crisp shadow under the jaw "
            "and bust, white wall bouncing light back onto the shadow side.\n"
            "Style: high fashion editorial meeting textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_miao_batik_silver_mature": {
        "label": "🌀 먀오 바틱 은장 — 30대 목조가옥",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her thirties, hourglass figure, defined waist and rounded hips, long "
            "black hair coiled high with a silver comb.\n"
            "Pose: standing frontally, chest and shoulders square to the camera, both arms held slightly "
            "out from the body, palms forward and open, chin level, direct gaze.\n\n"
            "Body fully painted with: Guizhou Miao wax-resist batik — deep indigo ground with fine white "
            "resist linework. Large spiral whorls across the chest, butterfly-mother figures with "
            "outspread wings over the shoulders, dragon-and-fish forms down the torso, dense concentric "
            "coils and comb-tooth bands filling the legs. Every line hand-drawn and slightly irregular, "
            "the wax crackle visible as fine hairline fractures throughout. No empty indigo ground "
            "remaining.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each.\n\n"
            "Footwear: hand-embroidered cloth shoes, indigo with red and green floral stitching, flat soled.\n"
            "Environment: the interior of a wooden stilt house, batik cloth drying on a rack, open "
            "doorway to a green valley.\n"
            "Lighting: daylight from the open doorway at the front left, 45 degrees, modeling the frontal "
            "form, dim wooden interior falling away behind.\n"
            "Style: documentary photography of textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_ndebele_geometric_mature": {
        "label": "▨ 은데벨레 기하 — 30대 워킹",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her thirties, curvy hourglass build, broad hips and narrow waist, hair "
            "in a high sculpted crown of coiled braids.\n"
            "Pose: mid-stride walking directly toward the camera, one leg forward and crossing slightly, "
            "torso squared and chest frontal, arms swinging naturally, shoulders open, looking straight "
            "into the lens.\n\n"
            "Body fully painted with: Ndebele geometric design — bold flat blocks of cobalt blue, chrome "
            "yellow, crimson, emerald and white, each block outlined in heavy black. Stepped gable and "
            "staircase forms across the chest and torso, razor-edge chevrons down the legs, small "
            "aeroplane and lightbulb motifs set into the larger fields, narrow black banding separating "
            "every shape. Blocks tiled edge to edge with no unpainted ground.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each. Nails long coffin-shaped, lacquered cobalt "
            "blue with a fine black outline.\n\n"
            "Footwear: white leather platform stiletto sandals, chunky 4cm platform, thick ankle cuff, "
            "open toe with painted toenails visible.\n"
            "Environment: a painted courtyard wall in matching Ndebele geometry, out of focus.\n"
            "Lighting: bright frontal-left key at 45 degrees, hard African midday sun quality, crisp "
            "shadow under the jaw and bust, white wall bounce filling the shadow side.\n"
            "Style: high fashion editorial meeting textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_kuba_raffia_mature": {
        "label": "◈ 쿠바 라피아 — 30대 비틀기",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her thirties, athletic hourglass build, defined waist and shoulders, "
            "hair shaved close with a geometric line pattern cut into it.\n"
            "Pose: body angled away from the camera at 45 degrees with the hips turned back, torso "
            "twisting forward so the chest rotates toward the lens and one breast is frontal in "
            "silhouette, one arm crossing the body to rest on the opposite hip, head turned over the "
            "shoulder, direct gaze.\n\n"
            "Body fully painted with: Kuba raffia cloth — irregular interlocking geometry in natural "
            "raffia beige, rust brown, charcoal and black. Meandering key-fret bands that break and "
            "restart out of alignment, cut-pile velvet blocks with visible plush texture, appliqué patch "
            "shapes with hand-stitched edges, small knot rows between fields. Deliberately asymmetric, "
            "every field filled, no repeating grid.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible, the cut-pile "
            "areas reading as raised velvet nap.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each. Nails short almond, lacquered matte charcoal.\n\n"
            "Footwear: sculptural bronze metallic heels with an architectural curved wedge, open toe.\n"
            "Environment: a concrete gallery space, one large Kuba panel mounted behind.\n"
            "Lighting: key from the front right at 45 degrees, raking across the twisted torso to carve "
            "the waist, secondary rim from behind left separating the shoulder.\n"
            "Style: high fashion editorial meeting textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_paj_ntaub_hmong_mature": {
        "label": "❖ 파응다우 몽족 — 30대 워킹",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her thirties, curvy hourglass build, defined waist and broad hips, hair "
            "coiled high in a sculpted turban-style wrap.\n"
            "Pose: mid-stride walking directly toward the camera, one leg crossing forward, torso squared "
            "and chest frontal, shoulders open, arms swinging naturally, chin level, looking into the lens.\n\n"
            "Body fully painted with: Hmong paj ntaub reverse appliqué and cross-stitch — the entire body "
            "surface covered in tiny interlocking geometry with zero blank ground. Snail-shell spiral "
            "coils, elephant-foot squares, ram's-horn hooks and stepped maze frets, all outlined in crisp "
            "black and filled with magenta, chartreuse, turquoise, orange and white. Motifs sized small "
            "and repeated tightly so the pattern reads as continuous texture at full-body scale. Uniform "
            "density everywhere — no separate panels, no skirt or bodice shape.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each. Nails long coffin-shaped, lacquered bright "
            "turquoise with fine black outline.\n\n"
            "Footwear: white patent platform stiletto sandals, 4cm platform, thick instep band, open toe "
            "with painted toenails visible.\n"
            "Environment: a plain concrete courtyard, one paj ntaub panel hung out of focus behind.\n"
            "Lighting: bright frontal-left key at 45 degrees, hard midday quality, crisp shadow under the "
            "jaw and bust, white wall bounce on the shadow side.\n"
            "Style: high fashion editorial meeting textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_termeh_boteh_mature": {
        "label": "🪶 테르메 보테 — 40대 앉은 비틀기",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her forties, full hourglass figure, soft strong build with a sharply "
            "defined waist, black hair in a low chignon.\n"
            "Pose: seated on a low bench, hips angled to one side, torso twisting back so the chest turns "
            "toward the camera and reads frontal, one hand planted on the bench behind her, the other "
            "resting on the thigh, spine long, chin level.\n\n"
            "Body fully painted with: Persian termeh weaving — the entire body covered in a continuous "
            "allover boteh paisley field with no plain ground anywhere. Curved teardrop boteh forms in "
            "jewel tones — garnet, lapis, emerald, saffron — each outlined in fine gold and filled with "
            "dense interior floral scrollwork, nested tightly so every boteh touches its neighbours. Tiny "
            "stem-and-leaf fillers occupy any remaining space. Uniform scale and density across chest, "
            "torso, arms and legs — no panels, no borders, no garment shape.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each. Nails medium almond-shaped, lacquered deep "
            "garnet.\n\n"
            "Footwear: garnet-red satin platform stiletto sandals, 3cm platform, open toe with painted "
            "toenails visible.\n"
            "Environment: a dark studio, one antique termeh panel mounted behind.\n"
            "Lighting: warm key from the front left at 45 degrees, low and directional so the gold "
            "outlines flare along the chest and thigh, deep falloff behind.\n"
            "Style: high fashion editorial meeting textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
    "bp_solo_ainu_moreu_mature": {
        "label": "🌀 아이누 모레우 — 30대 측면 비틀기",
        "aspect_ratio": "2:3",
        "prompt": (
            "Professional fashion photograph, full body shot.\n"
            "Model: one woman in her thirties, hourglass figure, narrow waist and rounded hips, long dark "
            "hair loose over one shoulder.\n"
            "Pose: hips in full profile at 90 degrees to the camera, torso rotating forward so the chest "
            "opens toward the lens and one breast reads frontal, shoulders squared to the camera, one arm "
            "extended down along the thigh, the other lifted to the collarbone, head facing the lens "
            "directly.\n\n"
            "Body fully painted with: Ainu attus appliqué and embroidery — the entire body covered in "
            "continuous flowing curvilinear pattern with no plain ground. Interlocking moreu spiral "
            "scrolls and ayus thorn-hook barbs in indigo navy and off-white, each band edged with fine "
            "chain-stitch outlines, the scrolls looping and branching without repeating, dense enough "
            "that navy and white share the surface evenly. Uniform density from collarbone to ankle — no "
            "panel, no band structure, no garment shape.\n\n"
            "Pigment applied directly on bare skin, matte, pores and skin texture visible.\n"
            "The paint ends at the wrist and ankle in ONE thin crisp border; hands and feet bare.\n"
            "Hands fully visible, five separated fingers each. Nails long coffin-shaped, lacquered deep "
            "indigo navy.\n\n"
            "Footwear: pale birch-wood platform wedge sandals, sculptural block form, open toe with "
            "painted toenails visible.\n"
            "Environment: a pale wood gallery interior, one attus robe mounted flat behind.\n"
            "Lighting: cool key from the front left at 45 degrees, raking across the rotated torso to "
            "define the bust and waist, soft rim from behind right.\n"
            "Style: high fashion editorial meeting textile craft. ultra-sharp 8K. portrait 2:3 vertical."
        ),
    },
}


def probe_schema():
    existing = sorted(glob.glob(os.path.join(PRESETS_DIR, "*.json")))
    if not existing:
        print("⚠ 기존 프리셋 JSON 없음 — 스키마 확인 불가")
        return None
    with open(existing[0], encoding="utf-8-sig") as f:
        data = json.load(f)
    print(f"🔍 기존 스키마 참고 ({os.path.basename(existing[0])}): {list(data.keys())}")
    return set(data.keys())


def main():
    os.makedirs(PRESETS_DIR, exist_ok=True)
    ref_keys = probe_schema()
    created, skipped = 0, 0

    for key, body in PRESETS.items():
        path = os.path.join(PRESETS_DIR, f"{key}.json")
        if os.path.exists(path):
            print(f"⏭ 이미 존재: {key}.json")
            skipped += 1
            continue

        payload = {
            "key": key,
            "label": body["label"],
            "category": CATEGORY,
            "prompt": body["prompt"],
            "aspect_ratio": body["aspect_ratio"],
        }

        if ref_keys:
            missing = ref_keys - set(payload.keys())
            extra = set(payload.keys()) - ref_keys
            if missing or extra:
                print(f"   ⚠ {key}: 스키마 차이 (누락 {sorted(missing)} / 추가 {sorted(extra)})")

        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print(f"✅ 생성: {key}.json")
        created += 1

    print(f"\n[SOLO] 총 {created}개 생성 / {skipped}개 스킵")


if __name__ == "__main__":
    main()
