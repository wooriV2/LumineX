"""
dashboard_hof_trigger_fix.py
_hof_quick_fire → _trigger_quick 변환 핸들러 삽입
"""
from pathlib import Path

TARGET = Path("C:/Dev/LumineX/dashboard.py")
content = TARGET.read_text(encoding="utf-8")

# _hof_quick_fire 세팅 확인
if "_hof_quick_fire" not in content:
    print("❌ _hof_quick_fire 플래그가 없습니다 — 패치 불필요")
    exit()

# 핸들러가 이미 있는지 확인
if "pop(\"_hof_quick_fire\"" in content or "pop('_hof_quick_fire'" in content:
    print("⏭️  핸들러 이미 존재 — 건너뜀")
    exit()

# btn_quick 버튼 정의 바로 앞에 핸들러 삽입
HANDLER = '''    # ── HOF 랜덤 빠른 생성 자동 트리거 ──
    if st.session_state.pop("_hof_quick_fire", False):
        st.session_state["_trigger_quick"] = True

'''

ANCHOR = '    if (btn_quick or st.session_state.pop(\'_trigger_quick\', False)) and selected_preset:'

if ANCHOR in content:
    content = content.replace(ANCHOR, HANDLER + ANCHOR, 1)
    print("✅ [1/1] _hof_quick_fire 핸들러 삽입 완료")
else:
    print("❌ [1/1] btn_quick 앵커를 찾지 못했습니다")

TARGET.write_text(content, encoding="utf-8")
print("\n🎉 수정 완료! HOF 랜덤 클릭 → 탭1에서 자동 빠른 생성 실행됩니다.")
