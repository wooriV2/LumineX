# -*- coding: utf-8 -*-
"""
HOF_TIER 밖에 잘못 삽입된 블록 제거 스크립트
타깃: core/presets_meta.py
"""
from pathlib import Path
import re

TARGET = Path("core/presets_meta.py")

# HOF에 있어야 할 41종 키
HOF_KEYS = [
    "club_vip_neon_goddess","club_rooftop_citylight","micro_sequin_club","rooftop_micro_night",
    "silk_slip_dawn_hotel","satin_slip_vanity_noir","satin_slip_micro",
    "leopard_power_editorial","leopard_micro_studio","snake_micro_marble","snakeskin_latex_glam",
    "gyeongbokgung_night_couture","bukchon_rain_editorial","namsan_tower_dusk","dongdaemun_neon_rain",
    "haeinsa_temple_dawn","jeju_volcanic_coast","fushimi_inari_crimson","arashiyama_bamboo_mist",
    "osaka_dotonbori_neon","mount_fuji_dawn_silk","japanese_garden_autumn","kabukiza_backstage_glam",
    "forbidden_city_golden_hour","li_river_karst_mist","shanghai_bund_noir","zhangjiajie_cloud_forest",
    "west_lake_lotus_dawn","bali_tanah_lot_sunset","hoi_an_lantern_rain","bangkok_wat_arun_gold",
    "singapore_marina_bay_night","luang_prabang_monk_dawn","rice_terrace_banaue_mist",
    "opera_house_goddess","venetian_carnival_palazzo","flamenco_tablao_fire","broadway_red_curtain",
    "scottish_castle_mist","sahara_dune_queen","ballet_stage_noir",
]

def find_tier_bounds(lines, tier_name):
    """tier_name = {  ...  } 블록의 시작/끝 줄 index 반환"""
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith(f"{tier_name} = {{"):
            start = i
            break
    if start is None:
        return None, None
    depth = 0
    for i in range(start, len(lines)):
        depth += lines[i].count("{") - lines[i].count("}")
        if depth <= 0 and i > start:
            return start, i
    return start, len(lines)-1

def cleanup():
    lines = TARGET.read_text(encoding="utf-8").splitlines(keepends=True)

    hof_start, hof_end = find_tier_bounds(lines, "HOF_TIER")
    sss_start, sss_end = find_tier_bounds(lines, "SSS_TIER")
    ss_start,  ss_end  = find_tier_bounds(lines, "SS_TIER")

    print(f"HOF_TIER: {hof_start+1}~{hof_end+1}줄")
    print(f"SSS_TIER: {sss_start+1}~{sss_end+1}줄")
    print(f"SS_TIER:  {ss_start+1}~{ss_end+1}줄")

    # 보호 구간 — 이 범위 안의 키는 건드리지 않음
    protected = set(range(hof_start, hof_end+1)) | \
                set(range(sss_start, sss_end+1)) | \
                set(range(ss_start,  ss_end+1))

    # HOF 키가 보호 구간 밖에 있는 줄 찾기
    key_pattern = re.compile(r'^\s*"(' + '|'.join(re.escape(k) for k in HOF_KEYS) + r')",?\s*$')
    comment_pattern = re.compile(r'^\s*#.*?(나이트|슬립드레스|애니멀프린트|극장적|2026-07-07).*$')

    # 제거할 줄 범위 탐지: 보호 밖에서 HOF 키 연속 블록 찾기
    to_remove = set()
    i = 0
    while i < len(lines):
        if i not in protected:
            if key_pattern.match(lines[i]) or comment_pattern.match(lines[i]):
                # 이 줄부터 연속된 HOF 키/관련 주석 블록 탐지
                block_start = i
                # 앞으로 빈줄+주석도 포함해서 블록 시작 확장
                j = i
                while j < len(lines) and j not in protected:
                    stripped = lines[j].strip()
                    if key_pattern.match(lines[j]) or comment_pattern.match(lines[j]) or stripped == "":
                        to_remove.add(j)
                        j += 1
                    else:
                        break
                i = j
                continue
        i += 1

    if not to_remove:
        print("⚠️  제거 대상 없음")
        return

    print(f"제거 대상: {len(to_remove)}줄 — {min(to_remove)+1}~{max(to_remove)+1}줄")

    new_lines = [line for i, line in enumerate(lines) if i not in to_remove]
    TARGET.write_text("".join(new_lines), encoding="utf-8")
    print("✅ 정리 완료")

    # 검증
    new_lines_text = TARGET.read_text(encoding="utf-8")
    remaining = sum(1 for k in HOF_KEYS if new_lines_text.count(f'"{k}"') > 1)
    print(f"중복 잔존: {remaining}개 {'✅' if remaining == 0 else '⚠️ 수동 확인 필요'}")

if __name__ == "__main__":
    cleanup()
