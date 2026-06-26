"""
patch_20260626_korean_historical.py
👑 한국 역사 & 궁중 글래머 — 78종 신설

작업:
1. dashboard.py PRESET_CATEGORIES에 새 카테고리 추가
2. presets/ 디렉토리에 JSON 78개 생성
3. SSS_TIER / SS_TIER 추가

컨셉: 전통 아이덴티티 + LumineX 글래머 극대화
(시스루/하이슬릿/라텍스/오일드/극노출 + 전통 배경/소품/복식 싱크)
"""

import json
import os
from pathlib import Path

DASHBOARD = r"C:\Dev\LumineX\dashboard.py"
PRESETS_DIR = r"C:\Dev\LumineX\presets"

# ══════════════════════════════════════════════════════════
# 78종 프리셋 정의 (key → preset dict)
# ══════════════════════════════════════════════════════════
KOREAN_HISTORICAL_PRESETS = {

    # ── 🏯 삼국/고대 왕실 (10종) ──────────────────────────
    "silla_queen_gold": {
        "subject": "a stunning Korean model as Silla queen goddess",
        "environment": "ancient Silla golden palace interior, ornate golden pillars, flickering torchlight, Gyeongju night",
        "outfit": "sheer gold silk royal robe draped over body, gold crown, minimal coverage beneath, deep plunging neckline, extreme high slit skirt",
        "material": "ultra-sheer gold silk, metallic gold foil accents, jeweled accessories",
        "lighting": "warm golden torchlight, dramatic chiaroscuro, oiled skin glow",
        "style": "Vogue Italia high-fashion editorial, ancient Korea meets luxury glamour",
        "quality": "ultra-sharp 8K, professional fashion photography, hyperrealistic skin",
        "mood": "powerful divine queen energy, ancient mystique",
        "body_oil": "heavy golden body oil, glistening oiled skin",
    },
    "silla_dancing_girl": {
        "subject": "a stunning Korean model as Silla sword dance warrior beauty",
        "environment": "Cheomseongdae observatory at night, flickering torches, ancient Silla stone walls, moonlight",
        "outfit": "traditional sword dance costume heavily modified — sheer silk cutout top, extreme high slit, bare midriff, holding two swords",
        "material": "sheer silk, gold thread embroidery, metallic accents",
        "lighting": "dramatic torchlight, rim lighting on oiled skin, moonlight backdrop",
        "style": "Harper's Bazaar sensual fashion editorial, warrior glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "fierce warrior beauty, dynamic sword pose",
        "body_oil": "medium body oil, glistening athletic skin",
    },
    "baekje_lotus_queen": {
        "subject": "a stunning Korean model as Baekje lotus queen",
        "environment": "ancient Baekje Sabi palace ruins at golden sunset, lotus pond reflection, stone lanterns",
        "outfit": "sheer white silk draped robe with lotus flower patterns, deep plunging neckline, thigh-high slit, lotus crown headpiece",
        "material": "ultra-sheer white silk organza, delicate lotus embroidery, pearl accessories",
        "lighting": "golden sunset backlight, soft ethereal glow, luminous skin",
        "style": "Vogue editorial, ancient Baekje elegance meets luxury glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "serene yet sensual, divine feminine energy",
        "body_oil": "light satin glow, radiant skin",
    },
    "goguryeo_warrior_queen": {
        "subject": "a stunning Korean model as Goguryeo warrior queen",
        "environment": "Gwanggaeto stele stone wall at night, dramatic storm clouds, ancient fortress gate, flickering torches",
        "outfit": "leather armor corset with extreme cutouts revealing body, arm guards, thigh-high boots, minimal coverage battle outfit, war paint",
        "material": "dark leather, iron studs and chains, battle-worn texture",
        "lighting": "dramatic storm lightning, harsh rim light on muscular oiled body",
        "style": "Alexander McQueen dark editorial, warrior goddess glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "fierce commanding warrior queen, raw power",
        "body_oil": "heavy oiled glistening warrior skin",
    },
    "gojoseon_shaman_queen": {
        "subject": "a stunning Korean model as ancient Gojoseon shaman queen",
        "environment": "ancient dolmen stone at moonlight, ritual fire, mysterious fog, prehistoric Korea night",
        "outfit": "sheer hemp cloth draped minimally, jade and bone jewelry covering body, ritual body paint markings, barefoot",
        "material": "sheer natural hemp, jade accessories, ritual body paint",
        "lighting": "ritual fire glow, blue moonlight, mystical atmospheric light",
        "style": "avant-garde editorial, prehistoric shaman goddess",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "ancient mystical power, primordial feminine energy",
        "body_oil": "oiled ritual skin, earth tones body paint",
    },
    "gaya_iron_goddess": {
        "subject": "a stunning Korean model as Gaya iron kingdom goddess",
        "environment": "ancient Gaya iron forge, molten metal glow, sparks flying, iron weapons display",
        "outfit": "iron-studded leather corset minimal outfit, thigh-high iron-detail boots, iron crown, extreme cutouts",
        "material": "dark iron-detailed leather, metallic accents, studded hardware",
        "lighting": "dramatic forge fire glow, orange and red light on oiled dark skin",
        "style": "Thierry Mugler power fashion, ancient forge goddess",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "industrial ancient power, dominant forge goddess",
        "body_oil": "heavy oiled skin glistening in forge light",
    },
    "silla_hwarang_girl": {
        "subject": "a stunning Korean model as female Silla Hwarang warrior beauty",
        "environment": "Cheomseongdae observatory moonlight, ancient Silla stone architecture, cherry blossoms",
        "outfit": "Hwarang armor heavily modified as corset, extreme high slit silk trousers, bare midriff, sword at hip",
        "material": "lacquered leather armor corset, sheer silk, metallic gold accents",
        "lighting": "moonlight editorial, cherry blossom petal rain, soft dramatic light",
        "style": "Vogue editorial, ancient Korean warrior elegance",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "elegant yet deadly, disciplined beauty",
        "body_oil": "satin glow oiled skin",
    },
    "ancient_mural_goddess": {
        "subject": "a stunning Korean model as living Goguryeo tomb mural goddess",
        "environment": "inside ancient Goguryeo burial mound, mural paintings surrounding, candle flame light, ancient stone chamber",
        "outfit": "Goguryeo mural painting patterns as full body paint, minimal actual clothing, body art as costume, barefoot",
        "material": "full body paint in Goguryeo mural style — red orange black patterns, ancient decorative motifs covering entire body",
        "lighting": "single candle flame light, deep shadow, mysterious ancient glow",
        "style": "avant-garde art editorial, living mural goddess",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "ancient living art, supernatural beauty",
        "body_oil": "matte body paint finish",
    },
    "three_kingdoms_spy": {
        "subject": "a stunning Korean model as Three Kingdoms era female spy",
        "environment": "ancient fortress wall at night, moonlight, Baekje stone gate, shadow and darkness",
        "outfit": "black sheer silk minimal spy outfit, black harness straps, thigh-high slit, shadow cloak barely covering, dark body",
        "material": "ultra-sheer black silk, black leather harness, shadow fabric",
        "lighting": "moonlight edge lighting only, deep shadow, dramatic contrast",
        "style": "film noir editorial, ancient Korean spy thriller glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "mysterious deadly beauty, shadow seduction",
        "body_oil": "dark oiled skin in moonlight",
    },
    "dongye_tribal_queen": {
        "subject": "a stunning Korean model as ancient Dongye tribal queen",
        "environment": "ancient tribal bonfire night, forest clearing, ritual drums, prehistoric Korean wilderness",
        "outfit": "tribal leather micro outfit, bone and feather accessories, tribal body paint covering arms and face, fur accents",
        "material": "leather strips, bone jewelry, tribal body paint, natural materials",
        "lighting": "dramatic bonfire glow, warm orange light on bronzed oiled skin",
        "style": "editorial tribal goddess, primordial Korean beauty",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "wild primal queen energy, tribal power",
        "body_oil": "heavy bronzed oiled tribal skin",
    },

    # ── 🏰 고려 궁중 (8종) ────────────────────────────────
    "goryeo_empress_silk": {
        "subject": "a stunning Korean model as Goryeo dynasty empress",
        "environment": "Goryeo imperial palace Gaekyeong at night, celadon ceramic displays, silk curtains, moonlight through palace windows",
        "outfit": "Goryeo silk royal robe dramatically modified — deep plunging neckline, extreme thigh-high slit, gold embroidered edges, royal crown",
        "material": "liquid silk, gold thread embroidery, celadon green and deep burgundy, pearl and jade accessories",
        "lighting": "candlelight warm glow, gold rim lighting, oiled skin luminosity",
        "style": "Vogue Paris editorial, Goryeo dynasty luxury glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "regal dominant empress, ancient luxury",
        "body_oil": "satin glow royal skin",
    },
    "goryeo_gisaeng_glam": {
        "subject": "a stunning Korean model as Goryeo era gisaeng entertainer",
        "environment": "Goryeo pavilion at moonlight, celadon blue-green backdrop, silk screen panels, lotus pond reflection",
        "outfit": "Goryeo silk entertainer costume — ultra-sheer silk top barely covering, extreme high slit skirt, layered transparent silk, elaborate hair ornaments",
        "material": "ultra-sheer Goryeo silk, celadon color palette, gold accessories",
        "lighting": "moonlit pavilion, soft celadon-toned light, glowing skin",
        "style": "Harper's Bazaar editorial, Goryeo gisaeng luxury",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "alluring entertainer, refined sensuality",
        "body_oil": "luminous oiled skin in moonlight",
    },
    "goryeo_celadon_goddess": {
        "subject": "a stunning Korean model as Goryeo celadon pottery goddess",
        "environment": "ancient Goryeo kiln site, celadon pottery surrounding, blue-green glaze glow, kiln fire backdrop",
        "outfit": "celadon blue-green sheer bodysuit, ceramic pattern body paint on exposed skin, minimal coverage, barefoot",
        "material": "sheer celadon-colored silk bodysuit, celadon glaze pattern body art",
        "lighting": "kiln fire warm glow, celadon blue-green ambient light",
        "style": "avant-garde art editorial, living celadon goddess",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "artistic divine beauty, living pottery",
        "body_oil": "celadon glaze-like glossy skin",
    },
    "goryeo_buddhist_temptress": {
        "subject": "a stunning Korean model as Goryeo Buddhist painting temptress",
        "environment": "Goryeo temple interior, Buddhist painting murals, incense smoke, golden candlelight altar",
        "outfit": "gold-leaf Buddhist mural pattern body paint as primary outfit, sheer white silk draped minimally, lotus flower accessories",
        "material": "gold leaf body paint, sheer white silk, Buddhist gold and crimson motifs",
        "lighting": "dramatic candlelight, incense smoke atmospheric, gold altar glow",
        "style": "avant-garde sacred editorial, Goryeo Buddhist art glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "sacred yet seductive, divine temptress",
        "body_oil": "gold gleaming oiled skin",
    },
    "goryeo_court_dancer": {
        "subject": "a stunning Korean model as Goryeo royal court dancer",
        "environment": "Goryeo palace banquet hall, silk banners, royal audience, candlelight ceremony",
        "outfit": "Goryeo jeongjaemu dance costume — sheer silk cutout design, extreme high slit allowing leg movement, elaborate sleeve dance, floor-length sheer",
        "material": "sheer layered silk in royal colors, gold embroidery, flowing dance sleeves",
        "lighting": "dramatic banquet candlelight, spot on dancer, silk shimmer",
        "style": "Vogue editorial, royal court dance glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "elegant performance beauty, royal dancer grace",
        "body_oil": "subtle satin glow dancing skin",
    },
    "goryeo_night_gisaeng": {
        "subject": "a stunning Korean model as Goryeo midnight gisaeng",
        "environment": "Goryeo pavilion at midnight, moonlight reflection on pond, weeping willow, silk lanterns",
        "outfit": "black sheer silk Goryeo robe, deep plunging neckline, thigh-high slit, silk barely draped over body, single shoulder exposed",
        "material": "ultra-sheer black silk, midnight blue accents, moonlit fabric",
        "lighting": "moonlight only, deep shadows, silver rim light on oiled skin",
        "style": "Givenchy dark luxury editorial, midnight Goryeo glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "mysterious midnight seduction, dark luxury",
        "body_oil": "moonlit oiled skin glow",
    },
    "mongol_goryeo_queen": {
        "subject": "a stunning Korean model as Mongol-Goryeo hybrid queen",
        "environment": "Yuan dynasty Mongolian imperial palace, silk tent interior, exotic decor, candlelight",
        "outfit": "Mongolian-Goryeo fusion corset outfit — leather corset with silk panels, extreme cutouts, thigh boots, elaborate headdress mixing both cultures",
        "material": "leather and silk fusion, Mongolian gold hardware, Goryeo silk panels",
        "lighting": "exotic candlelight, warm nomadic tent glow, oiled skin shimmer",
        "style": "Dolce and Gabbana exotic editorial, cultural fusion glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "exotic powerful hybrid queen, cultural collision",
        "body_oil": "warm bronzed oiled skin",
    },
    "goryeo_haenyeo_silk": {
        "subject": "a stunning Korean model as Goryeo era Haenyeo sea goddess",
        "environment": "Jeju island sea cliff at sunset, crashing waves, golden water reflection, ancient Goryeo Jeju landscape",
        "outfit": "traditional Haenyeo white cotton swimwear modified to micro bikini style, sheer wet silk wrap barely covering, soaking wet",
        "material": "wet sheer white cotton, transparent when wet, sea spray glistening",
        "lighting": "golden sunset, wet skin glistening, wave spray light",
        "style": "Sports Illustrated swimsuit editorial, ancient Haenyeo glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "powerful natural sea beauty, wet goddess",
        "body_oil": "extreme wet-look glistening sea-soaked skin",
    },

    # ── 👘 조선 왕실/궁중 (12종) ──────────────────────────
    "joseon_queen_slit": {
        "subject": "a stunning Korean model as Joseon dynasty queen in glamour interpretation",
        "environment": "Gyeongbokgung palace Geunjeongjeon hall at night, golden lanterns, stone floor reflection, royal court setting",
        "outfit": "Joseon queen daeryebok royal robe dramatically reinterpreted — ultra-deep plunging neckline exposing cleavage, extreme thigh-high slit, gold-embroidered silk barely covering, royal crown",
        "material": "liquid silk royal robe, gold embroidery, jade and gold royal accessories",
        "lighting": "golden lantern glow, dramatic palace lighting, luminous oiled skin",
        "style": "Vogue Italia high-fashion editorial, Joseon dynasty luxury meets maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography, hyperrealistic",
        "mood": "supreme queen power, regal dominance, sensual authority",
        "body_oil": "golden satin glow royal skin",
    },
    "joseon_consort_sheer": {
        "subject": "a stunning Korean model as Joseon royal consort",
        "environment": "Changdeokgung secret garden Huwon at moonlight, lotus pond, stone lanterns, weeping willows",
        "outfit": "Joseon consort silk jeogori robe — ultra-sheer white silk, visible through fabric, extreme thigh slit chima skirt, lotus flower hair ornaments",
        "material": "ultra-sheer white silk, transparent moonlit fabric, pearl accessories",
        "lighting": "moonlight through silk, ethereal blue-white glow, translucent skin effect",
        "style": "Harper's Bazaar sensual editorial, moonlit Joseon beauty",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "ethereal secret garden beauty, forbidden sensuality",
        "body_oil": "luminous moonlit skin glow",
    },
    "crown_princess_latex": {
        "subject": "a stunning Korean model as Joseon crown princess in latex fusion",
        "environment": "Gyeongbokgung Geunjeongjeon throne room, golden pillars, royal red carpet, dramatic palace night",
        "outfit": "latex-hanbok fusion — glossy black latex corset shaped like jeogori, silk chima skirt with extreme slit, royal crown, OTK patent boots",
        "material": "glossy black latex, silk panels, gold royal embroidery details, patent leather boots",
        "lighting": "dramatic palace spotlight, latex gleam, high-contrast glamour",
        "style": "Thierry Mugler power fashion, Joseon royal latex glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "dominant royal power, dark luxury queen",
        "body_oil": "latex-gleam oiled skin",
    },
    "joseon_court_dancer": {
        "subject": "a stunning Korean model as Joseon royal court jeongjaemu dancer",
        "environment": "Joseon palace banquet hall, silk screen paintings, candlelit ceremony, royal audience watching",
        "outfit": "jeongjaemu dance hanbok — sheer silk cutout layers, extreme high slit skirt, long flowing dance sleeves with cutout shoulders, flower crown",
        "material": "sheer layered silk, traditional Korean court dance colors, gold accents",
        "lighting": "ceremonial candlelight, dramatic spotlight on dancer, silk shimmer",
        "style": "Vogue editorial, Joseon court dance maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "graceful performance art, royal elegance",
        "body_oil": "subtle satin glow",
    },
    "joseon_painter_nude": {
        "subject": "a stunning Korean model as Shin Yun-bok Miin-do beauty painting come to life",
        "environment": "Joseon painting studio at candlelight, ink brushes and paper, traditional Korean art studio",
        "outfit": "Shin Yun-bok Miin-do painting style — traditional hanbok loosely draped, partially undone jeogori, extreme exposure, painted body art details",
        "material": "loosely draped silk, ink painting patterns on skin, traditional Korean aesthetics",
        "lighting": "single candle studio light, ink wash atmosphere, dramatic shadows",
        "style": "avant-garde art editorial, living Korean painting",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "artistic erotic beauty, living masterpiece",
        "body_oil": "luminous painting-like skin",
    },
    "hwajeon_court_lady": {
        "subject": "a stunning Korean model as Joseon court lady at hwajeon spring festival",
        "environment": "Joseon palace garden in spring bloom, cherry blossoms everywhere, flower petals falling, daytime golden light",
        "outfit": "spring festival hanbok — sheer floral silk, flower-printed transparent fabric, extreme high slit, flower petal accessories scattered on body",
        "material": "sheer flower-printed silk, petals decorating exposed skin, spring colors",
        "lighting": "golden spring sunlight through blossoms, petal rain, luminous glow",
        "style": "Vogue spring editorial, Joseon flower festival maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "sensual spring bloom beauty, floral abundance",
        "body_oil": "dewy spring skin glow",
    },
    "joseon_merchant_woman": {
        "subject": "a stunning Korean model as Joseon market merchant woman",
        "environment": "Joseon night market street, lantern light, bustling market stalls, wooden storefronts at night",
        "outfit": "Joseon commoner woman outfit reinterpreted — low-cut loose jeogori, short high-slit chima, exposed midriff, casual but provocative",
        "material": "cotton and linen, natural fabric, casual Korean traditional",
        "lighting": "warm lantern light, night market amber glow, natural skin luminosity",
        "style": "editorial street beauty, Joseon commoner glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "confident street beauty, accessible sensuality",
        "body_oil": "natural healthy skin glow",
    },
    "damo_warrior": {
        "subject": "a stunning Korean model as Joseon female damo investigator warrior",
        "environment": "Joseon poheung investigative office courtyard at night, interrogation setting, torchlight, stone floor",
        "outfit": "damo uniform dramatically modified — black leather corset top, high-slit dark trousers, leather harness straps, damo badge, sword at hip",
        "material": "dark leather, silk underpinning visible, black hardware harness",
        "lighting": "dramatic torchlight, hard shadows, powerful rim light",
        "style": "Alexander McQueen dark editorial, Joseon detective glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "powerful investigator dominance, dark authority beauty",
        "body_oil": "medium oiled strong skin",
    },
    "joseon_night_queen": {
        "subject": "a stunning Korean model as Joseon queen prowling at night",
        "environment": "Gyeongbokgung palace moonlit corridors at midnight, stone floor reflection, full moon, absolute silence",
        "outfit": "all-black sheer silk Joseon robe, ultra-transparent in moonlight, extreme slit, black royal crown, barefoot on cold stone",
        "material": "ultra-sheer black silk, moonlight-transparent fabric",
        "lighting": "full moonlight only, blue-silver light, dramatic deep shadows",
        "style": "Givenchy dark luxury editorial, midnight Joseon queen",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "dark dangerous queen, midnight power",
        "body_oil": "moonlit oiled dark skin",
    },
    "joseon_concubine_red": {
        "subject": "a stunning Korean model as Joseon royal concubine in red",
        "environment": "Joseon palace private chamber deep night, red silk curtains, candlelight, silk bedding visible",
        "outfit": "red latex-silk fusion concubine outfit — red latex corset shaped as jeogori, extreme deep plunge, sheer red chima with maximum slit, red accessories",
        "material": "red latex, red sheer silk, crimson accessories, gold detail",
        "lighting": "red candlelight, warm crimson glow, latex gleam",
        "style": "Versace bold glamour editorial, Joseon concubine red fantasy",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "seductive dangerous concubine, red power",
        "body_oil": "red-toned heavy oiled gleaming skin",
    },
    "changdeok_moonlight": {
        "subject": "a stunning Korean model at Changdeokgung palace moonlight",
        "environment": "Changdeokgung Huwon secret garden at full moon, lotus pond perfect reflection, ancient trees, stone bridge, silent night",
        "outfit": "white sheer silk hanbok — ultra-transparent white silk, moonlight visible through fabric, extreme slit, white lotus accessories, barefoot on stone",
        "material": "ultra-sheer white silk, moonlight-transparent, white jade accessories",
        "lighting": "full moonlight through silk, blue-white reflection on pond, ethereal glow",
        "style": "Vogue Italia ethereal editorial, Changdeokgung moonlight maximum beauty",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "ethereal moonlit beauty, transcendent femininity",
        "body_oil": "luminous moonlit satin skin",
    },
    "gyeongbokgung_geisha": {
        "subject": "a stunning Korean model at Gyeongbokgung palace night editorial",
        "environment": "Gyeongbokgung Heungnyemun gate at night, illuminated palace walls, stone lanterns, blue night sky",
        "outfit": "modern hanbok fusion glamour — sheer silk layers, architectural structure, deep plunge, extreme slit, contemporary luxury accessories",
        "material": "sheer modern silk, architectural hanbok structure, luxury accessories",
        "lighting": "palace illumination night, dramatic architectural light, skin luminosity",
        "style": "Vogue Korea editorial, Gyeongbokgung night maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "iconic Korean beauty, palace night editorial",
        "body_oil": "luminous editorial skin",
    },

    # ── 💃 기생/예인 (12종) ───────────────────────────────
    "gisaeng_joseon_sheer": {
        "subject": "a stunning Korean model as Joseon gisaeng entertainer",
        "environment": "Joseon gisaeng house gibang at night, red lanterns, silk screen rooms, candlelight, intimate setting",
        "outfit": "gisaeng silk hanbok — ultra-sheer silk jeogori with visible body beneath, extreme thigh-high slit chima, elaborate hair ornaments, silk robe falling off shoulder",
        "material": "ultra-sheer silk, transparent candlelit fabric, gold hair ornaments",
        "lighting": "red lantern candlelight, warm intimate glow, oiled skin luminosity",
        "style": "Harper's Bazaar sensual editorial, Joseon gisaeng maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "alluring entertainer, refined traditional seduction",
        "body_oil": "luminous oiled skin in red lantern light",
    },
    "gisaeng_red_lantern": {
        "subject": "a stunning Korean model as Joseon gisaeng under red lanterns",
        "environment": "Joseon night scene, dozens of red lanterns, dark street, red light everywhere, stone walls",
        "outfit": "red sheer silk gisaeng robe — maximum transparency, extreme cutout, barely covering body, red silk barely draped, extreme exposure",
        "material": "ultra-sheer red silk, red translucent fabric, minimal coverage",
        "lighting": "multiple red lanterns, all-red atmospheric glow, dramatic red light on skin",
        "style": "Vogue Italia dramatic editorial, red lantern maximum exposure",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "ultimate red seduction, dangerous beauty",
        "body_oil": "heavy oiled skin glowing red",
    },
    "gisaeng_sword_dance": {
        "subject": "a stunning Korean model as gisaeng sword dance performer",
        "environment": "outdoor torchlit stage at night, audience watching, dramatic smoke, fortress backdrop",
        "outfit": "sword dance costume extreme modification — sheer silk cutout dance outfit, extreme high slit, bare midriff, two swords as props",
        "material": "sheer silk, gold detail, dynamic dance-ready cutouts",
        "lighting": "dramatic torchlight, dynamic dance lighting, sparks and fire glow",
        "style": "Vogue performance editorial, sword dance glamour maximum",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "fierce beautiful dancer, dynamic warrior art",
        "body_oil": "athletic glistening dance skin",
    },
    "gisaeng_haiku_bath": {
        "subject": "a stunning Korean model as gisaeng in private bath ritual",
        "environment": "Joseon private bath chamber, ceramic bath, rose petals floating, candles surrounding, steam atmosphere",
        "outfit": "wet sheer white silk barely draped over body emerging from bath, water droplets on skin, silk clinging to body, flower petals on skin",
        "material": "wet transparent white silk, rose petals as decoration, steam atmosphere",
        "lighting": "candlelight bath glow, steam-diffused warm light, wet skin shimmer",
        "style": "boudoir luxury editorial, Joseon bath maximum intimacy",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "intimate sensual bath beauty, private luxury moment",
        "body_oil": "extreme wet-look bath skin, dripping",
    },
    "gisaeng_rain_dance": {
        "subject": "a stunning Korean model as gisaeng dancing in rain",
        "environment": "Joseon street at night in heavy rain, wet stone floor reflection, lantern light through rain, puddles",
        "outfit": "sheer white silk gisaeng hanbok completely soaked — transparent wet silk revealing body, hair soaked, wet silk clinging",
        "material": "soaking wet transparent white silk, completely see-through when wet",
        "lighting": "lantern light through rain, wet glistening reflections, rain-soaked atmospheric",
        "style": "dramatic rain editorial, Joseon wet beauty maximum",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "wild rain dance beauty, soaked uninhibited energy",
        "body_oil": "extreme wet-look rain-soaked skin",
    },
    "gisaeng_black_silk": {
        "subject": "a stunning Korean model as Joseon gisaeng in black silk",
        "environment": "Joseon pavilion at midnight, moonlight, minimal candlelight, black silk screen backdrop",
        "outfit": "black sheer silk gisaeng robe — ultra-transparent black silk, extreme plunge, thigh-high slit, black silk barely covering, moonlit",
        "material": "ultra-sheer black silk, midnight fabric, black jade accessories",
        "lighting": "single moonlight source, deep dramatic shadows, black silk against pale skin",
        "style": "Givenchy noir editorial, midnight gisaeng luxury",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "dark mysterious seduction, midnight danger",
        "body_oil": "moonlit pale oiled skin against black silk",
    },
    "wonhyang_legend": {
        "subject": "a stunning Korean model as legendary Nongae uinyeo warrior beauty",
        "environment": "Chokseongnu pavilion at Jinju, Nam River moonlight reflection, memorial stone, night atmosphere",
        "outfit": "Joseon uinyeo silk — sheer silk robe partially submerged at river edge, wet silk clinging to body, flower in hair, warrior dignity",
        "material": "wet sheer silk, river water, flower accessories, warrior dignity preserved",
        "lighting": "moonlight on river, dramatic reflection, powerful silhouette",
        "style": "editorial legendary beauty, historical heroism glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "heroic tragic beauty, legendary sacrifice",
        "body_oil": "water-soaked skin glistening in moonlight",
    },
    "hwang_jini_glam": {
        "subject": "a stunning Korean model as legendary gisaeng Hwang Jini",
        "environment": "Goryeo/Joseon era Songdo night, merchant district, scholar's pavilion, sophisticated setting",
        "outfit": "legendary gisaeng ultimate outfit — finest silk in deep jewel tones, ultra-sheer layers, maximum seductive exposure, ultimate beauty presentation",
        "material": "finest sheer jewel-tone silk, gold and jade accessories, maximum luxury",
        "lighting": "warm sophisticated candlelight, beauty dish on perfect face, golden skin glow",
        "style": "Vogue Italia ultra luxury editorial, legendary gisaeng maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "legendary beauty and intelligence, ultimate seduction mastery",
        "body_oil": "golden luxury oiled skin",
    },
    "gisaeng_fan_dance": {
        "subject": "a stunning Korean model as gisaeng buchaechum fan dancer",
        "environment": "outdoor moonlit stage, audience, dramatic night sky, atmospheric traditional festival",
        "outfit": "buchaechum fan dance costume modified — sheer silk panels, extreme slit allowing full leg movement, large decorative fans in both hands, hair ornaments",
        "material": "sheer silk panels, large painted fans, flowing transparent fabric",
        "lighting": "dramatic stage moonlight, fan spotlight, dynamic performance light",
        "style": "Vogue performance editorial, fan dance maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "graceful powerful fan performance, traditional art maximum beauty",
        "body_oil": "performance glow skin",
    },
    "gisaeng_pipa_night": {
        "subject": "a stunning Korean model as gisaeng pipa musician at night",
        "environment": "intimate Joseon pavilion at night, candlelight, silk cushions, intimate music setting",
        "outfit": "musician gisaeng silk — deep plunging jeogori barely covering, extreme slit chima, pipa instrument held in front, maximum seductive presentation",
        "material": "deep jewel-tone sheer silk, instrument as strategic prop",
        "lighting": "intimate candlelight, warm golden glow, musical atmosphere",
        "style": "intimate editorial, Joseon musician beauty",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "sophisticated musical seduction, artistic beauty",
        "body_oil": "warm candlelit glowing skin",
    },
    "gisaeng_mirror_boudoir": {
        "subject": "a stunning Korean model as gisaeng in private boudoir mirror scene",
        "environment": "Joseon gisaeng private room, large bronze mirror, red silk curtains, candles, intimate boudoir",
        "outfit": "private moment gisaeng — silk robe falling open, maximum exposure, dressing or undressing moment, red silk barely held",
        "material": "red and white silk robe falling open, intimate private moment",
        "lighting": "candlelight boudoir, mirror reflection doubling image, warm intimate glow",
        "style": "boudoir luxury editorial, Joseon intimate maximum exposure",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "private intimate seduction, mirror reflection beauty",
        "body_oil": "private boudoir glowing skin",
    },
    "pyongyang_gisaeng": {
        "subject": "a stunning Korean model as legendary Pyongyang gisaeng",
        "environment": "Pyongyang night scene, Daedong River reflection, traditional pavilion, romantic night atmosphere",
        "outfit": "Pyongyang gisaeng finest silk — distinctive regional style, sheer silk in Pyongyang palette, elaborate hair, maximum seductive presentation",
        "material": "finest sheer silk, regional Pyongyang gisaeng style, elaborate accessories",
        "lighting": "Daedong River moonlight, pavilion candlelight, romantic northern night",
        "style": "editorial legendary beauty, Northern Korea gisaeng glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "legendary Northern beauty, sophisticated regional seduction",
        "body_oil": "luminous moonlit northern skin",
    },

    # ── 🦊 신화 & 정령 (12종) ─────────────────────────────
    "gumiho_latex": {
        "subject": "a stunning Korean model as nine-tailed fox gumiho demon in latex",
        "environment": "moonlit bamboo forest, full moon, ancient Korean abandoned house, eerie blue atmosphere",
        "outfit": "fox-pattern latex full body — golden-red latex with nine tail motif, fox ears headpiece, nine CGI fox tails as accessories, extreme cutout, stiletto boots",
        "material": "golden-red latex with fox pattern, CGI fox tails, pointed ear accessories",
        "lighting": "full moonlight, blue eerie glow, latex reflection, supernatural light",
        "style": "dark fantasy editorial, gumiho latex maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography, fantasy CGI elements",
        "mood": "deadly seductive fox demon, supernatural danger",
        "body_oil": "latex gleam supernatural skin",
    },
    "gumiho_red_moon": {
        "subject": "a stunning Korean model as gumiho under blood moon",
        "environment": "blood moon night, abandoned Joseon manor, overgrown garden, eerie red atmosphere, supernatural mist",
        "outfit": "red sheer silk barely covering — blood-red transparent silk draped minimally, fox tail accessories, extreme exposure, supernatural styling",
        "material": "blood-red ultra-sheer silk, supernatural red glow fabric",
        "lighting": "blood moon red light only, dramatic red atmospheric glow, supernatural",
        "style": "dark fantasy horror glamour editorial, blood moon maximum danger",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "deadly supernatural seduction, blood moon danger",
        "body_oil": "red-toned supernatural glowing skin",
    },
    "samshin_goddess_glam": {
        "subject": "a stunning Korean model as Samshin grandmother goddess reborn as divine beauty",
        "environment": "above clouds, divine realm, golden celestial light, Korean mythological heaven",
        "outfit": "divine white silk robe — ultra-sheer white silk, celestial light through fabric, gold divine accessories, floating above clouds",
        "material": "ultra-sheer divine white silk, gold celestial accessories, cloud fabric",
        "lighting": "divine golden celestial backlight, glowing aura, supernatural luminosity",
        "style": "avant-garde divine editorial, Korean goddess maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography, divine CGI atmosphere",
        "mood": "divine maternal power, celestial beauty transcendence",
        "body_oil": "divine luminous celestial glow",
    },
    "dragon_daughter_sea": {
        "subject": "a stunning Korean model as dragon king's daughter underwater palace goddess",
        "environment": "underwater Korean dragon palace, bioluminescent sea creatures, coral formations, deep blue water glow",
        "outfit": "dragon scale body paint as primary outfit — iridescent blue-green dragon scales painted on body, sheer underwater silk barely draped, sea jewel accessories",
        "material": "dragon scale body paint, sheer underwater fabric, sea jewels and coral",
        "lighting": "bioluminescent underwater glow, blue-green deep sea light",
        "style": "dark fantasy underwater editorial, dragon daughter maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography, underwater CGI",
        "mood": "divine underwater dragon beauty, supernatural aquatic power",
        "body_oil": "wet glistening underwater skin",
    },
    "imoogi_seduction": {
        "subject": "a stunning Korean model as imoogi serpent spirit seductress",
        "environment": "waterfall cave interior, ancient Korean mountain waterfall, mist and spray, dramatic stone formations",
        "outfit": "snake scale latex body — iridescent serpent scale pattern latex covering body, extreme cutout, serpent tail accessories, minimal coverage",
        "material": "iridescent serpent scale latex, reptile texture, minimal coverage",
        "lighting": "waterfall spray light, cave dramatic shadow, iridescent scale reflection",
        "style": "dark fantasy editorial, imoogi serpent maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "dangerous serpent seduction, ancient mountain spirit power",
        "body_oil": "wet serpentine glistening skin",
    },
    "dokkaebi_girl": {
        "subject": "a stunning Korean model as female dokkaebi goblin spirit",
        "environment": "moonlit Korean forest at night, supernatural atmosphere, rocks and ancient trees, mischievous energy",
        "outfit": "dokkaebi costume reinterpreted — colorful sheer silk with dokkaebi pattern, goblin horn headpiece, dokkaebi club prop, extreme playful exposure",
        "material": "colorful sheer silk, goblin horn accessories, playful supernatural style",
        "lighting": "supernatural blue-green moonlight, mischievous glow, magical atmosphere",
        "style": "dark fantasy playful editorial, dokkaebi maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "mischievous supernatural beauty, playful dangerous goblin energy",
        "body_oil": "supernatural glowing skin",
    },
    "seonnyeo_descent": {
        "subject": "a stunning Korean model as seonnyeo heavenly fairy descending",
        "environment": "moonlit mountain pond, celestial clouds parting, divine light descending, lotus blossoms floating",
        "outfit": "cheonui heavenly robe — ultra-sheer five-color silk, barely draped celestial fabric, feather accessories, floating descent pose",
        "material": "ultra-sheer five-color celestial silk, feathers, divine floating fabric",
        "lighting": "divine descending light from above, ethereal backlight through silk, celestial glow",
        "style": "avant-garde celestial editorial, heavenly fairy maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography, celestial CGI",
        "mood": "divine celestial beauty, ethereal transcendence",
        "body_oil": "celestial luminous divine skin",
    },
    "haenyeo_mermaid": {
        "subject": "a stunning Korean model as Jeju haenyeo mermaid goddess",
        "environment": "Jeju underwater, coral and sea life, blue water light, surface shimmer above",
        "outfit": "haenyeo-mermaid fusion — iridescent mermaid scale body paint covering lower body, traditional haenyeo white top modified to micro coverage, soaking wet",
        "material": "mermaid scale body paint, wet white traditional fabric, sea elements",
        "lighting": "underwater blue-green light, surface shimmer, aquatic glow",
        "style": "fantasy underwater editorial, haenyeo mermaid maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "powerful aquatic goddess, haenyeo strength meets mermaid beauty",
        "body_oil": "extreme wet underwater glistening skin",
    },
    "baeksa_serpent": {
        "subject": "a stunning Korean model as white snake Baeksa spirit seductress",
        "environment": "heavy rain night, ancient Korean temple gates, rain-soaked stone, dramatic storm",
        "outfit": "white sheer silk rain-soaked — ultra-transparent white silk completely wet and clinging, white snake pattern, maximum see-through exposure",
        "material": "ultra-sheer white silk soaking wet, white serpent detail, transparent when wet",
        "lighting": "rain-soaked dramatic storm light, white in darkness, lightning flash",
        "style": "dark supernatural editorial, white snake maximum rain glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "supernatural rain seduction, white snake dangerous beauty",
        "body_oil": "extreme wet rain-soaked skin",
    },
    "chamsuri_ghost": {
        "subject": "a stunning Korean model as beautiful Joseon female ghost",
        "environment": "moonlit Joseon grave site, ancient stone memorial, night mist, eerie silence, blue moonlight",
        "outfit": "ghost sobok white — ultra-sheer white funeral silk, transparent ghost fabric barely there, pale ethereal presentation, hair down",
        "material": "ultra-sheer ghost white silk, ethereal transparent fabric",
        "lighting": "blue moonlight only, ethereal glow, ghostly atmospheric",
        "style": "supernatural horror glamour editorial, Korean ghost maximum beauty",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "beautiful tragic ghost, supernatural ethereal danger",
        "body_oil": "pale ghostly luminous skin",
    },
    "taoist_fairy_korea": {
        "subject": "a stunning Korean model as Korean Taoist immortal fairy",
        "environment": "Korean mythological paradise Sinseon realm, peach blossoms, crane birds, celestial mountains, divine atmosphere",
        "outfit": "five-color divine silk — layered sheer five-color Korean Taoist robes, transparent layers, crane feather accessories, maximum divine glamour",
        "material": "five-color sheer layered silk, crane feathers, divine accessories",
        "lighting": "paradise golden light, divine aura, peach blossom falling",
        "style": "avant-garde divine editorial, Korean Taoist paradise maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "divine immortal beauty, transcendent paradise femininity",
        "body_oil": "divine luminous immortal skin",
    },
    "nine_tail_dominatrix": {
        "subject": "a stunning Korean model as dominant gumiho fox dominatrix",
        "environment": "dark ancient Korean forest at night, full moon, supernatural power atmosphere, darkness surrounding",
        "outfit": "gumiho dominatrix fusion — black latex with gold fox patterns, nine tail whip accessories, fox ear headpiece, OTK boots, extreme cutout corset",
        "material": "black latex, gold fox pattern, chain accessories, dominatrix hardware",
        "lighting": "full moonlight, dramatic dark shadows, latex gold gleam, supernatural",
        "style": "dark fantasy dominatrix editorial, gumiho maximum power glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "ultimate supernatural dominance, deadly fox goddess power",
        "body_oil": "latex gleam supernatural dark skin",
    },

    # ── 🌊 민속 & 세시풍속 (8종) ──────────────────────────
    "haenyeo_wet_glam": {
        "subject": "a stunning Korean model as Jeju haenyeo sea diver goddess",
        "environment": "Jeju sea cliff at sunrise, crashing waves, volcanic black rock, turquoise water",
        "outfit": "haenyeo outfit reinterpreted as micro bikini — traditional white modified to string bikini coverage, wet and clinging, soaking wet, sea spray",
        "material": "wet white cotton micro coverage, sea spray glistening, traditional influence",
        "lighting": "sunrise golden light on wet skin, wave spray, dramatic cliff edge",
        "style": "Sports Illustrated swimsuit editorial, Jeju haenyeo maximum wet glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "powerful natural sea goddess, raw ocean beauty",
        "body_oil": "extreme wet-look sea-soaked glistening skin",
    },
    "dano_festival_glam": {
        "subject": "a stunning Korean model at Dano spring festival swing",
        "environment": "traditional Korean Dano festival, elaborate rope swing in flower garden, festival crowds blurred, spring blooms everywhere",
        "outfit": "Dano festival hanbok on swing — sheer silk flying in air, extreme high slit revealed in mid-swing, flower in hair, dynamic aerial pose",
        "material": "sheer festival silk, flying in wind, traditional spring colors",
        "lighting": "golden spring festival light, dynamic swing motion, flower petal rain",
        "style": "Vogue dynamic editorial, Dano festival swing maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "joyful festival beauty, dynamic aerial sensuality",
        "body_oil": "spring festival glowing skin",
    },
    "ganggangsullae_night": {
        "subject": "a stunning Korean model as ganggangsullae circle dance goddess",
        "environment": "Chuseok harvest moon seaside, massive full moon over ocean, circle of dancers in background, moonlit beach",
        "outfit": "ganggangsullae hanbok — sheer white silk, transparent in moonlight, flowing circular dance motion, hair flying, extreme high slit in movement",
        "material": "ultra-sheer white silk, moonlight transparent, flowing dance fabric",
        "lighting": "massive harvest moonlight, silver ocean reflection, ethereal night glow",
        "style": "Vogue editorial, harvest moon circle dance maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "transcendent harvest moon beauty, collective feminine power",
        "body_oil": "moonlit silver-toned glowing skin",
    },
    "mudang_fire_ritual": {
        "subject": "a stunning Korean model as mudang shaman in fire ritual",
        "environment": "outdoor mudang ritual gut, multiple fires, ritual altar, smoke and flames, night ceremony, ritual drums",
        "outfit": "mudang ritual costume extreme modification — sheer five-color silk cutout, extreme exposure allowing movement, ritual accessories, barefoot on ritual ground",
        "material": "five-color sheer silk, ritual accessories, fire-dancing movement",
        "lighting": "multiple fire sources, dramatic orange-red fire glow on skin, smoke atmosphere",
        "style": "avant-garde ritual editorial, mudang fire maximum power",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "supernatural ritual power, shaman fire goddess energy",
        "body_oil": "fire-lit oiled ritual skin",
    },
    "mudang_trance_glam": {
        "subject": "a stunning Korean model as mudang in divine trance state",
        "environment": "indoor ritual space, five-color silk banners everywhere, incense smoke, ritual objects, dramatic atmosphere",
        "outfit": "trance state mudang — five-color silk partially unwrapped in trance, maximum ritual exposure, divine possession state styling, ritual in hair",
        "material": "five-color silk unwinding, ritual accessories, trance exposure",
        "lighting": "ritual incense smoke light, five-color ambient atmospheric",
        "style": "avant-garde supernatural editorial, mudang trance maximum exposure",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "divine possession beauty, supernatural trance state",
        "body_oil": "ritual trance glowing skin",
    },
    "namsadang_acrobat": {
        "subject": "a stunning Korean model as Namsadang female acrobat performer",
        "environment": "traditional Korean performance outdoor stage, audience, dramatic sky, festival atmosphere",
        "outfit": "acrobat performance costume — tight sheer silk body-hugging outfit, extreme cutout for movement, acrobatic bare minimum coverage, aerial pose",
        "material": "sheer tight performance silk, minimal coverage for maximum movement",
        "lighting": "outdoor performance dramatic light, athletic body highlight",
        "style": "Vogue performance editorial, Korean acrobat maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "powerful athletic performance beauty, traditional circus glamour",
        "body_oil": "athletic glistening performance skin",
    },
    "jeju_shaman_sea": {
        "subject": "a stunning Korean model as Jeju simang sea shaman",
        "environment": "Jeju sea cliff ritual site, ocean crashing below, ritual flags, volcanic rock altar, sea wind",
        "outfit": "Jeju shaman ritual dress — white sheer silk wind-blown, extreme exposure in sea wind, ritual flags as accessories, barefoot on volcanic rock",
        "material": "wind-blown sheer white silk, sea spray soaked, ritual flags",
        "lighting": "ocean horizon dawn light, sea wind dramatic, ritual atmosphere",
        "style": "avant-garde sea ritual editorial, Jeju shaman maximum beauty",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "powerful sea ritual beauty, Jeju wind and ocean force",
        "body_oil": "sea-spray wet wind-blown skin",
    },
    "korean_harvest_goddess": {
        "subject": "a stunning Korean model as Chuseok harvest moon goddess",
        "environment": "golden harvest field at full moon, endless golden rice fields, massive harvest moon, traditional Korean countryside",
        "outfit": "harvest goddess hanbok — golden sheer silk, harvest colors, extreme high slit in golden fields, lunar crown headpiece",
        "material": "golden sheer silk, harvest color palette, lunar accessories",
        "lighting": "massive harvest moonlight, golden field glow, dual moon and field light",
        "style": "Vogue editorial, harvest moon goddess maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "abundant harvest goddess beauty, lunar feminine power",
        "body_oil": "golden harvest moonlit skin",
    },

    # ── ⚔️ 여전사 & 무인 (8종) ───────────────────────────
    "joseon_female_assassin": {
        "subject": "a stunning Korean model as Joseon female assassin",
        "environment": "Joseon rooftop tile at midnight, moonlit city below, shadow and stealth, dark Korean architecture",
        "outfit": "black assassin silk — ultra-sheer black silk skin-tight outfit, black harness straps, thigh-high slit, small daggers as accessories, shadow cloak",
        "material": "ultra-sheer black silk, black leather straps, shadow fabric",
        "lighting": "moonlight edge only, deep shadow, stealth dramatic contrast",
        "style": "Alexander McQueen dark editorial, Joseon assassin maximum dark glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "deadly silent beauty, midnight assassin power",
        "body_oil": "dark oiled stealth skin in moonlight",
    },
    "goryeo_archer_queen": {
        "subject": "a stunning Korean model as Goryeo female archer queen",
        "environment": "Goryeo fortress wall at night, stone battlements, moonlit landscape below, dramatic height",
        "outfit": "archer queen armor — leather corset cutout armor, extreme high-slit battle trousers, arm guards, longbow drawn, warrior battle ready",
        "material": "dark leather armor with cutouts, iron detail, battle accessories",
        "lighting": "moonlight battle scene, dramatic rim light on armor and skin",
        "style": "editorial warrior glamour, Goryeo archer maximum power beauty",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "commanding archer queen power, warrior dominance",
        "body_oil": "strong warrior oiled skin",
    },
    "silla_female_hwarang": {
        "subject": "a stunning Korean model as female Silla Hwarang elite warrior",
        "environment": "Cheomseongdae and Anapji pond Silla night, moonlit ancient architecture, cherry blossom falling",
        "outfit": "Hwarang elite armor modified — lacquered armor corset with deep cutouts, extreme high slit silk trousers, sword at hip, warrior flower crown",
        "material": "lacquered leather armor corset, sheer silk, gold hwarang detail",
        "lighting": "moonlit Silla palace, cherry blossom light, warrior dramatic",
        "style": "editorial warrior goddess, Silla hwarang maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "elite warrior beauty, disciplined deadly grace",
        "body_oil": "warrior satin glow skin",
    },
    "joseon_damo_noir": {
        "subject": "a stunning Korean model as Joseon damo detective in noir style",
        "environment": "Joseon interrogation room noir, single hanging light, dark stone room, suspect chair, dramatic shadow",
        "outfit": "damo noir — black leather corset damo outfit, chain harness, thigh-high patent boots, badge, maximum dark authority styling",
        "material": "black leather, chain harness, patent boots, dark authority",
        "lighting": "single harsh light, deep noir shadow, black and white-like contrast",
        "style": "film noir editorial, Joseon damo dominatrix power",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "dark authority dominance, noir detective power",
        "body_oil": "strong dark oiled noir skin",
    },
    "tiger_huntress_korea": {
        "subject": "a stunning Korean model as Joseon tiger huntress",
        "environment": "snow-covered Korean mountain forest at night, tiger tracks in snow, pine trees, dramatic winter scene",
        "outfit": "tiger huntress — tiger skin pattern leather micro outfit, extreme cutout, fur trim accents, hunting bow and arrow, warrior boots",
        "material": "tiger pattern leather, fur trim, hunting warrior accessories",
        "lighting": "snow reflection moonlight, cold blue-white dramatic light on bronzed skin contrast",
        "style": "editorial warrior huntress, Joseon tiger maximum power",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "fierce tiger huntress beauty, winter warrior power",
        "body_oil": "cold warrior skin glistening in snow light",
    },
    "wonhyang_warrior": {
        "subject": "a stunning Korean model as female Joseon military physician warrior",
        "environment": "Joseon battle aftermath, dramatic field at sunset, warrior context, medical kit",
        "outfit": "uinyeo warrior — white medical silk modified to extreme slit and cutout, warrior leather accents, medical kit as accessory, battle-ready beauty",
        "material": "white silk with warrior leather accents, battle-worn but glamorous",
        "lighting": "dramatic battle sunset, golden warrior light, heroic atmosphere",
        "style": "editorial warrior heroine, Joseon uinyeo maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "heroic warrior healer beauty, battlefield strength",
        "body_oil": "golden warrior sunset glowing skin",
    },
    "goguryeo_fire_warrior": {
        "subject": "a stunning Korean model as Goguryeo fire warrior goddess",
        "environment": "ancient battle with fire, Goguryeo fortress walls, flames everywhere, dramatic fire battle scene",
        "outfit": "fire warrior — burning armor effect costume, flame-pattern body paint on exposed skin, extreme cutout leather armor, fire as background element",
        "material": "leather armor with extreme cutouts, flame body paint, fire-resistant warrior",
        "lighting": "surrounding fire glow, dramatic orange-red fire light on oiled skin",
        "style": "Alexander McQueen dark fire editorial, Goguryeo fire maximum power",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "fire warrior goddess power, ancient battle rage beauty",
        "body_oil": "fire-lit heavy oiled warrior skin",
    },
    "joseon_spy_sheer": {
        "subject": "a stunning Korean model as Joseon female spy operative",
        "environment": "Joseon palace secret passage at night, narrow stone corridor, single torch, absolute stealth",
        "outfit": "spy silk — black ultra-sheer silk body-conforming outfit, strategic harness straps, absolute minimal coverage for stealth, shadow cloak element",
        "material": "ultra-sheer black silk, black leather harness minimal",
        "lighting": "single torch only, extreme shadow, stealth night light",
        "style": "dark thriller editorial, Joseon spy maximum dark glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "deadly spy beauty, stealth and danger",
        "body_oil": "dark stealth oiled skin",
    },

    # ── 🎭 근대 & 퓨전 (8종) ─────────────────────────────
    "joseon_modern_fusion": {
        "subject": "a stunning Korean model in Joseon-modern luxury fusion",
        "environment": "modern Gyeongbokgung palace at night with contemporary lighting, traditional meets ultra-modern",
        "outfit": "hanbok-modern fusion luxury — latex corset shaped as jeogori, contemporary high-fashion skirt with traditional pattern, stiletto heels, modern gold accessories",
        "material": "latex, contemporary silk, traditional pattern on modern cuts, luxury accessories",
        "lighting": "contemporary palace lighting, dramatic modern editorial light",
        "style": "Vogue Korea contemporary editorial, Joseon modern maximum luxury",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "contemporary Korean luxury, traditional identity modern power",
        "body_oil": "contemporary luxury glowing skin",
    },
    "gisaeng_cyberpunk": {
        "subject": "a stunning Korean model as cyberpunk future gisaeng",
        "environment": "futuristic neo-Seoul with holographic traditional Korean elements, neon hangeul signs, cyberpunk Joseon fusion",
        "outfit": "cyberpunk gisaeng — sheer silk with neon circuit patterns, holographic hanbok elements, cyber accessories, extreme cutout, neon makeup",
        "material": "neon-circuit sheer silk, holographic hanbok fabric, cyber accessories",
        "lighting": "neon cyberpunk light, holographic projections, electric atmosphere",
        "style": "Balenciaga avant-garde futuristic editorial, gisaeng cyberpunk maximum",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "futuristic gisaeng power, cyber-traditional fusion",
        "body_oil": "neon-lit cyberpunk glowing skin",
    },
    "hanbok_latex_queen": {
        "subject": "a stunning Korean model as latex hanbok queen",
        "environment": "Gyeongbokgung throne room at night, dramatic palace setting, royal court atmosphere",
        "outfit": "full latex hanbok — glossy black latex entire hanbok silhouette, plunging neckline, OTK patent boots, gold crown, maximum latex glamour",
        "material": "full glossy black latex, gold royal accessories, patent boots",
        "lighting": "dramatic palace spotlight, latex high-gloss reflection",
        "style": "Thierry Mugler power fashion, hanbok latex maximum dominance",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "ultimate hanbok latex queen dominance",
        "body_oil": "latex gleam oiled queen skin",
    },
    "joseon_noir": {
        "subject": "a stunning Korean model in 1930s Joseon noir glamour",
        "environment": "1930s Japanese colonial era Seoul, rain-soaked street, vintage shop signs, art deco influence, film noir atmosphere",
        "outfit": "1930s Joseon noir — dark silk hanbok modified with art deco glamour, deep plunge, high slit, vintage accessories, cigarette holder prop",
        "material": "dark silk, art deco details, vintage 1930s glamour accessories",
        "lighting": "1930s film noir, rain-soaked street light, black and white tones",
        "style": "film noir editorial, 1930s Joseon maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "mysterious 1930s noir beauty, colonial era dangerous glamour",
        "body_oil": "vintage noir pale glowing skin",
    },
    "gisaeng_opium_den": {
        "subject": "a stunning Korean model as 1920s gisaeng in opium den glamour",
        "environment": "1920s Shanghai-Seoul opium den, silk cushions, smoke and incense, art nouveau decor, exotic oriental atmosphere",
        "outfit": "1920s oriental gisaeng — sheer silk kimono-hanbok fusion, extreme exposure, vintage accessories, smoky opium den styling",
        "material": "sheer 1920s silk, art nouveau accessories, vintage orientalist glamour",
        "lighting": "opium den lamp glow, smoky atmospheric, warm vintage amber",
        "style": "editorial 1920s orientalist glamour, gisaeng maximum vintage",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "dangerous 1920s glamour, opium den seduction",
        "body_oil": "vintage amber-lit glowing skin",
    },
    "korean_vamp_modern": {
        "subject": "a stunning Korean model as Korean vampire in hanbok gothic",
        "environment": "gothic Joseon palace at night, blood moon, dark gothic architecture, supernatural atmosphere",
        "outfit": "hanbok vampire gothic — deep crimson silk with gothic elements, blood accents, fangs, extreme plunge, dark accessories, supernatural styling",
        "material": "deep crimson silk, gothic accessories, blood-themed details",
        "lighting": "blood moon light, gothic dramatic, crimson atmospheric",
        "style": "dark gothic editorial, Korean vampire hanbok maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "elegant Korean vampire beauty, gothic palace danger",
        "body_oil": "pale vampire gleaming skin",
    },
    "hanbok_wet_editorial": {
        "subject": "a stunning Korean model in wet hanbok editorial",
        "environment": "Gyeongbokgung palace in heavy rain, stone floor puddles reflecting palace, dramatic rain atmosphere",
        "outfit": "white silk hanbok completely soaked — ultra-transparent wet white silk hanbok clinging to body, rain-soaked, maximum wet see-through",
        "material": "ultra-sheer white silk completely transparent when wet, rain-soaked",
        "lighting": "rain-soaked palace dramatic, puddle reflections, rain drops glistening",
        "style": "dramatic rain editorial, wet hanbok maximum exposure",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "dramatic rain beauty, palace wet goddess",
        "body_oil": "extreme wet rain-soaked see-through skin",
    },
    "joseon_boudoir": {
        "subject": "a stunning Korean model in Joseon private boudoir scene",
        "environment": "Joseon private chamber, silk screen paintings, candlelight, silk bedding, intimate private space",
        "outfit": "Joseon private moment — silk undergarments barely covering, silk robe falling open, maximum intimate exposure, hair down, candlelit privacy",
        "material": "white silk undergarments, loosely draped robe, intimate private fabrics",
        "lighting": "multiple candles intimate glow, warm private room light",
        "style": "boudoir luxury editorial, Joseon intimate maximum glamour",
        "quality": "ultra-sharp 8K, professional fashion photography",
        "mood": "ultimate private intimate beauty, Joseon boudoir maximum",
        "body_oil": "warm candlelit intimate glowing skin",
    },
}

# ══════════════════════════════════════════════════════════
# SSS tier — 전통 싱크 + 글래머 경계 소멸 최강 종목
# ══════════════════════════════════════════════════════════
NEW_SSS = [
    # 삼국/고대 — 바디페인트+고분+불꽃 완전융합
    "silla_queen_gold", "ancient_mural_goddess", "goguryeo_warrior_queen",
    "gojoseon_shaman_queen", "dongye_tribal_queen",
    # 고려 — 청자+불화 예술 완전융합
    "goryeo_celadon_goddess", "goryeo_buddhist_temptress", "goryeo_haenyeo_silk",
    # 조선 왕실 — 경복궁+시스루 완전융합
    "joseon_queen_slit", "joseon_night_queen", "changdeok_moonlight",
    "crown_princess_latex", "joseon_concubine_red",
    # 기생 — 홍등+웨트룩+거울 완전융합
    "gisaeng_red_lantern", "gisaeng_rain_dance", "gisaeng_haiku_bath",
    "hwang_jini_glam", "gisaeng_mirror_boudoir",
    # 신화 — 구미호+용녀+선녀 완전융합
    "gumiho_latex", "gumiho_red_moon", "dragon_daughter_sea",
    "nine_tail_dominatrix", "seonnyeo_descent", "imoogi_seduction",
    # 민속 — 해녀+무당 완전융합
    "haenyeo_wet_glam", "mudang_fire_ritual", "ganggangsullae_night",
    # 여전사 — 고구려 화염+조선 자객 완전융합
    "goguryeo_fire_warrior", "joseon_female_assassin",
    # 퓨전 — 한복라텍스+사이버펑크 완전융합
    "hanbok_latex_queen", "gisaeng_cyberpunk", "hanbok_wet_editorial",
]

# SS tier — SSS 포함 전체
NEW_SS = list(KOREAN_HISTORICAL_PRESETS.keys())  # 78종 전부 SS 이상


# ══════════════════════════════════════════════════════════
# dashboard.py 패치
# ══════════════════════════════════════════════════════════

# 새 카테고리 블록
NEW_CATEGORY_BLOCK = '''
    "👑 한국 역사 & 궁중 글래머": [
        # 🏯 삼국/고대 왕실
        "silla_queen_gold", "silla_dancing_girl", "baekje_lotus_queen",
        "goguryeo_warrior_queen", "gojoseon_shaman_queen", "gaya_iron_goddess",
        "silla_hwarang_girl", "ancient_mural_goddess", "three_kingdoms_spy",
        "dongye_tribal_queen",
        # 🏰 고려 궁중
        "goryeo_empress_silk", "goryeo_gisaeng_glam", "goryeo_celadon_goddess",
        "goryeo_buddhist_temptress", "goryeo_court_dancer", "goryeo_night_gisaeng",
        "mongol_goryeo_queen", "goryeo_haenyeo_silk",
        # 👘 조선 왕실/궁중
        "joseon_queen_slit", "joseon_consort_sheer", "crown_princess_latex",
        "joseon_court_dancer", "joseon_painter_nude", "hwajeon_court_lady",
        "joseon_merchant_woman", "damo_warrior", "joseon_night_queen",
        "joseon_concubine_red", "changdeok_moonlight", "gyeongbokgung_geisha",
        # 💃 기생/예인
        "gisaeng_joseon_sheer", "gisaeng_red_lantern", "gisaeng_sword_dance",
        "gisaeng_haiku_bath", "gisaeng_rain_dance", "gisaeng_black_silk",
        "wonhyang_legend", "hwang_jini_glam", "gisaeng_fan_dance",
        "gisaeng_pipa_night", "gisaeng_mirror_boudoir", "pyongyang_gisaeng",
        # 🦊 신화 & 정령
        "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",
        "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",
        "seonnyeo_descent", "haenyeo_mermaid", "baeksa_serpent",
        "chamsuri_ghost", "taoist_fairy_korea", "nine_tail_dominatrix",
        # 🌊 민속 & 세시풍속
        "haenyeo_wet_glam", "dano_festival_glam", "ganggangsullae_night",
        "mudang_fire_ritual", "mudang_trance_glam", "namsadang_acrobat",
        "jeju_shaman_sea", "korean_harvest_goddess",
        # ⚔️ 여전사 & 무인
        "joseon_female_assassin", "goryeo_archer_queen", "silla_female_hwarang",
        "joseon_damo_noir", "tiger_huntress_korea", "wonhyang_warrior",
        "goguryeo_fire_warrior", "joseon_spy_sheer",
        # 🎭 근대 & 퓨전
        "joseon_modern_fusion", "gisaeng_cyberpunk", "hanbok_latex_queen",
        "joseon_noir", "gisaeng_opium_den", "korean_vamp_modern",
        "hanbok_wet_editorial", "joseon_boudoir",
    ],
'''

# SSS_TIER 추가 블록
SSS_INSERT = "\n    # 2026-06-26 한국 역사 & 궁중 글래머 SSS\n" + \
    "    # 삼국/고대\n" + \
    '    "silla_queen_gold", "ancient_mural_goddess", "goguryeo_warrior_queen",\n' + \
    '    "gojoseon_shaman_queen", "dongye_tribal_queen",\n' + \
    "    # 고려\n" + \
    '    "goryeo_celadon_goddess", "goryeo_buddhist_temptress", "goryeo_haenyeo_silk",\n' + \
    "    # 조선 왕실\n" + \
    '    "joseon_queen_slit", "joseon_night_queen", "changdeok_moonlight",\n' + \
    '    "crown_princess_latex", "joseon_concubine_red",\n' + \
    "    # 기생\n" + \
    '    "gisaeng_red_lantern", "gisaeng_rain_dance", "gisaeng_haiku_bath",\n' + \
    '    "hwang_jini_glam", "gisaeng_mirror_boudoir",\n' + \
    "    # 신화/정령\n" + \
    '    "gumiho_latex", "gumiho_red_moon", "dragon_daughter_sea",\n' + \
    '    "nine_tail_dominatrix", "seonnyeo_descent", "imoogi_seduction",\n' + \
    "    # 민속\n" + \
    '    "haenyeo_wet_glam", "mudang_fire_ritual", "ganggangsullae_night",\n' + \
    "    # 여전사\n" + \
    '    "goguryeo_fire_warrior", "joseon_female_assassin",\n' + \
    "    # 퓨전\n" + \
    '    "hanbok_latex_queen", "gisaeng_cyberpunk", "hanbok_wet_editorial",\n'

# SS_TIER 추가 블록 (78종 전체)
SS_INSERT = "\n    # 2026-06-26 한국 역사 & 궁중 글래머 SS (78종 전체)\n" + \
    '    "silla_queen_gold", "silla_dancing_girl", "baekje_lotus_queen",\n' + \
    '    "goguryeo_warrior_queen", "gojoseon_shaman_queen", "gaya_iron_goddess",\n' + \
    '    "silla_hwarang_girl", "ancient_mural_goddess", "three_kingdoms_spy",\n' + \
    '    "dongye_tribal_queen",\n' + \
    '    "goryeo_empress_silk", "goryeo_gisaeng_glam", "goryeo_celadon_goddess",\n' + \
    '    "goryeo_buddhist_temptress", "goryeo_court_dancer", "goryeo_night_gisaeng",\n' + \
    '    "mongol_goryeo_queen", "goryeo_haenyeo_silk",\n' + \
    '    "joseon_queen_slit", "joseon_consort_sheer", "crown_princess_latex",\n' + \
    '    "joseon_court_dancer", "joseon_painter_nude", "hwajeon_court_lady",\n' + \
    '    "joseon_merchant_woman", "damo_warrior", "joseon_night_queen",\n' + \
    '    "joseon_concubine_red", "changdeok_moonlight", "gyeongbokgung_geisha",\n' + \
    '    "gisaeng_joseon_sheer", "gisaeng_red_lantern", "gisaeng_sword_dance",\n' + \
    '    "gisaeng_haiku_bath", "gisaeng_rain_dance", "gisaeng_black_silk",\n' + \
    '    "wonhyang_legend", "hwang_jini_glam", "gisaeng_fan_dance",\n' + \
    '    "gisaeng_pipa_night", "gisaeng_mirror_boudoir", "pyongyang_gisaeng",\n' + \
    '    "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",\n' + \
    '    "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",\n' + \
    '    "seonnyeo_descent", "haenyeo_mermaid", "baeksa_serpent",\n' + \
    '    "chamsuri_ghost", "taoist_fairy_korea", "nine_tail_dominatrix",\n' + \
    '    "haenyeo_wet_glam", "dano_festival_glam", "ganggangsullae_night",\n' + \
    '    "mudang_fire_ritual", "mudang_trance_glam", "namsadang_acrobat",\n' + \
    '    "jeju_shaman_sea", "korean_harvest_goddess",\n' + \
    '    "joseon_female_assassin", "goryeo_archer_queen", "silla_female_hwarang",\n' + \
    '    "joseon_damo_noir", "tiger_huntress_korea", "wonhyang_warrior",\n' + \
    '    "goguryeo_fire_warrior", "joseon_spy_sheer",\n' + \
    '    "joseon_modern_fusion", "gisaeng_cyberpunk", "hanbok_latex_queen",\n' + \
    '    "joseon_noir", "gisaeng_opium_den", "korean_vamp_modern",\n' + \
    '    "hanbok_wet_editorial", "joseon_boudoir",\n'


def patch_dashboard():
    with open(DASHBOARD, "r", encoding="utf-8") as f:
        src = f.read()

    # ── 1. PRESET_CATEGORIES 마지막에 새 카테고리 추가 ──
    # 🌫️ 대기 & 파티클 블록 닫는 부분 뒤에 삽입
    anchor_cat = '"seed_pod_floating",\n    ],\n\n}'
    new_cat = '"seed_pod_floating",\n    ],' + NEW_CATEGORY_BLOCK + '\n}'

    if anchor_cat in src:
        src = src.replace(anchor_cat, new_cat, 1)
        print("✅ PRESET_CATEGORIES 새 카테고리 추가 완료")
    else:
        # 대안 앵커
        anchor_cat2 = '"seed_pod_floating",\n    ],\n}'
        if anchor_cat2 in src:
            src = src.replace(anchor_cat2, '"seed_pod_floating",\n    ],' + NEW_CATEGORY_BLOCK + '\n}', 1)
            print("✅ PRESET_CATEGORIES 추가 완료 (대안 앵커)")
        else:
            print("⚠️ PRESET_CATEGORIES 앵커 미발견")
            print("  수동으로 PRESET_CATEGORIES 끝에 추가 필요")

    # ── 2. SSS_TIER 추가 ──
    sss_anchor = '"hanbok_wet_editorial",\n\n\n# SS tier'
    sss_new = '"hanbok_wet_editorial",' + SSS_INSERT + '\n\n\n# SS tier'
    if sss_anchor not in src:
        # SSS_TIER 마지막 항목 찾기 — "seed_pod_floating" 이후
        sss_anchor = '"seed_pod_floating",\n}\n\n# SS tier'
        sss_new = '"seed_pod_floating",' + SSS_INSERT + '\n}\n\n# SS tier'

    if sss_anchor in src:
        src = src.replace(sss_anchor, sss_new, 1)
        print("✅ SSS_TIER 추가 완료")
    else:
        # SSS_TIER 블록 끝 찾기
        sss_end = '"milk_bath_petals",\n}\n\nBG'
        sss_end_new = '"milk_bath_petals",' + SSS_INSERT + '\n}\n\nBG'
        if sss_end in src:
            src = src.replace(sss_end, sss_end_new, 1)
            print("✅ SSS_TIER 추가 완료 (milk_bath_petals 앵커)")
        else:
            print("⚠️ SSS_TIER 앵커 미발견 — 수동 추가 필요")

    # ── 3. SS_TIER 추가 ──
    ss_anchor = '"milk_bath_petals",\n}\n\n# ─── 다크 테마'
    ss_new = '"milk_bath_petals",' + SS_INSERT + '\n}\n\n# ─── 다크 테마'
    if ss_anchor in src:
        src = src.replace(ss_anchor, ss_new, 1)
        print("✅ SS_TIER 추가 완료")
    else:
        print("⚠️ SS_TIER 앵커 미발견 — 수동 추가 필요")

    with open(DASHBOARD, "w", encoding="utf-8") as f:
        f.write(src)
    print(f"\n📝 dashboard.py 저장 완료")


def create_preset_jsons():
    """presets/ 디렉토리에 JSON 파일 78개 생성"""
    presets_path = Path(PRESETS_DIR)
    if not presets_path.exists():
        print(f"⚠️ presets 디렉토리 없음: {PRESETS_DIR}")
        return

    created = 0
    for key, data in KOREAN_HISTORICAL_PRESETS.items():
        filepath = presets_path / f"{key}.json"
        if not filepath.exists():
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            created += 1

    print(f"✅ preset JSON 생성: {created}개")
    print(f"   (기존 파일은 덮어쓰지 않음)")


if __name__ == "__main__":
    print("=" * 55)
    print("👑 한국 역사 & 궁중 글래머 78종 패치 시작")
    print("=" * 55)

    # 1. preset JSON 생성
    create_preset_jsons()

    # 2. dashboard.py 패치
    patch_dashboard()

    print("\n" + "=" * 55)
    print("검증 명령:")
    print('  Select-String -Path dashboard.py -Pattern "joseon_queen_slit" | Select-Object -First 3')
    print('  Select-String -Path dashboard.py -Pattern "gumiho_latex" | Select-Object -First 3')
    print('  Select-String -Path dashboard.py -Pattern "한국 역사" | Select-Object -First 3')
    print("\nGit:")
    print('  git add -A')
    print('  git commit -m "feat: 한국 역사&궁중 글래머 78종 신설 카테고리 추가"')
    print('  git push')
    print("=" * 55)
