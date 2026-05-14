"""
LumineX Dashboard v2.3 - 멀티 플랫폼 프롬프트 생성
실행: streamlit run dashboard.py
"""

import sys
import random
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from core.engine import list_presets, load_preset, build_prompt
from core.prompt_generator import generate_prompt_with_ai

st.set_page_config(
    page_title="LumineX Dashboard",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .stApp { background-color: #0a0a0a; }
    h1, h2, h3 { color: #f5c518 !important; }
    .stTextArea textarea {
        background-color: #111 !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
        font-size: 0.85rem !important;
    }
    .stButton > button { border-radius: 6px; font-weight: bold; }
    hr { border-color: #333 !important; }
</style>
""", unsafe_allow_html=True)

# ─── 비율 옵션 ────────────────────────────────────────────
ASPECT_RATIOS = {
    "세로 2:3 — 인물 기본": "portrait 2:3 vertical",
    "세로 3:4 — 전신샷": "portrait 3:4 vertical",
    "가로 16:9 — 시네마틱": "landscape 16:9 cinematic wide",
    "가로 4:3 — 화보": "landscape 4:3 editorial wide",
    "정방형 1:1 — 인스타": "square 1:1",
}

# ─── 데이터 ───────────────────────────────────────────────
MODEL_APPEARANCE = {
    # 아시안
    "🇰🇷 한국 — K-beauty, 하얀 피부, 또렷한 이목구비": "Korean beauty, fair porcelain skin, sharp elegant facial features, K-beauty aesthetic",
    "🇯🇵 일본 — J-beauty, 도자기 피부, 섬세한 이목구비": "Japanese beauty, porcelain delicate skin, refined subtle features, J-beauty aesthetic",
    "🇨🇳 중국 — 우아한 골격, 세련된 동양미": "Chinese beauty, elegant facial bone structure, sophisticated Eastern features",
    "🌏 동남아 — 골든 태닝, 이국적 태국/베트남 미녀": "Southeast Asian beauty, golden tan glowing skin, exotic Thai Vietnamese features",
    "🌙 중동 — 올리브 피부, 깊은 눈, 아라비안 뷰티": "Middle Eastern beauty, warm olive skin, deep dark sultry eyes, Arabian exotic features",
    # 서양/기타
    "🇪🇺 유럽 — 백인, 강한 골격, 유러피안 미녀": "European Caucasian beauty, fair skin, strong bone structure, classic European features",
    "🇺🇸 미국 — 올아메리칸, 건강미, 애슬레틱": "All-American beauty, sun-kissed healthy skin, fresh athletic look, girl-next-door glamour",
    "💃 라틴 — 브론즈 태닝, 볼륨감, 브라질/콜롬비안": "Latina beauty, bronzed tan glowing skin, voluptuous curves, Brazilian Colombian exotic",
    "✨ 혼혈 — 이국적 믹스, 독특한 매력": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
    "🖤 흑인 — 짙은 피부, 강렬한 이목구비, 파워풀": "Black beauty, rich deep dark skin, powerful striking features, African goddess",
}

MODEL_TYPES = {
    "글래머 피트니스 — 탄탄+볼륨, 섹시한 근육미": "glamorous fitness model, full bust, toned abs, round hips, fit and voluptuous, hourglass figure",
    "핫 글래머 — 가슴 볼륨, 잘록한 허리, 풍만한 힙": "hot glamour model, full voluptuous bust, extremely narrow waist, full round hips, ultra hourglass",
    "빅토리아 시크릿 — VS앤젤, 완벽한 볼륨+탄탄": "Victoria's Secret Angel, perfect full bust, toned flat abs, long legs, curvaceous yet athletic",
    "런웨이 글램 — 늘씬하면서 볼륨감 있는": "tall runway model, long legs, slender yet curvaceous, elegant glamorous figure",
    "피트니스 — 탄탄한 복근, 근육미, 스포티": "athletic fitness model, defined abs, toned muscular legs, powerful physique",
    "소프트 글램 — 부드러운 곡선, 여성스러운": "soft glamour model, feminine gentle curves, elegant posture, graceful",
    "런웨이 — 초장신, 극도로 늘씬, 다리 길이 강조": "extremely tall runway model, impossibly long legs, ultra-slender waist, elongated silhouette",
}

OUTFIT_TYPES = {
    # ── 비키니/수영복 ──────────────────────────────────────
    "마이크로 비키니 — 끈 비키니, SI 수영복 화보": {
        "gemini": "micro string bikini, barely-there coverage, Sports Illustrated swimsuit style",
        "chatgpt": "designer string bikini, minimalist swimwear, Sports Illustrated editorial style",
    },
    "원피스 수영복 — 하이컷, 컷아웃 디자인": {
        "gemini": "high-cut one-piece swimsuit, bold cutouts, athletic glamour",
        "chatgpt": "high-cut designer one-piece swimsuit, artistic cutouts, Sports Illustrated style",
    },
    # ── 미니/드레스 ────────────────────────────────────────
    "컷아웃 미니드레스 — 전략적 컷아웃, 섹시한 디자인": {
        "gemini": "cutout mini dress, strategic skin-baring cutouts, bold editorial design",
        "chatgpt": "designer cutout mini dress, architectural cutout details, fashion editorial",
    },
    "하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인": {
        "gemini": "ultra-high slit evening gown, deep plunging neckline, red carpet glamour",
        "chatgpt": "high slit evening gown, plunging neckline, luxury red carpet fashion",
    },
    "밴도탑+초미니 — 배꼽 노출, 극초미니 스커트": {
        "gemini": "bandeau crop top, exposed midriff, micro mini skirt, fashion editorial",
        "chatgpt": "bandeau crop top, midriff-baring, micro mini skirt, bold fashion editorial",
    },
    "바디콘 미니드레스 — 몸매 강조, 타이트핏": {
        "gemini": "bodycon mini dress, body-hugging silhouette, glamorous tight fit",
        "chatgpt": "bodycon mini dress, figure-hugging design, glamorous fashion editorial",
    },
    # ── 코르셋/탑 ──────────────────────────────────────────
    "코르셋 드레스 — 잘록한 허리, 볼륨감 강조": {
        "gemini": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "chatgpt": "fashion corset dress, cinched waist, dramatic neckline, haute couture style",
    },
    "브라탑+하이슬릿 — 브라탑, 롱 하이슬릿": {
        "gemini": "bra top, ultra-high slit skirt, maximum leg exposure, editorial",
        "chatgpt": "fashion bra top, high slit skirt, long leg emphasis, Vogue editorial",
    },
    # ── 란제리/바디수트 ────────────────────────────────────
    "란제리 에디토리얼 — VS 스타일, 실크 레이스": {
        "gemini": "luxury silk lace lingerie, Victoria's Secret editorial style, glamorous",
        "chatgpt": "luxury silk lace fashion set, Victoria's Secret editorial, artistic glamour photography",
    },
    "시스루 바디수트 — 메쉬, 아방가르드": {
        "gemini": "sheer mesh bodysuit, avant-garde fashion editorial, artistic",
        "chatgpt": "sheer fashion bodysuit, mesh overlay, avant-garde editorial style",
    },
    "오픈백 미니드레스 — 등 노출, 플런징 넥": {
        "gemini": "open back mini dress, plunging neckline, backless glamour",
        "chatgpt": "backless mini dress, dramatic plunging neckline, high-fashion editorial",
    },
    # ── 피트니스 ───────────────────────────────────────────
    "스포츠브라+레깅스 — 핫한 피트니스 룩": {
        "gemini": "sports bra, high-waist leggings, midriff bare, fitness editorial",
        "chatgpt": "athletic sports bra, high-waist leggings, fitness editorial, Sports Illustrated",
    },
}

ENVIRONMENTS = {
    # ── 럭셔리/도시 ────────────────────────────────────────
    "미니멀 스튜디오 — 흰 배경, 깔끔": "pure white minimalist studio, seamless backdrop",
    "두바이 펜트하우스 루프탑 — 야경": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
    "모나코 테라스 — 지중해 야경": "Monaco luxury terrace, Mediterranean night view, superyachts harbor",
    "베르사유 궁전 — 황금빛 홀": "Palace of Versailles golden hall, ornate chandeliers, luxury interior",
    "뉴욕 루프탑 — 맨하탄 야경": "New York City rooftop, Manhattan skyline at night, urban glamour",
    "파리 오스만 발코니 — 에펠탑 뷰": "Paris Haussmann balcony, Eiffel Tower view, golden hour",
    # ── 리조트/해변 ────────────────────────────────────────
    "럭셔리 인피니티 풀 — 열대 리조트": "luxury infinity pool edge, tropical resort, palm trees",
    "산토리니 절벽 — 에게해 야경": "Santorini cliff, blue dome church, Aegean sea at night",
    "말디브 수상빌라 — 크리스탈 바다": "Maldives overwater villa, crystal turquoise sea, tropical paradise",
    "리비에라 절벽 — 지중해 낮": "French Riviera cliff, azure Mediterranean sea, golden sunlight",
    "마이애미 비치 — 선셋": "Miami Beach sunset, Ocean Drive, warm pink sky",
    "럭셔리 요트 덱 — 지중해": "luxury superyacht deck, Mediterranean sea, ocean horizon",
    # ── 시네마틱/다크 ──────────────────────────────────────
    "도쿄 네온 거리 — 비 오는 밤": "Shinjuku neon-lit rainy alley, Tokyo cyberpunk night",
    "다크 바로크 — 화려한 실내": "dark baroque opulent chamber, velvet and gold interior",
    "파리 패션위크 런웨이 — 모던 무대": "Paris fashion week modernist runway stage, fashion show",
    "사하라 골든아워 — 황금빛 사막": "Sahara desert dunes, golden hour sunset, dramatic sky",
    "화산 절벽 — 극적인 자연": "dramatic volcanic cliff, stormy ocean, powerful nature",
    "얼음 동굴 — 크리스탈 블루": "ice cave interior, crystal blue formations, ethereal light",
}

STYLES = {
    "빅토리아 시크릿 패션쇼": "Victoria's Secret fashion show runway editorial",
    "스포츠 일러스트레이티드 수영복": "Sports Illustrated swimsuit special edition",
    "보그 이탈리아 하이패션": "Vogue Italia high-fashion editorial",
    "베르사체 캠페인 — 대담한 럭셔리": "Versace campaign bold luxury glamour",
    "하퍼스 바자 — 관능적 에디토리얼": "Harper's Bazaar sensual fashion editorial",
    "발렌티노 — 레드 카펫 럭셔리": "Valentino red carpet luxury editorial",
    "돌체앤가바나 — 이탈리안 글래머": "Dolce and Gabbana Italian glamour editorial",
    "티에리 뮈글러 — 파워 패션": "Thierry Mugler inspired power fashion editorial",
    "알렉산더 맥퀸 — 드라마틱": "Alexander McQueen dramatic fashion editorial",
    "사이버펑크 — 시네마틱": "cyberpunk cinematic fashion photography",
    "스포츠 럭셔리 — 나이키/아디다스 하이엔드": "luxury sports editorial, high-end athletic fashion",
}

MATERIALS = {
    "리퀴드 새틴 — 액체처럼 흐르는 광택": "liquid satin, ultra-glossy wet-look finish",
    "페이턴트 레더 — 하이글로스 가죽": "shiny patent leather, mirror-like high-gloss surface",
    "메탈릭 비닐 — 금속 광택, 미래적": "reflective metallic vinyl, chrome-like mirror sheen",
    "시스루 오간자 — 반투명, 살이 비치는": "sheer organza, semi-transparent, skin visible beneath",
    "라텍스 — 피부 밀착, 세컨드스킨": "latex second-skin, body-hugging vacuum-seal finish",
    "시퀸 — 빛을 받으면 반짝이는": "iridescent sequins, light-catching glittering surface",
    "웻룩 스판덱스 — 젖은 듯한 느낌": "wet-look spandex, soaking wet appearance, body-hugging",
    "크리스탈 메쉬 — 망사에 크리스탈": "crystal mesh, rhinestone-embellished sheer fabric",
    "벨벳 — 부드럽고 고급스러운": "crushed velvet, rich luxurious texture",
    "골드 포일 — 황금빛 메탈릭": "metallic gold foil, mirror-finish gold surface",
}

LIGHTING = {
    "골든아워 — 따뜻한 피부 발광": "golden hour warm backlight, skin luminosity, glowing",
    "옥타박스 스트로브 — 전문 스튜디오": "professional octabox strobe, high-contrast glamour lighting",
    "네온 엣지 — 멀티컬러 네온 빛": "multi-colored neon edge glow, cyberpunk light",
    "키아로스쿠로 — 극적인 명암": "dramatic chiaroscuro, deep shadows and sharp highlights",
    "소프트 뷰티라이트 — 균일하고 부드러운": "soft beauty dish light, even flattering illumination",
    "하드 스트로브 — 바디 정의 강조": "harsh direct strobe, body muscle definition emphasis",
    "볼류메트릭 포그 — 시네마틱 안개빛": "volumetric fog cinematic light, atmospheric mood",
    "림라이트 실루엣 — 역광 실루엣": "strong rim backlight, silhouette definition, halo effect",
}

CAMERA_ANGLES = {
    "전신샷 — 머리부터 발끝": "full body head-to-toe shot",
    "3/4 샷 — 허벅지까지": "3/4 body shot thigh to head",
    "웨이스트샷 — 상반신 집중": "waist-up shot upper body emphasis",
    "로우앵글 — 다리 강조, 아래서 위로": "low angle upward shot legs dramatically elongated",
    "클로즈업 — 얼굴+가슴 집중": "close-up beauty shot face and upper chest",
}

FOOTWEAR = {
    "스틸레토 힐 — 극도로 높은 힐, 다리 라인 강조": "wearing extreme stiletto heels, legs elongated",
    "스트래피 샌들 힐 — 얇은 끈 샌들 힐": "wearing strappy high heel sandals, elegant feet",
    "플랫폼 부츠 — 두꺼운 솔, 파워풀": "wearing platform boots, powerful stance",
    "무릎까지 부츠 — 니하이 부츠, 섹시한": "wearing knee-high boots, sexy long legs",
    "허벅지까지 부츠 — 싸이하이 부츠": "wearing thigh-high boots, ultra sexy",
    "포인티드 토 힐 — 뾰족한 앞코 힐": "wearing pointed toe stiletto pumps, classic glamour",
    "맨발 — 자연스러운": "barefoot, natural",
}

CAMERAS = {
    "하셀블라드 H6D — 80mm f/2.8": "Hasselblad H6D 80mm f/2.8 ISO 100",
    "캐논 EOS R5 — 85mm f/1.2 인물": "Canon EOS R5 85mm f/1.2 portrait lens ISO 100",
    "소니 A7R V — 50mm f/1.4": "Sony A7R V 50mm f/1.4 ISO 100",
    "니콘 Z9 — 85mm f/1.8": "Nikon Z9 85mm f/1.8 ISO 100",
    "페이즈원 XF IQ4 — 110mm f/2.8 중형": "Phase One XF IQ4 110mm f/2.8 medium format ISO 50",
}

# ─── 플랫폼별 프롬프트 빌더 ──────────────────────────────

def build_gemini_prompt(data: dict, aspect: str, realism: bool) -> str:
    """Gemini: 자연어 서술형, 길고 묘사적"""
    aspect_desc = ASPECT_RATIOS.get(aspect, "")
    realism_kw  = "photorealistic, RAW photo, hyperrealistic, natural skin texture, pore detail, film grain, professional photographer" if realism else ""
    appearance  = MODEL_APPEARANCE.get(data.get('appearance', ''), '')
    outfit_data = OUTFIT_TYPES[data['outfit']]
    outfit      = outfit_data["gemini"] if isinstance(outfit_data, dict) else outfit_data
    footwear    = FOOTWEAR.get(data.get('footwear', ''), '')

    parts = [
        f"Professional fashion photograph, {CAMERA_ANGLES[data['angle']]}, model fills the entire frame.",
        f"Model: stunning {MODEL_TYPES[data['model']]}{', ' + appearance if appearance else ''}.",
        f"Wearing: {outfit}, made of {MATERIALS[data['material']]}{', ' + footwear if footwear else ''}.",
        f"Environment: {ENVIRONMENTS[data['env']]}, background softly blurred bokeh.",
        f"Lighting: {LIGHTING[data['light']]}.",
        f"Style reference: {STYLES[data['style']]}.",
        f"Camera: {CAMERAS[data['camera']]}, sharp focus on model.",
    ]
    suffix = []
    if realism_kw:
        suffix.append(realism_kw)
    if aspect_desc:
        suffix.append(aspect_desc)
    suffix.append("model is the absolute primary subject, tight framing, background secondary")
    return " ".join(parts) + " " + ", ".join(suffix) + "."


def build_chatgpt_prompt(data: dict, aspect: str) -> str:
    """ChatGPT(DALL-E): 150-200단어 서술형, 필터 안전"""
    aspect_map = {
        "세로 2:3 — 인물 기본": "vertical portrait 2:3",
        "세로 3:4 — 전신샷": "vertical portrait 3:4",
        "가로 16:9 — 시네마틱": "wide cinematic 16:9",
        "가로 4:3 — 화보": "wide editorial 4:3",
        "정방형 1:1 — 인스타": "square format 1:1",
    }
    aspect_desc = aspect_map.get(aspect, "vertical portrait 2:3")
    appearance  = MODEL_APPEARANCE.get(data.get('appearance', ''), '')
    model       = MODEL_TYPES[data['model']]
    outfit_data = OUTFIT_TYPES[data['outfit']]
    outfit      = outfit_data["chatgpt"] if isinstance(outfit_data, dict) else outfit_data
    material    = MATERIALS[data['material']]
    env         = ENVIRONMENTS[data['env']]
    light       = LIGHTING[data['light']]
    style       = STYLES[data['style']]
    camera      = CAMERAS[data['camera']]
    angle       = CAMERA_ANGLES[data['angle']]
    footwear    = FOOTWEAR.get(data.get('footwear', ''), '')
    appearance_desc = f"with {appearance}" if appearance else ""

    return (
        f"Professional fashion photograph, {aspect_desc}, {angle}. "
        f"A stunning {model} {appearance_desc}, commanding the frame with confidence and elegance. "
        f"She wears {outfit}, crafted from {material}{', ' + footwear if footwear else ''}. "
        f"The scene unfolds at {env}, "
        f"bathed in {light}, creating a breathtaking atmosphere. "
        f"Shot in the style of {style}, "
        f"captured on {camera} with razor-sharp focus on the model. "
        f"The model fills the entire frame, background softly blurred. "
        f"Photorealistic, hyperrealistic skin texture, natural pore detail, "
        f"professional color grading, award-winning fashion photography, "
        f"stunning editorial masterpiece quality."
    )


def build_midjourney_prompt(data: dict, aspect: str) -> str:
    """Midjourney: 태그 나열 + 파라미터"""
    ar_map = {
        "세로 2:3 — 인물 기본": "2:3",
        "세로 3:4 — 전신샷": "3:4",
        "가로 16:9 — 시네마틱": "16:9",
        "가로 4:3 — 화보": "4:3",
        "정방형 1:1 — 인스타": "1:1",
    }
    ar         = ar_map.get(aspect, "2:3")
    appearance = MODEL_APPEARANCE.get(data.get('appearance', ''), '').split(',')[0]

    model_short    = MODEL_TYPES[data['model']].split(',')[0]
    outfit_data    = OUTFIT_TYPES[data['outfit']]
    outfit_short   = (outfit_data["chatgpt"] if isinstance(outfit_data, dict) else outfit_data).split(',')[0]
    material_short = MATERIALS[data['material']].split(',')[0]
    env_short      = ENVIRONMENTS[data['env']].split(',')[0]
    light_short    = LIGHTING[data['light']].split(',')[0]
    style_short    = STYLES[data['style']].split(',')[0]
    footwear_short = FOOTWEAR.get(data.get('footwear', ''), '').split(',')[0]

    tags = [t for t in [
        appearance, model_short, outfit_short, material_short,
        footwear_short, env_short, light_short,
        style_short, "photorealistic", "hyperrealistic",
        "fashion editorial", "sharp focus", "8K",
        "professional photography", "skin texture detail"
    ] if t]
    return f"{', '.join(tags)} --ar {ar} --style raw --q 2"


# ─── 헤더 ─────────────────────────────────────────────────
st.markdown('<h1 style="color:#f5c518;letter-spacing:6px;font-size:2.2rem;">✦ LumineX</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#666;font-size:0.85rem;margin-top:-15px;">AI Fashion Image Prompt Engine v2.5</p>', unsafe_allow_html=True)
st.markdown("---")

# ─── 사이드바 ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ 전역 설정")
    st.markdown("---")

    global_platform = st.radio(
        "🖥️ 출력 플랫폼",
        options=["Gemini", "ChatGPT (DALL-E)", "Midjourney"],
        index=0,
        help="플랫폼에 맞는 프롬프트 스타일로 자동 변환"
    )

    global_aspect = st.selectbox(
        "📐 이미지 비율",
        options=list(ASPECT_RATIOS.keys()),
        index=0,
    )

    global_realism = st.toggle("📷 실사 모드", value=True, help="photorealistic 키워드 자동 추가 (Gemini 전용)")

    st.markdown("---")
    platform_colors = {"Gemini": "🔵", "ChatGPT (DALL-E)": "🟢", "Midjourney": "🟣"}
    st.markdown(f"**플랫폼:** {platform_colors[global_platform]} `{global_platform}`")
    st.markdown(f"**비율:** `{global_aspect.split('—')[0].strip()}`")
    if global_platform == "Gemini":
        st.markdown(f"**실사:** `{'ON ✅' if global_realism else 'OFF'}`")

    st.markdown("---")
    st.markdown("### 📌 사용법")
    st.markdown("""
1. 플랫폼 선택
2. 탭 선택
3. 요소 선택
4. **프롬프트 조합** 클릭
5. 코드박스 클릭 → 복사
6. 해당 플랫폼에 붙여넣기
""")

    st.markdown("---")
    st.markdown("### 💡 플랫폼 팁")
    if global_platform == "Gemini":
        st.info("자연어 서술형 프롬프트. 길고 상세할수록 좋아요.")
    elif global_platform == "ChatGPT (DALL-E)":
        st.success("간결하고 키워드 중심. 짧고 강렬하게!")
    else:
        st.warning("태그 나열 + --파라미터 방식. Midjourney에 바로 붙여넣기!")


def get_prompt(data: dict) -> str:
    if global_platform == "Gemini":
        return build_gemini_prompt(data, global_aspect, global_realism)
    elif global_platform == "ChatGPT (DALL-E)":
        return build_chatgpt_prompt(data, global_aspect)
    else:
        return build_midjourney_prompt(data, global_aspect)


tab1, tab2, tab3, tab4 = st.tabs(["🎨 프리셋 모드", "🛠️ 수동 조합", "🎲 랜덤 모드", "🎬 영상 프롬프트"])

# ══════════════════════════════════════════════════════════
# 탭 1: 프리셋 모드
# ══════════════════════════════════════════════════════════
with tab1:
    st.markdown("### 프리셋으로 프롬프트 생성")
    presets = list_presets()

    col1, col2 = st.columns(2)
    with col1:
        selected_preset = st.selectbox("🎨 프리셋 선택", options=presets, format_func=lambda x: f"• {x}")

    # ── 8개 오버라이드 섹션 ──────────────────────────────
    NONE = "None — 프리셋 기본값 사용"

    col1, col2 = st.columns(2)
    with col1:
        preset_appearance = st.selectbox(
            "👩 인종/국적",
            [NONE] + list(MODEL_APPEARANCE.keys()),
            key="preset_appearance"
        )
        preset_body = st.selectbox(
            "👤 체형",
            [NONE] + list(MODEL_TYPES.keys()),
            key="preset_body"
        )
        preset_outfit = st.selectbox(
            "👗 의상",
            [NONE] + list(OUTFIT_TYPES.keys()),
            key="preset_outfit"
        )
        preset_material = st.selectbox(
            "🧵 소재",
            [NONE] + list(MATERIALS.keys()),
            key="preset_material"
        )
    with col2:
        preset_framing = st.selectbox(
            "📸 프레이밍",
            [NONE] + list(CAMERA_ANGLES.keys()),
            key="preset_framing"
        )
        preset_footwear = st.selectbox(
            "👠 신발",
            [NONE] + list(FOOTWEAR.keys()),
            key="preset_footwear"
        )
        preset_lighting = st.selectbox(
            "💡 조명 오버라이드",
            [NONE] + list(LIGHTING.keys()),
            key="preset_lighting"
        )
        preset_style = st.selectbox(
            "🎬 스타일 레퍼런스",
            [NONE] + list(STYLES.keys()),
            key="preset_style"
        )

    col_a, col_b, col_c = st.columns([1, 1, 2])
    with col_a:
        btn_ai = st.button("🤖 AI 생성", use_container_width=True, type="primary")
    with col_b:
        btn_quick = st.button("⚡ 빠른 생성", use_container_width=True)

    if "preset_prompt" not in st.session_state:
        st.session_state.preset_prompt = ""

    def build_preset_overrides() -> dict:
        """선택된 오버라이드 요소들을 딕셔너리로 반환 (프리셋 필드 덮어쓰기용)"""
        overrides = {}
        if preset_appearance != NONE:
            overrides['appearance'] = MODEL_APPEARANCE[preset_appearance]
        if preset_body != NONE:
            overrides['body'] = MODEL_TYPES[preset_body]
        if preset_outfit != NONE:
            od = OUTFIT_TYPES[preset_outfit]
            overrides['outfit'] = od["gemini"] if isinstance(od, dict) else od
        if preset_material != NONE:
            overrides['material'] = MATERIALS[preset_material]
        if preset_framing != NONE:
            overrides['framing'] = CAMERA_ANGLES[preset_framing]
        if preset_footwear != NONE:
            overrides['footwear'] = FOOTWEAR[preset_footwear]
        if preset_lighting != NONE:
            overrides['lighting'] = LIGHTING[preset_lighting]
        if preset_style != NONE:
            overrides['style'] = STYLES[preset_style]
        return overrides

    def apply_overrides_to_prompt(preset: dict, overrides: dict) -> str:
        """오버라이드를 프리셋에 적용해서 프롬프트 생성"""
        p = {**preset, **overrides}
        appearance_str = f"Model appearance: {overrides['appearance']}. " if 'appearance' in overrides else ""
        framing_str = overrides.get('framing', 'full body shot')
        footwear_str = f", {overrides['footwear']}" if 'footwear' in overrides else ""

        prompt = (
            f"Professional fashion photograph, {framing_str}. "
            f"{appearance_str}"
            f"Model: {p.get('subject', 'a stunning female model')}. "
            f"Body: {p.get('body', '')}. "
            f"Wearing: {p.get('outfit', '')}, made of {p.get('material', '')}{footwear_str}. "
            f"Environment: {p.get('environment', '')}. "
            f"Lighting: {p.get('lighting', '')}. "
            f"Style: {p.get('style', '')}. "
            f"{p.get('quality', 'ultra-sharp, 8K, professional photography')}."
        )
        return prompt.strip()

    if btn_ai and selected_preset:
        st.session_state.preset_prompt = ""
        with st.spinner("Claude가 프롬프트 생성 중..."):
            try:
                raw = generate_prompt_with_ai(selected_preset)
                overrides = build_preset_overrides()
                prefix = []
                if 'appearance' in overrides:
                    prefix.append(overrides['appearance'].split(',')[0])
                if 'body' in overrides:
                    prefix.append(overrides['body'].split(',')[0])
                if prefix:
                    raw = f"Model: {', '.join(prefix)}. " + raw
                aspect_desc = ASPECT_RATIOS.get(global_aspect, "")
                if aspect_desc:
                    raw += f" {aspect_desc}, vertical portrait orientation, taller than wide."
                st.session_state.preset_prompt = raw
            except Exception as e:
                st.error(f"오류: {str(e)}")

    if btn_quick and selected_preset:
        st.session_state.preset_prompt = ""
        preset = load_preset(selected_preset)
        overrides = build_preset_overrides()
        aspect_desc = ASPECT_RATIOS.get(global_aspect, "portrait 2:3 vertical")
        raw = apply_overrides_to_prompt(preset, overrides)

        if global_platform == "Gemini":
            raw += f" {aspect_desc}, vertical portrait orientation, taller than wide."

        elif global_platform == "ChatGPT (DALL-E)":
            raw += (
                f" {aspect_desc}. "
                f"Photorealistic, hyperrealistic skin texture, natural pore detail, "
                f"professional color grading, award-winning fashion photography, "
                f"stunning editorial masterpiece quality."
            )

        else:  # Midjourney
            ar_map = {
                "세로 2:3 — 인물 기본": "2:3",
                "세로 3:4 — 전신샷": "3:4",
                "가로 16:9 — 시네마틱": "16:9",
                "가로 4:3 — 화보": "4:3",
                "정방형 1:1 — 인스타": "1:1",
            }
            ar = ar_map.get(global_aspect, "2:3")
            raw += f" --ar {ar} --style raw --q 2"

        st.session_state.preset_prompt = raw

    if st.session_state.preset_prompt:
        st.text_area("생성된 프롬프트", value=st.session_state.preset_prompt, height=160)
        st.code(st.session_state.preset_prompt, language=None)
        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")

# ══════════════════════════════════════════════════════════
# 탭 2: 수동 조합
# ══════════════════════════════════════════════════════════
with tab2:
    st.markdown("### 요소별 수동 조합")

    if st.button("🎲 전체 랜덤으로 채우기"):
        st.session_state.r_appearance = random.choice(list(MODEL_APPEARANCE.keys()))
        st.session_state.r_model      = random.choice(list(MODEL_TYPES.keys()))
        st.session_state.r_outfit     = random.choice(list(OUTFIT_TYPES.keys()))
        st.session_state.r_material   = random.choice(list(MATERIALS.keys()))
        st.session_state.r_footwear   = random.choice(list(FOOTWEAR.keys()))
        st.session_state.r_env        = random.choice(list(ENVIRONMENTS.keys()))
        st.session_state.r_light      = random.choice(list(LIGHTING.keys()))
        st.session_state.r_angle      = random.choice(list(CAMERA_ANGLES.keys()))
        st.session_state.r_style      = random.choice(list(STYLES.keys()))
        st.session_state.r_camera     = random.choice(list(CAMERAS.keys()))

    col1, col2 = st.columns(2)
    with col1:
        appearance  = st.selectbox("👩 모델 외모 — 인종/국적",      list(MODEL_APPEARANCE.keys()),   index=list(MODEL_APPEARANCE.keys()).index(st.session_state.get("r_appearance", list(MODEL_APPEARANCE.keys())[0])), key="manual_appearance")
        model_type  = st.selectbox("👤 모델 타입 — 체형과 비율",    list(MODEL_TYPES.keys()),        index=list(MODEL_TYPES.keys()).index(st.session_state.get("r_model", list(MODEL_TYPES.keys())[0])))
        outfit      = st.selectbox("👗 의상 타입 — 스타일",         list(OUTFIT_TYPES.keys()),       index=list(OUTFIT_TYPES.keys()).index(st.session_state.get("r_outfit", list(OUTFIT_TYPES.keys())[0])))
        material    = st.selectbox("🧵 소재 — 옷감 질감",           list(MATERIALS.keys()),          index=list(MATERIALS.keys()).index(st.session_state.get("r_material", list(MATERIALS.keys())[0])))
        footwear    = st.selectbox("👠 신발 — 힐/부츠 스타일",      list(FOOTWEAR.keys()),           index=list(FOOTWEAR.keys()).index(st.session_state.get("r_footwear", list(FOOTWEAR.keys())[0])))
    with col2:
        style       = st.selectbox("🎬 스타일 — 화보 레퍼런스",     list(STYLES.keys()),             index=list(STYLES.keys()).index(st.session_state.get("r_style", list(STYLES.keys())[0])))
        environment = st.selectbox("🏙️ 환경 — 촬영 장소",          list(ENVIRONMENTS.keys()),       index=list(ENVIRONMENTS.keys()).index(st.session_state.get("r_env", list(ENVIRONMENTS.keys())[0])))
        lighting    = st.selectbox("💡 조명 — 빛의 분위기",         list(LIGHTING.keys()),           index=list(LIGHTING.keys()).index(st.session_state.get("r_light", list(LIGHTING.keys())[0])))
        angle       = st.selectbox("📸 카메라 앵글 — 촬영 각도",    list(CAMERA_ANGLES.keys()),      index=list(CAMERA_ANGLES.keys()).index(st.session_state.get("r_angle", list(CAMERA_ANGLES.keys())[0])))
        camera      = st.selectbox("📷 카메라 — 장비",              list(CAMERAS.keys()),            index=list(CAMERAS.keys()).index(st.session_state.get("r_camera", list(CAMERAS.keys())[0])))

    col_x, col_y, _ = st.columns([1, 1, 2])
    with col_x:
        btn_build = st.button("✨ 프롬프트 조합", type="primary", use_container_width=True)
    with col_y:
        btn_ai_enhance = st.button("🤖 AI로 강화", use_container_width=True)

    if "manual_prompt" not in st.session_state:
        st.session_state.manual_prompt = ""

    if btn_build:
        data = {
            "appearance": appearance,
            "model": model_type, "outfit": outfit,
            "material": material, "footwear": footwear,
            "env": environment, "light": lighting,
            "angle": angle, "style": style, "camera": camera,
        }
        st.session_state.manual_prompt = get_prompt(data)

    if btn_ai_enhance and st.session_state.manual_prompt:
        with st.spinner("Claude가 프롬프트 강화 중..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                platform_instruction = {
                    "Gemini": "Make it detailed and descriptive (150-200 words), natural language style.",
                    "ChatGPT (DALL-E)": "Make it concise and keyword-focused (under 80 words), punchy style.",
                    "Midjourney": "Convert to comma-separated tags with --ar 2:3 --style raw --q 2 at the end.",
                }
                response = client.messages.create(
                    model="claude-sonnet-4-5",
                    max_tokens=500,
                    messages=[{"role": "user", "content": f"""Enhance this fashion photography prompt for {global_platform}.
Rules: model fills frame, runway proportions, revealing outfit, photorealistic skin.
{platform_instruction[global_platform]}
Output ONLY the prompt:

{st.session_state.manual_prompt}"""}]
                )
                st.session_state.manual_prompt = response.content[0].text.strip()
            except Exception as e:
                st.error(f"오류: {str(e)}")

    if st.session_state.manual_prompt:
        st.text_area("조합된 프롬프트", value=st.session_state.manual_prompt, height=160)
        st.code(st.session_state.manual_prompt, language=None)
        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")

# ══════════════════════════════════════════════════════════
# 탭 3: 랜덤 모드
# ══════════════════════════════════════════════════════════
with tab3:
    st.markdown("### 완전 랜덤 프롬프트 생성")
    st.caption("모든 요소를 랜덤으로 조합하여 프롬프트를 생성합니다.")

    col1, col2, _ = st.columns([1, 1, 2])
    with col1:
        btn_rand = st.button("🎲 랜덤 생성", type="primary", use_container_width=True)
    with col2:
        btn_rand_ai = st.button("🤖 AI 랜덤", use_container_width=True)

    if "random_prompt" not in st.session_state:
        st.session_state.random_prompt = ""

    if btn_rand:
        data = {
            "appearance": random.choice(list(MODEL_APPEARANCE.keys())),
            "model":    random.choice(list(MODEL_TYPES.keys())),
            "outfit":   random.choice(list(OUTFIT_TYPES.keys())),
            "material": random.choice(list(MATERIALS.keys())),
            "footwear": random.choice(list(FOOTWEAR.keys())),
            "env":      random.choice(list(ENVIRONMENTS.keys())),
            "light":    random.choice(list(LIGHTING.keys())),
            "angle":    random.choice(list(CAMERA_ANGLES.keys())),
            "style":    random.choice(list(STYLES.keys())),
            "camera":   random.choice(list(CAMERAS.keys())),
        }
        st.session_state.random_prompt = get_prompt(data)

    if btn_rand_ai:
        preset_name = random.choice(list_presets())
        with st.spinner(f"Claude가 [{preset_name}] 기반으로 생성 중..."):
            try:
                st.session_state.random_prompt = generate_prompt_with_ai(preset_name)
            except Exception as e:
                st.error(f"오류: {str(e)}")

    if st.session_state.random_prompt:
        st.text_area("랜덤 프롬프트", value=st.session_state.random_prompt, height=160)
        st.code(st.session_state.random_prompt, language=None)
        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#444;font-size:0.75rem;">✦ LumineX v2.6 — AI Fashion Image Engine</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# 탭 4: 영상 프롬프트 (Veo 3)
# ══════════════════════════════════════════════════════════
with tab4:
    st.markdown("### 🎬 영상 프롬프트 생성 (Veo 3)")
    st.caption("Gemini 대화창의 Veo 3에 붙여넣어 영상을 생성하세요.")

    # ── 영상 설정 ──────────────────────────────────────────
    VIDEO_DURATIONS = {
        "5초 — 짧고 임팩트 있는": "5 seconds",
        "8초 — 표준 클립": "8 seconds",
        "10초 — 긴 클립": "10 seconds",
    }

    VIDEO_MOTIONS = {
        "워킹 — 런웨이 워크, 카메라 정면": "walking towards camera, confident runway walk, slow motion",
        "턴 — 360도 회전, 의상 전체 공개": "slow 360 degree turn, revealing full outfit",
        "포즈 — 정적 포즈, 바람에 머리 날림": "standing pose, hair flowing in wind, subtle movement",
        "댄스 — 섹시한 느낌의 부드러운 움직임": "slow sensual dance movement, fluid motion",
        "워킹+턴 — 걷다가 카메라 보며 턴": "walking then turning to camera, fashion editorial motion",
        "등장 — 안개/빛 속에서 천천히 등장": "emerging slowly from mist and light, dramatic entrance",
    }

    VIDEO_CAMERAS = {
        "시네마틱 — 느린 달리샷": "slow cinematic dolly shot, smooth camera movement",
        "오빗 — 모델 주위를 도는 카메라": "slow orbit around subject, 360 camera movement",
        "줌인 — 전신에서 얼굴로 천천히 줌": "slow zoom from full body to face, intimate close-up",
        "로우앵글 — 아래서 위로 올려다보기": "low angle upward camera, powerful perspective",
        "하이앵글 — 위에서 내려다보기": "high angle downward camera, elegant perspective",
        "핸드헬드 — 약간의 흔들림, 현장감": "slight handheld camera movement, documentary feel",
    }

    VIDEO_ATMOSPHERES = {
        "럭셔리 글래머 — 화려하고 고급스러운": "luxury glamour atmosphere, high-end fashion film",
        "다크 시네마틱 — 어둡고 영화적인": "dark cinematic atmosphere, noir fashion film",
        "골든아워 — 따뜻한 황금빛": "golden hour warm light, dreamy fashion film",
        "네온 사이버펑크 — 미래적 네온 분위기": "neon cyberpunk atmosphere, futuristic fashion film",
        "미니멀 클린 — 깔끔하고 모던한": "minimal clean white atmosphere, modern fashion film",
        "에디토리얼 — 잡지 화보 느낌": "editorial fashion film, Vogue video style",
    }

    col1, col2 = st.columns(2)
    with col1:
        # 이미지 프롬프트 기반 생성
        st.markdown("**📝 기존 프롬프트 기반으로 변환**")
        source_prompt = st.text_area(
            "이미지 프롬프트 붙여넣기 (선택사항)",
            placeholder="기존 이미지 프롬프트를 여기에 붙여넣으면 영상용으로 변환해줘요...",
            height=120,
            key="video_source"
        )
        video_duration = st.selectbox("⏱️ 영상 길이", list(VIDEO_DURATIONS.keys()))
        video_motion   = st.selectbox("🏃 모션 타입", list(VIDEO_MOTIONS.keys()))

    with col2:
        video_camera    = st.selectbox("📷 카메라 무브먼트", list(VIDEO_CAMERAS.keys()))
        video_atmosphere = st.selectbox("🌟 분위기", list(VIDEO_ATMOSPHERES.keys()))
        video_appearance = st.selectbox(
            "👩 모델 외모",
            ["None — 프롬프트 기반"] + list(MODEL_APPEARANCE.keys()),
            key="video_appearance"
        )
        video_outfit = st.selectbox(
            "👗 의상",
            ["None — 프롬프트 기반"] + list(OUTFIT_TYPES.keys()),
            key="video_outfit"
        )

    st.markdown("")
    col_x, col_y, _ = st.columns([1, 1, 2])
    with col_x:
        btn_video_build = st.button("🎬 영상 프롬프트 생성", type="primary", use_container_width=True)
    with col_y:
        btn_video_ai = st.button("🤖 AI로 강화", use_container_width=True, key="btn_video_ai")

    if "video_prompt" not in st.session_state:
        st.session_state.video_prompt = ""

    if btn_video_build:
        st.session_state.video_prompt = ""
        dur  = VIDEO_DURATIONS[video_duration]
        mot  = VIDEO_MOTIONS[video_motion]
        cam  = VIDEO_CAMERAS[video_camera]
        atm  = VIDEO_ATMOSPHERES[video_atmosphere]

        appearance_str = ""
        if video_appearance != "None — 프롬프트 기반":
            appearance_str = f"Model: {MODEL_APPEARANCE[video_appearance].split(',')[0]}. "

        outfit_str = ""
        if video_outfit != "None — 프롬프트 기반":
            od = OUTFIT_TYPES[video_outfit]
            outfit_str = f"Wearing: {(od['gemini'] if isinstance(od, dict) else od).split(',')[0]}. "

        if source_prompt:
            # 기존 이미지 프롬프트 기반 변환
            video_prompt = (
                f"Cinematic fashion video, {dur}. "
                f"Based on: {source_prompt[:200]}. "
                f"{appearance_str}{outfit_str}"
                f"Motion: {mot}. "
                f"Camera: {cam}. "
                f"Atmosphere: {atm}. "
                f"Photorealistic, hyperrealistic, 4K cinematic quality, "
                f"professional fashion film, no text, no watermark."
            )
        else:
            # 새로 생성
            video_prompt = (
                f"Cinematic fashion video, {dur}. "
                f"{appearance_str}{outfit_str}"
                f"Motion: {mot}. "
                f"Camera: {cam}. "
                f"Atmosphere: {atm}. "
                f"Photorealistic, hyperrealistic, 4K cinematic quality, "
                f"professional fashion film, no text, no watermark."
            )
        st.session_state.video_prompt = video_prompt

    if btn_video_ai and (source_prompt or st.session_state.video_prompt):
        with st.spinner("Claude가 영상 프롬프트 강화 중..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                base = source_prompt or st.session_state.video_prompt
                response = client.messages.create(
                    model="claude-sonnet-4-5",
                    max_tokens=500,
                    messages=[{"role": "user", "content": f"""You are an expert Veo 3 video prompt engineer.
Create a powerful cinematic fashion video prompt based on this:

{base}

Additional settings:
- Duration: {VIDEO_DURATIONS[video_duration]}
- Motion: {VIDEO_MOTIONS[video_motion]}
- Camera: {VIDEO_CAMERAS[video_camera]}
- Atmosphere: {VIDEO_ATMOSPHERES[video_atmosphere]}

Rules:
- Cinematic, photorealistic, 4K quality
- Focus on model movement and fashion
- Include lighting, mood, atmosphere details
- No text overlays, no watermarks
- Output ONLY the video prompt, 100-150 words"""}]
                )
                st.session_state.video_prompt = response.content[0].text.strip()
            except Exception as e:
                st.error(f"오류: {str(e)}")

    if st.session_state.video_prompt:
        st.text_area("생성된 영상 프롬프트", value=st.session_state.video_prompt, height=180)
        st.code(st.session_state.video_prompt, language=None)
        st.caption("👆 복사 후 Gemini 대화창 → Veo 3에 붙여넣으세요!")

        st.markdown("---")
        st.markdown("### 💡 Veo 3 사용 방법")
        st.markdown("""
1. [gemini.google.com](https://gemini.google.com) 접속
2. 좌측 **Veo 3** 선택
3. 위 프롬프트 붙여넣기
4. 생성 클릭!
        """)