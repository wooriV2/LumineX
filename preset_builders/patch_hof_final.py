# -*- coding: utf-8 -*-
"""
HOF_TIER에 누락된 50종 최종 삽입
- 나이트 4 + 슬립드레스 3 + 애니멀프린트 4 + 극장적 30 + 공식F 9 = 50종
타깃: core/presets_meta.py
"""
from pathlib import Path

TARGET = Path("core/presets_meta.py")

HOF_INSERT = '''    # 🌙 Night Glamour
    "club_vip_neon_goddess",
    "club_rooftop_citylight",
    "micro_sequin_club",
    "rooftop_micro_night",
    # 👗 Slip Dress Glamour
    "silk_slip_dawn_hotel",
    "satin_slip_vanity_noir",
    "satin_slip_micro",
    # 🐆 Animal Print Glamour
    "leopard_power_editorial",
    "leopard_micro_studio",
    "snake_micro_marble",
    "snakeskin_latex_glam",
    # 🎭 Theatrical Glamour
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
    # 🌿 Minimal Object Cover
    "silk_ribbon_minimal",
    "tropical_flower_minimal",
    "silver_foil_minimal",
    "moss_stone_minimal",
    "crystal_geode_minimal",
    "black_feather_minimal",
    "wet_lotus_pool_minimal",
    "butterfly_wings_minimal",
    "seaweed_ocean_minimal",
'''

# HOF_TIER 블록 안 마지막 항목 바로 앞 앵커
ANCHOR = '    "trio_inside_outside_bodypaint",'

def patch():
    content = TARGET.read_text(encoding="utf-8")

    # 이미 있으면 스킵
    if '"club_vip_neon_goddess"' in content:
        # HOF_TIER 블록 안에 있는지 확인
        hof_start = content.find("HOF_TIER = {")
        hof_end = content.find("\n}", hof_start)
        hof_block = content[hof_start:hof_end]
        if '"club_vip_neon_goddess"' in hof_block:
            print("⚠️ 이미 HOF_TIER에 존재")
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
    hof_end = content.find("\n}", hof_start)
    hof_block = content[hof_start:hof_end]
    checks = ["club_vip_neon_goddess", "ballet_stage_noir", "silk_ribbon_minimal", "seaweed_ocean_minimal"]
    ok = all(f'"{k}"' in hof_block for k in checks)
    count = hof_block.count('",') + hof_block.count('",\n')
    print(f"✅ 삽입 완료 — HOF 블록 내 검증: {'✅' if ok else '❌'}")
    print('git add core/presets_meta.py; git commit -m "👑 HOF_TIER 50종 최종 삽입 (나이트/슬립/애니멀/극장적/공식F)"; git push')

if __name__ == "__main__":
    patch()
