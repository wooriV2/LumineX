# -*- coding: utf-8 -*-
"""
Runway Slim 한국인 20종 JSON 생성 스크립트
실행: $env:PYTHONUTF8 = "1"; python preset_builders/generate_runway_korean_slim_20_jsons.py
"""

import json, os

OUTPUT_DIR = "presets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PRESETS = {
    "runway_korean_slim_void_studio": {
        "label": "런웨이 슬림 보이드 스튜디오",
        "tier": "SS",
        "tags": ["korean","runway","slim","void","studio"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim runway figure, impossibly long legs and neck, mid-20s, "
            "Korean features, luminous porcelain skin, severe sleek center-part jet-black hair to mid-back, "
            "sharp editorial cheekbones, cold high fashion expression. "
            "Wearing: ultra-minimal white micro structured bodysuit, architectural panel construction barely covering slim extreme tall frame, "
            "white patent thigh-high platform stiletto boots 6-inch heel, single massive sculptural silver ear piece only. "
            "Environment: black infinity studio, single hard overhead spot, pure editorial void. "
            "Lighting: single hard overhead spot, extreme tall slim silhouette as white architectural form against void. "
            "Style: Korean runway 185cm+ void studio high fashion editorial. "
            "Shot on Hasselblad X2D, 8K UHD, void runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_paris_window": {
        "label": "런웨이 슬림 파리 창가",
        "tier": "SS",
        "tags": ["korean","runway","slim","paris","window"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, impossibly long legs, mid-20s, "
            "Korean features, luminous porcelain skin in Paris morning light, severe sleek center-part platinum-dyed hair, "
            "sharp cheekbones, cold distant haute couture expression. "
            "Wearing: ultra-minimal ivory silk micro slip, spaghetti straps barely visible on slim frame, "
            "slip micro-length on extreme long legs, clear platform stiletto mules 6-inch on Paris parquet floor, "
            "single architectural pearl drop earring only. "
            "Environment: Haussmann Paris apartment, floor-to-ceiling tall French windows, zinc rooftops view, morning gold. "
            "Lighting: Paris morning gold from windows side-lighting extreme tall figure, ivory silk catching morning gold. "
            "Style: Korean runway 185cm+ Paris window haute couture editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Paris runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_milan_catwalk": {
        "label": "런웨이 슬림 밀라노 캣워크",
        "tier": "SSS",
        "tags": ["korean","runway","slim","milan","catwalk"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, legs that never end, mid-20s, "
            "Korean features, porcelain skin, severe sleek center-part black hair razor-cut to jawline, razor cheekbones, cold catwalk expression. "
            "Wearing: ultra-minimal black micro corset-structured runway top barely covering slim chest, "
            "black micro shorts high-cut maximum leg exposure on extreme long legs, "
            "black patent thigh-high platform stiletto boots 6-inch on Milan runway, "
            "single massive architectural chrome ear sculpture, no other accessories. "
            "Environment: Milan Fashion Week runway, white runway, fashion crowd both sides blur, designer backdrop, runway overhead spots. "
            "Lighting: runway overhead spots hard from above, porcelain skin in hard fashion light, extreme long legs endless on white runway. "
            "Style: Korean runway 185cm+ Milan catwalk micro editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Milan runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_tokyo_shibuya_rain": {
        "label": "런웨이 슬림 시부야 빗속",
        "tier": "SSS",
        "tags": ["korean","runway","slim","tokyo","rain"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, impossibly long legs in Tokyo neon rain, mid-20s, "
            "Korean features, luminous porcelain skin in neon light, sleek silver-dyed center-part hair, sharp cold editorial expression. "
            "Wearing: ultra-minimal holographic iridescent micro bodysuit, cut to maximum leg exposure on extreme long thighs, "
            "clear holographic thigh-high platform stiletto boots 6-inch in Shibuya puddles, single holographic ear cuff. "
            "Environment: Shibuya crossing midnight, full neon saturation, rain puddles reflecting rainbow below extreme long boots, crowds with umbrellas blurred. "
            "Lighting: full Shibuya neon rainbow + puddle reflection from below, porcelain skin in neon color wash, holographic bodysuit exploding every neon. "
            "Style: Korean runway 185cm+ Shibuya rain holographic editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Shibuya runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_dubai_penthouse": {
        "label": "런웨이 슬림 두바이 펜트하우스",
        "tier": "SS",
        "tags": ["korean","runway","slim","dubai","penthouse"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, legs to the ceiling, late-20s, "
            "Korean features, warm honey-porcelain skin in Dubai gold, severe center-part platinum blonde hair, cold commanding expression. "
            "Wearing: ultra-minimal gold metallic micro string bikini top — tiny triangles on slim frame barely existing, matching micro thong, "
            "gold chrome thigh-high platform stiletto boots 6-inch on Dubai penthouse terrace, single gold architectural ear cuff. "
            "Environment: Dubai penthouse terrace, Burj Khalifa dominating frame, city blazing gold below, infinity pool edge reflecting Burj. "
            "Lighting: Burj Khalifa gold ambient from behind + pool reflection upward + hard key, honey-porcelain skin in Dubai gold, extreme tall figure commanding Burj. "
            "Style: Korean runway 185cm+ Dubai penthouse gold night editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Dubai runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_nyc_rooftop": {
        "label": "런웨이 슬림 NYC 루프탑",
        "tier": "SS",
        "tags": ["korean","runway","slim","nyc","rooftop"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, warm porcelain skin, "
            "severe slicked-back jet-black hair, sharp editorial expression cold as NYC night. "
            "Wearing: ultra-minimal black micro bikini — absolute minimum on slim tall frame, "
            "black patent thigh-high platform stiletto boots 6-inch on NYC rooftop, single diamond drop earring, diamond anklet. "
            "Environment: NYC rooftop at night, Empire State Building lit directly behind tall figure, Manhattan grid gold below, water tower silhouettes. "
            "Lighting: NYC city gold + Empire State spotlight from behind, porcelain skin in NYC warm gold, extreme tall figure silhouetted against Manhattan. "
            "Style: Korean runway 185cm+ NYC rooftop night editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, NYC runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_seoulforest_spring": {
        "label": "런웨이 슬림 서울숲 봄",
        "tier": "SS",
        "tags": ["korean","runway","slim","seoul","spring"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, early-20s, Korean features, "
            "natural luminous porcelain skin in spring dappled light, severe sleek center-part dark hair, expression cool and distant in spring forest. "
            "Wearing: ultra-minimal white sheer micro dress — completely see-through fabric barely covering slim tall frame, "
            "visible micro white bikini underneath through sheer, clear platform stiletto mules 6-inch on forest path, single cherry blossom pin in hair. "
            "Environment: Seoul Forest in full spring bloom, cherry and forsythia in bloom, dappled spring light through young leaves, forest path. "
            "Lighting: spring forest dappled from above through canopy, porcelain skin in green-gold spring dapple, white sheer dress catching spring light as luminous veil. "
            "Style: Korean runway 185cm+ Seoul spring forest sheer editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Seoul spring runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_icelandic_glacier": {
        "label": "런웨이 슬림 아이슬란드 빙하",
        "tier": "SSS",
        "tags": ["korean","runway","slim","iceland","glacier"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, "
            "cold alabaster skin in glacier light, ice-blonde dyed center-part hair, expression cold as glacier, absolute cold editorial. "
            "Wearing: ultra-minimal silver chrome micro string bikini — silver triangles on slim alabaster frame, "
            "silver chrome thigh-high platform stiletto boots 6-inch on glacier ice, single crystal drop earring. "
            "Environment: Iceland glacier, massive blue-white ice walls behind, crevasses of deep blue ice, glacier silence total. "
            "Lighting: glacier ice blue-white ambient from ice walls all around + cold overcast above, "
            "alabaster skin in glacier ice-blue, silver bikini matching glacier palette. "
            "Style: Korean runway 185cm+ Iceland glacier ice-blue editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, glacier runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_moroccan_riad": {
        "label": "런웨이 슬림 모로코 리아드",
        "tier": "SS",
        "tags": ["korean","runway","slim","morocco","riad"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, "
            "warm olive-honey skin in Moroccan lantern light, long dark waves loose in riad warmth, expression exotic and commanding. "
            "Wearing: ultra-minimal gold sheer micro wrap dress, fabric transparent in lantern light revealing slim tall frame fully, "
            "gold stiletto platform mules 5-inch on Moroccan tile, layered gold necklaces, gold coin drop earrings. "
            "Environment: Moroccan luxury riad, intricate zellige tile walls, carved plaster archways, candles and lanterns warm amber, central fountain. "
            "Lighting: Moroccan lantern warm amber from multiple positions, candle warm below, olive-honey skin in Moroccan amber, gold sheer dress transparent in lantern. "
            "Style: Korean runway 185cm+ Morocco riad amber editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Morocco runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_amalfi_cliff": {
        "label": "런웨이 슬림 아말피 해안",
        "tier": "SS",
        "tags": ["korean","runway","slim","amalfi","cliff"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, impossibly long legs on Amalfi cliff, late-20s, "
            "Korean features, warm golden Mediterranean skin, long dark hair in Mediterranean wind, expression coastal and commanding. "
            "Wearing: ultra-minimal cobalt blue micro string bikini — tiny on slim tall frame, "
            "cobalt blue patent platform stiletto wedge 5-inch on cliff path, single gold ear cuff, gold anklet. "
            "Environment: Amalfi Coast cliff path, dramatic cliffside dropping to turquoise Tyrrhenian Sea below, colorful Amalfi village on cliff behind. "
            "Lighting: Mediterranean noon direct from above + turquoise sea reflection upward, golden Mediterranean skin in dual light, extreme tall figure over Amalfi drama. "
            "Style: Korean runway 185cm+ Amalfi Coast cliff Mediterranean editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Amalfi runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_berlin_underground": {
        "label": "런웨이 슬림 베를린 언더그라운드",
        "tier": "SS",
        "tags": ["korean","runway","slim","berlin","techno"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure as weapon in dark space, mid-20s, "
            "Korean features, porcelain skin cold in strobe light, severe architectural silver bob, cold industrial expression. "
            "Wearing: ultra-minimal black PVC micro bodysuit, bodysuit cut extreme high on endless long legs, "
            "black chrome thigh-high platform stiletto boots 6-inch on concrete floor, chrome chain harness over bodysuit, chrome geometric ear cuffs. "
            "Environment: Berlin underground techno club, raw concrete industrial, strobe cutting darkness, fog machine ground level. "
            "Lighting: strobe hard white cutting through dark + ground fog diffusing, porcelain skin in strobe cuts, silver bob catching strobe as silver flash. "
            "Style: Korean runway 185cm+ Berlin underground industrial editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Berlin runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_bali_temple_gold": {
        "label": "런웨이 슬림 발리 사원 골드",
        "tier": "SS",
        "tags": ["korean","runway","slim","bali","temple"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, 22 years old — first season runway youth, "
            "Korean features, warm golden skin in Bali temple amber, long straight dark hair with frangipani flower, expression serene and commanding. "
            "Wearing: ultra-minimal gold micro string bikini — tiny gold triangles on slim young frame, "
            "gold platform stiletto sandal 5-inch on Bali stone path, layered gold chains, gold coin drop earrings. "
            "Environment: Bali Hindu temple, intricate stone carved walls with moss, temple lanterns warm amber, incense smoke, tropical flowers. "
            "Lighting: temple lantern warm amber, golden-honey young skin in Bali amber, gold bikini on temple gold total palette. "
            "Style: Korean runway 185cm+ 22 Bali temple gold editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Bali runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_kyoto_autumn": {
        "label": "런웨이 슬림 교토 단풍",
        "tier": "SS",
        "tags": ["korean","runway","slim","kyoto","autumn"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Korean features, "
            "luminous porcelain skin in autumn dappled light, severe sleek center-part platinum hair, expression serene and distant in autumn beauty. "
            "Wearing: ultra-minimal cream silk micro slip dress, spaghetti straps invisible on slim frame, "
            "dress riding micro-length on endless long legs, clear platform stiletto mules 6-inch on Kyoto stone path, single maple leaf in hair, tiny pearl studs. "
            "Environment: Kyoto autumn, maples blazing red-orange-gold, stone path through autumn tunnel, ancient temple gate visible, fallen leaves. "
            "Lighting: Kyoto autumn dappled from canopy in red-gold-orange, porcelain skin in warm autumn dapple, cream silk catching autumn warmth. "
            "Style: Korean runway 185cm+ Kyoto autumn cream editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Kyoto autumn runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_palawan_karst": {
        "label": "런웨이 슬림 팔라완 카르스트",
        "tier": "SS",
        "tags": ["korean","runway","slim","palawan","karst"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, mid-20s, Filipino-Korean mixed features, "
            "warm golden-honey skin, long straight dark hair in sea wind, expression coastal commanding. "
            "Wearing: ultra-minimal white micro string bikini, micro thong, clear platform stiletto wedge mules 5-inch on white Palawan sand, "
            "single delicate gold anklet, tiny gold studs. "
            "Environment: El Nido Palawan, dramatic limestone karst cliffs towering above and behind extreme tall figure, turquoise lagoon water, hidden beach total. "
            "Lighting: Palawan tropical noon direct from above + turquoise lagoon reflection upward, golden-honey skin in tropical dual, massive karst cliffs scale backdrop. "
            "Style: Korean runway 185cm+ Palawan karst beach editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Palawan runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_aurora_finland": {
        "label": "런웨이 슬림 핀란드 오로라",
        "tier": "SSS",
        "tags": ["korean","runway","slim","finland","aurora"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure under aurora, mid-20s, Korean features, "
            "porcelain skin cold in aurora light, ice-white center-part hair, awe-struck cold expression. "
            "Wearing: ultra-minimal silver micro string bikini — silver on porcelain slim frame, "
            "silver chrome thigh-high platform stiletto boots 6-inch on Finland snow, silver fox fur stole draped extreme tall shoulders only. "
            "Environment: Finnish Lapland wilderness, massive aurora borealis green-purple filling sky above extreme tall figure, frozen lake reflection, pine silhouettes. "
            "Lighting: aurora green-purple from sky filling everything + snow reflection below, porcelain skin in aurora color wash, silver bikini as aurora mirror. "
            "Style: Korean runway 185cm+ Finland aurora silver editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Finland aurora runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_sahara_wind": {
        "label": "런웨이 슬림 사하라 바람",
        "tier": "SS",
        "tags": ["korean","runway","slim","sahara","desert"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure on sand dune crest, mid-20s, Korean features, "
            "golden-tan skin in Sahara sunset, long straight dark hair streaming horizontal in desert wind, expression fierce and free. "
            "Wearing: ultra-minimal burnt orange micro string bikini, micro thong, gold platform sandal wedge 5-inch on dune crest, layered gold chains, gold drop earrings. "
            "Environment: Sahara desert at golden sunset, massive orange sand dune crests, sun touching horizon blazing, camel silhouette in distance, total orange gold. "
            "Lighting: Sahara setting sun from horizon + sand reflection below, golden-tan skin in extreme warm orange, extreme tall slim silhouette as orange dune sculpture. "
            "Style: Korean runway 185cm+ Sahara sunset wind editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, Sahara runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_seychelles_granite": {
        "label": "런웨이 슬림 세이셸 화강암",
        "tier": "SS",
        "tags": ["korean","runway","slim","seychelles","granite"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure towering over Seychelles granite, mid-20s, Korean features, "
            "warm golden-honey skin in Indian Ocean light, long dark hair wild in ocean wind, expression commanding. "
            "Wearing: ultra-minimal turquoise micro string bikini — tiny turquoise against golden skin and pink granite, "
            "bare feet on smooth pink granite, single turquoise drop earring, turquoise anklet. "
            "Environment: Seychelles Anse Source d'Argent, massive smooth pink granite boulders, turquoise Indian Ocean between granite gaps, palm fronds. "
            "Lighting: Seychelles golden afternoon + turquoise ocean reflection between granite, golden skin in dual light, extreme tall figure over granite. "
            "Style: Korean runway 185cm+ Seychelles pink granite editorial. "
            "Shot on Hasselblad X2D, 8K UHD, Seychelles runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_tattoo_collarbone_void": {
        "label": "런웨이 슬림 쇄골타투 보이드",
        "tier": "SSS",
        "tags": ["korean","runway","slim","tattoo","collarbone"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure, collarbone and sternum tattoo — "
            "fine-line geometric mandala spreading from sternum across both collarbones as natural necklace effect, "
            "mid-20s, Korean features, porcelain skin cold, severe black hair architectural bun, cold haughty expression. "
            "Wearing: ultra-minimal black micro string bikini — thin strings disappearing on slim frame, collarbone tattoo as sole jewelry, "
            "black patent thigh-high platform stiletto boots 6-inch, no other accessories. "
            "Environment: pure white infinity studio, single overhead hard spot. "
            "Lighting: hard overhead spot + white bounce below, porcelain skin in white bilateral, sternum tattoo as editorial jewelry in hard light. "
            "Style: Korean runway 185cm+ collarbone tattoo white void editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, white void runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_newyork_snowstorm": {
        "label": "런웨이 슬림 NYC 눈보라",
        "tier": "SS",
        "tags": ["korean","runway","slim","nyc","blizzard"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure in NYC snowstorm, mid-20s, Korean features, "
            "porcelain skin cold in snowstorm, severe slicked-back platinum hair, fierce cold expression — immune to blizzard. "
            "Wearing: ultra-minimal black micro string bikini — absolute minimum against snowstorm, "
            "black patent thigh-high platform stiletto boots 6-inch in snow-wet NYC sidewalk, single crystal drop earring. "
            "Environment: NYC winter blizzard, snow falling heavy, 5th Avenue storefronts in snow behind, yellow taxi blurred, streetlamps in snow haze. "
            "Lighting: NYC snowstorm diffused cold from overcast + streetlamp warm from street, porcelain skin in cold-warm contrast, snowflakes visible falling around extreme tall figure. "
            "Style: Korean runway 185cm+ NYC blizzard cold editorial. "
            "Shot on Hasselblad X2D, 8K UHD, NYC blizzard runway grade, portrait 2:3 vertical."
        ),
        "aspect_ratio": "2:3",
    },
    "runway_korean_slim_crystal_gala": {
        "label": "런웨이 슬림 크리스탈 갈라",
        "tier": "SSS",
        "tags": ["korean","runway","slim","crystal","gala"],
        "prompt": (
            "Professional fashion photograph, full body shot. "
            "Model: Korean runway goddess, 185cm+ extreme tall slim figure at crystal gala, mid-20s, Korean features, "
            "luminous porcelain skin in chandelier prism light, elaborate silver-white architectural updo with crystal pins, regal cold expression. "
            "Wearing: ultra-minimal crystal micro gown — crystal fringe barely covering slim tall figure, "
            "crystal platform stiletto heels 6-inch on marble ballroom floor, massive crystal drop earrings, crystal body chain. "
            "Environment: grand European ballroom, massive crystal chandelier directly above extreme tall figure, gilded walls, mirror panels multiplying, marble floor reflecting. "
            "Lighting: crystal chandelier from above scattering prismatic light in all directions + marble reflection from below, "
            "luminous skin in prismatic crystal scatter, extreme tall figure as chandelier crystal itself. "
            "Style: Korean runway 185cm+ crystal gala chandelier editorial. "
            "Shot on Phase One XF IQ4, 8K UHD, crystal gala runway grade, portrait 2:3 vertical."
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

print(f"\n✅ Runway Slim 한국인 20종 JSON 생성 완료: {count}개 신규 생성")
