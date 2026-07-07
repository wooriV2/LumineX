# -*- coding: utf-8 -*-
"""
dashboard.py 긴급 핫픽스 — _pidx is not defined 오류
_pval/_pidx 함수를 with tab1: 블록 밖(전역)으로 이동

실행: python preset_builders\patch_pidx_hotfix.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path

DASHBOARD = Path("dashboard.py")
assert DASHBOARD.exists(), "dashboard.py 없음"

text = DASHBOARD.read_text(encoding="utf-8")

# ─────────────────────────────────────────────────────────
# 1. with tab1: 블록 안의 _pval/_pidx 정의 제거
# ─────────────────────────────────────────────────────────

OLD_INNER = """    # 매 렌더링마다 JSON 읽어서 default 계산
    def _pval(d, raw):
        \"\"\"dict에서 raw 값과 매칭되는 key 반환, 없으면 NONE\"\"\"
        if not raw:
            return NONE
        raw_lower = str(raw).lower()
        for k, v in d.items():
            v_str = (v.get("gemini", "") if isinstance(v, dict) else str(v)).lower()
            if raw_lower in v_str or v_str in raw_lower:
                return k
        return NONE

    def _pidx(opts, val):
        \"\"\"options 리스트에서 val의 index 반환, 없으면 0\"\"\"
        return opts.index(val) if val in opts else 0

    try:
        _pd = load_preset(selected_preset)
    except Exception:
        _pd = {}"""

NEW_INNER = """    # 매 렌더링마다 JSON 읽어서 default 계산
    try:
        _pd = load_preset(selected_preset)
    except Exception:
        _pd = {}"""

assert OLD_INNER in text, "tab1 내부 함수 블록을 찾을 수 없어요."
text = text.replace(OLD_INNER, NEW_INNER, 1)
print("✅ tab1 내부 _pval/_pidx 정의 제거")

# ─────────────────────────────────────────────────────────
# 2. with tab1: 선언 바로 위에 전역 함수로 추가
# ─────────────────────────────────────────────────────────

TAB1_MARKER = "\nwith tab1:"

GLOBAL_FUNCS = """
def _pval(d, raw, none_label):
    \"\"\"dict에서 raw 값과 매칭되는 key 반환, 없으면 none_label\"\"\"
    if not raw:
        return none_label
    raw_lower = str(raw).lower()
    for k, v in d.items():
        v_str = (v.get("gemini", "") if isinstance(v, dict) else str(v)).lower()
        if raw_lower in v_str or v_str in raw_lower:
            return k
    return none_label

def _pidx(opts, val):
    \"\"\"options 리스트에서 val의 index 반환, 없으면 0\"\"\"
    return opts.index(val) if val in opts else 0

"""

assert TAB1_MARKER in text, "with tab1: 마커를 찾을 수 없어요."
insert_pos = text.index(TAB1_MARKER)
text = text[:insert_pos] + GLOBAL_FUNCS + text[insert_pos:]
print("✅ _pval/_pidx 전역 함수로 이동")

# ─────────────────────────────────────────────────────────
# 3. _pval 호출부에서 NONE → none_label 인자 추가
#    _pval(d, raw) → _pval(d, raw, NONE)
# ─────────────────────────────────────────────────────────

import re
# _pval(DICT, _pd.get("key", "")) 패턴을 _pval(DICT, _pd.get("key", ""), NONE) 로 변경
old_pattern = r'_pval\(([^,]+),\s*(_pd\.get\([^)]+\))\)'
new_pattern = r'_pval(\1, \2, NONE)'
text, count = re.subn(old_pattern, new_pattern, text)
print(f"✅ _pval 호출부 none_label 인자 추가 ({count}개)")

DASHBOARD.write_text(text, encoding="utf-8")
print("✅ dashboard.py 저장 완료")

# 검증
verify = DASHBOARD.read_text(encoding="utf-8")
assert "def _pval" in verify,   "❌ _pval 함수 없음"
assert "def _pidx" in verify,   "❌ _pidx 함수 없음"
assert "with tab1:" in verify,  "❌ tab1 없음"
# 전역 위치 확인 (tab1보다 앞에 있어야 함)
pval_pos  = verify.index("def _pval")
tab1_pos  = verify.index("with tab1:")
assert pval_pos < tab1_pos, "❌ _pval이 tab1보다 뒤에 있음"
print(f"✅ 검증: _pval 전역 위치 확인 ({pval_pos} < {tab1_pos})")
print("\n🎉 완료! git add dashboard.py; git commit; git push 후 Cloud reboot")
