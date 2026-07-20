import json, os, ast

PRESETS_DIR = "presets"
os.makedirs(PRESETS_DIR, exist_ok=True)

# ============================================================
# 헬퍼 함수
# ============================================================
def save_json(key, data):
    path = os.path.join(PRESETS_DIR, f"{key}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def patch_hof(keys):
    with open("core/hof_tier.py", encoding="utf-8-sig") as f:
        content = f.read()
    added = 0
    for key in keys:
        if f'"{key}"' not in content:
            content = content.rstrip()
            content += f'\n    "{key}",'
            added += 1
    with open("core/hof_tier.py", "w", encoding="utf-8") as f:
        f.write(content)
    return added

def patch_sss(keys):
    with open("core/sss_tier.py", encoding="utf-8-sig") as f:
        content = f.read()
    added = 0
    for key in keys:
        if f'"{key}"' not in content:
            content = content.rstrip()
            if content.endswith("}"):
                content = content[:-1].rstrip()
                content += f'\n    "{key}",\n' + "}"
            else:
                content += f'\n    "{key}",'
            added += 1
    with open("core/sss_tier.py", "w", encoding="utf-8") as f:
        f.write(content)
    return added

# ============================================================
# I. 해골+국화 (SS 1 / HOF 4)
# ============================================================

save_json("irezumi_skull_chrysanthemum_black_glam_void", {
    "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
    "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich ebony skin — body fully covered in Japanese irezumi tattoos: large skull motif across chest surrounded by densely blooming chrysanthemums, tattoos covering entire body from neck to ankle with chrysanthemum petals filling every gap across torso, hips and thighs — jet black afro voluminous and commanding, expression fierce and untouchable. Wearing: tattoos only, black stiletto heels, black long stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight, skull detail catching cold blue rim light, chrysanthemum white petals glowing against deep ebony skin. Style: Vogue Italia black goddess irezumi skull chrysanthemum void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, obsidian skull chrysanthemum grade, portrait 2:3 vertical.",
    "environment": "pure black void",
    "lighting": "dramatic chiaroscuro single spotlight",
    "style": "Vogue Italia black goddess irezumi skull chrysanthemum void editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, obsidian skull chrysanthemum grade, portrait 2:3 vertical"
})

save_json("irezumi_skull_chrysanthemum_vs_angel_aurora", {
    "subject": "Scandinavian VS Angel, mid-20s, VS Angel athletic physique",
    "prompt": "Professional fashion photograph, full body shot. Model: Scandinavian VS Angel, mid-20s, VS Angel athletic physique — long lean muscular legs, tight athletic torso, luminous pale porcelain skin — body fully covered in Japanese irezumi tattoos: dramatic skull motif centered on chest with deep black ink, densely blooming chrysanthemums in crimson and gold surrounding skull and covering entire body from neck to ankle — platinum blonde hair windswept, expression cold and ethereal. Wearing: tattoos only, barefoot on glacial ice, crimson long stiletto nails. Environment: Iceland glacier at night, Aurora Borealis dancing overhead in violet and green curtains, glacial blue ice underfoot. Lighting: aurora borealis violet and green curtain washing over pale inked figure, skull catching cold aurora light, chrysanthemum crimson blazing warm against cool aurora. Style: Iceland aurora VS Angel irezumi skull chrysanthemum editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora skull chrysanthemum grade, portrait 2:3 vertical.",
    "environment": "Iceland glacier at night, Aurora Borealis",
    "lighting": "aurora borealis violet and green curtain",
    "style": "Iceland aurora VS Angel irezumi skull chrysanthemum editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora skull chrysanthemum grade, portrait 2:3 vertical"
})

save_json("irezumi_skull_chrysanthemum_hot_glam_versailles", {
    "subject": "Brazilian Latina goddess, late 20s, extreme hourglass physique",
    "prompt": "Professional fashion photograph, full body shot. Model: Brazilian Latina goddess, late 20s, extreme hourglass physique — explosively wide dramatic hips, impossibly tiny waist, thick powerful thighs, warm golden bronze skin — body fully covered in Japanese irezumi tattoos: large dramatic skull centered on chest surrounded by densely blooming chrysanthemums in crimson and gold, tattoos covering entire body from neck to ankle with chrysanthemum petals filling every gap across explosive hips and powerful thighs — long dark wavy hair swept back dramatically, expression Latin fire and confidence. Wearing: tattoos only, gold stiletto heels, deep crimson long stiletto nails. Environment: Hall of Mirrors Versailles, gilded baroque grandeur, chandeliers blazing above, golden marble floor. Lighting: warm golden candlelight flooding baroque hall, skull detail catching amber glow, chrysanthemum crimson and gold blazing warm in Versailles light. Style: Versailles hot glamour irezumi skull chrysanthemum editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Versailles skull chrysanthemum grade, portrait 2:3 vertical.",
    "environment": "Hall of Mirrors Versailles",
    "lighting": "warm golden candlelight flooding baroque hall",
    "style": "Versailles hot glamour irezumi skull chrysanthemum editorial",
    "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Versailles skull chrysanthemum grade, portrait 2:3 vertical"
})

save_json("irezumi_skull_chrysanthemum_sports_glam_void", {
    "subject": "Korean sports goddess, mid-20s, Korean athletic physique",
    "prompt": "Professional fashion photograph, full body shot. Model: Korean sports goddess, mid-20s, Korean athletic physique — powerfully defined muscles, compact tight frame, cool porcelain skin — body fully covered in Japanese irezumi tattoos: fierce skull motif with black ink across chest, densely blooming chrysanthemums in electric purple and white covering entire body from neck to ankle following every defined muscle contour — straight black hair slicked back, expression intense and focused. Wearing: tattoos only, black stiletto heels, electric purple long stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: harsh strobe spotlight, skull catching cold white light, chrysanthemum electric purple glowing against cool porcelain skin in void darkness. Style: Vogue Italia sports goddess irezumi skull chrysanthemum void editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, obsidian skull chrysanthemum sports grade, portrait 2:3 vertical.",
    "environment": "pure black void",
    "lighting": "harsh strobe spotlight",
    "style": "Vogue Italia sports goddess irezumi skull chrysanthemum void editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, obsidian skull chrysanthemum sports grade, portrait 2:3 vertical"
})

save_json("irezumi_skull_chrysanthemum_slim_runway_monaco", {
    "subject": "French European runway model, early 20s, high fashion slim physique",
    "prompt": "Professional fashion photograph, full body shot. Model: French European runway model, early 20s, high fashion slim physique — impossibly long legs, flat torso, angular sharp features, luminous fair skin — body fully covered in Japanese irezumi tattoos: razor-sharp skull with fine black ink centered on chest, densely blooming chrysanthemums in pale gold and silver covering entire body from neck to ankle along endless slim legs and sharp hip bones — platinum hair severe and straight, expression cold high-fashion disdain. Wearing: tattoos only, silver stiletto heels, silver long stiletto nails. Environment: Monaco rooftop terrace at night, Mediterranean harbor below, luxury yachts glittering. Lighting: Monaco cool blue night light, skull silver detail shimmering, chrysanthemum pale gold catching cool harbor light. Style: Balenciaga avant-garde runway irezumi skull chrysanthemum editorial. Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, Monaco skull chrysanthemum grade, portrait 2:3 vertical.",
    "environment": "Monaco rooftop terrace at night",
    "lighting": "Monaco cool blue night light",
    "style": "Balenciaga avant-garde runway irezumi skull chrysanthemum editorial",
    "quality": "Shot on Leica SL2 90mm f/2.0 APO, 8K UHD, Monaco skull chrysanthemum grade, portrait 2:3 vertical"
})

# ============================================================
# J. 잉어+단풍 (SS 3 / HOF 3)
# ============================================================

save_json("irezumi_koi_maple_black_glam_void", {
    "subject": "Black African goddess, mid-20s, Black glamour hourglass physique",
    "prompt": "Professional fashion photograph, full body shot. Model: Black African goddess, mid-20s, Black glamour hourglass physique — impossibly wide round hips, ultra-narrow waist, powerfully thick thighs, deep luminous rich ebony skin — body fully covered in Japanese irezumi tattoos: massive golden koi swimming upward from ankles to shoulders with scales in vivid gold and orange, red and crimson maple leaves scattering across entire body filling every gap between koi fins and scales — jet black afro voluminous and commanding, expression fierce and untouchable. Wearing: tattoos only, black stiletto heels, crimson long stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: dramatic chiaroscuro single spotlight, koi gold scales blazing warm against deep ebony skin, maple crimson leaves glowing rich in void darkness. Style: Vogue Italia black goddess irezumi koi maple void editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, obsidian koi maple grade, portrait 2:3 vertical.",
    "environment": "pure black void",
    "lighting": "dramatic chiaroscuro single spotlight",
    "style": "Vogue Italia black goddess irezumi koi maple void editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, obsidian koi maple grade, portrait 2:3 vertical"
})

save_json("irezumi_koi_maple_vs_angel_aurora", {
    "subject": "Scandinavian VS Angel, mid-20s, VS Angel athletic physique",
    "prompt": "Professional fashion photograph, full body shot. Model: Scandinavian VS Angel, mid-20s, VS Angel athletic physique — long lean muscular legs, tight athletic torso, luminous pale porcelain skin — body fully covered in Japanese irezumi tattoos: elegant silver koi ascending from ankles to shoulders with iridescent scales, golden and crimson maple leaves cascading across chest and hips in autumnal density — platinum blonde hair windswept, expression cold and ethereal. Wearing: tattoos only, barefoot on glacial ice, gold long stiletto nails. Environment: Iceland glacier at night, Aurora Borealis dancing overhead in violet and green curtains, glacial blue ice underfoot. Lighting: aurora borealis violet and green washing over pale inked figure, koi silver scales catching aurora shimmer, maple gold and crimson blazing warm against cool aurora light. Style: Iceland aurora VS Angel irezumi koi maple editorial. Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora koi maple grade, portrait 2:3 vertical.",
    "environment": "Iceland glacier at night, Aurora Borealis",
    "lighting": "aurora borealis violet and green washing",
    "style": "Iceland aurora VS Angel irezumi koi maple editorial",
    "quality": "Shot on Phase One XF IQ4 110mm f/2.8, 8K UHD, aurora koi maple grade, portrait 2:3 vertical"
})

save_json("irezumi_koi_maple_hot_glam_versailles", {
    "subject": "Brazilian Latina goddess, late 20s, extreme hourglass physique",
    "prompt": "Professional fashion photograph, full body shot. Model: Brazilian Latina goddess, late 20s, extreme hourglass physique — explosively wide dramatic hips, impossibly tiny waist, thick powerful thighs, warm golden bronze skin — body fully covered in Japanese irezumi tattoos: vibrant crimson and gold koi surging from ankles to neck with vivid scale detail, dense red and gold maple leaves covering explosive hips and full torso in autumnal glory — long dark wavy hair swept back dramatically, expression Latin fire and confidence. Wearing: tattoos only, gold stiletto heels, crimson long stiletto nails. Environment: Hall of Mirrors Versailles, gilded baroque grandeur, chandeliers blazing above, golden marble floor. Lighting: warm golden candlelight flooding baroque hall, koi crimson and gold scales blazing in amber light, maple leaves catching warm Versailles glow. Style: Versailles hot glamour irezumi koi maple editorial. Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Versailles koi maple grade, portrait 2:3 vertical.",
    "environment": "Hall of Mirrors Versailles",
    "lighting": "warm golden candlelight flooding baroque hall",
    "style": "Versailles hot glamour irezumi koi maple editorial",
    "quality": "Shot on Canon EOS R5 85mm f/1.2, 8K UHD, Versailles koi maple grade, portrait 2:3 vertical"
})

save_json("irezumi_koi_maple_sports_glam_void", {
    "subject": "Korean sports goddess, mid-20s, Korean athletic physique",
    "prompt": "Professional fashion photograph, full body shot. Model: Korean sports goddess, mid-20s, Korean athletic physique — powerfully defined muscles, compact tight frame, cool porcelain skin — body fully covered in Japanese irezumi tattoos: black and indigo koi surging powerfully from ankles to shoulders with bold scale detail, deep crimson and burnt orange maple leaves covering entire body following every defined muscle contour — straight black hair slicked back, expression intense and focused. Wearing: tattoos only, black stiletto heels, deep crimson long stiletto nails. Environment: pure black void, seamless obsidian backdrop, infinite darkness. Lighting: harsh strobe spotlight, koi indigo scales catching cold light, maple crimson leaves glowing deep against cool porcelain skin in void darkness. Style: Vogue Italia sports goddess irezumi koi maple void editorial. Shot on Sony A1 85mm f/1.4 GM, 8K UHD, obsidian koi maple sports grade, portrait 2:3 vertical.",
    "environment": "pure black void",
    "lighting": "harsh strobe spotlight",
    "style": "Vogue Italia sports goddess irezumi koi maple void editorial",
    "quality": "Shot on Sony A1 85mm f/1.4 GM, 8K UHD, obsidian koi maple sports grade, portrait 2:3 vertical"
})

save_json("irezumi_koi_maple_ballerina_kyoto", {
    "subject": "Japanese ballerina, early 20s, ballerina physique",
    "prompt": "Professional fashion photograph, full body shot. Model: Japanese ballerina, early 20s, ballerina physique — impossibly slender elongated figure, exquisitely defined muscle tone, pale porcelain skin — body fully covered in Japanese irezumi tattoos: graceful red and gold koi ascending from pointe shoe ribbons to collarbone in masterful flowing detail, brilliant crimson and orange maple leaves drifting across slender torso and delicate arms like falling autumn rain — black hair pinned in tight ballet bun, expression ethereal and transcendent. Wearing: tattoos only, crimson satin pointe shoes, crimson long stiletto nails. Environment: Kyoto bamboo forest at dawn, morning mist filtering through green canopy, ancient stone path, soft jade light. Lighting: soft dawn light filtering through bamboo, koi red and gold catching warm jade morning light, maple crimson luminous in misty autumn atmosphere. Style: Kyoto dawn ballerina irezumi koi maple editorial. Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Kyoto koi maple grade, portrait 2:3 vertical.",
    "environment": "Kyoto bamboo forest at dawn",
    "lighting": "soft dawn light filtering through bamboo",
    "style": "Kyoto dawn ballerina irezumi koi maple editorial",
    "quality": "Shot on Hasselblad H6D 80mm f/2.8, 8K UHD, Kyoto koi maple grade, portrait 2:3 vertical"
})

print("I/J 이레즈미 10종 JSON 생성 완료")
