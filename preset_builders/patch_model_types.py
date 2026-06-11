"""
preset_builders/patch_model_types.py
======================================
core/data.py MODEL_TYPES에 신규 체형 추가
- 한국인 특화 6종
- 키 특화 2종
- 체형 변형 3종
- 문화 특화 3종
- 판타지 극단 3종
총 17종 추가

실행: python preset_builders/patch_model_types.py
"""

from pathlib import Path

DATA_PATH = Path("core/data.py")

NEW_TYPES = {
    # ── 한국인 특화 ──
    "🇰🇷 K팝 아이돌 — 슬림+작은 얼굴+긴 다리": "K-pop idol proportions, extremely slim slender figure, small delicate face, disproportionately long legs, 168-172cm idol physique, flat stomach, narrow shoulders, youthful fresh Korean pop star body",
    "🇰🇷 K뷰티 순정 — 도자기 피부+가냘픈 체형": "Korean pure beauty, delicate porcelain fragile figure, very slender gentle frame, soft graceful curves, ethereal Korean feminine beauty, waif-like elegant proportions",
    "🇰🇷 걸그룹 댄서 — 탄탄+슬림 댄서 체형": "Korean girl group dancer physique, slim yet toned muscular figure, defined dancer legs, narrow waist, athletic slim silhouette with feminine grace, performance-ready body",
    "🇰🇷 울트라 코리안 슬림 — 극도로 가는 한국 체형": "ultra-slim Korean model, extremely thin delicate frame, 45-48kg editorial physique, razor-thin waist, very narrow hips, elongated fragile silhouette, high-fashion Korean editorial",
    "🇰🇷 한국 배우 글래머 — 성숙한 한국 미인": "Korean actress glamour, sophisticated mature Korean beauty proportions, elegant slim figure with subtle feminine curves, refined graceful silhouette, dramas leading lady presence",
    "🇰🇷 한국 재벌녀 — 세련된 상류층 체형": "Korean chaebol heiress physique, impeccably slim sophisticated figure, understated elegant curves, old money Korean glamour proportions, refined upper-class presence",

    # ── 키 특화 ──
    "🪆 미니어처 글래머 — 150cm 이하 초소형": "petite miniature model under 150cm, perfectly proportioned tiny figure, small delicate frame, compact glamour proportions, doll-like perfect miniature beauty",
    "🦒 수퍼모델 장신 — 185cm+ 극장신": "towering supermodel physique over 185cm, impossibly long legs taking up most of height, tiny head-to-body ratio, extreme elongated runway proportions, giraffe-like editorial height",

    # ── 체형 변형 ──
    "🏊 역삼각 — 어깨 넓고 허리 좁은": "inverted triangle physique, broad powerful shoulders dramatically narrowing to slim waist, athletic swimmer's build, strong defined shoulders, narrow hips, superhero body proportions",
    "📏 바나나 체형 — 직선형 앤드로지너스": "straight androgynous figure, shoulders waist and hips same width, minimal curves, sleek linear silhouette, high fashion androgynous editorial proportions, runway gender-fluid physique",
    "🍎 애플 체형 — 복부 중심 볼륨": "apple body shape, fuller rounded midsection, soft rounded belly as focal point, slimmer legs relative to torso, natural womanly volume centered at waist, body positive editorial",

    # ── 문화 특화 ──
    "🇯🇵 야마토 나데시코 — 가냘프고 우아한 전통 일본미": "Yamato Nadeshiko Japanese traditional beauty, extremely slender graceful figure, gentle soft curves, refined delicate proportions, classical Japanese feminine elegance, willow-like graceful silhouette",
    "🇨🇳 중국 고전미인 — 버드나무 허리": "classical Chinese beauty willow waist, impossibly slender waist like willow branch, delicate ethereal figure, Tang dynasty ideal proportions, ancient Chinese court beauty silhouette",
    "🇮🇩 발리니즈 댄서 — 가냘프고 유연한": "Balinese dancer physique, slender flexible figure, graceful elongated limbs, dancer's natural posture, Southeast Asian traditional beauty proportions, lithe artistic body",

    # ── 판타지 극단 ──
    "🧝 엘프 체형 — 극세장+긴 손발": "elven fantasy physique, impossibly elongated slender frame, extraordinarily long fingers and limbs, pointed ear aesthetic, ethereal otherworldly proportions, fantasy creature elegance, supernatural tall slender",
    "👼 치비 글래머 — 과장된 2등신 판타지": "chibi fantasy proportions, exaggerated large head to tiny body ratio, impossibly large eyes, miniature cute body, anime-inspired 2-head-height fantasy figure, adorable oversized head glamour",
    "🌌 거인 여신 — 현실 불가능한 신화적 스케일": "mythological giant goddess scale, impossibly towering divine proportions, colossal feminine figure, deity-scale body, universe-spanning goddess physique, transcendent scale beyond human",
}

print("=" * 55)
print("patch_model_types.py 시작")
print(f"추가할 체형: {len(NEW_TYPES)}종")
print("=" * 55)

content = DATA_PATH.read_text(encoding="utf-8")

# MODEL_TYPES 딕셔너리 닫는 } 찾기
# "슬라브 봄셸" 마지막 항목 뒤에 추가
ANCHOR = '    "🌹 슬라브 봄셸 — 1950s 조각 핀업 8자": "Slavic pin-up bombshell, sculpted hourglass, impossibly cinched corset waist, full high bust, wide rounded hips, retro bombshell proportions, statuesque porcelain skin",'

if ANCHOR not in content:
    print("❌ 앵커 텍스트 찾기 실패 — 수동 확인 필요")
    exit(1)

# 새 항목 생성
new_entries = "\n"
for key, value in NEW_TYPES.items():
    new_entries += f'    "{key}": "{value}",\n'

new_content = content.replace(
    ANCHOR,
    ANCHOR + new_entries
)

if new_content == content:
    print("❌ 교체 실패")
    exit(1)

DATA_PATH.write_text(new_content, encoding="utf-8")
print("✅ MODEL_TYPES 추가 완료")

# 검증
print("\n[ 검증 ]")
verify = DATA_PATH.read_text(encoding="utf-8")
for key in NEW_TYPES:
    status = "✅" if key in verify else "❌"
    print(f"  {status} {key}")

# 총 개수
import re
matches = re.findall(r'"[^"]+": "([^"]+)"', verify[verify.find("MODEL_TYPES"):verify.find("BODY_WEIGHT")])
print(f"\n  MODEL_TYPES 총 항목 수: {len(matches)}종")

print("\n완료! 커밋:")
print('  git add -A')
print('  git commit -m "feat: MODEL_TYPES 신규 체형 17종 추가 (한국/키/변형/문화/판타지)"')
print('  git push')
