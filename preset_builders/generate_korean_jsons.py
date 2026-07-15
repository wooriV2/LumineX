# -*- coding: utf-8 -*-
"""
LumineX — 한국인 신규 카테고리 JSON 생성
K-Idol / Mature Goddess / Elder Goddess / Fitness Model

실행:
  $env:PYTHONUTF8 = "1"
  python preset_builders/generate_korean_jsons.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path(__file__).parent.parent / "presets"
PRESETS_DIR.mkdir(exist_ok=True)

# ── 프리셋 정의 ──────────────────────────────────────────

PRESETS = {

    # ── 🎤 K-Idol ──────────────────────────────────────
    "korean_idol_gangnam_latex": {
        "subject": "K-pop idol goddess, slim perfect stage figure, early-20s, Korean features, warm porcelain skin, long straight jet-black hair sleek center-part, bold graphic eye makeup, fierce expression",
        "outfit": "ultra-minimal black latex micro stage bodysuit, latex vacuum-tight on slim idol frame, bodysuit cut high on perfect thighs, black patent thigh-high platform stiletto boots 6-inch heel, silver chain statement belt, silver geometric ear cuffs",
        "environment": "Gangnam luxury nightclub interior, LED stage lighting in electric blue and pink washing over idol figure, mirror disco ball fragments above, dark luxury crowd blur behind",
        "lighting": "stage LED blue-pink from above + mirror ball scattered light from all directions, porcelain skin in stage color wash, black latex catching every stage light as hard reflection",
        "style": "K-pop idol Gangnam latex stage night editorial, idol perfection commanding luxury club",
        "quality": "Shot on Hasselblad X2D, 8K UHD, K-idol stage grade, portrait 2:3 vertical",
    },
    "korean_idol_holographic_stage": {
        "subject": "K-pop idol goddess, slim perfect stage figure, early-20s, Korean features, luminous porcelain skin, long straight dark hair with holographic silver highlights, sharp dramatic stage makeup, fierce idol expression mid-performance",
        "outfit": "ultra-minimal holographic iridescent micro stage dress, rainbow shift on every movement, dress micro-short on slim perfect thighs, clear platform stiletto boots 6-inch heel with holographic LED sole, holographic geometric choker, holographic arm cuffs",
        "environment": "massive K-pop concert arena stage, holographic projections surrounding figure, laser beams cutting through fog machine haze, 50000-seat arena crowd blur in background",
        "lighting": "holographic stage projections from all directions + laser grid from above + fan light sticks creating ocean of light behind, luminous skin in holographic rainbow wash, iridescent dress exploding in multi-color from every angle",
        "style": "K-pop idol holographic arena concert stage editorial, idol goddess in holographic light spectacle",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, K-idol holographic grade, portrait 2:3 vertical",
    },
    "korean_idol_bukchon_morning": {
        "subject": "K-pop idol goddess, slim perfect figure, early-20s, Korean features, natural dewy porcelain skin, long soft dark waves loose in morning light, minimal fresh makeup, pure innocent expression, morning idol off-duty",
        "outfit": "ultra-minimal white linen micro slip dress, thin spaghetti straps, dress riding softly on slim perfect figure, white platform sandal mules 4-inch on Bukchon stone path, single delicate gold chain, tiny gold stud earrings",
        "environment": "Bukchon Hanok Village Seoul, traditional Korean tile rooftops cascading down hill behind, morning golden mist over hanok walls, stone path, hanji lantern visible, cherry blossom branch",
        "lighting": "Seoul morning golden from low horizon through hanok rooftop gaps, dewy porcelain skin in pure morning gold, white linen dress ethereal in morning haze",
        "style": "K-pop idol Bukchon hanok morning pure editorial, idol goddess in traditional Korean morning gold",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Bukchon morning grade, portrait 2:3 vertical",
    },
    "korean_idol_cyber_dongdaemun": {
        "subject": "K-pop idol goddess, slim perfect stage figure, early-20s, Korean features, warm honey-porcelain skin, blunt-cut silver-dyed bob, sharp graphic eye makeup with neon liner, fierce futuristic expression",
        "outfit": "ultra-minimal silver chrome micro structured bodysuit, futuristic panel construction barely covering slim frame, silver thigh-high platform stiletto boots 6-inch heel on DDP curved surface, neon pink geometric ear cuffs, chrome arm sleeve one side only",
        "environment": "Dongdaemun Design Plaza Seoul exterior night, DDP massive curved white aluminum surface behind, LED neon lighting on DDP architecture, Seoul night skyline, neon signs in Korean characters",
        "lighting": "DDP LED white from curved surface behind + neon pink-blue from Seoul signs surrounding, honey-porcelain skin in neon wash, chrome bodysuit catching DDP white as mirror on slim frame",
        "style": "K-pop idol Dongdaemun DDP cyber future editorial, idol goddess commanding futuristic Seoul architecture",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, cyber Seoul grade, portrait 2:3 vertical",
    },
    "korean_idol_jeju_ocean": {
        "subject": "K-pop idol goddess, slim perfect figure, early-20s, Korean features, warm golden porcelain skin kissed by Jeju sun, long dark hair wild in ocean wind, natural fresh makeup, expression free and joyful on Jeju coast",
        "outfit": "ultra-minimal white micro string bikini, minimal coverage on slim idol figure, bare feet on Jeju black volcanic rock, single delicate gold anklet, tiny gold hoop earrings",
        "environment": "Jeju Island volcanic coastline, dramatic black basalt columns and smooth volcanic rock formations, turquoise East Sea waves crashing below, clear blue sky",
        "lighting": "Jeju midday direct from above + turquoise ocean reflection upward from crashing waves, golden porcelain skin in perfect coastal dual light, white bikini against black volcanic rock maximum contrast",
        "style": "K-pop idol Jeju volcanic coast ocean natural editorial, idol goddess free on Jeju black rock paradise",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Jeju ocean grade, portrait 2:3 vertical",
    },

    # ── 👵 Mature Goddess ──────────────────────────────
    "mature_korean_silver_penthouse": {
        "subject": "Korean mature goddess, supreme hourglass figure with full feminine curves, late-40s, Korean features, warm honey-porcelain skin luminous and flawless, striking floor-length silver-white hair sleek and commanding, refined bold makeup, powerful mature expression",
        "outfit": "ultra-minimal black micro string bikini top, matching micro thong, black patent thigh-high platform stiletto boots 6-inch heel, single architectural silver choker, silver cuff",
        "environment": "Seoul luxury penthouse terrace, Han River city gold panorama below, Namsan Tower in distance, glass railing, full night city",
        "lighting": "Seoul city gold ambient from panorama + single hard key front, silver hair catching gold city light creating silver-gold halo, honey skin warm in city gold",
        "style": "Korean mature goddess silver hair Seoul penthouse night editorial, silver-white hair commanding Seoul skyline",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Seoul mature silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_onsen": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, warm porcelain skin dewy in onsen steam, dramatic floor-length silver-white hair loose and flowing in steam, serene powerful expression",
        "outfit": "ultra-minimal white silk micro slip, translucent in steam revealing mature curves, white platform geta 4-inch on hinoki wood, single silver jade drop earring, silver bracelet",
        "environment": "private ryokan hinoki onsen, steam rising from hot spring, bamboo lanterns, maple leaves, window to autumn forest",
        "lighting": "stone lantern warm amber + steam diffusing all light softly, porcelain skin warm in onsen amber, silver hair catching amber as warm silver-gold cascade in steam",
        "style": "Korean mature goddess silver hair ryokan onsen steam editorial, silver flowing in onsen mist",
        "quality": "Shot on Hasselblad X2D, 8K UHD, onsen silver steam grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_paris_window": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, luminous porcelain skin in Paris morning light, architectural silver-white hair in sleek chignon, refined editorial expression",
        "outfit": "ultra-minimal ivory satin slip dress, thin straps, dress draping on full mature curves, ivory platform stiletto mules 5-inch on herringbone parquet, single pearl drop earring, delicate silver chain",
        "environment": "classic Haussmann Paris apartment, tall French windows open to zinc rooftops, morning golden light flooding through sheer curtains, wrought iron balcony, cafe au lait on marble table",
        "lighting": "Paris morning gold through tall French windows from side, luminous skin in Paris morning warmth, silver chignon catching morning gold as warm silver luminescence",
        "style": "Korean mature goddess silver hair Paris morning window editorial, silver chignon in Paris golden morning",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Paris morning silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_dubai_pool": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, golden-honey skin oiled and gleaming in Dubai sun, long straight silver-white hair wild in desert wind, fierce commanding expression",
        "outfit": "ultra-minimal cobalt blue micro string bikini top barely containing full mature bust, matching micro thong, cobalt blue patent platform stiletto wedge 5-inch at infinity pool edge, gold layered necklaces, gold arm cuff",
        "environment": "Dubai luxury hotel infinity pool, Burj Khalifa dominating frame behind, blue pool water reflecting Dubai sky, desert afternoon gold total",
        "lighting": "Dubai direct afternoon sun from above + pool turquoise reflection from below, golden-honey skin in dual light, silver hair blazing in Dubai gold as platinum fire",
        "style": "Korean mature goddess silver hair Dubai infinity pool editorial, silver-white in Dubai gold and blue",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Dubai pool silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_void_studio": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, porcelain skin cold and perfect in void light, severe sleek center-part silver-white hair straight to waist, cold commanding editorial expression",
        "outfit": "ultra-minimal black micro string bikini, black patent thigh-high platform stiletto boots 6-inch heel, single silver geometric ear cuff only",
        "environment": "black infinity studio, single hard overhead spot, pure editorial void total",
        "lighting": "single hard overhead spot from above only, silver hair catching as blinding silver shaft in darkness, porcelain skin cold in chiaroscuro, supreme hourglass silhouette absolute against void",
        "style": "Korean mature goddess silver hair black void studio editorial, silver-white hair as light source in darkness",
        "quality": "Shot on Hasselblad X2D, 8K UHD, void silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_bali_temple": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, warm golden-olive skin in Bali temple light, long loose silver-white hair with frangipani flower tucked in, serene commanding expression",
        "outfit": "ultra-minimal deep gold micro string bikini, matching micro thong, gold platform sandal wedge 5-inch on Bali stone, layered gold chains, gold coin drop earrings",
        "environment": "Bali Hindu temple interior, intricate stone carved walls with moss, temple lanterns casting warm amber, incense smoke, tropical flowers scattered",
        "lighting": "temple lantern warm amber from multiple positions, incense smoke diffusing light, golden-olive skin blazing in Bali amber, silver hair catching amber as warm gold-silver in temple warmth",
        "style": "Korean mature goddess silver hair Bali temple amber editorial, silver-white in sacred Bali amber",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Bali temple amber grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_newyork_rooftop": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, warm honey skin in NYC night air, sleek silver-white hair in high architectural ponytail, fierce power expression",
        "outfit": "ultra-minimal red metallic micro string bikini, micro thong, red patent thigh-high platform stiletto boots 6-inch heel on NYC rooftop, red lips matching bikini, gold chain belt, gold ear cuffs",
        "environment": "New York City rooftop at night, Empire State Building lit behind, Manhattan grid blazing gold below, water tower silhouettes, full NYC panorama",
        "lighting": "NYC city gold ambient from grid below + Empire State spotlight from behind, honey skin in NYC warm gold, silver ponytail catching city light as silver-gold streak against Manhattan",
        "style": "Korean mature goddess silver hair NYC rooftop power editorial, silver ponytail commanding Manhattan night",
        "quality": "Shot on Hasselblad X2D, 8K UHD, NYC silver night grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_jeju_cliff": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, golden skin in Jeju coastal wind, long silver-white hair dramatically wind-swept horizontal, free powerful expression",
        "outfit": "ultra-minimal white micro string bikini, micro thong, bare feet on Jeju black volcanic cliff edge, single delicate silver anklet, silver hoop earrings",
        "environment": "Jeju Island coastal cliff, black basalt columns below, turquoise East Sea stretching to horizon, sky meeting sea, strong ocean wind",
        "lighting": "Jeju midday coastal from above + turquoise ocean reflection upward, golden skin in coastal dual light, silver hair streaming horizontal in wind catching all light as silver banner against Jeju blue",
        "style": "Korean mature goddess silver hair Jeju cliff wind editorial, silver streaming in Jeju ocean wind",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Jeju cliff silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_kyoto_bamboo": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, porcelain skin cool in bamboo dappled light, long straight silver-white hair loose, serene commanding expression",
        "outfit": "ultra-minimal sage green silk micro slip dress, thin straps, dress fluid on mature curves, sage green platform geta 4-inch on bamboo path, single jade drop earring, jade bracelet",
        "environment": "Kyoto Arashiyama bamboo grove, towering bamboo columns creating green cathedral above, dappled morning light through bamboo canopy, mist between bamboo trunks",
        "lighting": "dappled bamboo morning from above through canopy + cool green ambient from bamboo walls, porcelain skin in cool green dapple, silver hair catching green light as silver-green luminescence in bamboo",
        "style": "Korean mature goddess silver hair Kyoto bamboo grove editorial, silver-white against green bamboo cathedral",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Kyoto bamboo silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_london_rain": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, porcelain skin luminous in London rain, silver-white hair damp and dramatic in rain, cold fierce expression",
        "outfit": "ultra-minimal black leather micro corset top barely containing full bust, matching micro shorts, black patent thigh-high platform stiletto boots 6-inch heel in London rain puddle, black umbrella held low as prop, silver geometric ear cuffs",
        "environment": "London street in heavy rain, classic red double-decker bus blurred behind, wet cobblestone reflecting streetlamp gold, Big Ben in foggy distance, rain falling in sheets",
        "lighting": "London streetlamp warm gold from above + rain puddle reflection from below + rain scatter, porcelain skin cold in London rain gold, silver hair wet and catching streetlamp as molten silver in rain",
        "style": "Korean mature goddess silver hair London rain editorial, wet silver in London gold rain",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, London rain silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_maldives_overwater": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, golden-honey skin oiled in Maldives sun, long silver-white hair loose in ocean breeze, expression free and powerful",
        "outfit": "ultra-minimal turquoise micro string bikini top barely containing full mature bust, matching micro thong, turquoise platform stiletto wedge sandal 5-inch on overwater bungalow deck, layered silver chains, turquoise drop earrings",
        "environment": "Maldives overwater bungalow, turquoise Indian Ocean extending to horizon in every direction, water villa deck, coral below visible through crystal water, golden afternoon light",
        "lighting": "Maldives direct afternoon sun + turquoise ocean reflection from all water surrounding deck, golden-honey skin blazing in Maldives dual light, silver hair in turquoise-gold Maldives atmosphere",
        "style": "Korean mature goddess silver hair Maldives overwater editorial, silver-white over Maldives turquoise infinity",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Maldives turquoise silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_milan_fashion": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, porcelain skin flawless in runway light, severe architectural silver-white hair in extreme sculptural updo, cold high fashion editorial expression",
        "outfit": "ultra-minimal black structured micro bodysuit, architectural panel construction, matching micro thong visible, black platform stiletto boots 6-inch heel on Milan runway, single massive silver architectural ear sculpture, no other accessories",
        "environment": "Milan Fashion Week runway, white runway extending to infinity, fashion crowd blur on both sides, designer label backdrop, dramatic runway spotlights from above",
        "lighting": "runway overhead spots from above creating hard fashion light, porcelain elder skin in runway white hard light, silver sculptural updo catching runway light as architectural silver crown",
        "style": "Korean mature goddess silver hair Milan runway high fashion editorial, silver architectural updo as runway crown",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Milan runway silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_istanbul_hammam": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, porcelain skin luminous in hammam steam, long silver-white hair damp and loose in steam, serene commanding expression",
        "outfit": "ultra-minimal white marble-patterned micro wrap, marble texture on full mature curves, bare feet on Ottoman marble floor, single hammered silver cuff, silver hoop earrings",
        "environment": "Istanbul historic hammam, massive marble columns, domed ceiling with star-shaped light holes creating constellation of golden light beams, steam rising from marble floor, Ottoman tile detail",
        "lighting": "constellation light beams from dome above through star holes + steam diffusing and multiplying light, porcelain skin in golden beam constellation through steam, silver hair catching dome light beams as silver constellation in hammam",
        "style": "Korean mature goddess silver hair Istanbul hammam marble steam editorial, silver in Ottoman constellation light",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Istanbul hammam silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_rio_carnival": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, golden-bronze skin in Rio carnival light, massive silver-white hair in dramatic carnival plume upstyle with feathers, fierce joyful carnival expression",
        "outfit": "ultra-minimal silver sequin micro carnival bikini barely containing full mature curves, matching micro thong, silver platform stiletto carnival heels 6-inch, silver feather body accessory on hips, massive silver statement earrings",
        "environment": "Rio de Janeiro Sambadrome carnival night, samba school floats blazing in all colors behind, confetti in air, carnival crowd in costumes, total color explosion",
        "lighting": "carnival float lights from all directions in rainbow saturation, golden-bronze skin in carnival color explosion, silver carnival crown catching every carnival color",
        "style": "Korean mature goddess silver hair Rio carnival editorial, silver crown in carnival color chaos",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Rio carnival silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_alaska_aurora": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, porcelain skin cold and perfect in aurora light, long straight silver-white hair loose in arctic wind, awe-struck powerful expression",
        "outfit": "ultra-minimal silver chrome micro string bikini, micro thong, silver chrome thigh-high platform stiletto boots 6-inch heel on Alaska snow, silver fur stole draped over shoulders only, crystal drop earrings",
        "environment": "Alaska wilderness, massive aurora borealis in green-purple-blue filling entire sky above, snow field, pine silhouettes, frozen lake reflection below",
        "lighting": "aurora green-purple-blue from sky filling entire scene + snow reflection from below, porcelain skin in aurora color wash, silver hair catching aurora as multi-color silver aurora mirror",
        "style": "Korean mature goddess silver hair Alaska aurora editorial, silver-white as aurora mirror in arctic",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Alaska aurora silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_tokyo_shibuya": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, warm honey-porcelain skin in Tokyo neon, sleek silver-white hair in severe high bun with neon-lit strands escaping, fierce mature expression",
        "outfit": "ultra-minimal electric pink micro string bikini, micro thong, electric pink patent thigh-high platform stiletto boots 6-inch heel in Shibuya puddles, silver geometric ear cuffs, silver arm band",
        "environment": "Shibuya crossing at night, full neon saturation from all signs, rain puddles reflecting neon rainbow below boots, crowds with umbrellas blurred behind",
        "lighting": "full Tokyo neon rainbow from all Shibuya signs + neon puddle reflection from below, honey skin in neon color saturation, silver bun catching all neon colors as silver neon prism",
        "style": "Korean mature goddess silver hair Shibuya neon night editorial, silver bun as neon prism in Shibuya chaos",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Shibuya neon silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_sahara_sunset": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, golden-bronze skin in Sahara sun, long loose silver-white hair in Sahara wind, expression fierce and free",
        "outfit": "ultra-minimal burnt orange micro string bikini, micro thong, gold platform sandal wedge 5-inch on Sahara sand dune crest, layered gold chains, gold drop earrings, gold arm cuff",
        "environment": "Sahara desert at golden sunset, massive sand dune crests in deep orange-gold, sun on horizon blazing, camel silhouette in distance, orange sky meeting sand",
        "lighting": "Sahara setting sun low from horizon, golden-bronze skin in extreme warm orange-gold, silver hair catching Sahara sunset as blazing silver-orange fire against dune",
        "style": "Korean mature goddess silver hair Sahara sunset editorial, silver-white as silver fire in Sahara orange gold",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Sahara sunset silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_monaco_yacht": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, golden Mediterranean skin on Monaco yacht, silver-white hair in relaxed low side braid with sea wind, commanding luxe expression",
        "outfit": "ultra-minimal navy micro string bikini top barely containing full mature bust, matching micro thong, navy patent platform stiletto mules 5-inch on yacht deck, layered gold Mediterranean chains, gold anchor drop earrings",
        "environment": "Monaco luxury superyacht deck, Monaco harbor and principality cliffs behind, Mediterranean deep blue water surrounding, other yachts in distance, afternoon golden Mediterranean light",
        "lighting": "Mediterranean afternoon direct from above + Mediterranean blue reflection from water all around, golden skin in Mediterranean dual light, silver braid catching sea light as silver-gold in Monaco blue",
        "style": "Korean mature goddess silver hair Monaco superyacht Mediterranean editorial, silver braid on Monaco blue luxury",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Monaco yacht silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_berlin_techno": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, porcelain skin cold in strobe light, severe geometric silver-white hair in sharp architectural bob, fierce cold expression",
        "outfit": "ultra-minimal black PVC micro bodysuit, bodysuit cut high on full thighs, black chrome thigh-high platform stiletto boots 6-inch heel on industrial concrete floor, chrome chain harness over bodysuit, chrome geometric ear cuffs",
        "environment": "Berlin underground techno club, raw concrete industrial interior, strobe lights cutting through total darkness, fog machine low ground level, exposed steel pipes",
        "lighting": "strobe hard white from multiple positions cutting through dark + ground fog diffusing low, porcelain skin cold in strobe cuts, silver bob catching strobe as blinding silver flashes in Berlin dark",
        "style": "Korean mature goddess silver hair Berlin techno industrial editorial, silver bob in Berlin strobe darkness",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Berlin techno silver grade, portrait 2:3 vertical",
    },
    "mature_korean_silver_crystal_gala": {
        "subject": "Korean mature goddess, supreme hourglass figure, late-40s, Korean features, luminous porcelain skin in crystal chandelier light, elaborate silver-white hair in grand formal updo with crystal pins, regal commanding expression",
        "outfit": "ultra-minimal silver crystal micro gown, micro-short with crystal fringe barely covering full mature curves, silver crystal platform stiletto heels 6-inch on marble ballroom floor, massive crystal drop earrings, crystal body chain",
        "environment": "grand European ballroom, massive crystal chandelier directly above, gilded walls and ceiling, mirror panels multiplying crystal light, marble floor reflecting chandelier below, formal gala atmosphere",
        "lighting": "massive crystal chandelier from directly above scattering prismatic light in all directions + marble floor reflection from below, luminous skin in prismatic crystal scatter, silver updo catching chandelier as crown of prismatic silver crystal fire",
        "style": "Korean mature goddess silver hair crystal ballroom gala editorial, silver crystal crown in chandelier prism light",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, crystal gala silver grade, portrait 2:3 vertical",
    },

    # ── 👴 Elder Goddess ───────────────────────────────
    "elder_korean_silver_void_studio": {
        "subject": "Korean elder goddess, mature feminine curves with supreme dignity, 62 years old, Korean features, porcelain skin with fine character lines of lived experience, dramatic pure white hair in sleek center-part straight to shoulders, cold fierce elder editorial expression",
        "outfit": "ultra-minimal black micro string bikini, black patent thigh-high platform stiletto boots 6-inch heel, single massive silver geometric ear sculpture only",
        "environment": "black infinity studio, single hard overhead spot, pure editorial void",
        "lighting": "single hard overhead spot, pure white hair catching as blinding white shaft in darkness, character-lined porcelain skin in chiaroscuro, mature silhouette commanding void",
        "style": "Korean elder goddess 62 pure white hair black void editorial, white hair as light in darkness",
        "quality": "Shot on Hasselblad X2D, 8K UHD, elder void grade, portrait 2:3 vertical",
    },
    "elder_korean_silver_jeju_wind": {
        "subject": "Korean elder goddess, mature dignified figure, 65 years old, Korean features, golden-weathered skin kissed by a lifetime of sun, pure white hair dramatically wind-swept in full horizontal, expression fierce and free as haenyeo spirit",
        "outfit": "ultra-minimal white micro string bikini, bare feet on Jeju black volcanic rock, single silver bangle, small silver hoop earrings",
        "environment": "Jeju Island cliff, black basalt columns rising from crashing turquoise sea, spray in air, strong ocean gale, sky and sea merging on horizon",
        "lighting": "Jeju midday coastal + ocean spray diffusing light, golden-weathered skin in coastal light, pure white hair horizontal in wind catching all light as white banner against Jeju blue",
        "style": "Korean elder goddess 65 white hair Jeju cliff gale editorial, white streaming in Jeju ocean wind",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Jeju elder wind grade, portrait 2:3 vertical",
    },
    "elder_korean_silver_hanok_dawn": {
        "subject": "Korean elder goddess, mature dignified figure, 68 years old, Korean features, luminous porcelain skin in dawn light, pure white hair in traditional Korean binyeo-pinned bun, serene commanding ancestral expression",
        "outfit": "ultra-minimal white ramie micro hanbok-inspired wrap, bare feet on hanok wooden maru floor, single jade drop earring, jade bracelet",
        "environment": "traditional Korean hanok interior at dawn, wooden beams, hanji windows glowing with pink dawn light from outside, celadon pottery, wooden floor, gate visible through paper door",
        "lighting": "hanji window pink dawn from outside glowing through paper + interior candlelight warm, luminous skin in dawn-candle dual warmth, white binyeo bun catching pink dawn as soft white-pink luminescence",
        "style": "Korean elder goddess 68 white hair hanok dawn editorial, white binyeo bun in Korean dawn",
        "quality": "Shot on Hasselblad X2D, 8K UHD, hanok dawn elder grade, portrait 2:3 vertical",
    },
    "elder_korean_silver_paris_cafe": {
        "subject": "Korean elder goddess, refined mature figure with elegant curves, 61 years old, Korean features, luminous porcelain skin flawless in Paris cafe light, chic silver-white hair in precise short crop, refined cold Parisian elder expression",
        "outfit": "ultra-minimal black micro bodysuit, cut to reveal elegant mature figure, black patent thigh-high platform stiletto boots 6-inch heel on Paris cafe floor, single strand pearl choker, pearl drop earrings",
        "environment": "classic Paris cafe interior, zinc bar, rattan chairs, mosaic tile floor, large window to Paris street, morning golden light from window, cafe au lait on zinc table",
        "lighting": "Paris morning gold from cafe window from side, luminous skin in Paris morning warmth, silver crop catching morning gold as warm silver-gold Paris chic",
        "style": "Korean elder goddess 61 silver crop Paris cafe Chanel editorial, silver crop in Paris morning gold",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Paris cafe elder grade, portrait 2:3 vertical",
    },
    "elder_korean_silver_tokyo_garden": {
        "subject": "Korean elder goddess, serene mature figure, 70 years old, Korean features, porcelain skin with beautiful age lines in garden light, pure white hair in loose traditional Japanese-style bun with single camellia, expression of deep serenity and power",
        "outfit": "ultra-minimal white linen micro wrap, bare feet on raked gravel path, single camellia behind ear matching bun, minimal silver thread bracelet",
        "environment": "Tokyo traditional Japanese garden, raked karesansui gravel garden, mossy stones, ancient pine bonsai, stone lantern, koi pond reflection, autumn maple",
        "lighting": "garden diffused morning from overcast sky + stone lantern warm amber from below, porcelain elder skin in soft garden diffusion, white bun with camellia in garden light as wabi-sabi crown",
        "style": "Korean elder goddess 70 white hair Tokyo garden wabi-sabi editorial, white camellia bun in Japanese garden",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Tokyo garden elder grade, portrait 2:3 vertical",
    },
    "elder_korean_silver_maldives_sunrise": {
        "subject": "Korean elder goddess, mature curves with supreme dignity, 63 years old, Korean features, golden skin glowing in Maldives sunrise, long loose pure white hair in sunrise wind, expression awe and power combined",
        "outfit": "ultra-minimal rose gold micro string bikini, micro thong, bare feet on overwater bungalow deck at dawn, single gold anklet, small gold hoop earrings",
        "environment": "Maldives overwater bungalow at sunrise, horizon on fire in pink-orange-gold, turquoise water below turning rose in dawn light, total water horizon 360 degrees",
        "lighting": "Maldives sunrise from horizon blazing pink-orange-gold + water reflection rose-gold from below, golden elder skin in sunrise dual warmth, pure white hair in pink-gold dawn catching sunrise as white-gold-rose fire",
        "style": "Korean elder goddess 63 white hair Maldives sunrise editorial, white hair as dawn fire over Maldives",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Maldives sunrise elder grade, portrait 2:3 vertical",
    },
    "elder_korean_silver_nyc_museum": {
        "subject": "Korean elder goddess, refined mature figure, 67 years old, Korean features, porcelain skin in museum white light, sculptural pure white hair in bold architectural updo, cold intellectual elder expression",
        "outfit": "ultra-minimal white micro structured bodysuit, architectural construction, white platform stiletto boots 6-inch heel on museum marble floor, single massive sculptural silver ear piece only",
        "environment": "contemporary art museum white cube interior, massive abstract canvas on white wall behind, track lighting from above, marble floor reflecting white below, museum hush and scale",
        "lighting": "museum track spots from above hard white + marble floor reflection white from below, porcelain elder skin in museum white bilateral, white architectural updo and ear sculpture as museum object in white",
        "style": "Korean elder goddess 67 white hair NYC museum art editorial, white sculpture in white museum",
        "quality": "Shot on Hasselblad X2D, 8K UHD, museum white elder grade, portrait 2:3 vertical",
    },
    "elder_korean_silver_rio_beach": {
        "subject": "Korean elder goddess, mature curves with powerful presence, 64 years old, Korean features, deep golden-bronze skin from lifelong sun, wild pure white hair in ocean wind, expression fierce coastal elder goddess",
        "outfit": "ultra-minimal bright yellow micro string bikini, micro thong, bare feet in Ipanema sand, gold layered chains, gold hoop earrings",
        "environment": "Ipanema beach Rio de Janeiro, Dois Irmaos twin peaks behind in afternoon gold, turquoise Atlantic waves, white sand, Rio beach energy",
        "lighting": "Rio direct afternoon sun from above + white sand reflection + ocean reflection, deep golden-bronze elder skin blazing in Rio triple light, pure white wild hair in Rio sun as white solar explosion against Dois Irmaos",
        "style": "Korean elder goddess 64 white hair Rio Ipanema beach solar editorial, white wild hair as solar explosion in Rio",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Rio beach elder grade, portrait 2:3 vertical",
    },
    "elder_korean_silver_dubai_desert": {
        "subject": "Korean elder goddess, commanding mature figure, 69 years old, Korean features, deep golden-olive skin weathered by decades of desert sun, long pure white hair in desert wind dramatic, fierce desert elder expression",
        "outfit": "ultra-minimal deep gold micro string bikini, micro thong, gold platform sandal wedge 5-inch on dune crest, massive layered gold chains, gold cuff bracelet",
        "environment": "Dubai desert at golden sunset, massive sand dune crests in deep amber-orange, sun touching horizon blazing, Bedouin tent visible in distance, total desert gold",
        "lighting": "desert setting sun from horizon + sand reflection warm from below, deep golden-olive elder skin in extreme warm orange-gold, pure white hair in desert sunset as white-gold fire against dune",
        "style": "Korean elder goddess 69 white hair Dubai desert sunset editorial, white as desert fire in Dubai gold",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Dubai desert elder grade, portrait 2:3 vertical",
    },
    "elder_korean_70s_cliff_wind": {
        "subject": "Korean elder goddess, 72 years old, Korean features, deeply weathered golden skin with the beauty of seven decades of Korean sun and sea, pure white hair completely wild in East Sea gale horizontal streaming in maximum wind, expression of absolute fierce freedom and power beyond age, haenyeo goddess",
        "outfit": "ultra-minimal white micro string bikini, bare feet on East Sea cliff granite, single abalone shell pendant, no other accessories",
        "environment": "Korean East Sea coastal granite cliff, turquoise waves crashing far below, sea spray in air, horizon meeting sky, haenyeo diving waters, strong gale",
        "lighting": "East Sea noon coastal from above + sea spray diffusing + ocean reflection upward, deeply weathered skin in coastal spray light, pure white hair streaming completely horizontal in gale as white elder freedom flag",
        "style": "Korean elder goddess 72 white hair East Sea cliff haenyeo spirit ultimate editorial, white freedom flag in Korean sea gale",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, East Sea elder haenyeo grade, portrait 2:3 vertical",
    },

    # ── 💪 Fitness Model ───────────────────────────────
    "fitness_korean_black_sand_wave": {
        "subject": "Korean fitness goddess, competition-ready shredded physique, extreme muscle separation with feminine shape, visible abs and glutes, mid-20s, Korean features, warm honey-bronze skin oiled and competition-stage gleaming, long straight dark hair sleek high ponytail, fierce athletic expression",
        "outfit": "ultra-minimal black micro string bikini competition style, micro thong maximum glute exposure, black chrome thigh-high platform stiletto boots 6-inch heel on black sand, black chrome arm cuff",
        "environment": "volcanic black sand beach, black sand extending to horizon, turquoise ocean waves crashing against black sand, dramatic contrast total",
        "lighting": "overcast coastal diffused from above + turquoise ocean reflection + wet black sand reflection, oiled honey-bronze skin every muscle cut visible, black bikini on black sand body-forward composition",
        "style": "Korean fitness competition black sand beach editorial, shredded physique on volcanic black sand",
        "quality": "Shot on Hasselblad X2D, 8K UHD, black sand fitness grade, portrait 2:3 vertical",
    },
    "fitness_korean_chrome_gym_mirror": {
        "subject": "Korean fitness goddess, competition-ready shredded physique, extreme muscle separation visible in gym light, mid-20s, Korean features, warm porcelain-honey skin oiled stage-ready, sleek dark hair severe center-part bun, bold competition makeup, intense focused expression",
        "outfit": "ultra-minimal chrome metallic micro string bikini competition style, micro thong, chrome platform stiletto boots 6-inch on gym floor, chrome arm band",
        "environment": "luxury fitness studio, floor-to-ceiling mirrors multiplying figure infinitely, chrome equipment, hard overhead gymnasium spotlights, polished concrete floor",
        "lighting": "hard overhead spots creating dramatic muscle shadow + mirror reflections all angles, oiled skin every muscle cut, chrome bikini matching mirror infinity, infinite mirror multiplication of defined physique",
        "style": "Korean fitness chrome gym mirror infinite editorial, competition definition in chrome mirror infinity",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, chrome gym mirror grade, portrait 2:3 vertical",
    },
    "fitness_korean_tattoo_bali_pool": {
        "subject": "Korean fitness goddess with full sleeve tattoo on right arm, intricate floral and geometric Korean ink pattern covering shoulder to wrist, competition-ready lean physique with visible abs, 27 years old, Korean features, golden-honey skin oiled and gleaming, long dark waves loose at pool, fierce sultry expression",
        "outfit": "ultra-minimal coral pink micro string bikini, micro thong, coral pink platform stiletto wedge sandal 5-inch on pool edge, single gold ankle chain",
        "environment": "Bali luxury villa infinity pool, infinity edge dropping to jungle valley below, rice terrace terracing visible beyond, tropical flowers at pool rim, afternoon golden light",
        "lighting": "Bali direct afternoon sun + pool turquoise reflection from water below, golden oiled skin dual light, tattoo sleeve catching afternoon light in full ink detail",
        "style": "Korean fitness tattoo sleeve Bali pool sultry editorial, inked physique at Bali infinity",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Bali pool fitness grade, portrait 2:3 vertical",
    },
    "fitness_korean_gold_dubai_sunrise": {
        "subject": "Korean fitness goddess, lean competition physique with pronounced feminine curves, narrow waist accentuating full hips, 29 years old, Korean features, deep golden-bronze skin oiled in Dubai sunrise, sleek dark hair in severe warrior braid, fierce powerful expression",
        "outfit": "ultra-minimal gold metallic micro string bikini barely containing curves, micro thong, gold chrome thigh-high platform stiletto boots 6-inch heel on Dubai hotel terrace, gold chain body harness over bikini, gold arm cuff",
        "environment": "Dubai luxury hotel terrace at sunrise, Burj Khalifa in full silhouette against orange-pink dawn sky, desert city waking below, infinity pool catching sunrise color",
        "lighting": "Dubai sunrise orange-pink from horizon + pool reflection from below, deep golden-bronze skin blazing in dual sunrise, gold harness catching dawn as warm gold fire",
        "style": "Korean fitness curves Dubai sunrise gold editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Dubai sunrise fitness grade, portrait 2:3 vertical",
    },
    "fitness_korean_tattoo_void_red": {
        "subject": "Korean fitness goddess, extreme muscle definition visible glutes hamstrings back musculature, mid-20s, Korean features, warm honey skin, severe sleek bun, cold fierce expression, full back tattoo of massive Korean phoenix rising from lower back to shoulder blades in traditional ink",
        "outfit": "ultra-minimal red micro string bikini thong back fully exposing back tattoo and glute definition, red patent thigh-high platform stiletto boots 6-inch, single silver arm band",
        "environment": "black infinity studio, single hard red-tinted spot from above",
        "lighting": "hard red-tinted overhead spot, honey skin in red-warm chiaroscuro, phoenix back tattoo fully illuminated by hard spot, extreme back muscle definition visible through tattoo",
        "style": "Korean fitness back tattoo phoenix void red editorial, back muscle and phoenix as one",
        "quality": "Shot on Hasselblad X2D, 8K UHD, void red fitness grade, portrait 2:3 vertical",
    },
    "fitness_korean_30s_tokyo_neon": {
        "subject": "Korean fitness goddess, 30s shredded lean physique showing a decade of training, 32 years old, Korean features, luminous porcelain skin in Tokyo neon, platinum-dyed short hair fierce, bold graphic liner, smoldering expression",
        "outfit": "ultra-minimal holographic silver micro bodysuit cut to navel, micro thong back, silver chrome thigh-high platform stiletto boots 6-inch in Tokyo puddles, silver holographic ear cuffs, silver arm sleeve",
        "environment": "Shibuya at midnight, neon signs full saturation, rain puddles reflecting rainbow neon below boots, crowds with umbrellas blurred",
        "lighting": "full Tokyo neon rainbow from all signs + puddle reflection below, porcelain skin in neon color wash, holographic bodysuit exploding every neon",
        "style": "Korean fitness 30s platinum Tokyo neon midnight editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Tokyo neon fitness grade, portrait 2:3 vertical",
    },
    "fitness_korean_abs_maldives_crystal": {
        "subject": "Korean fitness goddess, ultra-defined 6-pack abs as primary visual weapon, razor-cut abdominal definition extreme, 25 years old, Korean features, golden-tan skin glistening with saltwater, long dark hair wet and wild from ocean, fierce coastal expression",
        "outfit": "ultra-minimal white micro string bikini, micro thong, bare feet on Maldives sandbar, single gold waist chain highlighting abs",
        "environment": "Maldives crystal sandbar, knee-deep turquoise water surrounding sandbar, perfect horizon blue sky meeting sea, total tropical paradise",
        "lighting": "Maldives midday direct from above + turquoise water reflection upward, golden-tan skin blazing in dual light, abs catching every angle of Maldives light as sculptural definition",
        "style": "Korean fitness 6-pack abs Maldives crystal water editorial, abs as sculpture in turquoise paradise",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Maldives crystal fitness grade, portrait 2:3 vertical",
    },
    "fitness_korean_tattoo_collar_paris": {
        "subject": "Korean fitness goddess, lean elegant muscle with collar and collarbone tattoo, delicate floral vine tattoo wrapping neck base and both collarbones creating natural jewelry effect, mid-20s, Korean features, warm porcelain skin, severe sleek center-part black hair, cold editorial expression",
        "outfit": "ultra-minimal black micro string bikini, black patent thigh-high platform stiletto boots 6-inch on Paris rooftop, single diamond drop earring, diamond anklet",
        "environment": "Paris rooftop at golden hour, Eiffel Tower lit gold behind figure, Haussmann zinc rooftops extending below, golden afternoon Paris",
        "lighting": "Paris golden hour from behind Eiffel + warm ambient below from city, porcelain skin in golden warmth, collarbone tattoo in golden light as natural jewelry",
        "style": "Korean fitness collarbone tattoo Paris Eiffel golden hour editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, Paris golden fitness grade, portrait 2:3 vertical",
    },
    "fitness_korean_powerglam_lasvegas": {
        "subject": "Korean fitness goddess, competition-ready physique with glamorous curves, 28 years old, Korean features, deep bronze-copper skin oiled, sleek dark hair in high power ponytail, fierce glamorous expression",
        "outfit": "ultra-minimal silver sequin micro string bikini barely covering competition physique, micro thong, silver chrome thigh-high platform stiletto boots 6-inch on Las Vegas Strip, silver body chain over bikini",
        "environment": "Las Vegas Strip at midnight, Bellagio fountains blazing behind, casino neon in all colors, crowd energy total",
        "lighting": "Las Vegas neon rainbow from all casino signs + Bellagio fountain mist light, bronze-copper skin in Vegas neon, silver sequin bikini exploding every neon as diamond scatter",
        "style": "Korean fitness power glamour Vegas midnight editorial",
        "quality": "Shot on Hasselblad X2D, 8K UHD, Vegas neon fitness grade, portrait 2:3 vertical",
    },
    "fitness_korean_bikini_pro_stage": {
        "subject": "Korean fitness goddess, IFBB bikini pro-level physique, competition peak conditioning, round full glutes, narrow waist, lean shoulders, 26 years old, Korean features, deep mahogany-bronze competition tan oiled to extreme gloss, hair in competition curls, full glamour competition makeup",
        "outfit": "ultra-minimal competition turquoise micro bikini with crystal embellishment barely covering pro physique, micro thong maximum glute exposure, clear platform 5-inch heels on competition stage",
        "environment": "bodybuilding competition stage, blinding white spotlights from above, judges panel blur below stage, audience in darkness behind",
        "lighting": "competition spot from above hard + stage fill lights, mahogany competition tan blazing under stage lights, crystal bikini sparkling under competition spot",
        "style": "Korean fitness IFBB bikini pro competition stage editorial",
        "quality": "Shot on Phase One XF IQ4, 8K UHD, competition stage grade, portrait 2:3 vertical",
    },
}


def main():
    created = 0
    skipped = 0
    errors  = 0

    for key, data in PRESETS.items():
        path = PRESETS_DIR / f"{key}.json"
        if path.exists():
            skipped += 1
            continue
        try:
            path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
            created += 1
            print(f"✅ {key}")
        except Exception as e:
            errors += 1
            print(f"❌ {key}: {e}")

    print(f"\n완료: 생성 {created}개 / 스킵 {skipped}개 / 오류 {errors}개")
    print(f"총 프리셋: {len(PRESETS)}개")


if __name__ == "__main__":
    main()
