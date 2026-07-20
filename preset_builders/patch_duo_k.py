import json, os, ast

PRESETS_DIR = "presets"
os.makedirs(PRESETS_DIR, exist_ok=True)

def save_json(key, data):
    path = os.path.join(PRESETS_DIR, f"{key}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ============================================================
# DUO-K Korean MILF 16종
# ============================================================

save_json("korean_milf_duo_dancheong_violet_void", {
    "subject": "TWO women — Latina MILF bombshell + European MILF goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Latina MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, explosively wide dramatic round hips, impossibly tiny cinched waist, thick powerful thighs, bronzed Latin skin with natural maturity — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid red, blue, green, gold sacred geometric temple ceiling patterns blazing across mature dramatic curves. RIGHT: European MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, sculpted hourglass, full high bust, wide rounded hips, luminous fair skin with natural maturity — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold stiletto heels, long crimson nails. RIGHT: violet stiletto heels, long amethyst nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight — dancheong vivid sacred colors blazing warm left, violet glitter exploding crystalline cold right. Style: Vogue Italia Korean dancheong MILF void duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Korean dancheong void duo grade, portrait 3:4 vertical.",
    "environment": "pure black void",
    "lighting": "dramatic chiaroscuro single spotlight",
    "style": "Vogue Italia Korean dancheong MILF void duo editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Korean dancheong void duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_minhwa_emerald_bukchon", {
    "subject": "TWO women — Korean MILF bust queen + Caribbean MILF goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean MILF bust queen, early 30s, MILF glamour physique — mature voluptuous curves, impossibly large full heavy bust dramatically dominating silhouette, extremely narrow cinched waist, luminous porcelain skin with natural maturity — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across mature abundant figure in traditional Korean colors. RIGHT: Caribbean MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, powerfully athletic bubble butt, snatched tiny waist, explosively wide round hips, muscular thick thighs, deeply bronzed Caribbean skin with natural maturity — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: gold stiletto heels, long coral nails. RIGHT: emerald stiletto heels, long emerald nails. Both: full body high-gloss oil. Environment: Bukchon Hanok Village rooftop at night, traditional tiled roofs below, Seoul city lights glittering in distance, full moon blazing above. Lighting: cool moonlight with Seoul city neon — Minhwa folk colors catching moonlight left, emerald glitter absorbing city light right. Style: Bukchon MILF luxury duo editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Bukchon duo grade, portrait 3:4 vertical.",
    "environment": "Bukchon Hanok Village rooftop at night",
    "lighting": "cool moonlight with Seoul city neon",
    "style": "Bukchon MILF luxury duo editorial",
    "quality": "Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Bukchon duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_haetae_obsidian_deoksugung", {
    "subject": "TWO women — BBW MILF glamour + Nordic MILF goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, dramatic full-figure silhouette, extremely wide heavy hips, maximalist abundant curves, warm caramel skin with natural maturity — body fully covered in Korean Haetae guardian lion tattoo from neck to ankle, mythological fire-eating beast in bold Korean traditional style covering voluminous mature figure. RIGHT: Nordic MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, tall commanding physique, broad strong shoulders, long lean mature legs, pale luminous arctic skin with natural maturity — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, matte-and-shine void contrast maximum. LEFT: gold stiletto heels, long black nails. RIGHT: matte black stiletto heels, long black nails. Both: full body high-gloss oil. Environment: Deoksugung Palace stone wall path at night, historic stone lanterns glowing amber, modern city buildings visible beyond ancient walls, autumn maple leaves falling. Lighting: warm stone lantern amber against cool night — Haetae guardian catching warm amber left, obsidian glitter dissolving into Korean palace night right. Style: Deoksugung MILF noir duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Deoksugung duo grade, portrait 3:4 vertical.",
    "environment": "Deoksugung Palace stone wall path at night",
    "lighting": "warm stone lantern amber against cool night",
    "style": "Deoksugung MILF noir duo editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Deoksugung duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_mudang_crimson_jongmyo", {
    "subject": "TWO women — Korean MILF pinup + Black BBW MILF, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean MILF pinup, early 30s, MILF glamour physique — mature voluptuous curves, impossibly tiny corseted waist, extremely wide round heavy hips, lush full mature bust, warm caramel skin with natural maturity — body fully covered in Korean Mudang shaman tattoo from neck to ankle, sacred ritual symbols, spirit summoning motifs and divine shamanic patterns in red and gold blazing across mature dramatic curves. RIGHT: Black BBW MILF, early 30s, MILF glamour physique — mature voluptuous curves, extremely curvy full-figure silhouette, very broad wide hips, very thick thighs, abundant voluptuous mature body, deep warm skin with natural maturity — body fully covered in crimson-gold ultra-fine glitter coating every inch from neck to ankle, blazing ember liquid fire effect. LEFT: crimson stiletto heels, long crimson nails. RIGHT: red stiletto heels, long flame nails. Both: full body high-gloss oil. Environment: Jongmyo Shrine at night, ancient royal ancestral hall, stone paths lined with spirit tablets, solemn moonlit atmosphere, sacred smoke rising. Lighting: moonlight with sacred ritual flame — Mudang shamanic red-gold catching ritual flame left, crimson glitter blazing fire ember right. Style: Jongmyo MILF sacred duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Jongmyo shrine duo grade, portrait 3:4 vertical.",
    "environment": "Jongmyo Shrine at night",
    "lighting": "moonlight with sacred ritual flame",
    "style": "Jongmyo MILF sacred duo editorial",
    "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Jongmyo shrine duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_baekja_teal_haeundae", {
    "subject": "TWO women — Korean MILF petite glamour + Athletic MILF bombshell, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean MILF petite glamour, early 30s, MILF glamour physique — mature voluptuous curves, compact yet dramatically curvaceous mature figure, full bust and wide hips on petite frame, miniature MILF hourglass, warm Korean golden skin with natural maturity — body fully covered in Korean Baekja white porcelain bodypaint from neck to ankle, pure white porcelain with blue cobalt brushwork crane and bamboo motifs coating mature compact body. RIGHT: Athletic MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, perfect balance of muscle definition and mature feminine curves, defined abs with round full mature hips, toned thick mature thighs, bronzed warm skin with natural maturity — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: white stiletto heels, long cobalt nails. RIGHT: teal stiletto heels, long violet nails. Both: full body high-gloss oil. Environment: Haeundae Beach Busan at night, city lights reflecting in dark ocean, luxury hotel towers blazing behind, waves lapping warm sand. Lighting: Busan beach night neon glow — Baekja white porcelain catching cool city light left, teal glitter refracting ocean shimmer right. Style: Haeundae MILF luxury duo editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Haeundae duo grade, portrait 3:4 vertical.",
    "environment": "Haeundae Beach Busan at night",
    "lighting": "Busan beach night neon glow",
    "style": "Haeundae MILF luxury duo editorial",
    "quality": "Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Haeundae duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_tanghwa_emerald_monaco", {
    "subject": "TWO women — Korean MILF elegance + Black MILF hourglass goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean MILF elegance, early 30s, MILF glamour physique — mature voluptuous curves, sophisticated mature Korean beauty, impeccably elegant mature figure, luminous porcelain skin with natural maturity — body fully covered in Korean Tang dynasty court flower Tanghwa bodypaint from neck to ankle, elaborate court flower patterns in crimson, gold and jade coating entire mature body, royal Joseon court botanical art as living mature body art. RIGHT: Black MILF hourglass goddess, early 30s, MILF glamour physique — mature voluptuous curves, impossibly dramatic waist-to-hip ratio, extremely wide round mature hips, ultra-narrow waist, very thick powerful thighs, deep luminous rich ebony skin with natural maturity — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: gold stiletto heels, long crimson nails. RIGHT: emerald stiletto heels, long emerald nails. Both: full body high-gloss oil. Environment: Monaco Casino terrace at night, electric violet and gold neon flooding wet marble, luxury harbor lights glittering below. Lighting: Monaco neon violet-gold flood — Korean Tanghwa court flowers catching warm gold neon left, emerald glitter absorbing cool harbor light right. Style: Monaco Korean MILF duo editorial. Shot on Hasselblad H6D 85mm f/2.0, 8K UHD, Monaco Korean duo grade, portrait 3:4 vertical.",
    "environment": "Monaco Casino terrace at night",
    "lighting": "Monaco neon violet-gold flood",
    "style": "Monaco Korean MILF duo editorial",
    "quality": "Shot on Hasselblad H6D 85mm f/2.0, 8K UHD, Monaco Korean duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_goryeo_crimson_shibuya", {
    "subject": "TWO women — Indian MILF goddess + Latina MILF bombshell, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Indian MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, dramatic waist-to-hip ratio, full rounded bust and very wide hips, warm glistening bronze skin with natural maturity — body fully covered in Korean Goryeo Buddhist art bodypaint from neck to ankle, elaborate Goryeo Buddhist painting motifs, gold Buddha haloes, lotus scrollwork and celestial beings covering entire mature body in traditional Korean Buddhist art style. RIGHT: Latina MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, extreme hourglass, impossibly tiny cinched waist, explosively wide dramatic round hips, thick powerful thighs, bronzed Latin skin with natural maturity — body fully covered in crimson-gold ultra-fine glitter coating every inch from neck to ankle, blazing liquid fire effect. LEFT: gold stiletto heels, long gold nails. RIGHT: crimson stiletto heels, long crimson nails. Both: full body high-gloss oil. Environment: Shibuya Scramble Crossing at night, neon crimson and gold advertisement floods blazing across wet pavement, urban chaos reflected in every puddle. Lighting: Shibuya neon crimson-gold flood — Goryeo Buddhist gold catching warm neon left, crimson glitter exploding fire right. Style: Shibuya Korean MILF duo editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Shibuya Korean duo grade, portrait 3:4 vertical.",
    "environment": "Shibuya Scramble Crossing at night",
    "lighting": "Shibuya neon crimson-gold flood",
    "style": "Shibuya Korean MILF duo editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Shibuya Korean duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_mugunghwa_teal_jeju_forest", {
    "subject": "TWO women — Korean MILF bust queen + Athletic MILF curvy, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean MILF bust queen, early 30s, MILF glamour physique — mature voluptuous curves, impossibly large full heavy bust dramatically dominating silhouette, extremely narrow cinched waist, luminous warm Korean golden skin with natural maturity — body fully covered in Korean Mugunghwa hibiscus tattoo from neck to ankle, national flower hibiscus blooms covering entire mature body in dense botanical tattoo style, flowers climbing from ankles to collarbone in vivid crimson and white. RIGHT: Athletic MILF curvy, early 30s, MILF glamour physique — mature voluptuous curves, perfect balance of muscle definition and mature feminine curves, defined abs with round full mature hips, bronzed warm skin with natural maturity — body fully covered in teal-to-green iridescent ultra-fine glitter coating every inch from neck to ankle, shifting teal-jade-forest. LEFT: crimson stiletto heels, long crimson nails. RIGHT: teal stiletto heels, long teal nails. Both: full body high-gloss oil. Environment: Jeju Bijarim ancient nutmeg forest at dawn, ancient tree canopy filtering soft light, moss-covered stone path, morning mist curling between ancient trunks. Lighting: soft Korean forest dawn — Mugunghwa crimson hibiscus blazing warm left, teal glitter absorbing jade forest dawn right. Style: Jeju forest MILF duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Jeju forest duo grade, portrait 3:4 vertical.",
    "environment": "Jeju Bijarim ancient nutmeg forest at dawn",
    "lighting": "soft Korean forest dawn",
    "style": "Jeju forest MILF duo editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Jeju forest duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_dokkaebi_gold_dongdaemun", {
    "subject": "TWO women — Mexican MILF hot glamour + Mediterranean MILF hot glamour, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Mexican MILF hot glamour, early 30s, MILF glamour physique — mature voluptuous curves, fiery curvaceous mature figure, dramatic hourglass, round full mature hips, bronzed warm skin with natural maturity — body fully covered in Korean Dokkaebi goblin tattoo from neck to ankle, mischievous Korean goblin spirits and supernatural folk motifs in traditional Korean folk art style covering entire mature body, goblin energy patterns blazing. RIGHT: Mediterranean MILF hot glamour, early 30s, MILF glamour physique — mature voluptuous curves, dramatically cinched narrow waist, va-va-voom wide round mature hips, full bust, warm golden skin with natural maturity — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture blazing effect. LEFT: black stiletto heels, long orange nails. RIGHT: gold stiletto heels, long gold nails. Both: full body high-gloss oil. Environment: Dongdaemun Design Plaza at night, futuristic curved DDP building blazing with LED light, Seoul night market energy, neon signs reflecting wet pavement. Lighting: DDP futuristic LED with Seoul neon — Dokkaebi folk art catching neon orange left, gold glitter blazing DDP light right. Style: Dongdaemun MILF duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, DDP Seoul duo grade, portrait 3:4 vertical.",
    "environment": "Dongdaemun Design Plaza at night",
    "lighting": "DDP futuristic LED with Seoul neon",
    "style": "Dongdaemun MILF duo editorial",
    "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, DDP Seoul duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_buncheong_violet_suncheon", {
    "subject": "TWO women — Korean MILF sophisticate + BBW MILF glamour, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean MILF sophisticate, early 30s, MILF glamour physique — mature voluptuous curves, sophisticated mature Korean beauty, wide mature hips, confident elegant presence, luminous porcelain skin with natural maturity — body fully covered in Korean Buncheong ware pottery bodypaint from neck to ankle, grey-green stoneware glaze with white slip inlay patterns, spontaneous brushwork fish and floral Joseon era ceramic motifs coating mature elegant body. RIGHT: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, extremely curvy full-figure mature silhouette, broad wide mature hips, very thick thighs, soft full rounded abdomen, abundant curves, warm caramel skin with natural maturity — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: grey stiletto heels, long jade nails. RIGHT: violet stiletto heels, long amethyst nails. Both: full body high-gloss oil. Environment: Suncheon Bay wetlands at sunset, reed marshes blazing gold, migratory birds silhouetted against crimson sky, wooden boardwalk over tidal flats. Lighting: Suncheon golden hour sunset — Buncheong grey-green catching warm sunset glow left, violet glitter absorbing crimson sunset right. Style: Suncheon MILF nature duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Suncheon Bay duo grade, portrait 3:4 vertical.",
    "environment": "Suncheon Bay wetlands at sunset",
    "lighting": "Suncheon golden hour sunset",
    "style": "Suncheon MILF nature duo editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Suncheon Bay duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_haenyeo_emerald_udo", {
    "subject": "TWO women — Polynesian MILF goddess + Mixed MILF beauty, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Polynesian MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, full heavy rounded mature hips and thighs, broad powerful shoulders, dramatically wide mature lower body, warm bronzed glowing skin with natural maturity — body fully covered in Korean Haenyeo diver tattoo from neck to ankle, iconic Jeju female diver motifs, ocean creatures, abalone and seaweed in Korean folk style celebrating sea goddess mature heritage. RIGHT: Mixed MILF beauty, early 30s, MILF glamour physique — mature voluptuous curves, model-perfect mature proportions, long lean mature legs, subtle mature feminine hourglass, glowing luminous skin with natural maturity — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: teal stiletto heels, long teal nails. RIGHT: emerald stiletto heels, long emerald nails. Both: full body high-gloss oil. Environment: Udo Island Jeju turquoise ocean cove, pristine peanut-sand beach, crystal clear shallow water, volcanic rock formations, blazing midday sun. Lighting: tropical midday sun with turquoise water reflection — Haenyeo ocean tattoo catching warm sun left, emerald glitter refracting turquoise ocean shimmer right. Style: Udo Island MILF duo editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Udo Island duo grade, portrait 3:4 vertical.",
    "environment": "Udo Island Jeju turquoise ocean cove",
    "lighting": "tropical midday sun with turquoise water reflection",
    "style": "Udo Island MILF duo editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Udo Island duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_dancheong_crimson_aurora", {
    "subject": "TWO women — Korean MILF pinup + Black MILF hourglass goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean MILF pinup, early 30s, MILF glamour physique — mature voluptuous curves, impossibly tiny corseted waist, extremely wide round heavy mature hips, maximum pinup hourglass silhouette, lush full bust, warm caramel skin with natural maturity — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid sacred geometric temple patterns in red, blue, green, gold blazing across mature dramatic curves. RIGHT: Black MILF hourglass goddess, early 30s, MILF glamour physique — mature voluptuous curves, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, very thick powerful thighs, deep luminous rich ebony skin with natural maturity — body fully covered in crimson-gold ultra-fine glitter coating every inch from neck to ankle, blazing ember fire effect. LEFT: gold stiletto heels, long crimson nails. RIGHT: crimson stiletto heels, long gold nails. Both: full body high-gloss oil. Environment: Iceland glacier at night, Aurora Borealis exploding across dark sky in electric green and violet curtains, glacial blue ice underfoot. Lighting: aurora borealis glow — Korean dancheong vivid colors blazing warm left, crimson glitter exploding fire under northern lights right. Style: Aurora Korean dancheong MILF duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora Korean duo grade, portrait 3:4 vertical.",
    "environment": "Iceland glacier at night, Aurora Borealis",
    "lighting": "aurora borealis glow",
    "style": "Aurora Korean dancheong MILF duo editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora Korean duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_gwisin_obsidian_jeonju", {
    "subject": "TWO women — Mexican MILF hot glamour + Black BBW MILF, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Mexican MILF hot glamour, early 30s, MILF glamour physique — mature voluptuous curves, fiery curvaceous mature figure, dramatic hourglass, round full mature hips, bronzed warm skin with natural maturity — body fully covered in Korean Gwisin ghost spirit tattoo from neck to ankle, ethereal Korean ghost woman in traditional ink style, long black hair spirit motifs, hauntingly beautiful Korean supernatural art covering entire mature body. RIGHT: Black BBW MILF, early 30s, MILF glamour physique — mature voluptuous curves, dramatic full-figure mature silhouette, extremely wide heavy hips, maximalist abundant mature curves, deep warm skin with natural maturity — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, void-black matte-and-shine maximum contrast. LEFT: white stiletto heels, long black nails. RIGHT: matte black stiletto heels, long black nails. Both: full body high-gloss oil. Environment: Jeonju Hanok Village at midnight, traditional Korean houses with curved tiled roofs, amber paper lanterns glowing, cobblestone alleys, full moon blazing. Lighting: midnight lantern amber with moon shadow — Gwisin ghost art catching cold moonlight left, obsidian glitter dissolving into hanok shadow right. Style: Jeonju MILF supernatural duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Jeonju hanok duo grade, portrait 3:4 vertical.",
    "environment": "Jeonju Hanok Village at midnight",
    "lighting": "midnight lantern amber with moon shadow",
    "style": "Jeonju MILF supernatural duo editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Jeonju hanok duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_minhwa_gold_yeouido", {
    "subject": "TWO women — Korean MILF natural beauty + Mediterranean MILF hot glamour, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean MILF natural beauty, early 30s, MILF glamour physique — mature voluptuous curves, very full soft natural mature bust, generously rounded chest, naturally voluptuous mature figure, warm Korean golden skin with natural maturity — body fully covered in Korean Minhwa ten longevity symbols bodypaint from neck to ankle, traditional sun, moon, mountains, water, clouds, pine, bamboo, tortoise, deer, crane symbols coating entire mature body in vivid folk painting style. RIGHT: Mediterranean MILF hot glamour, early 30s, MILF glamour physique — mature voluptuous curves, dramatically cinched narrow waist, va-va-voom wide round mature hips, full bust, warm olive skin with natural maturity — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture blazing effect. LEFT: gold stiletto heels, long jade nails. RIGHT: gold stiletto heels, long gold nails. Both: full body high-gloss oil. Environment: Yeouido Han River park at cherry blossom season night, pink sakura petals floating in night breeze, Seoul skyline blazing beyond river, bridge lights reflecting. Lighting: Seoul bridge neon with pink cherry blossom glow — Minhwa ten longevity symbols catching warm blossom light left, gold glitter blazing Seoul river neon right. Style: Yeouido MILF cherry blossom duo editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Yeouido Han River duo grade, portrait 3:4 vertical.",
    "environment": "Yeouido Han River park at cherry blossom season night",
    "lighting": "Seoul bridge neon with pink cherry blossom glow",
    "style": "Yeouido MILF cherry blossom duo editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Yeouido Han River duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_dragon_phoenix_void", {
    "subject": "TWO women — Black MILF hourglass goddess + Latina MILF bombshell, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Black MILF hourglass goddess, early 30s, MILF glamour physique — mature voluptuous curves, impossibly dramatic waist-to-hip ratio, extremely wide round mature hips, ultra-narrow waist, very thick powerful thighs, deep luminous rich ebony skin with natural maturity — body fully covered in Korean Cheongnyong azure dragon tattoo from neck to ankle, sacred blue-black dragon coiling full mature body with divine thunder clouds and fire pearls. RIGHT: Latina MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, extreme hourglass, explosively wide dramatic round mature hips, impossibly tiny waist, thick powerful thighs, bronzed Latin skin with natural maturity — body fully covered in Korean Jujak phoenix bodypaint from neck to ankle, sacred crimson phoenix in traditional Korean court painting style, fire feathers blazing across entire mature dramatic figure. LEFT: deep blue stiletto heels, long blue nails. RIGHT: crimson stiletto heels, long gold nails. Both: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, faint distant cosmic energy tendrils. Lighting: dramatic four-point void spotlight — Korean dragon azure catching cold blue rim left, Korean phoenix crimson-gold blazing warm right. Style: Vogue Italia Korean MILF dragon phoenix void duo editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Korean dragon phoenix void duo grade, portrait 3:4 vertical.",
    "environment": "pure black void",
    "lighting": "dramatic four-point void spotlight",
    "style": "Vogue Italia Korean MILF dragon phoenix void duo editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Korean dragon phoenix void duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_samshin_gold_countryside", {
    "subject": "TWO women — Korean MILF soft glamour + European MILF pinup, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: Korean MILF soft glamour, early 30s, MILF glamour physique — mature voluptuous curves, polished mature feminine curves, round soft mature hips, graceful sophisticated mature figure, warm Korean golden skin with natural maturity — body fully covered in Korean Samshin goddess bodypaint from neck to ankle, divine three-birth-goddess sacred protection symbols, divine feminine energy motifs in gold and white covering entire mature elegant body. RIGHT: European MILF pinup, early 30s, MILF glamour physique — mature voluptuous curves, impossibly tiny corseted waist, extremely wide round heavy mature hips, maximum pinup hourglass silhouette, lush full bust, luminous pale skin with natural maturity — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, molten liquid gold sculpture maximum density. LEFT: white stiletto heels, long gold nails. RIGHT: gold stiletto heels, long gold nails. Both: full body high-gloss oil. Environment: Korean countryside traditional village at golden hour, thatched roof farmhouses, golden rice paddy fields blazing in sunset light, ancient stone wall paths. Lighting: golden hour countryside warmth — Samshin divine goddess patterns blazing sacred gold left, gold glitter exploding molten sun right. Style: Korean countryside MILF duo editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Korean countryside duo grade, portrait 3:4 vertical.",
    "environment": "Korean countryside traditional village at golden hour",
    "lighting": "golden hour countryside warmth",
    "style": "Korean countryside MILF duo editorial",
    "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Korean countryside duo grade, portrait 3:4 vertical"
})

save_json("korean_milf_duo_haetae_teal_gyeongju", {
    "subject": "TWO women — BBW MILF glamour + Nordic MILF beauty, early 30s",
    "prompt": "Professional fashion photograph, full body shot. TWO women standing side by side. LEFT: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, extremely curvy full-figure mature silhouette, very broad wide mature hips, very thick thighs, soft full rounded abdomen, abundant voluptuous mature body, warm caramel skin with natural maturity — body fully covered in Korean Haetae guardian lion tattoo from neck to ankle, mythological fire-eating beast in bold Korean traditional style covering entire mature voluminous body. RIGHT: Nordic MILF beauty, early 30s, MILF glamour physique — mature voluptuous curves, tall commanding mature physique, broad strong shoulders, long lean mature legs, pale luminous arctic skin with natural maturity — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: gold stiletto heels, long black nails. RIGHT: teal stiletto heels, long violet nails. Both: full body high-gloss oil. Environment: Gyeongju Tumuli Park ancient royal tombs at dawn, grassy Silla burial mounds glowing rose-gold in morning light, cherry blossoms blooming around ancient capital. Lighting: Gyeongju rose-gold dawn — Haetae guardian catching warm dawn light left, teal glitter absorbing rose-gold dawn right. Style: Gyeongju MILF ancient duo editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Gyeongju duo grade, portrait 3:4 vertical.",
    "environment": "Gyeongju Tumuli Park ancient royal tombs at dawn",
    "lighting": "Gyeongju rose-gold dawn",
    "style": "Gyeongju MILF ancient duo editorial",
    "quality": "Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Gyeongju duo grade, portrait 3:4 vertical"
})

print("DUO-K 16종 JSON 생성 완료")
