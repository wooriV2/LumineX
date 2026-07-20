# -*- coding: utf-8 -*-
"""
Silver Fox DUO 50종 패치 스크립트
- presets/*.json 생성
- presets_meta.py 👯 Duo Glamour 카테고리에 키 추가
- hof_tier.py HOF 추가
- sss_tier.py SSS 추가 (} 앞)
"""
import json, os, ast

PRESETS_DIR = "presets"
os.makedirs(PRESETS_DIR, exist_ok=True)

PRESETS = {
    "korean_silverfox_duo_irezumi_crimson_void": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox siren, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round heavy hips, full high bust dramatically dominating silhouette, luminous porcelain skin with elegant silver-era maturity, silver-streaked chignon — body fully covered in Japanese irezumi dragon and peony tattoo from neck to ankle, full body coverage from neck to ankle, sacred black and crimson dragon coiling ageless hourglass figure with blood-red peonies filling every gap. RIGHT: Black silver fox bombshell, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched impossibly tiny waist, thick powerful mature thighs, deep luminous rich ebony skin with elegant silver-era maturity, natural silver afro — body fully covered in crimson ultra-fine glitter coating every inch from neck to ankle, liquid fire sculpture effect. LEFT: crimson platform stiletto heels, extra long stiletto crimson nails. RIGHT: black platform stiletto heels, extra long coffin crimson nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight — irezumi crimson dragon blazing left, crimson glitter exploding fire right — Silver Fox void fire duality. Style: Vogue Italia silver fox void fire duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver fox void fire duo grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic chiaroscuro single spotlight",
        "style": "Vogue Italia silver fox void fire duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dancheong_emerald_bukchon": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Latina silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, explosively wide round heavy hips, lush full bust, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across pinup siren curves. RIGHT: European silver fox amazon, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long powerful lean legs, luminous fair skin with elegant silver-era maturity, platinum silver bob — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: gold ankle strap heels, extra long almond gold nails. RIGHT: emerald stiletto heels, extra long stiletto emerald nails. Both: full body high-gloss oil. Environment: Bukchon Hanok Village rooftop at night, traditional tiled roofs below, Seoul city lights glittering in distance, full moon blazing above. Lighting: cool moonlight with Seoul city neon — dancheong vivid colors catching moonlight left, emerald glitter absorbing city light right. Style: Bukchon silver fox luxury duo editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Bukchon silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Bukchon Hanok Village rooftop at night",
        "lighting": "cool moonlight with Seoul city neon",
        "style": "Bukchon silver fox luxury duo editorial",
        "quality": "Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_minhwa_obsidian_deoksugung": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox bust queen, 50s, bust queen physique — impossibly large full heavy bust dramatically dominating every inch of silhouette, extremely narrow cinched waist, warm golden Korean skin with elegant silver-era maturity, silver updo — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across bust queen ageless curves in traditional Korean colors. RIGHT: Nordic silver fox vixen, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, pale luminous arctic skin with elegant silver-era maturity, platinum silver lob — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, matte-and-shine void contrast maximum. LEFT: gold thigh-high boots, extra long coffin gold nails. RIGHT: matte black over-the-knee boots, extra long stiletto black nails. Both: full body high-gloss oil. Environment: Deoksugung Palace stone wall path at night, historic stone lanterns glowing amber, modern city buildings visible beyond ancient walls, autumn maple leaves falling. Lighting: warm stone lantern amber against cool night — Minhwa folk colors catching warm amber left, obsidian glitter dissolving into palace night right. Style: Deoksugung silver fox noir duo editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Deoksugung silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Deoksugung Palace stone wall path at night",
        "lighting": "warm stone lantern amber against cool night",
        "style": "Deoksugung silver fox noir duo editorial",
        "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_haetae_violet_aurora": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: African silver fox BBW, 50s, BBW bombshell physique — massive full-figure ageless curves, extremely wide heavy commanding hips, enormous full bust, abundantly voluptuous silhouette, deep luminous ebony skin with elegant silver-era maturity, silver locs crown — body fully covered in Korean Haetae guardian lion bodypaint from neck to ankle, mythological fire-eating beast in bold Korean traditional style blazing across massive BBW curves. RIGHT: Mixed silver fox goddess, 50s, athletic vixen physique — shredded defined abs combined with wide round hips, thick muscular mature thighs, toned commanding silhouette, glowing honey skin with elegant silver-era maturity, silver-streaked locs — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold platform stiletto heels, extra long almond black nails. RIGHT: violet platform stiletto heels, extra long stiletto violet nails. Both: full body high-gloss oil. Environment: Iceland glacier field at night, Aurora Borealis exploding across vast dark sky in electric green and violet curtains, glacial blue ice underfoot. Lighting: aurora borealis glow — Haetae guardian catching aurora warmth left, violet glitter exploding crystalline cold right. Style: Aurora silver fox BBW duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, aurora silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Iceland glacier field at night, Aurora Borealis",
        "lighting": "aurora borealis glow",
        "style": "Aurora silver fox BBW duo editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dragon_teal_namsan": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, luminous porcelain skin with elegant silver-era maturity, silver chignon — body fully covered in Korean azure dragon irezumi tattoo from neck to ankle, full body coverage from neck to ankle, sacred blue-black dragon coiling ageless hourglass figure with divine clouds and fire pearls. RIGHT: Caribbean silver fox bombshell, 50s, bubble butt goddess physique — massive round bubble butt dominating silhouette, snatched waist, explosively wide round hips, deeply bronzed Caribbean skin with elegant silver-era maturity, silver-streaked curls — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: deep blue stiletto heels, extra long coffin blue nails. RIGHT: teal stiletto heels, extra long stiletto teal nails. Both: full body high-gloss oil. Environment: Seoul city tower rooftop at night, panoramic Seoul metropolis blazing below, Han River glittering silver in distance. Lighting: Seoul neon urban glow — azure dragon catching city blue light left, teal glitter exploding iridescent in Seoul neon right. Style: Namsan silver fox Seoul duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Namsan silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Seoul city tower rooftop at night, Han River",
        "lighting": "Seoul neon urban glow",
        "style": "Namsan silver fox Seoul duo editorial",
        "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_lotus_gold_versailles": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Indian silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, wide round heavy hips, lush full bust, warm bronze skin with elegant silver-era maturity, silver-streaked updo with gold pins — body fully covered in Korean Buddhist lotus bodypaint from neck to ankle, sacred lotus flowers in traditional Korean temple painting style, crimson and gold lotuses blooming across pinup siren curves. RIGHT: European silver fox bust queen, 50s, bust queen physique — impossibly large full heavy bust dramatically dominating silhouette, extremely narrow waist, wide commanding hips, luminous fair skin with elegant silver-era maturity, platinum silver waves — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: gold ankle strap heels, extra long almond crimson nails. RIGHT: gold stiletto heels, extra long coffin gold nails. Both: full body high-gloss oil. Environment: Versailles Hall of Mirrors, grand golden chandelier blazing above, infinite mirror reflections, baroque gold architecture. Lighting: warm Versailles gold chandelier — lotus crimson-gold catching warm light left, gold glitter blazing liquid sun right — Silver Fox Versailles opulence. Style: Versailles silver fox luxury duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Versailles silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Versailles Hall of Mirrors, baroque gold architecture",
        "lighting": "warm Versailles gold chandelier",
        "style": "Versailles silver fox luxury duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_celadon_silver_monaco": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Mediterranean silver fox amazon, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long powerful legs, dramatically wide hips, warm olive skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon glaze with inlaid crane and cloud motifs coating amazon ageless figure. RIGHT: Korean silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, luminous porcelain skin with elegant silver-era maturity, silver chignon — body fully covered in silver chrome ultra-fine glitter coating every inch from neck to ankle, shifting pearl-white-silver mirror effect. LEFT: jade stiletto heels, extra long stiletto jade nails. RIGHT: silver stiletto heels, extra long almond chrome nails. Both: full body high-gloss oil. Environment: Monaco casino terrace at night, luxury harbour below, superyachts glowing, city lights reflecting on wet marble. Lighting: Monaco luxury gold with cool night — celadon jade catching harbour light left, silver glitter refracting Monaco glow right. Style: Monaco silver fox luxury duo editorial. Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, Monaco silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Monaco casino terrace at night, luxury harbour",
        "lighting": "Monaco luxury gold with cool night",
        "style": "Monaco silver fox luxury duo editorial",
        "quality": "Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_phoenix_crimson_gyeongju": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Black silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, deep luminous ebony skin with elegant silver-era maturity, silver locs updo — body fully covered in Korean sacred crane and fire flower tattoo from neck to ankle, crimson and gold sacred crane rising full body in Korean traditional style blazing across BBW curves. RIGHT: Polynesian silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, warm bronzed Polynesian skin with elegant silver-era maturity, silver-streaked waves — body fully covered in crimson-gold ultra-fine glitter coating every inch from neck to ankle, blazing liquid fire effect. LEFT: crimson platform stiletto heels, extra long coffin gold nails. RIGHT: red stiletto heels, extra long stiletto crimson nails. Both: full body high-gloss oil. Environment: Gyeongju royal burial mounds at cherry blossom dawn, ancient grass mounds glowing rose-gold, cherry petals falling, misty morning light. Lighting: rose-gold Korean dawn — sacred crane crimson-gold blazing left, crimson glitter exploding fire ember right. Style: Gyeongju silver fox dawn fire duo editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Gyeongju silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Gyeongju royal burial mounds at cherry blossom dawn",
        "lighting": "rose-gold Korean dawn",
        "style": "Gyeongju silver fox dawn fire duo editorial",
        "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_minhwa_teal_bukhansan": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox athletic, 50s, athletic vixen physique — shredded defined abs, wide round commanding hips, thick muscular mature thighs, luminous porcelain skin with elegant silver-era maturity, silver-streaked pixie — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across athletic ageless curves. RIGHT: African silver fox amazon, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long powerful legs, oiled glistening deep skin with elegant silver-era maturity, silver natural afro — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: gold clear lucite heels, extra long almond coral nails. RIGHT: teal stiletto heels, extra long stiletto teal nails. Both: full body high-gloss oil. Environment: Bukhansan mountain peak at night, Seoul city lights blazing below in vast panorama, granite boulders, star-filled sky above. Lighting: cool starlight with Seoul city glow — Minhwa folk colors catching starlight left, teal glitter exploding aurora right. Style: Bukhansan silver fox mountain duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Bukhansan silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Bukhansan mountain peak at night, Seoul panorama",
        "lighting": "cool starlight with Seoul city glow",
        "style": "Bukhansan silver fox mountain duo editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_haetae_gold_jongmyo": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Latina silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched impossibly tiny waist, explosively wide round hips, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean Haetae guardian lion bodypaint from neck to ankle, mythological fire-eating beast in bold Korean traditional style blazing across bubble butt goddess curves. RIGHT: European silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, lush full bust, luminous fair skin with elegant silver-era maturity, platinum silver Hollywood waves — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: gold thigh-high boots, extra long coffin black nails. RIGHT: gold stiletto heels, extra long almond gold nails. Both: full body high-gloss oil. Environment: Jongmyo Shrine grand courtyard at night, ancient wooden shrine halls glowing amber, torches blazing along stone path, sacred smoke rising, full moon above. Lighting: warm torch amber with sacred moonlight — Haetae guardian catching torch glow left, gold glitter blazing warm right. Style: Jongmyo silver fox sacred duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Jongmyo silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Jongmyo Shrine grand courtyard at night, torches blazing",
        "lighting": "warm torch amber with sacred moonlight",
        "style": "Jongmyo silver fox sacred duo editorial",
        "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dragon_violet_void": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, luminous porcelain skin with elegant silver-era maturity, silver updo — body fully covered in Japanese irezumi dragon and wisteria tattoo from neck to ankle, full body coverage from neck to ankle, sacred black and purple dragon coiling ageless thick thigh figure with cascading wisteria filling every gap. RIGHT: Black silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, deep luminous rich ebony skin with elegant silver-era maturity, silver-streaked locs — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: violet stiletto heels, extra long stiletto purple nails. RIGHT: deep violet platform stiletto heels, extra long coffin amethyst nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro — dragon wisteria purple catching cold spotlight left, violet glitter exploding crystalline right — Silver Fox void violet supremacy. Style: Vogue Italia silver fox void violet duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver fox void violet duo grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic chiaroscuro cold spotlight",
        "style": "Vogue Italia silver fox void violet duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_celadon_crimson_busan": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Mixed silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, warm honey skin with elegant silver-era maturity, silver-streaked natural hair — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon glaze with inlaid crane and cloud motifs coating BBW ageless curves. RIGHT: Caribbean silver fox bust queen, 50s, bust queen physique — impossibly large full heavy bust dramatically dominating silhouette, extremely narrow waist, deeply bronzed Caribbean skin with elegant silver-era maturity, silver-streaked curls — body fully covered in crimson ultra-fine glitter coating every inch from neck to ankle, liquid fire sculpture effect. LEFT: jade ankle strap heels, extra long almond jade nails. RIGHT: crimson stiletto heels, extra long stiletto crimson nails. Both: full body high-gloss oil. Environment: Busan Gamcheon Culture Village hillside at sunset, colorful painted houses cascading below, sea glittering in distance, warm golden light. Lighting: warm Busan sunset — celadon jade catching golden light left, crimson glitter blazing sunset fire right. Style: Busan silver fox sunset duo editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Busan silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Busan Gamcheon Culture Village at sunset",
        "lighting": "warm Busan sunset",
        "style": "Busan silver fox sunset duo editorial",
        "quality": "Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dancheong_teal_changdeokgung": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: European silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, luminous fair skin with elegant silver-era maturity, platinum silver waves — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across hourglass queen ageless curves. RIGHT: Latina silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: crimson stiletto heels, extra long almond red nails. RIGHT: teal clear lucite heels, extra long stiletto teal nails. Both: full body high-gloss oil. Environment: Changdeokgung Secret Garden pavilion at dawn, ancient lotus pond reflecting rose-gold morning light, moss-covered stone paths, centuries-old pine trees glowing. Lighting: rose-gold Korean dawn — dancheong sacred colors blazing warm left, teal glitter refracting dawn right. Style: Changdeokgung silver fox dawn duo editorial. Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, Changdeokgung silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Changdeokgung Secret Garden pavilion at dawn",
        "lighting": "rose-gold Korean dawn",
        "style": "Changdeokgung silver fox dawn duo editorial",
        "quality": "Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_skull_chrysanthemum_obsidian_void": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox athletic, 50s, athletic vixen physique — shredded defined abs, wide round commanding hips, thick muscular mature thighs, luminous porcelain skin with elegant silver-era maturity, silver-streaked pixie cut — body fully covered in Japanese irezumi skull and chrysanthemum tattoo from neck to ankle, full body coverage from neck to ankle, bold black and white skull with cascading chrysanthemums covering athletic ageless figure. RIGHT: Black silver fox amazon, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long powerful legs, deep luminous ebony skin with elegant silver-era maturity, silver natural afro — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, matte-and-shine void contrast maximum. LEFT: silver ankle strap heels, extra long stiletto black nails. RIGHT: matte black thigh-high boots, extra long coffin obsidian nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight — skull chrysanthemum catching cold silver light left, obsidian glitter dissolving into void darkness right. Style: Vogue Italia silver fox void dark duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver fox void dark duo grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic chiaroscuro cold silver spotlight",
        "style": "Vogue Italia silver fox void dark duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_koi_maple_gold_suncheon": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Polynesian silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, warm bronzed Polynesian skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Japanese irezumi koi and maple tattoo from neck to ankle, full body coverage from neck to ankle, vivid orange koi leaping through crimson maple leaves covering massive BBW ageless figure. RIGHT: Mediterranean silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, warm olive skin with elegant silver-era maturity, silver-streaked waves — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture effect. LEFT: gold strappy sandals, extra long almond coral nails. RIGHT: gold stiletto heels, extra long coffin gold nails. Both: full body high-gloss oil. Environment: Suncheon Bay wetlands at sunset, golden reed fields stretching to horizon, wooden boardwalk, crimson sunset blazing, migratory birds in flight. Lighting: golden Korean sunset — koi maple autumn colors blazing warm left, gold glitter exploding molten sun right. Style: Suncheon silver fox sunset duo editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Suncheon silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Suncheon Bay wetlands at sunset, golden reed fields",
        "lighting": "golden Korean sunset",
        "style": "Suncheon silver fox sunset duo editorial",
        "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_baekja_emerald_jeju": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox bust queen, 50s, bust queen physique — impossibly large full heavy bust dramatically dominating silhouette, extremely narrow waist, luminous porcelain skin with elegant silver-era maturity, silver updo — body fully covered in Korean white porcelain Baekja bodypaint from neck to ankle, pure white porcelain surface with delicate blue crane and plum blossom inlay coating bust queen ageless figure. RIGHT: Caribbean silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, deeply bronzed Caribbean skin with elegant silver-era maturity, silver-streaked curls — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: white stiletto heels, extra long stiletto blue nails. RIGHT: emerald stiletto heels, extra long coffin emerald nails. Both: full body high-gloss oil. Environment: Jeju island volcanic basalt coastline at golden hour, dramatic black lava rock formations, turquoise ocean waves, lighthouse in distance, warm golden light. Lighting: Jeju golden hour — white porcelain catching golden light left, emerald glitter refracting ocean spray right. Style: Jeju silver fox coastal duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Jeju silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Jeju island volcanic basalt coastline at golden hour",
        "lighting": "Jeju golden hour",
        "style": "Jeju silver fox coastal duo editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dragon_phoenix_void": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: African silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, oiled glistening deep skin with elegant silver-era maturity, silver locs — body fully covered in Japanese irezumi dragon and cloud tattoo from neck to ankle, full body coverage from neck to ankle, sacred blue-black dragon coiling ageless thick thigh figure with divine clouds and fire pearls. RIGHT: Korean silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, warm golden Korean skin with elegant silver-era maturity, silver-streaked chignon — body fully covered in crimson-gold phoenix bodypaint from neck to ankle, sacred phoenix rising full body in brilliant crimson and gold. LEFT: navy stiletto heels, extra long almond blue nails. RIGHT: crimson stiletto heels, extra long stiletto gold nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro — dragon azure cold spotlight left, phoenix crimson-gold blazing right — Silver Fox void elemental duality. Style: Vogue Italia silver fox void elemental duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, silver fox void elemental duo grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic chiaroscuro elemental",
        "style": "Vogue Italia silver fox void elemental duo editorial",
        "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dancheong_violet_gyeongbokgung": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Latina silver fox athletic, 50s, athletic vixen physique — shredded defined abs, wide round commanding hips, thick muscular mature thighs, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across athletic ageless curves. RIGHT: European silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, luminous fair skin with elegant silver-era maturity, platinum silver bob — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold stiletto heels, extra long coffin red nails. RIGHT: violet platform stiletto heels, extra long stiletto violet nails. Both: full body high-gloss oil. Environment: Korean traditional palace courtyard at night, ancient throne hall blazing amber behind, stone lanterns lining stone path, dancheong wooden pillars glowing, full moon above. Lighting: warm palace lantern amber with cool moonlight — dancheong sacred colors catching warm amber left, violet glitter exploding crystalline cool right. Style: Korean palace silver fox duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Korean palace silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Korean traditional palace courtyard at night",
        "lighting": "warm palace lantern amber with cool moonlight",
        "style": "Korean palace silver fox duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_minhwa_crimson_dongdaemun": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, luminous porcelain skin with elegant silver-era maturity, silver chignon — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across hourglass ageless curves. RIGHT: Black silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, deep luminous ebony skin with elegant silver-era maturity, silver locs — body fully covered in crimson ultra-fine glitter coating every inch from neck to ankle, liquid fire sculpture effect. LEFT: gold ankle strap heels, extra long almond gold nails. RIGHT: crimson platform stiletto heels, extra long coffin crimson nails. Both: full body high-gloss oil. Environment: Dongdaemun DDP night market, futuristic curved silver architecture blazing behind, neon reflections on wet pavement, city energy pulsing. Lighting: Seoul DDP neon glow — Minhwa folk colors catching neon warmth left, crimson glitter exploding fire right. Style: DDP silver fox Seoul duo editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, DDP silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Dongdaemun DDP night market, futuristic architecture",
        "lighting": "Seoul DDP neon glow",
        "style": "DDP silver fox Seoul duo editorial",
        "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_haetae_gold_aurora": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, explosively wide hips, luminous porcelain skin with elegant silver-era maturity, silver updo — body fully covered in Korean Haetae guardian lion bodypaint from neck to ankle, mythological fire-eating beast in bold Korean traditional style blazing across bubble butt goddess curves. RIGHT: African silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, deep luminous ebony skin with elegant silver-era maturity, silver natural afro — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: gold thigh-high boots, extra long stiletto black nails. RIGHT: gold stiletto heels, extra long coffin gold nails. Both: full body high-gloss oil. Environment: Iceland glacier field at night, Aurora Borealis exploding across vast dark sky in electric green and gold curtains, glacial blue ice underfoot. Lighting: aurora borealis glow — Haetae guardian catching aurora warmth left, gold glitter exploding molten sun right. Style: Aurora silver fox gold duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, aurora silver fox gold duo grade, portrait 3:4 vertical.",
        "environment": "Iceland glacier field at night, Aurora Borealis green and gold",
        "lighting": "aurora borealis glow",
        "style": "Aurora silver fox gold duo editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_lotus_obsidian_bukchon": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Polynesian silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, warm bronzed Polynesian skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean Buddhist lotus bodypaint from neck to ankle, sacred white and gold lotus flowers in traditional Korean temple painting style blooming across thick thigh ageless curves. RIGHT: European silver fox athletic, 50s, athletic vixen physique — shredded defined abs, wide round commanding hips, thick muscular mature thighs, luminous fair skin with elegant silver-era maturity, platinum silver lob — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, matte-and-shine void contrast maximum. LEFT: gold clear lucite heels, extra long almond nude nails. RIGHT: matte black ankle boots, extra long stiletto black nails. Both: full body high-gloss oil. Environment: Bukchon Hanok Village moonlit alley at night, traditional wooden gates, stone lanterns, tile roofs under full moon. Lighting: cool moonlight with lantern amber — lotus white-gold catching moonlight left, obsidian glitter dissolving into Korean night right. Style: Bukchon silver fox moonlit duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Bukchon silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Bukchon Hanok Village moonlit alley at night",
        "lighting": "cool moonlight with lantern amber",
        "style": "Bukchon silver fox moonlit duo editorial",
        "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dragon_silver_shibuya": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Caribbean silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, lush full bust, deeply bronzed Caribbean skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Japanese irezumi dragon and cloud tattoo from neck to ankle, full body coverage from neck to ankle, sacred blue-silver dragon coiling ageless pinup figure with silver clouds filling every gap. RIGHT: Korean silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, luminous porcelain skin with elegant silver-era maturity, silver-streaked chignon — body fully covered in silver moonlight ultra-fine glitter coating every inch from neck to ankle, shifting pearl-white-silver mirror effect. LEFT: silver strappy sandals, extra long coffin blue nails. RIGHT: silver platform stiletto heels, extra long almond chrome nails. Both: full body high-gloss oil. Environment: Shibuya scramble crossing Tokyo at night, neon signs blazing, rain-soaked streets reflecting neon, umbrellas and crowds in distance. Lighting: Tokyo neon urban glow — dragon silver catching cool neon left, silver glitter refracting Shibuya neon right. Style: Shibuya silver fox Tokyo duo editorial. Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, Shibuya silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Shibuya scramble crossing Tokyo at night, rain-soaked neon",
        "lighting": "Tokyo neon urban glow",
        "style": "Shibuya silver fox Tokyo duo editorial",
        "quality": "Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_minhwa_emerald_monaco": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Mixed silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, warm honey skin with elegant silver-era maturity, silver-streaked natural hair — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across hourglass ageless curves. RIGHT: Indian silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, thick powerful thighs, warm bronze skin with elegant silver-era maturity, silver-streaked updo — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: gold stiletto heels, extra long almond coral nails. RIGHT: emerald stiletto heels, extra long coffin emerald nails. Both: full body high-gloss oil. Environment: Monaco casino terrace at night, luxury harbour below, superyachts glowing, wet marble reflecting city lights, palm trees swaying. Lighting: Monaco luxury gold with cool harbour — Minhwa folk colors catching Monaco warmth left, emerald glitter blazing crystalline right. Style: Monaco silver fox luxury duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Monaco silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Monaco casino terrace at night, superyachts",
        "lighting": "Monaco luxury gold with cool harbour",
        "style": "Monaco silver fox luxury duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dancheong_teal_void": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Nordic silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, pale luminous arctic skin with elegant silver-era maturity, platinum silver waves — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across bubble butt goddess curves. RIGHT: African silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, deep luminous ebony skin with elegant silver-era maturity, silver natural afro — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: gold clear lucite heels, extra long almond blue nails. RIGHT: teal platform stiletto heels, extra long stiletto teal nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro — dancheong vivid sacred colors blazing warm left, teal glitter exploding aurora cold right — Silver Fox void teal duality. Style: Vogue Italia silver fox void teal duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver fox void teal duo grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic chiaroscuro void teal",
        "style": "Vogue Italia silver fox void teal duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_haetae_emerald_void": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Black silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, deep luminous ebony skin with elegant silver-era maturity, silver locs crown — body fully covered in Korean Haetae guardian lion bodypaint from neck to ankle, mythological fire-eating beast in bold Korean traditional style blazing across thick thigh ageless curves. RIGHT: Korean silver fox amazon, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long powerful legs, luminous porcelain skin with elegant silver-era maturity, silver updo — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: gold over-the-knee boots, extra long coffin black nails. RIGHT: emerald stiletto heels, extra long stiletto emerald nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro — Haetae guardian catching warm spotlight left, emerald glitter exploding crystalline cold right — Silver Fox void emerald duality. Style: Vogue Italia silver fox void emerald duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver fox void emerald duo grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic chiaroscuro void emerald",
        "style": "Vogue Italia silver fox void emerald duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dragon_gold_changdeokgung": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Indian silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, warm bronze skin with elegant silver-era maturity, silver-streaked updo — body fully covered in Japanese irezumi dragon and wisteria tattoo from neck to ankle, full body coverage from neck to ankle, sacred black and purple dragon coiling ageless BBW figure with cascading wisteria filling every gap. RIGHT: Caribbean silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, deeply bronzed Caribbean skin with elegant silver-era maturity, silver-streaked curls — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: gold thigh-high boots, extra long almond purple nails. RIGHT: gold platform stiletto heels, extra long coffin gold nails. Both: full body high-gloss oil. Environment: Changdeokgung Secret Garden pavilion at night, ancient lotus pond reflecting moonlight, centuries-old pine trees, full moon blazing, sacred mist rising. Lighting: cool moonlight with sacred amber — dragon wisteria catching moonlight left, gold glitter blazing warm right. Style: Changdeokgung silver fox night duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Changdeokgung silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Changdeokgung Secret Garden pavilion at night",
        "lighting": "cool moonlight with sacred amber",
        "style": "Changdeokgung silver fox night duo editorial",
        "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_minhwa_obsidian_aurora": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: European silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, luminous fair skin with elegant silver-era maturity, platinum silver lob — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across thick thigh ageless curves. RIGHT: Korean silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, luminous porcelain skin with elegant silver-era maturity, silver chignon — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, matte-and-shine void contrast maximum. LEFT: gold stiletto heels, extra long stiletto coral nails. RIGHT: matte black thigh-high boots, extra long coffin obsidian nails. Both: full body high-gloss oil. Environment: Iceland glacier field at night, Aurora Borealis exploding across vast dark sky in electric green and violet curtains, glacial blue ice underfoot. Lighting: aurora borealis glow — Minhwa folk colors catching aurora warmth left, obsidian glitter dissolving into arctic night right. Style: Aurora silver fox dark duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora silver fox dark duo grade, portrait 3:4 vertical.",
        "environment": "Iceland glacier field at night, Aurora Borealis green violet",
        "lighting": "aurora borealis glow dark",
        "style": "Aurora silver fox dark duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_celadon_violet_bukhansan": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: African silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, deep luminous ebony skin with elegant silver-era maturity, silver locs — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon glaze with inlaid crane and cloud motifs coating hourglass ageless figure. RIGHT: Latina silver fox bust queen, 50s, bust queen physique — impossibly large full heavy bust dramatically dominating silhouette, extremely narrow waist, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: jade ankle strap heels, extra long almond jade nails. RIGHT: violet platform stiletto heels, extra long stiletto violet nails. Both: full body high-gloss oil. Environment: Bukhansan mountain peak at night, Seoul city lights blazing below in vast panorama, granite boulders, Milky Way above. Lighting: cool starlight with Seoul city glow — celadon jade catching starlight left, violet glitter exploding amethyst right. Style: Bukhansan silver fox mountain duo editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Bukhansan silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Bukhansan mountain peak at night, Milky Way",
        "lighting": "cool starlight with Seoul city glow",
        "style": "Bukhansan silver fox mountain duo editorial",
        "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_irezumi_gold_deoksugung": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, luminous porcelain skin with elegant silver-era maturity, silver-streaked chignon — body fully covered in Japanese irezumi tiger and lotus tattoo from neck to ankle, full body coverage from neck to ankle, bold black and gold tiger prowling ageless pinup figure with crimson lotus blooms filling every gap. RIGHT: Nordic silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, pale luminous arctic skin with elegant silver-era maturity, platinum silver updo — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: gold strappy sandals, extra long coffin black nails. RIGHT: gold stiletto heels, extra long almond gold nails. Both: full body high-gloss oil. Environment: Deoksugung Palace stone wall path at night, historic stone lanterns glowing amber, modern city buildings visible beyond ancient walls, autumn maple leaves falling. Lighting: warm stone lantern amber — irezumi tiger catching amber glow left, gold glitter blazing warm right. Style: Deoksugung silver fox autumn duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Deoksugung silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Deoksugung Palace stone wall path at night, autumn leaves",
        "lighting": "warm stone lantern amber",
        "style": "Deoksugung silver fox autumn duo editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_lotus_teal_suncheon": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Mixed silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, warm honey skin with elegant silver-era maturity, silver-streaked natural hair — body fully covered in Korean Buddhist lotus bodypaint from neck to ankle, sacred white and gold lotus flowers in traditional Korean temple painting style blooming across BBW ageless curves. RIGHT: Mediterranean silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, warm olive skin with elegant silver-era maturity, silver-streaked waves — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: gold ankle strap heels, extra long almond coral nails. RIGHT: teal stiletto heels, extra long coffin teal nails. Both: full body high-gloss oil. Environment: Suncheon Bay wetlands at dusk, golden reed fields stretching to horizon, wooden boardwalk over still water, crimson sunset blazing, birds in flight. Lighting: golden Korean dusk — lotus white-gold catching sunset left, teal glitter refracting dusk right. Style: Suncheon silver fox dusk duo editorial. Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, Suncheon silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Suncheon Bay wetlands at dusk",
        "lighting": "golden Korean dusk",
        "style": "Suncheon silver fox dusk duo editorial",
        "quality": "Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dragon_crimson_namsan": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, luminous porcelain skin with elegant silver-era maturity, silver updo — body fully covered in Japanese irezumi dragon and peony tattoo from neck to ankle, full body coverage from neck to ankle, sacred black and crimson dragon coiling ageless BBW figure with blood-red peonies filling every gap. RIGHT: European silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, luminous fair skin with elegant silver-era maturity, platinum silver waves — body fully covered in crimson ultra-fine glitter coating every inch from neck to ankle, liquid fire sculpture effect. LEFT: black thigh-high boots, extra long coffin black nails. RIGHT: crimson stiletto heels, extra long stiletto crimson nails. Both: full body high-gloss oil. Environment: Seoul city tower rooftop at night, panoramic Seoul metropolis blazing below, Han River glittering silver in distance, dramatic urban skyline. Lighting: Seoul neon urban glow — dragon crimson catching city warmth left, crimson glitter exploding fire right. Style: Namsan silver fox Seoul duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Namsan silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Seoul city tower rooftop at night, Han River panorama",
        "lighting": "Seoul neon urban glow crimson",
        "style": "Namsan silver fox Seoul duo editorial",
        "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_celadon_gold_versailles": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, luminous porcelain skin with elegant silver-era maturity, silver-streaked chignon — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon glaze with inlaid crane and cloud motifs coating pinup ageless curves. RIGHT: Latina silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: gold ankle strap heels, extra long almond jade nails. RIGHT: gold platform stiletto heels, extra long coffin gold nails. Both: full body high-gloss oil. Environment: Versailles Hall of Mirrors, grand golden chandelier blazing above, infinite mirror reflections, baroque gold architecture, warm amber candlelight. Lighting: warm Versailles gold chandelier — celadon jade catching warm gold light left, gold glitter blazing liquid sun right. Style: Versailles silver fox luxury duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Versailles silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Versailles Hall of Mirrors, baroque gold architecture",
        "lighting": "warm Versailles gold chandelier",
        "style": "Versailles silver fox luxury duo editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_irezumi_teal_void": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Nordic silver fox athletic, 50s, athletic vixen physique — shredded defined abs, wide round commanding hips, thick muscular mature thighs, pale luminous arctic skin with elegant silver-era maturity, platinum silver pixie — body fully covered in Japanese irezumi koi and maple tattoo from neck to ankle, full body coverage from neck to ankle, vivid orange koi leaping through crimson maple leaves covering athletic ageless figure. RIGHT: Caribbean silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, deeply bronzed Caribbean skin with elegant silver-era maturity, silver-streaked curls — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: gold clear lucite heels, extra long stiletto orange nails. RIGHT: teal stiletto heels, extra long coffin teal nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro — koi maple autumn colors blazing warm left, teal glitter exploding aurora cold right — Silver Fox void autumn duality. Style: Vogue Italia silver fox void autumn duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, silver fox void autumn duo grade, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic chiaroscuro void autumn",
        "style": "Vogue Italia silver fox void autumn duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dancheong_crimson_busan": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Black silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, deep luminous ebony skin with elegant silver-era maturity, silver locs — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across hourglass ageless curves. RIGHT: European silver fox bubble butt, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, luminous fair skin with elegant silver-era maturity, platinum silver waves — body fully covered in crimson ultra-fine glitter coating every inch from neck to ankle, liquid fire sculpture effect. LEFT: gold stiletto heels, extra long almond crimson nails. RIGHT: crimson platform stiletto heels, extra long coffin crimson nails. Both: full body high-gloss oil. Environment: Busan Gamcheon Culture Village hillside at sunset, colorful painted houses cascading down hillside, sea glittering in distance, warm golden sunset blazing. Lighting: warm Busan sunset — dancheong sacred colors catching sunset left, crimson glitter exploding sunset fire right. Style: Busan silver fox sunset duo editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Busan silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Busan Gamcheon Culture Village at golden sunset",
        "lighting": "warm Busan sunset crimson",
        "style": "Busan silver fox sunset duo editorial",
        "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_minhwa_gold_aurora": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, luminous porcelain skin with elegant silver-era maturity, silver chignon — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across thick thigh ageless curves. RIGHT: African silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, deep luminous ebony skin with elegant silver-era maturity, silver natural afro — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: gold thigh-high boots, extra long stiletto black nails. RIGHT: gold stiletto heels, extra long coffin gold nails. Both: full body high-gloss oil. Environment: Iceland glacier field at night, Aurora Borealis exploding across vast dark sky in electric green and gold curtains, glacial blue ice underfoot. Lighting: aurora borealis glow — Minhwa folk colors catching aurora warmth left, gold glitter exploding molten sun right. Style: Aurora silver fox gold duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, aurora silver fox gold duo grade, portrait 3:4 vertical.",
        "environment": "Iceland glacier field at night, Aurora Borealis green gold",
        "lighting": "aurora borealis gold glow",
        "style": "Aurora silver fox gold duo editorial",
        "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_haetae_teal_dongdaemun": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Latina silver fox amazon, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long powerful legs, bronzed Latin skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean Haetae guardian lion bodypaint from neck to ankle, mythological fire-eating beast in bold Korean traditional style blazing across amazon ageless curves. RIGHT: Indian silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, warm bronze skin with elegant silver-era maturity, silver-streaked updo — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: gold ankle strap heels, extra long almond black nails. RIGHT: teal clear lucite heels, extra long stiletto teal nails. Both: full body high-gloss oil. Environment: Dongdaemun DDP night market, futuristic curved silver architecture blazing behind, neon reflections on wet pavement, city energy pulsing. Lighting: Seoul DDP neon glow — Haetae guardian catching neon warmth left, teal glitter exploding iridescent right. Style: DDP silver fox Seoul duo editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, DDP silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Dongdaemun DDP night market, futuristic neon",
        "lighting": "Seoul DDP neon glow teal",
        "style": "DDP silver fox Seoul duo editorial",
        "quality": "Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dragon_obsidian_gyeongbokgung": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Mixed silver fox pinup, 50s, pinup siren physique — maximum pinup hourglass silhouette, corseted impossibly tiny waist, extremely wide round heavy hips, warm honey skin with elegant silver-era maturity, silver-streaked natural hair — body fully covered in Japanese irezumi dragon and chrysanthemum tattoo from neck to ankle, full body coverage from neck to ankle, sacred black and silver dragon coiling ageless pinup figure with white chrysanthemums filling every gap. RIGHT: Nordic silver fox thick thigh, 50s, thick thigh temptress physique — impossibly thick powerful thighs, wide commanding hips, full bust, pale luminous arctic skin with elegant silver-era maturity, platinum silver bob — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, matte-and-shine void contrast maximum. LEFT: silver stiletto heels, extra long coffin silver nails. RIGHT: matte black over-the-knee boots, extra long stiletto obsidian nails. Both: full body high-gloss oil. Environment: Korean traditional palace courtyard at night, ancient throne hall blazing amber behind, stone lanterns lining stone path, dancheong wooden pillars glowing, full moon above. Lighting: warm palace lantern amber — dragon silver catching cold moonlight left, obsidian glitter dissolving into palace night right. Style: Korean palace silver fox noir duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Korean palace silver fox duo grade, portrait 3:4 vertical.",
        "environment": "Korean traditional palace courtyard at night, full moon",
        "lighting": "warm palace lantern amber moonlight",
        "style": "Korean palace silver fox noir duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_lotus_crimson_aurora": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Polynesian silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, warm bronzed Polynesian skin with elegant silver-era maturity, silver-streaked waves — body fully covered in Korean Buddhist lotus bodypaint from neck to ankle, sacred crimson and gold lotus flowers in traditional Korean temple painting style blooming across BBW ageless curves. RIGHT: Korean silver fox athletic, 50s, athletic vixen physique — shredded defined abs, wide round commanding hips, thick muscular mature thighs, luminous porcelain skin with elegant silver-era maturity, silver-streaked pixie — body fully covered in crimson ultra-fine glitter coating every inch from neck to ankle, liquid fire sculpture effect. LEFT: gold clear lucite heels, extra long almond crimson nails. RIGHT: crimson platform stiletto heels, extra long stiletto crimson nails. Both: full body high-gloss oil. Environment: Iceland glacier field at night, Aurora Borealis exploding across vast dark sky in electric crimson and green curtains, glacial blue ice underfoot. Lighting: aurora borealis crimson glow — lotus crimson-gold blazing left, crimson glitter exploding aurora fire right. Style: Aurora silver fox crimson duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, aurora silver fox crimson duo grade, portrait 3:4 vertical.",
        "environment": "Iceland glacier field at night, crimson Aurora Borealis",
        "lighting": "aurora borealis crimson glow",
        "style": "Aurora silver fox crimson duo editorial",
        "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_dancheong_gold_bukchon": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Black silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, deep luminous ebony skin with elegant silver-era maturity, silver natural afro — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across hourglass ageless curves. RIGHT: European silver fox BBW, 50s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, luminous fair skin with elegant silver-era maturity, platinum silver Hollywood waves — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: crimson stiletto heels, extra long almond red nails. RIGHT: gold platform stiletto heels, extra long coffin gold nails. Both: full body high-gloss oil. Environment: Bukchon Hanok Village rooftop at night, traditional tiled roofs below, Seoul city lights glittering in distance, full moon blazing above, hanok lanterns glowing. Lighting: cool moonlight with Seoul city neon — dancheong vivid colors catching moonlight left, gold glitter blazing warm right. Style: Bukchon silver fox luxury duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Bukchon silver fox gold duo grade, portrait 3:4 vertical.",
        "environment": "Bukchon Hanok Village rooftop at night, full moon",
        "lighting": "cool moonlight with Seoul city neon gold",
        "style": "Bukchon silver fox luxury duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
}

# SF-01~03 (이전 세션 검증 완료분, 이번에 JSON + 티어 등록)
PRESETS_SF_01_03 = {
    "korean_silverfox_duo_dancheong_gold_void": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox siren, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round heavy hips, full high bust, luminous porcelain skin with elegant silver-era maturity, silver-streaked chignon — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across hourglass ageless curves. RIGHT: Black silver fox bombshell, 50s, bubble butt goddess physique — massive round bubble butt commanding every inch, snatched waist, deep luminous ebony skin with elegant silver-era maturity, silver natural afro — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture effect. LEFT: gold stiletto heels, long crimson nails. RIGHT: gold stiletto heels, long gold nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro — dancheong sacred colors blazing warm left, gold glitter blazing liquid sun right. Style: Vogue Italia silver fox void gold duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical.",
        "environment": "pure black void, seamless obsidian backdrop",
        "lighting": "dramatic chiaroscuro void gold",
        "style": "Vogue Italia silver fox void gold duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_irezumi_obsidian_deoksugung": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox hourglass, 50s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, luminous porcelain skin with elegant silver-era maturity, silver chignon — body fully covered in Japanese irezumi dragon and peony tattoo from neck to ankle, full body coverage from neck to ankle, sacred black and crimson dragon coiling ageless hourglass figure with blood-red peonies. RIGHT: Nordic silver fox amazon, 50s, amazon warrior physique — tall commanding physique, broad strong shoulders, long powerful legs, pale luminous arctic skin with elegant silver-era maturity, platinum silver lob — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, matte-and-shine void contrast. LEFT: crimson stiletto heels, long red nails. RIGHT: matte black thigh-high boots, long black nails. Both: full body high-gloss oil. Environment: Deoksugung Palace stone wall path at night, historic stone lanterns glowing amber, autumn maple leaves falling. Lighting: warm stone lantern amber against cool night. Style: Deoksugung silver fox noir duo editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, portrait 3:4 vertical.",
        "environment": "Deoksugung Palace stone wall path at night",
        "lighting": "warm stone lantern amber against cool night",
        "style": "Deoksugung silver fox noir duo editorial",
        "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, portrait 3:4 vertical"
    },
    "korean_silverfox_duo_minhwa_violet_aurora": {
        "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean silver fox bust queen, 50s, bust queen physique — impossibly large full heavy bust dramatically dominating silhouette, extremely narrow waist, warm golden Korean skin with elegant silver-era maturity, silver updo — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across bust queen ageless curves. RIGHT: Nordic silver fox goddess, 50s, amazon warrior physique — tall commanding ageless physique, broad strong shoulders, long lean legs, pale luminous arctic skin with elegant silver-era maturity, platinum silver lob — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold stiletto heels, long coral nails. RIGHT: violet stiletto heels, long amethyst nails. Both: full body high-gloss oil. Environment: Iceland glacier field at night, Aurora Borealis exploding across vast dark sky in electric green and violet curtains, glacial blue ice underfoot. Lighting: aurora borealis glow — Minhwa folk colors catching aurora warmth left, violet glitter exploding crystalline right. Style: Aurora Korean Minhwa silver fox duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical.",
        "environment": "Iceland glacier field at night, Aurora Borealis",
        "lighting": "aurora borealis glow violet",
        "style": "Aurora Korean Minhwa silver fox duo editorial",
        "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, portrait 3:4 vertical"
    },
}
PRESETS.update(PRESETS_SF_01_03)

# 1) JSON 파일 생성
for key, data in PRESETS.items():
    path = os.path.join(PRESETS_DIR, f"{key}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
print(f"JSON 생성 완료: {len(PRESETS)}개")

# 2) presets_meta.py — 👯 Duo Glamour 카테고리에 키 추가
DUO_SF_KEYS = list(PRESETS.keys())

with open("core/presets_meta.py", encoding="utf-8-sig") as f:
    content = f.read()

# 마지막 "👯 Duo Glamour" 블록 찾아서 키 추가
insert_keys = []
for key in DUO_SF_KEYS:
    if f'"{key}"' not in content:
        insert_keys.append(key)

if insert_keys:
    # 두 번째 "👯 Duo Glamour" 블록의 마지막 항목 뒤에 삽입
    # "duo_ice_bath_contrast" 뒤에 추가
    anchor = '"duo_ice_bath_contrast",'
    new_keys_str = "\n".join(f'        "{k}",' for k in insert_keys)
    content = content.replace(anchor, anchor + "\n" + new_keys_str)

with open("core/presets_meta.py", "w", encoding="utf-8") as f:
    f.write(content)
print(f"presets_meta.py 업데이트: {len(insert_keys)}개 키 추가")

# 3) hof_tier.py 패치
HOF_KEYS = [
    "korean_silverfox_duo_dancheong_gold_void",        # SF-01
    "korean_silverfox_duo_irezumi_obsidian_deoksugung",# SF-02
    "korean_silverfox_duo_minhwa_violet_aurora",       # SF-03
    "korean_silverfox_duo_irezumi_crimson_void",       # SF-04
    "korean_silverfox_duo_minhwa_obsidian_deoksugung", # SF-06
    "korean_silverfox_duo_lotus_gold_versailles",      # SF-09
    "korean_silverfox_duo_phoenix_crimson_gyeongju",   # SF-11
    "korean_silverfox_duo_koi_maple_gold_suncheon",    # SF-20
    "korean_silverfox_duo_minhwa_crimson_dongdaemun",  # SF-24
    "korean_silverfox_duo_haetae_gold_aurora",         # SF-26
    "korean_silverfox_duo_lotus_obsidian_bukchon",     # SF-27
    "korean_silverfox_duo_irezumi_crimson_jeonju",     # SF-31 (별도 JSON 필요)
    "korean_silverfox_duo_minhwa_obsidian_aurora",     # SF-36
    "korean_silverfox_duo_dragon_crimson_namsan",      # SF-41
    "korean_silverfox_duo_dancheong_crimson_busan",    # SF-45
    "korean_silverfox_duo_lotus_crimson_aurora",       # SF-49
]

with open("core/hof_tier.py", encoding="utf-8-sig") as f:
    hof_content = f.read()
for key in HOF_KEYS:
    if f'"{key}"' not in hof_content:
        hof_content = hof_content.rstrip()
        hof_content += f'\n    "{key}",'
with open("core/hof_tier.py", "w", encoding="utf-8") as f:
    f.write(hof_content)
print(f"hof_tier.py 업데이트: {len(HOF_KEYS)}개 HOF 추가")

# 4) sss_tier.py 패치 (반드시 } 앞에 삽입)
SSS_KEYS = [
    "korean_silverfox_duo_dancheong_emerald_bukchon",  # SF-05
    "korean_silverfox_duo_haetae_violet_aurora",       # SF-07
    "korean_silverfox_duo_dragon_teal_namsan",         # SF-08
    "korean_silverfox_duo_celadon_silver_monaco",      # SF-10
    "korean_silverfox_duo_minhwa_teal_bukhansan",      # SF-12
    "korean_silverfox_duo_haetae_gold_jongmyo",        # SF-13
    "korean_silverfox_duo_dragon_violet_void",         # SF-14
    "korean_silverfox_duo_celadon_crimson_busan",      # SF-15
    "korean_silverfox_duo_dancheong_teal_changdeokgung", # SF-18
    "korean_silverfox_duo_baekja_emerald_jeju",        # SF-21
    "korean_silverfox_duo_dragon_phoenix_void",        # SF-22
    "korean_silverfox_duo_dancheong_violet_gyeongbokgung", # SF-23
    "korean_silverfox_duo_dragon_silver_shibuya",      # SF-28
    "korean_silverfox_duo_minhwa_emerald_monaco",      # SF-29
    "korean_silverfox_duo_dancheong_teal_void",        # SF-32
    "korean_silverfox_duo_haetae_emerald_void",        # SF-34
    "korean_silverfox_duo_dragon_gold_changdeokgung",  # SF-35
    "korean_silverfox_duo_celadon_violet_bukhansan",   # SF-37
    "korean_silverfox_duo_irezumi_gold_deoksugung",    # SF-38
    "korean_silverfox_duo_lotus_teal_suncheon",        # SF-39
    "korean_silverfox_duo_celadon_gold_versailles",    # SF-43
    "korean_silverfox_duo_irezumi_teal_void",          # SF-44
    "korean_silverfox_duo_minhwa_gold_aurora",         # SF-46
    "korean_silverfox_duo_haetae_teal_dongdaemun",     # SF-47
    "korean_silverfox_duo_dragon_obsidian_gyeongbokgung", # SF-48
    "korean_silverfox_duo_dancheong_gold_bukchon",     # SF-50
]

# SS 키 (SF-19만)
SS_KEY = "korean_silverfox_duo_skull_chrysanthemum_obsidian_void"

with open("core/sss_tier.py", encoding="utf-8-sig") as f:
    sss_content = f.read()
for key in SSS_KEYS + [SS_KEY]:
    if f'"{key}"' not in sss_content:
        sss_content = sss_content.rstrip()
        if sss_content.endswith("}"):
            sss_content = sss_content[:-1].rstrip()
            sss_content += f'\n    "{key}",\n' + "}"
with open("core/sss_tier.py", "w", encoding="utf-8") as f:
    f.write(sss_content)
print(f"sss_tier.py 업데이트: {len(SSS_KEYS)}개 SSS + 1개 SS 추가")

# 5) AST 검증
for fname in ["core/presets_meta.py", "core/hof_tier.py", "core/sss_tier.py"]:
    ast.parse(open(fname, encoding="utf-8").read())
print("AST 검증 OK")
print(f"총 JSON 파일: {len(list(__import__('pathlib').Path(PRESETS_DIR).glob('*.json')))}개")
