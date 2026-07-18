# patch_trio_bae123.py
# 실행 위치: C:\Dev\LumineX\
# 실행: python preset_builders/patch_trio_bae123.py

import json
import os
import ast

PRESETS_DIR = "presets"

# ── 프리셋 데이터 ──────────────────────────────────────────────────────
# (key, tier, subject, prompt, environment, lighting, style, quality)

TRIOS = [
    # ── 배치1 HOF ──────────────────────────────────────────────────────
    (
        "trio_bae1_dragon_gold_klimt_versailles", "HOF",
        "Three women — irezumi dragon / 24k gold glitter / Klimt gold leaf bodypaint — Versailles Hall of Mirrors",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Brazilian capoeira goddess, mid-20s, powerful athletic physique — warm bronze skin — body fully covered in Japanese irezumi tattoos: black dragon coiling from ankles to shoulders, deep crimson scales with gold outline, dragon head cresting across chest. CENTER: Nigerian supermodel, early 30s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold glitter: molten metallic powder coating every inch, glitter so dense skin becomes liquid gold sculpture. RIGHT: Korean art student, early 20s, delicate petite physique — porcelain pale skin — body fully covered in Klimt-style gold leaf bodypaint: Byzantine mosaic patterns coating entire body, geometric Art Nouveau gold leaf so intricate skin becomes living altarpiece. LEFT: black stiletto heels, long crimson nails. CENTER: gold stiletto heels, long gold nails. RIGHT: nude stiletto heels, long gold nails. All three: full body high-gloss oil.",
        "Hall of Mirrors, Versailles, gilded baroque arches receding to infinity, crystal chandeliers blazing above, warm candlelight flooding marble floors.",
        "Warm golden candlelight — dragon irezumi scales catching amber left, gold glitter blazing like molten sun center, Klimt gold leaf shimmering Byzantine right — three expressions of gold unified by the gilded hall above.",
        "Versailles triple goddess editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, gilded trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae1_phoenix_teal_vangogh_aurora", "HOF",
        "Three women — irezumi phoenix / teal-violet glitter / Van Gogh Starry Night bodypaint — Iceland aurora",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Japanese fitness model, mid-20s, tall lean elongated physique — warm ivory skin — body fully covered in Japanese irezumi tattoos: crimson-gold phoenix rising from hips to shoulders, wings spread fully across chest, blazing feather tips reaching both arms. CENTER: Scandinavian dancer, early 20s, athletic lithe physique — luminous fair skin — body fully covered in teal-to-violet iridescent glitter: aurora spectrum ultra-fine glitter coating every inch, shifting teal-violet-green with every movement. RIGHT: Cuban artist, late 20s, lush curvy physique — warm caramel skin — body fully covered in Van Gogh Starry Night bodypaint: cobalt blue and gold swirling impasto brushstrokes coating entire body, night sky patterns following every curve. LEFT: crimson stiletto heels, long gold nails. CENTER: violet stiletto heels, long teal nails. RIGHT: cobalt stiletto heels, long cobalt nails. All three: full body high-gloss oil.",
        "Iceland glacier at night, Aurora Borealis exploding across vast dark sky in electric green and violet curtains, glacial blue ice underfoot.",
        "Bioluminescent aurora glow — phoenix feathers blazing crimson-gold left, teal glitter refracting aurora spectrum center, Van Gogh swirls absorbing cobalt light right — three distinct light worlds unified by aurora above.",
        "Aurora trinity goddess editorial.",
        "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, aurora phoenix trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae1_wave_obsidian_pollock_void", "HOF",
        "Three women — irezumi Great Wave / obsidian black glitter / Pollock drip bodypaint — deep space void",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean swimmer, mid-20s, lean streamlined physique — cool fair skin — body fully covered in Japanese irezumi tattoos: Great Wave motif surging from ankles to shoulders, deep indigo-black ink with white foam crests crashing across chest. CENTER: West African sculpture goddess, late 20s, powerful plus-size physique — deep rich skin — body fully covered in obsidian black glitter: void-black ultra-fine glitter coating every inch, matte-and-shine contrast making body disappear into darkness. RIGHT: American CrossFit athlete, mid-20s, powerful muscular definition — medium tan skin — body fully covered in Pollock-style drip bodypaint: dense black and white chaotic splatter coating entire body, drip density so extreme it reads as living action painting. LEFT: black stiletto heels, long indigo nails. CENTER: matte black stiletto heels, long black nails. RIGHT: white stiletto heels, long white nails. All three: full body high-gloss oil.",
        "Pure black void, seamless obsidian backdrop, faint distant nebula tendrils.",
        "Near-zero ambient, stark rim lighting only — wave irezumi catching cold blue rim left, obsidian glitter dissolving into void center, Pollock splatter exploding white strobe right — maximum tension between presence and disappearance.",
        "Vogue Italia black void trinity editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, obsidian void trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae1_skull_violet_dali_monaco", "HOF",
        "Three women — irezumi chrysanthemum skull / violet amethyst glitter / Dalí surrealist bodypaint — Monaco Casino",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Mexican dark goddess, late 20s, lush curvy physique — warm caramel skin — body fully covered in Japanese irezumi tattoos: chrysanthemum skull across chest and abdomen, purple-black ink with silver accent filling entire body. CENTER: French Riviera model, mid-20s, athletic toned physique — luminous fair skin — body fully covered in deep violet amethyst glitter: crystalline purple ultra-fine glitter coating every inch, shifting amethyst-violet-indigo under neon light. RIGHT: Spanish conceptual artist, early 20s, lean angular physique — warm medium skin — body fully covered in Dalí surrealist bodypaint: violet and gold melting clock drip patterns coating entire body, surrealist landscapes dissolving across every limb. LEFT: black stiletto heels, long purple nails. CENTER: violet stiletto heels, long amethyst nails. RIGHT: gold stiletto heels, long violet nails. All three: full body high-gloss oil.",
        "Monaco Casino terrace at night, electric violet neon flooding wet marble, luxury harbor lights glittering below, deep Mediterranean darkness beyond.",
        "Neon violet backlight — skull irezumi silver catching electric violet left, amethyst glitter exploding crystalline center, Dalí melt dripping gold-violet right — dark luxury trinity unified by Monaco neon.",
        "Monaco dark luxury trinity editorial.",
        "Shot on Phase One XF IQ4 85mm f/2.0, 8K UHD, violet noir trinity grade, portrait 3:4 vertical.",
    ),
    # ── 배치1 SS ───────────────────────────────────────────────────────
    (
        "trio_bae1_samurai_emerald_kandinsky_kyoto", "SS",
        "Three women — irezumi samurai armor / emerald glitter / Kandinsky abstract bodypaint — Kyoto bamboo",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Japanese kendo champion, late 20s, tall powerful physique — cool porcelain skin — body fully covered in Japanese irezumi tattoos: samurai armor motif coating entire body, silver-black ink with red lacquer accent across chest and shoulders. CENTER: Ghanaian goddess, mid-20s, full plus-size physique — deep rich skin — body fully covered in emerald forest ultra-fine glitter: deep green crystalline glitter coating every inch, shifting emerald-jade-forest under dawn light. RIGHT: Russian abstract painter, early 20s, delicate petite physique — fair skin — body fully covered in Kandinsky abstract bodypaint: emerald and crimson geometric circles and lines coating entire body, pure abstraction covering every surface. LEFT: black stiletto heels, long red nails. CENTER: emerald stiletto heels, long emerald nails. RIGHT: white stiletto heels, long crimson nails. All three: full body high-gloss oil.",
        "Kyoto bamboo forest at dawn, morning mist weaving through dense green canopy, filtered jade light falling across mossy ground.",
        "Soft dawn diffusion through bamboo — samurai armor catching cold grey-green left, emerald glitter absorbing forest light center, Kandinsky geometry refracting jade-crimson right — warrior serenity unified by Kyoto morning mist.",
        "Kyoto bamboo trinity editorial.",
        "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, jade warrior trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae1_snake_fire_dali_shibuya", "SS",
        "Three women — irezumi emerald snake / fire-orange glitter / Dalí urban bodypaint — Shibuya night",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Chinese contemporary model, mid-20s, lean angular physique — cool fair skin — body fully covered in Japanese irezumi tattoos: emerald snake coiling from ankles to collarbone, lotus blooms scattered across hips, clean black outline throughout. CENTER: Puerto Rican dancer, late 20s, lush curvy physique — warm caramel skin — body fully covered in fire-orange glitter: blazing ember ultra-fine glitter coating every inch, heat shimmer effect making body radiate like living flame. RIGHT: Australian fitness model, mid-20s, powerful athletic physique — medium tan skin — body fully covered in Dalí surrealist bodypaint: neon-orange melting urban landscape drip patterns across entire body, surrealist city dissolving down every limb. LEFT: black stiletto heels, long emerald nails. CENTER: orange stiletto heels, long flame nails. RIGHT: white stiletto heels, long neon nails. All three: full body high-gloss oil.",
        "Shibuya Scramble Crossing at night, neon orange and green advertisement floods blazing across wet pavement, urban chaos reflected in every puddle.",
        "Urban neon flood — snake irezumi emerald catching cool neon left, fire glitter exploding orange ember center, Dalí melt dripping neon-orange right — cool-warm neon collision unified by Shibuya night chaos.",
        "Shibuya neon chaos trinity editorial.",
        "Shot on Hasselblad H6D 85mm f/2.0, 8K UHD, neon chaos trinity grade, portrait 3:4 vertical.",
    ),
    # ── 배치2 HOF ──────────────────────────────────────────────────────
    (
        "trio_bae2_phoenix_snake_violet_aurora", "HOF",
        "Three women — irezumi phoenix / irezumi emerald snake / violet glitter — Iceland aurora",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Japanese fitness model, mid-20s, tall lean elongated physique — warm ivory skin — body fully covered in Japanese irezumi tattoos: crimson-gold phoenix rising from hips to shoulders, wings spread fully across chest, blazing feather tips reaching both arms. CENTER: Chinese contemporary model, mid-20s, lean angular physique — cool fair skin — body fully covered in Japanese irezumi tattoos: emerald snake coiling from ankles to collarbone, lotus blooms scattered across hips, clean black outline throughout. RIGHT: Scandinavian dancer, early 20s, athletic lithe physique — luminous fair skin — body fully covered in deep violet-to-teal iridescent glitter: aurora spectrum ultra-fine glitter coating every inch, shifting violet-teal-green with every movement. LEFT: crimson stiletto heels, long gold nails. CENTER: black stiletto heels, long emerald nails. RIGHT: violet stiletto heels, long teal nails. All three: full body high-gloss oil.",
        "Iceland glacier at night, Aurora Borealis exploding across dark sky in electric violet and green curtains, glacial blue ice underfoot.",
        "Aurora borealis glow — phoenix feathers blazing crimson-gold left, emerald snake refracting cold aurora light center, violet glitter exploding aurora spectrum right — fire and ice unified by northern lights above.",
        "Aurora fire-and-ice trinity editorial.",
        "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, aurora fire-ice trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae2_gold_teal_obsidian_monaco", "HOF",
        "Three women — 24k gold glitter / teal iridescent glitter / obsidian black glitter — Monaco Casino",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Nigerian supermodel, late 20s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold ultra-fine glitter: molten metallic powder coating every inch, liquid gold sculpture effect. CENTER: Scandinavian dancer, early 20s, athletic lithe physique — luminous fair skin — body fully covered in teal-to-violet iridescent glitter: aurora spectrum ultra-fine glitter coating every inch, shifting teal-violet-green with every movement. RIGHT: West African sculpture goddess, late 20s, powerful plus-size physique — deep rich skin — body fully covered in obsidian black glitter: void-black ultra-fine glitter coating every inch, matte-and-shine contrast maximum. LEFT: gold stiletto heels, long gold nails. CENTER: teal stiletto heels, long violet nails. RIGHT: matte black stiletto heels, long black nails. All three: full body high-gloss oil.",
        "Monaco Casino terrace at night, electric violet and gold neon flooding wet marble, luxury harbor lights glittering below, deep Mediterranean darkness beyond.",
        "Neon gold-violet-black trifecta — gold glitter blazing warm left, teal glitter refracting violet neon center, obsidian glitter dissolving into Monaco darkness right — three glitter worlds unified by casino neon.",
        "Monaco glitter trinity editorial.",
        "Shot on Hasselblad H6D 85mm f/2.0, 8K UHD, monaco glitter trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae2_crimson_emerald_silver_void", "HOF",
        "Three women — crimson glitter / emerald glitter / silver glitter — deep space void",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Puerto Rican dancer, late 20s, lush curvy physique — warm caramel skin — body fully covered in crimson-gold ultra-fine glitter: blazing ember glitter coating every inch, liquid fire effect maximum density. CENTER: Ghanaian goddess, mid-20s, full plus-size physique — deep rich skin — body fully covered in emerald forest ultra-fine glitter: deep green crystalline glitter coating every inch, shifting emerald-jade-forest under stark light. RIGHT: Swedish editorial model, mid-20s, tall willowy physique — luminous pale skin — body fully covered in silver moonlight ultra-fine glitter: pale cool silver glitter coating every inch, shifting pearl-white-silver under stark rim light. LEFT: red stiletto heels, long crimson nails. CENTER: emerald stiletto heels, long emerald nails. RIGHT: silver stiletto heels, long silver nails. All three: full body high-gloss oil.",
        "Pure black void, seamless obsidian backdrop, faint nebula tendrils.",
        "Three-point dramatic spotlight — harsh strobe on crimson glitter making fire explode left, cold rim on emerald glitter making forest crystallize center, cool blue on silver glitter making moonlight shatter right — crimson-emerald-silver trinity against pure void.",
        "Vogue Italia triple glitter void editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, triple glitter void grade, portrait 3:4 vertical.",
    ),
    # ── 배치2 SS ───────────────────────────────────────────────────────
    (
        "trio_bae2_wave_peacock_silver_versailles", "SS",
        "Three women — irezumi Great Wave / irezumi peacock / silver glitter — Versailles Hall of Mirrors",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean swimmer, mid-20s, lean streamlined physique — cool fair skin — body fully covered in Japanese irezumi tattoos: Great Wave motif surging from ankles to shoulders, deep indigo-black ink with white foam crests crashing across chest. CENTER: Thai royal beauty, late 20s, classic hourglass physique — warm golden skin — body fully covered in Japanese irezumi tattoos: peacock feather spread across back and chest, teal-gold ink with iridescent eye motifs cascading down both arms and legs. RIGHT: Swedish editorial model, mid-20s, tall willowy physique — luminous pale skin — body fully covered in silver moonlight glitter: pale cool silver ultra-fine glitter coating every inch, shifting pearl-white-silver under chandelier light. LEFT: indigo stiletto heels, long indigo nails. CENTER: teal stiletto heels, long teal nails. RIGHT: silver stiletto heels, long silver nails. All three: full body high-gloss oil.",
        "Hall of Mirrors, Versailles, gilded baroque arches receding to infinity, crystal chandeliers blazing above, warm candlelight flooding marble floors.",
        "Warm golden candlelight with cool silver reflection — wave irezumi indigo catching cold mirror light left, peacock teal-gold blazing warm center, silver glitter exploding chandelier prismatic right — baroque grandeur unifying all three.",
        "Versailles wave-peacock-silver trinity editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, versailles trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae2_dragon_phoenix_crimson_shibuya", "SS",
        "Three women — irezumi dragon / irezumi phoenix / crimson glitter — Shibuya night",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Brazilian capoeira goddess, mid-20s, powerful athletic physique — warm bronze skin — body fully covered in Japanese irezumi tattoos: black dragon coiling from ankles to shoulders, deep crimson scales with gold outline, dragon head dominating chest. CENTER: Japanese fitness model, mid-20s, tall lean elongated physique — warm ivory skin — body fully covered in Japanese irezumi tattoos: crimson-gold phoenix rising from hips to shoulders, wings spread fully across chest, blazing feather tips reaching both arms. RIGHT: Puerto Rican dancer, late 20s, lush curvy physique — warm caramel skin — body fully covered in crimson-gold ultra-fine glitter: blazing ember glitter coating every inch, liquid fire effect, maximum density crimson-amber-gold shift. LEFT: black stiletto heels, long crimson nails. CENTER: gold stiletto heels, long gold nails. RIGHT: red stiletto heels, long flame nails. All three: full body high-gloss oil.",
        "Shibuya Scramble Crossing at night, neon orange and red advertisement floods blazing across wet pavement, urban chaos reflected in every puddle.",
        "Urban crimson-amber neon flood — dragon scales catching red neon left, phoenix feathers blazing gold-crimson center, glitter exploding fire ember right — dragon-phoenix-fire trinity unified by Shibuya night chaos.",
        "Shibuya dragon-phoenix-fire trinity editorial.",
        "Shot on Hasselblad H6D 85mm f/2.0, 8K UHD, crimson neon trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae2_skull_samurai_vangogh_kyoto", "SS",
        "Three women — irezumi skull / irezumi samurai / Van Gogh bodypaint — Kyoto bamboo night",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Mexican dark goddess, late 20s, lush curvy physique — warm caramel skin — body fully covered in Japanese irezumi tattoos: chrysanthemum skull motif across chest and abdomen, purple-black ink with silver accent filling entire body. CENTER: Japanese kendo champion, late 20s, tall powerful physique — cool porcelain skin — body fully covered in Japanese irezumi tattoos: samurai armor motif coating entire body, silver-black ink with red lacquer accent across chest and shoulders. RIGHT: Cuban artist, late 20s, lush curvy physique — warm caramel skin — body fully covered in Van Gogh Starry Night bodypaint: cobalt blue and gold swirling impasto brushstrokes coating entire body, night sky patterns following every curve. LEFT: black stiletto heels, long purple nails. CENTER: black stiletto heels, long red nails. RIGHT: cobalt stiletto heels, long cobalt nails. All three: full body high-gloss oil.",
        "Kyoto bamboo forest at night, moonlight filtering through dense canopy, silver-blue shadows across mossy ground, paper lanterns glowing amber in distance.",
        "Cool moonlight with warm lantern accent — skull irezumi silver catching blue moonlight left, samurai armor catching cold steel light center, Van Gogh swirls absorbing cobalt-gold lantern glow right — warrior night unified by Kyoto moonlight.",
        "Kyoto midnight warrior trinity editorial.",
        "Shot on Phase One XF IQ4 85mm f/2.0, 8K UHD, kyoto midnight trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae2_gold_violet_klimt_dali_aurora", "SS",
        "Three women — 24k gold glitter / violet glitter / Klimt-Dalí fusion bodypaint — Iceland aurora",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Nigerian supermodel, late 20s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold ultra-fine glitter: molten metallic powder coating every inch, liquid gold sculpture effect maximum density. CENTER: French Riviera model, mid-20s, athletic toned physique — luminous fair skin — body fully covered in deep violet amethyst ultra-fine glitter: crystalline purple glitter coating every inch, shifting amethyst-violet-indigo under aurora light. RIGHT: Korean art student, early 20s, delicate petite physique — porcelain pale skin — body fully covered in Klimt-meets-Dalí fusion bodypaint: upper body Klimt gold leaf mosaic Byzantine pattern, lower body Dalí surrealist melt dripping gold into violet, the two styles bleeding into each other at the waist. LEFT: gold stiletto heels, long gold nails. CENTER: violet stiletto heels, long amethyst nails. RIGHT: gold stiletto heels, long violet nails. All three: full body high-gloss oil.",
        "Iceland glacier at night, Aurora Borealis exploding across dark sky in electric gold and violet curtains, glacial blue ice underfoot.",
        "Aurora gold-violet glow — gold glitter blazing warm aurora left, violet glitter refracting purple aurora center, Klimt-Dalí fusion catching both gold and violet light simultaneously right — aurora trinity unified above.",
        "Aurora gold-violet fusion trinity editorial.",
        "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, aurora fusion trinity grade, portrait 3:4 vertical.",
    ),
    # ── 배치3 HOF ──────────────────────────────────────────────────────
    (
        "trio_bae3_koi_samurai_emerald_aurora", "HOF",
        "Three women — irezumi koi / irezumi samurai armor / emerald glitter — Iceland aurora",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Vietnamese ballet dancer, early 20s, delicate petite physique — warm golden skin — body fully covered in Japanese irezumi tattoos from neck to ankle: coral-gold koi ascending full body, cherry blossom petals covering entire legs to ankles, full body coverage from neck to ankle. CENTER: Japanese kendo champion, late 20s, tall powerful physique — cool porcelain skin — body fully covered in Japanese irezumi tattoos from neck to ankle: samurai armor motif coating entire body, silver-black ink with red lacquer accent, full body coverage from neck to ankle. RIGHT: Ghanaian goddess, mid-20s, full plus-size physique — deep rich skin — body fully covered in emerald forest ultra-fine glitter: deep green crystalline glitter coating every inch from neck to ankle, shifting emerald-jade-forest. LEFT: rose gold stiletto heels, long coral nails. CENTER: black stiletto heels, long red nails. RIGHT: emerald stiletto heels, long emerald nails. All three: full body high-gloss oil.",
        "Iceland glacier at night, Aurora Borealis in electric green and violet curtains across dark sky, glacial blue ice underfoot.",
        "Aurora green glow — koi coral-gold catching warm aurora left, samurai armor catching cold steel-green light center, emerald glitter absorbing forest aurora right — warrior-nature trinity unified by northern lights.",
        "Aurora warrior-nature trinity editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora warrior trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae3_snake_peacock_crimson_versailles", "HOF",
        "Three women — irezumi emerald snake / irezumi peacock / crimson glitter — Versailles Hall of Mirrors",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Chinese contemporary model, mid-20s, lean angular physique — cool fair skin — body fully covered in Japanese irezumi tattoos from neck to ankle: emerald snake coiling full body from ankles to collarbone, lotus blooms covering entire legs, full body coverage from neck to ankle. CENTER: Thai royal beauty, late 20s, classic hourglass physique — warm golden skin — body fully covered in Japanese irezumi tattoos from neck to ankle: peacock feather spread covering entire body, teal-gold ink with iridescent eye motifs covering entire legs to ankles, full body coverage from neck to ankle. RIGHT: Puerto Rican dancer, late 20s, lush curvy physique — warm caramel skin — body fully covered in crimson-gold ultra-fine glitter: blazing ember glitter coating every inch from neck to ankle, liquid fire effect. LEFT: black stiletto heels, long emerald nails. CENTER: teal stiletto heels, long teal nails. RIGHT: red stiletto heels, long crimson nails. All three: full body high-gloss oil.",
        "Hall of Mirrors, Versailles, gilded baroque arches receding to infinity, crystal chandeliers blazing above, warm candlelight flooding marble floors.",
        "Warm golden candlelight — emerald snake catching amber glow left, peacock teal-gold blazing warm center, crimson glitter exploding fire right — snake-peacock-fire trinity unified by Versailles golden hall.",
        "Versailles snake-peacock-fire trinity editorial.",
        "Shot on Hasselblad H6D 110mm f/2.8, 8K UHD, versailles fire trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae3_gold_silver_crimson_shibuya", "HOF",
        "Three women — 24k gold glitter / silver glitter / crimson glitter — Shibuya Scramble Crossing",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Nigerian supermodel, late 20s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold ultra-fine glitter: molten metallic powder coating every inch from neck to ankle, liquid gold sculpture effect. CENTER: Swedish editorial model, mid-20s, tall willowy physique — luminous pale skin — body fully covered in silver moonlight ultra-fine glitter: pale cool silver glitter coating every inch from neck to ankle, shifting pearl-white-silver. RIGHT: Puerto Rican dancer, late 20s, lush curvy physique — warm caramel skin — body fully covered in crimson-gold ultra-fine glitter: blazing ember glitter coating every inch from neck to ankle, liquid fire effect. LEFT: gold stiletto heels, long gold nails. CENTER: silver stiletto heels, long silver nails. RIGHT: red stiletto heels, long crimson nails. All three: full body high-gloss oil.",
        "Shibuya Scramble Crossing at night, neon gold and red advertisement floods blazing across wet pavement, urban chaos reflected in every puddle.",
        "Urban neon gold-silver-red flood — gold glitter blazing warm neon left, silver glitter catching cool neon center, crimson glitter exploding red ember right — gold-silver-crimson trinity unified by Shibuya neon chaos.",
        "Shibuya glitter trinity editorial.",
        "Shot on Phase One XF IQ4 85mm f/2.0, 8K UHD, shibuya glitter trinity grade, portrait 3:4 vertical.",
    ),
    # ── 배치3 SS ───────────────────────────────────────────────────────
    (
        "trio_bae3_phoenix_skull_violet_void", "SS",
        "Three women — irezumi phoenix / irezumi skull / violet glitter — deep space void",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Japanese fitness model, mid-20s, tall lean elongated physique — warm ivory skin — body fully covered in Japanese irezumi tattoos from neck to ankle: crimson-gold phoenix rising from ankles to shoulders, wings spread fully across chest, full body coverage from neck to ankle. CENTER: Mexican dark goddess, late 20s, lush curvy physique — warm caramel skin — body fully covered in Japanese irezumi tattoos from neck to ankle: chrysanthemum skull across chest, purple-black ink with silver accent, full body coverage from neck to ankle. RIGHT: French Riviera model, mid-20s, athletic toned physique — luminous fair skin — body fully covered in deep violet amethyst ultra-fine glitter: crystalline purple glitter coating every inch from neck to ankle, shifting amethyst-violet-indigo. LEFT: crimson stiletto heels, long gold nails. CENTER: black stiletto heels, long purple nails. RIGHT: violet stiletto heels, long amethyst nails. All three: full body high-gloss oil.",
        "Pure black void, seamless obsidian backdrop, faint distant nebula tendrils.",
        "Three-point dramatic spotlight — warm amber on phoenix making feathers blaze left, cold blue rim on skull making silver accents gleam center, harsh strobe on violet glitter making amethyst explode right — deep shadows between bodies creating maximum tension.",
        "Vogue Italia phoenix-skull-violet void trinity editorial.",
        "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, void trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae3_teal_violet_obsidian_kyoto", "SS",
        "Three women — teal glitter / violet glitter / obsidian black glitter — Kyoto bamboo forest night",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Scandinavian dancer, early 20s, athletic lithe physique — luminous fair skin — body fully covered in teal-to-green iridescent ultra-fine glitter: aurora spectrum glitter coating every inch from neck to ankle, shifting teal-green-jade. CENTER: French Riviera model, mid-20s, athletic toned physique — luminous fair skin — body fully covered in deep violet amethyst ultra-fine glitter: crystalline purple glitter coating every inch from neck to ankle, shifting amethyst-violet-indigo. RIGHT: West African sculpture goddess, late 20s, powerful plus-size physique — deep rich skin — body fully covered in obsidian black ultra-fine glitter: void-black glitter coating every inch from neck to ankle, matte-and-shine contrast maximum. LEFT: teal stiletto heels, long teal nails. CENTER: violet stiletto heels, long amethyst nails. RIGHT: matte black stiletto heels, long black nails. All three: full body high-gloss oil.",
        "Kyoto bamboo forest at night, moonlight filtering through dense canopy, silver-blue shadows across mossy ground, paper lanterns glowing amber in distance.",
        "Cool moonlight with warm lantern accent — teal glitter catching jade moonlight left, violet glitter absorbing purple shadow center, obsidian glitter dissolving into Kyoto darkness right — three glitter worlds unified by bamboo night.",
        "Kyoto midnight glitter trinity editorial.",
        "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, kyoto glitter trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae3_dragon_koi_pollock_aurora", "SS",
        "Three women — irezumi dragon / irezumi koi / Pollock drip bodypaint — Iceland aurora",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Brazilian capoeira goddess, mid-20s, powerful athletic physique — warm bronze skin — body fully covered in Japanese irezumi tattoos from neck to ankle: black dragon coiling full body, deep crimson scales with gold outline, full body coverage from neck to ankle. CENTER: Vietnamese ballet dancer, early 20s, delicate petite physique — warm golden skin — body fully covered in Japanese irezumi tattoos from neck to ankle: coral-gold koi ascending full body, cherry blossom petals covering entire legs to ankles, full body coverage from neck to ankle. RIGHT: American CrossFit athlete, mid-20s, powerful muscular definition — medium tan skin — body fully covered in Pollock-style drip bodypaint: dense black and white chaotic splatter coating entire body from neck to ankle, drip density maximum. LEFT: black stiletto heels, long crimson nails. CENTER: rose gold stiletto heels, long coral nails. RIGHT: white stiletto heels, long white nails. All three: full body high-gloss oil.",
        "Iceland glacier at night, Aurora Borealis exploding across dark sky in electric green and violet curtains, glacial blue ice underfoot.",
        "Aurora borealis glow — dragon crimson scales catching cold aurora left, koi coral-gold glowing warm center, Pollock splatter refracting aurora spectrum right — dragon-koi-chaos trinity unified by northern lights above.",
        "Aurora dragon-koi-chaos trinity editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora chaos trinity grade, portrait 3:4 vertical.",
    ),
    (
        "trio_bae3_wave_phoenix_vangogh_versailles", "SS",
        "Three women — irezumi Great Wave / irezumi phoenix / Van Gogh bodypaint — Versailles Hall of Mirrors",
        "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: Korean swimmer, mid-20s, lean streamlined physique — cool fair skin — body fully covered in Japanese irezumi tattoos from neck to ankle: Great Wave motif surging across entire body, deep indigo-black ink with white foam crests, full body coverage from neck to ankle. CENTER: Japanese fitness model, mid-20s, tall lean elongated physique — warm ivory skin — body fully covered in Japanese irezumi tattoos from neck to ankle: crimson-gold phoenix rising full body from ankles to shoulders, wings spread across chest, full body coverage from neck to ankle. RIGHT: Cuban artist, late 20s, lush curvy physique — warm caramel skin — body fully covered in Van Gogh Starry Night bodypaint: cobalt blue and gold swirling impasto brushstrokes coating entire body from neck to ankle, full body coverage. LEFT: indigo stiletto heels, long indigo nails. CENTER: gold stiletto heels, long crimson nails. RIGHT: cobalt stiletto heels, long cobalt nails. All three: full body high-gloss oil.",
        "Hall of Mirrors, Versailles, gilded baroque arches receding to infinity, crystal chandeliers blazing above, warm candlelight flooding marble floors.",
        "Warm golden candlelight with cool mirror reflection — wave indigo catching cool mirror light left, phoenix crimson-gold blazing warm center, Van Gogh cobalt-gold swirls absorbing chandelier glow right — wave-phoenix-starry trinity unified by Versailles.",
        "Versailles wave-phoenix-starry trinity editorial.",
        "Shot on Hasselblad H6D 110mm f/2.8, 8K UHD, versailles starry trinity grade, portrait 3:4 vertical.",
    ),
]

# ── JSON 파일 생성 ────────────────────────────────────────────────────
hof_keys = []
ss_keys = []

for key, tier, subject, prompt, environment, lighting, style, quality in TRIOS:
    data = {
        "subject": subject,
        "prompt": prompt,
        "environment": environment,
        "lighting": lighting,
        "style": style,
        "quality": quality,
    }
    path = os.path.join(PRESETS_DIR, f"{key}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ {key}.json [{tier}]")

    if tier == "HOF":
        hof_keys.append(key)
    else:
        ss_keys.append(key)

print(f"\nJSON 생성 완료: HOF {len(hof_keys)}종 / SS {len(ss_keys)}종")

# ── presets_meta.py 패치 ─────────────────────────────────────────────
META_FILE = "core/presets_meta.py"
with open(META_FILE, encoding="utf-8-sig") as f:
    meta = f.read()

NEW_BLOCK = '''

# ── Bare Art Ensemble: Trio bae1 ──────────────────────────────────────
BARE_ART_TRIO_BAE1 = {
''' + "".join(f'''    "{k}": {{"name": "{k}", "tier": "{"HOF" if k in hof_keys else "SS"}"}},\n''' for k, t, *_ in TRIOS if "bae1" in k) + '''}

# ── Bare Art Ensemble: Trio bae2 ──────────────────────────────────────
BARE_ART_TRIO_BAE2 = {
''' + "".join(f'''    "{k}": {{"name": "{k}", "tier": "{"HOF" if k in hof_keys else "SS"}"}},\n''' for k, t, *_ in TRIOS if "bae2" in k) + '''}

# ── Bare Art Ensemble: Trio bae3 ──────────────────────────────────────
BARE_ART_TRIO_BAE3 = {
''' + "".join(f'''    "{k}": {{"name": "{k}", "tier": "{"HOF" if k in hof_keys else "SS"}"}},\n''' for k, t, *_ in TRIOS if "bae3" in k) + '''}
'''

if "BARE_ART_TRIO_BAE1" not in meta:
    meta = meta.rstrip() + "\n" + NEW_BLOCK
    print("✅ presets_meta.py 블록 추가 완료")
else:
    print("⚠️  BARE_ART_TRIO_BAE1 이미 존재 — 스킵")

with open(META_FILE, "w", encoding="utf-8") as f:
    f.write(meta)

# ── hof_tier.py 패치 ─────────────────────────────────────────────────
HOF_FILE = "core/hof_tier.py"
with open(HOF_FILE, encoding="utf-8-sig") as f:
    hof_content = f.read()

added_hof = 0
for key in hof_keys:
    if f'"{key}"' not in hof_content:
        hof_content = hof_content.rstrip()
        hof_content += f'\n    "{key}",'
        added_hof += 1

with open(HOF_FILE, "w", encoding="utf-8") as f:
    f.write(hof_content)
print(f"✅ hof_tier.py에 {added_hof}종 추가")

# ── sss_tier.py SS 패치 ───────────────────────────────────────────────
SSS_FILE = "core/sss_tier.py"
with open(SSS_FILE, encoding="utf-8-sig") as f:
    sss_content = f.read()

added_ss = 0
for key in ss_keys:
    if f'"{key}"' not in sss_content:
        sss_content = sss_content.rstrip()
        sss_content += f'\n    "{key}",'
        added_ss += 1

with open(SSS_FILE, "w", encoding="utf-8") as f:
    f.write(sss_content)
print(f"✅ sss_tier.py에 {added_ss}종 추가")

# ── 최종 검증 ─────────────────────────────────────────────────────────
ast.parse(open(META_FILE, encoding="utf-8").read())
print("\n✅ presets_meta.py AST 검증 통과")
print(f"✅ JSON {len(TRIOS)}개 생성")
print(f"✅ HOF {len(hof_keys)}종 / SS {len(ss_keys)}종 등록 완료")
print("\n다음 단계:")
print('git add -A')
print('git commit -m "feat: Bare Art Ensemble trio bae1~3 (HOF 10종 + SS 9종)"')
print('git push')
