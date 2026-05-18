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
    "🇧🇷 브라질리언 — 브라질, 구릿빛 피부, 풍만한 글래머": "Brazilian beauty, bronzed tan skin, full voluptuous curves, tropical glamour",
    "🇨🇴 콜롬비안 — 콜롬비아, 이국적 라틴 미녀": "Colombian beauty, exotic Latin features, olive skin, sultry dark eyes",
    "🇸🇪 스칸디나비안 — 북유럽, 금발, 차갑고 우아한": "Scandinavian beauty, platinum blonde, ice blue eyes, tall elegant Nordic features",
    "🇷🇺 동유럽 — 슬라브 미녀, 강한 골격, 매혹적": "Eastern European beauty, Slavic features, high cheekbones, mysterious allure",
    "🇲🇦 모로칸 — 북아프리카, 이국적 중동+아프리카 믹스": "Moroccan beauty, exotic North African features, olive skin, dark almond eyes",
    "🇪🇬 이집트 — 클레오파트라 느낌, 강렬한 눈매": "Egyptian beauty, Cleopatra-like features, intense dark eyes, Mediterranean skin",
}

MODEL_TYPES = {
    "글래머 피트니스 — 탄탄+볼륨, 섹시한 근육미": "glamorous fitness model, full bust, toned abs, round hips, fit and voluptuous, hourglass figure",
    "핫 글래머 — 가슴 볼륨, 잘록한 허리, 풍만한 힙": "hot glamour model, full voluptuous bust, extremely narrow waist, full round hips, ultra hourglass",
    "빅토리아 시크릿 — VS앤젤, 완벽한 볼륨+탄탄": "Victoria's Secret Angel, perfect full bust, toned flat abs, long legs, curvaceous yet athletic",
    "런웨이 글램 — 늘씬하면서 볼륨감 있는": "tall runway model, long legs, slender yet curvaceous, elegant glamorous figure",
    "피트니스 — 탄탄한 복근, 근육미, 스포티": "athletic fitness model, defined abs, toned muscular legs, powerful physique",
    "소프트 글램 — 부드러운 곡선, 여성스러운": "soft glamour model, feminine gentle curves, elegant posture, graceful",
    "런웨이 — 초장신, 극도로 늘씬, 다리 길이 강조": "extremely tall runway model, impossibly long legs, ultra-slender waist, elongated silhouette",
    "플러스사이즈 글래머 — 풍만하고 자신감 넘치는": "plus-size glamour model, full voluptuous curves, confident powerful presence, body positive glamour",
    "피트니스 비키니 컴페티션 — 대회용 극강 근육미": "fitness bikini competition model, extremely defined muscles, competition-ready physique, shredded athletic body",
    "발레리나 — 길고 가늘고 극도로 우아한": "ballerina physique, extremely slender and elongated, graceful elegant posture, dancer's perfect poise",
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
    # ── 스페셜 ─────────────────────────────────────────────
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
    "백샷 — 뒤에서 촬영, 등 강조": "rear view back shot, spine and back emphasis",
    "익스트림 클로즈업 — 얼굴만 극접사": "extreme close-up face only, skin texture detail",
}

FOOTWEAR = {
    "스틸레토 힐 — 극도로 높은 힐, 다리 라인 강조": "wearing extreme stiletto heels, legs elongated",
    "스트래피 샌들 힐 — 얇은 끈 샌들 힐": "wearing strappy high heel sandals, elegant feet",
    "플랫폼 부츠 — 두꺼운 솔, 파워풀": "wearing platform boots, powerful stance",
    "무릎까지 부츠 — 니하이 부츠, 섹시한": "wearing knee-high boots, sexy long legs",
    "허벅지까지 부츠 — 싸이하이 부츠": "wearing thigh-high boots, ultra sexy",
    "포인티드 토 힐 — 뾰족한 앞코 힐": "wearing pointed toe stiletto pumps, classic glamour",
    "글래디에이터 샌들 — 끈이 종아리까지": "wearing gladiator sandals, lace-up straps up the calf",
    "뮬 힐 — 뒤가 없는 슬링백 힐": "wearing mule heels, backless slip-on stiletto",
    "크리스탈 힐 — 반짝이는 투명 힐": "wearing crystal clear transparent heels, Cinderella glass slipper",
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
    "AI 자동 — 프롬프트 기반": "",
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
    "코르넬로 — 뿔 모양 아방가르드 업스타일": "avant-garde horn updo, sculptural hair art, editorial",
}

HAIR_COLORS = {
    "AI 자동 — 프롬프트 기반": "",
    "블랙 — 짙은 검정, 아시안 느낌": "jet black hair, deep dark black",
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
    "1명 — 싱글 모델 (기본)": {
        "count": 1,
        "prompt": "A stunning female model",
    },
    "2명 — 듀오, 두 모델 나란히": {
        "count": 2,
        "prompt": "Two stunning female models standing together side by side",
    },
    "2명 — 듀오, 대비되는 포즈": {
        "count": 2,
        "prompt": "Two stunning female models, contrasting poses, one in foreground one behind",
    },
    "3명 — 트리오, 세 모델": {
        "count": 3,
        "prompt": "Three stunning female models posing together, trio fashion editorial",
    },
    "그룹 — VS 런웨이 그룹샷": {
        "count": 4,
        "prompt": "Group of stunning female models on runway, Victoria's Secret fashion show group shot",
    },
}

ERA = {
    "없음": "",
    "현대 — 2020년대 트렌디": "contemporary 2020s fashion, modern trendy style",
    "레트로 80s — 네온, 빅헤어, 글램록": "retro 1980s fashion, neon colors, big hair, glam rock era",
    "레트로 90s — 슈퍼모델 황금시대": "1990s supermodel era, minimalist chic, heroin chic aesthetic",
    "빅토리안 — 코르셋, 드라마틱": "Victorian era fashion, dramatic corset, ornate period costume",
    "1920s 플래퍼 — 재즈시대 글래머": "1920s flapper era, art deco glamour, jazz age fashion",
    "미래 2100년 — SF 하이테크": "year 2100 futuristic fashion, high-tech sci-fi costume, future era",
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

BODY_WEIGHT = {
    "없음": "",
    "애노렉식 — 극도로 마른, 뼈만 앙상한": "anorexic extremely emaciated body, bones visibly protruding, skeletal figure, severely underweight, no body fat whatsoever",
    "익스트림 슬림 — 뼈가 보이는 초마름": "extremely underweight body, visible ribs and hip bones, very bony thin figure, severely slim, waif-like skeletal",
    "슈퍼 슬림 — 매우 마른 하이패션": "super slim ultra-thin body, very narrow waist, no curves, razor-thin silhouette, high fashion underweight model",
    "슬림 — 날씬한 체형": "slim slender body, lean light frame, thin waist, minimal body fat, delicate figure",
    "슬림 톤 — 날씬하고 탄탄한": "slim toned athletic body, lean defined muscles, flat stomach, light but fit",
    "애슬레틱 — 탄탄한 운동선수": "athletic muscular body, defined muscles, sports-toned physique, powerful build, visible muscle definition",
    "핏 글래머 — 탄탄하면서 볼륨": "fit glamorous body, toned yet curvy, athletic hourglass, defined abs with full bust and hips",
    "보통 — 평균적인 자연스러운": "average natural body type, realistic proportions, normal weight, natural soft curves",
    "커브 — 자연스러운 여성 곡선미": "curvy feminine body, natural soft curves, womanly figure, healthy weight with visible curves",
    "풀 피규어 — 풍만하고 글래머러스": "full figure glamorous body, voluptuous curves, plus glamour, full bust and hips, soft rounded stomach",
    "플러스사이즈 — 플러스사이즈 모델": "plus-size model body, full voluptuous figure, size 16-18, soft belly, full thighs, body positive",
    "라지 플러스 — 매우 풍만한 체형": "large plus-size body, size 20-22, very full figure, round soft belly, heavy thighs, wide hips, abundant curves",
    "BBW 글래머 — 극도로 풍만한 글래머": "BBW glamour body, obese figure, large protruding belly, very full heavy thighs, wide heavy hips, chubby arms, overweight body, 250 pound figure",
    "슈퍼 BBW — 매우 큰 풍만한 체형": "super BBW body, massively obese figure, very large hanging belly with multiple rolls, enormous thighs, very heavy arms, extremely wide hips, significantly overweight, 300+ pound body type",
}

BUST_SIZE = {
    "없음": "",
    "플랫 — 거의 없는 평평한": "very flat chest, barely-there bust, AA-cup, no breast tissue visible",
    "스몰 — 작은 가슴": "small A-cup breasts, petite modest chest, minimal bust",
    "미디엄 스몰 — 약간 작은": "B-cup breasts, natural modest bust, small but present",
    "미디엄 — 보통 사이즈": "C-cup breasts, natural proportionate bust, medium fullness",
    "풀 미디엄 — 보통보다 약간 큰": "full D-cup breasts, naturally full bust, prominent cleavage",
    "라지 — 큰 가슴": "large DD-cup breasts, very full heavy bust, deep cleavage, overflowing top",
    "엑스라지 — 매우 큰 가슴": "extremely large DDD/F-cup breasts, massive heavy bust, extreme cleavage, barely contained",
    "슈퍼 라지 — 극도로 큰 가슴": "enormous G/H-cup breasts, gigantic heavy bust, overflowing, extremely voluminous chest",
    "글래머 — 완벽한 글래머 볼륨": "perfect glamour bust, lifted full round breasts, maximum volume cleavage, pinup perfection",
}

HIP_SIZE = {
    "없음": "",
    "플랫 — 거의 없는 평평한 힙": "very flat hips, no curves, straight boyish lower body, minimal buttocks",
    "슬림 — 날씬한 힙": "slim narrow hips, small flat buttocks, petite lower body",
    "미디엄 — 보통 힙": "medium hips, natural proportionate buttocks, modest curves",
    "풀 — 풍만한 힙": "full round hips, prominent rounded buttocks, womanly curves, wide hip-to-waist ratio",
    "글래머 힙 — 모래시계 글래머": "dramatic hourglass hips, very wide full hips, large round prominent buttocks, extreme waist-to-hip ratio",
    "라지 힙 — 큰 힙": "very large wide hips, large heavy buttocks, thick full thighs, abundant lower body curves",
    "바비 힙 — 극강 모래시계": "extreme Barbie hourglass, impossibly wide hips, tiny waist, enormous round buttocks, hyper-feminine silhouette",
    "브라질리언 힙 — 크고 둥근": "Brazilian-style enormous round buttocks, very large protruding rear, thick heavy thighs, maximum gluteal volume",
    "슈퍼 커브 — 극도로 풍만한 힙": "super curvy massive hips, extremely wide lower body, huge round heavy buttocks, thighs touching, very thick legs",
    "엑스트림 커브 — 과장된 곡선": "hyper-exaggerated curves, cartoonishly wide hips, gigantic round protruding buttocks, maximum possible hip volume, impossibly curvy",
}

MAKEUP = {
    "AI 자동 — 프롬프트 기반": "",
    "스모키 아이 — 강렬한 눈매, 다크 섀도우": "dramatic smoky eye makeup, dark eyeshadow, intense gaze",
    "누드 글램 — 자연스럽고 섹시한": "nude glam makeup, natural yet sexy, glossy lips, subtle glow",
    "레드립 — 클래식 빨간 입술": "classic red lip makeup, bold red lipstick, timeless glamour",
    "글리터 글램 — 반짝이는 파티 메이크업": "glitter glam makeup, sparkling eyeshadow, festival beauty",
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
    "AI 자동 — 프롬프트 기반": "",
    "골드 주얼리 — 목걸이+귀걸이 골드 세트": "gold jewelry set, gold necklace and earrings, luxury accessories",
    "다이아몬드 — 럭셔리 다이아 주얼리": "diamond jewelry, sparkling diamond necklace and earrings, ultra luxury",
    "초커 — 섹시한 목 초커": "choker necklace, sexy neck choker, edgy accessory",
    "바디체인 — 몸에 두르는 골드 체인": "gold body chain, draped across torso, glamorous body jewelry",
    "레이어드 체인 — 여러 겹 목걸이": "layered chain necklaces, multiple gold chains, trendy stacked look",
    "진주 — 클래식 우아한 진주": "pearl jewelry, classic pearl necklace and earrings, timeless elegance",
    "크리스탈 — 반짝이는 크리스탈 주얼리": "crystal jewelry, sparkling rhinestone accessories, glamorous",
    "귀걸이만 — 드라마틱한 드롭 귀걸이": "statement drop earrings only, dramatic dangling earrings",
    "럭셔리 워치 — 명품 시계": "luxury watch, designer timepiece on wrist, status accessory",
    "팔찌 스택 — 여러 겹 팔찌": "stacked bracelets, multiple bangles and cuffs on wrist",
    "없음 — 미니멀 액세서리 없음": "no accessories, minimalist, clean look",
}

SKIN_TONES = {
    "AI 자동 — 프롬프트 기반": "",
    "오일드 스킨 — 윤기있는 글로시 피부": "oiled glossy skin, shiny wet-look skin, body oil gleaming",
    "태닝 — 브론즈 골든 태닝": "bronzed tan skin, golden sun-kissed tan, beach goddess",
    "딥 태닝 — 짙은 초콜릿 태닝": "deep dark tan, rich chocolate bronzed skin, intense tanning",
    "페일 — 창백하고 신비로운": "pale porcelain skin, ethereal fair complexion, mysterious allure",
    "글로우 — 발광하는 빛나는 피부": "luminous glowing skin, radiant inner glow, lit-from-within effect",
    "매트 — 무광 세련된 피부": "matte flawless skin, powdery smooth complexion, editorial finish",
    "듀이 — 촉촉하고 생기있는": "dewy fresh skin, hydrated plump complexion, youthful glow",
    "스웨티 — 운동 후 땀나는 느낌": "sweaty glistening skin, post-workout sheen, athletic perspiration",
    "프로스티 — 차갑고 얼음같은 피부": "frosty icy skin tone, cold ethereal complexion, winter goddess",
}

POSES = {
    "파워 스탠딩 — 손 허리, 당당한 자세": "powerful standing pose, hands on hips, confident dominant stance",
    "런웨이 워킹 — 카메라를 향해 걸어오는": "walking confidently toward camera, runway catwalk stride",
    "S커브 — 한쪽 다리 구부린 섹시 포즈": "sexy S-curve pose, one leg bent, hip tilted, sultry stance",
    "백포즈 — 뒤돌아 어깨 너머 시선": "back to camera, looking over shoulder seductively, rear view",
    "기댄 포즈 — 벽에 기댄 캐주얼": "leaning against wall, casual yet sexy pose, relaxed confidence",
    "앉은 포즈 — 바닥/의자에 우아하게": "seated elegantly, legs crossed, sophisticated sitting pose",
    "역동적 — 머리카락 날리는 움직임": "dynamic pose, hair flowing in wind, motion blur effect",
    "크로스 암 — 팔짱 끼고 강렬한 시선": "arms crossed, intense gaze, powerful commanding expression",
    "손 들어 — 머리 위로 손, 관능적": "arms raised above head, sensual elongated pose, arched back",
    "등 보이기 — 백뷰, 어깨 라인 강조": "back view pose, spine visible, shoulder blade emphasis",
    "누운 포즈 — 바닥/침대에 관능적으로": "lying down pose, reclined on floor or bed, sensual and languid",
    "수영장 입수 — 물가에서 다이빙 직전": "standing at pool edge, about to dive, water reflection below",
    "거울 앞 — 거울 반영, 이중 시선": "standing before mirror, reflection visible, double perspective pose",
}

COLOR_GRADES = {
    "컬러 — 자연스러운 색감 (기본)": "",
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
    """Gemini: 자연어 서술형, 길고 묘사적"""
    aspect_desc = ASPECT_RATIOS.get(aspect, "")
    realism_kw  = "photorealistic, RAW photo, hyperrealistic, natural skin texture, pore detail, film grain, professional photographer" if realism else ""
    appearance  = MODEL_APPEARANCE.get(data.get('appearance', ''), '')
    outfit_data = OUTFIT_TYPES[data['outfit']]
    outfit      = outfit_data["gemini"] if isinstance(outfit_data, dict) else outfit_data
    footwear    = FOOTWEAR.get(data.get('footwear', ''), '')
    pose        = POSES.get(data.get('pose', ''), '')
    color_grade = COLOR_GRADES.get(data.get('color_grade', ''), '')
    hair_style  = HAIR_STYLES.get(data.get('hair_style', ''), '')
    hair_color  = HAIR_COLORS.get(data.get('hair_color', ''), '')
    hair_str    = " ".join(filter(None, [hair_color, hair_style]))
    makeup         = MAKEUP.get(data.get('makeup', ''), '')
    accessories    = ACCESSORIES.get(data.get('accessories', ''), '')
    skin_tone      = SKIN_TONES.get(data.get('skin_tone', ''), '')
    count_data     = MODEL_COUNT.get(data.get('model_count', '1명 — 싱글 모델 (기본)'), MODEL_COUNT['1명 — 싱글 모델 (기본)'])
    model_subject  = count_data['prompt']
    era            = ERA.get(data.get('era', ''), '')
    concept        = CONCEPT.get(data.get('concept', ''), '')
    special_fx     = SPECIAL_EFFECTS.get(data.get('special_effects', ''), '')
    img_style      = IMAGE_STYLE.get(data.get('image_style', ''), '')
    props          = PROPS.get(data.get('props', ''), '')
    body_weight    = BODY_WEIGHT.get(data.get('body_weight', ''), '')
    bust_size      = BUST_SIZE.get(data.get('bust_size', ''), '')
    hip_size       = HIP_SIZE.get(data.get('hip_size', ''), '')
    body_str       = ", ".join(filter(None, [body_weight, bust_size, hip_size]))

    parts = [
        f"Professional fashion photograph, {CAMERA_ANGLES[data['angle']]}, model fills the entire frame.",
        f"{model_subject}: {MODEL_TYPES[data['model']]}{', ' + appearance if appearance else ''}.",
        f"Body details: {body_str}." if body_str else "",
        f"Era: {era}." if era else "",
        f"Concept: {concept}." if concept else "",
        f"Skin: {skin_tone}." if skin_tone else "",
        f"Hair: {hair_str}." if hair_str else "",
        f"Makeup: {makeup}." if makeup else "",
        f"Accessories: {accessories}." if accessories else "",
        f"Props: {props}." if props else "",
        f"Pose: {pose}." if pose else "",
        f"Wearing: {outfit}, made of {MATERIALS[data['material']]}{', ' + footwear if footwear else ''}.",
        f"Environment: {ENVIRONMENTS[data['env']]}, background softly blurred bokeh.",
        f"Special effects: {special_fx}." if special_fx else "",
        f"Lighting: {LIGHTING[data['light']]}.",
        f"Style reference: {STYLES[data['style']]}.",
        f"Image style: {img_style}." if img_style else "",
        f"Camera: {CAMERAS[data['camera']]}, sharp focus on model.",
        f"Color grade: {color_grade}." if color_grade else "",
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
    pose        = POSES.get(data.get('pose', ''), '')
    color_grade = COLOR_GRADES.get(data.get('color_grade', ''), '')
    hair_style  = HAIR_STYLES.get(data.get('hair_style', ''), '')
    hair_color  = HAIR_COLORS.get(data.get('hair_color', ''), '')
    hair_str    = " ".join(filter(None, [hair_color, hair_style]))
    makeup         = MAKEUP.get(data.get('makeup', ''), '')
    accessories    = ACCESSORIES.get(data.get('accessories', ''), '')
    skin_tone      = SKIN_TONES.get(data.get('skin_tone', ''), '')
    count_data     = MODEL_COUNT.get(data.get('model_count', '1명 — 싱글 모델 (기본)'), MODEL_COUNT['1명 — 싱글 모델 (기본)'])
    model_subject  = count_data['prompt']
    era            = ERA.get(data.get('era', ''), '')
    concept        = CONCEPT.get(data.get('concept', ''), '')
    special_fx     = SPECIAL_EFFECTS.get(data.get('special_effects', ''), '')
    img_style      = IMAGE_STYLE.get(data.get('image_style', ''), '')
    props          = PROPS.get(data.get('props', ''), '')
    body_weight    = BODY_WEIGHT.get(data.get('body_weight', ''), '')
    bust_size      = BUST_SIZE.get(data.get('bust_size', ''), '')
    hip_size       = HIP_SIZE.get(data.get('hip_size', ''), '')
    body_str       = ", ".join(filter(None, [body_weight, bust_size, hip_size]))
    appearance_desc = f"with {appearance}" if appearance else ""

    return (
        f"Professional fashion photograph, {aspect_desc}, {angle}. "
        f"{model_subject} {appearance_desc}, {model}, commanding the frame with confidence and elegance. "
        f"{'Body: ' + body_str + '. ' if body_str else ''}"
        f"{'Era: ' + era + '. ' if era else ''}"
        f"{'Concept: ' + concept + '. ' if concept else ''}"
        f"{'Skin: ' + skin_tone + '. ' if skin_tone else ''}"
        f"{'Hair: ' + hair_str + '. ' if hair_str else ''}"
        f"{'Makeup: ' + makeup + '. ' if makeup else ''}"
        f"{'Accessories: ' + accessories + '. ' if accessories else ''}"
        f"{'Props: ' + props + '. ' if props else ''}"
        f"{'Pose: ' + pose + '. ' if pose else ''}"
        f"Wearing {outfit}, crafted from {material}{', ' + footwear if footwear else ''}. "
        f"The scene unfolds at {env}, "
        f"{'Special effects: ' + special_fx + '. ' if special_fx else ''}"
        f"bathed in {light}, creating a breathtaking atmosphere. "
        f"{'Image style: ' + img_style + '. ' if img_style else ''}"
        f"Shot in the style of {style}, "
        f"captured on {camera} with razor-sharp focus on the model. "
        f"{'Color grade: ' + color_grade + '. ' if color_grade else ''}"
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
    st.markdown("### 🎬 영상 플랫폼")
    global_video_platform = st.radio(
        "영상 생성 플랫폼",
        options=["Veo 3 (Gemini)", "Kling AI", "Runway", "Hailuo"],
        index=0,
    )

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
        preset_pose = st.selectbox(
            "💃 포즈",
            [NONE] + list(POSES.keys()),
            key="preset_pose"
        )
    with col2:
        preset_color_grade = st.selectbox(
            "🎨 색감",
            [NONE] + list(COLOR_GRADES.keys()),
            key="preset_color_grade"
        )
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
        btn_ai = st.button("🤖 AI 생성", use_container_width=True, type="primary", key="preset_btn_ai")
    with col_b:
        btn_quick = st.button("⚡ 빠른 생성", use_container_width=True, key="preset_btn_quick")

    if "preset_prompt" not in st.session_state:
        st.session_state.preset_prompt = ""
    if "preset_selected" not in st.session_state:
        st.session_state.preset_selected = ""

    # 프리셋 변경 감지 → 자동 초기화
    if selected_preset != st.session_state.preset_selected:
        st.session_state.preset_selected = selected_preset
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
        if preset_pose != NONE:
            overrides['pose'] = POSES[preset_pose]
        if preset_color_grade != NONE:
            overrides['color_grade'] = COLOR_GRADES[preset_color_grade]
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
        framing_str    = overrides.get('framing', 'full body shot')
        footwear_str   = f", {overrides['footwear']}" if 'footwear' in overrides else ""
        pose_str       = f"Pose: {overrides['pose']}. " if 'pose' in overrides else ""
        color_str      = f"Color grade: {overrides['color_grade']}. " if 'color_grade' in overrides else ""

        prompt = (
            f"Professional fashion photograph, {framing_str}. "
            f"{appearance_str}"
            f"Model: {p.get('subject', 'a stunning female model')}. "
            f"Body: {p.get('body', '')}. "
            f"{pose_str}"
            f"Wearing: {p.get('outfit', '')}, made of {p.get('material', '')}{footwear_str}. "
            f"Environment: {p.get('environment', '')}. "
            f"Lighting: {p.get('lighting', '')}. "
            f"Style: {p.get('style', '')}. "
            f"{color_str}"
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
        st.session_state.r_appearance  = random.choice(list(MODEL_APPEARANCE.keys()))
        st.session_state.r_model       = random.choice(list(MODEL_TYPES.keys()))
        st.session_state.r_outfit      = random.choice(list(OUTFIT_TYPES.keys()))
        st.session_state.r_material    = random.choice(list(MATERIALS.keys()))
        st.session_state.r_footwear    = random.choice(list(FOOTWEAR.keys()))
        st.session_state.r_pose        = random.choice(list(POSES.keys()))
        st.session_state.r_color_grade = random.choice(list(COLOR_GRADES.keys()))
        st.session_state.r_hair_style  = random.choice(list(HAIR_STYLES.keys()))
        st.session_state.r_hair_color  = random.choice(list(HAIR_COLORS.keys()))
        st.session_state.r_makeup      = random.choice(list(MAKEUP.keys()))
        st.session_state.r_accessories = random.choice(list(ACCESSORIES.keys()))
        st.session_state.r_skin_tone   = random.choice(list(SKIN_TONES.keys()))
        st.session_state.r_model_count    = random.choice(list(MODEL_COUNT.keys())[:2])
        st.session_state.r_era            = "없음"
        st.session_state.r_concept        = "없음"
        st.session_state.r_special_effects = "없음"
        st.session_state.r_image_style    = "없음"
        st.session_state.r_props          = "없음"
        st.session_state.r_body_weight    = "없음"
        st.session_state.r_bust_size      = "없음"
        st.session_state.r_hip_size       = "없음"
        st.session_state.r_env         = random.choice(list(ENVIRONMENTS.keys()))
        st.session_state.r_light       = random.choice(list(LIGHTING.keys()))
        st.session_state.r_angle       = random.choice(list(CAMERA_ANGLES.keys()))
        st.session_state.r_style       = random.choice(list(STYLES.keys()))
        st.session_state.r_camera      = random.choice(list(CAMERAS.keys()))

    col1, col2 = st.columns(2)
    with col1:
        appearance  = st.selectbox("👩 모델 외모 — 인종/국적 ",     list(MODEL_APPEARANCE.keys()),   index=list(MODEL_APPEARANCE.keys()).index(st.session_state.get("r_appearance", list(MODEL_APPEARANCE.keys())[0])))
        model_type  = st.selectbox("👤 모델 타입 — 체형과 비율",    list(MODEL_TYPES.keys()),        index=list(MODEL_TYPES.keys()).index(st.session_state.get("r_model", list(MODEL_TYPES.keys())[0])))
        outfit      = st.selectbox("👗 의상 타입 — 스타일",         list(OUTFIT_TYPES.keys()),       index=list(OUTFIT_TYPES.keys()).index(st.session_state.get("r_outfit", list(OUTFIT_TYPES.keys())[0])))
        material    = st.selectbox("🧵 소재 — 옷감 질감",           list(MATERIALS.keys()),          index=list(MATERIALS.keys()).index(st.session_state.get("r_material", list(MATERIALS.keys())[0])))
        footwear    = st.selectbox("👠 신발 — 힐/부츠 스타일",      list(FOOTWEAR.keys()),           index=list(FOOTWEAR.keys()).index(st.session_state.get("r_footwear", list(FOOTWEAR.keys())[0])))
        pose        = st.selectbox("💃 포즈 — 자세와 동작",         list(POSES.keys()),              index=list(POSES.keys()).index(st.session_state.get("r_pose", list(POSES.keys())[0])))
        hair_style  = st.selectbox("💇 헤어스타일",                 list(HAIR_STYLES.keys()),        index=list(HAIR_STYLES.keys()).index(st.session_state.get("r_hair_style", list(HAIR_STYLES.keys())[0])))
        hair_color  = st.selectbox("🎨 헤어컬러",                   list(HAIR_COLORS.keys()),        index=list(HAIR_COLORS.keys()).index(st.session_state.get("r_hair_color", list(HAIR_COLORS.keys())[0])))
        makeup      = st.selectbox("💄 메이크업",                   list(MAKEUP.keys()),             index=list(MAKEUP.keys()).index(st.session_state.get("r_makeup", list(MAKEUP.keys())[0])))
        model_count = st.selectbox("👥 모델 수",                    list(MODEL_COUNT.keys()),        index=list(MODEL_COUNT.keys()).index(st.session_state.get("r_model_count", list(MODEL_COUNT.keys())[0])))
        era         = st.selectbox("🌍 시대/시간대",                 list(ERA.keys()),                index=list(ERA.keys()).index(st.session_state.get("r_era", list(ERA.keys())[0])))
        concept     = st.selectbox("🎭 컨셉/페르소나",               list(CONCEPT.keys()),            index=list(CONCEPT.keys()).index(st.session_state.get("r_concept", list(CONCEPT.keys())[0])))
        body_weight = st.selectbox("⚖️ 체중/체형",                  list(BODY_WEIGHT.keys()),        index=list(BODY_WEIGHT.keys()).index(st.session_state.get("r_body_weight", list(BODY_WEIGHT.keys())[0])))
        bust_size   = st.selectbox("👙 가슴 사이즈",                 list(BUST_SIZE.keys()),          index=list(BUST_SIZE.keys()).index(st.session_state.get("r_bust_size", list(BUST_SIZE.keys())[0])))
        hip_size    = st.selectbox("🍑 힙 사이즈",                   list(HIP_SIZE.keys()),           index=list(HIP_SIZE.keys()).index(st.session_state.get("r_hip_size", list(HIP_SIZE.keys())[0])))
    with col2:
        accessories  = st.selectbox("💍 액세서리",                   list(ACCESSORIES.keys()),        index=list(ACCESSORIES.keys()).index(st.session_state.get("r_accessories", list(ACCESSORIES.keys())[0])))
        skin_tone    = st.selectbox("🌊 피부 톤/질감",               list(SKIN_TONES.keys()),         index=list(SKIN_TONES.keys()).index(st.session_state.get("r_skin_tone", list(SKIN_TONES.keys())[0])))
        special_fx   = st.selectbox("🌈 특수 효과",                  list(SPECIAL_EFFECTS.keys()),    index=list(SPECIAL_EFFECTS.keys()).index(st.session_state.get("r_special_effects", list(SPECIAL_EFFECTS.keys())[0])))
        img_style    = st.selectbox("📐 이미지 스타일",              list(IMAGE_STYLE.keys()),        index=list(IMAGE_STYLE.keys()).index(st.session_state.get("r_image_style", list(IMAGE_STYLE.keys())[0])))
        props        = st.selectbox("🎪 특별 소품",                  list(PROPS.keys()),              index=list(PROPS.keys()).index(st.session_state.get("r_props", list(PROPS.keys())[0])))
        color_grade  = st.selectbox("🖼️ 색감 — 컬러 그레이딩",      list(COLOR_GRADES.keys()),       index=list(COLOR_GRADES.keys()).index(st.session_state.get("r_color_grade", list(COLOR_GRADES.keys())[0])))
        style        = st.selectbox("🎬 스타일 — 화보 레퍼런스",     list(STYLES.keys()),             index=list(STYLES.keys()).index(st.session_state.get("r_style", list(STYLES.keys())[0])))
        environment  = st.selectbox("🏙️ 환경 — 촬영 장소",          list(ENVIRONMENTS.keys()),       index=list(ENVIRONMENTS.keys()).index(st.session_state.get("r_env", list(ENVIRONMENTS.keys())[0])))
        lighting     = st.selectbox("💡 조명 — 빛의 분위기",         list(LIGHTING.keys()),           index=list(LIGHTING.keys()).index(st.session_state.get("r_light", list(LIGHTING.keys())[0])))
        angle        = st.selectbox("📸 카메라 앵글 — 촬영 각도",    list(CAMERA_ANGLES.keys()),      index=list(CAMERA_ANGLES.keys()).index(st.session_state.get("r_angle", list(CAMERA_ANGLES.keys())[0])))
        camera       = st.selectbox("📷 카메라 — 장비",              list(CAMERAS.keys()),            index=list(CAMERAS.keys()).index(st.session_state.get("r_camera", list(CAMERAS.keys())[0])))

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
            "pose": pose, "color_grade": color_grade,
            "hair_style": hair_style, "hair_color": hair_color,
            "makeup": makeup, "accessories": accessories,
            "skin_tone": skin_tone, "model_count": model_count,
            "era": era, "concept": concept,
            "special_effects": special_fx,
            "image_style": img_style, "props": props,
            "body_weight": body_weight,
            "bust_size": bust_size, "hip_size": hip_size,
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
            "appearance":      random.choice(list(MODEL_APPEARANCE.keys())),
            "model":           random.choice(list(MODEL_TYPES.keys())),
            "outfit":          random.choice(list(OUTFIT_TYPES.keys())),
            "material":        random.choice(list(MATERIALS.keys())),
            "footwear":        random.choice(list(FOOTWEAR.keys())),
            "pose":            random.choice(list(POSES.keys())),
            "color_grade":     random.choice(list(COLOR_GRADES.keys())),
            "hair_style":      random.choice(list(HAIR_STYLES.keys())),
            "hair_color":      random.choice(list(HAIR_COLORS.keys())),
            "makeup":          random.choice(list(MAKEUP.keys())),
            "accessories":     random.choice(list(ACCESSORIES.keys())),
            "skin_tone":       random.choice(list(SKIN_TONES.keys())),
            "model_count":     random.choice(list(MODEL_COUNT.keys())[:2]),
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
st.markdown('<div style="text-align:center;color:#444;font-size:0.75rem;">✦ LumineX v2.6 — AI Fashion Image Engine</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# 탭 4: 영상 프롬프트 (Veo 3)
# ══════════════════════════════════════════════════════════
with tab4:
    st.markdown(f"### 🎬 영상 프롬프트 생성 — {global_video_platform}")

    VIDEO_PLATFORM_TIPS = {
        "Veo 3 (Gemini)": ("🔵", "gemini.google.com", "Gemini Advanced 구독 필요. 좌측 메뉴에서 Veo 3 선택."),
        "Kling AI": ("🟡", "klingai.com", "무료 티어 사용 가능. 매일 크레딧 지급."),
        "Runway": ("🟢", "runwayml.com", "무료 크레딧 제공. Gen-3 Alpha 사용."),
        "Hailuo": ("🟠", "hailuoai.video", "완전 무료. 중국 서비스."),
    }
    color, url, tip = VIDEO_PLATFORM_TIPS[global_video_platform]
    st.info(f"{color} **{global_video_platform}** — {tip} → [{url}](https://{url})")

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
        st.markdown(f"### 💡 {global_video_platform} 사용 방법")
        if global_video_platform == "Veo 3 (Gemini)":
            st.markdown("""
1. [gemini.google.com](https://gemini.google.com) 접속
2. 좌측 **Veo 3** 선택
3. 위 프롬프트 붙여넣기
4. 생성 클릭!
            """)
        elif global_video_platform == "Kling AI":
            st.markdown("""
1. [klingai.com](https://klingai.com) 접속
2. **Text to Video** 선택
3. 위 프롬프트 붙여넣기
4. 생성 클릭!
            """)
        elif global_video_platform == "Runway":
            st.markdown("""
1. [runwayml.com](https://runwayml.com) 접속
2. **Gen-3 Alpha** 선택
3. 위 프롬프트 붙여넣기
4. 생성 클릭!
            """)
        else:  # Hailuo
            st.markdown("""
1. [hailuoai.video](https://hailuoai.video) 접속
2. **Text to Video** 선택
3. 위 프롬프트 붙여넣기
4. 생성 클릭!
            """)