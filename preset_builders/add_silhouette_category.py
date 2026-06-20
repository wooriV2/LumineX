"""
LumineX 실루엣 카테고리 추가 패치 스크립트
- 새 카테고리 "🌑 실루엣 & 섀도우" 30종 추가
- dashboard.py PRESET_CATEGORIES에 추가
- presets/ 폴더에 JSON 파일 30개 복사
실행: python add_silhouette_category.py
"""

import os
import json
import shutil
from pathlib import Path

# ── 경로 설정 ──────────────────────────────────────────────
BASE_DIR = Path("C:/Dev/LumineX")
PRESETS_DIR = BASE_DIR / "presets"
DASHBOARD = BASE_DIR / "dashboard.py"
SCRIPT_DIR = Path(__file__).parent / "silhouette_presets"

# ── 프리셋 데이터 ──────────────────────────────────────────
SILHOUETTE_PRESETS = {
    "silhouette_spotlight_smoke": {
        "subject": "a woman standing center stage",
        "body": "curvaceous silhouette, full body",
        "outfit": "form-fitting bodysuit, details hidden in shadow",
        "environment": "dark stage, single spotlight from directly above, smoke machine fog swirling around feet",
        "lighting": "single harsh spotlight, dramatic chiaroscuro, deep shadows, rim light outlining body curves",
        "style": "cinematic noir, high contrast black and white, theatrical",
        "quality": "ultra-sharp, photorealistic, 8K, professional photography",
        "pose": "standing tall, facing away, head slightly turned",
        "special": "smoke wisps catching spotlight, silhouette only, body outline visible"
    },
    "silhouette_spotlight_latex": {
        "subject": "a woman in latex",
        "body": "tall, curvaceous silhouette",
        "outfit": "latex catsuit, glossy surface catching spotlight",
        "environment": "pitch black studio, single overhead spotlight",
        "lighting": "single spotlight from above, latex surface reflecting light, deep shadow everywhere else",
        "style": "cinematic, high contrast, fashion editorial",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "powerful stance, hands on hips",
        "special": "latex shine visible even in silhouette, dramatic body outline"
    },
    "silhouette_spotlight_heels": {
        "subject": "a woman in stiletto heels",
        "body": "long legs, curvaceous figure silhouette",
        "outfit": "minimal, high heels clearly visible",
        "environment": "dark empty stage, single spotlight from above",
        "lighting": "dramatic spotlight, rim lighting on leg curves, heels catching light",
        "style": "cinematic noir, fashion photography, high contrast",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "side profile, one leg forward, confident strut",
        "special": "stiletto heels glinting in spotlight, long leg lines emphasized"
    },
    "silhouette_spotlight_hair": {
        "subject": "a woman with long flowing hair",
        "body": "full body silhouette",
        "outfit": "flowing dress or minimal, hair is the focus",
        "environment": "dark studio, single spotlight, wind machine",
        "lighting": "spotlight from above, hair strands catching light, halo effect",
        "style": "cinematic, editorial, dramatic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "head thrown back, hair flowing dramatically",
        "special": "hair backlit creating luminous halo, individual strands visible against dark"
    },
    "silhouette_spotlight_dance": {
        "subject": "a dancing woman",
        "body": "athletic, curvaceous silhouette in motion",
        "outfit": "minimal dance outfit, movement suggested",
        "environment": "dark stage, single spotlight",
        "lighting": "spotlight catching motion blur, dynamic shadow",
        "style": "cinematic, performance art, high contrast",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "mid-dance pose, leg raised, arms extended, dynamic movement",
        "special": "motion captured in silhouette, elegant dance lines"
    },
    "silhouette_spotlight_chair": {
        "subject": "a woman seated in a chair",
        "body": "silhouette, legs crossed elegantly",
        "outfit": "suggested by silhouette shape only",
        "environment": "dark studio, single chair, overhead spotlight",
        "lighting": "spotlight from above, chair casting dramatic shadow",
        "style": "film noir, boudoir photography, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "seated, legs crossed, one arm resting on chair back, head tilted",
        "special": "chair and figure as unified silhouette composition"
    },
    "silhouette_spotlight_back": {
        "subject": "a woman from behind",
        "body": "back view silhouette, spine and curve lines",
        "outfit": "backless dress or minimal, back fully visible",
        "environment": "dark studio, spotlight from above and slightly behind",
        "lighting": "rim lighting on shoulder blades, spine highlighted, deep shadow in front",
        "style": "cinematic, editorial, sensual noir",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing, facing away from camera, slight head turn",
        "special": "spine line and shoulder curve highlighted by rim light"
    },
    "silhouette_spotlight_pole": {
        "subject": "a woman on a vertical pole",
        "body": "athletic silhouette, extended limbs",
        "outfit": "minimal, suggested by silhouette",
        "environment": "dark stage, vertical pole, single spotlight",
        "lighting": "spotlight on pole and figure, dramatic shadow on floor",
        "style": "performance art, cinematic, high contrast",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "wrapped around pole, one leg extended, artistic pose",
        "special": "pole catching spotlight vertically, figure as artistic composition"
    },
    "silhouette_window_city": {
        "subject": "a woman standing at a floor-to-ceiling window",
        "body": "full body silhouette against city lights",
        "outfit": "sheer robe or dress, translucent against backlight",
        "environment": "luxury high-rise hotel room, panoramic city view at night, bokeh city lights",
        "lighting": "city lights as backlight, figure in complete silhouette, warm room light from sides",
        "style": "cinematic, luxury noir, architectural photography",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing facing window, one hand touching glass",
        "special": "city lights bokeh through window, sheer fabric catching backlight"
    },
    "silhouette_window_rain": {
        "subject": "a woman by a rain-streaked window",
        "body": "full body silhouette",
        "outfit": "minimal, suggested by silhouette",
        "environment": "dark room, large window with rain streaming down, gray city outside",
        "lighting": "diffused rainy daylight as backlight, figure in deep silhouette, rain streaks catching light",
        "style": "film noir, black and white, melancholic cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing side profile, forehead resting on window glass",
        "special": "rain droplets on glass catching light, moody atmosphere"
    },
    "silhouette_window_sheer": {
        "subject": "a woman behind sheer curtains",
        "body": "soft silhouette through translucent fabric",
        "outfit": "implied through curtain diffusion",
        "environment": "bright window, white sheer curtains billowing in breeze",
        "lighting": "strong daylight through curtains, figure as soft shadow behind fabric",
        "style": "dreamy, soft focus, boudoir editorial",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "arms slightly raised, curtain wrapping around figure",
        "special": "curtain fabric diffusing and softening silhouette, ethereal quality"
    },
    "silhouette_doorway_light": {
        "subject": "a woman standing in a doorway",
        "body": "full body silhouette framed by doorway",
        "outfit": "form suggested by strong backlight",
        "environment": "dark hallway, bright light source behind open doorway",
        "lighting": "extreme backlight from doorway, figure completely silhouetted, light halo around edges",
        "style": "cinematic, noir, dramatic architectural",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing in doorway, one hand on door frame",
        "special": "doorway framing silhouette perfectly, light spilling onto dark floor"
    },
    "silhouette_window_sunset": {
        "subject": "a woman silhouetted against sunset",
        "body": "full body silhouette, warm orange glow outline",
        "outfit": "dress with flowing hem catching orange light",
        "environment": "large window, dramatic orange and red sunset sky",
        "lighting": "intense sunset backlight, orange rim light on hair and shoulders, warm color cast",
        "style": "cinematic, golden hour, dramatic editorial",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing facing window, arms slightly open",
        "special": "orange sunset glow rimming entire silhouette, warm color gradient"
    },
    "silhouette_window_neon": {
        "subject": "a woman by a neon-lit window",
        "body": "silhouette with colored neon rim lighting",
        "outfit": "suggested by neon color on edges",
        "environment": "dark room, window overlooking neon sign street",
        "lighting": "neon sign colors casting pink and blue rim light on figure, deep shadow interior",
        "style": "cyberpunk noir, neon editorial, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "leaning against window frame, profile view",
        "special": "neon colors splitting on figure edges, pink and blue dual rim light"
    },
    "silhouette_neon_pink": {
        "subject": "a woman in pink neon light",
        "body": "curvaceous silhouette with pink neon outline",
        "outfit": "form-fitting, edges glowing pink",
        "environment": "dark smoky club interior, pink neon sign background",
        "lighting": "pink neon as sole light source, smoke catching pink light, deep shadow",
        "style": "cyberpunk, neon noir, editorial",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "confident stance, hip cocked",
        "special": "pink neon smoke haze, monochromatic pink glow on silhouette edges"
    },
    "silhouette_neon_blue": {
        "subject": "a woman in blue neon rain",
        "body": "silhouette with blue neon and rain",
        "outfit": "wet surface catching blue light",
        "environment": "rainy alley, blue neon reflections on wet pavement",
        "lighting": "blue neon from above, rain catching light, reflections on wet ground",
        "style": "cyberpunk noir, rain editorial, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing in rain, looking up slightly",
        "special": "blue neon reflected in rain puddles, wet silhouette against neon"
    },
    "silhouette_neon_red": {
        "subject": "a woman in red neon alley",
        "body": "dramatic silhouette with red rim light",
        "outfit": "dark outfit, red neon outlining edges",
        "environment": "dark back alley, single red neon sign",
        "lighting": "red neon as sole light, deep shadow, danger aesthetic",
        "style": "film noir, danger aesthetic, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "leaning against wall, arms crossed",
        "special": "red neon casting dangerous glow, noir shadow play"
    },
    "silhouette_neon_purple": {
        "subject": "a woman in purple neon club",
        "body": "silhouette with purple and violet rim light",
        "outfit": "suggested by purple neon edges",
        "environment": "dark nightclub, purple neon lighting, smoke machine",
        "lighting": "purple and violet neon, smoke catching light, strobing effect frozen",
        "style": "club editorial, cyberpunk, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "dancing pose, arms raised",
        "special": "purple smoke haze, violet rim light on hair and shoulders"
    },
    "silhouette_neon_multicolor": {
        "subject": "a woman in cyberpunk neon city",
        "body": "silhouette with multicolor neon rim lighting",
        "outfit": "dark, edges lit by multiple neon colors",
        "environment": "cyberpunk street, multiple neon signs in pink blue green yellow",
        "lighting": "multiple neon colors splitting across silhouette, pink left blue right",
        "style": "cyberpunk, neon editorial, blade runner aesthetic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "powerful stance, facing camera",
        "special": "multicolor neon splitting across figure, cyberpunk atmosphere"
    },
    "silhouette_sunset_beach": {
        "subject": "a woman on the beach at sunset",
        "body": "full body silhouette against sunset sky",
        "outfit": "bikini or dress suggested by silhouette",
        "environment": "beach, ocean horizon, dramatic orange red sunset sky",
        "lighting": "sunset backlight, orange and gold rim on hair and shoulders, reflection on wet sand",
        "style": "golden hour editorial, cinematic, travel photography",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing at water's edge, arms slightly raised",
        "special": "wet sand reflecting sunset, ocean waves catching golden light"
    },
    "silhouette_sunset_cliff": {
        "subject": "a woman on a cliff edge at sunset",
        "body": "dramatic silhouette against sky",
        "outfit": "flowing dress catching wind",
        "environment": "dramatic cliff edge, vast sky, sunset clouds in orange and purple",
        "lighting": "sunset as backlight, dress hem and hair catching warm light",
        "style": "cinematic, epic editorial, landscape photography",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing at cliff edge, dress and hair blowing in wind",
        "special": "vast sky as backdrop, dress silhouette flowing dramatically"
    },
    "silhouette_moonlight": {
        "subject": "a woman in moonlight",
        "body": "silhouette with silver moonlight rim",
        "outfit": "flowing night dress suggested by moonlight edges",
        "environment": "outdoor night, full moon, minimal light, stars",
        "lighting": "full moon as backlight, silver blue rim light, deep night shadows",
        "style": "gothic romantic, moonlit editorial, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "arms slightly raised, looking up at moon",
        "special": "moonbeam catching hair and dress edges, ethereal silver glow"
    },
    "silhouette_aurora": {
        "subject": "a woman under aurora borealis",
        "body": "silhouette with aurora color rim lighting",
        "outfit": "suggested by green and purple aurora light on edges",
        "environment": "arctic landscape, snow, dramatic aurora borealis filling sky",
        "lighting": "aurora as backlight, green and purple light on silhouette edges, snow reflecting aurora",
        "style": "ethereal, arctic editorial, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "looking up at aurora, arms slightly open",
        "special": "aurora colors splitting green purple on silhouette edges, snow sparkle"
    },
    "silhouette_pool_underwater": {
        "subject": "a woman seen from underwater",
        "body": "silhouette from below water surface",
        "outfit": "bikini suggested by underwater silhouette",
        "environment": "swimming pool, underwater perspective looking up, sunlight through water",
        "lighting": "sunlight filtering through water surface, caustic light patterns, figure silhouetted from below",
        "style": "underwater photography, cinematic, ethereal",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "floating or swimming at surface, limbs extended",
        "special": "caustic light patterns on silhouette, water surface ripple effects"
    },
    "silhouette_pool_edge": {
        "subject": "a woman at infinity pool edge at night",
        "body": "silhouette reflected in pool water",
        "outfit": "swimwear suggested by reflection and silhouette",
        "environment": "infinity pool at night, city lights beyond, pool water reflection",
        "lighting": "city lights as backlight, pool water reflecting everything, under-pool lighting",
        "style": "luxury editorial, cinematic, resort photography",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing at pool edge, looking at city view",
        "special": "perfect reflection in still pool water, city lights bokeh"
    },
    "silhouette_bath_candle": {
        "subject": "a woman in candlelit bathroom",
        "body": "silhouette with warm candle rim light",
        "outfit": "nothing suggested, steam and shadow",
        "environment": "luxury bathroom, multiple candles, steam rising from bath",
        "lighting": "candle flames as sole light source, warm golden rim light, steam catching candlelight",
        "style": "boudoir, intimate editorial, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing by bathtub, profile view",
        "special": "candle flames reflected in bath water, steam diffusing light"
    },
    "silhouette_rain_wet": {
        "subject": "a woman standing in rain",
        "body": "wet silhouette, rain catching light",
        "outfit": "wet clothing clinging to figure, rain making fabric transparent",
        "environment": "dark street, rain pouring, street lamp above",
        "lighting": "single street lamp above, rain drops catching light, wet pavement reflection",
        "style": "noir, rain editorial, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing in rain, head slightly tilted up",
        "special": "rain drops backlit by street lamp, wet hair and clothes, puddle reflection"
    },
    "silhouette_fire_dark": {
        "subject": "a woman before a large fire",
        "body": "silhouette with orange fire rim lighting",
        "outfit": "dark outfit, fire light on edges",
        "environment": "dark outdoor night, large bonfire or fire wall behind figure",
        "lighting": "fire as sole backlight, orange and red flickering rim light, deep shadow in front",
        "style": "dramatic editorial, fire photography, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "standing before fire, arms slightly extended",
        "special": "fire light flickering on silhouette edges, orange glow intensifying outline"
    },
    "silhouette_candle_boudoir": {
        "subject": "a woman in candlelit boudoir",
        "body": "soft warm silhouette from candle glow",
        "outfit": "lingerie suggested by warm candlelight edges",
        "environment": "luxury boudoir bedroom, dozens of candles, velvet and silk decor",
        "lighting": "multiple candles creating warm golden silhouette, soft shadows",
        "style": "boudoir photography, intimate editorial, old Hollywood",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "seated on bed edge or standing, soft feminine pose",
        "special": "warm candle glow creating soft romantic silhouette, golden atmosphere"
    },
    "silhouette_smoke_studio": {
        "subject": "a woman in smoke-filled studio",
        "body": "partially visible silhouette through smoke",
        "outfit": "hidden in smoke, form suggested",
        "environment": "professional photo studio, heavy smoke machine, multiple light sources",
        "lighting": "colored lights cutting through smoke, figure semi-visible through haze",
        "style": "editorial fashion, artistic, cinematic",
        "quality": "ultra-sharp, photorealistic, 8K",
        "pose": "emerging from smoke, mysterious pose",
        "special": "smoke tendrils catching colored light, figure partially obscured"
    },
}

CATEGORY_NAME = "🌑 실루엣 & 섀도우"
PRESET_NAMES = list(SILHOUETTE_PRESETS.keys())

def create_preset_files():
    """presets/ 폴더에 JSON 파일 생성"""
    created = 0
    for name, data in SILHOUETTE_PRESETS.items():
        path = PRESETS_DIR / f"{name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        created += 1
    print(f"✅ 프리셋 JSON {created}개 생성 완료")

def patch_dashboard():
    """dashboard.py PRESET_CATEGORIES에 새 카테고리 추가"""
    with open(DASHBOARD, "r", encoding="utf-8") as f:
        content = f.read()

    # 이미 존재하면 스킵
    if CATEGORY_NAME in content:
        print(f"⚠️  '{CATEGORY_NAME}' 카테고리 이미 존재 — 스킵")
        return

    # 앵커: "🌌 불가능 & 초현실" 카테고리 앞에 삽입
    anchor = '    "🌌 불가능 & 초현실":'
    
    preset_list = ",\n        ".join([f'"{p}"' for p in PRESET_NAMES])
    
    new_category = f'''    "{CATEGORY_NAME}": [
        {preset_list},
    ],

    '''
    
    if anchor not in content:
        print(f"❌ 앵커 찾기 실패: {anchor}")
        print("dashboard.py를 수동으로 확인하세요.")
        return

    new_content = content.replace(anchor, new_category + anchor)

    with open(DASHBOARD, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✅ dashboard.py PRESET_CATEGORIES에 '{CATEGORY_NAME}' 추가 완료")

def verify():
    """Select-String으로 검증할 PowerShell 명령 출력"""
    print("\n📋 검증 PowerShell 명령:")
    print(f'Select-String -Path "C:\\Dev\\LumineX\\dashboard.py" -Pattern "실루엣"')
    print(f'Select-String -Path "C:\\Dev\\LumineX\\presets\\silhouette_spotlight_smoke.json" -Pattern "spotlight"')
    print(f'(Get-ChildItem "C:\\Dev\\LumineX\\presets\\silhouette_*.json").Count')

if __name__ == "__main__":
    print("=" * 50)
    print("LumineX 실루엣 카테고리 패치")
    print("=" * 50)
    create_preset_files()
    patch_dashboard()
    verify()
    print("\n🎉 패치 완료! streamlit run dashboard.py 로 확인하세요.")
