# -*- coding: utf-8 -*-
"""
dashboard.py 패치 — tab4/tab5 순서 재수정

실행: python preset_builders\patch_tab_order.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path

DASHBOARD = Path("dashboard.py")
assert DASHBOARD.exists(), "dashboard.py 없음"

text = DASHBOARD.read_text(encoding="utf-8")

TAB5_HEADER = "# ══════════════════════════════════════════════════════════\n# 탭 5: 히스토리 & HOF 배치 생성\n# ══════════════════════════════════════════════════════════\nwith tab5:"
TAB4_HEADER = "# ══════════════════════════════════════════════════════════\n# 탭 4: 영상 프롬프트\n# ══════════════════════════════════════════════════════════\nwith tab4:"
FOOTER_MARKER = "\nst.markdown('<div style=\"text-align:center"

assert TAB5_HEADER in text, "tab5 헤더 없음"
assert TAB4_HEADER in text, "tab4 헤더 없음"
assert FOOTER_MARKER in text, "footer 없음"

tab5_start   = text.index(TAB5_HEADER)
tab4_start   = text.index(TAB4_HEADER)
footer_start = text.index(FOOTER_MARKER)

tab5_block   = text[tab5_start:tab4_start]
tab4_block   = text[tab4_start:footer_start]
footer_block = text[footer_start:]
before_tabs  = text[:tab5_start]

text = before_tabs + tab4_block + tab5_block + footer_block

DASHBOARD.write_text(text, encoding="utf-8")
print("✅ tab4/tab5 순서 교체 완료")

# 검증
verify = DASHBOARD.read_text(encoding="utf-8")
import re
tabs = [(m.group(), verify[:m.start()].count('\n')+1) for m in re.finditer(r'with tab[0-9]+:', verify)]
for tab, line in tabs:
    print(f"  line {line}: {tab}")

tab4_pos = verify.index("with tab4:")
tab5_pos = verify.index("with tab5:")
assert tab4_pos < tab5_pos, "❌ 순서 여전히 잘못됨"
print("✅ 순서 정상 확인")
print("\n🎉 완료! git add dashboard.py; git commit; git push")
