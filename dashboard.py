"""
LumineX Dashboard v3.3 - 리팩토링: 데이터/로직 분리
실행: streamlit run dashboard.py
"""

import sys
import random
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from core.engine import list_presets, load_preset, build_prompt
from core.prompt_generator import generate_prompt_with_ai
from core.data import (
    ASPECT_RATIOS,
    MODEL_APPEARANCE, AGE_APPEARANCE, MODEL_TYPES,
    BODY_WEIGHT, BUST_SIZE, HIP_SIZE,
    OUTFIT_TYPES, MATERIALS, ENVIRONMENTS, STYLES,
    LIGHTING, CAMERA_ANGLES, FOOTWEAR, CAMERAS,
    HAIR_STYLES, HAIR_COLORS, MODEL_COUNT,
    ERA, CONCEPT, SPECIAL_EFFECTS, IMAGE_STYLE, PROPS,
    MAKEUP, ACCESSORIES, SKIN_TONES,
    POSES, WEATHER, EXPRESSION, TATTOO, BODY_OIL, BG_CROWD,
    COLOR_GRADES,
)
from core.combos import GOOD_COMBOS, CONFLICT_RULES, check_conflicts, get_combo_recommendations
from core.builders import build_gemini_prompt, build_chatgpt_prompt, build_midjourney_prompt

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
        def rnd(d):
            """없음 제외하고 랜덤 뽑기"""
            keys = [k for k in d.keys() if k != "없음"]
            return random.choice(keys) if keys else "없음"

        # 고정 섹션 — 항상 랜덤
        st.session_state.r_appearance  = rnd(MODEL_APPEARANCE)
        st.session_state.r_model       = rnd(MODEL_TYPES)
        st.session_state.r_outfit      = rnd(OUTFIT_TYPES)
        st.session_state.r_material    = rnd(MATERIALS)
        st.session_state.r_env         = rnd(ENVIRONMENTS)
        st.session_state.r_light       = rnd(LIGHTING)
        st.session_state.r_angle       = rnd(CAMERA_ANGLES)
        st.session_state.r_style       = rnd(STYLES)
        st.session_state.r_camera      = rnd(CAMERAS)
        st.session_state.r_pose        = rnd(POSES)
        st.session_state.r_expression  = rnd(EXPRESSION)
        st.session_state.r_skin_tone   = rnd(SKIN_TONES)
        st.session_state.r_hair_style  = rnd(HAIR_STYLES)
        st.session_state.r_hair_color  = rnd(HAIR_COLORS)
        st.session_state.r_makeup      = rnd(MAKEUP)

        # 확률 섹션 — 50% 랜덤, 50% 없음
        def rnd_maybe(d, prob=0.5):
            return rnd(d) if random.random() < prob else "없음"

        st.session_state.r_footwear        = rnd_maybe(FOOTWEAR,       0.50)
        st.session_state.r_color_grade     = rnd_maybe(COLOR_GRADES,   0.50)
        st.session_state.r_accessories     = rnd_maybe(ACCESSORIES,    0.40)
        st.session_state.r_body_oil        = rnd_maybe(BODY_OIL,       0.30)
        st.session_state.r_weather         = rnd_maybe(WEATHER,        0.30)
        st.session_state.r_bg_crowd        = rnd_maybe(BG_CROWD,       0.30)
        st.session_state.r_tattoo          = rnd_maybe(TATTOO,         0.15)
        st.session_state.r_special_effects = rnd_maybe(SPECIAL_EFFECTS,0.15)
        st.session_state.r_props           = rnd_maybe(PROPS,          0.15)
        st.session_state.r_image_style     = rnd_maybe(IMAGE_STYLE,    0.15)
        st.session_state.r_era             = rnd_maybe(ERA,            0.15)
        st.session_state.r_concept         = rnd_maybe(CONCEPT,        0.15)

        # 보정 섹션 — 기본 없음
        st.session_state.r_age         = "없음"
        st.session_state.r_model_count = "1명 — 싱글 모델 (기본)"
        st.session_state.r_body_weight = "없음"
        st.session_state.r_bust_size   = "없음"
        st.session_state.r_hip_size    = "없음"
        st.rerun()

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