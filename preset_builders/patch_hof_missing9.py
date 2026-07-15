# -*- coding: utf-8 -*-
"""
patch_hof_missing9.py
극장적 글래머 누락 9종을 core/hof_tier.py 에 추가합니다.
실행: python patch_hof_missing9.py  (프로젝트 루트에서)
"""

missing_9 = [
    "storm_cliff_goddess",
    "aurora_borealis_silk",
    "colosseum_goddess_dawn",
    "angkor_wat_silk",
    "tokyo_rainstorm_neon",
    "versailles_hall_of_mirrors",
    "volcano_lava_goddess",
    "waterfall_goddess",
    "cherry_blossom_storm",
]

path = "core/hof_tier.py"
content = open(path, encoding="utf-8").read()

# 삽입 위치: ballet_stage_noir 바로 뒤
insert_after = '    "ballet_stage_noir",'
new_lines = "\n".join(f'    "{k}",' for k in missing_9)
replacement = insert_after + "\n" + new_lines

if insert_after not in content:
    print("❌ 삽입 위치를 찾지 못했습니다.")
    exit(1)

content = content.replace(insert_after, replacement, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# 검증
import ast
try:
    ast.parse(content)
    print("✅ Syntax OK")
except SyntaxError as e:
    print(f"❌ SyntaxError: {e}")
    exit(1)

exec(content)
print(f"✅ HOF_TIER 총 {len(HOF_TIER)}종 확인")
print("📁 저장 완료: core/hof_tier.py")
