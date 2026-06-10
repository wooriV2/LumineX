"""
LumineX - 신규 프리셋 추가 스크립트 (v3.4 추가분)
실행: python add_new_presets.py
최근 성공 케이스 + 누적 데이터 기반
"""

import json
import os

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "presets")
os.makedirs(PRESETS_DIR, exist_ok=True)

NEW_PRESETS_V34 = {

    # ── 아트 스타일 계열 (필터 완화 효과 확인됨) ────────────────
    "pop_art_glamour": {
        "tag": "Pop Art Glamour",
        "subject": "a stunning glamorous female model",
        "body": "ultra-slim high fashion figure, elongated silhouette, fashion week physique",
        "outfit": "designer string bikini, minimalist swimwear, Sports Illustrated editorial style",
        "material": "liquid metallic fabric, mirror-finish surface",
        "environment": "pure white minimalist studio, seamless backdrop",
        "lighting": "professional studio strobe, high-contrast glamour lighting",
        "style": "pop art style, Andy Warhol inspired, bold graphic colors, Harper's Bazaar editorial",
        "quality": "shot on Hasselblad H6D, purple moody color grade, violet atmospheric tones, portrait 2:3 vertical"
    },
    "watercolor_goddess": {
        "tag": "Watercolor Goddess",
        "subject": "a stunning power fitness female model",
        "body": "bikini competition physique, extremely defined muscles, round athletic hips",
        "outfit": "crystal embellished bikini, luxury swimwear editorial",
        "material": "crystal embellished couture fabric, sequined surface",
        "environment": "Mediterranean seaside village, white-washed buildings, blue sea",
        "lighting": "firelight, warm flickering flames, dramatic orange glow",
        "style": "watercolor painting style, soft translucent washes, cyberpunk cinematic fashion",
        "quality": "shot on Nikon Z9, warm golden film grade, vintage golden hour tone, portrait 2:3 vertical"
    },
    "renaissance_fantasy": {
        "tag": "Renaissance Fantasy",
        "subject": "a slender elegant female model",
        "body": "slender elegant model, slim narrow frame, graceful delicate figure",
        "outfit": "bandeau crop top, high-fashion skirt, editorial silhouette",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "tropical forest waterfall paradise, lush jungle, cascading water",
        "lighting": "moonlight, silvery blue natural light, mysterious outdoor glow",
        "style": "Renaissance painting tableau, classical masterpiece composition, Valentino red carpet luxury",
        "quality": "shot on Phase One XF IQ4, purple moody color grade, galaxy and stars background, portrait 2:3 vertical"
    },

    # ── 더블 익스포저 계열 (Gemini 특화) ───────────────────────
    "double_exposure_dark": {
        "tag": "Double Exposure Dark",
        "subject": "a mysterious exotic female model",
        "body": "glamorous figure, powerful presence, expressive features",
        "outfit": "minimal draped fabric, body art emphasis",
        "material": "tribal body paint, natural earth tones",
        "environment": "dramatic desert landscape, stormy sky, rain",
        "lighting": "golden hour backlight, silhouette definition, halo effect",
        "style": "double exposure photography, artistic silhouette overlay, fine art editorial",
        "quality": "shot on Canon EOS R5, cinematic teal and orange color grade, portrait 2:3 vertical"
    },
    "double_exposure_ethereal": {
        "tag": "Double Exposure Ethereal",
        "subject": "a ethereal mysterious female model",
        "body": "slender elegant figure, graceful posture",
        "outfit": "flowing minimal white dress, ethereal movement",
        "material": "lightweight chiffon, flowing airy drape",
        "environment": "misty forest, cascading waterfall, aurora borealis",
        "lighting": "moonlight, silvery blue natural light, mystical outdoor glow",
        "style": "double exposure photography, artistic silhouette overlay, fine art editorial, Nick Knight inspired",
        "quality": "shot on Hasselblad H6D, cool blue color grade, cold steel tones, portrait 2:3 vertical"
    },

    # ── 스포티 글램 계열 (새로 추가) ───────────────────────────
    "golf_glam": {
        "tag": "Golf Glam",
        "subject": "a stunning sporty glamorous female model",
        "body": "slim toned model, lean athletic build, flat stomach, slim toned silhouette",
        "outfit": "golf tennis pleated mini skirt, sporty chic editorial, athletic fashion, structured crop top",
        "material": "luxury stretch fabric, elegant fitted silhouette",
        "environment": "country club golf course, manicured green lawn, preppy glamour",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "luxury sports editorial, high-end athletic fashion, Chanel sport glamour",
        "quality": "shot on Canon EOS R5, high key bright white tone, overexposed glamour, portrait 2:3 vertical"
    },
    "tennis_luxe": {
        "tag": "Tennis Luxe",
        "subject": "a stunning athletic glamorous female model",
        "body": "slim fitness model, lean defined muscles, flat abs, athletic slim silhouette",
        "outfit": "tennis court editorial, pleated mini skirt, structured sports top, athletic chic",
        "material": "luxury performance fabric, tailored silhouette",
        "environment": "classic tennis club, clean white court, preppy glamour",
        "lighting": "soft beauty dish light, even flattering illumination",
        "style": "sports luxury editorial, Stella McCartney athletic glamour",
        "quality": "shot on Sony A7R V, high key bright white tone, clean light, portrait 2:3 vertical"
    },
    "biker_glam": {
        "tag": "Biker Glam",
        "subject": "a fierce glamorous Latina female model",
        "body": "plus-size glamour model, soft belly, wide full hips, thick thighs, confident couture presence",
        "outfit": "high-cut one-piece swimsuit, bold cutouts, athletic glamour, denim fabric",
        "material": "denim fabric, casual glamour styling",
        "environment": "dramatic volcanic cliff, stormy ocean, powerful nature",
        "lighting": "multi-colored neon edge glow, cyberpunk light",
        "style": "luxury sports editorial, high-end biker fashion",
        "quality": "shot on Canon EOS R5, vintage film grain, faded colors, analog photography look, portrait 2:3 vertical"
    },

    # ── 럭셔리 욕조/스파 계열 ───────────────────────────────────
    "spa_noir": {
        "tag": "Spa Noir",
        "subject": "a mature glamorous female model",
        "body": "slim toned model, lean athletic build, gracefully aged beauty, senior glamour",
        "outfit": "halter neck dress, open back, summer glamour editorial, spa luxury",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "luxury hotel suite, penthouse bedroom, floor-to-ceiling windows",
        "lighting": "underwater pool light reflection, rippling aqua light patterns",
        "style": "Harper's Bazaar sensual fashion editorial, cinematic spa glamour",
        "quality": "shot on Sony A7R V, cinematic teal and orange color grade, Hollywood film look, portrait 2:3 vertical"
    },

    # ── 신화/컨셉 계열 ──────────────────────────────────────────
    "medusa_queen": {
        "tag": "Medusa Queen",
        "subject": "a powerful African goddess female model",
        "body": "super plus-size runway model, dramatic full-figure silhouette, maximalist curvy fashion",
        "outfit": "bohemian tiered skirt, layered flowing fabric, free-spirited summer style",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "dramatic volcanic cliff, stormy ocean, powerful nature",
        "lighting": "firelight, warm flickering flames, dramatic orange glow",
        "style": "Medusa Greek mythology concept, Gucci eclectic maximalism, bold prints",
        "quality": "shot on Canon EOS R5, high key bright white tone, overexposed glamour, portrait 2:3 vertical"
    },
    "valkyrie_storm": {
        "tag": "Valkyrie Storm",
        "subject": "a powerful Nordic warrior female model",
        "body": "power fitness model, very muscular defined body, strong arms and legs",
        "outfit": "warrior goddess armor-inspired couture, glamorous battle-ready editorial",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Iceland glacier, northern lights aurora borealis, mystical arctic landscape",
        "lighting": "lightning strike background, electric energy, storm effects",
        "style": "Alexander McQueen dramatic fashion editorial, Valkyrie Norse mythology",
        "quality": "shot on Nikon Z9, dark moody color grade, deep shadows, dramatic contrast, portrait 2:3 vertical"
    },
    "nine_tails": {
        "tag": "Nine Tails",
        "subject": "a mysterious enchanting Korean female model",
        "body": "soft glamour model, feminine gentle curves, round soft hips, elegant graceful figure",
        "outfit": "traditional meets modern fusion dress, flowing ethereal layers",
        "material": "lightweight chiffon fabric, flowing airy drape, soft feminine movement",
        "environment": "Tokyo Shinto shrine, traditional Japanese architecture, modern city contrast",
        "lighting": "moonlight, silvery blue natural light, mysterious outdoor glow",
        "style": "nine-tailed fox spirit concept, Korean mythology, Harper's Bazaar sensual editorial",
        "quality": "shot on Fujifilm GFX 100S, soft pink glamour grade, rose gold tones, portrait 2:3 vertical"
    },

    # ── 사이버펑크 + 드라마틱 ────────────────────────────────────
    "cyber_fire": {
        "tag": "Cyber Fire",
        "subject": "a fierce African goddess female model",
        "body": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",
        "outfit": "off-shoulder bodycon dress, bardot neckline, elegant shoulder reveal",
        "material": "latex second-skin styled as satin performance fabric, sleek couture finish",
        "environment": "futuristic sci-fi corridor, spaceship interior, glowing panels",
        "lighting": "surrounded by flames and fire, dramatic fire effects, moonlight silvery blue",
        "style": "Harper's Bazaar sensual fashion editorial, cyberpunk cinematic",
        "quality": "shot on Fujifilm GFX 100S, dark moody color grade, deep shadows, dramatic contrast, portrait 2:3 vertical"
    },
    "neon_rain_goddess": {
        "tag": "Neon Rain Goddess",
        "subject": "a powerful BBW glamour female model",
        "body": "BBW glamour model, extremely curvy fashion silhouette, broad hips, luxurious BBW presence",
        "outfit": "corset mini dress, cinched waist, dramatic silhouette",
        "material": "wet-look spandex, glossy performance fabric",
        "environment": "rain-soaked urban street, wet pavement reflections, city lights",
        "lighting": "multi-colored neon edge glow, cyberpunk light, wet reflections",
        "style": "Vogue Italia high-fashion editorial, cyberpunk neon glamour",
        "quality": "shot on Sony A7R V, purple moody color grade, violet atmospheric tones, portrait 2:3 vertical"
    },

    # ── 시즌/여름 ────────────────────────────────────────────────
    "tropical_storm": {
        "tag": "Tropical Storm",
        "subject": "a glamorous curvy Moroccan female model",
        "body": "glamour curvy model, dramatic waist-to-hip ratio, very wide round hips",
        "outfit": "cutout mini dress, strategic skin-baring cutouts, bold editorial design",
        "material": "tropical print fabric, exotic botanical pattern, vacation glamour",
        "environment": "pure white minimalist studio, seamless backdrop",
        "lighting": "volumetric fog cinematic light, atmospheric mood",
        "style": "Chanel classic luxury elegance, tropical summer editorial",
        "quality": "shot on Canon EOS R5, photorealistic, RAW photo, portrait 2:3 vertical"
    },
    "santorini_lightning": {
        "tag": "Santorini Lightning",
        "subject": "a elegant Scandinavian female model",
        "body": "slender elegant model, slim narrow frame, graceful delicate figure, tall elegant Nordic features",
        "outfit": "wrap dress, tied waist, elegant flowing summer editorial",
        "material": "lightweight chiffon fabric, flowing airy drape, soft feminine movement",
        "environment": "Santorini cliff, blue dome church, Aegean sea at night",
        "lighting": "lightning strike background, electric energy, storm effects",
        "style": "Prada intellectual minimalist luxury, avant-garde editorial",
        "quality": "shot on iPhone cinematic mode, photorealistic, hyperrealistic skin texture, portrait 2:3 vertical"
    },
}


def main():
    print("\n  ✦ LumineX v3.4 신규 프리셋 추가 시작...\n")
    created = 0
    skipped = 0

    for name, data in NEW_PRESETS_V34.items():
        path = os.path.join(PRESETS_DIR, f"{name}.json")
        if os.path.exists(path):
            print(f"  ⏭️  건너뜀 (이미 존재): {name}.json")
            skipped += 1
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  ✅ 생성: {name}.json")
            created += 1

    print(f"\n  완료: 생성 {created}개 / 건너뜀 {skipped}개")
    total = len([f for f in os.listdir(PRESETS_DIR) if f.endswith('.json')])
    print(f"  총 프리셋: {total}개\n")

    print("  📋 추가된 카테고리:")
    print("  - 아트 스타일 계열 (팝아트/수채화/르네상스) × 3")
    print("  - 더블 익스포저 계열 (Gemini 특화)  × 2")
    print("  - 스포티 글램 (골프/테니스/바이크)   × 3")
    print("  - 럭셔리 스파/욕조                   × 1")
    print("  - 신화/컨셉 (메두사/발키리/구미호)   × 3")
    print("  - 사이버펑크+드라마틱                × 2")
    print("  - 시즌/여름                          × 2")
    print(f"  총 16개 신규 프리셋\n")


if __name__ == "__main__":
    main()
    