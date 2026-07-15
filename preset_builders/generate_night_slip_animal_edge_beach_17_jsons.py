# -*- coding: utf-8 -*-
"""
generate_night_slip_animal_edge_beach_13_jsons.py
나이트+4 / 슬립+3 / 애니멀+3 / 파워엣지+4 / 비치+3 — 총 17종
(나이트 4종은 판정 완료 HOF/SSS, 나머지 9종은 이미지 생성 후 판정)
"""

import json, os

OUTPUT_DIR = "presets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PRESETS = {

# ─────────────────────────────────────────────────────
# 🌙 나이트 글래머 +4종 (판정 완료)
# ─────────────────────────────────────────────────────
"night_bust_queen_dubai": {
    "label": "나이트 버스트퀸 두바이 버즈칼리파",
    "category": "night_glamour",
    "tags": ["night","bust_queen","dubai","burj_khalifa","gold"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: bust queen goddess, legendary full mature bust with impossibly cinched waist, mid-20s, Emirati features, warm golden-olive skin oiled and gleaming, long jet-black waves with subtle gold highlights, kohl-lined eyes, deep plum lips, expression commanding-regal. Wearing: ultra-minimal gold micro string bikini top barely containing legendary bust — fabric at absolute maximum tension, matching micro thong, gold chrome thigh-high platform stiletto boots 6-inch heel, layered gold choker stacked three levels, gold serpent arm cuff. Environment: Dubai penthouse terrace, Burj Khalifa dominating entire frame behind, city blazing in full night gold below, infinity pool edge reflecting Burj lights, desert night air. Lighting: Burj Khalifa gold ambient from behind + infinity pool reflection upward + single hard key from front, golden-olive skin blazing in Dubai gold from all directions, legendary bust catching every light source as golden sculpture. Style: bust queen Dubai Burj Khalifa night penthouse editorial, legendary proportions commanding Dubai skyline. Shot on Hasselblad X2D, 8K UHD, Dubai gold night grade, portrait 2:3 vertical."
},
"night_brazil_tokyo_neon": {
    "label": "나이트 브라질 도쿄 시부야 네온",
    "category": "night_glamour",
    "tags": ["night","brazil","tokyo","shibuya","neon"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: Brazilian goddess, extreme sculpted hourglass with maximum hip-to-waist ratio, dramatically wide hips and full bust, mid-20s, Brazilian features, warm deep bronze skin gleaming in neon, long voluminous dark waves with copper highlights wild in night air, bold dramatic eye, deep red lip, expression fierce-commanding. Wearing: ultra-minimal neon pink holographic micro string bikini, micro thong maximum exposure on extreme wide hips, neon pink chrome thigh-high platform stiletto boots 6-inch heel in Shibuya puddles, gold waist chain emphasizing extreme cinch, pink holographic ear cuffs. Environment: Shibuya crossing Tokyo midnight, massive LED billboards in every direction, neon reflection in rain puddles below boots, crowd blurred, total Tokyo neon chaos. Lighting: Shibuya neon rainbow from all billboard directions + puddle reflection from below, deep bronze skin in full neon saturation, holographic bikini shifting every neon color on extreme curves. Style: Brazilian extreme hourglass Tokyo Shibuya neon night editorial, maximum curves commanding neon city. Shot on Phase One XF IQ4, 8K UHD, Tokyo neon night grade, portrait 2:3 vertical."
},
"night_supermodel_paris_rooftop": {
    "label": "나이트 수퍼모델 파리 에펠탑 루프탑",
    "category": "night_glamour",
    "tags": ["night","supermodel","paris","eiffel","rooftop"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: supermodel goddess, 182cm extreme tall slim figure, impossibly long legs, late-20s, French-Korean mixed features, cool ivory-golden skin, sleek severe center-part platinum-dyed hair, sharp editorial cheekbones, cold distant haute couture expression. Wearing: ultra-minimal black micro slip dress, spaghetti straps vanishing on tall slim frame, dress micro-short on extreme long legs, clear platform stiletto mules 6-inch heel on Paris rooftop stone, single massive sculptural silver ear piece only, silver anklet. Environment: luxury Paris rooftop, Eiffel Tower blazing gold directly behind tall figure, Paris night panorama below, zinc rooftops, warm Parisian night amber. Lighting: Eiffel Tower gold from behind creating dramatic backlit halo + warm Paris city ambient from below, ivory-golden skin in warm Parisian gold, extreme tall slim silhouette as black sculpture against Eiffel gold. Style: supermodel 182cm Paris Eiffel rooftop night micro slip editorial, extreme tall figure commanding Paris night. Shot on Hasselblad X2D, 8K UHD, Paris night supermodel grade, portrait 2:3 vertical."
},
"night_powerlifter_lasvegas": {
    "label": "나이트 파워리프터 라스베가스 스트립",
    "category": "night_glamour",
    "tags": ["night","powerlifter","las_vegas","strip","neon"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: powerlifter goddess, extreme defined musculature with full feminine curves maintained, 30s, Korean-American features, deep bronze iron skin oiled gleaming, severe high bun, ice-cold fierce expression, bold lip. Wearing: ultra-minimal chrome silver latex micro bodysuit, latex vacuum-tight on every extreme muscle group revealing definition through chrome, bodysuit cut extreme high on powerful thighs, silver chrome thigh-high platform stiletto boots 6-inch heel on Vegas sidewalk, silver titanium arm cuffs, chrome choker. Environment: Las Vegas Strip at night, massive casino LED signs blazing in all directions, Bellagio fountains behind, neon reflection everywhere, Vegas night total excess. Lighting: Vegas neon from all casino signs in every color + ground reflection from below, bronze iron skin blazing in Vegas color saturation through chrome panels, chrome bodysuit as total mirror on every muscle. Style: powerlifter Las Vegas Strip chrome latex night editorial, iron physique commanding Vegas excess. Shot on Phase One XF IQ4, 8K UHD, Vegas neon night grade, portrait 2:3 vertical."
},

# ─────────────────────────────────────────────────────
# 👗 슬립드레스 +3종
# ─────────────────────────────────────────────────────
"slip_brazil_paris_apartment": {
    "label": "슬립드레스 브라질 파리 아파트 아침",
    "category": "slip_dress_glamour",
    "tags": ["slip_dress","brazil","paris","morning","satin"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: Brazilian goddess, extreme sculpted hourglass maximum hip-to-waist ratio, dramatically wide hips and full bust, mid-20s, Brazilian features, warm caramel-honey skin luminous in Paris morning light, long voluminous dark waves loose in morning air, natural fresh expression, nude gloss lip. Wearing: ultra-minimal champagne satin micro slip dress, bias-cut satin clinging to every extreme curve and riding up on full wide hips, spaghetti straps barely containing full bust, dress hem barely below extreme wide hips, clear platform stiletto mules 5-inch heel on Paris parquet floor, single pearl drop earring only. Environment: Haussmann Paris apartment, floor-to-ceiling tall French windows, zinc rooftop morning view, warm Paris morning gold flooding interior, unmade bed visible behind. Lighting: Paris morning gold from windows creating warm side light on extreme curves, champagne satin catching morning gold as liquid metal on Brazilian hourglass, warm domestic intimate Paris morning. Style: Brazilian extreme hourglass Paris morning apartment satin slip editorial, maximum curves in intimate Paris luxury. Shot on Hasselblad X2D, 8K UHD, Paris morning slip grade, portrait 2:3 vertical."
},
"slip_colombia_morocco_riad": {
    "label": "슬립드레스 콜롬비안 모로코 리야드 촛불",
    "category": "slip_dress_glamour",
    "tags": ["slip_dress","colombian","morocco","riad","candlelight"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: Colombian goddess, extreme sculpted hourglass maximum hip-to-waist ratio, dramatically wide hips and impossibly cinched waist, mid-20s, Colombian features, warm olive-bronze skin luminous in Moroccan lantern light, long straight dark hair with copper highlights loose, seductive commanding expression, deep berry lip. Wearing: ultra-minimal deep gold satin micro slip dress, bias-cut fabric transparent in lantern light revealing extreme hourglass fully, wide hips stretching fabric to maximum, spaghetti straps, dress micro-short, gold stiletto platform mules 5-inch heel on Moroccan tile, layered gold coin necklaces, gold coin drop earrings. Environment: luxury Moroccan riad, intricate zellige tile walls in cobalt and gold, carved plaster archways, candles and lanterns warm amber from all positions, central fountain, extreme figure as riad centerpiece. Lighting: Moroccan lantern warm amber from multiple positions + candle warm below, olive-bronze skin in total warm Moroccan amber, gold satin transparent in lantern revealing extreme Colombian curves. Style: Colombian extreme hourglass Morocco riad amber candlelight slip dress editorial. Shot on Phase One XF IQ4, 8K UHD, Morocco riad slip grade, portrait 2:3 vertical."
},
"slip_powerlifter_onsen": {
    "label": "슬립드레스 파워리프터 일본 료칸 온센",
    "category": "slip_dress_glamour",
    "tags": ["slip_dress","powerlifter","onsen","ryokan","steam"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: powerlifter goddess, extreme defined musculature with feminine curves, 30s, Japanese-Korean features, warm porcelain skin luminous in steam, severe warrior braid loosened into soft waves in onsen steam, fierce-serene expression, nude glossy lip. Wearing: ultra-minimal white silk micro slip dress completely soaked in onsen steam — silk transparent and clinging to every extreme muscle definition and curve, spaghetti straps on powerful shoulders, dress barely below powerful thighs, white platform geta sandals 4-inch on hinoki wood, single jade drop earring only. Environment: private ryokan outdoor hinoki onsen, steam rising from hot spring, stone lanterns amber, bamboo swaying, maple in autumn color, total Japanese luxury intimacy. Lighting: stone lantern warm amber + steam diffusing and scattering light, porcelain skin luminous through steam-soaked transparent silk, every muscle group visible through soaked fabric as iron sculpture in amber steam. Style: powerlifter ryokan onsen soaked white silk slip dress editorial, iron physique revealed in Japanese luxury steam. Shot on Hasselblad X2D, 8K UHD, onsen slip powerlifter grade, portrait 2:3 vertical."
},

# ─────────────────────────────────────────────────────
# 🐆 애니멀프린트 +3종
# ─────────────────────────────────────────────────────
"animal_supermodel_python_gown": {
    "label": "애니멀프린트 수퍼모델 파이톤 플로어 가운",
    "category": "animal_print_glamour",
    "tags": ["animal_print","supermodel","python","gown","floor_length"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: supermodel goddess, 183cm extreme tall slim figure, impossibly long legs, late-20s, Korean features, warm honey-golden skin, sleek severe center-part dark hair with silver highlights, sharp editorial cheekbones, cold regal expression, deep wine lip. Wearing: ultra-minimal python snake print micro bodycon floor-grazing gown, python print fabric vacuum-tight on extreme tall slim figure with floor-length slit revealing extreme long leg from hip to floor, gown micro-cut at hip creating maximum leg exposure on walk, black patent thigh-high platform stiletto boots 6-inch heel visible through slit, single architectural python-print ear cuff. Environment: luxury fashion week venue, white marble floors, photographers at front row, runway lighting, fashion elite total. Lighting: runway hard white overhead + photographer flash from front row, honey-golden skin in hard fashion light, python print gown catching every flash as living snake scales on extreme tall figure. Style: supermodel 183cm python floor gown fashion week runway editorial, extreme tall figure commanding fashion world. Shot on Phase One XF IQ4, 8K UHD, python gown supermodel grade, portrait 2:3 vertical."
},
"animal_miniature_ocelot_mini": {
    "label": "애니멀프린트 미니어처 오셀롯 마이크로 미니",
    "category": "animal_print_glamour",
    "tags": ["animal_print","miniature","ocelot","micro_mini","petite"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: miniature goddess, ultra-petite compact figure with maximum curves on tiny frame, 148cm, mid-20s, Korean features, warm honey skin, long voluminous dark waves wild, bold cat-eye makeup, bold fuchsia lip, fierce expression. Wearing: ultra-minimal ocelot print micro bodycon mini dress, ocelot pattern vacuum-tight on compact maximum curves — curves amplified dramatically by tiny frame, dress barely below compact full hips, fuchsia patent thigh-high platform stiletto boots 6-inch heel creating extreme height contrast on tiny frame, gold waist chain, fuchsia crystal ear cuffs. Environment: pure black infinity studio, single overhead hard spot, pure editorial void. Lighting: single hard overhead, ocelot print in full graphic specular detail on compact maximum curves, honey skin between animal print as warm contrast, dramatic height proportion. Style: miniature petite ocelot micro mini maximum proportion studio editorial, tiny frame commanding maximum impact. Shot on Hasselblad X2D, 8K UHD, ocelot miniature studio grade, portrait 2:3 vertical."
},
"animal_colombia_giraffe_bodycon": {
    "label": "애니멀프린트 콜롬비안 지라프 바디콘",
    "category": "animal_print_glamour",
    "tags": ["animal_print","colombian","giraffe","bodycon","savanna"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: Colombian goddess, extreme sculpted hourglass maximum hip-to-waist ratio, dramatically wide hips and full bust, mid-20s, Colombian features, warm terra-cotta bronze skin, long straight dark hair severe, bold smoky eye, deep nude lip, commanding expression. Wearing: ultra-minimal giraffe print latex micro bodycon dress, giraffe tan-and-brown pattern vacuum-tight on every extreme curve — wide hips stretching fabric to architectural limit, dress barely below extreme hips, tan chrome thigh-high platform stiletto boots 6-inch heel, gold waist chain at extreme cinch, gold hoop earrings. Environment: luxury rooftop at golden sunset, savanna-toned golden light, city skyline behind creating urban-safari fusion, warm golden hour total. Lighting: golden sunset from low angle creating warm savanna palette, terra-cotta bronze skin blazing in warm gold, giraffe print creating natural camouflage pattern in savanna golden light on extreme curves. Style: Colombian extreme hourglass giraffe bodycon urban savanna sunset editorial. Shot on Phase One XF IQ4, 8K UHD, giraffe Colombian sunset grade, portrait 2:3 vertical."
},

# ─────────────────────────────────────────────────────
# ⚔️ 파워 & 엣지 +4종
# ─────────────────────────────────────────────────────
"edge_bust_queen_cyber_armor": {
    "label": "파워엣지 버스트퀸 사이버펑크 아머",
    "category": "power_edge_glamour",
    "tags": ["power_edge","bust_queen","cyberpunk","armor","neon"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: bust queen goddess, legendary full mature bust with impossibly cinched waist, mid-20s, Korean features, warm honey-golden skin, sleek center-part dark hair with electric blue streaks severe, cyber holographic eye makeup, bold electric blue lip, fierce cyber expression. Wearing: ultra-minimal black cyber armor micro bodysuit, geometric panel construction barely covering legendary bust — armor panels framing bust at maximum display, bodysuit cut extreme high on full hips, electric blue chrome thigh-high platform stiletto boots 6-inch heel, electric blue LED chest panel pulsing, chrome shoulder spaulders, chrome choker. Environment: cyberpunk Seoul underground, neon blue grid floor, holographic Korean text projections, low fog, DDP cyber aesthetic. Lighting: cyber neon blue from grid floor + electric blue from LED chest panel + cool overhead, honey-golden skin in cyber blue shift, chrome panels reflecting cyber environment, legendary bust in electric blue frame. Style: bust queen cyberpunk Seoul cyber armor editorial, legendary proportions in cyber power. Shot on Hasselblad X2D, 8K UHD, cyber armor bust grade, portrait 2:3 vertical."
},
"edge_supermodel_neon_warrior": {
    "label": "파워엣지 수퍼모델 네온 워리어 스팀펑크",
    "category": "power_edge_glamour",
    "tags": ["power_edge","supermodel","neon","warrior","steampunk"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: supermodel goddess, 182cm extreme tall slim warrior figure, impossibly long powerful legs, late-20s, Korean features, warm honey-golden skin, silver-dyed center-part hair severe architectural updo with brass gear pins, fierce warrior expression, bold dark lip. Wearing: ultra-minimal steampunk-neon micro warrior bodysuit, brass gear and rivet construction barely covering tall slim figure, neon green accent strips running bodysuit seams, bodysuit high-cut on extreme long thighs, brass-chrome thigh-high platform stiletto combat boots 6-inch heel, brass wide arm gauntlets, brass gear choker. Environment: steampunk industrial warehouse, massive brass pipe machinery, neon green accent lights, steam venting, industrial power total. Lighting: neon green from accent strips + industrial warm from steam vents + hard overhead spot, honey-golden skin in neon green and warm brass dual, brass hardware catching industrial warm as gold, extreme tall figure commanding industrial domain. Style: supermodel 182cm steampunk neon warrior industrial editorial. Shot on Phase One XF IQ4, 8K UHD, steampunk warrior supermodel grade, portrait 2:3 vertical."
},
"edge_miniature_spike_latex": {
    "label": "파워엣지 미니어처 스파이크 라텍스",
    "category": "power_edge_glamour",
    "tags": ["power_edge","miniature","spike","latex","punk"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: miniature goddess, ultra-petite compact maximum curves on tiny frame, 148cm, mid-20s, Korean features, warm honey skin, severe platinum undercut fade with black tips, heavy dark punk eye, bold black lip, fierce dangerous expression. Wearing: ultra-minimal black spike-studded latex micro bodycon dress, chrome spike hardware covering every seam and edge creating armored aesthetic, black latex vacuum-tight on compact maximum curves, dress barely below compact full hips, black chrome thigh-high platform stiletto spike boots 6-inch heel — platform creating dramatic height on tiny figure, chrome spike choker, chrome spike arm cuffs. Environment: dark industrial studio, single hard overhead spot, concrete below, pure power void. Lighting: single hard overhead, chrome spikes creating constellation of specular points across compact curves, black latex as dark mirror on tiny powerful figure. Style: miniature petite spike latex punk power editorial, tiny frame maximum dangerous impact. Shot on Hasselblad X2D, 8K UHD, spike latex miniature grade, portrait 2:3 vertical."
},
"edge_bbw_steampunk_corset": {
    "label": "파워엣지 BBW 스팀펑크 코르셋",
    "category": "power_edge_glamour",
    "tags": ["power_edge","bbw","steampunk","corset","industrial"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: BBW goddess, massively full magnificent curves commanding frame, 30s, Korean features, deep warm honey skin, voluminous natural waves with copper steampunk highlights, bold dramatic eye, deep wine lip, expression owning-everything. Wearing: ultra-minimal steampunk brass corset brutally cinching massive waist creating dramatic hourglass — corset panel construction with brass gears and rivets, matching micro thong below, black patent thigh-high platform stiletto boots 6-inch heel, brass wide arm cuffs with gear details, brass gear drop earrings, brass clock-piece choker. Environment: steampunk Victorian industrial interior, massive brass pipe organ machinery, candle-and-gas-lamp warm amber, steam venting, antique industrial power. Lighting: gas lamp warm amber from multiple positions + steam diffusing warmly, deep honey skin blazing in warm amber, brass corset creating golden centerpiece on massive curves, gear hardware catching warm as working gold. Style: BBW steampunk brass corset Victorian industrial editorial, massive curves commanding steampunk power. Shot on Phase One XF IQ4, 8K UHD, steampunk BBW grade, portrait 2:3 vertical."
},

# ─────────────────────────────────────────────────────
# 🏖️ 비치 & 리조트 +3종
# ─────────────────────────────────────────────────────
"beach_powerlifter_seychelles": {
    "label": "비치 파워리프터 세이셸 핑크 화강암",
    "category": "beach_resort_glamour",
    "tags": ["beach","powerlifter","seychelles","granite","indian_ocean"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: powerlifter goddess, extreme defined musculature with feminine curves, 30s, Korean features, deep bronze iron skin oiled gleaming in Indian Ocean light, severe warrior braid, fierce warrior-ocean expression, bold lip. Wearing: ultra-minimal turquoise micro string bikini, micro thong, turquoise platform stiletto wedge sandals 5-inch heel on smooth pink Seychelles granite, single bronze arm cuff only — iron physique is the editorial. Environment: Anse Source d'Argent Seychelles, massive smooth pink granite boulders towering around powerful figure, turquoise Indian Ocean between granite gaps, palm fronds, paradise total. Lighting: Seychelles golden afternoon direct from above + turquoise Indian Ocean reflection between granite gaps from below, deep oiled bronze iron skin blazing in dual golden-turquoise on every extreme muscle definition, turquoise bikini perfectly matching Indian Ocean palette. Style: powerlifter Seychelles pink granite Indian Ocean editorial, iron physique commanding paradise. Shot on Hasselblad X2D, 8K UHD, Seychelles powerlifter grade, portrait 2:3 vertical."
},
"beach_bust_queen_amalfi": {
    "label": "비치 버스트퀸 아말피 코스트 절벽",
    "category": "beach_resort_glamour",
    "tags": ["beach","bust_queen","amalfi","cliff","mediterranean"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: bust queen goddess, legendary full mature bust with impossibly cinched waist, mid-20s, Italian-Korean features, warm golden Mediterranean skin, long dark waves in Mediterranean cliff wind, sultry commanding expression, bold coral lip. Wearing: ultra-minimal cobalt blue micro string bikini top barely containing legendary bust — fabric at absolute maximum tension, matching micro thong, cobalt blue patent platform stiletto wedge sandals 5-inch heel on Amalfi cliff path, layered gold chains, gold hoop earrings, gold anklet. Environment: Amalfi Coast cliff path, dramatic cliffside dropping to turquoise Tyrrhenian Sea below, colorful Amalfi village on cliff behind, lemon trees, Mediterranean total beauty. Lighting: Mediterranean noon direct from above + turquoise sea reflection upward from below + cliff bounce, golden Mediterranean skin blazing in triple light, legendary bust in cobalt at maximum tension over Amalfi drama. Style: bust queen Amalfi Coast cliff Mediterranean legendary proportions editorial. Shot on Phase One XF IQ4, 8K UHD, Amalfi bust queen grade, portrait 2:3 vertical."
},
"beach_supermodel_palawan": {
    "label": "비치 수퍼모델 팔라완 카르스트 석회암",
    "category": "beach_resort_glamour",
    "tags": ["beach","supermodel","palawan","karst","philippines"],
    "aspect": "2:3",
    "prompt": "Professional fashion photograph, full body shot. Model: supermodel goddess, 182cm extreme tall slim figure, impossibly long legs, mid-20s, Filipino-Korean mixed features, warm golden-honey skin, long straight dark hair in sea wind, coastal commanding expression, bold lip. Wearing: ultra-minimal white micro string bikini, micro thong, clear platform stiletto wedge mules 5-inch heel on white Palawan sand, single delicate gold anklet, tiny gold studs. Environment: El Nido Palawan Philippines, dramatic limestone karst cliffs towering above and behind extreme tall figure — scale contrast between 182cm figure and massive karst, turquoise lagoon water, hidden beach total paradise. Lighting: Palawan tropical noon direct from above + turquoise lagoon reflection upward, golden-honey skin in tropical dual, massive limestone karst scale dwarfing even the extreme tall figure. Style: supermodel 182cm Palawan karst limestone scale contrast beach editorial, extreme tall figure in paradise scale. Shot on Hasselblad X2D, 8K UHD, Palawan supermodel grade, portrait 2:3 vertical."
},
}

count = 0
for key, data in PRESETS.items():
    filepath = os.path.join(OUTPUT_DIR, f"{key}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {key}.json")
    count += 1

print(f"\n총 {count}종 JSON 생성 완료")
print(f"저장 위치: {OUTPUT_DIR}/")
