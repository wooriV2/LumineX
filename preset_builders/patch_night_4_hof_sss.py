# -*- coding: utf-8 -*-
"""
patch_night_4_hof_sss.py
나이트 글래머 신규 4종 HOF/SSS 패치
- HOF: night_bust_queen_dubai, night_powerlifter_lasvegas
- SSS: night_brazil_tokyo_neon, night_supermodel_paris_rooftop
"""

HOF_PATH  = "core/hof_tier.py"
META_PATH = "core/presets_meta.py"

HOF_NEW = [
    "night_bust_queen_dubai",
    "night_powerlifter_lasvegas",
]

SSS_NEW = [
    "night_brazil_tokyo_neon",
    "night_supermodel_paris_rooftop",
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
print("나이트 4종 HOF/SSS 패치")
print("=" * 50)

print("\n[HOF]")
with open(HOF_PATH, "r", encoding="utf-8-sig") as f:
    hof = f.read()
hof = patch_set_block(hof, "HOF_TIER = {", HOF_NEW)
with open(HOF_PATH, "w", encoding="utf-8") as f:
    f.write(hof)

print("\n[SSS]")
with open(META_PATH, "r", encoding="utf-8-sig") as f:
    meta = f.read()
meta = patch_set_block(meta, "SSS_TIER = {", SSS_NEW)
with open(META_PATH, "w", encoding="utf-8") as f:
    f.write(meta)

print("\n✅ 완료!")
