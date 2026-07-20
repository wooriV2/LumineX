# -*- coding: utf-8 -*-
"""
Silver Fox TRIO 13종 + DUO SF-31 누락분 패치 스크립트
- presets/*.json 생성
- presets_meta.py 🎭 Trio Glamour 카테고리에 키 추가
- hof_tier.py HOF 추가
- sss_tier.py SSS 추가 (} 앞)
"""
import json, os, ast

PRESETS_DIR = "presets"
os.makedirs(PRESETS_DIR, exist_ok=True)

PRESETS = {
    # DUO SF-31 누락분
    "korean_silverfox_duo_irezumi_crimson_jeonju": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, luminous porcelain skin with elegant silver-era maturity, silver updo — body fully covered in Japanese irezumi skull and chrysanthemum tattoo from neck to ankle, full body coverage from neck to ankle, bold black skull with cascading crimson chrysanthemums blazing across massive BBW ageless figure. RIGHT: Latina silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in crimson ultra-fine glitter coating every inch from neck to ankle, liquid fire sculpture effect. LEFT: black ankle strap heels, extra long coffin black nails. RIGHT: crimson stiletto heels, extra long stiletto crimson nails. Both: full body high-gloss oil. Environment: Jeonju Hanok Village moonlit alley at night, traditional tile roofs, stone lanterns glowing amber, persimmon trees, paper lanterns casting warm light. Lighting: warm lantern amber with cool moonlight — skull chrysanthemum catching warm amber left, crimson glitter blazing fire right. Style: Jeonju silver fox moonlit duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Jeonju silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Jeonju Hanok Village moonlit alley at night, persimmon trees",
        "lighting": "warm lantern amber with cool moonlight",
        "style": "Jeonju silver fox moonlit duo editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    # TRIO SF-01~03 (이전 검증 완료)
    "korean_silverfox_trio_dragon_celadon_crimson_void": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean silver fox bust queen, 50s, silver fox glamour physique — ageless bombshell mature curves, impossibly large full heavy bust dramatically dominating silhouette, extremely narrow distinguished waist, luminous porcelain skin with elegant silver-era maturity, silver updo — body fully covered in Korean azure dragon irezumi tattoo from neck to ankle, full body coverage from neck to ankle, sacred blue-black dragon coiling ageless distinguished body with divine clouds and silver pearls. CENTER: African silver fox powerhouse, 50s, silver fox glamour physique — ageless bombshell mature curves, shredded defined abs combined with extremely wide round commanding hips, thick muscular distinguished thighs, oiled glistening deep skin with elegant silver-era maturity, natural silver afro crown — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon glaze with inlaid crane and cloud motifs coating ageless distinguished figure. RIGHT: Mediterranean silver fox glamour, 50s, silver fox glamour physique — ageless bombshell mature curves, dramatically cinched narrow waist, very wide commanding hips, full bust, warm olive skin with elegant silver-era maturity, silver-streaked waves — body fully covered in crimson-gold ultra-fine glitter coating every inch from neck to ankle, blazing liquid fire effect. LEFT: deep blue stiletto heels, long blue nails. CENTER: jade stiletto heels, long jade nails. RIGHT: crimson stiletto heels, long gold nails. All: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic triple chiaroscuro — dragon azure catching cold spotlight left, celadon jade gleaming center, crimson glitter blazing fire right. Style: Vogue Italia Korean silver fox void trio editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Korean silver fox void trio grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic triple chiaroscuro void",
        "style": "Vogue Italia Korean silver fox void trio editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_trio_minhwa_haetae_gold_bukchon": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: BBW silver fox glamour, 50s, silver fox glamour physique — ageless bombshell mature curves, dramatic full-figure distinguished silhouette, extremely wide heavy commanding hips, maximalist abundant ageless curves, warm caramel skin with elegant silver-era maturity, silver-streaked natural hair — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across ageless abundant figure. CENTER: Korean silver fox pinup, 50s, silver fox glamour physique — ageless bombshell mature curves, supremely elegant distinguished hourglass, wide commanding hips, full bust, luminous porcelain skin with elegant silver-era maturity, silver-streaked chignon — body fully covered in Korean Haetae guardian lion bodypaint from neck to ankle, mythological fire-eating beast in bold Korean traditional style covering ageless distinguished figure. RIGHT: Polynesian silver fox goddess, 50s, silver fox glamour physique — ageless bombshell mature curves, full heavy rounded commanding hips and thighs, broad powerful shoulders, dramatically wide lower body, warm bronzed glowing skin with elegant silver-era maturity, silver-streaked waves — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: gold stiletto heels, long black nails. CENTER: crimson stiletto heels, long gold nails. RIGHT: gold stiletto heels, long gold nails. All: full body high-gloss oil. Environment: Bukchon Hanok Village rooftop at night, traditional tiled roofs below, Seoul city lights glittering in distance, full moon blazing above. Lighting: cool moonlight with Seoul city neon. Style: Bukchon silver fox luxury trio editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Bukchon silver fox trio grade, portrait 3:4 vertical.",
        "environment": "Bukchon Hanok Village rooftop at night, full moon",
        "lighting": "cool moonlight with Seoul city neon",
        "style": "Bukchon silver fox luxury trio editorial",
        "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_trio_irezumi_dancheong_violet_namsan": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Mixed silver fox beauty, 50s, silver fox glamour physique — ageless bombshell mature curves, toned defined distinguished body with round full commanding hips, thick mature powerful thighs, glowing healthy skin with elegant silver-era maturity, silver-streaked locs — body fully covered in Japanese irezumi tiger and lotus tattoo from neck to ankle, full body coverage from neck to ankle, bold black and gold tiger prowling ageless distinguished figure with crimson lotus blooms. CENTER: Indian silver fox goddess, 50s, silver fox glamour physique — ageless bombshell mature curves, dramatic distinguished waist-to-hip ratio, full rounded bust and very wide commanding hips, warm glistening bronze skin with elegant silver-era maturity, silver-streaked updo — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across ageless dramatic curves. RIGHT: European silver fox bombshell, 50s, silver fox glamour physique — ageless bombshell mature curves, maximum pinup distinguished hourglass silhouette, impossibly tiny corseted waist, extremely wide round commanding hips, lush full bust, luminous fair skin with elegant silver-era maturity, platinum silver bob — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold stiletto heels, long black nails. CENTER: crimson stiletto heels, long red nails. RIGHT: violet stiletto heels, long silver nails. All: full body high-gloss oil. Environment: Seoul city tower rooftop at night, panoramic Seoul metropolis blazing below, Han River glittering silver in distance. Lighting: Seoul neon urban glow — irezumi tiger catching city amber left, dancheong sacred colors blazing center, violet glitter exploding amethyst right. Style: Seoul tower silver fox trio editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Seoul tower silver fox trio grade, portrait 3:4 vertical.",
        "environment": "Seoul city tower rooftop at night, Han River panorama",
        "lighting": "Seoul neon urban glow triple",
        "style": "Seoul tower silver fox trio editorial",
        "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, portrait 3:4 vertical"
    },
    # TRIO SF-04
    "korean_silverfox_trio_dancheong_crimson_void": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, luminous porcelain skin with elegant silver-era maturity, silver chignon — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across hourglass ageless curves. CENTER: Black silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, deep luminous ebony skin with elegant silver-era maturity, silver locs crown — body fully covered in crimson ultra-fine glitter coating every inch from neck to ankle, liquid fire sculpture effect. RIGHT: Nordic silver fox amazon, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long powerful legs, pale luminous arctic skin with elegant silver-era maturity, platinum silver bob — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, matte-and-shine void contrast maximum. LEFT: gold stiletto heels, extra long almond crimson nails. CENTER: crimson platform stiletto heels, extra long coffin crimson nails. RIGHT: matte black thigh-high boots, extra long stiletto black nails. All: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic triple chiaroscuro — dancheong vivid sacred colors blazing warm left, crimson glitter exploding fire center, obsidian glitter dissolving into void right — Silver Fox void fire dark trinity. Style: Vogue Italia silver fox void fire trio editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, silver fox void fire trio grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic triple chiaroscuro void fire dark",
        "style": "Vogue Italia silver fox void fire trio editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    # TRIO SF-05
    "korean_silverfox_trio_minhwa_teal_aurora": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Latina silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across bubble butt ageless curves. CENTER: Korean silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, luminous porcelain skin with elegant silver-era maturity, silver chignon — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. RIGHT: African silver fox bust queen, 50s, bust queen physique — impossibly large full heavy bust dramatically dominating silhouette, extremely narrow waist, deep luminous ebony skin with elegant silver-era maturity, silver natural afro — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold stiletto heels, extra long almond coral nails. CENTER: teal stiletto heels, extra long stiletto teal nails. RIGHT: violet platform stiletto heels, extra long coffin violet nails. All: full body high-gloss oil. Environment: Iceland glacier field at night, Aurora Borealis exploding across vast dark sky in electric green and violet curtains, glacial blue ice underfoot. Lighting: aurora borealis glow — Minhwa folk colors catching aurora warmth left, teal glitter shifting center, violet glitter exploding crystalline right. Style: Aurora silver fox trio editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora silver fox trio grade, portrait 3:4 vertical.",
        "environment": "Iceland glacier field at night, Aurora Borealis green violet",
        "lighting": "aurora borealis glow triple",
        "style": "Aurora silver fox trio editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    # TRIO SF-07
    "korean_silverfox_trio_irezumi_celadon_violet_void": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Indian silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, warm bronze skin with elegant silver-era maturity, silver-streaked updo — body fully covered in Japanese irezumi tiger and lotus tattoo from neck to ankle, full body coverage from neck to ankle, bold black and gold tiger prowling ageless BBW figure with crimson lotus blooms filling every gap. CENTER: Mediterranean silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, warm olive skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon glaze with inlaid crane and cloud motifs coating bubble butt ageless figure. RIGHT: Polynesian silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, warm bronzed Polynesian skin with elegant silver-era maturity, silver-streaked waves — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold thigh-high boots, extra long coffin black nails. CENTER: jade stiletto heels, extra long almond jade nails. RIGHT: violet platform stiletto heels, extra long stiletto violet nails. All: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic triple chiaroscuro — irezumi tiger warm spotlight left, celadon jade gleaming center, violet glitter exploding crystalline right. Style: Vogue Italia silver fox void trio editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, silver fox void trio grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic triple chiaroscuro void trinity",
        "style": "Vogue Italia silver fox void trio editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    # TRIO SF-08
    "korean_silverfox_trio_haetae_minhwa_emerald_bukchon": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean silver fox amazon, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long powerful legs, luminous porcelain skin with elegant silver-era maturity, silver-streaked chignon — body fully covered in Korean Haetae guardian lion bodypaint from neck to ankle, mythological fire-eating beast in bold Korean traditional style blazing across amazon ageless curves. CENTER: African silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, deep luminous ebony skin with elegant silver-era maturity, silver locs — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across pinup ageless curves. RIGHT: Caribbean silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, deeply bronzed Caribbean skin with elegant silver-era maturity, silver-streaked curls — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: crimson stiletto heels, extra long almond black nails. CENTER: gold stiletto heels, extra long coffin coral nails. RIGHT: emerald platform stiletto heels, extra long stiletto emerald nails. All: full body high-gloss oil. Environment: Bukchon Hanok Village rooftop at night, traditional tiled roofs below, Seoul city lights glittering in distance, full moon blazing above. Lighting: cool moonlight with Seoul city neon — Haetae guardian catching amber left, Minhwa folk colors catching moonlight center, emerald glitter absorbing city light right. Style: Bukchon silver fox trio editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Bukchon silver fox trio grade, portrait 3:4 vertical.",
        "environment": "Bukchon Hanok Village rooftop at night, Seoul skyline",
        "lighting": "cool moonlight with Seoul city neon triple",
        "style": "Bukchon silver fox trio editorial",
        "quality": "Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, portrait 3:4 vertical"
    },
    # TRIO SF-09
    "korean_silverfox_trio_dragon_phoenix_obsidian_void": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Nordic silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, pale luminous arctic skin with elegant silver-era maturity, platinum silver updo — body fully covered in Japanese irezumi dragon and cloud tattoo from neck to ankle, full body coverage from neck to ankle, sacred blue-black dragon coiling ageless BBW figure with silver clouds filling every gap. CENTER: Latina silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in crimson-gold phoenix bodypaint from neck to ankle, sacred phoenix rising full body in brilliant crimson and gold blazing across hourglass ageless curves. RIGHT: Korean silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, luminous porcelain skin with elegant silver-era maturity, silver chignon — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, matte-and-shine void contrast maximum. LEFT: navy thigh-high boots, extra long coffin blue nails. CENTER: crimson stiletto heels, extra long stiletto gold nails. RIGHT: matte black platform stiletto heels, extra long almond obsidian nails. All: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic triple chiaroscuro — dragon azure cold left, phoenix crimson-gold blazing center, obsidian void darkness right. Style: Vogue Italia silver fox void elemental trio editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver fox void elemental trio grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic triple chiaroscuro elemental void",
        "style": "Vogue Italia silver fox void elemental trio editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    # TRIO SF-10
    "korean_silverfox_trio_dancheong_irezumi_gold_jongmyo": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Black silver fox athletic, 50s, athletic vixen physique — shredded defined abs, wide round commanding hips, thick muscular mature thighs, deep luminous ebony skin with elegant silver-era maturity, silver natural afro — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across athletic ageless curves. CENTER: Indian silver fox bust queen, 50s, bust queen physique — impossibly large full heavy bust dramatically dominating silhouette, extremely narrow waist, warm bronze skin with elegant silver-era maturity, silver-streaked updo with gold pins — body fully covered in Japanese irezumi skull and chrysanthemum tattoo from neck to ankle, full body coverage from neck to ankle, bold black skull with cascading white chrysanthemums covering bust queen ageless figure. RIGHT: European silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, luminous fair skin with elegant silver-era maturity, platinum silver Hollywood waves — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: gold ankle strap heels, extra long almond crimson nails. CENTER: silver stiletto heels, extra long coffin black nails. RIGHT: gold platform stiletto heels, extra long stiletto gold nails. All: full body high-gloss oil. Environment: Jongmyo Shrine grand courtyard at night, ancient wooden shrine halls glowing amber, torches blazing along stone path, sacred smoke rising, full moon above. Lighting: warm torch amber — dancheong sacred colors blazing left, skull chrysanthemum catching cold silver center, gold glitter blazing warm right. Style: Jongmyo silver fox sacred trio editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Jongmyo silver fox trio grade, portrait 3:4 vertical.",
        "environment": "Jongmyo Shrine grand courtyard at night, torches blazing",
        "lighting": "warm torch amber triple sacred",
        "style": "Jongmyo silver fox sacred trio editorial",
        "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, portrait 3:4 vertical"
    },
    # TRIO SF-11
    "korean_silverfox_trio_minhwa_celadon_crimson_gyeongju": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Polynesian silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, warm bronzed Polynesian skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across thick thigh ageless curves. CENTER: Korean silver fox amazon, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long powerful legs, luminous porcelain skin with elegant silver-era maturity, silver updo — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon glaze with inlaid crane and cloud motifs coating amazon ageless figure. RIGHT: Mediterranean silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, warm olive skin with elegant silver-era maturity, silver-streaked waves — body fully covered in crimson ultra-fine glitter coating every inch from neck to ankle, liquid fire sculpture effect. LEFT: gold stiletto heels, extra long almond coral nails. CENTER: jade ankle strap heels, extra long stiletto jade nails. RIGHT: crimson stiletto heels, extra long coffin crimson nails. All: full body high-gloss oil. Environment: Gyeongju Anapji Pond at night, ancient pavilion reflected in still water, stone lanterns glowing amber, lotus leaves floating, full moon blazing above. Lighting: warm pavilion amber with cool moonlight — Minhwa folk colors catching moonlight left, celadon jade gleaming center, crimson glitter exploding fire right. Style: Gyeongju silver fox pond trio editorial. Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, Gyeongju silver fox trio grade, portrait 3:4 vertical.",
        "environment": "Gyeongju Anapji Pond at night, ancient pavilion",
        "lighting": "warm pavilion amber with cool moonlight",
        "style": "Gyeongju silver fox pond trio editorial",
        "quality": "Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, portrait 3:4 vertical"
    },
    # TRIO SF-12
    "korean_silverfox_trio_haetae_dragon_violet_aurora": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: African silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, deep luminous ebony skin with elegant silver-era maturity, silver locs crown — body fully covered in Korean Haetae guardian lion bodypaint from neck to ankle, mythological fire-eating beast in bold Korean traditional style blazing across massive BBW ageless curves. CENTER: Mixed silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, warm honey skin with elegant silver-era maturity, silver-streaked natural hair — body fully covered in Japanese irezumi dragon and chrysanthemum tattoo from neck to ankle, full body coverage from neck to ankle, sacred black and silver dragon coiling ageless bubble butt figure. RIGHT: Nordic silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, pale luminous arctic skin with elegant silver-era maturity, platinum silver waves — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold over-the-knee boots, extra long almond black nails. CENTER: silver stiletto heels, extra long coffin silver nails. RIGHT: violet thigh-high boots, extra long stiletto violet nails. All: full body high-gloss oil. Environment: Iceland glacier field at night, Aurora Borealis exploding across vast dark sky in electric green and violet curtains, glacial blue ice underfoot. Lighting: aurora borealis glow — Haetae guardian catching aurora warmth left, dragon catching cold light center, violet glitter exploding crystalline right. Style: Aurora silver fox trio editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, aurora silver fox trio grade, portrait 3:4 vertical.",
        "environment": "Iceland glacier field at night, Aurora Borealis green violet",
        "lighting": "aurora borealis glow triple",
        "style": "Aurora silver fox trio editorial haetae dragon",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
}

# 1) JSON 파일 생성
for key, data in PRESETS.items():
    path = os.path.join(PRESETS_DIR, f"{key}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
print(f"JSON 생성 완료: {len(PRESETS)}개")

# 2) presets_meta.py 업데이트
# DUO SF-31은 👯 Duo Glamour에, TRIO는 🎭 Trio Glamour에
with open("core/presets_meta.py", encoding="utf-8-sig") as f:
    content = f.read()

# SF-31 DUO 키 추가 (duo_ice_bath_contrast 앵커 뒤)
duo_key = "korean_silverfox_duo_irezumi_crimson_jeonju"
if f'"{duo_key}"' not in content:
    anchor = '"duo_ice_bath_contrast",'
    content = content.replace(anchor, anchor + f'\n        "{duo_key}",')

# TRIO 키 추가 (trio_penthouse_pool_dawn 앵커 뒤)
trio_keys = [k for k in PRESETS.keys() if k != duo_key]
trio_insert = []
for key in trio_keys:
    if f'"{key}"' not in content:
        trio_insert.append(key)

if trio_insert:
    anchor2 = '"trio_penthouse_pool_dawn",'
    new_trio_str = "\n".join(f'        "{k}",' for k in trio_insert)
    content = content.replace(anchor2, anchor2 + "\n" + new_trio_str)

with open("core/presets_meta.py", "w", encoding="utf-8") as f:
    f.write(content)
print(f"presets_meta.py 업데이트 완료")

# 3) hof_tier.py — TRIO HOF 추가 (SF-04, SF-11)
HOF_KEYS = [
    "korean_silverfox_trio_dancheong_crimson_void",        # TRIO SF-04
    "korean_silverfox_trio_minhwa_celadon_crimson_gyeongju", # TRIO SF-11
    # DUO SF-01~03도 여기 추가 (patch_sf_duo에서 이미 처리됐을 수도 있으나 중복 체크로 안전)
]

with open("core/hof_tier.py", encoding="utf-8-sig") as f:
    hof_content = f.read()
for key in HOF_KEYS:
    if f'"{key}"' not in hof_content:
        hof_content = hof_content.rstrip()
        hof_content += f'\n    "{key}",'
with open("core/hof_tier.py", "w", encoding="utf-8") as f:
    f.write(hof_content)
print(f"hof_tier.py 업데이트: {len(HOF_KEYS)}개 TRIO HOF 추가")

# 4) sss_tier.py — TRIO SSS 추가 (SF-05, 07, 08, 09, 10, 12)
SSS_KEYS = [
    "korean_silverfox_trio_minhwa_haetae_gold_bukchon",    # TRIO SF-02 (SS)
    "korean_silverfox_trio_irezumi_dancheong_violet_namsan", # TRIO SF-03 (SSS)
    "korean_silverfox_trio_minhwa_teal_aurora",            # TRIO SF-05
    "korean_silverfox_trio_irezumi_celadon_violet_void",   # TRIO SF-07
    "korean_silverfox_trio_haetae_minhwa_emerald_bukchon", # TRIO SF-08
    "korean_silverfox_trio_dragon_phoenix_obsidian_void",  # TRIO SF-09
    "korean_silverfox_trio_dancheong_irezumi_gold_jongmyo", # TRIO SF-10
    "korean_silverfox_trio_haetae_dragon_violet_aurora",   # TRIO SF-12
    "korean_silverfox_duo_irezumi_crimson_jeonju",         # DUO SF-31 HOF (sss_tier에도 포함)
]

with open("core/sss_tier.py", encoding="utf-8-sig") as f:
    sss_content = f.read()
for key in SSS_KEYS:
    if f'"{key}"' not in sss_content:
        sss_content = sss_content.rstrip()
        if sss_content.endswith("}"):
            sss_content = sss_content[:-1].rstrip()
            sss_content += f'\n    "{key}",\n' + "}"
with open("core/sss_tier.py", "w", encoding="utf-8") as f:
    f.write(sss_content)
print(f"sss_tier.py 업데이트: {len(SSS_KEYS)}개 추가")

# 5) AST 검증
for fname in ["core/presets_meta.py", "core/hof_tier.py", "core/sss_tier.py"]:
    ast.parse(open(fname, encoding="utf-8").read())
print("AST 검증 OK")
print(f"총 JSON: {len(list(__import__('pathlib').Path(PRESETS_DIR).glob('*.json')))}개")
