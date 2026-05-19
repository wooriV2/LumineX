"""
LumineX Dashboard v3.2 - 스마트 랜덤 session_state+rerun 방식으로 수정
실행: streamlit run dashboard.py
"""

import sys
import random
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

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
.stApp { background-color: #080808 !important; }
[data-testid="stAppViewContainer"] { background-color: #080808 !important; }
[data-testid="stHeader"] { background-color: #080808 !important; }
[data-testid="stSidebar"] { background-color: #0f0f0f !important; border-right: 1px solid #1e1e1e !important; }
[data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label { color: #aaa !important; font-size: 0.78rem !important; }
[data-testid="stSidebar"] h3 { color: #8a6f30 !important; font-size: 0.65rem !important; letter-spacing: 2.5px !important; text-transform: uppercase !important; font-weight: 500 !important; }
h1, h2, h3 { color: #c9a84c !important; letter-spacing: 2px !important; }
h3 { font-size: 0.65rem !important; letter-spacing: 2.5px !important; text-transform: uppercase !important; color: #8a6f30 !important; }
.stTabs [data-baseweb="tab-list"] { background-color: transparent !important; border-bottom: 1px solid #1e1e1e !important; gap: 0 !important; }
.stTabs [data-baseweb="tab"] { background-color: transparent !important; color: #555 !important; font-size: 0.78rem !important; padding: 10px 20px !important; border-bottom: 2px solid transparent !important; }
.stTabs [aria-selected="true"] { color: #c9a84c !important; border-bottom: 2px solid #c9a84c !important; background-color: transparent !important; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none !important; }
.stSelectbox > div > div { background-color: #1c1c1c !important; border: 1px solid #333 !important; border-radius: 6px !important; color: #e0e0e0 !important; font-size: 0.8rem !important; transition: border-color 0.2s !important; }
.stSelectbox > div > div:hover { border-color: rgba(201,168,76,0.35) !important; }
.stSelectbox > div > div:focus-within { border-color: rgba(201,168,76,0.6) !important; box-shadow: 0 0 0 1px rgba(201,168,76,0.2) !important; }
.stSelectbox label { color: #c9a84c !important; font-size: 0.68rem !important; letter-spacing: 1.5px !important; text-transform: uppercase !important; font-weight: 500 !important; }
.stSelectbox [data-baseweb="select"] span, .stSelectbox [data-baseweb="select"] div, .stSelectbox [data-baseweb="select"] input { color: #ddd !important; }
[data-baseweb="popover"] [data-baseweb="menu"] { background-color: #1c1c1c !important; border: 1px solid #333 !important; }
[data-baseweb="popover"] li { background-color: #1c1c1c !important; color: #ccc !important; font-size: 0.8rem !important; }
[data-baseweb="popover"] li:hover { background-color: rgba(201,168,76,0.08) !important; color: #c9a84c !important; }
.stButton > button { border-radius: 6px !important; font-size: 0.75rem !important; letter-spacing: 1.5px !important; text-transform: uppercase !important; font-weight: 700 !important; transition: all 0.2s !important; height: 42px !important; }
.stButton > button[kind="primary"] { background: linear-gradient(135deg, #c9a84c, #a07830) !important; border: none !important; color: #000 !important; }
.stButton > button[kind="primary"]:hover { background: linear-gradient(135deg, #e8c96a, #c9a84c) !important; transform: translateY(-1px) !important; }
.stButton > button[kind="secondary"] { background: transparent !important; border: 1px solid rgba(201,168,76,0.4) !important; color: #c9a84c !important; }
.stButton > button[kind="secondary"]:hover { background: rgba(201,168,76,0.08) !important; border-color: rgba(201,168,76,0.7) !important; }
.stRadio > div { gap: 6px !important; }
.stRadio label { background: #111 !important; border: 1px solid #222 !important; border-radius: 6px !important; padding: 7px 12px !important; font-size: 0.78rem !important; color: #666 !important; cursor: pointer !important; transition: all 0.2s !important; }
.stRadio label:has(input:checked) { background: rgba(201,168,76,0.1) !important; border-color: rgba(201,168,76,0.4) !important; color: #c9a84c !important; }
.stTextArea textarea { background-color: #0d0d0d !important; color: #ccc !important; border: 1px solid #1e1e1e !important; border-radius: 6px !important; font-size: 0.78rem !important; line-height: 1.8 !important; }
.stTextArea textarea:focus { border-color: rgba(201,168,76,0.4) !important; box-shadow: 0 0 0 1px rgba(201,168,76,0.15) !important; }
.stCode { background-color: #0d0d0d !important; border: 1px solid rgba(201,168,76,0.2) !important; border-radius: 6px !important; }
.stCode code { color: #a8945a !important; font-size: 0.75rem !important; line-height: 1.8 !important; }
.stCode button { background: rgba(201,168,76,0.1) !important; border: 1px solid rgba(201,168,76,0.3) !important; color: #c9a84c !important; border-radius: 4px !important; }
[data-testid="stToggle"] > div { background-color: #c9a84c !important; }
.stAlert { background-color: #111 !important; border: 1px solid #222 !important; border-radius: 6px !important; color: #888 !important; font-size: 0.78rem !important; }
hr { border-color: #1e1e1e !important; margin: 12px 0 !important; }
.stCaption { color: #666 !important; font-size: 0.7rem !important; }
p, li, .stMarkdown { color: #bbb !important; font-size: 0.82rem !important; }
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #080808; }
::-webkit-scrollbar-thumb { background: #2a2a2a; border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: #8a6f30; }
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
    "🇰🇷 한국 — K-beauty, 하얀 피부, 또렷한 이목구비": "Korean beauty, fair porcelain skin, sharp elegant facial features, K-beauty aesthetic",
    "🇯🇵 일본 — J-beauty, 도자기 피부, 섬세한 이목구비": "Japanese beauty, porcelain delicate skin, refined subtle features, J-beauty aesthetic",
    "🇨🇳 중국 — 우아한 골격, 세련된 동양미": "Chinese beauty, elegant facial bone structure, sophisticated Eastern features",
    "🌏 동남아 — 골든 태닝, 이국적 태국/베트남 미녀": "Southeast Asian beauty, golden tan glowing skin, exotic Thai Vietnamese features",
    "🌙 중동 — 올리브 피부, 깊은 눈, 아라비안 뷰티": "Middle Eastern beauty, warm olive skin, deep dark sultry eyes, Arabian exotic features",
    "🇪🇺 유럽 — 백인, 강한 골격, 유러피안 미녀": "European Caucasian beauty, fair skin, strong bone structure, classic European features",
    "🇺🇸 미국 — 올아메리칸, 건강미, 애슬레틱": "All-American beauty, sun-kissed healthy skin, fresh athletic look, girl-next-door glamour",
    "💃 라틴 — 브론즈 태닝, 볼륨감, 브라질/콜롬비안": "Latina beauty, bronzed tan glowing skin, voluptuous curves, Brazilian Colombian exotic",
    "✨ 혼혈 — 이국적 믹스, 독특한 매력": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
    "🖤 흑인 — 짙은 피부, 강렬한 이목구비, 파워풀": "Black beauty, rich deep dark skin, powerful striking features, African goddess",
    "🇧🇷 브라질리언 — 브라질, 구릿빛 피부, 풍만한 글래머": "Brazilian beauty, bronzed tan skin, full voluptuous curves, tropical glamour",
    "🇨🇴 콜롬비안 — 콜롬비아, 이국적 라틴 미녀": "Colombian beauty, exotic Latin features, olive skin, sultry dark eyes",
    "🇸🇪 스칸디나비안 — 북유럽, 금발, 차갑고 우아한": "Scandinavian beauty, platinum blonde, ice blue eyes, tall elegant Nordic features",
    "🇷🇺 동유럽 — 슬라브 미녀, 강한 골격, 매혹적": "Eastern European beauty, Slavic features, high cheekbones, mysterious allure",
    "🇲🇦 모로칸 — 북아프리카, 이국적 중동+아프리카 믹스": "Moroccan beauty, exotic North African features, olive skin, dark almond eyes",
    "🇪🇬 이집트 — 클레오파트라 느낌, 강렬한 눈매": "Egyptian beauty, Cleopatra-like features, intense dark eyes, Mediterranean skin",
}

AGE_APPEARANCE = {
    "없음": "",
    "18-20 — 어린 성인, 청순한": "18-20 years old young adult, fresh youthful face, college age",
    "20대 초반 — 발랄하고 생기있는": "early 20s, vibrant youthful beauty, 21-24 years old",
    "20대 중반 — 전성기 글래머": "mid 20s, peak glamour beauty, 25-27 years old",
    "20대 후반 — 성숙미 시작": "late 20s, maturing beauty, 28-29 years old, sophisticated",
    "30대 초반 — 세련된 성숙미": "early 30s, refined mature beauty, 30-33 years old, elegant",
    "30대 중반 — 카리스마 있는": "mid 30s, charismatic mature glamour, 34-37 years old",
    "40대 — 우아한 중년 글래머": "40s, elegant mature woman, 40-49 years old, sophisticated glamour",
    "50대 — 실버 글래머": "50s, silver glamour, mature distinguished beauty, 50-59 years old",
    "60대+ — 우아한 시니어": "60s and above, gracefully aged beauty, senior glamour, distinguished",
}

MODEL_TYPES = {
    # ── 극초슬림 계열 ──
    "울트라 슬림 — 뼈가 보이는 하이패션": "ultra-thin high fashion model, very slender waif figure, barely visible small bust, extremely narrow hips, razor-thin silhouette, fashion week physique",
    "슈퍼 슬림 — 매우 마른 런웨이": "super slim runway model, very thin frame, minimal bust, narrow hips, elongated ultra-slender body, editorial thin",
    "슬림 런웨이 — 초장신 늘씬": "extremely tall runway model, impossibly long legs, ultra-slender waist, small A-cup bust, narrow hips, elongated silhouette",
    "슬림 엘레강스 — 날씬하고 우아한": "slender elegant model, slim narrow frame, small B-cup bust, slim narrow hips, graceful delicate figure",
    # ── 슬림톤 계열 ──
    "슬림 톤 — 날씬하고 탄탄한": "slim toned model, lean athletic build, flat stomach, small C-cup bust, slim toned hips, light but defined",
    "발레리나 — 길고 가늘고 우아한": "ballerina physique, extremely slender elongated figure, small bust, narrow hips, graceful elegant posture, dancer's perfect poise",
    "슬림 피트니스 — 날씬한 운동선수": "slim fitness model, lean defined muscles, flat abs, small C-cup bust, athletic slim hips, lightweight athletic",
    # ── 애슬레틱 계열 ──
    "피트니스 — 탄탄한 복근, 근육미": "athletic fitness model, defined six-pack abs, toned muscular legs, full C-cup bust, round athletic hips, powerful physique",
    "비키니 컴페티션 — 대회용 극강 근육": "bikini competition model, extremely defined muscles, shredded competition physique, full D-cup bust, round athletic hips, competition-ready body",
    "파워 피트니스 — 강한 근육미": "power fitness model, very muscular defined body, strong arms and legs, full D-cup bust, muscular round hips, powerful athletic build",
    "스포츠 글램 — 탄탄+볼륨": "sports glamour model, toned athletic body with curves, defined abs, full D-cup bust, round hips, fit and voluptuous",
    # ── 글래머 계열 ──
    "소프트 글램 — 부드러운 여성미": "soft glamour model, feminine gentle curves, full C-cup bust, round soft hips, elegant graceful figure, naturally beautiful",
    "VS 앤젤 — 완벽한 VS 글래머": "Victoria's Secret Angel, perfect full D-cup bust, toned flat abs, long legs, round hips, curvaceous yet athletic, runway perfect",
    "핫 글래머 — 잘록한 허리+볼륨": "hot glamour model, full DD-cup bust, extremely narrow cinched waist, very wide round hips, ultra hourglass figure",
    "슈퍼 글래머 — 극강 모래시계": "super glamour model, enormous F-cup bust overflowing, impossibly tiny waist, enormous wide round hips, maximum hourglass, pinup perfection",
    "럭셔리 글램 — 고급스러운 볼륨": "luxury glamour model, full DD-cup bust, defined waist, wide round hips, sophisticated voluptuous elegance, high-end glamour",
    # ── 커브 계열 ──
    "내추럴 커브 — 자연스러운 곡선미": "natural curvy model, naturally full C-cup bust, round natural hips, soft gentle curves, realistic womanly figure",
    "소프트 커브 — 부드럽고 풍만한": "soft curvy model, full D-cup bust, wide round hips, full soft thighs, gentle voluptuous curves, feminine warmth",
    "풀 커브 — 볼륨감 있는 커브": "full curvy model, very full DD-cup bust, very wide hips, full round thighs, voluptuous hourglass, abundant curves",
    "글래머 커브 — 커브+글래머 믹스": "glamour curvy model, large DD/F-cup bust, dramatic waist-to-hip ratio, very wide round hips, thick thighs, glamorous voluptuous",
    # ── 플러스사이즈 계열 ──
    "플러스 내추럴 — 자연스러운 플러스": "natural plus-size model, full bust, soft rounded belly, wide hips, full thighs, body positive natural figure, size 14-16",
    "플러스 글램 — 플러스사이즈 글래머": "plus-size glamour model, very full heavy bust, soft belly, wide full hips, thick thighs, confident voluptuous presence, size 16-18",
    "라지 플러스 — 매우 풍만한": "large plus-size model, large heavy bust, round protruding belly, very wide hips, heavy full thighs, abundant curves, size 20-22",
    "슈퍼 플러스 — 초풍만": "super plus-size model, enormous heavy bust, large soft belly rolls, extremely wide hips, very heavy thighs, massively full figure, size 24+",
    # ── BBW 계열 ──
    "BBW 글래머 — BBW 글래머": "BBW glamour model, massive full heavy bust, large protruding belly, very wide thick hips, heavy arms, chubby full thighs, 250 pound glamour figure",
    "라지 BBW — 큰 BBW": "large BBW model, very large heavy pendulous bust, large hanging belly with rolls, extremely wide hips, massive thighs, very heavy arms, 300+ pound figure",
    "슈퍼 BBW — 극도로 풍만한": "super BBW model, gigantic pendulous bust, no waist definition, massively obese figure, large apron belly with multiple rolls, enormous thighs, 400+ pound body",
    "슈퍼 BBW 글래머 — 극도로 풍만한 글래머": "super BBW glamour model, gigantic full bust, no waist definition, extremely wide thick torso, massively obese figure, apron belly hanging low, belly folds cascading, enormous thighs, very heavy arms, 400+ pound glamour",
}

# ── 보정 섹션 (MODEL_TYPES 미세조정용) ──
BODY_WEIGHT = {
    "없음": "",
    "슬림 톤 보정": "additionally slim toned, lean defined muscles, flat stomach",
    "오일드 볼륨 보정": "additionally oiled voluminous body, gleaming full curves",
    "근육 정의 보정": "additionally very muscular defined, visible muscle striations",
    "배 겹살 보정": "additionally large hanging belly with multiple rolls, apron belly",
    "허벅지 볼륨 보정": "additionally very thick heavy thighs, massive legs touching",
}

BUST_SIZE = {
    "없음": "",
    "플랫 보정": "additionally very flat chest, AA-cup, minimal breast tissue",
    "스몰 보정": "additionally small A-cup breasts, petite modest chest",
    "미디엄 보정": "additionally C-cup breasts, natural proportionate bust",
    "라지 보정": "additionally large DD-cup breasts, very full heavy bust, deep cleavage",
    "엑스라지 보정": "additionally extremely large DDD/F-cup breasts, massive heavy bust, barely contained",
    "슈퍼라지 보정": "additionally enormous G/H-cup breasts, gigantic heavy pendulous bust, overflowing",
    "글래머 보정": "additionally H/I/J-cup breasts, impossibly enormous bust, massively overflowing",
}

HIP_SIZE = {
    "없음": "",
    "플랫 보정": "additionally very flat hips, minimal buttocks, boyish lower body",
    "슬림 보정": "additionally slim narrow hips, small flat buttocks",
    "풀 보정": "additionally full round hips, prominent rounded buttocks, wide hip-to-waist ratio",
    "글래머 보정": "additionally dramatic hourglass hips, large round prominent buttocks, extreme curves",
    "브라질리언 보정": "additionally Brazilian-style enormous round buttocks, very large protruding rear, maximum gluteal volume",
    "엑스트림 보정": "additionally hyper-exaggerated curves, gigantic round protruding buttocks, impossibly curvy",
}

OUTFIT_TYPES = {
    "마이크로 비키니 — 끈 비키니, SI 수영복 화보": {
        "gemini": "micro string bikini, tiny triangle top, string thong bottom, minimal coverage, Sports Illustrated swimsuit style",
        "chatgpt": "designer string bikini, minimalist swimwear, Sports Illustrated editorial style",
    },
    "원피스 수영복 — 하이컷, 컷아웃 디자인": {
        "gemini": "high-cut one-piece swimsuit, bold cutouts, athletic glamour",
        "chatgpt": "high-cut designer one-piece swimsuit, artistic cutouts, Sports Illustrated style",
    },
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
    "코르셋 드레스 — 잘록한 허리, 볼륨감 강조": {
        "gemini": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "chatgpt": "fashion corset dress, cinched waist, dramatic neckline, haute couture style",
    },
    "브라탑+하이슬릿 — 브라탑, 롱 하이슬릿": {
        "gemini": "bra top, ultra-high slit skirt, maximum leg exposure, editorial",
        "chatgpt": "fashion bra top, high slit skirt, long leg emphasis, Vogue editorial",
    },
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
    "스포츠브라+레깅스 — 핫한 피트니스 룩": {
        "gemini": "sports bra, high-waist leggings, midriff bare, fitness editorial",
        "chatgpt": "athletic sports bra, high-waist leggings, fitness editorial, Sports Illustrated",
    },
    "모노키니 — 원피스 수영복 변형, 대담한 컷아웃": {
        "gemini": "monokini swimsuit, bold cutout one-piece, daring swimwear design",
        "chatgpt": "designer monokini, cutout one-piece swimsuit, bold editorial swimwear",
    },
    "웨딩 드레스 — 럭셔리 브라이달, 관능적": {
        "gemini": "luxurious wedding dress, plunging neckline bridal gown, sensual bridal fashion",
        "chatgpt": "luxury bridal gown, dramatic wedding dress, high fashion bridal editorial",
    },
    "코트 only — 롱코트만 입은 미니멀 글래머": {
        "gemini": "long coat only, nothing underneath, minimal glamour, coat barely covering",
        "chatgpt": "oversized long coat, minimalist glamour, fashion editorial coat look",
    },
    "가죽 재킷 + 란제리 — 엣지있는 레이어드": {
        "gemini": "leather jacket over lingerie, edgy layered look, rock glamour style",
        "chatgpt": "leather jacket with lingerie, edgy fashion editorial, bold layered style",
    },
}

ENVIRONMENTS = {
    "미니멀 스튜디오 — 흰 배경, 깔끔": "pure white minimalist studio, seamless backdrop",
    "두바이 펜트하우스 루프탑 — 야경": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
    "모나코 테라스 — 지중해 야경": "Monaco luxury terrace, Mediterranean night view, superyachts harbor",
    "베르사유 궁전 — 황금빛 홀": "Palace of Versailles golden hall, ornate chandeliers, luxury interior",
    "뉴욕 루프탑 — 맨하탄 야경": "New York City rooftop, Manhattan skyline at night, urban glamour",
    "파리 오스만 발코니 — 에펠탑 뷰": "Paris Haussmann balcony, Eiffel Tower view, golden hour",
    "럭셔리 인피니티 풀 — 열대 리조트": "luxury infinity pool edge, tropical resort, palm trees",
    "산토리니 절벽 — 에게해 야경": "Santorini cliff, blue dome church, Aegean sea at night",
    "말디브 수상빌라 — 크리스탈 바다": "Maldives overwater villa, crystal turquoise sea, tropical paradise",
    "리비에라 절벽 — 지중해 낮": "French Riviera cliff, azure Mediterranean sea, golden sunlight",
    "마이애미 비치 — 선셋": "Miami Beach sunset, Ocean Drive, warm pink sky",
    "럭셔리 요트 덱 — 지중해": "luxury superyacht deck, Mediterranean sea, ocean horizon",
    "도쿄 네온 거리 — 비 오는 밤": "Shinjuku neon-lit rainy alley, Tokyo cyberpunk night",
    "다크 바로크 — 화려한 실내": "dark baroque opulent chamber, velvet and gold interior",
    "파리 패션위크 런웨이 — 모던 무대": "Paris fashion week modernist runway stage, fashion show",
    "사하라 골든아워 — 황금빛 사막": "Sahara desert dunes, golden hour sunset, dramatic sky",
    "화산 절벽 — 극적인 자연": "dramatic volcanic cliff, stormy ocean, powerful nature",
    "얼음 동굴 — 크리스탈 블루": "ice cave interior, crystal blue formations, ethereal light",
    "부다페스트 온천 — 럭셔리 스파, 증기": "Budapest thermal bath, luxury spa pool, steam and warm water",
    "모로코 리야드 — 이슬람 아치, 타일": "Moroccan riad, ornate Islamic arches, colorful mosaic tiles",
    "싱가포르 인피니티 풀 — 마리나베이 뷰": "Singapore Marina Bay Sands infinity pool, city skyline view",
    "발리 정글 빌라 — 열대 럭셔리, 자연": "Bali jungle villa, tropical luxury, lush greenery, infinity pool",
    "모던 럭셔리 맨션 — 현대적 고급 저택": "modern luxury mansion interior, sleek contemporary design, high ceilings",
    "사이버펑크 네온 도시 — 미래 도시 거리": "cyberpunk neon city street, futuristic urban dystopia, neon signs",
    "미래 SF 복도 — 우주선/미래 건물": "futuristic sci-fi corridor, spaceship interior, glowing panels",
    "럭셔리 호텔 스위트 — 펜트하우스 스위트룸": "luxury hotel suite, penthouse bedroom, floor-to-ceiling windows",
    "빗속 도시 거리 — 비 오는 도시, 반사": "rain-soaked urban street, wet pavement reflections, city lights",
    "지중해 해변 마을 — 화이트 빌리지": "Mediterranean seaside village, white-washed buildings, blue sea",
    "자연 폭포 낙원 — 열대 폭포, 자연": "tropical forest waterfall paradise, lush jungle, cascading water",
    "설산 리조트 — 눈 덮인 산, 스키 럭셔리": "snow-covered mountain luxury resort, alpine chalet, winter scenery",
    "우아한 볼룸 — 샹들리에, 대형 파티홀": "elegant grand ballroom, crystal chandeliers, marble floors, opulent",
    "루프탑 도시 스카이라인 — 도시 전경": "rooftop city skyline, panoramic urban view, golden sunset",
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
    "크로셰 — 뜨개 수영복, 보헤미안": "crochet knit fabric, handmade boho swimwear style",
    "골드 체인 메쉬 — 금속 체인 망사": "gold chain mail mesh, metallic chainlink fabric",
    "페더 — 깃털 장식, 쇼걸 글래머": "feather-trimmed fabric, showgirl glamour, luxury plumes",
    "니트 — 몸에 딱 붙는 립 니트": "ribbed knit fabric, body-hugging stretch knit",
    "PVC — 투명 비닐, 미래적": "clear PVC vinyl, transparent plastic material, futuristic",
    "데님 — 청바지 소재, 캐주얼 섹시": "denim fabric, sexy denim, casual glamour",
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
    "문라이트 — 달빛, 신비로운 야외": "moonlight, silvery blue natural light, mysterious outdoor glow",
    "네온 핑크 — 핑크 단색 네온": "single pink neon light, hot pink glow, moody pink atmosphere",
    "파이어 — 불빛, 따뜻한 드라마틱": "firelight, warm flickering flames, dramatic orange glow",
    "수중 반사 — 수영장 물빛 반사": "underwater pool light reflection, rippling aqua light patterns",
    "스플릿 라이팅 — 얼굴 반반 명암": "split lighting, half face light half shadow, dramatic contrast",
}

CAMERA_ANGLES = {
    "전신샷 — 머리부터 발끝": "full body head-to-toe shot",
    "3/4 샷 — 허벅지까지": "3/4 body shot thigh to head",
    "웨이스트샷 — 상반신 집중": "waist-up shot upper body emphasis",
    "로우앵글 — 다리 강조, 아래서 위로": "low angle upward shot legs dramatically elongated",
    "클로즈업 — 얼굴+가슴 집중": "close-up beauty shot face and upper chest",
    "오버헤드 — 위에서 내려다보기": "overhead top-down angle, bird's eye view",
    "사이드 프로필 — 옆모습 실루엣": "side profile shot, elegant silhouette from the side",
    "백샷 — 뒤에서 촬영, 등 강조": "back view shot, looking over shoulder, spine emphasis",
    "익스트림 클로즈업 — 얼굴만 극접사": "extreme close-up face only, skin texture detail",
}

FOOTWEAR = {
    "없음": "",
    "스틸레토 힐 — 극도로 높은 힐": "wearing extreme stiletto heels, legs elongated",
    "스트래피 샌들 힐 — 얇은 끈 샌들 힐": "wearing strappy high heel sandals, elegant feet",
    "플랫폼 부츠 — 두꺼운 솔, 파워풀": "wearing platform boots, powerful stance",
    "무릎까지 부츠 — 니하이 부츠": "wearing knee-high boots, sexy long legs",
    "허벅지까지 부츠 — 싸이하이 부츠": "wearing thigh-high boots, ultra sexy",
    "포인티드 토 힐 — 뾰족한 앞코 힐": "wearing pointed toe stiletto pumps, classic glamour",
    "글래디에이터 샌들 — 끈이 종아리까지": "wearing gladiator sandals, lace-up straps up the calf",
    "뮬 힐 — 뒤가 없는 슬링백 힐": "wearing mule heels, backless slip-on stiletto",
    "크리스탈 힐 — 반짝이는 투명 힐": "wearing crystal clear transparent heels",
    "맨발 — 자연스러운": "barefoot, natural",
}

CAMERAS = {
    "하셀블라드 H6D — 80mm f/2.8": "Hasselblad H6D 80mm f/2.8 ISO 100",
    "캐논 EOS R5 — 85mm f/1.2 인물": "Canon EOS R5 85mm f/1.2 portrait lens ISO 100",
    "소니 A7R V — 50mm f/1.4": "Sony A7R V 50mm f/1.4 ISO 100",
    "니콘 Z9 — 85mm f/1.8": "Nikon Z9 85mm f/1.8 ISO 100",
    "페이즈원 XF IQ4 — 110mm f/2.8 중형": "Phase One XF IQ4 110mm f/2.8 medium format ISO 50",
    "라이카 SL2 — 50mm f/1.4 독일 감성": "Leica SL2 50mm f/1.4 Summilux, German precision",
    "후지 GFX 100S — 중형 110mm": "Fujifilm GFX 100S 110mm f/2 medium format",
    "아이폰 시네마틱 — 모바일 시네마틱 모드": "iPhone cinematic mode, natural realistic style",
}

HAIR_STYLES = {
    "없음": "",
    "롱 웨이브 — 긴 웨이브, 볼륨감": "long wavy hair, voluminous waves, flowing",
    "롱 스트레이트 — 긴 생머리, 실키": "long straight silky hair, sleek and smooth",
    "하이 포니테일 — 높은 포니테일, 섹시": "high ponytail, sleek tight ponytail, sexy",
    "업스타일 — 올린 머리, 우아한": "elegant updo, sophisticated chignon, classic",
    "단발 — 깔끔한 보브컷": "sleek bob cut, sharp jawline bob",
    "웨이브 하프업 — 반묶음 웨이브": "half-up half-down wavy hair, romantic style",
    "빅 볼륨 — 풍성하고 글래머러스": "big voluminous glamorous hair, full body",
    "웻룩 — 젖은 듯한 윤기": "wet look slicked back hair, glossy and sleek",
    "바람에 날리는 — 역동적인 플로잉": "windswept flowing hair, dynamic movement",
    "브레이드 — 땋은 머리, 보헤미안": "braided hair, bohemian braids, artistic weave",
    "크롭 픽시컷 — 짧고 대담한": "short pixie cut, bold cropped hair, edgy chic",
    "코르넬로 — 뿔 모양 아방가르드": "avant-garde horn updo, sculptural hair art, editorial",
    # ── 추가 ──
    "프렌치 보브 — 클래식 파리지앵 단발": "French bob, classic Parisian chin-length cut, sleek fringe",
    "울프컷 — 레이어드 섹시 울프": "wolf cut, layered shaggy style, curtain bangs, effortless sexy",
    "스택드 보브 — 뒤짧고 앞긴 엣지 단발": "stacked bob, shorter back longer front, edgy angled cut",
    "컬리 비치웨이브 — 해변 곱슬 웨이브": "curly beach waves, natural tousled curls, sun-kissed texture",
    "슬릭백 올백 — 뒤로 완전히 넘긴": "sleek slicked back hair, pulled back tight, wet gel look",
    "루즈 업도 — 흘러내리는 웨이브 업": "loose romantic updo, soft tendrils falling, undone elegance",
    "스포티 번 — 높은 번 헤어": "high messy bun, sporty topknot, casual athletic chic",
    "사이드 스웹 — 한쪽으로 넘긴 글래머": "side-swept hair, dramatic one-side drape, old Hollywood glamour",
}

HAIR_COLORS = {
    "없음": "",
    "블랙 — 짙은 검정": "jet black hair, deep dark black",
    "다크 브라운 — 짙은 갈색": "dark brown hair, rich chocolate brown",
    "라이트 브라운 — 밝은 갈색": "light brown hair, warm caramel brown",
    "골든 블론드 — 황금빛 금발": "golden blonde hair, sun-kissed golden",
    "플래티넘 블론드 — 밝은 백금 금발": "platinum blonde hair, icy white blonde",
    "레드 — 붉은 빨간 머리": "red hair, vibrant auburn red",
    "버건디 — 와인빛 다크 레드": "burgundy hair, deep wine dark red",
    "로즈골드 — 핑크빛 골드": "rose gold hair, pink golden shimmer",
    "오닉스 블루블랙 — 블루 광택 검정": "blue-black hair, onyx with blue sheen",
}

MODEL_COUNT = {
    "1명 — 싱글 모델 (기본)": {"count": 1, "prompt": "A stunning female model"},
    "2명 — 듀오, 두 모델 나란히": {"count": 2, "prompt": "Two stunning female models standing together side by side"},
    "2명 — 듀오, 대비되는 포즈": {"count": 2, "prompt": "Two stunning female models, contrasting poses, one in foreground one behind"},
    "3명 — 트리오, 세 모델": {"count": 3, "prompt": "Three stunning female models posing together, trio fashion editorial"},
    "그룹 — VS 런웨이 그룹샷": {"count": 4, "prompt": "Group of stunning female models on runway, Victoria's Secret fashion show group shot"},
}

ERA = {
    "없음": "",
    "현대 — 2020년대 트렌디": "contemporary 2020s fashion, modern trendy style",
    "레트로 80s — 네온, 빅헤어, 글램록": "retro 1980s fashion, neon colors, big hair, glam rock era",
    "레트로 90s — 슈퍼모델 황금시대": "1990s supermodel era, minimalist chic",
    "빅토리안 — 코르셋, 드라마틱": "Victorian era fashion, dramatic corset, ornate period costume",
    "1920s 플래퍼 — 재즈시대 글래머": "1920s flapper era, art deco glamour, jazz age fashion",
    "미래 2100년 — SF 하이테크": "year 2100 futuristic fashion, high-tech sci-fi costume",
    "고대 그리스 — 여신 드레이핑": "ancient Greek goddess, draped fabric, classical mythology aesthetic",
}

CONCEPT = {
    "없음": "",
    "CEO 글래머 — 파워수트, 강한 여성": "powerful CEO glamour, sharp power suit, dominant businesswoman",
    "악당 빌런 — 다크 글래머, 카리스마": "villain dark glamour, evil seductive charisma, dark queen energy",
    "여전사 — 갑옷+글래머 융합": "warrior goddess, glamorous armor, fierce battle-ready beauty",
    "팝스타 — 무대 의상, 공연 에너지": "pop star stage costume, performance energy, concert glamour",
    "비밀요원 — 스파이 글래머, 미스터리": "secret agent spy glamour, mysterious sleek operative, femme fatale",
    "여신 — 신화적 존재, 초월적 아름다움": "mythological goddess, ethereal divine beauty, supernatural aura",
    "뱀파이어 — 다크 불멸의 존재": "vampire dark immortal beauty, gothic supernatural elegance",
    "인어 — 바다의 여신": "mermaid ocean goddess, aquatic beauty, sea creature glamour",
    "천사 — 천상의 존재": "angel celestial beauty, ethereal divine wings, heavenly glamour",
    "마녀 — 마법사 글래머": "witch magical glamour, mystical sorceress, dark magic beauty",
}

SPECIAL_EFFECTS = {
    "없음": "",
    "불꽃 — 주변에 불이 타오르는": "surrounded by flames and fire, dramatic fire effects",
    "물 — 물에 젖거나 물속 장면": "water effects, soaking wet, underwater or water splashing",
    "연기 — 드라이아이스 안개": "dry ice smoke effects, mysterious fog surrounding model",
    "꽃비 — 꽃잎이 날리는": "flower petals raining down, blooming flowers surrounding",
    "번개 — 번개가 치는 배경": "lightning strike background, electric energy, storm effects",
    "우주 — 별빛, 은하수 배경": "galaxy and stars background, cosmic universe, nebula effects",
    "거울 파편 — 깨진 거울 조각": "broken mirror shards floating, glass fragments effect",
    "황금 — 황금 가루가 날리는": "golden dust particles floating, gilded shimmer effect",
    "얼음 — 얼음 결정, 냉기": "ice crystal effects, frozen breath, winter frost magic",
    "네온 빛줄기 — 네온 레이저 빛": "neon laser light beams, colorful light rays cutting through",
}

IMAGE_STYLE = {
    "없음": "",
    "하이퍼리얼 — 극사실주의 사진": "hyperrealistic photography, ultra-detailed photorealism",
    "오일페인팅 — 유화 회화 느낌": "oil painting style, painterly brushstrokes, fine art aesthetic",
    "필름누아르 — 1940s 흑백 시네마": "film noir style, 1940s black and white cinema, dramatic shadows",
    "팝아트 — 앤디워홀 스타일": "pop art style, Andy Warhol inspired, bold graphic colors",
    "수채화 — 부드러운 수채화": "watercolor painting style, soft translucent washes",
    "만화 — 코믹북 스타일": "comic book style, graphic novel illustration, bold outlines",
    "3D 렌더링 — CGI 퀄리티": "3D rendered CGI quality, Unreal Engine photorealistic render",
    "글리치 아트 — 디지털 왜곡": "glitch art effect, digital distortion, cyberpunk pixel corruption",
    "더블 익스포저 — 이중 노출": "double exposure photography, overlapping silhouette effect",
    "타블로 — 르네상스 명화 스타일": "Renaissance painting tableau, classical masterpiece composition",
}

PROPS = {
    "없음": "",
    "스포츠카 — 페라리/람보르기니": "posing with Ferrari or Lamborghini sports car, luxury supercar",
    "오토바이 — 바이크 위에": "sitting on motorcycle, biker glamour, powerful motorbike",
    "말 — 승마 글래머": "with horse, equestrian glamour, majestic stallion",
    "의자 — 럭셔리 체어 포즈": "with luxury chair, seated or draped over elegant furniture",
    "우산 — 비 오는 날 우산": "holding umbrella in rain, elegant rainy day accessory",
    "꽃다발 — 화려한 꽃": "holding large flower bouquet, floral luxury arrangement",
    "검/칼 — 여전사 무기": "holding sword or blade, warrior weapon, powerful stance",
    "샴페인 — 럭셔리 파티": "holding champagne glass, luxury party celebration",
    "고양이 — 팜므파탈과 고양이": "with elegant cat, femme fatale and feline, mysterious companion",
    "거울 — 손거울 들고": "holding ornate mirror, self-reflection pose, vanity glamour",
}

MAKEUP = {
    "없음": "",
    "스모키 아이 — 강렬한 눈매": "dramatic smoky eye makeup, dark eyeshadow, intense gaze",
    "누드 글램 — 자연스럽고 섹시한": "nude glam makeup, natural yet sexy, glossy lips, subtle glow",
    "레드립 — 클래식 빨간 입술": "classic red lip makeup, bold red lipstick, timeless glamour",
    "글리터 글램 — 반짝이는 파티": "glitter glam makeup, sparkling eyeshadow, festival beauty",
    "노메이크업 — 청순 내추럴": "no-makeup natural look, fresh dewy skin, barely-there beauty",
    "고딕 다크 — 다크 립, 페일 스킨": "gothic dark makeup, black or deep plum lips, pale dramatic skin",
    "메탈릭 아이 — 금속빛 아이섀도우": "metallic eye makeup, chrome silver or gold eyeshadow, futuristic",
    "선번 글로우 — 여름 태양 느낌": "sun-kissed glow makeup, bronzed healthy skin, summer radiance",
    "코랄 핑크 — 발랄하고 귀여운": "coral pink makeup, fresh peachy tones, youthful glow",
    "오렌지 팝 — 트렌디한 컬러풀": "bold orange makeup, trendy color pop, fashion editorial look",
    "캣아이 — 날카로운 아이라인": "sharp cat eye liner, winged eyeliner, feline sexy look",
    "홀로그램 — 아방가르드 미래적": "holographic makeup, iridescent highlights, avant-garde editorial",
}

ACCESSORIES = {
    "없음": "",
    "골드 주얼리 — 목걸이+귀걸이": "gold jewelry set, gold necklace and earrings, luxury accessories",
    "다이아몬드 — 럭셔리 다이아 주얼리": "diamond jewelry, sparkling diamond necklace and earrings, ultra luxury",
    "초커 — 섹시한 목 초커": "choker necklace, sexy neck choker, edgy accessory",
    "바디체인 — 몸에 두르는 골드 체인": "gold body chain, draped across torso, glamorous body jewelry",
    "레이어드 체인 — 여러 겹 목걸이": "layered chain necklaces, multiple gold chains, trendy stacked look",
    "진주 — 클래식 우아한 진주": "pearl jewelry, classic pearl necklace and earrings, timeless elegance",
    "크리스탈 — 반짝이는 크리스탈": "crystal jewelry, sparkling rhinestone accessories, glamorous",
    "귀걸이만 — 드라마틱한 드롭 귀걸이": "statement drop earrings only, dramatic dangling earrings",
    "럭셔리 워치 — 명품 시계": "luxury watch, designer timepiece on wrist, status accessory",
    "팔찌 스택 — 여러 겹 팔찌": "stacked bracelets, multiple bangles and cuffs on wrist",
}

SKIN_TONES = {
    "없음": "",
    "오일드 스킨 — 윤기있는 글로시": "oiled glossy skin, shiny wet-look skin, body oil gleaming",
    "태닝 — 브론즈 골든 태닝": "bronzed tan skin, golden sun-kissed tan, beach goddess",
    "딥 태닝 — 짙은 초콜릿 태닝": "deep dark tan, rich chocolate bronzed skin, intense tanning",
    "페일 — 창백하고 신비로운": "pale porcelain skin, ethereal fair complexion, mysterious allure",
    "글로우 — 발광하는 빛나는 피부": "luminous glowing skin, radiant inner glow, lit-from-within effect",
    "매트 — 무광 세련된 피부": "matte flawless skin, powdery smooth complexion, editorial finish",
    "듀이 — 촉촉하고 생기있는": "dewy fresh skin, hydrated plump complexion, youthful glow",
    "스웨티 — 운동 후 땀나는 느낌": "sweaty glistening skin, post-workout sheen, athletic perspiration",
    "프로스티 — 차갑고 얼음같은": "frosty icy skin tone, cold ethereal complexion, winter goddess",
}

POSES = {
    "없음": "",
    # ── 스탠딩 계열 ──
    "파워 스탠딩 — 손 허리, 당당한": "powerful standing pose, hands on hips, confident dominant stance",
    "런웨이 워킹 — 카메라를 향해": "walking confidently toward camera, runway catwalk stride",
    "걸어가는 뒷모습 — 카메라 등지고 걷기": "walking away from camera, back view, confident stride, looking over shoulder",
    "S커브 — 한쪽 다리 구부린 섹시": "sexy S-curve pose, one leg bent, hip tilted, sultry stance",
    "크로스 암 — 팔짱 끼고 강렬한": "arms crossed, intense gaze, powerful commanding expression",
    "손 들어 — 머리 위로 손, 관능적": "arms raised above head, sensual elongated pose, arched back",
    "기둥 포즈 — 기둥 감싸며 기댄": "leaning against pillar, arms wrapped around column, seductive lean",
    # ── 기대기 계열 ──
    "기댄 포즈 — 벽에 기댄 캐주얼": "leaning against wall, casual yet sexy pose, relaxed confidence",
    "창문 기대기 — 창문에 손 짚고 빛 받으며": "leaning against window, hand pressed on glass, backlit silhouette, dreamy glow",
    "차 위 포즈 — 보닛에 기댄 글래머": "leaning on car hood, luxury supercar, sultry glamour pose",
    # ── 앉기 계열 ──
    "앉은 포즈 — 바닥/의자에 우아하게": "seated elegantly, legs crossed, sophisticated sitting pose",
    "땅에 앉기 — 무릎 세우고 바닥에": "sitting on floor, knees drawn up, casual intimate pose",
    "계단 포즈 — 계단에 앉거나 기댄": "seated or leaning on staircase steps, architectural glamour",
    # ── 눕기 계열 ──
    "누운 포즈 — 바닥/침대에 관능적": "lying down pose, reclined on floor or bed, sensual and languid",
    "엎드린 포즈 — 배를 깔고 관능적": "lying face down, propped on elbows, arched back, looking at camera",
    # ── 뒷모습 계열 ──
    "백포즈 — 뒤돌아 어깨 너머 시선": "back to camera, looking over shoulder seductively",
    "등 보이기 — 백뷰, 어깨 라인": "back view pose, spine visible, shoulder blade emphasis",
    # ── 역동적 계열 ──
    "역동적 — 머리카락 날리는 움직임": "dynamic pose, hair flowing in wind, motion blur effect",
    "스트레칭 — 몸을 길게 늘인 유연한": "full body stretch pose, elongated limbs, graceful flexibility, dancer energy",
    "점프 — 공중에 뜬 역동적": "mid-air jump pose, feet off ground, dynamic energy, motion captured",
    # ── 수중/풀 계열 ──
    "수영장 입수 — 물가에서 다이빙": "standing at pool edge, about to dive, water reflection below",
    "수영장 물속 — 하반신 물에 잠긴": "standing waist-deep in pool, water surface at hips, wet glistening body",
    "욕조 포즈 — 욕조 안 럭셔리": "reclining in luxury bathtub, bubbles or petals, spa glamour",
    # ── 얼굴/클로즈업 계열 ──
    "손으로 얼굴 감싸기 — 양손으로 얼굴": "hands framing face, fingers touching cheeks, intimate beauty pose",
    "턱 괴기 — 손으로 턱 받치고": "chin resting on hand, thoughtful seductive gaze, close-up ready",
    "거울 앞 — 거울 반영, 이중 시선": "standing before mirror, reflection visible, double perspective pose",
}

# ── 날씨/기상 ──
WEATHER = {
    "없음": "",
    "맑음 — 강한 햇살, 선명한 그림자": "bright sunny day, strong sunlight, sharp shadows, clear blue sky",
    "골든아워 — 석양 직전 황금빛": "golden hour just before sunset, warm amber light flooding the scene",
    "흐림 — 부드러운 확산광, 무드있는": "overcast sky, soft diffused light, moody atmospheric feel",
    "비 — 빗속, 젖은 바닥 반사": "raining, wet ground reflections, rain droplets, dramatic rain atmosphere",
    "폭우 — 거센 비, 극적인 분위기": "heavy downpour, intense rain, dramatic storm, soaking wet everything",
    "안개 — 신비로운 안개, 몽환적": "dense fog, mysterious misty atmosphere, ethereal soft focus background",
    "눈 — 눈 내리는, 겨울 분위기": "snowfall, snowflakes falling, winter atmosphere, breath visible in cold air",
    "번개/폭풍 — 극적인 폭풍우": "lightning storm, dramatic storm clouds, electric atmosphere, intense weather",
    "바람 — 강한 바람, 옷과 머리 날림": "strong wind, clothes and hair dramatically blown, dynamic wind effect",
    "황사/모래폭풍 — 사막 먼지 분위기": "sandstorm dust haze, desert wind, warm orange dusty atmosphere",
    "무지개 — 비 온 뒤 무지개": "rainbow after rain, fresh air, vibrant colors in sky, hopeful atmosphere",
}

# ── 표정/눈빛 ──
EXPRESSION = {
    "없음": "",
    "도발적 — 강렬하고 유혹적인 눈빛": "seductive provocative gaze, smoldering eyes, sultry expression, lips slightly parted",
    "차가운 — 무표정, 냉한 카리스마": "cold expressionless face, icy stare, aloof powerful charisma, stone cold beauty",
    "당당한 — 자신감 넘치는 눈빛": "confident powerful expression, direct commanding gaze, dominant energy",
    "미소 — 부드러운 매혹적 미소": "soft alluring smile, gentle warm expression, approachable glamour",
    "활짝 웃음 — 환한 밝은 미소": "bright radiant smile, joyful expression, teeth showing, infectious happiness",
    "청순 — 순수하고 맑은 눈빛": "innocent pure expression, wide bright eyes, fresh youthful look, doe-eyed",
    "신비로운 — 알 수 없는 표정": "mysterious enigmatic expression, subtle smirk, secretive knowing look",
    "관능적 — 반쯤 감은 눈, 육감적": "half-lidded sensual eyes, heavy-lidded gaze, deeply seductive expression",
    "강렬한 — 눈을 부릅뜨고 압도하는": "intense piercing stare, powerful overwhelming gaze, magnetic eye contact",
    "우수 — 슬프고 몽환적인 눈빛": "melancholic dreamy expression, faraway gaze, wistful beauty",
    "화난 — 강렬한 분노, 악당 느낌": "fierce angry expression, villainous intensity, dark powerful rage",
    "입술 벌림 — 입술 살짝 열린": "lips slightly parted, open mouth, breathless expression, editorial beauty",
}

# ── 문신/바디아트 ──
TATTOO = {
    "없음": "",
    "슬리브 타투 — 한쪽 팔 전체 문신": "full sleeve tattoo on one arm, intricate detailed ink art",
    "목 타투 — 목 옆 작은 문신": "small delicate neck tattoo, side of neck ink",
    "가슴 타투 — 가슴 위 문신": "chest tattoo above bust, decorative upper chest ink",
    "등 타투 — 등 전체 대형 문신": "large back tattoo, full back ink art, intricate spine tattoo",
    "허리 타투 — 허리 옆 타투": "hip/waist tattoo, lower side tattoo, sensual placement",
    "손 타투 — 손등/손가락 문신": "hand and finger tattoos, knuckle ink, delicate hand art",
    "꽃 타투 — 플로럴 패턴": "floral tattoo pattern, rose and botanical ink, feminine tattoo art",
    "기하학 타투 — 선명한 기하학적": "geometric tattoo, clean line art, minimalist geometric ink",
    "뱀 타투 — 뱀 문양, 엣지있는": "snake tattoo, serpent ink art, edgy mystical tattoo",
    "천사/악마 타투 — 종교적 아트워크": "angel or demon tattoo, religious iconography ink, dramatic body art",
    "부족 타투 — 폴리네시안/마오리": "tribal tattoo, Polynesian Maori style ink, bold black patterns",
    "전신 바디페인팅 — 몸에 그림": "full body painting art, painted skin, artistic body art canvas",
}

# ── 바디 오일/글로스 강도 ──
BODY_OIL = {
    "없음": "",
    "라이트 글로우 — 자연스러운 윤기": "light natural skin glow, subtle healthy sheen, barely-there luminosity",
    "새틴 글로우 — 새틴처럼 빛나는": "satin skin finish, smooth silky sheen, elegant glow",
    "미디엄 오일 — 적당한 오일감": "medium body oil, moderate skin glistening, healthy oiled appearance",
    "하이 글로스 — 강한 오일, 반짝이는": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
    "익스트림 웻룩 — 물에 젖은 듯한": "extreme wet-look skin, soaking wet glistening appearance, dripping oil effect",
    "선탠 오일 — 골든 태닝 오일": "tanning oil sheen, golden bronzed glistening skin, beach goddess oil",
    "메탈릭 글로스 — 금속빛 광택": "metallic body gloss, chrome-like skin sheen, futuristic metallic finish",
    "스웨티 글로스 — 땀+오일 믹스": "sweaty oiled skin, post-workout glistening, athletic perspiration mixed with oil",
}

# ── 배경 인물 ──
BG_CROWD = {
    "없음": "",
    "완전 단독 — 배경에 아무도 없음": "completely alone, empty background, solitary subject, no other people",
    "흐릿한 군중 — 배경에 흐릿한 사람들": "blurred crowd in background, busy environment, bokeh people, social scene",
    "런웨이 관중 — 패션쇼 관중석": "fashion show audience in background, runway crowd, photographers flashing",
    "파티 군중 — 화려한 파티 배경": "glamorous party crowd in background, celebratory atmosphere, luxury event",
    "도시 행인 — 거리의 지나가는 사람들": "urban pedestrians blurred in background, busy city street life",
    "해변 군중 — 해변의 사람들": "beach crowd in background, summer beach scene, vacationers blurred",
    "두 명 — 다른 모델 한 명 배경에": "another model blurred in background, duo scene, second figure",
    "그림자 인물 — 배경에 실루엣만": "shadowy silhouette figures in background, mysterious dark outlines",
}

COLOR_GRADES = {
    "없음": "",
    "흑백 — 클래식 모노크롬": "black and white photography, classic monochrome, high contrast B&W",
    "시네마틱 틸 & 오렌지 — 영화적": "cinematic teal and orange color grade, Hollywood film look",
    "골든 — 따뜻한 황금빛 필름": "warm golden film grade, vintage golden hour tone",
    "다크 무드 — 어둡고 드라마틱": "dark moody color grade, deep shadows, dramatic contrast",
    "쿨 블루 — 차갑고 세련된": "cool blue color grade, cold steel tones, sleek editorial",
    "핑크 글램 — 핑크빛 글래머": "soft pink glamour grade, rose gold tones, feminine glow",
    "하이키 — 밝고 화사한 흰빛": "high key bright white tone, overexposed glamour, clean light",
    "빈티지 필름 — 필름 느낌": "vintage film grain, faded colors, analog photography look",
}


def build_gemini_prompt(data: dict, aspect: str, realism: bool) -> str:
    aspect_desc   = ASPECT_RATIOS.get(aspect, "")
    realism_kw    = "photorealistic, RAW photo, hyperrealistic, natural skin texture, pore detail, film grain, professional photographer" if realism else ""
    appearance    = MODEL_APPEARANCE.get(data.get('appearance', ''), '')
    age           = AGE_APPEARANCE.get(data.get('age', ''), '')
    outfit_data   = OUTFIT_TYPES[data['outfit']]
    outfit        = outfit_data["gemini"] if isinstance(outfit_data, dict) else outfit_data
    footwear      = FOOTWEAR.get(data.get('footwear', ''), '')
    pose          = POSES.get(data.get('pose', ''), '')
    color_grade   = COLOR_GRADES.get(data.get('color_grade', ''), '')
    hair_style    = HAIR_STYLES.get(data.get('hair_style', ''), '')
    hair_color    = HAIR_COLORS.get(data.get('hair_color', ''), '')
    hair_str      = " ".join(filter(None, [hair_color, hair_style]))
    makeup        = MAKEUP.get(data.get('makeup', ''), '')
    accessories   = ACCESSORIES.get(data.get('accessories', ''), '')
    skin_tone     = SKIN_TONES.get(data.get('skin_tone', ''), '')
    count_data    = MODEL_COUNT.get(data.get('model_count', '1명 — 싱글 모델 (기본)'), MODEL_COUNT['1명 — 싱글 모델 (기본)'])
    model_subject = count_data['prompt']
    era           = ERA.get(data.get('era', ''), '')
    concept       = CONCEPT.get(data.get('concept', ''), '')
    special_fx    = SPECIAL_EFFECTS.get(data.get('special_effects', ''), '')
    img_style     = IMAGE_STYLE.get(data.get('image_style', ''), '')
    props         = PROPS.get(data.get('props', ''), '')
    body_weight   = BODY_WEIGHT.get(data.get('body_weight', ''), '')
    bust_size     = BUST_SIZE.get(data.get('bust_size', ''), '')
    hip_size      = HIP_SIZE.get(data.get('hip_size', ''), '')
    body_str      = ", ".join(filter(None, [body_weight, bust_size, hip_size]))
    weather       = WEATHER.get(data.get('weather', ''), '')
    expression    = EXPRESSION.get(data.get('expression', ''), '')
    tattoo        = TATTOO.get(data.get('tattoo', ''), '')
    body_oil      = BODY_OIL.get(data.get('body_oil', ''), '')
    bg_crowd      = BG_CROWD.get(data.get('bg_crowd', ''), '')

    parts = [
        f"Professional fashion photograph, {CAMERA_ANGLES[data['angle']]}, model fills the entire frame.",
        f"{model_subject}: {MODEL_TYPES[data['model']]}{', ' + appearance if appearance else ''}.",
        f"Age: {age}." if age else "",
        f"Body adjustment: {body_str}." if body_str else "",
        f"Era: {era}." if era else "",
        f"Concept: {concept}." if concept else "",
        f"Expression: {expression}." if expression else "",
        f"Skin: {skin_tone}." if skin_tone else "",
        f"Body oil: {body_oil}." if body_oil else "",
        f"Tattoo/Body art: {tattoo}." if tattoo else "",
        f"Hair: {hair_str}." if hair_str else "",
        f"Makeup: {makeup}." if makeup else "",
        f"Accessories: {accessories}." if accessories else "",
        f"Props: {props}." if props else "",
        f"Pose: {pose}." if pose else "",
        f"Wearing: {outfit}, made of {MATERIALS[data['material']]}{', ' + footwear if footwear else ''}.",
        f"Environment: {ENVIRONMENTS[data['env']]}, background softly blurred bokeh.",
        f"Weather: {weather}." if weather else "",
        f"Background: {bg_crowd}." if bg_crowd else "",
        f"Special effects: {special_fx}." if special_fx else "",
        f"Lighting: {LIGHTING[data['light']]}.",
        f"Style reference: {STYLES[data['style']]}.",
        f"Image style: {img_style}." if img_style else "",
        f"Camera: {CAMERAS[data['camera']]}, sharp focus on model.",
        f"Color grade: {color_grade}." if color_grade else "",
    ]
    suffix = []
    if realism_kw: suffix.append(realism_kw)
    if aspect_desc: suffix.append(aspect_desc)
    suffix.append("model is the absolute primary subject, tight framing, background secondary")
    return " ".join(filter(None, parts)) + " " + ", ".join(suffix) + "."


def build_chatgpt_prompt(data: dict, aspect: str) -> str:
    aspect_map    = {"세로 2:3 — 인물 기본": "vertical portrait 2:3", "세로 3:4 — 전신샷": "vertical portrait 3:4", "가로 16:9 — 시네마틱": "wide cinematic 16:9", "가로 4:3 — 화보": "wide editorial 4:3", "정방형 1:1 — 인스타": "square format 1:1"}
    aspect_desc   = aspect_map.get(aspect, "vertical portrait 2:3")
    appearance    = MODEL_APPEARANCE.get(data.get('appearance', ''), '')
    age           = AGE_APPEARANCE.get(data.get('age', ''), '')
    model         = MODEL_TYPES[data['model']]
    outfit_data   = OUTFIT_TYPES[data['outfit']]
    outfit        = outfit_data["chatgpt"] if isinstance(outfit_data, dict) else outfit_data
    material      = MATERIALS[data['material']]
    env           = ENVIRONMENTS[data['env']]
    light         = LIGHTING[data['light']]
    style         = STYLES[data['style']]
    camera        = CAMERAS[data['camera']]
    angle         = CAMERA_ANGLES[data['angle']]
    footwear      = FOOTWEAR.get(data.get('footwear', ''), '')
    pose          = POSES.get(data.get('pose', ''), '')
    color_grade   = COLOR_GRADES.get(data.get('color_grade', ''), '')
    hair_style    = HAIR_STYLES.get(data.get('hair_style', ''), '')
    hair_color    = HAIR_COLORS.get(data.get('hair_color', ''), '')
    hair_str      = " ".join(filter(None, [hair_color, hair_style]))
    makeup        = MAKEUP.get(data.get('makeup', ''), '')
    accessories   = ACCESSORIES.get(data.get('accessories', ''), '')
    skin_tone     = SKIN_TONES.get(data.get('skin_tone', ''), '')
    count_data    = MODEL_COUNT.get(data.get('model_count', '1명 — 싱글 모델 (기본)'), MODEL_COUNT['1명 — 싱글 모델 (기본)'])
    model_subject = count_data['prompt']
    era           = ERA.get(data.get('era', ''), '')
    concept       = CONCEPT.get(data.get('concept', ''), '')
    special_fx    = SPECIAL_EFFECTS.get(data.get('special_effects', ''), '')
    img_style     = IMAGE_STYLE.get(data.get('image_style', ''), '')
    props         = PROPS.get(data.get('props', ''), '')
    body_weight   = BODY_WEIGHT.get(data.get('body_weight', ''), '')
    bust_size     = BUST_SIZE.get(data.get('bust_size', ''), '')
    hip_size      = HIP_SIZE.get(data.get('hip_size', ''), '')
    body_str      = ", ".join(filter(None, [body_weight, bust_size, hip_size]))
    weather       = WEATHER.get(data.get('weather', ''), '')
    expression    = EXPRESSION.get(data.get('expression', ''), '')
    tattoo        = TATTOO.get(data.get('tattoo', ''), '')
    body_oil      = BODY_OIL.get(data.get('body_oil', ''), '')
    bg_crowd      = BG_CROWD.get(data.get('bg_crowd', ''), '')
    appearance_desc = f"with {appearance}" if appearance else ""

    return (
        f"Professional fashion photograph, {aspect_desc}, {angle}. "
        f"{model_subject} {appearance_desc}, {model}, commanding the frame. "
        f"{'Age: ' + age + '. ' if age else ''}"
        f"{'Body adjustment: ' + body_str + '. ' if body_str else ''}"
        f"{'Era: ' + era + '. ' if era else ''}"
        f"{'Concept: ' + concept + '. ' if concept else ''}"
        f"{'Expression: ' + expression + '. ' if expression else ''}"
        f"{'Skin: ' + skin_tone + '. ' if skin_tone else ''}"
        f"{'Body oil: ' + body_oil + '. ' if body_oil else ''}"
        f"{'Tattoo: ' + tattoo + '. ' if tattoo else ''}"
        f"{'Hair: ' + hair_str + '. ' if hair_str else ''}"
        f"{'Makeup: ' + makeup + '. ' if makeup else ''}"
        f"{'Accessories: ' + accessories + '. ' if accessories else ''}"
        f"{'Props: ' + props + '. ' if props else ''}"
        f"{'Pose: ' + pose + '. ' if pose else ''}"
        f"Wearing {outfit}, crafted from {material}{', ' + footwear if footwear else ''}. "
        f"Scene at {env}, {'Weather: ' + weather + '. ' if weather else ''}"
        f"{'Background: ' + bg_crowd + '. ' if bg_crowd else ''}"
        f"{'Special effects: ' + special_fx + '. ' if special_fx else ''}"
        f"bathed in {light}. "
        f"{'Image style: ' + img_style + '. ' if img_style else ''}"
        f"Style of {style}, captured on {camera}. "
        f"{'Color grade: ' + color_grade + '. ' if color_grade else ''}"
        f"Photorealistic, hyperrealistic skin texture, award-winning fashion photography."
    )


def build_midjourney_prompt(data: dict, aspect: str) -> str:
    ar_map        = {"세로 2:3 — 인물 기본":"2:3","세로 3:4 — 전신샷":"3:4","가로 16:9 — 시네마틱":"16:9","가로 4:3 — 화보":"4:3","정방형 1:1 — 인스타":"1:1"}
    ar            = ar_map.get(aspect, "2:3")
    appearance    = MODEL_APPEARANCE.get(data.get('appearance', ''), '').split(',')[0]
    model_short   = MODEL_TYPES[data['model']].split(',')[0]
    outfit_data   = OUTFIT_TYPES[data['outfit']]
    outfit_short  = (outfit_data["chatgpt"] if isinstance(outfit_data, dict) else outfit_data).split(',')[0]
    material_short = MATERIALS[data['material']].split(',')[0]
    env_short     = ENVIRONMENTS[data['env']].split(',')[0]
    light_short   = LIGHTING[data['light']].split(',')[0]
    style_short   = STYLES[data['style']].split(',')[0]
    footwear_short = FOOTWEAR.get(data.get('footwear', ''), '').split(',')[0]
    tags = [t for t in [appearance, model_short, outfit_short, material_short, footwear_short, env_short, light_short, style_short, "photorealistic", "hyperrealistic", "fashion editorial", "sharp focus", "8K"] if t]
    return f"{', '.join(tags)} --ar {ar} --style raw --q 2"


# ─── 헤더 ─────────────────────────────────────────────────
st.markdown('''
<div style="padding:8px 0 20px;">
  <div style="font-size:1.6rem;font-weight:700;letter-spacing:8px;color:#c9a84c;">✦ LumineX</div>
  <div style="font-size:0.65rem;letter-spacing:3px;color:#444;margin-top:4px;text-transform:uppercase;">AI Fashion Image Engine · v3.2</div>
</div>
''', unsafe_allow_html=True)

# ─── 사이드바 ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ 전역 설정")
    st.markdown("---")
    global_platform = st.radio("🖥️ 출력 플랫폼", options=["Gemini", "ChatGPT (DALL-E)", "Midjourney"], index=0)
    global_aspect   = st.selectbox("📐 이미지 비율", options=list(ASPECT_RATIOS.keys()), index=0)
    global_realism  = st.toggle("📷 실사 모드", value=True)
    st.markdown("---")
    st.markdown("### 🎬 영상 플랫폼")
    global_video_platform = st.radio("영상 생성 플랫폼", options=["Veo 3 (Gemini)", "Kling AI", "Runway", "Hailuo"], index=0)
    st.markdown("---")
    platform_colors = {"Gemini": "🔵", "ChatGPT (DALL-E)": "🟢", "Midjourney": "🟣"}
    st.markdown(f"**플랫폼:** {platform_colors[global_platform]} `{global_platform}`")
    st.markdown(f"**비율:** `{global_aspect.split('—')[0].strip()}`")
    if global_platform == "Gemini":
        st.markdown(f"**실사:** `{'ON ✅' if global_realism else 'OFF'}`")
    st.markdown("---")
    st.markdown("### 📌 사용법")
    st.markdown("1. 플랫폼 선택\n2. 탭 선택\n3. 요소 선택\n4. **프롬프트 조합** 클릭\n5. 코드박스 클릭 → 복사\n6. 해당 플랫폼에 붙여넣기")
    st.markdown("---")
    st.markdown("### 💡 플랫폼 팁")
    if global_platform == "Gemini":
        st.info("자연어 서술형. 길고 상세할수록 좋아요.")
    elif global_platform == "ChatGPT (DALL-E)":
        st.success("키워드 중심. 짧고 강렬하게!")
    else:
        st.warning("태그 나열 + --파라미터 방식.")


# ══════════════════════════════════════════════════════════
# 방법 2: 추천 조합 데이터
# ══════════════════════════════════════════════════════════
GOOD_COMBOS = {
    # ── 극초슬림 계열 ──
    "울트라 슬림 — 뼈가 보이는 하이패션": {
        "outfit":   ["컷아웃 미니드레스 — 전략적 컷아웃, 섹시한 디자인", "하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인", "시스루 바디수트 — 메쉬, 아방가르드"],
        "material": ["시스루 오간자 — 반투명, 살이 비치는", "리퀴드 새틴 — 액체처럼 흐르는 광택", "메탈릭 비닐 — 금속 광택, 미래적"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지", "사이드 프로필 — 옆모습 실루엣"],
        "pose":     ["런웨이 워킹 — 카메라를 향해", "파워 스탠딩 — 손 허리, 당당한", "S커브 — 한쪽 다리 구부린 섹시"],
        "style":    ["보그 이탈리아 하이패션", "알렉산더 맥퀸 — 드라마틱", "티에리 뮈글러 — 파워 패션"],
        "env":      ["파리 패션위크 런웨이 — 모던 무대", "미니멀 스튜디오 — 흰 배경, 깔끔", "다크 바로크 — 화려한 실내"],
    },
    "슈퍼 슬림 — 매우 마른 런웨이": {
        "outfit":   ["컷아웃 미니드레스 — 전략적 컷아웃, 섹시한 디자인", "하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인", "시스루 바디수트 — 메쉬, 아방가르드"],
        "material": ["시스루 오간자 — 반투명, 살이 비치는", "리퀴드 새틴 — 액체처럼 흐르는 광택"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["런웨이 워킹 — 카메라를 향해", "파워 스탠딩 — 손 허리, 당당한"],
        "style":    ["보그 이탈리아 하이패션", "알렉산더 맥퀸 — 드라마틱"],
        "env":      ["파리 패션위크 런웨이 — 모던 무대", "미니멀 스튜디오 — 흰 배경, 깔끔"],
    },
    "슬림 런웨이 — 초장신 늘씬": {
        "outfit":   ["하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인", "컷아웃 미니드레스 — 전략적 컷아웃, 섹시한 디자인", "브라탑+하이슬릿 — 브라탑, 롱 하이슬릿"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "시스루 오간자 — 반투명, 살이 비치는"],
        "angle":    ["전신샷 — 머리부터 발끝", "로우앵글 — 다리 강조, 아래서 위로"],
        "pose":     ["런웨이 워킹 — 카메라를 향해", "S커브 — 한쪽 다리 구부린 섹시"],
        "style":    ["보그 이탈리아 하이패션", "빅토리아 시크릿 패션쇼"],
        "env":      ["파리 패션위크 런웨이 — 모던 무대", "미니멀 스튜디오 — 흰 배경, 깔끔"],
    },
    "슬림 엘레강스 — 날씬하고 우아한": {
        "outfit":   ["하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인", "웨딩 드레스 — 럭셔리 브라이달, 관능적", "오픈백 미니드레스 — 등 노출, 플런징 넥"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "시퀸 — 빛을 받으면 반짝이는"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지", "사이드 프로필 — 옆모습 실루엣"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게", "S커브 — 한쪽 다리 구부린 섹시"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼", "발렌티노 — 레드 카펫 럭셔리", "보그 이탈리아 하이패션"],
        "env":      ["베르사유 궁전 — 황금빛 홀", "파리 오스만 발코니 — 에펠탑 뷰", "우아한 볼룸 — 샹들리에, 대형 파티홀"],
    },
    # ── 슬림톤 계열 ──
    "슬림 톤 — 날씬하고 탄탄한": {
        "outfit":   ["스포츠브라+레깅스 — 핫한 피트니스 룩", "바디콘 미니드레스 — 몸매 강조, 타이트핏", "마이크로 비키니 — 끈 비키니, SI 수영복 화보"],
        "material": ["웻룩 스판덱스 — 젖은 듯한 느낌", "라텍스 — 피부 밀착, 세컨드스킨", "리퀴드 새틴 — 액체처럼 흐르는 광택"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지", "로우앵글 — 다리 강조, 아래서 위로"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "S커브 — 한쪽 다리 구부린 섹시", "런웨이 워킹 — 카메라를 향해"],
        "style":    ["스포츠 일러스트레이티드 수영복", "빅토리아 시크릿 패션쇼", "스포츠 럭셔리 — 나이키/아디다스 하이엔드"],
        "env":      ["럭셔리 인피니티 풀 — 열대 리조트", "마이애미 비치 — 선셋", "말디브 수상빌라 — 크리스탈 바다"],
    },
    "발레리나 — 길고 가늘고 우아한": {
        "outfit":   ["하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인", "웨딩 드레스 — 럭셔리 브라이달, 관능적", "컷아웃 미니드레스 — 전략적 컷아웃, 섹시한 디자인"],
        "material": ["시스루 오간자 — 반투명, 살이 비치는", "리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운"],
        "angle":    ["전신샷 — 머리부터 발끝", "사이드 프로필 — 옆모습 실루엣"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "손 들어 — 머리 위로 손, 관능적", "앉은 포즈 — 바닥/의자에 우아하게"],
        "style":    ["보그 이탈리아 하이패션", "하퍼스 바자 — 관능적 에디토리얼"],
        "env":      ["미니멀 스튜디오 — 흰 배경, 깔끔", "베르사유 궁전 — 황금빛 홀"],
    },
    "슬림 피트니스 — 날씬한 운동선수": {
        "outfit":   ["스포츠브라+레깅스 — 핫한 피트니스 룩", "마이크로 비키니 — 끈 비키니, SI 수영복 화보", "바디콘 미니드레스 — 몸매 강조, 타이트핏"],
        "material": ["웻룩 스판덱스 — 젖은 듯한 느낌", "라텍스 — 피부 밀착, 세컨드스킨"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "크로스 암 — 팔짱 끼고 강렬한", "S커브 — 한쪽 다리 구부린 섹시"],
        "style":    ["스포츠 일러스트레이티드 수영복", "스포츠 럭셔리 — 나이키/아디다스 하이엔드"],
        "env":      ["럭셔리 인피니티 풀 — 열대 리조트", "마이애미 비치 — 선셋"],
    },
    # ── 애슬레틱 계열 ──
    "피트니스 — 탄탄한 복근, 근육미": {
        "outfit":   ["스포츠브라+레깅스 — 핫한 피트니스 룩", "마이크로 비키니 — 끈 비키니, SI 수영복 화보", "바디콘 미니드레스 — 몸매 강조, 타이트핏"],
        "material": ["웻룩 스판덱스 — 젖은 듯한 느낌", "라텍스 — 피부 밀착, 세컨드스킨", "메탈릭 비닐 — 금속 광택, 미래적"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지", "로우앵글 — 다리 강조, 아래서 위로"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "크로스 암 — 팔짱 끼고 강렬한", "S커브 — 한쪽 다리 구부린 섹시"],
        "style":    ["스포츠 일러스트레이티드 수영복", "빅토리아 시크릿 패션쇼", "스포츠 럭셔리 — 나이키/아디다스 하이엔드"],
        "env":      ["럭셔리 인피니티 풀 — 열대 리조트", "마이애미 비치 — 선셋", "미니멀 스튜디오 — 흰 배경, 깔끔"],
    },
    "비키니 컴페티션 — 대회용 극강 근육": {
        "outfit":   ["마이크로 비키니 — 끈 비키니, SI 수영복 화보", "스포츠브라+레깅스 — 핫한 피트니스 룩", "원피스 수영복 — 하이컷, 컷아웃 디자인"],
        "material": ["웻룩 스판덱스 — 젖은 듯한 느낌", "시퀸 — 빛을 받으면 반짝이는", "메탈릭 비닐 — 금속 광택, 미래적"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "크로스 암 — 팔짱 끼고 강렬한"],
        "style":    ["스포츠 일러스트레이티드 수영복", "스포츠 럭셔리 — 나이키/아디다스 하이엔드"],
        "env":      ["미니멀 스튜디오 — 흰 배경, 깔끔", "마이애미 비치 — 선셋"],
    },
    "파워 피트니스 — 강한 근육미": {
        "outfit":   ["스포츠브라+레깅스 — 핫한 피트니스 룩", "마이크로 비키니 — 끈 비키니, SI 수영복 화보", "바디콘 미니드레스 — 몸매 강조, 타이트핏"],
        "material": ["웻룩 스판덱스 — 젖은 듯한 느낌", "라텍스 — 피부 밀착, 세컨드스킨", "메탈릭 비닐 — 금속 광택, 미래적"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "크로스 암 — 팔짱 끼고 강렬한"],
        "style":    ["스포츠 럭셔리 — 나이키/아디다스 하이엔드", "티에리 뮈글러 — 파워 패션"],
        "env":      ["미니멀 스튜디오 — 흰 배경, 깔끔", "마이애미 비치 — 선셋"],
    },
    "스포츠 글램 — 탄탄+볼륨": {
        "outfit":   ["마이크로 비키니 — 끈 비키니, SI 수영복 화보", "스포츠브라+레깅스 — 핫한 피트니스 룩", "바디콘 미니드레스 — 몸매 강조, 타이트핏"],
        "material": ["웻룩 스판덱스 — 젖은 듯한 느낌", "리퀴드 새틴 — 액체처럼 흐르는 광택", "시퀸 — 빛을 받으면 반짝이는"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지", "로우앵글 — 다리 강조, 아래서 위로"],
        "pose":     ["S커브 — 한쪽 다리 구부린 섹시", "파워 스탠딩 — 손 허리, 당당한"],
        "style":    ["빅토리아 시크릿 패션쇼", "스포츠 일러스트레이티드 수영복"],
        "env":      ["럭셔리 인피니티 풀 — 열대 리조트", "마이애미 비치 — 선셋", "말디브 수상빌라 — 크리스탈 바다"],
    },
    # ── 글래머 계열 ──
    "소프트 글램 — 부드러운 여성미": {
        "outfit":   ["하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인", "바디콘 미니드레스 — 몸매 강조, 타이트핏", "코르셋 드레스 — 잘록한 허리, 볼륨감 강조"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "시퀸 — 빛을 받으면 반짝이는"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["S커브 — 한쪽 다리 구부린 섹시", "파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게"],
        "style":    ["빅토리아 시크릿 패션쇼", "하퍼스 바자 — 관능적 에디토리얼", "돌체앤가바나 — 이탈리안 글래머"],
        "env":      ["모나코 테라스 — 지중해 야경", "파리 오스만 발코니 — 에펠탑 뷰", "두바이 펜트하우스 루프탑 — 야경"],
    },
    "VS 앤젤 — 완벽한 VS 글래머": {
        "outfit":   ["마이크로 비키니 — 끈 비키니, SI 수영복 화보", "란제리 에디토리얼 — VS 스타일, 실크 레이스", "바디콘 미니드레스 — 몸매 강조, 타이트핏"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "시퀸 — 빛을 받으면 반짝이는", "크리스탈 메쉬 — 망사에 크리스탈"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지", "로우앵글 — 다리 강조, 아래서 위로"],
        "pose":     ["런웨이 워킹 — 카메라를 향해", "S커브 — 한쪽 다리 구부린 섹시", "파워 스탠딩 — 손 허리, 당당한"],
        "style":    ["빅토리아 시크릿 패션쇼", "스포츠 일러스트레이티드 수영복"],
        "env":      ["파리 패션위크 런웨이 — 모던 무대", "미니멀 스튜디오 — 흰 배경, 깔끔", "두바이 펜트하우스 루프탑 — 야경"],
    },
    "핫 글래머 — 잘록한 허리+볼륨": {
        "outfit":   ["코르셋 드레스 — 잘록한 허리, 볼륨감 강조", "바디콘 미니드레스 — 몸매 강조, 타이트핏", "하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인"],
        "material": ["라텍스 — 피부 밀착, 세컨드스킨", "리퀴드 새틴 — 액체처럼 흐르는 광택", "페이턴트 레더 — 하이글로스 가죽"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["S커브 — 한쪽 다리 구부린 섹시", "파워 스탠딩 — 손 허리, 당당한", "백포즈 — 뒤돌아 어깨 너머 시선"],
        "style":    ["베르사체 캠페인 — 대담한 럭셔리", "돌체앤가바나 — 이탈리안 글래머", "티에리 뮈글러 — 파워 패션"],
        "env":      ["두바이 펜트하우스 루프탑 — 야경", "모나코 테라스 — 지중해 야경", "다크 바로크 — 화려한 실내"],
    },
    "슈퍼 글래머 — 극강 모래시계": {
        "outfit":   ["코르셋 드레스 — 잘록한 허리, 볼륨감 강조", "바디콘 미니드레스 — 몸매 강조, 타이트핏", "하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인"],
        "material": ["라텍스 — 피부 밀착, 세컨드스킨", "리퀴드 새틴 — 액체처럼 흐르는 광택", "페이턴트 레더 — 하이글로스 가죽"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["S커브 — 한쪽 다리 구부린 섹시", "파워 스탠딩 — 손 허리, 당당한"],
        "style":    ["베르사체 캠페인 — 대담한 럭셔리", "티에리 뮈글러 — 파워 패션"],
        "env":      ["다크 바로크 — 화려한 실내", "두바이 펜트하우스 루프탑 — 야경"],
    },
    "럭셔리 글램 — 고급스러운 볼륨": {
        "outfit":   ["하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인", "웨딩 드레스 — 럭셔리 브라이달, 관능적", "코르셋 드레스 — 잘록한 허리, 볼륨감 강조"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "시퀸 — 빛을 받으면 반짝이는"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게"],
        "style":    ["발렌티노 — 레드 카펫 럭셔리", "하퍼스 바자 — 관능적 에디토리얼", "돌체앤가바나 — 이탈리안 글래머"],
        "env":      ["베르사유 궁전 — 황금빛 홀", "모나코 테라스 — 지중해 야경", "우아한 볼룸 — 샹들리에, 대형 파티홀"],
    },
    # ── 커브 계열 ──
    "내추럴 커브 — 자연스러운 곡선미": {
        "outfit":   ["바디콘 미니드레스 — 몸매 강조, 타이트핏", "원피스 수영복 — 하이컷, 컷아웃 디자인", "하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "니트 — 몸에 딱 붙는 립 니트"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["S커브 — 한쪽 다리 구부린 섹시", "파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게"],
        "style":    ["빅토리아 시크릿 패션쇼", "하퍼스 바자 — 관능적 에디토리얼"],
        "env":      ["말디브 수상빌라 — 크리스탈 바다", "파리 오스만 발코니 — 에펠탑 뷰", "럭셔리 인피니티 풀 — 열대 리조트"],
    },
    "소프트 커브 — 부드럽고 풍만한": {
        "outfit":   ["바디콘 미니드레스 — 몸매 강조, 타이트핏", "원피스 수영복 — 하이컷, 컷아웃 디자인", "코르셋 드레스 — 잘록한 허리, 볼륨감 강조"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "니트 — 몸에 딱 붙는 립 니트"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["S커브 — 한쪽 다리 구부린 섹시", "파워 스탠딩 — 손 허리, 당당한"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼", "돌체앤가바나 — 이탈리안 글래머"],
        "env":      ["말디브 수상빌라 — 크리스탈 바다", "럭셔리 인피니티 풀 — 열대 리조트"],
    },
    "풀 커브 — 볼륨감 있는 커브": {
        "outfit":   ["바디콘 미니드레스 — 몸매 강조, 타이트핏", "원피스 수영복 — 하이컷, 컷아웃 디자인", "란제리 에디토리얼 — VS 스타일, 실크 레이스"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "니트 — 몸에 딱 붙는 립 니트"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["S커브 — 한쪽 다리 구부린 섹시", "파워 스탠딩 — 손 허리, 당당한", "누운 포즈 — 바닥/침대에 관능적"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼", "베르사체 캠페인 — 대담한 럭셔리"],
        "env":      ["럭셔리 호텔 스위트 — 펜트하우스 스위트룸", "다크 바로크 — 화려한 실내"],
    },
    "글래머 커브 — 커브+글래머 믹스": {
        "outfit":   ["코르셋 드레스 — 잘록한 허리, 볼륨감 강조", "바디콘 미니드레스 — 몸매 강조, 타이트핏", "란제리 에디토리얼 — VS 스타일, 실크 레이스"],
        "material": ["라텍스 — 피부 밀착, 세컨드스킨", "리퀴드 새틴 — 액체처럼 흐르는 광택", "페이턴트 레더 — 하이글로스 가죽"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["S커브 — 한쪽 다리 구부린 섹시", "파워 스탠딩 — 손 허리, 당당한", "백포즈 — 뒤돌아 어깨 너머 시선"],
        "style":    ["베르사체 캠페인 — 대담한 럭셔리", "티에리 뮈글러 — 파워 패션"],
        "env":      ["다크 바로크 — 화려한 실내", "두바이 펜트하우스 루프탑 — 야경"],
    },
    # ── 플러스사이즈 계열 ──
    "플러스 내추럴 — 자연스러운 플러스": {
        "outfit":   ["원피스 수영복 — 하이컷, 컷아웃 디자인", "바디콘 미니드레스 — 몸매 강조, 타이트핏", "하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "니트 — 몸에 딱 붙는 립 니트"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "S커브 — 한쪽 다리 구부린 섹시", "앉은 포즈 — 바닥/의자에 우아하게"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼", "스포츠 일러스트레이티드 수영복"],
        "env":      ["말디브 수상빌라 — 크리스탈 바다", "럭셔리 인피니티 풀 — 열대 리조트", "파리 오스만 발코니 — 에펠탑 뷰"],
    },
    "플러스 글램 — 플러스사이즈 글래머": {
        "outfit":   ["바디콘 미니드레스 — 몸매 강조, 타이트핏", "코르셋 드레스 — 잘록한 허리, 볼륨감 강조", "하이슬릿 이브닝 — 극하이슬릿, 플런징 넥라인"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "시퀸 — 빛을 받으면 반짝이는"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "S커브 — 한쪽 다리 구부린 섹시"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼", "베르사체 캠페인 — 대담한 럭셔리"],
        "env":      ["다크 바로크 — 화려한 실내", "두바이 펜트하우스 루프탑 — 야경", "우아한 볼룸 — 샹들리에, 대형 파티홀"],
    },
    "라지 플러스 — 매우 풍만한": {
        "outfit":   ["바디콘 미니드레스 — 몸매 강조, 타이트핏", "란제리 에디토리얼 — VS 스타일, 실크 레이스", "원피스 수영복 — 하이컷, 컷아웃 디자인"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "니트 — 몸에 딱 붙는 립 니트"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게", "누운 포즈 — 바닥/침대에 관능적"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼", "스포츠 일러스트레이티드 수영복"],
        "env":      ["럭셔리 호텔 스위트 — 펜트하우스 스위트룸", "다크 바로크 — 화려한 실내"],
    },
    "슈퍼 플러스 — 초풍만": {
        "outfit":   ["바디콘 미니드레스 — 몸매 강조, 타이트핏", "란제리 에디토리얼 — VS 스타일, 실크 레이스", "원피스 수영복 — 하이컷, 컷아웃 디자인"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼"],
        "env":      ["럭셔리 호텔 스위트 — 펜트하우스 스위트룸", "다크 바로크 — 화려한 실내"],
    },
    # ── BBW 계열 ──
    "BBW 글래머 — BBW 글래머": {
        "outfit":   ["바디콘 미니드레스 — 몸매 강조, 타이트핏", "란제리 에디토리얼 — VS 스타일, 실크 레이스", "원피스 수영복 — 하이컷, 컷아웃 디자인"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "시퀸 — 빛을 받으면 반짝이는"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게", "누운 포즈 — 바닥/침대에 관능적"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼", "스포츠 일러스트레이티드 수영복"],
        "env":      ["럭셔리 호텔 스위트 — 펜트하우스 스위트룸", "다크 바로크 — 화려한 실내", "도쿄 네온 거리 — 비 오는 밤"],
    },
    "라지 BBW — 큰 BBW": {
        "outfit":   ["바디콘 미니드레스 — 몸매 강조, 타이트핏", "란제리 에디토리얼 — VS 스타일, 실크 레이스", "원피스 수영복 — 하이컷, 컷아웃 디자인"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼"],
        "env":      ["럭셔리 호텔 스위트 — 펜트하우스 스위트룸", "다크 바로크 — 화려한 실내"],
    },
    "슈퍼 BBW — 극도로 풍만한": {
        "outfit":   ["란제리 에디토리얼 — VS 스타일, 실크 레이스", "바디콘 미니드레스 — 몸매 강조, 타이트핏"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼"],
        "env":      ["럭셔리 호텔 스위트 — 펜트하우스 스위트룸", "다크 바로크 — 화려한 실내"],
    },
    "슈퍼 BBW 글래머 — 극도로 풍만한 글래머": {
        "outfit":   ["란제리 에디토리얼 — VS 스타일, 실크 레이스", "바디콘 미니드레스 — 몸매 강조, 타이트핏"],
        "material": ["리퀴드 새틴 — 액체처럼 흐르는 광택", "벨벳 — 부드럽고 고급스러운", "시퀸 — 빛을 받으면 반짝이는"],
        "angle":    ["전신샷 — 머리부터 발끝", "3/4 샷 — 허벅지까지"],
        "pose":     ["파워 스탠딩 — 손 허리, 당당한", "앉은 포즈 — 바닥/의자에 우아하게"],
        "style":    ["하퍼스 바자 — 관능적 에디토리얼", "베르사체 캠페인 — 대담한 럭셔리"],
        "env":      ["럭셔리 호텔 스위트 — 펜트하우스 스위트룸", "다크 바로크 — 화려한 실내", "두바이 펜트하우스 루프탑 — 야경"],
    },
}

# 충돌 규칙 (angle_keyword, pose_keyword, 경고메시지)
CONFLICT_RULES = [
    ("웨이스트샷", "pool", "앵글(상반신)과 포즈(풀사이드) 불일치 → 전신샷 권장"),
    ("웨이스트샷", "diving", "앵글(상반신)과 포즈(다이빙) 불일치 → 전신샷 권장"),
    ("클로즈업", "전신", "클로즈업 앵글에 전신 포즈 → 웨이스트샷 권장"),
    ("익스트림 클로즈업", "런웨이", "극접사 앵글에 워킹 포즈 → 전신샷 권장"),
    ("사이버펑크", "골든선셋", "스타일(사이버펑크)과 환경(골든선셋) 분위기 불일치"),
    ("사이버펑크", "베르사유", "스타일(사이버펑크)과 환경(궁전) 불일치"),
    ("빅토리안", "사이버펑크", "시대(빅토리안)과 스타일(사이버펑크) 불일치"),
    ("BBW", "latex", "BBW 체형 + 라텍스 → AI 타협 가능성 높음, 새틴/벨벳 권장"),
    ("슈퍼 BBW", "latex", "슈퍼BBW + 라텍스 → AI 거부 가능성, 새틴/벨벳으로 변경 강력 권장"),
    ("슈퍼 플러스", "latex", "슈퍼플러스 + 라텍스 → AI 타협 가능성 높음"),
    ("수영장 입수", "웨이스트샷", "다이빙 포즈에 상반신 앵글 → 전신샷 권장"),
    ("누운 포즈", "전신샷", "누운 포즈 + 전신샷 → 로우앵글 또는 오버헤드 권장"),
]

def check_conflicts(angle: str, pose: str, style: str, environment: str, model: str, material: str) -> list:
    """충돌 감지 → 경고 메시지 리스트 반환"""
    warnings = []
    combined = f"{angle} {pose} {style} {environment} {model} {material}".lower()
    for kw1, kw2, msg in CONFLICT_RULES:
        k1 = kw1.lower()
        k2 = kw2.lower()
        if k1 in combined and k2 in combined:
            warnings.append(msg)
    return warnings

def get_combo_recommendations(model_type: str) -> dict:
    """체형에 맞는 추천 조합 반환"""
    return GOOD_COMBOS.get(model_type, {})

# ══════════════════════════════════════════════════════════

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
    col1, _ = st.columns(2)
    with col1:
        selected_preset = st.selectbox("🎨 프리셋 선택", options=presets, format_func=lambda x: f"• {x}")

    NONE = "None — 프리셋 기본값 사용"
    col1, col2 = st.columns(2)
    with col1:
        preset_appearance  = st.selectbox("👩 인종/국적",       [NONE] + list(MODEL_APPEARANCE.keys()), key="preset_appearance")
        preset_body        = st.selectbox("👤 체형",            [NONE] + list(MODEL_TYPES.keys()),      key="preset_body")
        preset_outfit      = st.selectbox("👗 의상",            [NONE] + list(OUTFIT_TYPES.keys()),     key="preset_outfit")
        preset_material    = st.selectbox("🧵 소재",            [NONE] + list(MATERIALS.keys()),        key="preset_material")
        preset_pose        = st.selectbox("💃 포즈",            [NONE] + list(POSES.keys()),            key="preset_pose")
    with col2:
        preset_color_grade = st.selectbox("🎨 색감",            [NONE] + list(COLOR_GRADES.keys()),    key="preset_color_grade")
        preset_framing     = st.selectbox("📸 프레이밍",        [NONE] + list(CAMERA_ANGLES.keys()),   key="preset_framing")
        preset_footwear    = st.selectbox("👠 신발",            [NONE] + list(FOOTWEAR.keys()),        key="preset_footwear")
        preset_lighting    = st.selectbox("💡 조명",            [NONE] + list(LIGHTING.keys()),        key="preset_lighting")
        preset_style       = st.selectbox("🎬 스타일",          [NONE] + list(STYLES.keys()),          key="preset_style")

    col_a, col_b, _ = st.columns([1, 1, 2])
    with col_a:
        btn_ai    = st.button("🤖 AI 생성",   use_container_width=True, type="primary", key="preset_btn_ai")
    with col_b:
        btn_quick = st.button("⚡ 빠른 생성", use_container_width=True, key="preset_btn_quick")

    if "preset_prompt"   not in st.session_state: st.session_state.preset_prompt   = ""
    if "preset_selected" not in st.session_state: st.session_state.preset_selected = ""
    if selected_preset != st.session_state.preset_selected:
        st.session_state.preset_selected = selected_preset
        st.session_state.preset_prompt   = ""

    def build_preset_overrides() -> dict:
        overrides = {}
        if preset_appearance  != NONE: overrides['appearance']  = MODEL_APPEARANCE[preset_appearance]
        if preset_body        != NONE: overrides['body']        = MODEL_TYPES[preset_body]
        if preset_outfit      != NONE:
            od = OUTFIT_TYPES[preset_outfit]
            overrides['outfit'] = od["gemini"] if isinstance(od, dict) else od
        if preset_material    != NONE: overrides['material']    = MATERIALS[preset_material]
        if preset_pose        != NONE: overrides['pose']        = POSES[preset_pose]
        if preset_color_grade != NONE: overrides['color_grade'] = COLOR_GRADES[preset_color_grade]
        if preset_framing     != NONE: overrides['framing']     = CAMERA_ANGLES[preset_framing]
        if preset_footwear    != NONE: overrides['footwear']    = FOOTWEAR[preset_footwear]
        if preset_lighting    != NONE: overrides['lighting']    = LIGHTING[preset_lighting]
        if preset_style       != NONE: overrides['style']       = STYLES[preset_style]
        return overrides

    def apply_overrides_to_prompt(preset: dict, overrides: dict) -> str:
        p = {**preset, **overrides}
        return (
            f"Professional fashion photograph, {overrides.get('framing', 'full body shot')}. "
            f"{'Model appearance: ' + overrides['appearance'] + '. ' if 'appearance' in overrides else ''}"
            f"Model: {p.get('subject', 'a stunning female model')}. Body: {p.get('body', '')}. "
            f"{'Pose: ' + overrides['pose'] + '. ' if 'pose' in overrides else ''}"
            f"Wearing: {p.get('outfit', '')}, made of {p.get('material', '')}{', ' + overrides['footwear'] if 'footwear' in overrides else ''}. "
            f"Environment: {p.get('environment', '')}. Lighting: {p.get('lighting', '')}. Style: {p.get('style', '')}. "
            f"{'Color grade: ' + overrides['color_grade'] + '. ' if 'color_grade' in overrides else ''}"
            f"{p.get('quality', 'ultra-sharp, 8K, professional photography')}."
        ).strip()

    if btn_ai and selected_preset:
        st.session_state.preset_prompt = ""
        with st.spinner("Claude가 프롬프트 생성 중..."):
            try:
                raw       = generate_prompt_with_ai(selected_preset)
                overrides = build_preset_overrides()
                prefix    = []
                if 'appearance' in overrides: prefix.append(overrides['appearance'].split(',')[0])
                if 'body'       in overrides: prefix.append(overrides['body'].split(',')[0])
                if prefix: raw = f"Model: {', '.join(prefix)}. " + raw
                aspect_desc = ASPECT_RATIOS.get(global_aspect, "")
                if aspect_desc: raw += f" {aspect_desc}."
                st.session_state.preset_prompt = raw
            except Exception as e:
                st.error(f"오류: {str(e)}")

    if btn_quick and selected_preset:
        st.session_state.preset_prompt = ""
        raw = apply_overrides_to_prompt(load_preset(selected_preset), build_preset_overrides())
        aspect_desc = ASPECT_RATIOS.get(global_aspect, "portrait 2:3 vertical")
        if global_platform == "Gemini":
            raw += f" {aspect_desc}."
        elif global_platform == "ChatGPT (DALL-E)":
            raw += f" {aspect_desc}. Photorealistic, hyperrealistic skin texture, award-winning fashion photography."
        else:
            ar = {"세로 2:3 — 인물 기본":"2:3","세로 3:4 — 전신샷":"3:4","가로 16:9 — 시네마틱":"16:9","가로 4:3 — 화보":"4:3","정방형 1:1 — 인스타":"1:1"}.get(global_aspect, "2:3")
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
    st.caption("💡 핵심 요소(외모/체형/의상/환경)만 선택해도 좋은 프롬프트가 나와요. 나머지는 필요할 때만!")

    if st.button("🎲 전체 랜덤으로 채우기"):
        st.session_state.r_appearance      = random.choice(list(MODEL_APPEARANCE.keys()))
        st.session_state.r_age             = "없음"
        st.session_state.r_model           = random.choice(list(MODEL_TYPES.keys()))
        st.session_state.r_outfit          = random.choice(list(OUTFIT_TYPES.keys()))
        st.session_state.r_material        = random.choice(list(MATERIALS.keys()))
        st.session_state.r_footwear        = "없음"
        st.session_state.r_pose            = "없음"
        st.session_state.r_color_grade     = "없음"
        st.session_state.r_hair_style      = "없음"
        st.session_state.r_hair_color      = "없음"
        st.session_state.r_makeup          = "없음"
        st.session_state.r_accessories     = "없음"
        st.session_state.r_skin_tone       = "없음"
        st.session_state.r_model_count     = "1명 — 싱글 모델 (기본)"
        st.session_state.r_era             = "없음"
        st.session_state.r_concept         = "없음"
        st.session_state.r_special_effects = "없음"
        st.session_state.r_image_style     = "없음"
        st.session_state.r_props           = "없음"
        st.session_state.r_body_weight     = "없음"
        st.session_state.r_bust_size       = "없음"
        st.session_state.r_hip_size        = "없음"
        st.session_state.r_weather         = "없음"
        st.session_state.r_expression      = "없음"
        st.session_state.r_tattoo          = "없음"
        st.session_state.r_body_oil        = "없음"
        st.session_state.r_bg_crowd        = "없음"
        st.session_state.r_env             = random.choice(list(ENVIRONMENTS.keys()))
        st.session_state.r_light           = random.choice(list(LIGHTING.keys()))
        st.session_state.r_angle           = random.choice(list(CAMERA_ANGLES.keys()))
        st.session_state.r_style           = random.choice(list(STYLES.keys()))
        st.session_state.r_camera          = random.choice(list(CAMERAS.keys()))

    def idx(d, key, default=0):
        keys = list(d.keys())
        val  = st.session_state.get(key, keys[default])
        return keys.index(val) if val in keys else default

    col1, col2 = st.columns(2)
    with col1:
        appearance  = st.selectbox("👩 모델 외모 — 인종/국적",   list(MODEL_APPEARANCE.keys()), index=idx(MODEL_APPEARANCE, "r_appearance"))
        age         = st.selectbox("🎂 연령대",                   list(AGE_APPEARANCE.keys()),   index=idx(AGE_APPEARANCE,   "r_age"))
        model_type  = st.selectbox("👤 모델 타입 — 체형과 비율", list(MODEL_TYPES.keys()),       index=idx(MODEL_TYPES,      "r_model"))
        outfit      = st.selectbox("👗 의상 타입 — 스타일",      list(OUTFIT_TYPES.keys()),      index=idx(OUTFIT_TYPES,     "r_outfit"))
        material    = st.selectbox("🧵 소재 — 옷감 질감",        list(MATERIALS.keys()),         index=idx(MATERIALS,        "r_material"))
        footwear    = st.selectbox("👠 신발",                    list(FOOTWEAR.keys()),          index=idx(FOOTWEAR,         "r_footwear"))
        pose        = st.selectbox("💃 포즈 — 자세와 동작",      list(POSES.keys()),             index=idx(POSES,            "r_pose"))
        hair_style  = st.selectbox("💇 헤어스타일",              list(HAIR_STYLES.keys()),       index=idx(HAIR_STYLES,      "r_hair_style"))
        hair_color  = st.selectbox("🎨 헤어컬러",               list(HAIR_COLORS.keys()),       index=idx(HAIR_COLORS,      "r_hair_color"))
        makeup      = st.selectbox("💄 메이크업",                list(MAKEUP.keys()),            index=idx(MAKEUP,           "r_makeup"))
        model_count = st.selectbox("👥 모델 수",                 list(MODEL_COUNT.keys()),       index=idx(MODEL_COUNT,      "r_model_count"))
        era         = st.selectbox("🌍 시대/시간대",              list(ERA.keys()),               index=idx(ERA,              "r_era"))
        concept     = st.selectbox("🎭 컨셉/페르소나",            list(CONCEPT.keys()),           index=idx(CONCEPT,          "r_concept"))
        body_weight = st.selectbox("⚖️ 체형 보정 추가",          list(BODY_WEIGHT.keys()),       index=idx(BODY_WEIGHT,      "r_body_weight"))
        bust_size   = st.selectbox("👙 가슴 보정 추가",           list(BUST_SIZE.keys()),         index=idx(BUST_SIZE,        "r_bust_size"))
        hip_size    = st.selectbox("🍑 힙 보정 추가",            list(HIP_SIZE.keys()),          index=idx(HIP_SIZE,         "r_hip_size"))
        expression  = st.selectbox("😏 표정/눈빛",               list(EXPRESSION.keys()),        index=idx(EXPRESSION,       "r_expression"))
    with col2:
        accessories = st.selectbox("💍 액세서리",                list(ACCESSORIES.keys()),       index=idx(ACCESSORIES,      "r_accessories"))
        skin_tone   = st.selectbox("🌊 피부 톤/질감",            list(SKIN_TONES.keys()),        index=idx(SKIN_TONES,       "r_skin_tone"))
        body_oil    = st.selectbox("✨ 바디 오일/글로스",         list(BODY_OIL.keys()),          index=idx(BODY_OIL,         "r_body_oil"))
        tattoo      = st.selectbox("🎨 문신/바디아트",            list(TATTOO.keys()),            index=idx(TATTOO,           "r_tattoo"))
        special_fx  = st.selectbox("🌈 특수 효과",               list(SPECIAL_EFFECTS.keys()),   index=idx(SPECIAL_EFFECTS,  "r_special_effects"))
        img_style   = st.selectbox("📐 이미지 스타일",           list(IMAGE_STYLE.keys()),       index=idx(IMAGE_STYLE,      "r_image_style"))
        props       = st.selectbox("🎪 특별 소품",               list(PROPS.keys()),             index=idx(PROPS,            "r_props"))
        color_grade = st.selectbox("🖼️ 색감 — 컬러 그레이딩",   list(COLOR_GRADES.keys()),      index=idx(COLOR_GRADES,     "r_color_grade"))
        style       = st.selectbox("🎬 스타일 — 화보 레퍼런스",  list(STYLES.keys()),            index=idx(STYLES,           "r_style"))
        environment = st.selectbox("🏙️ 환경 — 촬영 장소",       list(ENVIRONMENTS.keys()),      index=idx(ENVIRONMENTS,     "r_env"))
        weather     = st.selectbox("🌦️ 날씨/기상",               list(WEATHER.keys()),           index=idx(WEATHER,          "r_weather"))
        bg_crowd    = st.selectbox("👥 배경 인물",               list(BG_CROWD.keys()),          index=idx(BG_CROWD,         "r_bg_crowd"))
        lighting    = st.selectbox("💡 조명 — 빛의 분위기",      list(LIGHTING.keys()),          index=idx(LIGHTING,         "r_light"))
        angle       = st.selectbox("📸 카메라 앵글",             list(CAMERA_ANGLES.keys()),     index=idx(CAMERA_ANGLES,    "r_angle"))
        camera      = st.selectbox("📷 카메라 — 장비",           list(CAMERAS.keys()),           index=idx(CAMERAS,          "r_camera"))

    # ── 방법 2: 추천 조합 표시 ──────────────────────────────
    rec = get_combo_recommendations(model_type)
    if rec:
        with st.expander("✅ 이 체형에 잘 맞는 조합 추천", expanded=False):
            rc1, rc2, rc3 = st.columns(3)
            with rc1:
                st.markdown("**👗 의상**")
                for o in rec.get("outfit", []):
                    is_selected = (outfit == o)
                    st.markdown(f"{'🟡 ' if is_selected else '• '}{o.split('—')[0].strip()}")
                st.markdown("**🧵 소재**")
                for m in rec.get("material", []):
                    is_selected = (material == m)
                    st.markdown(f"{'🟡 ' if is_selected else '• '}{m.split('—')[0].strip()}")
            with rc2:
                st.markdown("**📸 앵글**")
                for a in rec.get("angle", []):
                    is_selected = (angle == a)
                    st.markdown(f"{'🟡 ' if is_selected else '• '}{a.split('—')[0].strip()}")
                st.markdown("**💃 포즈**")
                for p in rec.get("pose", []):
                    is_selected = (pose == p)
                    st.markdown(f"{'🟡 ' if is_selected else '• '}{p.split('—')[0].strip()}")
            with rc3:
                st.markdown("**🎬 스타일**")
                for s in rec.get("style", []):
                    is_selected = (style == s)
                    st.markdown(f"{'🟡 ' if is_selected else '• '}{s.split('—')[0].strip()}")
                st.markdown("**🏙️ 환경**")
                for e in rec.get("env", []):
                    is_selected = (environment == e)
                    st.markdown(f"{'🟡 ' if is_selected else '• '}{e.split('—')[0].strip()}")
            st.caption("🟡 = 현재 선택됨  •  = 추천 항목")

    # ── 충돌 감지 실시간 표시 ───────────────────────────────
    conflicts = check_conflicts(angle, pose, style, environment, model_type, material)
    if conflicts:
        for c in conflicts:
            st.warning(f"⚠️ {c}")

    col_x, col_y, col_z, _ = st.columns([1, 1, 1, 1])
    with col_x:
        btn_build      = st.button("✨ 프롬프트 조합", type="primary", use_container_width=True)
    with col_y:
        btn_ai_enhance = st.button("🤖 AI로 강화", use_container_width=True)
    with col_z:
        btn_ai_review  = st.button("🔍 AI 검수", use_container_width=True)

    if "manual_prompt" not in st.session_state:
        st.session_state.manual_prompt = ""
    if "review_result" not in st.session_state:
        st.session_state.review_result = ""

    # ── 방법 3: AI 검수 ─────────────────────────────────────
    if btn_ai_review:
        st.session_state.review_result = ""
        with st.spinner("Claude가 조합 검수 중..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                response = client.messages.create(
                    model="claude-sonnet-4-5",
                    max_tokens=800,
                    messages=[{"role": "user", "content": f"""You are an expert AI image prompt analyst for fashion photography.
Review this combination for conflicts and issues:

- 체형(Body type): {model_type}
- 의상(Outfit): {outfit}
- 소재(Material): {material}
- 앵글(Angle): {angle}
- 포즈(Pose): {pose}
- 환경(Environment): {environment}
- 스타일(Style): {style}
- 조명(Lighting): {lighting}

Analyze for:
1. Angle vs Pose conflicts (e.g. waist-up + full body pose)
2. Body type vs Outfit/Material conflicts (e.g. BBW + latex)
3. Style vs Environment mood mismatch (e.g. cyberpunk + golden sunset)
4. Any other AI generation issues

Respond in Korean. Format:
⚠️ 충돌/문제:
[list each issue]

✅ 수정 제안:
[specific fix for each issue]

🎯 최적 조합:
[brief recommended combination]"""}]
                )
                st.session_state.review_result = response.content[0].text.strip()
            except Exception as e:
                st.error(f"오류: {str(e)}")

    if st.session_state.review_result:
        st.markdown("---")
        st.markdown("#### 🔍 AI 검수 결과")
        st.markdown(st.session_state.review_result)
        st.markdown("---")

    if btn_build:
        def smart_update(key, d, prob):
            """session_state[key]가 없음이면 prob 확률로 랜덤 업데이트"""
            cur = st.session_state.get(key, "없음")
            if cur == "없음":
                keys = [k for k in d.keys() if k != "없음"]
                if keys and random.random() < prob:
                    st.session_state[key] = random.choice(keys)

        # 80% — 거의 항상
        smart_update("r_pose",        POSES,          0.80)
        smart_update("r_expression",  EXPRESSION,     0.80)
        smart_update("r_skin_tone",   SKIN_TONES,     0.80)
        # 50% — 절반 확률
        smart_update("r_hair_style",  HAIR_STYLES,    0.50)
        smart_update("r_hair_color",  HAIR_COLORS,    0.50)
        smart_update("r_makeup",      MAKEUP,         0.50)
        smart_update("r_footwear",    FOOTWEAR,       0.50)
        smart_update("r_color_grade", COLOR_GRADES,   0.50)
        # 30% — 가끔
        smart_update("r_accessories", ACCESSORIES,    0.30)
        smart_update("r_body_oil",    BODY_OIL,       0.30)
        smart_update("r_weather",     WEATHER,        0.30)
        smart_update("r_bg_crowd",    BG_CROWD,       0.30)
        # 15% — 드물게
        smart_update("r_tattoo",      TATTOO,         0.15)
        smart_update("r_special_effects", SPECIAL_EFFECTS, 0.15)
        smart_update("r_props",       PROPS,          0.15)
        smart_update("r_image_style", IMAGE_STYLE,    0.15)
        smart_update("r_era",         ERA,            0.15)
        smart_update("r_concept",     CONCEPT,        0.15)

        st.session_state._trigger_build = True
        st.rerun()

    # rerun 후 실제 프롬프트 생성
    if st.session_state.get("_trigger_build", False):
        st.session_state._trigger_build = False

        # 현재 session_state 값으로 data 구성
        def ss(key, d, default=None):
            keys = list(d.keys())
            val = st.session_state.get(key, keys[0] if keys else "없음")
            return val if val in d else (keys[0] if keys else "없음")

        # 자동 선택된 항목 추적 (이전값과 비교)
        _prev = {k: st.session_state.get(f"_prev_{k}", "없음") for k in [
            "r_pose","r_expression","r_skin_tone","r_hair_style","r_hair_color",
            "r_makeup","r_footwear","r_color_grade","r_accessories","r_body_oil",
            "r_weather","r_bg_crowd","r_tattoo","r_special_effects","r_props",
            "r_image_style","r_era","r_concept",
        ]}
        auto_labels = {
            "r_pose": "💃 포즈", "r_expression": "😏 표정", "r_skin_tone": "🌊 피부",
            "r_hair_style": "💇 헤어", "r_hair_color": "🎨 헤어컬러", "r_makeup": "💄 메이크업",
            "r_footwear": "👠 신발", "r_color_grade": "🖼️ 색감", "r_accessories": "💍 액세서리",
            "r_body_oil": "✨ 바디오일", "r_weather": "🌦️ 날씨", "r_bg_crowd": "👥 배경",
            "r_tattoo": "🎨 문신", "r_special_effects": "🌈 특수효과", "r_props": "🎪 소품",
            "r_image_style": "📐 이미지스타일", "r_era": "🌍 시대", "r_concept": "🎭 컨셉",
        }
        picked_items = {}
        for key, label in auto_labels.items():
            cur = st.session_state.get(key, "없음")
            if _prev[key] == "없음" and cur != "없음":
                picked_items[label] = cur.split("—")[0].strip()
            # 다음 비교를 위해 현재값 저장
            st.session_state[f"_prev_{key}"] = cur

        if picked_items:
            picked_str = "  |  ".join([f"{k} → **{v}**" for k, v in picked_items.items()])
            st.session_state._auto_picked_msg = f"🎲 자동 선택: {picked_str}"
        else:
            st.session_state._auto_picked_msg = ""

        data = {
            "appearance":    ss("r_appearance",  MODEL_APPEARANCE),
            "age":           ss("r_age",          AGE_APPEARANCE),
            "model":         ss("r_model",        MODEL_TYPES),
            "outfit":        ss("r_outfit",       OUTFIT_TYPES),
            "material":      ss("r_material",     MATERIALS),
            "footwear":      ss("r_footwear",     FOOTWEAR),
            "pose":          ss("r_pose",         POSES),
            "color_grade":   ss("r_color_grade",  COLOR_GRADES),
            "hair_style":    ss("r_hair_style",   HAIR_STYLES),
            "hair_color":    ss("r_hair_color",   HAIR_COLORS),
            "makeup":        ss("r_makeup",       MAKEUP),
            "accessories":   ss("r_accessories",  ACCESSORIES),
            "skin_tone":     ss("r_skin_tone",    SKIN_TONES),
            "model_count":   ss("r_model_count",  MODEL_COUNT),
            "era":           ss("r_era",          ERA),
            "concept":       ss("r_concept",      CONCEPT),
            "special_effects": ss("r_special_effects", SPECIAL_EFFECTS),
            "image_style":   ss("r_image_style",  IMAGE_STYLE),
            "props":         ss("r_props",        PROPS),
            "body_weight":   ss("r_body_weight",  BODY_WEIGHT),
            "bust_size":     ss("r_bust_size",    BUST_SIZE),
            "hip_size":      ss("r_hip_size",     HIP_SIZE),
            "weather":       ss("r_weather",      WEATHER),
            "expression":    ss("r_expression",   EXPRESSION),
            "tattoo":        ss("r_tattoo",       TATTOO),
            "body_oil":      ss("r_body_oil",     BODY_OIL),
            "bg_crowd":      ss("r_bg_crowd",     BG_CROWD),
            "env":           ss("r_env",          ENVIRONMENTS),
            "light":         ss("r_light",        LIGHTING),
            "angle":         ss("r_angle",        CAMERA_ANGLES),
            "style":         ss("r_style",        STYLES),
            "camera":        ss("r_camera",       CAMERAS),
        }
        st.session_state.manual_prompt = get_prompt(data)

    # 자동선택 메시지 표시
    if st.session_state.get("_auto_picked_msg"):
        st.info(st.session_state._auto_picked_msg)

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
Rules: model fills frame, photorealistic skin.
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
    st.caption("핵심 요소만 랜덤 조합 — 프롬프트 최적 길이 유지")

    col1, col2, _ = st.columns([1, 1, 2])
    with col1:
        btn_rand    = st.button("🎲 랜덤 생성", type="primary", use_container_width=True)
    with col2:
        btn_rand_ai = st.button("🤖 AI 랜덤", use_container_width=True)

    if "random_prompt" not in st.session_state:
        st.session_state.random_prompt = ""

    if btn_rand:
        data = {
            "appearance":      random.choice(list(MODEL_APPEARANCE.keys())),
            "age":             "없음",
            "model":           random.choice(list(MODEL_TYPES.keys())),
            "outfit":          random.choice(list(OUTFIT_TYPES.keys())),
            "material":        random.choice(list(MATERIALS.keys())),
            "footwear":        "없음",
            "pose":            random.choice(list(POSES.keys())),
            "color_grade":     "없음",
            "hair_style":      "없음",
            "hair_color":      "없음",
            "makeup":          "없음",
            "accessories":     "없음",
            "skin_tone":       "없음",
            "model_count":     "1명 — 싱글 모델 (기본)",
            "era":             "없음",
            "concept":         "없음",
            "special_effects": "없음",
            "image_style":     "없음",
            "props":           "없음",
            "body_weight":     "없음",
            "bust_size":       "없음",
            "hip_size":        "없음",
            "env":             random.choice(list(ENVIRONMENTS.keys())),
            "light":           random.choice(list(LIGHTING.keys())),
            "angle":           random.choice(list(CAMERA_ANGLES.keys())),
            "style":           random.choice(list(STYLES.keys())),
            "camera":          random.choice(list(CAMERAS.keys())),
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
st.markdown('<div style="text-align:center;color:#444;font-size:0.75rem;">✦ LumineX v3.2 — AI Fashion Image Engine</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# 탭 4: 영상 프롬프트
# ══════════════════════════════════════════════════════════
with tab4:
    st.markdown(f"### 🎬 영상 프롬프트 생성 — {global_video_platform}")

    VIDEO_PLATFORM_TIPS = {
        "Veo 3 (Gemini)": ("🔵", "gemini.google.com", "Gemini Advanced 구독 필요. 좌측 메뉴에서 Veo 3 선택."),
        "Kling AI":        ("🟡", "klingai.com",       "무료 티어 사용 가능. 매일 크레딧 지급."),
        "Runway":          ("🟢", "runwayml.com",      "무료 크레딧 제공. Gen-3 Alpha 사용."),
        "Hailuo":          ("🟠", "hailuoai.video",    "완전 무료. 중국 서비스."),
    }
    color, url, tip = VIDEO_PLATFORM_TIPS[global_video_platform]
    st.info(f"{color} **{global_video_platform}** — {tip} → [{url}](https://{url})")

    VIDEO_DURATIONS  = {"5초 — 짧고 임팩트 있는": "5 seconds", "8초 — 표준 클립": "8 seconds", "10초 — 긴 클립": "10 seconds"}
    VIDEO_MOTIONS    = {
        "워킹 — 런웨이 워크, 카메라 정면":     "walking towards camera, confident runway walk, slow motion",
        "턴 — 360도 회전, 의상 전체 공개":      "slow 360 degree turn, revealing full outfit",
        "포즈 — 정적 포즈, 바람에 머리 날림":   "standing pose, hair flowing in wind, subtle movement",
        "댄스 — 섹시한 느낌의 부드러운 움직임": "slow sensual dance movement, fluid motion",
        "워킹+턴 — 걷다가 카메라 보며 턴":      "walking then turning to camera, fashion editorial motion",
        "등장 — 안개/빛 속에서 천천히 등장":    "emerging slowly from mist and light, dramatic entrance",
    }
    VIDEO_CAMERAS    = {
        "시네마틱 — 느린 달리샷":           "slow cinematic dolly shot, smooth camera movement",
        "오빗 — 모델 주위를 도는 카메라":   "slow orbit around subject, 360 camera movement",
        "줌인 — 전신에서 얼굴로 천천히 줌": "slow zoom from full body to face, intimate close-up",
        "로우앵글 — 아래서 위로 올려다보기": "low angle upward camera, powerful perspective",
        "하이앵글 — 위에서 내려다보기":     "high angle downward camera, elegant perspective",
        "핸드헬드 — 약간의 흔들림, 현장감":  "slight handheld camera movement, documentary feel",
    }
    VIDEO_ATMOSPHERES = {
        "럭셔리 글래머 — 화려하고 고급스러운":  "luxury glamour atmosphere, high-end fashion film",
        "다크 시네마틱 — 어둡고 영화적인":      "dark cinematic atmosphere, noir fashion film",
        "골든아워 — 따뜻한 황금빛":             "golden hour warm light, dreamy fashion film",
        "네온 사이버펑크 — 미래적 네온 분위기": "neon cyberpunk atmosphere, futuristic fashion film",
        "미니멀 클린 — 깔끔하고 모던한":        "minimal clean white atmosphere, modern fashion film",
        "에디토리얼 — 잡지 화보 느낌":          "editorial fashion film, Vogue video style",
    }

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**📝 기존 프롬프트 기반으로 변환**")
        source_prompt    = st.text_area("이미지 프롬프트 붙여넣기 (선택사항)", placeholder="기존 이미지 프롬프트를 여기에 붙여넣으면 영상용으로 변환해줘요...", height=120, key="video_source")
        video_duration   = st.selectbox("⏱️ 영상 길이", list(VIDEO_DURATIONS.keys()))
        video_motion     = st.selectbox("🏃 모션 타입", list(VIDEO_MOTIONS.keys()))
    with col2:
        video_camera     = st.selectbox("📷 카메라 무브먼트", list(VIDEO_CAMERAS.keys()))
        video_atmosphere = st.selectbox("🌟 분위기", list(VIDEO_ATMOSPHERES.keys()))
        video_appearance = st.selectbox("👩 모델 외모", ["None — 프롬프트 기반"] + list(MODEL_APPEARANCE.keys()), key="video_appearance")
        video_outfit     = st.selectbox("👗 의상", ["None — 프롬프트 기반"] + list(OUTFIT_TYPES.keys()), key="video_outfit")

    st.markdown("")
    col_x, col_y, _ = st.columns([1, 1, 2])
    with col_x:
        btn_video_build = st.button("🎬 영상 프롬프트 생성", type="primary", use_container_width=True)
    with col_y:
        btn_video_ai    = st.button("🤖 AI로 강화", use_container_width=True, key="btn_video_ai")

    if "video_prompt" not in st.session_state:
        st.session_state.video_prompt = ""

    if btn_video_build:
        st.session_state.video_prompt = ""
        appearance_str = f"Model: {MODEL_APPEARANCE[video_appearance].split(',')[0]}. " if video_appearance != "None — 프롬프트 기반" else ""
        outfit_str = ""
        if video_outfit != "None — 프롬프트 기반":
            od = OUTFIT_TYPES[video_outfit]
            outfit_str = f"Wearing: {(od['gemini'] if isinstance(od, dict) else od).split(',')[0]}. "
        base = f"Based on: {source_prompt[:200]}. " if source_prompt else ""
        st.session_state.video_prompt = (
            f"Cinematic fashion video, {VIDEO_DURATIONS[video_duration]}. {base}"
            f"{appearance_str}{outfit_str}"
            f"Motion: {VIDEO_MOTIONS[video_motion]}. Camera: {VIDEO_CAMERAS[video_camera]}. "
            f"Atmosphere: {VIDEO_ATMOSPHERES[video_atmosphere]}. "
            f"Photorealistic, hyperrealistic, 4K cinematic quality, professional fashion film, no text, no watermark."
        )

    if btn_video_ai and (source_prompt or st.session_state.video_prompt):
        with st.spinner("Claude가 영상 프롬프트 강화 중..."):
            try:
                import anthropic
                client = anthropic.Anthropic()
                base   = source_prompt or st.session_state.video_prompt
                response = client.messages.create(
                    model="claude-sonnet-4-5",
                    max_tokens=500,
                    messages=[{"role": "user", "content": f"""You are an expert video prompt engineer.
Create a powerful cinematic fashion video prompt based on this: {base}
Settings: Duration: {VIDEO_DURATIONS[video_duration]}, Motion: {VIDEO_MOTIONS[video_motion]}, Camera: {VIDEO_CAMERAS[video_camera]}, Atmosphere: {VIDEO_ATMOSPHERES[video_atmosphere]}
Rules: Cinematic, photorealistic, 4K. No text overlays. Output ONLY the prompt, 100-150 words."""}]
                )
                st.session_state.video_prompt = response.content[0].text.strip()
            except Exception as e:
                st.error(f"오류: {str(e)}")

    if st.session_state.video_prompt:
        st.text_area("생성된 영상 프롬프트", value=st.session_state.video_prompt, height=180)
        st.code(st.session_state.video_prompt, language=None)
        st.caption("👆 복사 후 해당 플랫폼에 붙여넣으세요!")
        st.markdown("---")
        st.markdown(f"### 💡 {global_video_platform} 사용 방법")
        if global_video_platform == "Veo 3 (Gemini)":
            st.markdown("1. [gemini.google.com](https://gemini.google.com) 접속\n2. 좌측 **Veo 3** 선택\n3. 위 프롬프트 붙여넣기\n4. 생성 클릭!")
        elif global_video_platform == "Kling AI":
            st.markdown("1. [klingai.com](https://klingai.com) 접속\n2. **Text to Video** 선택\n3. 위 프롬프트 붙여넣기\n4. 생성 클릭!")
        elif global_video_platform == "Runway":
            st.markdown("1. [runwayml.com](https://runwayml.com) 접속\n2. **Gen-3 Alpha** 선택\n3. 위 프롬프트 붙여넣기\n4. 생성 클릭!")
        else:
            st.markdown("1. [hailuoai.video](https://hailuoai.video) 접속\n2. **Text to Video** 선택\n3. 위 프롬프트 붙여넣기\n4. 생성 클릭!")