# patch_quad_bae1.py
# 실행 위치: C:\Dev\LumineX\
# 실행: python preset_builders/patch_quad_bae1.py

import json
import os
import ast

PRESETS_DIR = "presets"

QUADS = [
    # ── HOF ───────────────────────────────────────────────────────────
    (
        "quad_bae1_dragon_gold_klimt_obsidian_void", "HOF",
        "Four women — irezumi dragon / 24k gold glitter / Klimt bodypaint / obsidian glitter — deep space void",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Brazilian capoeira goddess, mid-20s, powerful athletic physique — warm bronze skin — body fully covered in Japanese irezumi tattoos from neck to ankle: black dragon coiling full body, deep crimson scales with gold outline, full body coverage. CENTER-LEFT: Nigerian supermodel, late 20s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold ultra-fine glitter: molten metallic powder coating every inch from neck to ankle, liquid gold sculpture effect. CENTER-RIGHT: Korean art student, early 20s, delicate petite physique — porcelain pale skin — body fully covered in Klimt-style gold leaf bodypaint: Byzantine mosaic patterns coating entire body from neck to ankle, geometric Art Nouveau gold leaf. RIGHT: West African sculpture goddess, late 20s, powerful plus-size physique — deep rich skin — body fully covered in obsidian black ultra-fine glitter: void-black glitter coating every inch from neck to ankle, matte-and-shine contrast maximum. LEFT: black stiletto heels, long crimson nails. CENTER-LEFT: gold stiletto heels, long gold nails. CENTER-RIGHT: nude stiletto heels, long gold nails. RIGHT: matte black stiletto heels, long black nails. All four: full body high-gloss oil.",
        "Pure black void, seamless obsidian backdrop, faint distant nebula tendrils.",
        "Four-point dramatic spotlight — cold blue rim on dragon left, warm strobe on gold glitter center-left, warm amber on Klimt center-right, near-zero rim on obsidian right dissolving into void — gold-dark spectrum unified by obsidian backdrop.",
        "Vogue Italia four-goddess void editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, obsidian quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_koi_violet_dali_emerald_monaco", "HOF",
        "Four women — irezumi koi / violet glitter / Dalí bodypaint / emerald glitter — Monaco Casino",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Vietnamese ballet dancer, early 20s, delicate petite physique — warm golden skin — body fully covered in Japanese irezumi tattoos from neck to ankle: coral-gold koi ascending full body, cherry blossom petals covering entire legs to ankles, full body coverage. CENTER-LEFT: French Riviera model, mid-20s, athletic toned physique — luminous fair skin — body fully covered in deep violet amethyst ultra-fine glitter: crystalline purple glitter coating every inch from neck to ankle, shifting amethyst-violet-indigo. CENTER-RIGHT: Spanish conceptual artist, early 20s, lean angular physique — warm medium skin — body fully covered in Dalí surrealist bodypaint: violet and gold melting clock drip patterns coating entire body from neck to ankle, surrealist landscapes dissolving across every limb. RIGHT: Ghanaian goddess, mid-20s, full plus-size physique — deep rich skin — body fully covered in emerald forest ultra-fine glitter: deep green crystalline glitter coating every inch from neck to ankle, shifting emerald-jade-forest. LEFT: rose gold stiletto heels, long coral nails. CENTER-LEFT: violet stiletto heels, long amethyst nails. CENTER-RIGHT: gold stiletto heels, long violet nails. RIGHT: emerald stiletto heels, long emerald nails. All four: full body high-gloss oil.",
        "Monaco Casino terrace at night, electric violet and gold neon flooding wet marble, luxury harbor lights glittering below, deep Mediterranean darkness beyond.",
        "Neon violet-gold flood — koi coral catching warm gold neon left, violet glitter exploding amethyst center-left, Dalí melt dripping violet-gold center-right, emerald glitter catching cool neon right — four-way luxury unified by Monaco casino glow.",
        "Monaco four-goddess editorial.",
        "Shot on Hasselblad H6D 85mm f/2.0, 8K UHD, monaco quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_snake_peacock_gold_silver_void", "HOF",
        "Four women — irezumi snake / irezumi peacock / 24k gold glitter / silver glitter — deep space void",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Chinese contemporary model, mid-20s, lean angular physique — cool fair skin — body fully covered in Japanese irezumi tattoos from neck to ankle: emerald snake coiling full body from ankles to collarbone, lotus blooms covering entire legs, full body coverage. CENTER-LEFT: Thai royal beauty, late 20s, classic hourglass physique — warm golden skin — body fully covered in Japanese irezumi tattoos from neck to ankle: peacock feather spread covering entire body, teal-gold ink with iridescent eye motifs covering entire legs to ankles, full body coverage. CENTER-RIGHT: Nigerian supermodel, late 20s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold ultra-fine glitter: molten metallic powder coating every inch from neck to ankle, liquid gold sculpture effect. RIGHT: Swedish editorial model, mid-20s, tall willowy physique — luminous pale skin — body fully covered in silver moonlight ultra-fine glitter: pale cool silver glitter coating every inch from neck to ankle, shifting pearl-white-silver. LEFT: black stiletto heels, long emerald nails. CENTER-LEFT: teal stiletto heels, long teal nails. CENTER-RIGHT: gold stiletto heels, long gold nails. RIGHT: silver stiletto heels, long silver nails. All four: full body high-gloss oil.",
        "Pure black void, seamless obsidian backdrop, faint distant nebula tendrils.",
        "Four-point dramatic spotlight — cold green rim on snake left, warm gold on peacock center-left, harsh strobe on gold glitter center-right, cool blue on silver glitter right — nature-luxury quad unified by void darkness.",
        "Vogue Italia nature-luxury void quad editorial.",
        "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, void quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_gold_silver_crimson_emerald_versailles", "HOF",
        "Four women — 24k gold / silver / crimson / emerald glitter — Versailles Hall of Mirrors",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Nigerian supermodel, late 20s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold ultra-fine glitter: molten metallic powder coating every inch from neck to ankle, liquid gold sculpture effect. CENTER-LEFT: Swedish editorial model, mid-20s, tall willowy physique — luminous pale skin — body fully covered in silver moonlight ultra-fine glitter: pale cool silver glitter coating every inch from neck to ankle, shifting pearl-white-silver. CENTER-RIGHT: Puerto Rican dancer, late 20s, lush curvy physique — warm caramel skin — body fully covered in crimson-gold ultra-fine glitter: blazing ember glitter coating every inch from neck to ankle, liquid fire effect. RIGHT: Ghanaian goddess, mid-20s, full plus-size physique — deep rich skin — body fully covered in emerald forest ultra-fine glitter: deep green crystalline glitter coating every inch from neck to ankle, shifting emerald-jade-forest. LEFT: gold stiletto heels, long gold nails. CENTER-LEFT: silver stiletto heels, long silver nails. CENTER-RIGHT: red stiletto heels, long crimson nails. RIGHT: emerald stiletto heels, long emerald nails. All four: full body high-gloss oil.",
        "Hall of Mirrors, Versailles, gilded baroque arches receding to infinity, crystal chandeliers blazing above, warm candlelight flooding marble floors.",
        "Warm golden chandelier light — gold glitter blazing molten left, silver glitter catching prismatic mirror center-left, crimson glitter blazing fire center-right, emerald glitter catching warm-green refraction right — four-glitter spectrum unified by Versailles gold.",
        "Versailles four-glitter goddess editorial.",
        "Shot on Hasselblad H6D 110mm f/2.8, 8K UHD, versailles glitter quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_dragon_wave_gold_obsidian_shibuya", "HOF",
        "Four women — irezumi dragon / irezumi Great Wave / 24k gold glitter / obsidian glitter — Shibuya night",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Brazilian capoeira goddess, mid-20s, powerful athletic physique — warm bronze skin — body fully covered in Japanese irezumi tattoos from neck to ankle: black dragon coiling full body, deep crimson scales with gold outline, full body coverage from neck to ankle. CENTER-LEFT: Korean swimmer, mid-20s, lean streamlined physique — cool fair skin — body fully covered in Japanese irezumi tattoos from neck to ankle: Great Wave motif surging across entire body, deep indigo-black ink with white foam crests, full body coverage. CENTER-RIGHT: Nigerian supermodel, late 20s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold ultra-fine glitter: molten metallic powder coating every inch from neck to ankle, liquid gold sculpture effect. RIGHT: West African sculpture goddess, late 20s, powerful plus-size physique — deep rich skin — body fully covered in obsidian black ultra-fine glitter: void-black glitter coating every inch from neck to ankle, matte-and-shine contrast maximum. LEFT: black stiletto heels, long crimson nails. CENTER-LEFT: indigo stiletto heels, long indigo nails. CENTER-RIGHT: gold stiletto heels, long gold nails. RIGHT: matte black stiletto heels, long black nails. All four: full body high-gloss oil.",
        "Shibuya Scramble Crossing at night, neon gold and blue advertisement floods blazing across wet pavement, urban chaos reflected in every puddle.",
        "Urban neon gold-blue-black flood — dragon crimson catching blue neon left, wave indigo refracting gold light center-left, gold glitter blazing liquid metal center-right, obsidian glitter dissolving into Shibuya darkness right — four-way urban quad unified by neon chaos.",
        "Shibuya urban quad editorial.",
        "Shot on Phase One XF IQ4 85mm f/2.0, 8K UHD, shibuya urban quad grade, portrait 4:5 vertical.",
    ),
    # ── SS ────────────────────────────────────────────────────────────
    (
        "quad_bae1_phoenix_teal_vangogh_silver_aurora", "SS",
        "Four women — irezumi phoenix / teal glitter / Van Gogh bodypaint / silver glitter — Iceland aurora",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Japanese fitness model, mid-20s, tall lean elongated physique — warm ivory skin — body fully covered in Japanese irezumi tattoos from neck to ankle: crimson-gold phoenix rising full body, wings spread across chest, full body coverage from neck to ankle. CENTER-LEFT: Scandinavian dancer, early 20s, athletic lithe physique — luminous fair skin — body fully covered in teal-to-violet iridescent ultra-fine glitter: aurora spectrum glitter coating every inch from neck to ankle, shifting teal-violet-green. CENTER-RIGHT: Cuban artist, late 20s, lush curvy physique — warm caramel skin — body fully covered in Van Gogh Starry Night bodypaint: cobalt blue and gold swirling impasto brushstrokes coating entire body from neck to ankle, full body coverage. RIGHT: Swedish editorial model, mid-20s, tall willowy physique — luminous pale skin — body fully covered in silver moonlight ultra-fine glitter: pale cool silver glitter coating every inch from neck to ankle, shifting pearl-white-silver. LEFT: crimson stiletto heels, long gold nails. CENTER-LEFT: violet stiletto heels, long teal nails. CENTER-RIGHT: cobalt stiletto heels, long cobalt nails. RIGHT: silver stiletto heels, long silver nails. All four: full body high-gloss oil.",
        "Iceland glacier at night, Aurora Borealis exploding across vast dark sky in electric green and violet curtains, glacial blue ice underfoot.",
        "Bioluminescent aurora glow — phoenix feathers blazing crimson-gold left, teal glitter refracting aurora center-left, Van Gogh swirls absorbing cobalt light center-right, silver glitter catching cool aurora right — four-way aurora spectrum unified above.",
        "Aurora four-goddess editorial.",
        "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, aurora quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_wave_skull_crimson_pollock_versailles", "SS",
        "Four women — irezumi Great Wave / irezumi skull / crimson glitter / Pollock bodypaint — Versailles",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Korean swimmer, mid-20s, lean streamlined physique — cool fair skin — body fully covered in Japanese irezumi tattoos from neck to ankle: Great Wave motif surging across entire body, deep indigo-black ink with white foam crests, full body coverage. CENTER-LEFT: Mexican dark goddess, late 20s, lush curvy physique — warm caramel skin — body fully covered in Japanese irezumi tattoos from neck to ankle: chrysanthemum skull across chest, purple-black ink with silver accent, full body coverage from neck to ankle. CENTER-RIGHT: Puerto Rican dancer, late 20s, powerful athletic physique — warm tan skin — body fully covered in crimson-gold ultra-fine glitter: blazing ember glitter coating every inch from neck to ankle, liquid fire effect. RIGHT: American CrossFit athlete, mid-20s, powerful muscular definition — medium tan skin — body fully covered in Pollock-style drip bodypaint: dense black and white chaotic splatter coating entire body from neck to ankle, drip density maximum. LEFT: indigo stiletto heels, long indigo nails. CENTER-LEFT: black stiletto heels, long purple nails. CENTER-RIGHT: red stiletto heels, long crimson nails. RIGHT: white stiletto heels, long white nails. All four: full body high-gloss oil.",
        "Hall of Mirrors, Versailles, gilded baroque arches receding to infinity, crystal chandeliers blazing above, warm candlelight flooding marble floors.",
        "Warm golden candlelight — wave indigo catching cool mirror light left, skull silver catching candlelight center-left, crimson glitter blazing fire center-right, Pollock splatter refracting chandelier right — four-way contrast unified by Versailles gold.",
        "Versailles four-goddess editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, versailles quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_samurai_gold_teal_vangogh_kyoto", "SS",
        "Four women — irezumi samurai / gold glitter / teal glitter / Van Gogh bodypaint — Kyoto bamboo night",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Japanese kendo champion, late 20s, tall powerful physique — cool porcelain skin — body fully covered in Japanese irezumi tattoos from neck to ankle: samurai armor motif coating entire body, silver-black ink with red lacquer accent, full body coverage. CENTER-LEFT: Nigerian supermodel, late 20s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold ultra-fine glitter: molten metallic powder coating every inch from neck to ankle, liquid gold sculpture effect. CENTER-RIGHT: Scandinavian dancer, early 20s, athletic lithe physique — luminous fair skin — body fully covered in teal-to-violet iridescent ultra-fine glitter: aurora spectrum glitter coating every inch from neck to ankle, shifting teal-violet-green. RIGHT: Cuban artist, late 20s, lush curvy physique — warm caramel skin — body fully covered in Van Gogh Starry Night bodypaint: cobalt blue and gold swirling impasto brushstrokes coating entire body from neck to ankle, full body coverage. LEFT: black stiletto heels, long red nails. CENTER-LEFT: gold stiletto heels, long gold nails. CENTER-RIGHT: teal stiletto heels, long teal nails. RIGHT: cobalt stiletto heels, long cobalt nails. All four: full body high-gloss oil.",
        "Kyoto bamboo forest at night, moonlight filtering through dense canopy, silver-blue shadows across mossy ground, paper lanterns glowing amber in distance.",
        "Cool moonlight with warm lantern accent — samurai armor catching steel moonlight left, gold glitter blazing warm lantern center-left, teal glitter catching jade moonlight center-right, Van Gogh swirls absorbing cobalt-gold glow right — warrior night unified by Kyoto bamboo.",
        "Kyoto four-goddess editorial.",
        "Shot on Phase One XF IQ4 85mm f/2.0, 8K UHD, kyoto quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_dragon_phoenix_crimson_violet_shibuya", "SS",
        "Four women — irezumi dragon / irezumi phoenix / crimson glitter / violet glitter — Shibuya night",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Brazilian capoeira goddess, mid-20s, powerful athletic physique — warm bronze skin — body fully covered in Japanese irezumi tattoos from neck to ankle: black dragon coiling full body, deep crimson scales with gold outline, full body coverage from neck to ankle. CENTER-LEFT: Japanese fitness model, mid-20s, tall lean elongated physique — warm ivory skin — body fully covered in Japanese irezumi tattoos from neck to ankle: crimson-gold phoenix rising full body from ankles to shoulders, wings spread across chest, full body coverage. CENTER-RIGHT: Puerto Rican dancer, late 20s, lush curvy physique — warm caramel skin — body fully covered in crimson-gold ultra-fine glitter: blazing ember glitter coating every inch from neck to ankle, liquid fire effect. RIGHT: French Riviera model, mid-20s, athletic toned physique — luminous fair skin — body fully covered in deep violet amethyst ultra-fine glitter: crystalline purple glitter coating every inch from neck to ankle, shifting amethyst-violet-indigo. LEFT: black stiletto heels, long crimson nails. CENTER-LEFT: gold stiletto heels, long gold nails. CENTER-RIGHT: red stiletto heels, long crimson nails. RIGHT: violet stiletto heels, long amethyst nails. All four: full body high-gloss oil.",
        "Shibuya Scramble Crossing at night, neon crimson and violet advertisement floods blazing across wet pavement, urban chaos reflected in every puddle.",
        "Urban crimson-violet neon flood — dragon scales catching red neon left, phoenix feathers blazing gold-crimson center-left, crimson glitter exploding fire center-right, violet glitter catching purple neon right — dragon-phoenix-fire-violet quad unified by Shibuya chaos.",
        "Shibuya four-goddess editorial.",
        "Shot on Phase One XF IQ4 85mm f/2.0, 8K UHD, shibuya quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_koi_samurai_teal_pollock_aurora", "SS",
        "Four women — irezumi koi / irezumi samurai / teal glitter / Pollock bodypaint — Iceland aurora",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Vietnamese ballet dancer, early 20s, delicate petite physique — warm golden skin — body fully covered in Japanese irezumi tattoos from neck to ankle: coral-gold koi ascending full body, cherry blossom petals covering entire legs, full body coverage. CENTER-LEFT: Japanese kendo champion, late 20s, tall powerful physique — cool porcelain skin — body fully covered in Japanese irezumi tattoos from neck to ankle: samurai armor motif coating entire body, silver-black ink with red lacquer accent, full body coverage. CENTER-RIGHT: Scandinavian dancer, early 20s, athletic lithe physique — luminous fair skin — body fully covered in teal-to-violet iridescent ultra-fine glitter: aurora spectrum glitter coating every inch from neck to ankle, shifting teal-violet-green. RIGHT: American CrossFit athlete, mid-20s, powerful muscular definition — medium tan skin — body fully covered in Pollock-style drip bodypaint: dense black and white chaotic splatter coating entire body from neck to ankle, drip density maximum. LEFT: rose gold stiletto heels, long coral nails. CENTER-LEFT: black stiletto heels, long red nails. CENTER-RIGHT: teal stiletto heels, long teal nails. RIGHT: white stiletto heels, long white nails. All four: full body high-gloss oil.",
        "Iceland glacier at night, Aurora Borealis in electric green and violet curtains across dark sky, glacial blue ice underfoot.",
        "Aurora glow — koi coral-gold catching warm aurora left, samurai armor catching cold steel-green center-left, teal glitter refracting aurora spectrum center-right, Pollock splatter exploding white strobe right — warrior-nature-chaos quad unified by northern lights.",
        "Aurora warrior quad editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora warrior quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_snake_gold_violet_vangogh_monaco", "SS",
        "Four women — irezumi snake / gold glitter / violet glitter / Van Gogh bodypaint — Monaco Casino",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Chinese contemporary model, mid-20s, lean angular physique — cool fair skin — body fully covered in Japanese irezumi tattoos from neck to ankle: emerald snake coiling full body, lotus blooms covering entire legs, full body coverage from neck to ankle. CENTER-LEFT: Nigerian supermodel, late 20s, commanding hourglass physique — deep ebony skin — body fully covered in 24k gold ultra-fine glitter: molten metallic powder coating every inch from neck to ankle, liquid gold sculpture effect. CENTER-RIGHT: French Riviera model, mid-20s, athletic toned physique — luminous fair skin — body fully covered in deep violet amethyst ultra-fine glitter: crystalline purple glitter coating every inch from neck to ankle, shifting amethyst-violet-indigo. RIGHT: Cuban artist, late 20s, lush curvy physique — warm caramel skin — body fully covered in Van Gogh Starry Night bodypaint: cobalt blue and gold swirling impasto brushstrokes coating entire body from neck to ankle, full body coverage. LEFT: black stiletto heels, long emerald nails. CENTER-LEFT: gold stiletto heels, long gold nails. CENTER-RIGHT: violet stiletto heels, long amethyst nails. RIGHT: cobalt stiletto heels, long cobalt nails. All four: full body high-gloss oil.",
        "Monaco Casino terrace at night, electric violet and gold neon flooding wet marble, luxury harbor lights glittering below, deep Mediterranean darkness beyond.",
        "Neon violet-gold flood — emerald snake catching cool neon left, gold glitter blazing warm center-left, violet glitter exploding amethyst center-right, Van Gogh swirls absorbing cobalt-violet right — nature-luxury-art quad unified by Monaco neon.",
        "Monaco four-goddess editorial.",
        "Shot on Hasselblad H6D 85mm f/2.0, 8K UHD, monaco art quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_phoenix_skull_emerald_silver_kyoto", "SS",
        "Four women — irezumi phoenix / irezumi skull / emerald glitter / silver glitter — Kyoto bamboo night",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Japanese fitness model, mid-20s, tall lean elongated physique — warm ivory skin — body fully covered in Japanese irezumi tattoos from neck to ankle: crimson-gold phoenix rising full body, wings spread across chest, full body coverage from neck to ankle. CENTER-LEFT: Mexican dark goddess, late 20s, lush curvy physique — warm caramel skin — body fully covered in Japanese irezumi tattoos from neck to ankle: chrysanthemum skull across chest, purple-black ink with silver accent, full body coverage from neck to ankle. CENTER-RIGHT: Ghanaian goddess, mid-20s, full plus-size physique — deep rich skin — body fully covered in emerald forest ultra-fine glitter: deep green crystalline glitter coating every inch from neck to ankle, shifting emerald-jade-forest. RIGHT: Swedish editorial model, mid-20s, tall willowy physique — luminous pale skin — body fully covered in silver moonlight ultra-fine glitter: pale cool silver glitter coating every inch from neck to ankle, shifting pearl-white-silver. LEFT: crimson stiletto heels, long gold nails. CENTER-LEFT: black stiletto heels, long purple nails. CENTER-RIGHT: emerald stiletto heels, long emerald nails. RIGHT: silver stiletto heels, long silver nails. All four: full body high-gloss oil.",
        "Kyoto bamboo forest at night, moonlight filtering through dense canopy, silver-blue shadows across mossy ground, paper lanterns glowing amber in distance.",
        "Cool moonlight with warm lantern accent — phoenix feathers blazing crimson left, skull silver catching blue moonlight center-left, emerald glitter absorbing jade forest center-right, silver glitter catching cool moonlight right — life-death-nature quad unified by Kyoto night.",
        "Kyoto life-death quad editorial.",
        "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, kyoto life-death quad grade, portrait 4:5 vertical.",
    ),
    (
        "quad_bae1_wave_peacock_crimson_klimt_versailles", "SS",
        "Four women — irezumi Great Wave / irezumi peacock / crimson glitter / Klimt bodypaint — Versailles",
        "Professional fashion photograph, full body shot. FOUR women standing side by side. LEFT: Korean swimmer, mid-20s, lean streamlined physique — cool fair skin — body fully covered in Japanese irezumi tattoos from neck to ankle: Great Wave motif surging across entire body, deep indigo-black ink with white foam crests, full body coverage. CENTER-LEFT: Thai royal beauty, late 20s, classic hourglass physique — warm golden skin — body fully covered in Japanese irezumi tattoos from neck to ankle: peacock feather spread covering entire body, teal-gold ink with iridescent eye motifs covering entire legs, full body coverage. CENTER-RIGHT: Puerto Rican dancer, late 20s, lush curvy physique — warm caramel skin — body fully covered in crimson-gold ultra-fine glitter: blazing ember glitter coating every inch from neck to ankle, liquid fire effect. RIGHT: Korean art student, early 20s, delicate petite physique — porcelain pale skin — body fully covered in Klimt-style gold leaf bodypaint: Byzantine mosaic patterns coating entire body from neck to ankle, geometric Art Nouveau gold leaf. LEFT: indigo stiletto heels, long indigo nails. CENTER-LEFT: teal stiletto heels, long teal nails. CENTER-RIGHT: red stiletto heels, long crimson nails. RIGHT: gold stiletto heels, long gold nails. All four: full body high-gloss oil.",
        "Hall of Mirrors, Versailles, gilded baroque arches receding to infinity, crystal chandeliers blazing above, warm candlelight flooding marble floors.",
        "Warm golden candlelight — wave indigo catching cool mirror left, peacock teal-gold blazing warm center-left, crimson glitter exploding fire center-right, Klimt gold leaf shimmering Byzantine right — nature-fire-art quad unified by Versailles gold.",
        "Versailles nature-fire-art quad editorial.",
        "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, versailles art quad grade, portrait 4:5 vertical.",
    ),
]

# ── JSON 생성 ──────────────────────────────────────────────────────────
hof_keys = []
ss_keys = []

for key, tier, subject, prompt, environment, lighting, style, quality in QUADS:
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

# ── presets_meta.py 패치 ──────────────────────────────────────────────
META_FILE = "core/presets_meta.py"
with open(META_FILE, encoding="utf-8-sig") as f:
    meta = f.read()

NEW_BLOCK = '''

# ── Bare Art Ensemble: Quad bae1 ──────────────────────────────────────
BARE_ART_QUAD_BAE1 = {
''' + "".join(
    f'    "{k}": {{"name": "{k}", "tier": "{"HOF" if k in hof_keys else "SS"}"}},\n'
    for k, t, *_ in QUADS
) + '''}
'''

if "BARE_ART_QUAD_BAE1" not in meta:
    meta = meta.rstrip() + "\n" + NEW_BLOCK
    print("✅ presets_meta.py BARE_ART_QUAD_BAE1 블록 추가")
else:
    print("⚠️  BARE_ART_QUAD_BAE1 이미 존재 — 스킵")

with open(META_FILE, "w", encoding="utf-8") as f:
    f.write(meta)

# ── hof_tier.py 패치 ──────────────────────────────────────────────────
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
        # } 앞에 삽입
        sss_content = sss_content.rstrip()
        if sss_content.endswith("}"):
            sss_content = sss_content[:-1].rstrip()
            sss_content += f'\n    "{key}",\n' + "}"
        added_ss += 1

with open(SSS_FILE, "w", encoding="utf-8") as f:
    f.write(sss_content)
print(f"✅ sss_tier.py에 {added_ss}종 추가")

# ── 최종 검증 ─────────────────────────────────────────────────────────
ast.parse(open(META_FILE, encoding="utf-8").read())
ast.parse(open(HOF_FILE, encoding="utf-8").read())
ast.parse(open(SSS_FILE, encoding="utf-8").read())
print("\n✅ 전체 AST 검증 통과")
print(f"✅ JSON {len(QUADS)}개 생성")
print(f"✅ HOF {len(hof_keys)}종 / SS {len(ss_keys)}종 등록 완료")
print("\n다음 단계:")
print('git add -A')
print('git commit -m "feat: Bare Art Ensemble quad bae1 (HOF 5종 + SS 8종, JSON 13개)"')
print('git push')
