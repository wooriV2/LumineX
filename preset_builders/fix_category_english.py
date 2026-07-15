# -*- coding: utf-8 -*-
"""
core/presets_meta.py 카테고리명 영어로 일괄 변환
- 깨진 인코딩 수정 + 영어 카테고리명 적용
- PRESET_CATEGORIES dict key + HOF/SSS/SS 주석 내 카테고리명 모두 변환
실행: python preset_builders/fix_category_english.py (프로젝트 루트에서)
"""
from pathlib import Path
import re

TARGET = Path("core/presets_meta.py")

# 한글 → 영어 매핑 (줄번호 무관, 문자열 치환)
CATEGORY_MAP = {
    "🖌️ 바디페인팅 & 스킨 트랜스폼": "🖌️ Body Paint & Skin Transform",
    "💫 럭셔리 글래머":               "💫 Luxury Glamour",
    "🔥 핫 & 섹시":                   "🔥 Hot & Sexy",
    "💋 에로틱 & 페티쉬":             "💋 Erotic & Fetish",
    "🌿 자연 & 원소":                 "🌿 Nature & Elements",
    "🌃 도시 & 나이트":               "🌃 City & Night",
    "🎬 에디토리얼 & 무드":           "🎬 Editorial & Mood",
    "🏺 문명 & 신화":                 "🏺 Civilization & Myth",
    "✈️ 직업 & 라이프스타일":          "✈️ Career & Lifestyle",
    "🔮 판타지 & 다크":               "🔮 Fantasy & Dark",
    "⚔️ 파워 & 엣지":                 "⚔️ Power & Edge",
    "🏖️ 비치 & 리조트":               "🏖️ Beach & Resort",
    "🎭 퍼포먼스 & 댄스":             "🎭 Performance & Dance",
    "👘 전통 & 문화의상":             "👘 Traditional Costume",
    "🌸 계절 & 테마":                 "🌸 Season & Theme",
    "🍬 팝 & 카와이":                 "🍬 Pop & Kawaii",
    "🎌 애니 & 글래머":               "🎌 Anime & Glamour",
    "🎨 애니 아트스타일":             "🎨 Anime Art Style",
    "🌑 실루엣 & 섀도우":             "🌑 Silhouette & Shadow",
    "🌌 불가능 & 초현실":             "🌌 Impossible & Surreal",
    "🏛️ 유적 & 문명":                 "🏛️ Ruins & Civilization",
    "🌋 엘리멘탈 갓데스":             "🌋 Elemental Goddess",
    "💧 웨트 & 글로스":               "💧 Wet & Gloss",
    "🌫️ 대기 & 파티클":               "🌫️ Atmosphere & Particle",
    "👑 한국 역사 & 궁중 글래머":     "👑 Korean History & Court",
    "🎨 멀티 바디페인팅":             "🎨 Multi Body Paint",
    "👯 듀오 글래머":                 "👯 Duo Glamour",
    "🪞 거울 & 반사 글래머":          "🪞 Mirror & Reflection",
    "🧬 SF & 바이오펑크":             "🧬 Sci-Fi & Biopunk",
    "🌀 환경 일체 바디페인팅":        "🌀 Environment Merge",
    "🌙 나이트 글래머":               "🌙 Night Glamour",
    "👗 슬립드레스 글래머":           "👗 Slip Dress Glamour",
    "🐆 애니멀프린트 글래머":         "🐆 Animal Print Glamour",
    "🎭 극장적 글래머":               "🎭 Theatrical Glamour",
    "🌿 미니멀 오브제 커버":          "🌿 Minimal Object Cover",
    "🎀 미니멀 커버 글래머":          "🎀 Minimal Cover Glamour",
    "🛁 스파 & 바디 글래머":          "🛁 Spa & Body Glamour",
    "🌋 자연 온천 & 수중":            "🌋 Hot Spring & Underwater",
    "💦 풀 & 이머전스":               "💦 Pool & Emergence",
    "🌧️ 웨트 드레스 글래머":          "🌧️ Wet Dress Glamour",
}

# 깨진 줄번호 → 올바른 영어 줄 (인코딩 깨진 것은 줄번호로 직접 교체)
BROKEN_LINE_FIXES = {
    11:   '    "🖌️ Body Paint & Skin Transform": [',
    127:  '    "💫 Luxury Glamour": [',
    150:  '    "🔥 Hot & Sexy": [',
    197:  '    "💋 Erotic & Fetish": [',
    231:  '    "🌿 Nature & Elements": [',
    248:  '    "🌃 City & Night": [',
    262:  '    "🎬 Editorial & Mood": [',
    279:  '    "🏺 Civilization & Myth": [',
    297:  '    "✈️ Career & Lifestyle": [',
    309:  '    "🔮 Fantasy & Dark": [',
    318:  '    "⚔️ Power & Edge": [',
    367:  '    "🏖️ Beach & Resort": [',
    375:  '    "🎭 Performance & Dance": [',
    384:  '    "👘 Traditional Costume": [',
    398:  '    "🌸 Season & Theme": [',
    407:  '    "🍬 Pop & Kawaii": [',
    423:  '    "🎌 Anime & Glamour": [',
    441:  '    "🎨 Anime Art Style": [',
    476:  '    "🌑 Silhouette & Shadow": [',
    509:  '        "🌌 Impossible & Surreal": [',
    541:  '    "🏛️ Ruins & Civilization": [',
    550:  '    "🌋 Elemental Goddess": [',
    595:  '    "💧 Wet & Gloss": [',
    629:  '    "🌫️ Atmosphere & Particle": [',
    648:  '    "👑 Korean History & Court": [',
    687:  '    "🎨 Multi Body Paint": [',
    915:  '    "👯 Duo Glamour": [',
    953:  '    "🪞 Mirror & Reflection": [',
    984:  '    "🧬 Sci-Fi & Biopunk": [',
    1014: '    "🌀 Environment Merge": [',
    1064: "            \"🌙 Night Glamour\": ['club_vip_neon_goddess', 'club_rooftop_citylight', 'micro_sequin_club', 'rooftop_micro_night'],",
    1065: "        \"👗 Slip Dress Glamour\": ['silk_slip_dawn_hotel', 'satin_slip_vanity_noir', 'satin_slip_micro'],",
    1066: "        \"🐆 Animal Print Glamour\": ['leopard_power_editorial', 'leopard_micro_studio', 'snake_micro_marble', 'snakeskin_latex_glam'],",
    1067: "    \"🎭 Theatrical Glamour\": ['gyeongbokgung_night_couture', 'bukchon_rain_editorial', 'namsan_tower_dusk', 'dongdaemun_neon_rain', 'haeinsa_temple_dawn', 'jeju_volcanic_coast', 'fushimi_inari_crimson', 'arashiyama_bamboo_mist', 'osaka_dotonbori_neon', 'mount_fuji_dawn_silk', 'japanese_garden_autumn', 'kabukiza_backstage_glam', 'forbidden_city_golden_hour', 'li_river_karst_mist', 'shanghai_bund_noir', 'zhangjiajie_cloud_forest', 'west_lake_lotus_dawn', 'bali_tanah_lot_sunset', 'hoi_an_lantern_rain', 'bangkok_wat_arun_gold', 'singapore_marina_bay_night', 'luang_prabang_monk_dawn', 'rice_terrace_banaue_mist', 'opera_house_goddess', 'venetian_carnival_palazzo', 'flamenco_tablao_fire', 'broadway_red_curtain', 'scottish_castle_mist', 'sahara_dune_queen', 'ballet_stage_noir'],",
    1068: '    "🌿 Minimal Object Cover": [',
    1079: '    "🎀 Minimal Cover Glamour": [',
    1099: '    "🛁 Spa & Body Glamour": [',
    1112: '    "🌋 Hot Spring & Underwater": [',
    1124: '    "💦 Pool & Emergence": [',
    1131: '    "🌧️ Wet Dress Glamour": [',
}

def fix():
    lines = TARGET.read_text(encoding="utf-8").splitlines(keepends=True)

    # 1단계: 깨진 줄 직접 교체
    broken_fixed = 0
    for lineno, correct in BROKEN_LINE_FIXES.items():
        idx = lineno - 1
        if idx < len(lines):
            lines[idx] = correct + "\n"
            broken_fixed += 1

    content = "".join(lines)

    # 2단계: 정상 한글 카테고리명 → 영어 치환
    korean_fixed = 0
    for kor, eng in CATEGORY_MAP.items():
        if kor in content:
            content = content.replace(kor, eng)
            korean_fixed += 1

    TARGET.write_text(content, encoding="utf-8")
    print(f"✅ 깨진 줄 직접 교체: {broken_fixed}개")
    print(f"✅ 한글→영어 치환: {korean_fixed}개")

    # 검증
    final = TARGET.read_text(encoding="utf-8")
    broken_remain = len(re.findall(r'"[^"]*[\uAC00-\uD7A3][^"]*":\s*\[', final))
    broken_encoded = len(re.findall(r'"\?[^"]*":\s*\[', final))
    print(f"\n검증:")
    print(f"  잔존 한글 카테고리명: {broken_remain}개 {'✅' if broken_remain == 0 else '⚠️'}")
    print(f"  잔존 깨진 카테고리명: {broken_encoded}개 {'✅' if broken_encoded == 0 else '⚠️'}")

    if broken_remain == 0 and broken_encoded == 0:
        print("\n🎉 완료! 커밋:")
        print('git add core/presets_meta.py; git commit -m "🔧 카테고리명 전체 영어 변환 + 인코딩 수정"; git push')

if __name__ == "__main__":
    fix()
