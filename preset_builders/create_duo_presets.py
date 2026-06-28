"""
create_duo_presets.py
듀오 글래머 프리셋 30종 JSON 파일 생성
실행: python create_duo_presets.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path("C:/Dev/LumineX/presets")

# 듀오 프리셋 정의
# 구조 판단 근거:
# - subject: 두 인물을 하나의 문장으로 통합 (Gemini가 가장 잘 인식하는 방식)
# - body: 두 체형 대비를 명시
# - outfit: 각 모델 의상을 "first model... second model..." 구조로
# - material: 두 소재 중 더 지배적인 것 또는 공통 질감
# - environment/lighting/style/quality: 단독 프리셋과 동일 구조 유지

DUO_PRESETS = {

    # ── G1: 웨트 & 풀 ──────────────────────────────────────

    "duo_infinity_pool_contrast": {
        "tag": "Duo Infinity Pool Contrast",
        "subject": "two goddess-level female models back to back at rooftop infinity pool edge, both soaking wet, twin goddesses owning the skyline",
        "body": "first model tall slim Korean beauty soaking wet slicked hair / second model powerful curvy Black goddess box braids dripping, contrasting silhouettes side by side",
        "outfit": "first model silver metallic high-cut swimsuit clinging like liquid metal / second model dark green sheer fabric dissolving against glistening skin",
        "material": "wet metallic and wet sheer, both drenched and skin-revealing",
        "environment": "Dubai rooftop infinity pool, city skyline at dusk, water merging with horizon, Burj Khalifa behind",
        "lighting": "dusk city glow, pool underwater blue lighting uplighting both models, golden hour rim from behind",
        "style": "high-end resort duo campaign, architectural wet editorial, Sports Illustrated meets Vogue",
        "quality": "shot on Hasselblad X2D, cinematic teal-orange grade, portrait 2:3 vertical, ultra-sharp 8K"
    },

    "duo_rain_neon_soaked": {
        "tag": "Duo Rain Neon Soaked",
        "subject": "two fierce female models completely soaked in Tokyo neon rainstorm, both drenched and glowing under neon",
        "body": "first model tall Scandinavian platinum blonde / second model Brazilian bombshell bronzed curves, both rain-slicked and unapologetic",
        "outfit": "first model white sheer fabric utterly transparent from rain, nothing left to imagination / second model iridescent micro bikini top with rain-soaked wrap clinging to every curve",
        "material": "drenched sheer and wet iridescent, rain making both fabrics transparent and skin-tight",
        "environment": "Shinjuku neon-lit rainy alley Tokyo at night, neon signs reflected in flooded street, steam rising from grates",
        "lighting": "hot pink and electric blue neon reflected upward from puddles, rain backlit by streetlamps, multicolor skin",
        "style": "cyberpunk wet editorial duo, fashion storm photography, Versace meets Ghost in the Shell",
        "quality": "shot on Sony A7R V, high contrast neon saturated, rain streaks razor sharp, portrait 2:3 vertical"
    },

    "duo_pool_bodypaint_micro": {
        "tag": "Duo Pool Bodypaint Micro",
        "subject": "two artistic models at luxury tropical pool, one emerging from water, one seated at edge, artistic bodypaint meets micro swimwear",
        "body": "first model slim athletic with tropical flowers and butterflies painted across chest and hips / second model athletic hourglass with iridescent mermaid scale paint from waist down",
        "outfit": "first model tropical floral bodypaint as coverage with micro string bottom only / second model mermaid scale bodypaint with metallic micro triangle top",
        "material": "body paint pigment on bare skin NOT fabric, painted directly on body, plus minimal metallic swimwear",
        "environment": "luxury resort infinity pool, tropical flowers floating, turquoise water, Bali afternoon paradise",
        "lighting": "tropical afternoon sun, water caustics dancing on painted skin, warm paradise golden light",
        "style": "artistic resort editorial duo, bodypaint meets swimwear, Sports Illustrated art edition",
        "quality": "shot on Canon EOS R5, tropical saturated cinematic, portrait 2:3 vertical, 8K hyperrealistic"
    },

    "duo_wet_glass_divide": {
        "tag": "Duo Wet Glass Divide",
        "subject": "two female models on opposite sides of rain-soaked floor-to-ceiling glass wall, pressing palms together from divided worlds",
        "body": "first model slim inside pressing against warm glass / second model curvy outside in heavy rain, both visible simultaneously through glass",
        "outfit": "first model white sheer slip inside, condensation fogging glass around her silhouette / second model soaking wet minimal clinging to absolutely nothing outside",
        "material": "sheer silk inside warm and dry / outside soaking wet transparent, glass dividing two realities",
        "environment": "floor to ceiling glass wall, rain pouring outside, warm amber interior, city lights visible beyond the storm",
        "lighting": "warm amber inside illuminating first model / cold neon rain outside on second model, glass as light membrane",
        "style": "cinematic glass barrier duo editorial, temperature and light contrast, Alexander McQueen meets Blade Runner",
        "quality": "shot on Sony A7R V, dual light cinematic, glass detail perfect, portrait 2:3 vertical, 8K"
    },

    # ── G2: 바디페인트 대결 ────────────────────────────────

    "duo_bodypaint_vs_latex": {
        "tag": "Duo Bodypaint vs Latex",
        "subject": "two dangerously beautiful female models in stark material contrast, facing each other with electric tension",
        "body": "first model slim athletic body fully painted / second model dramatic hourglass in vacuum-sealed latex, hands almost touching between them",
        "outfit": "first model entire body painted in liquid gold tribal geometric patterns, barefoot, paint as sole coverage / second model jet black high-gloss latex catsuit vacuum-sealed to every curve",
        "material": "gold body paint pigment on bare skin NOT clothing for first / liquid latex second-skin for second",
        "environment": "dark minimal void studio, black seamless backdrop, single dramatic light beam splitting between them",
        "lighting": "split lighting, warm gold on painted model, cold chrome rim light on latex model, dramatic darkness between",
        "style": "Thierry Mugler meets tribal body art, dark haute couture duo, maximum contrast editorial",
        "quality": "shot on Phase One XF IQ4, ultra-sharp 8K, split light cinematic, portrait 2:3 vertical"
    },

    "duo_ocean_bodypaint": {
        "tag": "Duo Ocean Bodypaint",
        "subject": "two painted ocean goddesses rising triumphant as wave crashes behind them, arms raised",
        "body": "first model athletic body painted in bioluminescent blue ocean wave patterns / second model curvy body painted in coral reef and tropical fish across every curve, gold at collarbone",
        "outfit": "first model entire body painted in ocean patterns barefoot in surf, paint as sole coverage / second model coral reef patterns covering every inch, barefoot",
        "material": "bioluminescent blue and coral bodypaint pigment applied directly on bare skin NOT clothing, both barefoot",
        "environment": "tropical beach at golden hour, massive wave breaking dramatically behind them, wet sand reflecting sunset",
        "lighting": "golden hour backlight making bodypaint literally glow, wave spray catching sunlight, warm amber goddess light",
        "style": "Sports Illustrated meets body art, ocean goddess duo editorial, Vogue Italia beach",
        "quality": "shot on Canon EOS R5, 85mm golden hour cinematic, portrait 2:3 vertical, 8K hyperrealistic"
    },

    "duo_golden_desert_bodypaint": {
        "tag": "Duo Golden Desert Bodypaint",
        "subject": "two ancient painted desert goddesses in Sahara at golden hour, one kneeling as offering one standing as queen",
        "body": "first model athletic body painted in geometric Berber tribal patterns gold and copper / second model curvy body painted in ancient Egyptian hieroglyph patterns in gold across every curve",
        "outfit": "first model Berber tribal geometric gold bodypaint as sole coverage barefoot in sand / second model Egyptian hieroglyph gold bodypaint covering every curve barefoot",
        "material": "gold and copper bodypaint pigment on bare skin NOT clothing, ancient ritual aesthetic",
        "environment": "Sahara dunes at golden hour, sky burning orange and purple, sand as warm as their skin, endless ancient landscape",
        "lighting": "setting sun directly behind creating halo, models backlit with golden rim, bodypaint glowing like fire",
        "style": "ancient goddess ritual editorial, desert body art duo, National Geographic meets haute couture",
        "quality": "shot on Phase One XF IQ4, golden hour maximum drama, portrait 2:3 vertical, 8K"
    },

    "duo_aurora_bodypaint": {
        "tag": "Duo Aurora Bodypaint",
        "subject": "two celestial painted goddesses standing barefoot in arctic snow under blazing aurora, both looking upward communing with sky",
        "body": "first model slim ethereal with aurora borealis painted across entire body in green gold purple / second model athletic powerful with galaxy and star map painted head to toe cosmic patterns",
        "outfit": "first model aurora bodypaint as sole coverage barefoot in snow / second model galaxy bodypaint covering everything barefoot on ice",
        "material": "aurora and galaxy bodypaint pigment directly on bare skin NOT clothing, cold skin glowing warm",
        "environment": "Iceland arctic landscape, aurora borealis blazing impossibly above, pristine snow, absolute crystalline silence",
        "lighting": "aurora light from above matching bodypaint colors perfectly, magical cold blue-green glow, celestial",
        "style": "celestial body art duo, northern lights editorial, ethereal goddess fashion",
        "quality": "shot on Sony A7R V, aurora detail maximum, portrait 2:3 vertical, 8K hyperrealistic"
    },

    "duo_cyberpunk_bodypaint": {
        "tag": "Duo Cyberpunk Bodypaint",
        "subject": "two cyberpunk goddesses with circuit board neon patterns painted full body leaning against neon-lit wall with digital cool",
        "body": "first model slim with electric blue and cyan circuit board patterns painted entire body / second model curvy with hot pink and purple neon tribal cyber patterns painted everywhere",
        "outfit": "first model electric blue circuit bodypaint barefoot, paint as sole coverage / second model hot pink neon bodypaint barefoot",
        "material": "neon circuit bodypaint pigment on bare skin NOT clothing, both barefoot, digital tribal aesthetic",
        "environment": "Tokyo back alley at night, neon signs blazing, rain-wet reflective street, futuristic urban darkness",
        "lighting": "neon signs casting electric colored light on bodypaint making it glow, rain making paint glisten and run",
        "style": "Ghost in the Shell meets body art, cyberpunk duo editorial, dark futuristic glamour",
        "quality": "shot on Sony A7R V, neon saturated maximum, rain sharp, portrait 2:3 vertical, 8K"
    },

    "duo_jungle_tribal_bodypaint": {
        "tag": "Duo Jungle Tribal Bodypaint",
        "subject": "two primal goddess models at ancient jungle temple, one on stone steps above one below, jungle priestesses in power",
        "body": "first model athletic with intricate jaguar spot bodypaint neck to ankles tribal gold arm cuffs only / second model powerful with serpent scale bodypaint spiraling entire body python goddess",
        "outfit": "first model jaguar bodypaint as sole coverage with gold cuffs / second model serpent scale bodypaint covering everything",
        "material": "jaguar spot and serpent scale bodypaint pigment on bare skin NOT clothing, tribal gold metal cuffs only",
        "environment": "Angkor Wat jungle temple at dawn, mist curling through ancient stone, jungle breaking through ruins",
        "lighting": "dawn golden light breaking through jungle canopy, mist catching light beams, ancient amber atmosphere",
        "style": "primal goddess editorial, ancient ritual body art duo, National Geographic high fashion",
        "quality": "shot on Canon EOS R5, dawn cinematic gold, portrait 2:3 vertical, 8K hyperrealistic"
    },

    # ── G3: 라텍스 & 소재 대비 ────────────────────────────

    "duo_latex_color_block": {
        "tag": "Duo Latex Color Block",
        "subject": "two latex goddess models in pure color opposition against white wall, crossed arms, strategic chess pieces",
        "body": "first model ultra-slim ice queen in white / second model powerful hourglass danger in blood red, both commanding camera",
        "outfit": "first model pure white latex micro dress and thigh-high boots, ice queen energy / second model blood red latex catsuit skintight from neck to toe, predator energy",
        "material": "high-gloss latex second-skin, vacuum-sealed to every contour, both colors maximum saturation",
        "environment": "pure white minimal studio, seamless white backdrop, nothing to distract from the color opposition",
        "lighting": "soft octabox beauty light, even shadowless illumination, color pop to absolute maximum",
        "style": "Helmut Newton color block duo, minimalist maximum impact, Versace editorial power",
        "quality": "shot on Hasselblad H6D, color accurate perfect, ultra clean, portrait 2:3 vertical, 8K"
    },

    "duo_latex_storm_opposites": {
        "tag": "Duo Latex Storm Opposites",
        "subject": "two models dominating clifftop electrical storm, complete opposites of coverage and energy",
        "body": "first model powerful athletic facing storm head-on in electric yellow / second model ethereal slim embracing lightning arms spread in dissolving white",
        "outfit": "first model electric yellow latex catsuit skintight, lightning illuminating every seam, storm warrior / second model white sheer organza barely draped, wind and rain making it transparent to nothing",
        "material": "yellow latex second-skin for first / sheer organza dissolving in rain for second, maximum contrast",
        "environment": "dramatic clifftop during electrical storm, lightning strikes illuminating everything, wild storm clouds, ocean below",
        "lighting": "lightning flash as natural strobe, blue-white electrical light, dramatic storm shadows, nature as lighting",
        "style": "Alexander McQueen storm editorial duo, power of nature meets fashion extremes",
        "quality": "shot on Nikon Z9, 1/2000s storm frozen in frame, ultra dramatic, portrait 2:3 vertical, 8K"
    },

    "duo_dark_latex_power": {
        "tag": "Duo Dark Latex Power",
        "subject": "two dominant models in dark industrial space, hierarchy and power, one seated commanding one standing behind",
        "body": "first model athletic seated on industrial chair commanding / second model tall hourglass standing behind her equally commanding, both facing camera with predatory confidence",
        "outfit": "first model red latex micro corset and thigh-high boots, industrial chains as accessories / second model black PVC harness and micro skirt, metal hardware, power stance",
        "material": "red latex and black PVC, both high-gloss skin-tight, metal hardware catching single light",
        "environment": "dark industrial concrete space, exposed brick, single industrial pendant light, dramatic deep shadows",
        "lighting": "single hard pendant light beam, deep shadow filling everywhere else, latex and PVC catching harsh light",
        "style": "dark couture power duo editorial, industrial dominance fashion, Mugler meets industrial",
        "quality": "shot on Sony A7R V, maximum contrast, deep shadow detail, portrait 2:3 vertical, 8K"
    },

    "duo_flamenco_latex_fusion": {
        "tag": "Duo Flamenco Latex Fusion",
        "subject": "two models fusing flamenco passion with latex power, mid-dance freeze facing each other, flamenco confrontation",
        "body": "first model fierce Spanish dark hair rose in hair / second model powerful commanding dancer, both frozen in maximum tension",
        "outfit": "first model red latex micro flamenco dress with dramatic ruffled slit, rose in hair, passion / second model black latex bodysuit with sheer flamenco skirt panels, danger",
        "material": "red latex and black latex with sheer flamenco panels, both skin-tight with dramatic movement",
        "environment": "dark Spanish bodega at night, candlelight flickering, rose petals on stone floor, old world drama",
        "lighting": "warm candlelight dramatic from below, deep theatrical shadows, rose red tones, intimate and dangerous",
        "style": "flamenco meets latex couture duo, dark Spanish editorial, passion and danger",
        "quality": "shot on Canon EOS R5, candlelight warm cinematic, portrait 2:3 vertical, 8K"
    },

    # ── G4: 오일 & 그림자 ──────────────────────────────────

    "duo_oiled_shadows": {
        "tag": "Duo Oiled Shadows",
        "subject": "two heavily oiled goddesses emerging from darkness, one slightly behind the other overlapping silhouettes",
        "body": "first model ultra-slim with shadow and light as only coverage, strategic darkness hiding nothing / second model full figure with maximum oil gloss, shadow painting her curves, hint of gold chain",
        "outfit": "first model shadow and spotlight as sole coverage, extreme body oil, no fabric / second model gold body chain as only accessory over oiled skin, darkness as dress",
        "material": "extreme high-gloss body oil on bare skin, shadow and light as coverage, gold chain only",
        "environment": "black void studio, single hard overhead spotlight, oil droplets catching the single beam",
        "lighting": "single hard overhead spotlight, deep absolute shadows below, oil catching every available photon",
        "style": "Herb Ritts body oil editorial duo, Studio Newton high-gloss, Irving Penn darkness",
        "quality": "shot on Hasselblad H6D, maximum shadow detail, oil gloss perfect, portrait 2:3 vertical, 8K"
    },

    "duo_smoke_noir": {
        "tag": "Duo Smoke Noir",
        "subject": "two mystery models partially veiled in smoke-filled noir studio, only curves and eyes visible emerging from void",
        "body": "first model slim with black body paint and smoke swirl patterns / second model hourglass with dark charcoal body oil maximum gloss, shadow as costume",
        "outfit": "first model black smoke-pattern bodypaint from neck to thighs, smoke as additional veil / second model dark oil and shadow as costume, nothing else needed",
        "material": "black bodypaint for first / extreme body oil and shadow for second, both using darkness as couture",
        "environment": "black void studio, dry ice smoke filling entire space, single spotlight cutting dramatically through",
        "lighting": "single beam through dense smoke, dramatic film noir contrast, smoke catching and diffusing light",
        "style": "film noir body art duo editorial, smoke and shadow fashion, dark glamour mystery",
        "quality": "shot on Hasselblad H6D, smoke detail perfect texture, portrait 2:3 vertical, 8K"
    },

    # ── G5: 럭셔리 씬 ──────────────────────────────────────

    "duo_versailles_latex_gold": {
        "tag": "Duo Versailles Latex Gold",
        "subject": "two commanding models walking toward camera in Versailles Hall of Mirrors, 357 mirrors multiplying them to infinite army",
        "body": "first model statuesque European in ivory / second model regal Middle Eastern beauty in burgundy, both walking in formation, unstoppable",
        "outfit": "first model ivory liquid latex gown slit to hip, golden chandelier light reflecting in latex / second model deep burgundy latex corset dress, gold jewelry, queen energy",
        "material": "ivory and burgundy liquid latex, both mirror-like, catching and multiplying chandelier reflections",
        "environment": "Palace of Versailles Hall of Mirrors, 357 mirrors, crystal chandeliers, golden afternoon light, infinite reflections",
        "lighting": "chandelier light fracturing across all mirror panels, warm gold everywhere, latex catching every reflection",
        "style": "old world power duo, Vogue Italia palace editorial, Versace meets Versailles",
        "quality": "shot on Leica SL2 50mm, cinematic wide, portrait 2:3 vertical, 8K hyperrealistic"
    },

    "duo_monaco_yacht": {
        "tag": "Duo Monaco Yacht",
        "subject": "two ultra glamorous models casually commanding superyacht deck at Monaco, effortless Mediterranean power",
        "body": "first model lean toned just emerged from swimming / second model curvy bronzed Mediterranean goddess, both owning the yacht and the harbor",
        "outfit": "first model gold chain mail micro bikini dripping from swimming, pure gold against wet skin / second model white string bikini with sheer sarong dissolving in sea breeze",
        "material": "gold chain mail and white sheer dissolving sarong, both minimal and sea-drenched",
        "environment": "superyacht deck Monaco harbor, other yachts and Monte Carlo behind, Mediterranean golden afternoon perfection",
        "lighting": "Mediterranean afternoon sun direct and golden, water reflections dancing on skin, perfect natural luxury light",
        "style": "Dolce and Gabbana yacht campaign, old money Mediterranean duo editorial",
        "quality": "shot on Fujifilm GFX 100S, medium format luxury light, portrait 2:3 vertical, 8K"
    },

    "duo_champagne_gala": {
        "tag": "Duo Champagne Gala",
        "subject": "two iconic models radiating untouchable energy at black tie gala, one perched on bar one standing, champagne in hand",
        "body": "first model tall European effortless in liquid gold / second model statuesque Black goddess commanding in gold body chain, both untouchable",
        "outfit": "first model liquid gold micro dress barely covering, effortless old money / second model gold body chain as primary coverage over maximum oiled skin, new money goddess",
        "material": "liquid gold micro dress and gold body chain over oiled skin, both maximum gold, both commanding",
        "environment": "grand ballroom crystal chandeliers, black tie crowd blurred bokeh behind, champagne tower glittering",
        "lighting": "chandelier warm gold light from above, champagne bubbles catching light, glamorous warm editorial glow",
        "style": "Vogue black tie duo editorial, champagne gold power, old and new money collision",
        "quality": "shot on Leica SL2, warm gold cinematic, portrait 2:3 vertical, 8K"
    },

    "duo_villa_italy": {
        "tag": "Duo Villa Italy",
        "subject": "two effortlessly glamorous models at Positano cliffside villa, Italian dolce vita duo, paradise as their living room",
        "body": "first model lean Mediterranean olive skin poolside / second model sun-drenched blonde European at pool edge, both golden Italian afternoon",
        "outfit": "first model white micro linen barely covering, olive skin golden in afternoon heat / second model peach string bikini sun-drenched, Positano and sea behind her",
        "material": "white micro linen and peach string bikini, both minimal, both Mediterranean summer perfect",
        "environment": "Positano cliffside villa infinity pool, Mediterranean sea below, bougainvillea blooming, golden afternoon",
        "lighting": "warm Italian afternoon sun from west, pool water reflection on skin, golden hour paradise",
        "style": "Dolce Vita resort editorial duo, Italian summer luxury, La Dolce Vita meets Vogue",
        "quality": "shot on Fujifilm GFX 100S, warm Mediterranean grade, portrait 2:3 vertical, 8K"
    },

    "duo_casino_power": {
        "tag": "Duo Casino Power",
        "subject": "two untouchable models commanding Monte Carlo casino floor, chips in hand, every eye in the room on them",
        "body": "first model sleek European sharp in emerald / second model powerful hourglass commanding in gold, both owning the casino",
        "outfit": "first model black liquid satin micro dress slit to hip, emerald jewels, old money untouchable / second model gold sequin micro cocktail dress, curves at absolute maximum, new money unstoppable",
        "material": "black liquid satin and gold sequin, both minimal coverage maximum impact, jewels catching casino light",
        "environment": "Monte Carlo casino grand floor, crystal chandeliers, green baize tables, tuxedo crowd bokeh behind",
        "lighting": "chandelier warm casino light from above, emerald and gold catching every photon, old world glamour",
        "style": "Casino Royale femme fatale duo, Monaco power editorial, Versace meets old money",
        "quality": "shot on Leica SL2, warm casino cinematic, portrait 2:3 vertical, 8K"
    },

    # ── G6: 엘리멘탈 대비 ─────────────────────────────────

    "duo_fire_and_ice": {
        "tag": "Duo Fire and Ice",
        "subject": "two elemental goddess models embodying fire and ice facing each other, hands almost meeting in center, steam rising between them",
        "body": "first model fiery Latina in flame patterns / second model ice-cold Nordic in frost crystals, both mythological forces facing off",
        "outfit": "first model flame bodypaint covering torso and thighs in red orange gold, fire goddess / second model white and silver frost crystal bodypaint, frozen goddess",
        "material": "flame bodypaint and frost bodypaint on bare skin NOT clothing, elemental forces as coverage",
        "environment": "black void studio split, fire atmosphere left side, ice cave atmosphere right side, elemental division",
        "lighting": "warm orange fire glow on flame goddess / cold blue ice light on frost goddess, dramatic split at center",
        "style": "elemental duality editorial duo, high concept fashion, primordial forces as fashion",
        "quality": "shot on Phase One XF IQ4, split light master, portrait 2:3 vertical, 8K"
    },

    "duo_angel_devil": {
        "tag": "Duo Angel Devil",
        "subject": "two models embodying celestial opposites back to back, wings spread filling frame, angel and devil in perfect equilibrium",
        "body": "first model ethereal blonde angel with white wings divine / second model dark haired devil with black wings dangerous, both equally powerful",
        "outfit": "first model white micro bodysuit barely there with white feather wings, divine and almost nothing / second model black latex micro dress with dark feather wings, danger in minimal coverage",
        "material": "white sheer micro bodysuit and black latex, feather wings, celestial opposition",
        "environment": "split studio, pure white divine light on angel side, deep red dramatic on devil side, two worlds",
        "lighting": "pure white beauty light on angel / deep saturated red on devil, meeting in dramatic center shadow",
        "style": "Victoria Secret fantasy meets dark couture, celestial duo editorial, heaven and hell",
        "quality": "shot on Canon EOS R5, split light dramatic, portrait 2:3 vertical, 8K"
    },

    "duo_chrome_future": {
        "tag": "Duo Chrome Future",
        "subject": "two futuristic chrome goddesses in all-chrome studio facing each other in mirror pose, reflections infinite",
        "body": "first model slim chrome liquid metal bodypaint mirror skin / second model powerful athletic silver metallic second-skin painted on, robotic glamour",
        "outfit": "first model chrome liquid metal bodypaint entire body, mirror skin effect, no fabric / second model silver metallic bodypaint second-skin, robotic goddess",
        "material": "chrome and silver metallic bodypaint on bare skin NOT clothing, both mirror-like reflective",
        "environment": "all-chrome studio floor ceiling walls, every surface reflecting, futuristic void, infinite reflections",
        "lighting": "single white beam, chrome reflecting in all directions simultaneously, monochromatic silver editorial",
        "style": "Mugler futurism meets body art, chrome future duo, robotic goddess editorial",
        "quality": "shot on Phase One XF IQ4, chrome detail maximum, portrait 2:3 vertical, 8K"
    },

    # ── G7: 실루엣 & 미니멀 ───────────────────────────────

    "duo_sunset_silhouette": {
        "tag": "Duo Sunset Silhouette",
        "subject": "two silhouette goddesses arms spread wide at Miami rooftop edge against burning sunset, freedom and power",
        "body": "first model slim silhouette arms spread / second model curvy silhouette curves dramatic against burning sky, both worshipping the sunset",
        "outfit": "first model micro string bikini backlit pure silhouette / second model high-cut swimsuit curves as dramatic silhouette against burning orange sky",
        "material": "micro string bikini and high-cut swimsuit, both in pure backlit silhouette, form over coverage",
        "environment": "Miami rooftop at golden hour, city below, sky on fire orange pink purple, ocean beyond",
        "lighting": "pure backlight from setting sun, models in dramatic silhouette, rim light catching curves edges",
        "style": "sunset silhouette duo editorial, Miami heat campaign, Sports Illustrated golden hour",
        "quality": "shot on Sony A7R V, exposed for sky backlit, portrait 2:3 vertical, 8K"
    },

    "duo_desert_minimal": {
        "tag": "Duo Desert Minimal",
        "subject": "two sun goddess models in Sahara at peak golden hour, one kneeling one standing, maximum skin minimum coverage",
        "body": "first model bronzed slim oiled to maximum sheen kneeling / second model powerful curvy sand on glistening skin standing, both Sahara queens",
        "outfit": "first model tiny gold micro triangle bikini, body oiled to mirror sheen / second model copper micro string bikini, sand clinging to oiled curves",
        "material": "gold and copper micro bikini with extreme body oil, minimum fabric maximum gleaming skin",
        "environment": "Sahara Desert dunes at perfect golden hour, sky burning orange and pink, endless ancient sand",
        "lighting": "direct golden hour sun from low angle, shadows dramatic on oiled curves, skin luminous like metal",
        "style": "Sports Illustrated desert goddess duo, golden hour maximum, sun worship editorial",
        "quality": "shot on Canon EOS R5, 85mm golden hour cinematic, portrait 2:3 vertical, 8K"
    },

    "duo_kpop_stage": {
        "tag": "Duo Kpop Stage",
        "subject": "two K-pop goddess models on massive concert stage in dynamic performance poses, explosive synchronized energy",
        "body": "first model slim Korean idol stage presence maximum / second model athletic Korean dancer powerful, both commanding the stage",
        "outfit": "first model holographic micro crop top and micro pleated skirt, stage lighting making holographic fabric disappear / second model iridescent bodysuit cut to absolute minimum, stage presence maximum",
        "material": "holographic and iridescent micro fabrics, both catching and reflecting stage lights in all directions",
        "environment": "massive concert stage with neon light rigs everywhere, fog machine, screaming crowd blurred bokeh",
        "lighting": "concert multi-colored spot lights from all angles, fog catching beams, high energy spectacle lighting",
        "style": "K-pop main stage performance duo editorial, idol power, Blackpink meets Victoria Secret",
        "quality": "shot on Sony A7R V, stage light captured perfectly, portrait 2:3 vertical, 8K"
    },

    "duo_penthouse_power": {
        "tag": "Duo Penthouse Power",
        "subject": "two dominant models at Manhattan penthouse floor-to-ceiling window, city far below them, owning the skyline",
        "body": "first model slim in jet black commanding / second model hourglass in black equally commanding, both facing camera, city their backdrop",
        "outfit": "first model jet black latex open-back micro dress, thigh-high black patent boots, no compromise / second model black latex corset and micro skirt, fishnet thigh highs, maximum power",
        "material": "black latex and black patent leather, both high-gloss, city light reflecting in every surface",
        "environment": "Manhattan penthouse 60th floor, floor-to-ceiling windows, entire city skyline at night below them",
        "lighting": "city lights from far below casting dramatic upward glow, latex catching city light, power from below",
        "style": "Versace power duo editorial, dark luxury penthouse, untouchable wealth glamour",
        "quality": "shot on Hasselblad H6D, city light dramatic, portrait 2:3 vertical, 8K"
    },

    "duo_ice_bath_contrast": {
        "tag": "Duo Ice Bath Contrast",
        "subject": "two models in extreme temperature contrast editorial, one submerged in ice one radiating heat, primal artistic tension",
        "body": "first model slim submerged to chest in ice bath frost on skin / second model curvy standing beside with heat steam rising, sweat glistening, hot versus cold",
        "outfit": "first model ice water covering to chest, frost crystals on bare skin above, cold as only coverage / second model body heat and steam as only covering, maximum sweat gloss",
        "material": "ice water and steam as coverage, bare skin in extreme contrast, body oil on heat model",
        "environment": "minimal white clinical studio, ice bath and rising steam simultaneously, pure white seamless",
        "lighting": "pure white beauty dish light, ice and steam both catching light, clinical cold gorgeous",
        "style": "high concept temperature contrast duo editorial, body art meets science, avant-garde fashion",
        "quality": "shot on Hasselblad X2D, pure white ultra detail, portrait 2:3 vertical, 8K"
    },

}

def create_preset_files():
    """모든 프리셋 JSON 파일 생성"""
    PRESETS_DIR.mkdir(parents=True, exist_ok=True)
    created = []
    skipped = []

    for key, data in DUO_PRESETS.items():
        path = PRESETS_DIR / f"{key}.json"
        if path.exists():
            skipped.append(key)
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        created.append(key)

    print(f"\n✅ 생성 완료: {len(created)}종")
    for k in created:
        print(f"  + {k}.json")

    if skipped:
        print(f"\n⚠️  이미 존재 (스킵): {len(skipped)}종")
        for k in skipped:
            print(f"  - {k}.json")

    return created

if __name__ == "__main__":
    print("듀오 글래머 프리셋 생성 시작...")
    created = create_preset_files()
    print(f"\n총 {len(created)}종 생성 완료")
    print("다음 단계: python add_duo_category.py 실행")
