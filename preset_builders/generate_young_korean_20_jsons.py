# -*- coding: utf-8 -*-
"""
Young Adult 한국인 20종 JSON 생성 스크립트
실행: $env:PYTHONUTF8 = "1"; python preset_builders/generate_young_korean_20_jsons.py
"""

import json, os

OUTPUT_DIR = "presets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PRESETS = {
    "young_korean_jeju_sunrise": {
        "label": "영어덜트 제주 일출",
        "tier": "SS",
        "tags": ["korean","young","jeju","sunrise"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, "
            "natural dewy porcelain skin in sunrise warmth, long straight dark hair loose in morning breeze, "
            "pure natural minimal makeup, expression pure joy and wonder at sunrise. "
            "Wearing: ultra-minimal white micro string bikini, bare feet on Jeju volcanic rock at Seongsan Ilchulbong, "
            "single delicate gold anklet, tiny gold stud earrings. "
            "Environment: Seongsan Ilchulbong at sunrise, dramatic volcanic crater, sun rising from East Sea horizon blazing orange-pink-gold, "
            "turquoise sea far below, morning mist. "
            "Lighting: Jeju sunrise from horizon blazing + sea reflection pink below, dewy 20-year porcelain skin in pure sunrise. "
            "Style: Korean young adult 20 Jeju Seongsan sunrise pure editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Jeju sunrise young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_studio_black_minimal": {
        "label": "영어덜트 블랙 스튜디오",
        "tier": "SS",
        "tags": ["korean","young","studio","minimal"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old, slim perfect figure with subtle curves just emerging, "
            "Korean features, luminous porcelain skin, long straight jet-black hair sleek center-part, sharp eyes, bold red lip on young face, fierce debut expression. "
            "Wearing: ultra-minimal black micro string bikini, black patent thigh-high platform stiletto boots 6-inch, single silver geometric ear cuff only. "
            "Environment: black infinity studio, single hard overhead spot, pure editorial void. "
            "Lighting: single hard overhead spot, luminous porcelain young skin in hard chiaroscuro. "
            "Style: Korean young adult 21 debut studio editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, debut studio grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_pool_pastel": {
        "label": "영어덜트 파스텔 풀",
        "tier": "S",
        "tags": ["korean","young","pool","pastel"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, "
            "natural golden-porcelain skin in pool light, long dark hair wet and sleek from pool, natural fresh makeup, playful joyful expression. "
            "Wearing: ultra-minimal pastel pink micro string bikini, micro thong, clear platform stiletto wedge mules 4-inch at pool edge, "
            "delicate gold chain, tiny heart stud earrings. "
            "Environment: luxury resort pool, pastel blue water, pink and white poolside furniture, tropical flowers, afternoon golden light. "
            "Lighting: afternoon sun direct + pastel blue pool reflection below, golden-porcelain 20-year skin in dual. "
            "Style: Korean young adult 20 pastel pool summer editorial. "
            "Shot on Hasselblad X2D, 8K UHD, pastel pool young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_cherry_blossom": {
        "label": "영어덜트 벚꽃",
        "tier": "SS",
        "tags": ["korean","young","cherry","blossom"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, slim perfect figure, Korean features, "
            "natural luminous porcelain skin in cherry blossom light, long dark wavy hair with petals caught in it, "
            "pure natural no-makeup makeup, expression pure innocent spring joy. "
            "Wearing: ultra-minimal blush pink micro slip dress, spaghetti straps, dress floating on slim young figure, "
            "white platform sandal mules 4-inch, cherry blossom branch in hair, tiny pearl studs. "
            "Environment: Korean cherry blossom park at peak bloom, pink blossom canopy above, petals falling like snow. "
            "Lighting: cherry blossom pink diffused from canopy — total pink floral diffusion, blush skin in pink blossom light. "
            "Style: Korean young adult 20 cherry blossom pure editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, cherry blossom young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_neon_first_night": {
        "label": "영어덜트 홍대 네온",
        "tier": "SS",
        "tags": ["korean","young","hongdae","neon"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, "
            "warm honey-porcelain skin in Hongdae neon, long straight dark hair with neon-dyed pink tips, sharp liner, glossy pink lip, excited fierce young expression. "
            "Wearing: ultra-minimal neon pink micro string bikini, micro thong, clear holographic thigh-high platform stiletto boots 5-inch on Hongdae street, "
            "neon pink mini crossbody bag, silver small hoops. "
            "Environment: Hongdae at midnight, indie club street, neon and LED art, street art murals, young crowd blur, puddles reflecting neon. "
            "Lighting: Hongdae neon pink-purple + puddle reflection below, honey-porcelain 21-year skin in neon wash. "
            "Style: Korean young adult 21 Hongdae first night editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Hongdae neon young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_maldives_first_trip": {
        "label": "영어덜트 몰디브 첫 여행",
        "tier": "SS",
        "tags": ["korean","young","maldives","first"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, "
            "warm golden-porcelain skin glowing in Maldives sun — first real tan of young life, long straight dark hair in ocean breeze, "
            "smile wide and genuine, expression of pure 20-year joy at paradise. "
            "Wearing: ultra-minimal sky blue micro string bikini, micro thong, bare feet on overwater bungalow deck, single gold anklet, tiny gold studs. "
            "Environment: Maldives overwater bungalow, turquoise Indian Ocean surrounding, coral visible through crystal water, blue sky and sea. "
            "Lighting: Maldives midday direct from above + turquoise ocean reflection upward, golden-porcelain young skin in tropical dual, first-tan golden warmth. "
            "Style: Korean young adult 20 Maldives first trip editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Maldives young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_tokyo_first_solo": {
        "label": "영어덜트 도쿄 하라주쿠",
        "tier": "S",
        "tags": ["korean","young","tokyo","harajuku"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, luminous porcelain skin, "
            "long dark hair with colorful hair clip accessories — Harajuku youth aesthetic, expression excited and fierce first-adult solo travel. "
            "Wearing: ultra-minimal white micro string bikini, micro thong, white platform sneaker boots 5-inch on Harajuku street, "
            "colorful micro shoulder bag, stacked bracelets on both wrists, tiny star earrings. "
            "Environment: Harajuku Takeshita Street, colorful fashion shops, youth crowd, crepe shops, full Japanese youth culture. "
            "Lighting: Harajuku afternoon dappled through street + colorful shop sign ambient, porcelain 21-year skin in Harajuku color wash. "
            "Style: Korean young adult 21 Tokyo Harajuku first solo editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Harajuku young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_paris_first_europe": {
        "label": "영어덜트 파리 에펠탑",
        "tier": "SSS",
        "tags": ["korean","young","paris","eiffel"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, "
            "luminous porcelain skin in Paris morning light, long dark waves loose in morning Paris air, "
            "expression of pure wonder and joy — first time in Europe at 20. "
            "Wearing: ultra-minimal cream micro slip dress, thin straps, dress barely covering slim young figure, "
            "cream platform stiletto mules 4-inch on Paris stone path, small pearl studs, delicate gold necklace, tiny Paris map print micro crossbody. "
            "Environment: Champ de Mars Paris, Eiffel Tower directly behind at golden morning, Parisian couples in background, French morning golden light. "
            "Lighting: Paris morning golden from side, porcelain 20-year skin in Paris golden warmth, cream dress in Paris gold total palette. "
            "Style: Korean young adult 20 Paris Eiffel first Europe editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Paris young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_tattoo_first_wrist": {
        "label": "영어덜트 손목타투 서울카페",
        "tier": "SS",
        "tags": ["korean","young","tattoo","wrist"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, warm honey-porcelain skin, "
            "long dark hair loose and free, natural fresh makeup, expression confident and proud — just got her first tattoo. "
            "First tattoo: delicate fine-line moon and stars on right wrist, small but meaningful. "
            "Wearing: ultra-minimal beige micro string bikini, micro thong, beige platform sandal mules 4-inch on Seoul café street, "
            "wrist tattoo prominently displayed, tiny gold studs, delicate gold necklace. "
            "Environment: Seoul Bukchon or Insadong café street, hanok wall behind, autumn leaves, warm café amber glow. "
            "Lighting: Seoul café street warm afternoon + café amber, honey-porcelain 21-year skin in warm glow, wrist tattoo visible in detail. "
            "Style: Korean young adult 21 first wrist tattoo Seoul café editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Seoul café young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_bali_first_solo": {
        "label": "영어덜트 발리 첫 배낭",
        "tier": "SS",
        "tags": ["korean","young","bali","sunset"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, slim perfect figure, Korean features, "
            "warm honey skin golden from first week in Bali sun, long dark hair with flower tucked in from Bali morning market, "
            "expression of pure free-spirited 20-year happiness. "
            "Wearing: ultra-minimal gold micro string bikini, micro thong, bare feet on Bali beach sand, handmade Bali woven anklet, small lotus stud earrings. "
            "Environment: Bali beach at sunset, temple silhouette on cliff in background, golden sand, palm trees, Bali sunset orange-pink sky. "
            "Lighting: Bali golden sunset from horizon, honey-golden young skin in warm Bali gold — first real tan glowing. "
            "Style: Korean young adult 20 Bali first solo trip golden editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Bali young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_gym_first_gains": {
        "label": "영어덜트 홈짐 첫 근육",
        "tier": "S",
        "tags": ["korean","young","gym","gains"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old, figure beginning to show first real gym results — "
            "slim with just-emerging ab definition and slight muscle tone, the fresh beginning of a fitness journey, "
            "Korean features, warm honey-porcelain skin, dark hair in gym ponytail, expression proud and confident — first gains. "
            "Wearing: ultra-minimal black micro sports bikini — athletic micro top and micro thong, black chrome platform stiletto boots 6-inch on gym floor, single silver arm band. "
            "Environment: home gym with full-length mirror, dumbbells visible, motivational vibe, natural afternoon light through window. "
            "Lighting: natural afternoon from window + mirror reflection, honey-porcelain 21-year skin in natural light, first ab definition visible. "
            "Style: Korean young adult 21 first gym gains mirror editorial. "
            "Shot on Hasselblad X2D, 8K UHD, gym young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_summer_busan": {
        "label": "영어덜트 부산 해운대",
        "tier": "SS",
        "tags": ["korean","young","busan","summer"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, "
            "warm golden-tan skin from Busan summer beach, long dark hair wild in sea breeze, smile wide and radiant — summer vacation with friends. "
            "Wearing: ultra-minimal bright yellow micro string bikini, micro thong, bare feet in Haeundae sand, yellow anklet, tiny gold hoop earrings. "
            "Environment: Haeundae Beach Busan, crowd of summer beachgoers blurred behind, turquoise East Sea waves, Gwangan Bridge visible in distance. "
            "Lighting: Busan midday direct from above + sea reflection, golden-tan 20-year skin in summer dual, yellow bikini against blue sea. "
            "Style: Korean young adult 20 Busan Haeundae summer editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Busan summer young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_tattoo_ankle_jeju": {
        "label": "영어덜트 발목타투 제주",
        "tier": "SS",
        "tags": ["korean","young","tattoo","ankle"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, "
            "warm golden porcelain skin kissed by Jeju sun, long dark hair in ocean wind, expression free and joyful, "
            "delicate ankle tattoo — tiny wave pattern wrapping right ankle. "
            "Wearing: ultra-minimal white micro string bikini, bare feet on Jeju black volcanic rock — ankle tattoo prominently visible, "
            "single gold chain on tattooed ankle, tiny gold hoops. "
            "Environment: Jeju Island volcanic coastline, black basalt columns, turquoise East Sea crashing below. "
            "Lighting: Jeju midday coastal + ocean reflection upward, golden-porcelain 21-year skin in coastal dual, ankle wave tattoo visible in full detail. "
            "Style: Korean young adult 21 ankle tattoo Jeju volcanic coast editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Jeju ankle tattoo young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_midnight_rooftop_seoul": {
        "label": "영어덜트 서울 새벽 루프탑",
        "tier": "SSS",
        "tags": ["korean","young","seoul","midnight"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, "
            "warm porcelain skin in Seoul night air, long dark hair slightly wild from dancing, makeup slightly smudged and perfect — "
            "21-year-old after first real night out, expression fierce and alive and free. "
            "Wearing: ultra-minimal black micro string bikini, black patent thigh-high platform stiletto boots 6-inch on Seoul rooftop, "
            "black leather micro crossbody, silver small hoop earrings. "
            "Environment: Seoul rooftop at 3AM, Han River glowing below, Seoul skyline blazing gold, Namsan Tower behind, dawn just starting to hint on horizon. "
            "Lighting: Seoul city gold ambient from panorama + hint of pre-dawn blue on horizon, porcelain 21-year skin in warm-cool contrast. "
            "Style: Korean young adult 21 first Seoul midnight rooftop editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Seoul midnight young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_nyc_first_american": {
        "label": "영어덜트 NYC 타임스퀘어",
        "tier": "SSS",
        "tags": ["korean","young","nyc","times_square"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, slim perfect youthful figure, Korean features, "
            "luminous porcelain skin in NYC neon, long dark hair in NYC wind, expression overwhelmed and fierce and alive — first time in New York at 20. "
            "Wearing: ultra-minimal white micro string bikini — pure white against NYC neon chaos, white platform stiletto boots 5-inch in Times Square, "
            "tiny American flag pin, silver small studs. "
            "Environment: Times Square full neon explosion, massive LED billboards in all directions, yellow taxis, NYC crowd energy. "
            "Lighting: Times Square full LED neon from all billboard directions, porcelain 20-year skin in neon color saturation, "
            "white bikini catching every Times Square LED as white prism. "
            "Style: Korean young adult 20 NYC Times Square first America editorial. "
            "Shot on Hasselblad X2D, 8K UHD, NYC young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_campus_spring": {
        "label": "영어덜트 캠퍼스 봄",
        "tier": "S",
        "tags": ["korean","young","campus","spring"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, first year of university — slim perfect figure, fresh and bright, Korean features, "
            "natural luminous porcelain skin in spring campus light, long dark waves with cute clips, expression bright and youthful. "
            "Wearing: ultra-minimal white micro string bikini, white mini platform sneakers 4-inch on campus path, small campus tote bag, "
            "stacked friendship bracelets, tiny star studs. "
            "Environment: Korean university campus in spring, cherry blossom trees along campus path, students in background, university building, spring afternoon gold. "
            "Lighting: spring afternoon golden dappled through cherry blossoms, porcelain 20-year skin in spring cherry gold. "
            "Style: Korean young adult 20 university campus spring first year editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, campus spring young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_tattoo_shoulder_okinawa": {
        "label": "영어덜트 어깨타투 오키나와",
        "tier": "SS",
        "tags": ["korean","young","tattoo","shoulder"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old, slim perfect figure, Korean features, "
            "warm golden skin from Okinawa sun, long dark hair in tropical breeze, expression fierce and proud — shoulder tattoo just healed. "
            "Shoulder tattoo: delicate fine-line crane on left shoulder blade, small but perfectly placed. "
            "Wearing: ultra-minimal turquoise micro string bikini — micro top revealing shoulder tattoo, micro thong, bare feet in white Okinawa sand, simple gold anklet. "
            "Environment: Okinawa Emerald Beach, turquoise sea, white sand, tropical paradise Japan. "
            "Lighting: Okinawa midday direct + turquoise sea reflection, golden 21-year skin in tropical dual, shoulder crane tattoo visible in full detail. "
            "Style: Korean young adult 21 shoulder crane tattoo Okinawa editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Okinawa young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_debut_red_carpet": {
        "label": "영어덜트 레드카펫 데뷔",
        "tier": "SSS",
        "tags": ["korean","young","debut","red_carpet"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old, slim perfect figure on red carpet debut — the moment before everything changes, "
            "Korean features, luminous porcelain skin under red carpet flash, long dark hair in perfect waves, bold red lip, fierce debut expression. "
            "Wearing: ultra-minimal silver crystal micro gown — crystal micro dress barely covering debut figure, "
            "silver platform stiletto heels 6-inch on red carpet, crystal drop earrings, crystal body chain. "
            "Environment: awards show red carpet, camera flash from all directions, press photographers, red carpet velvet, backdrop signage blurred. "
            "Lighting: camera flash multi-directional explosion + overhead red carpet spots, porcelain 21-year skin in flash constellation, "
            "crystal gown catching every flash as diamond explosion. "
            "Style: Korean young adult 21 debut red carpet crystal editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, red carpet debut young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_first_snowfall_seoul": {
        "label": "영어덜트 서울 첫눈",
        "tier": "SS",
        "tags": ["korean","young","seoul","snow"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 20 years old, slim perfect figure, Korean features, "
            "luminous porcelain skin in Seoul first snow, long dark hair with snowflakes caught in it, expression of pure childlike wonder — first snow of the year at 20. "
            "Wearing: ultra-minimal white micro string bikini — pure white matching snowflakes, white platform stiletto boots 5-inch in Seoul snow, "
            "white fluffy ear muffs only, snowflakes on skin. "
            "Environment: Seoul street in first winter snow, Gyeongbok Palace gate visible through snowfall, traditional lanterns lit warm amber through snow, snow falling. "
            "Lighting: Seoul overcast snow-diffused cold white + palace lantern warm amber, porcelain 20-year skin in cold-warm contrast, snowflakes catching on skin and hair. "
            "Style: Korean young adult 20 Seoul first snow palace editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Seoul snow young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "young_korean_21_birthday_gold": {
        "label": "영어덜트 21세 생일 골드",
        "tier": "SSS",
        "tags": ["korean","young","birthday","gold"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean young adult goddess, 21 years old — her birthday, the moment of adulthood, slim perfect figure, Korean features, "
            "luminous golden-porcelain skin under party lights, long dark hair in perfect waves, bold coral lip, expression of fierce joy and ownership of her 21 — this is her night. "
            "Wearing: ultra-minimal gold sequin micro string bikini barely containing emerging 21-year curves, micro thong, "
            "gold chrome thigh-high platform stiletto boots 6-inch, gold chain belt, '21' tiny diamond pendant necklace, gold ear cuffs. "
            "Environment: luxury Seoul rooftop party, balloon installation in gold and white, Han River panorama below, confetti in air, friends blurred celebrating behind. "
            "Lighting: party golden warm from balloon lights above + Han River city ambient below + confetti catching light, "
            "golden-porcelain 21-year skin blazing in birthday gold. "
            "Style: Korean young adult 21 birthday party gold commanding editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, birthday gold young grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
}

count = 0
for key, data in PRESETS.items():
    path = os.path.join(OUTPUT_DIR, f"{key}.json")
    if os.path.exists(path):
        print(f"[SKIP] 이미 존재: {path}")
        continue
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[OK] {path}")
    count += 1

print(f"\n✅ Young Adult 한국인 20종 JSON 생성 완료: {count}개 신규 생성")
