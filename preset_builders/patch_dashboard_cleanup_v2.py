# -*- coding: utf-8 -*-
"""
dashboard.py 정리 패치 v2
1. footer 4개 → 1개 (줄 번호 기반)
2. stray markdown("---") 제거
3. tab4/tab5 순서 교체 (블록 경계 정확히 찾기)

실행: python preset_builders\patch_dashboard_cleanup_v2.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path
import re

DASHBOARD = Path("dashboard.py")
text = DASHBOARD.read_text(encoding="utf-8")
lines = text.splitlines()

print(f"시작: {len(lines)}줄")

# ─────────────────────────────────────────────────────────
# 1. 모든 with tabN: 위치 파악
# ─────────────────────────────────────────────────────────
tab_lines = {}
for i, l in enumerate(lines):
    m = re.match(r'^with (tab\d):', l.strip())
    if m:
        tab_name = m.group(1)
        if tab_name not in tab_lines:
            tab_lines[tab_name] = i  # 0-indexed
        print(f"  발견: line {i+1}: with {tab_name}:")

# ─────────────────────────────────────────────────────────
# 2. footer 위치 파악
# ─────────────────────────────────────────────────────────
footer_indices = [i for i, l in enumerate(lines) if 'LumineX v4.4' in l]
print(f"\nfooter 위치 (0-indexed): {[i+1 for i in footer_indices]}")

# ─────────────────────────────────────────────────────────
# 3. 블록 경계 정의
#    tab3 끝 ~ tab5 시작: stray markdown + tab5 블록
#    tab5 블록: tab5 시작 ~ tab4 시작
#    footer: tab5 블록 안에 있는 것들
# ─────────────────────────────────────────────────────────

# tab3, tab4, tab5 시작 줄 (0-indexed)
t3_start = tab_lines.get('tab3')
t4_start = tab_lines.get('tab4')
t5_start = tab_lines.get('tab5')

print(f"\nt3_start: {t3_start+1}, t4_start: {t4_start+1}, t5_start: {t5_start+1}")

# 현재 순서: tab3 → tab5 → tab4 (잘못됨)
# 목표 순서: tab3 → tab4 → tab5

# tab3 끝 찾기: tab5 시작 전, stray markdown("---") 줄 찾기
stray_idx = None
for i in range(t3_start, t5_start):
    if lines[i].strip() == 'st.markdown("---")':
        stray_idx = i
        print(f"stray markdown: line {i+1}")
        break

# 블록 분리
# before_tab5: tab3까지 (stray markdown 제거)
if stray_idx is not None:
    # stray markdown 줄과 앞뒤 빈줄 제거
    before_t5 = lines[:stray_idx]
    # 끝의 빈줄 정리
    while before_t5 and before_t5[-1].strip() == '':
        before_t5.pop()
    before_t5.append('')  # 빈줄 1개만
else:
    before_t5 = lines[:t5_start]

# tab5 블록: t5_start ~ t4_start
tab5_block = lines[t5_start:t4_start]

# tab4 블록: t4_start ~ 끝
tab4_block = lines[t4_start:]

# ─────────────────────────────────────────────────────────
# 4. footer 정리: tab5 블록에서 footer 1개만 남기기
#    (tab5 블록 끝에 footer가 여러 개 있음)
# ─────────────────────────────────────────────────────────
# tab5 블록에서 footer 줄 찾기
footer_in_t5 = [i for i, l in enumerate(tab5_block) if 'LumineX v4.4' in l]
print(f"tab5 블록 내 footer: {len(footer_in_t5)}개 at {[i+1 for i in footer_in_t5]}")

# 첫 번째 footer 이후 모든 footer 줄 + 앞 빈줄 제거
if len(footer_in_t5) > 1:
    keep_until = footer_in_t5[0]  # 첫 번째 footer까지만 유지
    tab5_trimmed = tab5_block[:keep_until+1]
    # 끝 빈줄 정리
    while tab5_trimmed and tab5_trimmed[-1].strip() == '':
        tab5_trimmed.pop()
    tab5_block = tab5_trimmed
    print(f"✅ tab5 블록 footer 정리: {keep_until+1}줄까지 유지")

# tab4 블록에서도 footer 있으면 제거
footer_in_t4 = [i for i, l in enumerate(tab4_block) if 'LumineX v4.4' in l]
if footer_in_t4:
    print(f"tab4 블록 내 footer: {len(footer_in_t4)}개 — 제거")
    tab4_block = [l for l in tab4_block if 'LumineX v4.4' not in l]

# ─────────────────────────────────────────────────────────
# 5. 재조합: before_t5 + tab4_block + tab5_block + footer
# ─────────────────────────────────────────────────────────
FOOTER_LINE = "st.markdown('<div style=\"text-align:center;color:#444;font-size:0.75rem;\">✦ LumineX v4.4 — AI Fashion Image Engine</div>', unsafe_allow_html=True)"

new_lines = (
    before_t5
    + ['']
    + tab4_block
    + ['']
    + tab5_block
    + ['', FOOTER_LINE, '']
)

new_text = '\n'.join(new_lines) + '\n'
DASHBOARD.write_text(new_text, encoding='utf-8')
print(f"\n✅ 저장 완료: {len(new_lines)}줄")

# ─────────────────────────────────────────────────────────
# 검증
# ─────────────────────────────────────────────────────────
verify = DASHBOARD.read_text(encoding='utf-8')
v_lines = verify.splitlines()

footer_count = verify.count('LumineX v4.4')
print(f"\n검증:")
print(f"  footer: {footer_count}개 {'✅' if footer_count == 1 else '❌'}")
print(f"  tab5 있음: {'✅' if 'with tab5:' in verify else '❌'}")
print(f"  tab4 있음: {'✅' if 'with tab4:' in verify else '❌'}")
print(f"  히스토리 있음: {'✅' if '히스토리' in verify else '❌'}")

# tab 순서
tab_pos = {}
for i, l in enumerate(v_lines):
    m = re.match(r'^with (tab\d):', l.strip())
    if m and m.group(1) not in tab_pos:
        tab_pos[m.group(1)] = i+1
for k, v in sorted(tab_pos.items()):
    print(f"  line {v:4d}: with {k}:")

if 'tab4' in tab_pos and 'tab5' in tab_pos:
    ok = tab_pos['tab4'] < tab_pos['tab5']
    print(f"  tab4 < tab5: {'✅' if ok else '❌'}")

print("\n🎉 완료! git add dashboard.py; git commit; git push")
