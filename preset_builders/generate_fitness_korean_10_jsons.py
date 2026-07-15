# -*- coding: utf-8 -*-
"""
Fitness 한국인 10종 JSON 생성 스크립트
실행: $env:PYTHONUTF8 = "1"; python preset_builders/generate_fitness_korean_10_jsons.py
생성 위치: presets/*.json
"""

import json, os

OUTPUT_DIR = "presets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PRESETS = {
    "fitness_korean_tattoo_rio_carnival": {
        "label": "피트니스 타투 리우 카니발",
        "tier": "SS",
        "tags": ["korean", "fitness", "tattoo", "rio", "carnival"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess, competition physique with hip and waist tattoo — "
            "intricate mandala pattern wrapping entire hip and lower abdomen accentuating narrow waist, "
            "mid-20s, Korean features, golden-bronze skin in carnival light, wild dark waves with carnival feathers tucked in, "
            "fierce joyful expression. "
            "Wearing: ultra-minimal gold carnival micro bikini, micro thong exposing hip tattoo fully, "
            "gold platform carnival heels 6-inch, gold feather hip accessory framing tattoo, gold earrings. "
            "Environment: Rio Sambadrome carnival night, samba school float blazing all colors behind, "
            "confetti exploding, total carnival chaos. "
            "Lighting: carnival float lights rainbow saturation, golden-bronze skin blazing in carnival color, "
            "hip mandala tattoo visible in carnival light. "
            "Style: Korean fitness hip tattoo Rio carnival editorial, mandala and carnival as one. "
            "Shot on Hasselblad X2D, 8K UHD, Rio carnival fitness grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "fitness_korean_silver_hair_cliff": {
        "label": "피트니스 실버헤어 제주 절벽",
        "tier": "SS",
        "tags": ["korean", "fitness", "silver_hair", "jeju", "cliff"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess with silver-white hair — 35 years old, decade of training visible in lean mature muscle definition, "
            "Korean features, golden-honey skin in coastal wind, long silver-white hair dramatically wind-swept, fierce free expression. "
            "Wearing: ultra-minimal electric blue micro string bikini, micro thong, bare feet on Jeju volcanic cliff edge, "
            "single silver anklet, silver small hoops. "
            "Environment: Jeju Island volcanic cliff, black basalt columns below, turquoise East Sea crashing, strong ocean gale. "
            "Lighting: Jeju midday coastal + ocean reflection upward, golden-honey skin in coastal dual, "
            "silver hair catching all light as silver banner. "
            "Style: Korean fitness silver hair 35 Jeju cliff wind editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Jeju cliff fitness grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "fitness_korean_abs_neon_void": {
        "label": "피트니스 복근 네온 보이드",
        "tier": "SS",
        "tags": ["korean", "fitness", "abs", "neon", "void"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess, competition peak — 6-pack abs razor-cut, obliques visible, 24 years old, "
            "Korean features, golden-tan skin, dark hair severe ponytail, expression cold and fierce. "
            "Wearing: ultra-minimal electric pink micro string bikini, micro thong, "
            "electric pink thigh-high platform stiletto boots 6-inch, no other accessories — abs as sole accessory. "
            "Environment: dark studio, neon pink strip lights framing figure from sides creating neon outline. "
            "Lighting: neon pink strip lights bilateral + hard overhead, golden-tan skin in neon pink outline, "
            "abs catching every angle as sculptural definition in neon. "
            "Style: Korean fitness neon pink abs void editorial, abs as neon sculpture. "
            "Shot on Hasselblad X2D, 8K UHD, neon void abs grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "fitness_korean_tattoo_thigh_monaco": {
        "label": "피트니스 허벅지타투 모나코",
        "tier": "SS",
        "tags": ["korean", "fitness", "tattoo", "thigh", "monaco"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess, lean competition physique with full thigh tattoo — "
            "intricate botanical garden tattoo covering entire right thigh from hip to knee in fine-line Korean ink, "
            "late-20s, Korean features, golden Mediterranean skin, dark waves in sea breeze, sultry commanding expression. "
            "Wearing: ultra-minimal white micro string bikini, micro thong fully exposing thigh tattoo, "
            "white platform stiletto wedge mules 5-inch on Monaco yacht deck, layered gold chains, gold hoop earrings. "
            "Environment: Monaco superyacht deck, Monaco principality cliffs behind, Mediterranean deep blue water, afternoon golden Med. "
            "Lighting: Mediterranean afternoon direct + sea reflection bilateral, golden skin in Med dual light, "
            "thigh botanical tattoo fully visible in Mediterranean gold. "
            "Style: Korean fitness thigh tattoo Monaco yacht Mediterranean editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Monaco yacht fitness grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "fitness_korean_mature_40_seoul_penthouse": {
        "label": "피트니스 40세 서울 펜트하우스",
        "tier": "SS",
        "tags": ["korean", "fitness", "mature", "40", "seoul"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess, 40 years old — 20 years of training visible in mature elite physique, "
            "muscle definition with feminine curves, Korean features, warm porcelain-honey skin luminous, "
            "sleek dark hair in severe architectural updo, powerful mature expression, beauty of elite fitness at 40. "
            "Wearing: ultra-minimal black micro string bikini barely containing mature fit curves, micro thong, "
            "black patent thigh-high platform stiletto boots 6-inch on penthouse terrace, "
            "silver chain body harness, silver geometric ear cuffs. "
            "Environment: Seoul luxury penthouse, Han River blazing gold below, Namsan Tower, glass railing, full night panorama. "
            "Lighting: Seoul city gold ambient + hard key front, porcelain skin in warm gold, "
            "mature muscle definition visible in city light. "
            "Style: Korean fitness 40 mature elite Seoul penthouse night editorial, 40-year peak physique commanding Seoul skyline. "
            "Shot on Hasselblad X2D, 8K UHD, Seoul mature fitness grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "fitness_korean_glutes_ibiza_sunset": {
        "label": "피트니스 글루트 이비자 선셋",
        "tier": "SS",
        "tags": ["korean", "fitness", "glutes", "ibiza", "sunset"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess, glute-specialist physique — extraordinary rounded full glutes with extremely narrow waist "
            "creating dramatic silhouette, lean everywhere else, mid-20s, Korean features, deep bronze-tan skin in Ibiza sunset, "
            "long dark wavy hair in ocean breeze, fierce sultry expression. "
            "Wearing: ultra-minimal neon yellow micro string bikini, micro thong maximally exposing legendary glutes, "
            "clear platform stiletto wedge 5-inch on Ibiza cliff, gold chain hip belt, small gold hoops. "
            "Environment: Ibiza coastal cliff at sunset, Balearic Sea blazing in orange-gold below, white limestone formations. "
            "Lighting: Ibiza setting sun from horizon + sea reflection, bronze-tan skin in warm Ibiza gold, "
            "glutes catching sunset from all angles in legendary definition. "
            "Style: Korean fitness glutes Ibiza sunset cliff editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Ibiza sunset fitness grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "fitness_korean_tattoo_sleeve_aurora": {
        "label": "피트니스 슬리브타투 오로라",
        "tier": "SSS",
        "tags": ["korean", "fitness", "tattoo", "sleeve", "aurora"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess, competition physique with full color sleeve tattoo on left arm — "
            "vibrant traditional Korean haenyeo and sea creatures in vivid color covering shoulder to wrist, "
            "mid-20s, Korean features, porcelain skin cold in aurora light, dark hair wild in arctic wind, awe-struck fierce expression. "
            "Wearing: ultra-minimal silver chrome micro string bikini, micro thong, "
            "silver chrome thigh-high platform stiletto boots 6-inch on Iceland snow, silver fur wrap draped shoulders only. "
            "Environment: Iceland wilderness, massive aurora borealis in green-purple-blue filling sky, snow field, frozen lake reflection. "
            "Lighting: aurora green-purple-blue from sky + snow reflection, porcelain skin in aurora color wash, "
            "haenyeo tattoo catching aurora as color-charged ink in arctic light. "
            "Style: Korean fitness haenyeo color tattoo Iceland aurora editorial. "
            "Shot on Hasselblad X2D, 8K UHD, aurora tattoo fitness grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "fitness_korean_abs_seychelles_granite": {
        "label": "피트니스 복근글루트 세이셸",
        "tier": "SS",
        "tags": ["korean", "fitness", "abs", "seychelles", "granite"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess, dual weapon physique — razor 6-pack abs AND legendary full rounded glutes, "
            "the complete package, late-20s, Korean features, warm honey-bronze skin oiled in Seychelles sun, "
            "natural afro-wavy hair wild in ocean wind, fierce free expression. "
            "Wearing: ultra-minimal turquoise micro string bikini, micro thong maximum glute exposure, "
            "bare feet on smooth Seychelles pink granite, bronze arm cuff. "
            "Environment: Anse Source d'Argent Seychelles, massive smooth pink granite boulders towering, "
            "turquoise Indian Ocean between granite gaps, palm fronds. "
            "Lighting: Seychelles golden afternoon + turquoise ocean reflection between granite, "
            "honey-bronze oiled skin dual light, abs and glutes visible from every angle on pink granite. "
            "Style: Korean fitness abs+glutes Seychelles granite editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Seychelles fitness grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "fitness_korean_cyber_muscle_ddp": {
        "label": "피트니스 사이버 DDP 서울",
        "tier": "SS",
        "tags": ["korean", "fitness", "cyber", "ddp", "seoul"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess, defined athletic muscle with cyberpunk aesthetic — visible abs and deltoids, "
            "26 years old, Korean features, porcelain-honey skin, silver-dyed undercut fade hair fierce, "
            "graphic neon liner makeup, fierce cyber expression. "
            "Wearing: ultra-minimal chrome structured micro bodysuit cut to expose abs — armor-panel construction barely covering lean physique, "
            "chrome thigh-high platform stiletto boots 6-inch on DDP curved surface, "
            "neon blue geometric ear cuffs, chrome arm sleeve one side. "
            "Environment: Dongdaemun Design Plaza Seoul exterior night, DDP massive curved white aluminum surface behind, "
            "LED neon Seoul signs, Korean script neon. "
            "Lighting: DDP LED white from curved surface + neon blue-pink from Seoul signs, "
            "porcelain-honey skin in neon wash, chrome bodysuit catching DDP white as mirror. "
            "Style: Korean fitness cyber muscle DDP Seoul night editorial. "
            "Shot on Hasselblad X2D, 8K UHD, cyber Seoul fitness grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "fitness_korean_tattoo_full_maldives_void": {
        "label": "피트니스 풀타투 몰디브 나이트",
        "tier": "SSS",
        "tags": ["korean", "fitness", "tattoo", "full", "maldives"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean fitness goddess, competition physique as living canvas — full body tattoo, both arms, torso sides, thighs "
            "covered in flowing traditional Korean nature motifs: cranes, chrysanthemums, waves, mountains in fine-line black ink "
            "covering 60% of body surface, mid-20s, Korean features, golden-bronze skin between tattoo ink, "
            "long dark hair with flower tucked, sultry commanding expression. "
            "Wearing: ultra-minimal white micro string bikini — white maximum contrast against tattoo canvas, micro thong, "
            "white platform stiletto wedge 5-inch on overwater bungalow deck, no other accessories — tattoos are all jewelry. "
            "Environment: Maldives overwater bungalow at night, stars reflecting in dark Indian Ocean below, "
            "warm lantern light, infinity water horizon total. "
            "Lighting: warm lantern amber from bungalow + star reflection cool from dark water below, "
            "golden-bronze skin in warm-cool dual, tattoo motifs catching lantern as warm ink on dark night. "
            "Style: Korean fitness full body tattoo Maldives night editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Maldives night tattoo grade, portrait 2:3 vertical."
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

print(f"\n✅ fitness 한국인 10종 JSON 생성 완료: {count}개 신규 생성")
