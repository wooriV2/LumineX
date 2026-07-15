# -*- coding: utf-8 -*-
"""
HOF_TIER 누락 41종 패치
나이트글래머 4 + 슬립드레스 3 + 애니멀프린트 4 + 극장적글래머 30
타깃: core/presets_meta.py
실행: python preset_builders/patch_hof_missing.py (프로젝트 루트에서)
"""
from pathlib import Path

TARGET = Path("core/presets_meta.py")

HOF_INSERT = '''    # 🌙 나이트 글래머
    "club_vip_neon_goddess",
    "club_rooftop_citylight",
    "micro_sequin_club",
    "rooftop_micro_night",
    # 👗 슬립드레스 글래머
    "silk_slip_dawn_hotel",
    "satin_slip_vanity_noir",
    "satin_slip_micro",
    # 🐆 애니멀프린트 글래머
    "leopard_power_editorial",
    "leopard_micro_studio",
    "snake_micro_marble",
    "snakeskin_latex_glam",
    # 🎭 극장적 글래머
    "gyeongbokgung_night_couture",
    "bukchon_rain_editorial",
    "namsan_tower_dusk",
    "dongdaemun_neon_rain",
    "haeinsa_temple_dawn",
    "jeju_volcanic_coast",
    "fushimi_inari_crimson",
    "arashiyama_bamboo_mist",
    "osaka_dotonbori_neon",
    "mount_fuji_dawn_silk",
    "japanese_garden_autumn",
    "kabukiza_backstage_glam",
    "forbidden_city_golden_hour",
    "li_river_karst_mist",
    "shanghai_bund_noir",
    "zhangjiajie_cloud_forest",
    "west_lake_lotus_dawn",
    "bali_tanah_lot_sunset",
    "hoi_an_lantern_rain",
    "bangkok_wat_arun_gold",
    "singapore_marina_bay_night",
    "luang_prabang_monk_dawn",
    "rice_terrace_banaue_mist",
    "opera_house_goddess",
    "venetian_carnival_palazzo",
    "flamenco_tablao_fire",
    "broadway_red_curtain",
    "scottish_castle_mist",
    "sahara_dune_queen",
    "ballet_stage_noir",
'''

# HOF_TIER 블록 안의 첫 항목 앞에 삽입
ANCHOR = '    "amalfi_cliff_storm",'

def patch():
    content = TARGET.read_text(encoding="utf-8")

    # 이미 패치됐는지 확인
    if '"club_vip_neon_goddess"' in content:
        # HOF_TIER 안에 있는지 확인 (SSS_TIER에만 있을 수 있음)
        hof_start = content.find("HOF_TIER = {")
        hof_end   = content.find("\n}", hof_start)
        hof_block = content[hof_start:hof_end]
        if '"club_vip_neon_goddess"' in hof_block:
            print("⚠️  이미 HOF_TIER에 존재 — 스킵")
            return

    idx = content.find(ANCHOR)
    if idx == -1:
        print(f"❌ 앵커 미발견: {ANCHOR}")
        return

    line_start = content.rfind("\n", 0, idx) + 1
    content = content[:line_start] + HOF_INSERT + content[line_start:]
    TARGET.write_text(content, encoding="utf-8")

    # 검증
    hof_start = content.find("HOF_TIER = {")
    hof_end   = content.find("\n}", hof_start)
    hof_block = content[hof_start:hof_end]

    checks = [
        "club_vip_neon_goddess", "silk_slip_dawn_hotel",
        "leopard_power_editorial", "gyeongbokgung_night_couture",
        "ballet_stage_noir",
    ]
    ok = all(f'"{k}"' in hof_block for k in checks)
    print(f"✅ HOF_TIER 41종 삽입 완료 — 검증: {'✅' if ok else '❌'}")
    print("\n다음 명령으로 커밋하세요:")
    print('git add core/presets_meta.py; git commit -m "🔧 HOF_TIER 누락 41종 추가 (나이트/슬립드레스/애니멀프린트/극장적)"; git push')

if __name__ == "__main__":
    patch()
