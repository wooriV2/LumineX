# -*- coding: utf-8 -*-
"""
patch_milf_41_75_hof_sss.py
- core/hof_tier.py  : HOF_TIER에 19종 추가
- core/presets_meta.py : SSS_TIER에 22종 추가, SS_TIER에 6종 추가
"""

HOF_PATH  = "core/hof_tier.py"
META_PATH = "core/presets_meta.py"

# ── HOF 19종 ─────────────────────────────────────────────────────
HOF_NEW = [
    "milf_korean_oil_body_studio",
    "milf_korean_jeweled_micro_gala",
    "milf_korean_micro_wrap_sunset",
    "milf_korean_wet_silk_onsen",
    "milf_korean_micro_swimsuit_yacht",
    "milf_korean_micro_bikini_snow",
    "milf_korean_colombian_neon_alley",
    "milf_korean_amazon_rooftop_storm",
    "milf_korean_amazon_beach_power",
    "milf_korean_amazon_gladiator_ruins",
    "milf_korean_bust_queen_corset_latex",
    "milf_korean_bust_queen_micro_bandeau",
    "milf_korean_powerlifter_titanium",
    "milf_korean_powerlifter_beach",
    "milf_korean_powerlifter_latex_studio",
    "milf_korean_supermodel_runway",
    "milf_korean_supermodel_jeju_cliff",
    "milf_korean_thick_boudoir_lace",
    "milf_korean_thick_micro_bikini_pool",
]

# ── SSS 22종 ─────────────────────────────────────────────────────
SSS_NEW = [
    "milf_korean_micro_shorts_neon_bar",
    "milf_korean_deep_back_plunge_dinner",
    "milf_korean_cutout_dress_night",
    "milf_korean_colombian_beach_sunset",
    "milf_korean_colombian_latex_club",
    "milf_korean_bust_queen_deep_plunge_gala",
    "milf_korean_bbw_jazz_stage",
    "milf_korean_bbw_penthouse_velvet",
    "milf_korean_bbw_beach_kaftan",
    "milf_korean_bbw_latex_bodycon",
    "milf_korean_miniature_penthouse",
    "milf_korean_miniature_latex_studio",
    "milf_korean_miniature_beach_sunset",
    "milf_korean_supermodel_penthouse_window",
    "milf_korean_thick_latex_neon",
    "milf_korean_thick_boudoir_lace",   # SSS도 등록 (HOF 중복 허용)
    "milf_korean_amazon_rooftop_storm",  # SSS도 등록
    "milf_korean_wet_silk_onsen",
    "milf_korean_jeweled_micro_gala",
    "milf_korean_powerlifter_beach",
    "milf_korean_colombian_neon_alley",
    "milf_korean_bbw_beach_kaftan",
]

# 중복 제거
SSS_NEW = list(dict.fromkeys(SSS_NEW))

# HOF에 있는 것은 SSS에서 제외 (HOF가 상위)
SSS_NEW = [k for k in SSS_NEW if k not in HOF_NEW]

# ── SS 6종 ──────────────────────────────────────────────────────
SS_NEW = [
    "milf_korean_deep_back_plunge_dinner",   # 이미지7
    "milf_korean_colombian_beach_sunset",    # 이미지3
    "milf_korean_colombian_latex_club",      # 이미지5
    "milf_korean_bust_queen_deep_plunge_gala",
    "milf_korean_miniature_latex_studio",    # 이미지9
    "milf_korean_supermodel_penthouse_window", # 이미지4
]

# SS에서 SSS/HOF 중복 제거
SS_NEW = [k for k in SS_NEW if k not in HOF_NEW and k not in SSS_NEW]


def patch_set_block(content: str, block_anchor: str, new_items: list) -> str:
    start_idx = content.find(block_anchor)
    if start_idx == -1:
        raise ValueError(f"앵커를 찾을 수 없음: {block_anchor!r}")

    brace_depth = 0
    i = start_idx
    block_end = -1
    while i < len(content):
        if content[i] == '{':
            brace_depth += 1
        elif content[i] == '}':
            brace_depth -= 1
            if brace_depth == 0:
                block_end = i
                break
        i += 1

    if block_end == -1:
        raise ValueError(f"블록 닫기 }} 를 찾을 수 없음")

    block_body = content[start_idx:block_end]
    to_add = []
    for key in new_items:
        if f'"{key}"' in block_body or f"'{key}'" in block_body:
            print(f"  [SKIP] 이미 존재: {key}")
        else:
            to_add.append(key)

    if not to_add:
        print("  추가할 항목 없음 (모두 이미 존재)")
        return content

    insert_str = "\n" + "".join(f'    "{k}",\n' for k in to_add)
    new_content = content[:block_end] + insert_str + content[block_end:]
    print(f"  {len(to_add)}종 추가 완료")
    return new_content


print("=" * 60)
print("패치 시작: MILF 41~75종 HOF/SSS/SS")
print("=" * 60)

# HOF 패치
print(f"\n[HOF_TIER] 대상 {len(HOF_NEW)}종 →", HOF_PATH)
with open(HOF_PATH, "r", encoding="utf-8-sig") as f:
    hof_content = f.read()
hof_content = patch_set_block(hof_content, "HOF_TIER = {", HOF_NEW)
with open(HOF_PATH, "w", encoding="utf-8") as f:
    f.write(hof_content)

# SSS 패치
print(f"\n[SSS_TIER] 대상 {len(SSS_NEW)}종 →", META_PATH)
with open(META_PATH, "r", encoding="utf-8-sig") as f:
    meta_content = f.read()
meta_content = patch_set_block(meta_content, "SSS_TIER = {", SSS_NEW)

# SS 패치
print(f"\n[SS_TIER] 대상 {len(SS_NEW)}종 →", META_PATH)
meta_content = patch_set_block(meta_content, "SS_TIER = {", SS_NEW)

with open(META_PATH, "w", encoding="utf-8") as f:
    f.write(meta_content)

print()
print("=" * 60)
print(f"✅ 완료! HOF {len(HOF_NEW)}종 / SSS {len(SSS_NEW)}종 / SS {len(SS_NEW)}종")
print("=" * 60)
