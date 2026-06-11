"""
preset_builders/patch_ss_sss_update.py
========================================
1. 익스트림 글래머 SS 4종 등록
   uyuni_wet_silk, aurora_bare, antelope_light_sheer, lava_field_latex

2. SSS_TIER 딕셔너리 dashboard.py에 신설
3. body_paint_nude SSS 첫 등록

실행: python preset_builders/patch_ss_sss_update.py
"""

import re
from pathlib import Path

DASHBOARD = Path("dashboard.py")

# ── 1. SS 4종 추가 ────────────────────────────────────────
NEW_SS = [
    "uyuni_wet_silk",
    "aurora_bare",
    "antelope_light_sheer",
    "lava_field_latex",
]

# ── 2. SSS 초기 멤버 ──────────────────────────────────────
NEW_SSS = [
    "body_paint_nude",
]

print("=" * 55)
print("patch_ss_sss_update.py 시작")
print("=" * 55)

content = DASHBOARD.read_text(encoding="utf-8")

# ── SS_TIER에 4종 추가 ────────────────────────────────────
ss_match = re.search(r'(SS_TIER\s*=\s*\{)([^}]+)(\})', content, re.DOTALL)
if not ss_match:
    print("❌ SS_TIER 블록 찾기 실패")
    exit(1)

ss_block = ss_match.group(2)
already = [p for p in NEW_SS if p in ss_block]
to_add  = [p for p in NEW_SS if p not in ss_block]

if already:
    print(f"SS 이미 등록됨 (스킵): {already}")

if to_add:
    new_entries = "\n" + "\n".join(f'    "{p}",' for p in to_add)
    content = content.replace(
        ss_match.group(0),
        ss_match.group(1) + ss_block.rstrip() + new_entries + "\n" + ss_match.group(3)
    )
    print(f"✅ SS_TIER 추가: {to_add}")

# ── SSS_TIER 딕셔너리 신설 ────────────────────────────────
if "SSS_TIER" in content:
    print("⚠️  SSS_TIER 이미 존재 — 항목만 추가")
    sss_match = re.search(r'(SSS_TIER\s*=\s*\{)([^}]+)(\})', content, re.DOTALL)
    if sss_match:
        sss_block = sss_match.group(2)
        to_add_sss = [p for p in NEW_SSS if p not in sss_block]
        if to_add_sss:
            new_entries = "\n" + "\n".join(f'    "{p}",' for p in to_add_sss)
            content = content.replace(
                sss_match.group(0),
                sss_match.group(1) + sss_block.rstrip() + new_entries + "\n" + sss_match.group(3)
            )
            print(f"✅ SSS_TIER 추가: {to_add_sss}")
else:
    # SS_TIER 블록 바로 앞에 SSS_TIER 삽입
    sss_entries = "\n".join(f'    "{p}",' for p in NEW_SSS)
    sss_block = f'''
# SSS tier — "이게 AI야?" 수준. 스크롤 완전 정지. 4박자 완벽 + 차별성
# 기준: 체형 오버라이드만으로 문화/패턴/포즈 자동완성, 2장 이상 일관성, 독보적 임팩트
SSS_TIER = {{
{sss_entries}
}}

'''
    # SS_TIER 앞에 삽입
    content = content.replace("# SS tier", sss_block + "# SS tier", 1)
    if "SSS_TIER" not in content:
        # fallback: SS_TIER = { 바로 앞에 삽입
        content = content.replace("SS_TIER = {", sss_block + "SS_TIER = {", 1)
    print(f"✅ SSS_TIER 딕셔너리 신설 + body_paint_nude 등록")

# ── 저장 ──────────────────────────────────────────────────
DASHBOARD.write_text(content, encoding="utf-8")

# ── 검증 ──────────────────────────────────────────────────
print("\n[ 검증 ]")
verify = DASHBOARD.read_text(encoding="utf-8")

ss_match2 = re.search(r'SS_TIER\s*=\s*\{([^}]+)\}', verify, re.DOTALL)
ss_block2 = ss_match2.group(1) if ss_match2 else ""
for p in NEW_SS:
    status = "✅" if p in ss_block2 else "❌"
    print(f"  {status} SS: {p}")

sss_ok = "SSS_TIER" in verify
sss_body = "body_paint_nude" in verify
print(f"  {'✅' if sss_ok else '❌'} SSS_TIER 딕셔너리 존재")
print(f"  {'✅' if sss_body else '❌'} SSS: body_paint_nude")

ss_count = len(re.findall(r'"[\w_]+"', ss_block2))
print(f"\n  SS_TIER 총 항목 수: {ss_count}개")
print(f"  SSS_TIER 총 항목 수: {len(NEW_SSS)}개")

print("\n완료! 커밋:")
print('  git add -A')
print('  git commit -m "feat: 익스트림글래머 SS 4종 + SSS_TIER 신설 + body_paint_nude SSS 등록"')
print('  git push')
