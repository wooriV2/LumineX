"""
dashboard_hof_random_fix.py
HOF 랜덤 버튼 수정:
- load_preset() 제거 (JSON 없음)
- preset_selected 세팅 + _trigger_quick_generate 플래그로 탭1 빠른 생성 자동 실행
"""
from pathlib import Path

TARGET = Path("C:/Dev/LumineX/dashboard.py")
content = TARGET.read_text(encoding="utf-8")

# ── 1. 기존 HOF 랜덤 버튼 블록 교체 ──
OLD = '''    if st.button("🎲 HOF 랜덤 1개", use_container_width=True, key="sb_hof_random"):
        import random as _random
        _hof_pick = _random.choice(list(HOF_TIER))
        try:
            _hof_preset = load_preset(_hof_pick)
            from core.builders import build_gemini_prompt as _bgp
            _hof_prompt = _bgp(
                {
                    "env":      list(ENVIRONMENTS.keys())[0],
                    "light":    list(LIGHTING.keys())[0],
                    "style":    list(STYLES.keys())[0],
                    "model":    list(MODEL_TYPES.keys())[0],
                    "outfit":   list(OUTFIT_TYPES.keys())[0],
                    "material": list(MATERIALS.keys())[0],
                    "camera":   list(CAMERAS.keys())[0],
                    **_hof_preset,
                },
                list(ASPECT_RATIOS.keys())[0],
                True,
            )
        except Exception:
            _hof_prompt = f"프리셋 모드 탭에서 [{_hof_pick}]을 선택해 생성하세요."
        st.session_state.preset_selected = _hof_pick
        st.session_state.preset_prompt   = _hof_prompt
        _add_history(_hof_pick, _hof_prompt, global_platform)
        st.success(f"👑 {_hof_pick}")
        st.rerun()'''

NEW = '''    if st.button("🎲 HOF 랜덤 1개", use_container_width=True, key="sb_hof_random"):
        import random as _random
        _hof_pick = _random.choice(list(HOF_TIER))
        # preset_selected 세팅 → 탭1 드롭다운이 이 프리셋으로 맞춰짐
        st.session_state.preset_selected  = _hof_pick
        st.session_state.preset_prompt    = ""
        # 빠른 생성 자동 트리거 플래그
        st.session_state._hof_quick_fire  = True
        st.rerun()'''

if OLD in content:
    content = content.replace(OLD, NEW, 1)
    print("✅ [1/3] HOF 랜덤 버튼 교체 완료")
else:
    print("❌ [1/3] 기존 블록을 찾지 못했습니다")

# ── 2. 탭1 상단 — _hof_quick_fire 플래그 처리 삽입 ──
# 기존: "if not selected_preset:" 바로 앞에 삽입
QUICK_FIRE_HANDLER = '''    # ── HOF 랜덤 빠른 생성 자동 트리거 ──
    if st.session_state.pop("_hof_quick_fire", False):
        st.session_state._trigger_quick = True

'''

ANCHOR = "    if not selected_preset:\n        st.stop()"
if ANCHOR in content and "_hof_quick_fire" not in content:
    content = content.replace(ANCHOR, QUICK_FIRE_HANDLER + ANCHOR, 1)
    print("✅ [2/3] HOF 빠른 생성 트리거 핸들러 삽입 완료")
elif "_hof_quick_fire" in content:
    print("⏭️  [2/3] 트리거 핸들러 이미 존재 — 건너뜀")
else:
    # fallback: btn_quick 버튼 정의 바로 앞
    ANCHOR2 = "    col_a, col_b, _ = st.columns([1, 1, 2])\n"
    if ANCHOR2 in content and "_hof_quick_fire" not in content:
        content = content.replace(ANCHOR2, QUICK_FIRE_HANDLER + ANCHOR2, 1)
        print("✅ [2/3] HOF 빠른 생성 트리거 핸들러 삽입 완료 (fallback)")
    else:
        print("❌ [2/3] 삽입 앵커를 찾지 못했습니다")

# ── 3. btn_quick 처리 블록에 _trigger_quick 플래그 연동 ──
# 기존: "if btn_quick and selected_preset:"
# 변경: "if (btn_quick or st.session_state.pop('_trigger_quick', False)) and selected_preset:"
OLD_QUICK = "    if btn_quick and selected_preset:"
NEW_QUICK = "    if (btn_quick or st.session_state.pop('_trigger_quick', False)) and selected_preset:"

if OLD_QUICK in content:
    content = content.replace(OLD_QUICK, NEW_QUICK, 1)
    print("✅ [3/3] btn_quick 트리거 연동 완료")
elif NEW_QUICK in content:
    print("⏭️  [3/3] 이미 연동됨 — 건너뜀")
else:
    print("❌ [3/3] btn_quick 블록을 찾지 못했습니다")

TARGET.write_text(content, encoding="utf-8")
print("\n🎉 수정 완료! streamlit run dashboard.py 로 확인하세요.")
print("   사이드바 [🎲 HOF 랜덤 1개] → 탭1 자동 빠른 생성 실행")
