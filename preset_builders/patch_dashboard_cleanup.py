# -*- coding: utf-8 -*-
"""
dashboard.py 정리 패치
1. footer 4중 중복 제거 (1개만 남기기)
2. tab3 뒤 stray st.markdown("---") 제거
3. tab4/tab5 순서 교체 (tab4 먼저, tab5 나중)

실행: python preset_builders\patch_dashboard_cleanup.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path
import re

DASHBOARD = Path("dashboard.py")
assert DASHBOARD.exists(), "dashboard.py 없음"

text = DASHBOARD.read_text(encoding="utf-8")
original = text

# ─────────────────────────────────────────────────────────
# 1. footer 중복 제거 — 1개만 남기기
# ─────────────────────────────────────────────────────────
FOOTER = "st.markdown('<div style=\"text-align:center;color:#444;font-size:0.75rem;\">✦ LumineX v4.4 — AI Fashion Image Engine</div>', unsafe_allow_html=True)"

count = text.count(FOOTER)
print(f"footer 발견: {count}개")

if count > 1:
    # 첫 번째만 남기고 나머지 제거
    first_pos = text.index(FOOTER)
    # 첫 번째 이후 모든 footer 제거
    after_first = text[first_pos + len(FOOTER):]
    after_first_cleaned = after_first.replace("\n\n" + FOOTER, "").replace("\n" + FOOTER, "")
    text = text[:first_pos + len(FOOTER)] + after_first_cleaned
    remaining = text.count(FOOTER)
    print(f"✅ footer 정리 완료: {count}개 → {remaining}개")
else:
    print("✅ footer 이미 1개")

# ─────────────────────────────────────────────────────────
# 2. stray st.markdown("---") 제거 — tab3 닫힌 후 떠있는 것
# ─────────────────────────────────────────────────────────
STRAY = '\nst.markdown("---")\n\n# ══════════════════════════════════════════════════════════\n# 탭 5: 히스토리'
CLEAN = '\n\n# ══════════════════════════════════════════════════════════\n# 탭 5: 히스토리'

if STRAY in text:
    text = text.replace(STRAY, CLEAN, 1)
    print("✅ stray st.markdown('---') 제거 완료")
else:
    print("✅ stray markdown 없음 (이미 정리됨)")

# ─────────────────────────────────────────────────────────
# 3. tab4/tab5 순서 교체
# ─────────────────────────────────────────────────────────
TAB5_HEADER  = "# ══════════════════════════════════════════════════════════\n# 탭 5: 히스토리 & HOF 배치 생성\n# ══════════════════════════════════════════════════════════\nwith tab5:"
TAB4_HEADER  = "# ══════════════════════════════════════════════════════════\n# 탭 4: 영상 프롬프트\n# ══════════════════════════════════════════════════════════\nwith tab4:"
FOOTER_MARKER = "\nst.markdown('<div style=\"text-align:center"

if TAB5_HEADER in text and TAB4_HEADER in text:
    tab5_start   = text.index(TAB5_HEADER)
    tab4_start   = text.index(TAB4_HEADER)

    if tab5_start < tab4_start:
        # tab5가 tab4보다 앞에 있는 잘못된 순서 → 교체
        footer_start = text.index(FOOTER_MARKER)
        tab5_block   = text[tab5_start:tab4_start]
        tab4_block   = text[tab4_start:footer_start]
        footer_block = text[footer_start:]
        before_tabs  = text[:tab5_start]
        text = before_tabs + tab4_block + tab5_block + footer_block
        print("✅ tab4/tab5 순서 교체 완료")
    else:
        print("✅ tab4/tab5 순서 이미 정상")
else:
    print("⚠️  tab4 또는 tab5 헤더를 찾을 수 없음")

# ─────────────────────────────────────────────────────────
# 저장
# ─────────────────────────────────────────────────────────
if text != original:
    DASHBOARD.write_text(text, encoding="utf-8")
    print("✅ dashboard.py 저장 완료")
else:
    print("⚠️  변경사항 없음")

# ─────────────────────────────────────────────────────────
# 검증
# ─────────────────────────────────────────────────────────
verify = DASHBOARD.read_text(encoding="utf-8")

footer_count = verify.count("✦ LumineX v4.4 — AI Fashion Image Engine")
print(f"\n검증 결과:")
print(f"  footer 개수: {footer_count} {'✅' if footer_count == 1 else '❌'}")

stray_ok = 'st.markdown("---")\n\n# ══' not in verify
print(f"  stray markdown 없음: {'✅' if stray_ok else '❌'}")

# tab 순서 확인
tab_positions = [(m.group(), verify[:m.start()].count('\n')+1) for m in re.finditer(r'with tab[0-9]+:', verify)]
for tab, line in tab_positions:
    print(f"  line {line:4d}: {tab}")

tab4_lines = [ln for tab, ln in tab_positions if tab == 'with tab4:']
tab5_lines = [ln for tab, ln in tab_positions if tab == 'with tab5:']
if tab4_lines and tab5_lines:
    order_ok = tab4_lines[-1] < tab5_lines[-1]
    print(f"  tab4({tab4_lines[-1]}) < tab5({tab5_lines[-1]}): {'✅' if order_ok else '❌'}")

print("\n🎉 완료! git add dashboard.py; git commit; git push")
