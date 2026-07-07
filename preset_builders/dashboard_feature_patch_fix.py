"""
dashboard_feature_patch_fix.py
사이드바 HOF 버튼 들여쓰기 오류 수정
"""
from pathlib import Path

TARGET = Path("C:/Dev/LumineX/dashboard.py")
content = TARGET.read_text(encoding="utf-8")

# ── 잘못 삽입된 블록 제거 후 올바른 위치에 재삽입 ──

OLD_BLOCK = '''    st.markdown("---")
    st.markdown("### 👑 HOF 빠른 실행")

    if st.button("🎲 HOF 랜덤 1개", use_container_width=True, key="sb_hof_random"):
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
        st.rerun()

    if st.button("📦 HOF 전체 배치 생성", use_container_width=True, key="sb_hof_batch"):
        st.session_state.hof_batch_result = "__GENERATE__"
        st.rerun()
'''

# 올바른 들여쓰기 (with st.sidebar: 블록 안 → 4칸)
NEW_BLOCK = '''    st.markdown("---")
    st.markdown("### 👑 HOF 빠른 실행")

    if st.button("🎲 HOF 랜덤 1개", use_container_width=True, key="sb_hof_random"):
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
        st.rerun()

    if st.button("📦 HOF 전체 배치 생성", use_container_width=True, key="sb_hof_batch"):
        st.session_state.hof_batch_result = "__GENERATE__"
        st.rerun()
'''

# 기존 잘못된 블록을 찾아서 제거
if OLD_BLOCK in content:
    # 잘못 삽입된 블록 제거
    content = content.replace(OLD_BLOCK, "", 1)
    print("✅ [1/3] 잘못된 HOF 블록 제거 완료")
else:
    print("⚠️  [1/3] 기존 블록 패턴 불일치 — 수동 확인 필요")

# ── 사이드바 끝 (st.markdown("---") 마지막) 바로 뒤에 재삽입 ──
# 사이드바 with 블록은 "# ─── 헤더" 앞에서 끝남
# 안전한 앵커: 사이드바 마지막 st.caption
SIDEBAR_END_ANCHOR = '    st.caption("💡 같은 창 반복 생성 시 타투/헤어 오염 주의")'

if SIDEBAR_END_ANCHOR in content:
    pos = content.find(SIDEBAR_END_ANCHOR)
    eol = content.find("\n", pos) + 1
    content = content[:eol] + NEW_BLOCK + content[eol:]
    print("✅ [2/3] HOF 블록 올바른 위치에 재삽입 완료")
else:
    # fallback: 사이드바 내 마지막 st.markdown("---") 찾기
    FALLBACK = '    st.markdown(f"**카테고리:** `{len(PRESET_CATEGORIES)}개`")\n'
    if FALLBACK in content:
        pos = content.find(FALLBACK)
        eol = content.find("\n", pos) + 1
        content = content[:eol] + NEW_BLOCK + content[eol:]
        print("✅ [2/3] HOF 블록 fallback 위치에 재삽입 완료")
    else:
        print("❌ [2/3] 삽입 앵커를 찾지 못했습니다 — 수동 삽입 필요")

TARGET.write_text(content, encoding="utf-8")
print("✅ [3/3] dashboard.py 저장 완료")
print("\n🎉 수정 완료! streamlit run dashboard.py 로 확인하세요.")
