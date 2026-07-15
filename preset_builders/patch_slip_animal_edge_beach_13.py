# -*- coding: utf-8 -*-
"""
patch_slip_animal_edge_beach_13.py
HOF 4종 / SSS 9종 패치
"""

HOF_PATH  = "core/hof_tier.py"
META_PATH = "core/presets_meta.py"

HOF_NEW = [
    "animal_supermodel_python_gown",
    "edge_supermodel_neon_warrior",
    "edge_bbw_steampunk_corset",
    "beach_powerlifter_seychelles",
]

SSS_NEW = [
    "slip_brazil_paris_apartment",
    "slip_colombia_morocco_riad",
    "slip_powerlifter_onsen",
    "animal_miniature_ocelot_mini",
    "animal_colombia_giraffe_bodycon",
    "edge_bust_queen_cyber_armor",
    "edge_miniature_spike_latex",
    "beach_bust_queen_amalfi",
    "beach_supermodel_palawan",
]


def patch_set_block(content, anchor, new_items):
    start = content.find(anchor)
    if start == -1:
        raise ValueError(f"앵커 없음: {anchor!r}")
    depth, i, end = 0, start, -1
    while i < len(content):
        if content[i] == '{': depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0: end = i; break
        i += 1
    if end == -1:
        raise ValueError("블록 닫기 } 없음")
    body = content[start:end]
    to_add = [k for k in new_items if f'"{k}"' not in body and f"'{k}'" not in body]
    if not to_add:
        print("  추가할 항목 없음 (모두 이미 존재)")
        return content
    insert = "\n" + "".join(f'    "{k}",\n' for k in to_add)
    print(f"  {len(to_add)}종 추가: {to_add}")
    return content[:end] + insert + content[end:]


print("=" * 50)
print("슬립/애니멀/엣지/비치 13종 HOF/SSS 패치")
print("=" * 50)

print(f"\n[HOF] {len(HOF_NEW)}종")
with open(HOF_PATH, "r", encoding="utf-8-sig") as f:
    hof = f.read()
hof = patch_set_block(hof, "HOF_TIER = {", HOF_NEW)
with open(HOF_PATH, "w", encoding="utf-8") as f:
    f.write(hof)

print(f"\n[SSS] {len(SSS_NEW)}종")
with open(META_PATH, "r", encoding="utf-8-sig") as f:
    meta = f.read()
meta = patch_set_block(meta, "SSS_TIER = {", SSS_NEW)
with open(META_PATH, "w", encoding="utf-8") as f:
    f.write(meta)

print("\n✅ 완료!")
