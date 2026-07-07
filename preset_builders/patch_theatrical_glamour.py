# -*- coding: utf-8 -*-
"""
LumineX 극장적 글래머 30종 패치
- 신규 카테고리: 🎭 극장적 글래머
- 전종 HOF 확정
- 한국 6 / 일본 7 / 중국 5 / 동남아 6 / 서양 6

실행: python preset_builders\patch_theatrical_glamour.py
위치: C:\Dev\LumineX\ 에서 실행
"""

import json
from pathlib import Path

PRESETS_DIR = Path("presets")
META        = Path("core/presets_meta.py")

assert PRESETS_DIR.exists(), "presets/ 없음"
assert META.exists(), "core/presets_meta.py 없음"

# ─────────────────────────────────────────────────────────
# 1. JSON 프리셋 정의
# ─────────────────────────────────────────────────────────

PRESETS = {

    # ── 🇰🇷 한국 6종 ──────────────────────────────────────
    "gyeongbokgung_night_couture": {
        "tag": "Gyeongbokgung Night Couture",
        "subject": "a stunning Korean female model standing before Gwanghwamun gate at night",
        "body": "tall elegant Korean model, sharp features, commanding presence",
        "outfit": "wearing black silk couture gown, deep plunging neckline, structured shoulders, ultra-high slit, dramatic floor-length train, gold embroidery bodice",
        "material": "black silk satin, gold embroidery",
        "environment": "Gyeongbokgung Palace Gwanghwamun gate at night, royal guard ceremony with torches flanking, full moon overhead, wet stone courtyard reflecting torchlight",
        "lighting": "warm torchlight glow, full moon backlight, torch flame illumination on wet stone",
        "style": "modern Korean dark couture editorial",
        "quality": "shot on Hasselblad H6D, Korean palace night grade, portrait 2:3 vertical"
    },
    "bukchon_rain_editorial": {
        "tag": "Bukchon Rain Editorial",
        "subject": "a stunning Korean female model walking in Bukchon Hanok Village in heavy rain",
        "body": "fierce editorial Korean model, rain-soaked hair, wet skin glistening",
        "outfit": "wearing white structured trench coat soaked by heavy rain, belt loosely tied, deep V opening, thigh-high front slit, wet fabric clinging to figure",
        "material": "white cotton trench coat, completely rain-soaked",
        "environment": "Bukchon Hanok Village narrow stone alley at night in heavy rain, traditional tile rooftops, lanterns reflecting in rain puddles, misty Seoul atmosphere",
        "lighting": "warm lantern glow reflected in rain puddles, rain-diffused orange light, wet surface mirror reflections",
        "style": "Korean rain noir editorial",
        "quality": "shot on Canon EOS R5, Seoul rain grade, portrait 2:3 vertical"
    },
    "namsan_tower_dusk": {
        "tag": "Namsan Tower Dusk",
        "subject": "a stunning Korean female model at Namsan Tower observation deck at blue hour",
        "body": "sophisticated Korean model, sharp features, city energy",
        "outfit": "wearing deep navy silk gown, completely backless to lower back, extreme plunging neckline, ultra-high slit exposing full leg, skin-tight form-fitting silhouette",
        "material": "deep navy silk charmeuse, backless",
        "environment": "Namsan Tower Seoul observation deck at blue hour dusk, Han River glittering below, Seoul city grid to horizon, golden blue sky gradient",
        "lighting": "blue hour ambient city glow, golden dusk sky, city light reflection",
        "style": "Seoul skyline couture editorial",
        "quality": "shot on Leica SL2, Seoul blue hour grade, portrait 2:3 vertical"
    },
    "dongdaemun_neon_rain": {
        "tag": "Dongdaemun Neon Rain",
        "subject": "a stunning Korean female model at Dongdaemun Design Plaza in heavy rain at night",
        "body": "fierce Korean model, rain-soaked, neon-lit wet skin glistening",
        "outfit": "wearing silver metallic mini dress, ultra-short barely covering, completely backless, deep plunge, sheer panels on sides, wet fabric clinging to body",
        "material": "silver metallic stretch fabric, wet",
        "environment": "Dongdaemun Design Plaza at night in heavy rain, Zaha Hadid curved white architecture, neon reflections on wet curved surfaces, Korean signage glowing",
        "lighting": "DDP architectural lighting reflecting in rain, neon color cast, wet surface mirror effect",
        "style": "Korean futurism rain editorial",
        "quality": "shot on Sony A7R V, DDP neon grade, portrait 2:3 vertical"
    },
    "haeinsa_temple_dawn": {
        "tag": "Haeinsa Temple Dawn",
        "subject": "a stunning Korean female model at Haeinsa Temple at dawn in autumn",
        "body": "ethereal Korean model with spiritual presence, porcelain skin",
        "outfit": "wearing deep burgundy silk gown, one-shoulder asymmetric, completely backless, ultra-high side slit to hip, draped silk barely covering",
        "material": "deep burgundy silk charmeuse, one-shoulder",
        "environment": "Haeinsa Temple Gayasan mountain at dawn, ancient wooden corridors, Tripitaka Koreana storehouse, autumn maple trees blazing red, morning mist in mountain valley",
        "lighting": "soft golden dawn mountain light, warm wooden corridor glow, autumn amber ambient",
        "style": "Korean heritage couture editorial",
        "quality": "shot on Canon EOS R5, autumn temple grade, portrait 2:3 vertical"
    },
    "jeju_volcanic_coast": {
        "tag": "Jeju Volcanic Coast",
        "subject": "a stunning Korean female model on Jeju volcanic basalt coast in storm",
        "body": "powerful Korean model, wild energy, wind-blown hair, ocean spray on skin",
        "outfit": "wearing black structured gown, completely backless, deep plunging front, ultra-high slit, dramatic train whipping in ocean wind, sheer panels",
        "material": "black silk chiffon, sheer panels, backless",
        "environment": "Jeju Island Jusangjeolli volcanic columnar basalt coast, crashing Pacific waves, dramatic black rock formations, Hallasan silhouette, dark stormy sky",
        "lighting": "dramatic stormy coastal backlight, wave spray mist, powerful natural light",
        "style": "volcanic island editorial",
        "quality": "shot on Nikon Z9, Jeju storm grade, portrait 2:3 vertical"
    },

    # ── 🇯🇵 일본 7종 ──────────────────────────────────────
    "fushimi_inari_crimson": {
        "tag": "Fushimi Inari Crimson",
        "subject": "a stunning Japanese female model in Fushimi Inari torii gate tunnel",
        "body": "fierce Japanese model, pale porcelain skin, predator energy, intense gaze",
        "outfit": "wearing deep crimson silk gown, extreme plunging neckline, ultra-high slit to hip, structured shoulders, completely backless",
        "material": "deep crimson silk satin, backless",
        "environment": "Fushimi Inari Shrine thousand torii gates tunnel at night, endless crimson gates receding into darkness, stone fox guardians, lantern warm glow, sacred mountain mist",
        "lighting": "filtered lantern light through torii gates, crimson red ambient glow, deep mystical shadows",
        "style": "shrine goddess editorial",
        "quality": "shot on Canon EOS R5, Kyoto shrine grade, portrait 2:3 vertical"
    },
    "arashiyama_bamboo_mist": {
        "tag": "Arashiyama Bamboo Mist",
        "subject": "a stunning Japanese female model in Arashiyama bamboo grove at dawn",
        "body": "ethereal Japanese model, pale beauty, serene expression",
        "outfit": "wearing white silk minimal gown, one-shoulder, completely backless, deep side slit to hip, sheer fabric layers barely covering, floating in morning breeze",
        "material": "white silk organza, one-shoulder, sheer",
        "environment": "Arashiyama bamboo grove at dawn, towering green bamboo columns creating cathedral effect, dappled light, stone path, morning mist",
        "lighting": "filtered misty dawn light through bamboo, green ambient, soft ethereal diffused",
        "style": "Kyoto zen couture editorial",
        "quality": "shot on Leica SL2, bamboo mist grade, portrait 2:3 vertical"
    },
    "osaka_dotonbori_neon": {
        "tag": "Osaka Dotonbori Neon",
        "subject": "a stunning Japanese female model at Dotonbori canal in rain at night",
        "body": "fierce Japanese model, Osaka energy, neon reflections dancing on wet skin",
        "outfit": "wearing holographic micro dress, ultra-short barely hip-length, completely backless, deep plunge, color-shifting sequins, wet fabric clinging",
        "material": "holographic sequin stretch, micro-length",
        "environment": "Osaka Dotonbori canal at night in rain, giant Glico running man neon sign, canal reflections, Ebisubashi bridge, neon explosion",
        "lighting": "Dotonbori neon color explosion, rain-diffused glow, wet canal mirror reflections",
        "style": "Osaka neon rain editorial",
        "quality": "shot on Sony A7R V, Dotonbori neon grade, portrait 2:3 vertical"
    },
    "mount_fuji_dawn_silk": {
        "tag": "Mount Fuji Dawn Silk",
        "subject": "a stunning Japanese female model at Chureito Pagoda with Mount Fuji at dawn",
        "body": "serene Japanese goddess model, arms slightly raised",
        "outfit": "wearing white and ice blue silk goddess gown, halter neck deep plunge, completely backless, ultra-high slit both sides, sheer chiffon layers floating in wind",
        "material": "white and ice blue silk chiffon, halter neck, sheer",
        "environment": "Chureito Pagoda at dawn, perfect Mount Fuji reflection in Kawaguchiko lake, cherry blossoms framing, pagoda silhouette, pink dawn sky",
        "lighting": "dawn golden pink light, Fuji water reflection, cherry blossom soft ambient glow",
        "style": "iconic Japan goddess editorial",
        "quality": "shot on Sony A1, Fuji dawn grade, portrait 2:3 vertical"
    },
    "japanese_garden_autumn": {
        "tag": "Japanese Garden Autumn",
        "subject": "a stunning Japanese female model in Kenroku-en Garden in peak autumn",
        "body": "composed classical Japanese beauty, autumn goddess energy",
        "outfit": "wearing deep copper and gold silk gown, strapless structured bodice, completely backless, extreme front slit to hip, obi-inspired waist detail, draped skirt",
        "material": "deep copper silk jacquard, strapless, backless",
        "environment": "Kenroku-en Garden Kanazawa in peak autumn, maple trees blazing crimson and gold, stone lantern reflecting in koi pond, wooden bridge, perfect Japanese garden",
        "lighting": "soft autumn diffused light, maple red ambient, golden pond reflections",
        "style": "Japanese garden couture editorial",
        "quality": "shot on Hasselblad H6D, autumn garden grade, portrait 2:3 vertical"
    },
    "kabukiza_backstage_glam": {
        "tag": "Kabukiza Backstage Glam",
        "subject": "a stunning Japanese female model in Kabukiza Theatre backstage with kabuki makeup",
        "body": "dramatic theatrical Japanese model, kabuki-inspired bold makeup",
        "outfit": "wearing modern black and white structured gown, architectural origami-inspired, deep plunge neckline, completely backless, high slit, sheer black panels revealing figure",
        "material": "black and white structured silk, sheer panels",
        "environment": "Kabukiza Theatre Tokyo backstage, silk kimono racks, large makeup mirror with warm bulb lights, lacquered prop boxes, red curtain glimpse",
        "lighting": "makeup mirror bulb warm glow, backstage amber light, theatrical shadows",
        "style": "contemporary kabuki couture editorial",
        "quality": "shot on Canon EOS R5, kabuki backstage grade, portrait 2:3 vertical"
    },

    # ── 🇨🇳 중국 5종 ──────────────────────────────────────
    "forbidden_city_golden_hour": {
        "tag": "Forbidden City Golden Hour",
        "subject": "a stunning Chinese female model in Forbidden City courtyard at golden hour",
        "body": "commanding Chinese model, imperial dangerous beauty, sharp features",
        "outfit": "wearing deep red qipao-inspired couture gown, extreme thigh-high slit both sides, plunging mandarin collar neckline, gold dragon embroidery, skin-tight form-fitting",
        "material": "deep red silk brocade, gold dragon embroidery",
        "environment": "Forbidden City Beijing main courtyard at golden hour, Hall of Supreme Harmony, yellow glazed tile rooftops glowing gold, red imperial walls, vast empty stone courtyard",
        "lighting": "intense golden hour amber light, imperial red walls radiant glow, long dramatic stone shadows",
        "style": "Imperial China couture editorial",
        "quality": "shot on Phase One XF, Forbidden City golden grade, portrait 2:3 vertical"
    },
    "li_river_karst_mist": {
        "tag": "Li River Karst Mist",
        "subject": "a stunning Chinese female model on bamboo raft on Li River at dawn",
        "body": "ethereal Chinese model, classical ink-wash beauty",
        "outfit": "wearing flowing white silk hanfu-inspired gown, deep V neckline, completely backless, ultra-high side slit, sheer silk layers barely covering, long sleeves trailing",
        "material": "white silk organza, hanfu-inspired, sheer",
        "environment": "Li River Guilin at dawn, dramatic karst mountain peaks emerging from mist, bamboo raft on still water, classical Chinese landscape painting atmosphere",
        "lighting": "dawn mist soft diffused light, ink-wash atmosphere, classical landscape glow",
        "style": "Chinese ink wash couture editorial",
        "quality": "shot on Canon EOS R5, Li River mist grade, portrait 2:3 vertical"
    },
    "shanghai_bund_noir": {
        "tag": "Shanghai Bund Noir",
        "subject": "a stunning Chinese female model on Shanghai Bund at night",
        "body": "1930s Shanghai femme fatale Chinese model, dark eyes, red lips",
        "outfit": "wearing black silk bias-cut gown, deep plunge neckline, completely backless to lower back, ultra-high slit exposing full leg, sheer lace panels, art deco gold jewelry",
        "material": "black silk satin bias-cut, sheer lace panels",
        "environment": "Shanghai Bund at night, art deco colonial buildings illuminated in gold, Pudong skyline across Huangpu River, Pearl Tower, wet cobblestones reflecting lights",
        "lighting": "art deco warm gold illumination, Pudong neon reflection, Shanghai night glamour",
        "style": "Shanghai noir 1930s couture editorial",
        "quality": "shot on Leica SL2, Shanghai noir grade, portrait 2:3 vertical"
    },
    "zhangjiajie_cloud_forest": {
        "tag": "Zhangjiajie Cloud Forest",
        "subject": "a stunning Chinese female model at Zhangjiajie Avatar mountains in cloud",
        "body": "otherworldly powerful Chinese model, forest goddess energy",
        "outfit": "wearing sculptural grey-green silk gown, asymmetric one-shoulder, completely backless, extreme high slit, sheer chiffon panels floating in mountain breeze",
        "material": "grey-green silk chiffon, sculptural, asymmetric",
        "environment": "Zhangjiajie Avatar Hallelujah Mountains, floating sandstone pillars in clouds, ancient trees, sea of clouds below, mystical forest mist",
        "lighting": "cloud-diffused mysterious mountain light, green forest ambient, mist atmosphere",
        "style": "Avatar world couture editorial",
        "quality": "shot on Nikon Z9, Zhangjiajie mist grade, portrait 2:3 vertical"
    },
    "west_lake_lotus_dawn": {
        "tag": "West Lake Lotus Dawn",
        "subject": "a stunning Chinese female model at West Lake Hangzhou at dawn",
        "body": "classical Chinese Song dynasty beauty, lotus goddess energy",
        "outfit": "wearing pale pink and white silk gown, strapless, completely backless, ultra-high slit, sheer chiffon overlay barely covering, lotus embroidery, fabric trailing",
        "material": "pale pink silk chiffon, lotus embroidery, strapless",
        "environment": "Hangzhou West Lake at dawn, pink lotus in full bloom carpet, Broken Bridge arching over water, weeping willows, classical pavilion silhouette, morning mist",
        "lighting": "soft pink dawn light, lotus reflection in still water, classical Chinese painting glow",
        "style": "classical China goddess editorial",
        "quality": "shot on Sony A1, West Lake dawn grade, portrait 2:3 vertical"
    },

    # ── 🌏 동남아 6종 ──────────────────────────────────────
    "bali_tanah_lot_sunset": {
        "tag": "Bali Tanah Lot Sunset",
        "subject": "a stunning Balinese Indonesian female model at Tanah Lot temple at sunset",
        "body": "Balinese goddess model, warm bronzed skin, wind-blown hair",
        "outfit": "wearing deep gold silk goddess gown, sheer fabric clinging to body, deep plunge neckline, completely backless, dramatic train whipping in ocean wind",
        "material": "deep gold silk chiffon, sheer, backless",
        "environment": "Tanah Lot sea temple Bali at sunset, temple silhouette on ocean rock, dramatic crashing waves, blazing orange-red sunset sky, ocean spray mist",
        "lighting": "dramatic sunset backlight, temple silhouette, orange-red sky glow, ocean mist",
        "style": "Balinese goddess editorial",
        "quality": "shot on Canon EOS R5, Bali sunset grade, portrait 2:3 vertical"
    },
    "hoi_an_lantern_rain": {
        "tag": "Hoi An Lantern Rain",
        "subject": "a stunning Vietnamese female model in Hoi An Ancient Town at night in rain",
        "body": "graceful Vietnamese model, delicate beauty, rain-soaked skin glowing",
        "outfit": "wearing white ao dai couture gown, modern interpretation, deep plunge, completely backless, ultra-high slit, sheer wet fabric clinging to slender figure",
        "material": "white silk ao dai, sheer, wet",
        "environment": "Hoi An Ancient Town at night in light rain, hundreds of colorful silk lanterns glowing, Thu Bon River reflections, ancient yellow walls, wet cobblestone streets",
        "lighting": "lantern warm multicolor glow reflected in rain puddles, romantic wet atmosphere",
        "style": "Hoi An lantern rain editorial",
        "quality": "shot on Sony A1, Hoi An lantern grade, portrait 2:3 vertical"
    },
    "bangkok_wat_arun_gold": {
        "tag": "Bangkok Wat Arun Gold",
        "subject": "a stunning Thai female model at Wat Arun Temple Bangkok at golden hour",
        "body": "radiant Thai model, bronzed skin, royal presence",
        "outfit": "wearing deep gold silk goddess gown, halter neck deep plunge, completely backless, ultra-high slit both sides, sheer lace panels revealing bronzed legs",
        "material": "deep gold silk and lace, halter neck, backless",
        "environment": "Wat Arun Temple Bangkok at golden hour, porcelain mosaic spires glowing, Chao Phraya River reflection, longtail boats, blazing golden sky",
        "lighting": "golden hour warm light on mosaic, river mirror reflection, magical hour glow",
        "style": "Thai royal goddess editorial",
        "quality": "shot on Hasselblad H6D, Bangkok golden grade, portrait 2:3 vertical"
    },
    "singapore_marina_bay_night": {
        "tag": "Singapore Marina Bay Night",
        "subject": "a stunning Singaporean Chinese female model at Marina Bay Sands at night",
        "body": "sleek futuristic Singaporean model, sharp beauty",
        "outfit": "wearing structural silver liquid metal gown, sharp geometric lines, completely backless, deep plunge, ultra-high slit, sheer metallic panels, skin-tight",
        "material": "silver liquid metal fabric, geometric, sheer panels",
        "environment": "Marina Bay Sands Singapore infinity pool at night, city skyline reflection in pool, Gardens by the Bay supertrees glowing, spectacular light show",
        "lighting": "Marina Bay light show color, infinity pool reflection, Singapore skyline glow",
        "style": "Singapore luxury futurism editorial",
        "quality": "shot on Sony A7R V, Singapore night grade, portrait 2:3 vertical"
    },
    "luang_prabang_monk_dawn": {
        "tag": "Luang Prabang Monk Dawn",
        "subject": "a stunning Laotian female model in Luang Prabang at dawn alms giving ceremony",
        "body": "serene Laotian model, spiritual beauty, saffron light on bronzed skin",
        "outfit": "wearing saffron and ivory silk gown, one-shoulder, completely backless, ultra-high side slit, sheer silk layers barely covering, flowing monastic-inspired drape",
        "material": "saffron and ivory silk, one-shoulder, sheer",
        "environment": "Luang Prabang alms giving ceremony at dawn, line of saffron-robed monks in procession, ancient temple walls, morning mist, frangipani flowers scattered",
        "lighting": "soft saffron dawn golden light, monk robe ambient glow, sacred misty morning",
        "style": "spiritual Laos goddess editorial",
        "quality": "shot on Canon EOS R5, Luang Prabang dawn grade, portrait 2:3 vertical"
    },
    "rice_terrace_banaue_mist": {
        "tag": "Rice Terrace Banaue Mist",
        "subject": "a stunning Filipino Ifugao female model at Banaue Rice Terraces in morning mist",
        "body": "powerful Filipino earth goddess model, bronzed skin",
        "outfit": "wearing emerald green silk gown, deep plunge neckline, completely backless, ultra-high slit, sheer panels barely covering, tribal gold jewelry, fabric trailing across terraces",
        "material": "emerald green silk chiffon, sheer panels",
        "environment": "Banaue Rice Terraces Philippines at dawn, 2000-year-old terraces carved into mountains, green steps cascading to horizon, cloud sea filling valley, ancient Ifugao villages",
        "lighting": "dawn mist diffused light, green terrace ambient, ancient mountain atmosphere",
        "style": "ancient earth goddess editorial",
        "quality": "shot on Nikon Z9, Banaue mist grade, portrait 2:3 vertical"
    },

    # ── 🌍 서양 6종 ──────────────────────────────────────
    "opera_house_goddess": {
        "tag": "Opera House Goddess",
        "subject": "a stunning French European female model at Paris Opera House Palais Garnier",
        "body": "aristocratic French model, dangerous elegance, sharp cheekbones",
        "outfit": "wearing deep crimson off-shoulder velvet gown, extreme plunging neckline, backless to lower back, ultra-high front slit revealing full leg, long cathedral train, silk opera gloves",
        "material": "deep crimson silk velvet, opera gloves",
        "environment": "Paris Opera House Palais Garnier grand staircase, gilded baroque gold interior, red velvet curtains, crystal chandeliers, gold leaf ceiling, marble staircase",
        "lighting": "warm chandelier golden glow, baroque theatrical illumination",
        "style": "Valentino haute couture opera editorial",
        "quality": "shot on Hasselblad H6D, Paris baroque grade, portrait 2:3 vertical"
    },
    "venetian_carnival_palazzo": {
        "tag": "Venetian Carnival Palazzo",
        "subject": "a stunning Italian European female model in Venice palazzo during carnival",
        "body": "mysterious Italian model, dangerous beauty, dark eyes",
        "outfit": "wearing gold and black Venetian couture gown, extreme plunging neckline, sheer lace panels revealing body, elaborate ornate masquerade mask, jeweled headdress",
        "material": "black lace and gold silk, sheer panels, masquerade",
        "environment": "Venice grand palazzo ballroom during carnival at night, Murano glass chandeliers, canal view through arched windows, masquerade crowd, golden candlelight",
        "lighting": "Murano chandelier warm gold glow, candlelight dancing shadows, carnival mysterious atmosphere",
        "style": "Venetian carnival couture editorial",
        "quality": "shot on Leica SL2, Venice carnival grade, portrait 2:3 vertical"
    },
    "flamenco_tablao_fire": {
        "tag": "Flamenco Tablao Fire",
        "subject": "a stunning Spanish female model dancing flamenco in Seville tablao",
        "body": "fierce passionate Spanish model, smoldering dark eyes, dance energy",
        "outfit": "wearing deep red flamenco couture gown, structured strapless bodice completely backless, extreme high slit both sides, sheer ruffled lace panels, rose in hair, castanets",
        "material": "deep red silk and lace, strapless, sheer ruffles",
        "environment": "intimate Seville tablao flamenco stage at night, dramatic stage spotlight, smoke rising, Spanish Moorish tile walls, candles, audience shadows",
        "lighting": "single dramatic stage spotlight, candle amber glow, passionate red atmosphere, smoke diffusion",
        "style": "Flamenco couture editorial",
        "quality": "shot on Canon EOS R5, Seville flamenco grade, portrait 2:3 vertical"
    },
    "broadway_red_curtain": {
        "tag": "Broadway Red Curtain",
        "subject": "a stunning American female model on Broadway theatre stage",
        "body": "showstopping theatrical American model, Broadway star presence",
        "outfit": "wearing spectacular crystal-encrusted showgirl gown, deep plunge neckline, completely backless, ultra-high slit, sheer panels with strategic crystal coverage, dramatic feather headdress",
        "material": "crystal-encrusted sheer fabric, feather headdress",
        "environment": "Broadway theatre stage, dramatic red velvet curtain parting, single spotlight from above, orchestra pit below, packed house audience in darkness",
        "lighting": "single powerful stage spotlight, red velvet curtain warm glow, theatrical drama",
        "style": "Broadway showstopper editorial",
        "quality": "shot on Phase One XF, Broadway stage grade, portrait 2:3 vertical"
    },
    "scottish_castle_mist": {
        "tag": "Scottish Castle Mist",
        "subject": "a stunning Scottish European female model at Eilean Donan Castle in morning mist",
        "body": "powerful dramatic Scottish model, wild hair in wind",
        "outfit": "wearing dramatic dark tartan and black structured gown, completely backless, deep plunge, ultra-high slit, sheer lace panels barely covering, dramatic train sweeping wet stone",
        "material": "dark tartan and black lace, sheer panels, backless",
        "environment": "Eilean Donan Castle Scotland in morning mist, loch water reflection, highland mountains rising behind, ancient stone bridge, purple heather moorland, dramatic cloudy sky",
        "lighting": "misty highland diffused light, loch mirror reflection, dramatic Scottish atmosphere",
        "style": "Scottish highlands couture editorial",
        "quality": "shot on Nikon Z9, Scottish highlands grade, portrait 2:3 vertical"
    },
    "sahara_dune_queen": {
        "tag": "Sahara Dune Queen",
        "subject": "a stunning North African female model atop Sahara dune at golden hour",
        "body": "commanding North African goddess model, warm bronzed skin",
        "outfit": "wearing liquid gold pleated goddess gown, halter neck deep plunge, completely backless, ultra-high slit both sides, sheer panels barely covering, gold body chain jewelry",
        "material": "liquid gold pleated metallic silk, halter neck",
        "environment": "Sahara desert enormous dune crest at golden hour, endless rolling dune landscape, deep blue sky, camel caravan silhouette far in distance, dramatic long shadows",
        "lighting": "intense golden hour amber sun, warm light on bronzed skin, long dramatic dune shadows",
        "style": "desert goddess editorial",
        "quality": "shot on Hasselblad H6D, Sahara golden grade, portrait 2:3 vertical"
    },
    "ballet_stage_noir": {
        "tag": "Ballet Stage Noir",
        "subject": "a stunning European female model dancing on dark ballet stage with single spotlight",
        "body": "lithe ballerina European model, dark dramatic beauty",
        "outfit": "wearing deconstructed black avant-garde bodysuit, sheer mesh panels revealing figure, black feather skirt barely covering, black feather bodice with strategic coverage, pointe shoes",
        "material": "black feathers, sheer mesh, bodysuit",
        "environment": "completely dark empty ballet stage, single overhead spotlight creating perfect circle of light, low smoke machine fog swirling, distant ballet barre silhouette",
        "lighting": "single harsh overhead spotlight, deep noir shadows, smoke diffusing light edges, theatrical darkness",
        "style": "Black Swan dark couture editorial",
        "quality": "shot on Canon EOS R5, ballet noir grade, portrait 2:3 vertical"
    },
}

# ─────────────────────────────────────────────────────────
# 2. JSON 파일 생성
# ─────────────────────────────────────────────────────────
created = []
skipped = []
for name, data in PRESETS.items():
    p = PRESETS_DIR / f"{name}.json"
    if p.exists():
        skipped.append(name)
    else:
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        created.append(name)

print(f"✅ JSON 생성: {len(created)}개")
if skipped:
    print(f"⚠️  이미 존재 (스킵): {len(skipped)}개 — {skipped}")

# ─────────────────────────────────────────────────────────
# 3. presets_meta.py 패치
# ─────────────────────────────────────────────────────────
text = META.read_text(encoding="utf-8")

PRESET_NAMES = list(PRESETS.keys())
HOF_NAMES    = PRESET_NAMES  # 전종 HOF

# 3-1. PRESET_CATEGORIES에 새 카테고리 추가
CAT_MARKER = '"🎀 미니멀 커버 글래머":'
NEW_CAT = f'''    "🎭 극장적 글래머": {repr(PRESET_NAMES)},
    {CAT_MARKER}'''

if "🎭 극장적 글래머" in text:
    print("⚠️  카테고리 이미 존재 — 스킵")
else:
    assert CAT_MARKER in text, f"카테고리 삽입 마커 없음: {CAT_MARKER}"
    text = text.replace(CAT_MARKER, NEW_CAT, 1)
    print("✅ PRESET_CATEGORIES에 🎭 극장적 글래머 추가")

# 3-2. HOF_TIER에 추가
HOF_MARKER = "# 2026-07-06 공식E 오브제 커버 HOF 7종"
HOF_LINES  = "\n    # 2026-07-07 극장적 글래머 30종 HOF\n"
HOF_LINES += "\n".join([f'    "{n}",' for n in HOF_NAMES]) + "\n"

if HOF_NAMES[0] in text and "극장적 글래머 30종 HOF" not in text:
    # 이미 일부 있으면 블록만 추가
    pass

if "극장적 글래머 30종 HOF" in text:
    print("⚠️  HOF 이미 존재 — 스킵")
else:
    assert HOF_MARKER in text, f"HOF 마커 없음: {HOF_MARKER}"
    text = text.replace(HOF_MARKER, HOF_LINES + "    " + HOF_MARKER, 1)
    print("✅ HOF_TIER에 30종 추가")

# 3-3. SSS_TIER에 추가
SSS_MARKER = "    # 2026-07-06 공식E 오브제 커버 HOF→SSS 포함 (7종) + SSS 1종"
SSS_LINES  = "    # 2026-07-07 극장적 글래머 30종 SSS\n"
SSS_LINES += "\n".join([f'    "{n}",' for n in HOF_NAMES]) + "\n"

if "극장적 글래머 30종 SSS" in text:
    print("⚠️  SSS 이미 존재 — 스킵")
else:
    assert SSS_MARKER in text, f"SSS 마커 없음: {SSS_MARKER}"
    text = text.replace(SSS_MARKER, SSS_LINES + "    " + SSS_MARKER, 1)
    print("✅ SSS_TIER에 30종 추가")

# 3-4. SS_TIER에 추가
SS_MARKER = "    # 2026-07-03 신규 QUAD/QUINT/HEXA/OCTET SS 전체"
SS_LINES  = "    # 2026-07-07 극장적 글래머 30종 SS\n"
SS_LINES += "\n".join([f'    "{n}",' for n in HOF_NAMES]) + "\n"

if "극장적 글래머 30종 SS" in text:
    print("⚠️  SS 이미 존재 — 스킵")
else:
    assert SS_MARKER in text, f"SS 마커 없음: {SS_MARKER}"
    text = text.replace(SS_MARKER, SS_LINES + "    " + SS_MARKER, 1)
    print("✅ SS_TIER에 30종 추가")

META.write_text(text, encoding="utf-8")
print("✅ core/presets_meta.py 저장 완료")

# ─────────────────────────────────────────────────────────
# 4. 검증
# ─────────────────────────────────────────────────────────
verify = META.read_text(encoding="utf-8")
ok = True
for n in PRESET_NAMES:
    if n not in verify:
        print(f"❌ {n} 누락")
        ok = False
    if not (PRESETS_DIR / f"{n}.json").exists():
        print(f"❌ {n}.json 없음")
        ok = False

if ok:
    total = sum(1 for _ in PRESETS_DIR.glob("*.json"))
    print(f"\n🎉 패치 완료!")
    print(f"   총 JSON: {total}개")
    print(f"   신규: {len(created)}종 (전종 HOF)")
    print(f"\n다음: git add . && git commit -m '...' && git push")
