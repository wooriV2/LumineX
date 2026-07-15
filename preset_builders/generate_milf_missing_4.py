# -*- coding: utf-8 -*-
"""누락된 MILF 4종 JSON 생성"""
import json, os

OUTPUT_DIR = "presets"

MISSING = {
"milf_korean_micro_hanbok_palace": {
    "label": "MILF 경복궁 마이크로 한복 나이트",
    "category": "milf_korean",
    "tags": ["milf","korean","hanbok","palace","night","empress"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: MILF goddess, full mature hourglass with regal bearing, 43 years old, Korean features, warm porcelain-golden skin, sophisticated updo with jade ornamental pin, mature refined smoky eye, deep rose lip, expression empress. Wearing: ultra-minimal deconstructed micro hanbok, traditional deep crimson jeogori collar reduced to extreme micro crop barely covering full mature bust, matching crimson micro chima skirt ending extreme high on full mature thighs — maximum exposure traditional fusion, crimson patent thigh-high platform stiletto boots 6-inch heel, jade drop earrings, gold daenggi ribbon reimagined as choker. Environment: Gyeongbokgung palace night, lanterns glowing warm amber, traditional architecture illuminated, palace courtyard. Lighting: palace lantern warm amber + cool night blue from sky, porcelain-golden mature skin in dual traditional light. Style: Korean MILF empress palace micro hanbok night editorial. Shot on Hasselblad X2D, 8K UHD, portrait 2:3 vertical."
},
"milf_korean_bbw_wet_pool": {
    "label": "MILF BBW 강남 루프탑 풀 웨트 골드",
    "category": "milf_korean",
    "tags": ["milf","korean","bbw","pool","wet","gold"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: MILF BBW goddess, massively full mature magnificent curves, 42 years old, Korean features, warm deep honey skin soaked in pool water, voluminous waves drenched, bold expression, bold lip. Wearing: ultra-minimal gold metallic micro string bikini soaking wet — wet fabric vacuum-tight and partially transparent on massive full mature curves, gold patent platform stiletto heeled sandals 5-inch at pool edge, gold body chain, gold hoop earrings. Environment: luxury Gangnam rooftop pool, Seoul skyline behind, afternoon golden, water dripping from full figure. Lighting: golden afternoon + turquoise pool reflection upward, deep honey skin blazing in dual light, wet gold bikini as liquid gold on massive mature curves. Style: Korean MILF BBW Gangnam rooftop pool wet gold editorial. Shot on Phase One XF IQ4, 8K UHD, portrait 2:3 vertical."
},
"milf_korean_chrome_bodysuit_cyber": {
    "label": "MILF 사이버펑크 크롬 미러 바디수트",
    "category": "milf_korean",
    "tags": ["milf","korean","cyberpunk","chrome","bodysuit","ddp"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: MILF goddess, dramatic mature hourglass sculpted, 37 years old, Korean features, warm honey skin, sleek center-part straight dark hair, fierce cyber expression, holographic eye, bold lip. Wearing: ultra-minimal chrome mirror micro bodysuit, mirror panels catching everything reflecting as living mirror on mature curves, bodysuit cut extreme high on full hips, chrome thigh-high platform stiletto boots 6-inch heel, chrome choker, chrome ear cuffs. Environment: cyberpunk Seoul DDP underground, holographic Korean ads projected, neon blue grid floor, low fog, total Seoul cyber future. Lighting: cyber neon blue-pink from all positions + grid floor reflection, honey skin in cyber color shift through chrome panels. Style: Korean MILF cyberpunk Seoul chrome mirror bodysuit editorial. Shot on Hasselblad X2D, 8K UHD, portrait 2:3 vertical."
},
"milf_korean_open_shirt_beach": {
    "label": "MILF 부산 해운대 오픈 셔츠 비치 골든아워",
    "category": "milf_korean",
    "tags": ["milf","korean","beach","busan","open_shirt","golden_hour"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: MILF goddess, full dramatic mature hourglass, 38 years old, Korean features, warm bronze-golden beach skin, long dark waves loose in sea wind, bold eye, bold red lip. Wearing: ultra-minimal white micro string bikini, white oversized button shirt fully open revealing full mature figure beneath — shirt open as only cover-up, white platform stiletto wedge sandals 5-inch heel in wet Busan sand, gold chain necklace, gold hoop earrings. Environment: Busan Haeundae beach golden hour, ocean behind, wet sand mirror at feet, golden sun at horizon. Lighting: golden hour from horizon + wet sand reflection upward, bronze-golden mature skin blazing in dual beach golden light. Style: Korean MILF Busan Haeundae open shirt beach golden hour editorial. Shot on Phase One XF IQ4, 8K UHD, portrait 2:3 vertical."
},
}

count = 0
for key, data in MISSING.items():
    filepath = os.path.join(OUTPUT_DIR, f"{key}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {key}.json")
    count += 1

print(f"\n완료: {count}종 추가 생성")
