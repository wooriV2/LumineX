import json, os, ast

PRESETS_DIR = "presets"
os.makedirs(PRESETS_DIR, exist_ok=True)

def save_json(key, data):
    path = os.path.join(PRESETS_DIR, f"{key}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ============================================================
# TRIO-K Korean MILF 20종
# ============================================================

save_json("korean_milf_trio_phoenix_celadon_crimson_changdeokgung", {
    "subject": "THREE women — African MILF carnival goddess + Korean MILF sophisticate + Latina MILF bombshell, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: African MILF carnival goddess, early 30s, MILF glamour physique — mature voluptuous curves, massive round bubble butt, extremely wide hips, narrow waist, powerfully thick thighs, bronzed deep mature skin with natural maturity — body fully covered in Korean Jujak phoenix tattoo from neck to ankle, crimson-gold sacred phoenix rising full mature body. CENTER: Korean MILF sophisticate, early 30s, MILF glamour physique — mature voluptuous curves, impeccably elegant mature figure, wide mature hips, luminous porcelain skin with natural maturity — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon with inlaid crane and cloud motifs coating mature elegant body. RIGHT: Latina MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, extreme hourglass, explosively wide dramatic hips, impossibly tiny waist, bronzed Latin skin with natural maturity — body fully covered in crimson-gold ultra-fine glitter coating every inch from neck to ankle, blazing liquid fire effect. LEFT: crimson stiletto heels, long gold nails. CENTER: jade stiletto heels, long jade nails. RIGHT: red stiletto heels, long crimson nails. All three: full body high-gloss oil. Environment: Changdeokgung Secret Garden at dawn, ancient lotus pond reflecting rose-gold light, moss paths, centuries-old pine trees glowing. Lighting: rose-gold Korean dawn — phoenix crimson blazing left, celadon jade catching dawn mist center, crimson glitter exploding fire right. Style: Changdeokgung MILF dawn trio editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Korean secret garden trio grade, portrait 3:4 vertical.",
    "environment": "Changdeokgung Secret Garden at dawn",
    "lighting": "rose-gold Korean dawn",
    "style": "Changdeokgung MILF dawn trio editorial",
    "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Korean secret garden trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_dragon_minhwa_violet_void", {
    "subject": "THREE women — Black MILF hourglass goddess + Indian MILF goddess + European MILF pinup, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Black MILF hourglass goddess, early 30s, MILF glamour physique — mature voluptuous curves, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, deep luminous ebony skin with natural maturity — body fully covered in Korean Cheongnyong azure dragon tattoo from neck to ankle, sacred blue-black dragon coiling full mature body with thunder clouds. CENTER: Indian MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, dramatic waist-to-hip ratio, full rounded bust and wide mature hips, warm bronze skin with natural maturity — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, cranes, lotus and magpies blazing across mature voluptuous curves. RIGHT: European MILF pinup, early 30s, MILF glamour physique — mature voluptuous curves, sculpted mature hourglass, full high bust, wide rounded mature hips, luminous fair skin with natural maturity — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: deep blue stiletto heels, long blue nails. CENTER: gold stiletto heels, long crimson nails. RIGHT: violet stiletto heels, long amethyst nails. All three: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic three-point chiaroscuro — Korean dragon cold blue rim left, Minhwa folk colors warm amber center, violet glitter crystalline cold right. Style: Vogue Italia Korean MILF mythology void trio editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Korean mythology void trio grade, portrait 3:4 vertical.",
    "environment": "pure black void",
    "lighting": "dramatic three-point chiaroscuro",
    "style": "Vogue Italia Korean MILF mythology void trio editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Korean mythology void trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_gumiho_lotus_emerald_haeinsa", {
    "subject": "THREE women — Korean MILF pinup + Mixed MILF beauty + Caribbean MILF goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean MILF pinup, early 30s, MILF glamour physique — mature voluptuous curves, impossibly tiny corseted waist, extremely wide round heavy mature hips, lush full bust, warm caramel skin with natural maturity — body fully covered in Korean Gumiho nine-tailed fox tattoo from neck to ankle, mystical fox spirit with nine golden tails swirling full mature body, enchanted Korean forest motifs. CENTER: Mixed MILF beauty, early 30s, MILF glamour physique — mature voluptuous curves, model-perfect mature proportions, long lean mature legs, subtle mature feminine hourglass, glowing luminous skin with natural maturity — body fully covered in Korean Buddhist lotus bodypaint from neck to ankle, sacred gold and white lotus flowers in temple painting style blooming across mature body. RIGHT: Caribbean MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, powerfully athletic bubble butt, snatched tiny waist, explosively wide round hips, muscular thick thighs, deeply bronzed skin with natural maturity — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: gold stiletto heels, long gold nails. CENTER: white stiletto heels, long coral nails. RIGHT: emerald stiletto heels, long emerald nails. All three: full body high-gloss oil. Environment: Haeinsa Temple mountain sacred forest at dawn, ancient wooden halls, morning mist through pines, sacred mountain atmosphere. Lighting: Korean mountain sacred dawn — gumiho golden tails catching dawn left, lotus gold-white blazing sacred center, emerald glitter absorbing forest light right. Style: Haeinsa MILF sacred trio editorial. Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Haeinsa trio grade, portrait 3:4 vertical.",
    "environment": "Haeinsa Temple mountain sacred forest at dawn",
    "lighting": "Korean mountain sacred dawn",
    "style": "Haeinsa MILF sacred trio editorial",
    "quality": "Shot on Leica SL2 50mm f/1.4 Summilux, 8K UHD, Haeinsa trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_haetae_pojagi_silver_bukchon", {
    "subject": "THREE women — BBW MILF glamour + Korean MILF bust queen + European MILF pinup, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, dramatic full-figure mature silhouette, extremely wide heavy hips, maximalist abundant mature curves, warm caramel skin with natural maturity — body fully covered in Korean Haetae guardian lion tattoo from neck to ankle, mythological fire-eating beast in bold Korean traditional style covering voluminous mature figure. CENTER: Korean MILF bust queen, early 30s, MILF glamour physique — mature voluptuous curves, impossibly large full heavy bust dramatically dominating silhouette, extremely narrow cinched waist, luminous Korean porcelain skin with natural maturity — body fully covered in Korean Pojagi patchwork bodypaint from neck to ankle, translucent silk patchwork jewel tones — sapphire, emerald, crimson, gold — traditional Korean wrapping cloth as living mature body art. RIGHT: European MILF pinup, early 30s, MILF glamour physique — mature voluptuous curves, sculpted mature hourglass, impossibly cinched waist, full high bust, wide rounded mature hips, porcelain skin with natural maturity — body fully covered in silver moonlight ultra-fine glitter coating every inch from neck to ankle, shifting pearl-white-silver prismatic. LEFT: gold stiletto heels, long black nails. CENTER: jewel tone stiletto heels, long ruby nails. RIGHT: silver stiletto heels, long silver nails. All three: full body high-gloss oil. Environment: Bukchon Hanok Village rooftop at night, traditional tiled roofs below, Seoul city lights glittering in distance, full moon blazing above. Lighting: moonlight with Seoul city glow — Haetae guardian catching warm amber lantern left, Pojagi jewel tones blazing stained glass center, silver glitter catching city light right. Style: Bukchon MILF luxury trio editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Bukchon trio grade, portrait 3:4 vertical.",
    "environment": "Bukchon Hanok Village rooftop at night",
    "lighting": "moonlight with Seoul city glow",
    "style": "Bukchon MILF luxury trio editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Bukchon trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_silla_dancheong_obsidian_aurora", {
    "subject": "THREE women — African MILF carnival goddess + Latina MILF bombshell + Black MILF hourglass goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: African MILF carnival goddess, early 30s, MILF glamour physique — mature voluptuous curves, massive round bubble butt, extremely wide hips, narrow waist, bronzed mature body with natural maturity — body fully covered in Silla Kingdom gold crown bodypaint from neck to ankle, ancient Silla gold crown patterns and jade comma jewels coating mature dramatic body as living art. CENTER: Latina MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, extreme hourglass, explosively wide hips, impossibly tiny waist, bronzed Latin skin with natural maturity — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid sacred geometric patterns red, blue, green, gold blazing across mature dramatic curves. RIGHT: Black MILF hourglass goddess, early 30s, MILF glamour physique — mature voluptuous curves, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, deep luminous ebony skin with natural maturity — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, void-black matte-and-shine maximum contrast. LEFT: gold stiletto heels, long gold nails. CENTER: gold stiletto heels, long crimson nails. RIGHT: matte black stiletto heels, long black nails. All three: full body high-gloss oil. Environment: Iceland glacier at night, Aurora Borealis exploding across dark sky in electric green and violet curtains, glacial blue ice underfoot. Lighting: aurora borealis glow — Silla ancient gold blazing warm left, dancheong sacred colors vivid center, obsidian glitter dissolving into void right. Style: Aurora Korean MILF trio editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora Korean trio grade, portrait 3:4 vertical.",
    "environment": "Iceland glacier at night, Aurora Borealis",
    "lighting": "aurora borealis glow",
    "style": "Aurora Korean MILF trio editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora Korean trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_mudang_celadon_crimson_jongmyo", {
    "subject": "THREE women — Mediterranean MILF hot glamour + Korean MILF sophisticate + BBW MILF glamour, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Mediterranean MILF hot glamour, early 30s, MILF glamour physique — mature voluptuous curves, dramatically cinched narrow waist, wide round mature hips, full bust, warm olive skin with natural maturity — body fully covered in Korean Mudang shaman tattoo from neck to ankle, sacred ritual symbols, spirit summoning divine shamanic patterns in red and gold blazing across mature curves. CENTER: Korean MILF sophisticate, early 30s, MILF glamour physique — mature voluptuous curves, sophisticated mature Korean beauty, elegant mature figure, luminous porcelain skin with natural maturity — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon with inlaid crane and cloud motifs coating mature elegant body. RIGHT: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, extremely curvy full-figure mature silhouette, very broad wide mature hips, very thick thighs, soft full abdomen, abundant curves, warm caramel skin with natural maturity — body fully covered in crimson-gold ultra-fine glitter coating every inch from neck to ankle, blazing ember fire effect. LEFT: crimson stiletto heels, long crimson nails. CENTER: jade stiletto heels, long jade nails. RIGHT: red stiletto heels, long gold nails. All three: full body high-gloss oil. Environment: Jongmyo Shrine at night, ancient royal ancestral hall, stone paths lined with spirit tablets, solemn moonlit atmosphere, sacred smoke rising from ritual fires. Lighting: moonlight with sacred ritual flame — Mudang shamanic red-gold catching ritual flame left, celadon jade-green catching cool moonlight center, crimson glitter blazing fire ember right. Style: Jongmyo MILF sacred trio editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Jongmyo trio grade, portrait 3:4 vertical.",
    "environment": "Jongmyo Shrine at night",
    "lighting": "moonlight with sacred ritual flame",
    "style": "Jongmyo MILF sacred trio editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Jongmyo trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_dragon_phoenix_gold_namsan", {
    "subject": "THREE women — African MILF powerhouse + Latina MILF bombshell + Korean MILF pinup, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: African MILF powerhouse, early 30s, MILF glamour physique — mature voluptuous curves, shredded defined abs combined with extremely wide round hips, thick muscular thighs, snatched waist, powerful mature physique, deep glistening skin with natural maturity — body fully covered in Korean Cheongnyong azure dragon tattoo from neck to ankle, sacred blue-black dragon coiling full powerful mature body with divine thunder clouds. CENTER: Latina MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, extreme hourglass, explosively wide hips, impossibly tiny waist, bronzed Latin skin with natural maturity — body fully covered in Korean Jujak phoenix bodypaint from neck to ankle, sacred crimson phoenix in Korean court painting style, fire feathers blazing across entire mature dramatic figure. RIGHT: Korean MILF pinup, early 30s, MILF glamour physique — mature voluptuous curves, impossibly tiny corseted waist, extremely wide round heavy mature hips, maximum pinup hourglass, warm caramel skin with natural maturity — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: deep blue stiletto heels, long blue nails. CENTER: crimson stiletto heels, long gold nails. RIGHT: gold stiletto heels, long gold nails. All three: full body high-gloss oil. Environment: Namsan Seoul Tower at night, city lights of Seoul blazing below, Han River glittering in distance, dramatic urban panorama. Lighting: Seoul neon urban panorama — Korean dragon azure catching city blue left, phoenix crimson-gold blazing warm center, gold glitter exploding Seoul neon right. Style: Namsan MILF Seoul trio editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Namsan Tower trio grade, portrait 3:4 vertical.",
    "environment": "Namsan Seoul Tower at night",
    "lighting": "Seoul neon urban panorama",
    "style": "Namsan MILF Seoul trio editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Namsan Tower trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_minhwa_lotus_teal_versailles", {
    "subject": "THREE women — Indian MILF goddess + Korean MILF bust queen + Polynesian MILF goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Indian MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, dramatic waist-to-hip ratio, full rounded bust and very wide mature hips, warm bronze skin with natural maturity — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes blazing across mature voluptuous curves in traditional Korean colors. CENTER: Korean MILF bust queen, early 30s, MILF glamour physique — mature voluptuous curves, impossibly large full heavy bust dominating silhouette, extremely narrow cinched waist, luminous warm Korean skin with natural maturity — body fully covered in Korean Buddhist lotus bodypaint from neck to ankle, sacred gold and white lotuses in temple painting style blooming across mature abundant body. RIGHT: Polynesian MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, full heavy rounded mature hips and thighs, broad powerful shoulders, dramatically wide mature lower body, warm bronzed glowing skin with natural maturity — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: gold stiletto heels, long coral nails. CENTER: gold stiletto heels, long gold nails. RIGHT: teal stiletto heels, long teal nails. All three: full body high-gloss oil. Environment: Hall of Mirrors Versailles, gilded baroque arches receding to infinity, crystal chandeliers blazing above, warm golden candlelight flooding marble floors. Lighting: warm golden candlelight — Minhwa folk colors blazing vivid left, lotus gold-white sacred center, teal glitter catching prismatic chandelier right. Style: Versailles Korean MILF trio editorial. Shot on Hasselblad H6D 110mm f/2.8, 8K UHD, Versailles Korean trio grade, portrait 3:4 vertical.",
    "environment": "Hall of Mirrors Versailles",
    "lighting": "warm golden candlelight",
    "style": "Versailles Korean MILF trio editorial",
    "quality": "Shot on Hasselblad H6D 110mm f/2.8, 8K UHD, Versailles Korean trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_gumiho_mudang_violet_shibuya", {
    "subject": "THREE women — Korean MILF sophisticate + Mexican MILF hot glamour + BBW MILF glamour, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean MILF sophisticate, early 30s, MILF glamour physique — mature voluptuous curves, sophisticated mature Korean beauty, elegant mature figure, luminous porcelain skin with natural maturity — body fully covered in Korean Gumiho nine-tailed fox tattoo from neck to ankle, mystical fox spirit with nine golden tails swirling full mature body, enchanted Korean forest motifs. CENTER: Mexican MILF hot glamour, early 30s, MILF glamour physique — mature voluptuous curves, fiery curvaceous mature figure, dramatic hourglass, round full mature hips, bronzed warm skin with natural maturity — body fully covered in Korean Mudang shaman bodypaint from neck to ankle, sacred ritual symbols, spirit summoning divine patterns in red and gold blazing across mature voluminous figure. RIGHT: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, extremely curvy full-figure mature silhouette, very broad wide mature hips, very thick thighs, soft full abdomen, abundant mature curves, deep warm skin with natural maturity — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold stiletto heels, long gold nails. CENTER: crimson stiletto heels, long crimson nails. RIGHT: violet stiletto heels, long amethyst nails. All three: full body high-gloss oil. Environment: Shibuya Scramble Crossing at night, neon gold and purple advertisement floods blazing across wet pavement, SHIBUYA 109 blazing behind, urban chaos in every puddle. Lighting: Shibuya neon gold-purple flood — gumiho golden tails catching warm neon left, mudang sacred red-gold blazing center, violet glitter exploding purple neon right. Style: Shibuya Korean MILF supernatural trio editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Shibuya Korean trio grade, portrait 3:4 vertical.",
    "environment": "Shibuya Scramble Crossing at night",
    "lighting": "Shibuya neon gold-purple flood",
    "style": "Shibuya Korean MILF supernatural trio editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Shibuya Korean trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_irezumi_celadon_crimson_busan", {
    "subject": "THREE women — BBW MILF glamour + Korean MILF sophisticate + African MILF carnival goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, extremely curvy full-figure mature silhouette, very broad wide mature hips, very thick thighs, soft full abdomen, abundant voluptuous mature curves, deep warm caramel skin with natural maturity — body fully covered in Korean-style irezumi tattoo from neck to ankle, bold Korean dragon, crane and lotus in irezumi technique covering voluminous mature figure. CENTER: Korean MILF sophisticate, early 30s, MILF glamour physique — mature voluptuous curves, impeccably elegant mature Korean figure, wide mature hips, luminous porcelain skin with natural maturity — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon glaze with inlaid crane and cloud motifs coating mature elegant body as living masterpiece. RIGHT: African MILF carnival goddess, early 30s, MILF glamour physique — mature voluptuous curves, massive round bubble butt, extremely wide hips, narrow waist, bronzed voluptuous mature body with natural maturity — body fully covered in crimson-gold ultra-fine glitter coating every inch from neck to ankle, blazing liquid fire effect. LEFT: black stiletto heels, long jade nails. CENTER: jade stiletto heels, long jade nails. RIGHT: crimson stiletto heels, long crimson nails. All three: full body high-gloss oil. Environment: Busan Gamcheon Culture Village at golden hour, colorful stacked houses cascading down hillside, golden hour blazing over Pacific ocean below, fishing boats silhouetted. Lighting: Busan golden hour sunset — Korean irezumi catching warm golden left, celadon jade catching crimson sunset center, crimson glitter exploding fire sunset right. Style: Busan MILF trio editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Busan Gamcheon trio grade, portrait 3:4 vertical.",
    "environment": "Busan Gamcheon Culture Village at golden hour",
    "lighting": "Busan golden hour sunset",
    "style": "Busan MILF trio editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Busan Gamcheon trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_phoenix_minhwa_obsidian_gwanghwamun", {
    "subject": "THREE women — Latina MILF bombshell + Indian MILF goddess + Black MILF hourglass goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Latina MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, extreme hourglass, explosively wide hips, impossibly tiny waist, thick powerful thighs, bronzed Latin skin with natural maturity — body fully covered in Korean Jujak phoenix tattoo from neck to ankle, sacred crimson-gold phoenix rising full mature body, divine fire feathers blazing across dramatic mature figure. CENTER: Indian MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, dramatic waist-to-hip ratio, full rounded bust and wide mature hips, warm bronze skin with natural maturity — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, cranes, lotus in traditional Korean colors blazing across mature voluptuous curves. RIGHT: Black MILF hourglass goddess, early 30s, MILF glamour physique — mature voluptuous curves, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, deep luminous ebony skin with natural maturity — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, void-black matte-and-shine maximum contrast. LEFT: crimson stiletto heels, long gold nails. CENTER: gold stiletto heels, long crimson nails. RIGHT: matte black stiletto heels, long black nails. All three: full body high-gloss oil. Environment: Gwanghwamun Plaza at night, illuminated Gyeongbokgung gate blazing gold behind, Admiral Yi statue silhouetted, Seoul buildings framing ancient gate, fountain blazing. Lighting: Gwanghwamun dramatic night — phoenix crimson blazing warm left, Minhwa folk colors vivid center, obsidian glitter dissolving into palace shadow right. Style: Gwanghwamun MILF trio editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Gwanghwamun trio grade, portrait 3:4 vertical.",
    "environment": "Gwanghwamun Plaza at night",
    "lighting": "Gwanghwamun dramatic night",
    "style": "Gwanghwamun MILF trio editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Gwanghwamun trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_dragon_lotus_gold_incheon", {
    "subject": "THREE women — African MILF statuesque + Mediterranean MILF hot glamour + Korean MILF pinup, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: African MILF statuesque, early 30s, MILF glamour physique — mature voluptuous curves, towering elongated mature physique, impossibly long mature legs, sharp sculpted collarbones, deep luminous skin with natural maturity — body fully covered in Korean Cheongnyong azure dragon tattoo from neck to ankle, sacred blue-black dragon coiling magnificent towering mature body with divine thunder pearls. CENTER: Mediterranean MILF hot glamour, early 30s, MILF glamour physique — mature voluptuous curves, dramatically cinched narrow waist, wide round mature hips, full bust, warm golden skin with natural maturity — body fully covered in Korean Buddhist lotus bodypaint from neck to ankle, sacred gold and white lotus flowers in temple painting style covering entire mature body. RIGHT: Korean MILF pinup, early 30s, MILF glamour physique — mature voluptuous curves, impossibly tiny corseted waist, extremely wide round heavy mature hips, maximum pinup hourglass, lush full bust, warm caramel skin with natural maturity — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: deep blue stiletto heels, long blue nails. CENTER: gold stiletto heels, long coral nails. RIGHT: gold stiletto heels, long gold nails. All three: full body high-gloss oil. Environment: Incheon International Airport grand terminal at night, soaring architectural glass ceiling blazing with light, modern Korean infrastructure grandeur. Lighting: airport architectural night light — Korean dragon azure catching cool terminal left, lotus gold blazing sacred warm center, gold glitter exploding terminal light right. Style: Incheon MILF trio editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Incheon airport trio grade, portrait 3:4 vertical.",
    "environment": "Incheon International Airport grand terminal at night",
    "lighting": "airport architectural night light",
    "style": "Incheon MILF trio editorial",
    "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Incheon airport trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_gumiho_haetae_teal_jeonju", {
    "subject": "THREE women — Korean MILF sophisticate + BBW MILF glamour + Mixed MILF beauty, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean MILF sophisticate, early 30s, MILF glamour physique — mature voluptuous curves, impeccably elegant mature Korean figure, wide mature hips, luminous porcelain skin with natural maturity — body fully covered in Korean Gumiho nine-tailed fox tattoo from neck to ankle, mystical fox spirit with nine golden tails swirling across elegant mature body. CENTER: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, dramatic full-figure mature silhouette, extremely wide heavy hips, maximalist abundant mature curves, warm caramel skin with natural maturity — body fully covered in Korean Haetae guardian lion tattoo from neck to ankle, mythological fire-eating beast in bold Korean style covering mature voluminous body. RIGHT: Mixed MILF beauty, early 30s, MILF glamour physique — mature voluptuous curves, model-perfect mature proportions, long lean mature legs, subtle mature feminine hourglass, glowing luminous skin with natural maturity — body fully covered in teal-to-violet iridescent ultra-fine glitter coating every inch from neck to ankle, aurora spectrum shifting teal-violet-green. LEFT: gold stiletto heels, long gold nails. CENTER: black stiletto heels, long orange nails. RIGHT: teal stiletto heels, long violet nails. All three: full body high-gloss oil. Environment: Jeonju Hanok Village at night, traditional Korean houses with curved tiled roofs, amber paper lanterns glowing, cobblestone alleys, full moon blazing above historic village. Lighting: Jeonju lantern amber moonlight — gumiho golden tails catching moonlight left, Haetae guardian catching warm lantern center, teal glitter absorbing cool moonlight right. Style: Jeonju MILF hanok trio editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Jeonju hanok trio grade, portrait 3:4 vertical.",
    "environment": "Jeonju Hanok Village at night",
    "lighting": "Jeonju lantern amber moonlight",
    "style": "Jeonju MILF hanok trio editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Jeonju hanok trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_silla_dancheong_emerald_versailles", {
    "subject": "THREE women — Korean MILF bust queen + African MILF carnival goddess + Polynesian MILF goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean MILF bust queen, early 30s, MILF glamour physique — mature voluptuous curves, impossibly large full heavy bust dramatically dominating silhouette, extremely narrow cinched waist, warm golden Korean skin with natural maturity — body fully covered in Silla Kingdom gold crown bodypaint from neck to ankle, ancient Silla gold crown patterns and jade comma jewels coating mature abundant body as living Silla art. CENTER: African MILF carnival goddess, early 30s, MILF glamour physique — mature voluptuous curves, massive round bubble butt, extremely wide hips, narrow waist, bronzed mature voluptuous body with natural maturity — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid sacred geometric patterns red, blue, green, gold blazing across mature dramatic figure. RIGHT: Polynesian MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, full heavy rounded mature hips and thighs, broad powerful shoulders, dramatically wide mature lower body, warm bronzed glowing skin with natural maturity — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: gold stiletto heels, long gold nails. CENTER: gold stiletto heels, long crimson nails. RIGHT: emerald stiletto heels, long emerald nails. All three: full body high-gloss oil. Environment: Hall of Mirrors Versailles, gilded baroque arches receding to infinity, crystal chandeliers blazing, warm golden candlelight flooding marble floors. Lighting: warm golden candlelight — Silla ancient gold blazing warm left, dancheong sacred colors vivid warm center, emerald glitter catching prismatic chandelier right. Style: Versailles Korean ancient MILF trio editorial. Shot on Hasselblad H6D 110mm f/2.8, 8K UHD, Versailles Korean ancient trio grade, portrait 3:4 vertical.",
    "environment": "Hall of Mirrors Versailles",
    "lighting": "warm golden candlelight",
    "style": "Versailles Korean ancient MILF trio editorial",
    "quality": "Shot on Hasselblad H6D 110mm f/2.8, 8K UHD, Versailles Korean ancient trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_dragon_gumiho_violet_dongdaemun", {
    "subject": "THREE women — Black MILF hourglass goddess + Korean MILF sophisticate + Mexican MILF hot glamour, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Black MILF hourglass goddess, early 30s, MILF glamour physique — mature voluptuous curves, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, deep luminous ebony skin with natural maturity — body fully covered in Korean Cheongnyong azure dragon tattoo from neck to ankle, sacred blue-black dragon coiling full powerful mature body with divine thunder clouds and pearls. CENTER: Korean MILF sophisticate, early 30s, MILF glamour physique — mature voluptuous curves, sophisticated mature Korean beauty, elegant mature figure, luminous porcelain skin with natural maturity — body fully covered in Korean Gumiho nine-tailed fox bodypaint from neck to ankle, mystical fox spirit with nine golden tails swirling across elegant mature body. RIGHT: Mexican MILF hot glamour, early 30s, MILF glamour physique — mature voluptuous curves, fiery curvaceous mature figure, dramatic hourglass, round full mature hips, bronzed warm skin with natural maturity — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: deep blue stiletto heels, long blue nails. CENTER: gold stiletto heels, long gold nails. RIGHT: violet stiletto heels, long amethyst nails. All three: full body high-gloss oil. Environment: Dongdaemun Design Plaza at night, futuristic curved DDP building blazing with LED light installations, Seoul night energy, neon signs reflecting wet pavement. Lighting: DDP futuristic LED with Seoul neon — Korean dragon azure catching cool DDP blue left, gumiho golden tails catching warm LED center, violet glitter absorbing DDP purple right. Style: Dongdaemun DDP MILF trio editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, DDP Seoul trio grade, portrait 3:4 vertical.",
    "environment": "Dongdaemun Design Plaza at night",
    "lighting": "DDP futuristic LED with Seoul neon",
    "style": "Dongdaemun DDP MILF trio editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, DDP Seoul trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_haenyeo_dragon_gold_void", {
    "subject": "THREE women — Polynesian MILF goddess + African MILF statuesque + African MILF carnival goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Polynesian MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, full heavy rounded mature hips and thighs, broad powerful shoulders, dramatically wide mature lower body, warm bronzed glowing skin with natural maturity — body fully covered in Korean Haenyeo diver tattoo from neck to ankle, Jeju female diver motifs, ocean creatures, abalone and seaweed in Korean folk style celebrating mature sea goddess heritage. CENTER: African MILF statuesque, early 30s, MILF glamour physique — mature voluptuous curves, towering elongated mature physique, impossibly long mature legs, sharp sculpted collarbones, deep luminous skin with natural maturity — body fully covered in Korean Cheongnyong azure dragon tattoo from neck to ankle, sacred blue-black dragon coiling magnificent towering mature body with divine thunder pearls. RIGHT: African MILF carnival goddess, early 30s, MILF glamour physique — mature voluptuous curves, massive round bubble butt, extremely wide hips, narrow waist, bronzed voluptuous mature body with natural maturity — body fully covered in 24k gold ultra-fine glitter coating every inch from neck to ankle, liquid gold sculpture maximum density. LEFT: teal stiletto heels, long teal nails. CENTER: deep blue stiletto heels, long blue nails. RIGHT: gold stiletto heels, long gold nails. All three: full body high-gloss oil. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic three-point void spotlight — Haenyeo ocean tattoo catching cool blue rim left, Korean dragon azure catching cold spotlight center, gold glitter exploding strobe right. Style: Vogue Italia Korean MILF sea void trio editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Korean void trio grade, portrait 3:4 vertical.",
    "environment": "pure black void",
    "lighting": "dramatic three-point void spotlight",
    "style": "Vogue Italia Korean MILF sea void trio editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, Korean void trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_minhwa_pojagi_obsidian_bukhansan", {
    "subject": "THREE women — Mediterranean MILF hot glamour + Korean MILF bust queen + Black MILF hourglass goddess, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Mediterranean MILF hot glamour, early 30s, MILF glamour physique — mature voluptuous curves, dramatically cinched narrow waist, wide round mature hips, full bust, warm olive skin with natural maturity — body fully covered in Korean Minhwa folk art bodypaint from neck to ankle, vivid folk tigers, magpies, lotus and cranes in traditional Korean colors blazing across mature curves. CENTER: Korean MILF bust queen, early 30s, MILF glamour physique — mature voluptuous curves, impossibly large full heavy bust dominating silhouette, extremely narrow cinched waist, luminous warm Korean skin with natural maturity — body fully covered in Korean Pojagi patchwork bodypaint from neck to ankle, translucent silk patchwork jewel tones — sapphire, emerald, crimson, gold — traditional Korean wrapping cloth as living mature body art. RIGHT: Black MILF hourglass goddess, early 30s, MILF glamour physique — mature voluptuous curves, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, deep luminous ebony skin with natural maturity — body fully covered in obsidian black ultra-fine glitter coating every inch from neck to ankle, void-black matte-and-shine maximum contrast. LEFT: gold stiletto heels, long crimson nails. CENTER: jewel tone stiletto heels, long ruby nails. RIGHT: matte black stiletto heels, long black nails. All three: full body high-gloss oil. Environment: Bukhansan mountain granite summit at night, dramatic rock formations silhouetted against star-blazing sky, Seoul city lights blazing far below. Lighting: mountain starlight with Seoul city glow below — Minhwa folk colors catching starlight left, Pojagi jewel tones blazing stained glass center, obsidian glitter dissolving into mountain darkness right. Style: Bukhansan MILF mountain night trio editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Bukhansan night trio grade, portrait 3:4 vertical.",
    "environment": "Bukhansan mountain granite summit at night",
    "lighting": "mountain starlight with Seoul city glow below",
    "style": "Bukhansan MILF mountain night trio editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Bukhansan night trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_tiger_phoenix_crimson_gyeongju", {
    "subject": "THREE women — Latina MILF bombshell + Black MILF hourglass goddess + BBW MILF glamour, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Latina MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, extreme hourglass, explosively wide hips, impossibly tiny waist, thick powerful thighs, bronzed Latin skin with natural maturity — body fully covered in Korean Baekho white tiger tattoo from neck to ankle, fierce guardian Silla-era tiger in bold Minhwa folk style blazing across dramatic mature figure. CENTER: Black MILF hourglass goddess, early 30s, MILF glamour physique — mature voluptuous curves, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, deep luminous ebony skin with natural maturity — body fully covered in Korean Jujak phoenix bodypaint from neck to ankle, sacred crimson phoenix in Korean court painting style blazing fire feathers across powerful mature figure. RIGHT: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, extremely curvy full-figure mature silhouette, very broad wide mature hips, very thick thighs, soft full abdomen, abundant mature curves, warm caramel skin with natural maturity — body fully covered in crimson-gold ultra-fine glitter coating every inch from neck to ankle, blazing ember liquid fire effect. LEFT: white stiletto heels, long crimson nails. CENTER: crimson stiletto heels, long gold nails. RIGHT: red stiletto heels, long crimson nails. All three: full body high-gloss oil. Environment: Gyeongju Tumuli Park ancient royal tombs at dawn, grassy Silla burial mounds glowing rose-gold in morning light, cherry blossoms blooming around ancient capital. Lighting: Gyeongju rose-gold dawn — white tiger catching cold dawn left, phoenix crimson blazing warm center, crimson glitter exploding fire ember right. Style: Gyeongju MILF ancient trio editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Gyeongju trio grade, portrait 3:4 vertical.",
    "environment": "Gyeongju Tumuli Park ancient royal tombs at dawn",
    "lighting": "Gyeongju rose-gold dawn",
    "style": "Gyeongju MILF ancient trio editorial",
    "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Gyeongju trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_celadon_samshin_emerald_suncheon", {
    "subject": "THREE women — BBW MILF glamour + Korean MILF soft glamour + Mixed MILF beauty, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: BBW MILF glamour, early 30s, MILF glamour physique — mature voluptuous curves, extremely curvy full-figure mature silhouette, very broad wide mature hips, very thick thighs, soft full abdomen, abundant voluptuous mature body, deep warm skin with natural maturity — body fully covered in Korean Goryeo celadon bodypaint from neck to ankle, jade-green celadon glaze with inlaid crane and cloud motifs coating mature voluminous body as living Goryeo masterpiece. CENTER: Korean MILF soft glamour, early 30s, MILF glamour physique — mature voluptuous curves, polished mature feminine curves, round soft mature hips, graceful sophisticated mature figure, warm Korean golden skin with natural maturity — body fully covered in Korean Samshin goddess bodypaint from neck to ankle, divine three-birth-goddess sacred protection symbols in gold and white covering entire mature elegant body. RIGHT: Mixed MILF beauty, early 30s, MILF glamour physique — mature voluptuous curves, model-perfect mature proportions, long lean mature legs, subtle mature feminine hourglass, glowing luminous skin with natural maturity — body fully covered in emerald forest ultra-fine glitter coating every inch from neck to ankle, shifting emerald-jade crystalline. LEFT: jade stiletto heels, long jade nails. CENTER: gold stiletto heels, long white nails. RIGHT: emerald stiletto heels, long emerald nails. All three: full body high-gloss oil. Environment: Suncheon Bay wetlands at golden hour, reed marshes blazing gold, migratory birds soaring, wooden boardwalk over tidal flats, crimson sunset sky. Lighting: Suncheon golden hour wetland sunset — celadon jade catching warm sunset left, Samshin divine gold blazing sacred center, emerald glitter absorbing crimson wetland sunset right. Style: Suncheon Bay MILF nature trio editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Suncheon Bay trio grade, portrait 3:4 vertical.",
    "environment": "Suncheon Bay wetlands at golden hour",
    "lighting": "Suncheon golden hour wetland sunset",
    "style": "Suncheon Bay MILF nature trio editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, Suncheon Bay trio grade, portrait 3:4 vertical"
})

save_json("korean_milf_trio_gumiho_dancheong_violet_gyeongbokgung", {
    "subject": "THREE women — African MILF carnival goddess + Indian MILF goddess + Latina MILF bombshell, early 30s",
    "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: African MILF carnival goddess, early 30s, MILF glamour physique — mature voluptuous curves, massive round bubble butt, extremely wide hips, narrow waist, bronzed voluptuous mature body with natural maturity — body fully covered in Korean Gumiho nine-tailed fox tattoo from neck to ankle, mystical fox spirit with nine golden tails swirling across mature dramatic figure. CENTER: Indian MILF goddess, early 30s, MILF glamour physique — mature voluptuous curves, dramatic waist-to-hip ratio, full rounded bust and wide mature hips, warm bronze skin with natural maturity — body fully covered in Korean dancheong temple bodypaint from neck to ankle, vivid sacred geometric patterns red, blue, green, gold blazing across mature voluptuous curves. RIGHT: Latina MILF bombshell, early 30s, MILF glamour physique — mature voluptuous curves, extreme hourglass, explosively wide hips, impossibly tiny waist, bronzed Latin skin with natural maturity — body fully covered in deep violet amethyst ultra-fine glitter coating every inch from neck to ankle, crystalline shifting amethyst-violet-indigo. LEFT: gold stiletto heels, long gold nails. CENTER: gold stiletto heels, long crimson nails. RIGHT: violet stiletto heels, long amethyst nails. All three: full body high-gloss oil. Environment: Gyeongbokgung Palace Hyangwonjeong pavilion at night, hexagonal pavilion reflected in moonlit pond, stone lanterns glowing amber, lotus leaves floating in dark water. Lighting: Gyeongbokgung moonlit pond reflection — gumiho golden tails catching moonlight left, dancheong sacred colors blazing warm center, violet glitter absorbing cool pond reflection right. Style: Gyeongbokgung pavilion MILF trio editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Gyeongbokgung pavilion trio grade, portrait 3:4 vertical.",
    "environment": "Gyeongbokgung Palace Hyangwonjeong pavilion at night",
    "lighting": "Gyeongbokgung moonlit pond reflection",
    "style": "Gyeongbokgung pavilion MILF trio editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Gyeongbokgung pavilion trio grade, portrait 3:4 vertical"
})

print("TRIO-K 20종 JSON 생성 완료")

# ============================================================
# HOF 패치
# ============================================================
HOF_KEYS = [
    # I/J 이레즈미 HOF 7종
    "irezumi_skull_chrysanthemum_vs_angel_aurora",
    "irezumi_skull_chrysanthemum_hot_glam_versailles",
    "irezumi_skull_chrysanthemum_sports_glam_void",
    "irezumi_skull_chrysanthemum_slim_runway_monaco",
    "irezumi_koi_maple_black_glam_void",
    "irezumi_koi_maple_vs_angel_aurora",
    "irezumi_koi_maple_ballerina_kyoto",
    # DUO-K HOF 3종
    "korean_milf_duo_dokkaebi_gold_dongdaemun",
    "korean_milf_duo_dancheong_crimson_aurora",
    "korean_milf_duo_gwisin_obsidian_jeonju",
    # TRIO-K HOF 10종
    "korean_milf_trio_dragon_minhwa_violet_void",
    "korean_milf_trio_silla_dancheong_obsidian_aurora",
    "korean_milf_trio_mudang_celadon_crimson_jongmyo",
    "korean_milf_trio_dragon_phoenix_gold_namsan",
    "korean_milf_trio_irezumi_celadon_crimson_busan",
    "korean_milf_trio_phoenix_minhwa_obsidian_gwanghwamun",
    "korean_milf_trio_dragon_gumiho_violet_dongdaemun",
    "korean_milf_trio_minhwa_pojagi_obsidian_bukhansan",
    "korean_milf_trio_tiger_phoenix_crimson_gyeongju",
    "korean_milf_trio_gumiho_dancheong_violet_gyeongbokgung",
]

with open("core/hof_tier.py", encoding="utf-8-sig") as f:
    content = f.read()
added_hof = 0
for key in HOF_KEYS:
    if f'"{key}"' not in content:
        content = content.rstrip()
        content += f'\n    "{key}",'
        added_hof += 1
with open("core/hof_tier.py", "w", encoding="utf-8") as f:
    f.write(content)
print(f"HOF 패치: {added_hof}종 추가")

# ============================================================
# SSS 패치
# ============================================================
SSS_KEYS = [
    # DUO-K SSS 8종
    "korean_milf_duo_mudang_crimson_jongmyo",
    "korean_milf_duo_tanghwa_emerald_monaco",
    "korean_milf_duo_goryeo_crimson_shibuya",
    "korean_milf_duo_buncheong_violet_suncheon",
    "korean_milf_duo_minhwa_gold_yeouido",
    "korean_milf_duo_dragon_phoenix_void",
    "korean_milf_duo_samshin_gold_countryside",
    "korean_milf_duo_haetae_teal_gyeongju",
    # TRIO-K SSS 8종
    "korean_milf_trio_phoenix_celadon_crimson_changdeokgung",
    "korean_milf_trio_gumiho_lotus_emerald_haeinsa",
    "korean_milf_trio_haetae_pojagi_silver_bukchon",
    "korean_milf_trio_gumiho_mudang_violet_shibuya",
    "korean_milf_trio_dragon_lotus_gold_incheon",
    "korean_milf_trio_gumiho_haetae_teal_jeonju",
    "korean_milf_trio_haenyeo_dragon_gold_void",
    "korean_milf_trio_celadon_samshin_emerald_suncheon",
]

with open("core/sss_tier.py", encoding="utf-8-sig") as f:
    content = f.read()
added_sss = 0
for key in SSS_KEYS:
    if f'"{key}"' not in content:
        content = content.rstrip()
        if content.endswith("}"):
            content = content[:-1].rstrip()
            content += f'\n    "{key}",\n' + "}"
        else:
            content += f'\n    "{key}",'
        added_sss += 1
with open("core/sss_tier.py", "w", encoding="utf-8") as f:
    f.write(content)
print(f"SSS 패치: {added_sss}종 추가")

# ============================================================
# AST 검증
# ============================================================
for fname in ["core/presets_meta.py", "core/hof_tier.py", "core/sss_tier.py"]:
    ast.parse(open(fname, encoding="utf-8").read())
print("AST 검증: OK")
print("전체 완료!")
