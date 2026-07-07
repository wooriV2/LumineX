"""
LumineX Dashboard Feature Patch
================================
1순위: 프롬프트 히스토리 (세션 내 최근 20개)
2순위: 랜덤 HOF 원클릭 (사이드바)
3순위: HOF 배치 생성 (전체 프롬프트 txt 출력)

적용 방법:
  dashboard.py 에서 아래 3곳에 코드를 삽입하세요.
  각 섹션에 ### PATCH START / ### PATCH END 주석으로 범위 표시.

────────────────────────────────────────────────
[삽입 위치 A] st.set_page_config(...) 직후
  → 히스토리 세션 초기화

[삽입 위치 B] with st.sidebar: 블록 끝부분 (st.markdown("---") 마지막 줄 다음)
  → HOF 랜덤 버튼 + 배치 생성 버튼

[삽입 위치 C] 탭1(프리셋 모드) st.code(...) 출력 직후
  → 히스토리에 자동 저장

[삽입 위치 D] 탭3(랜덤 모드) st.code(...) 출력 직후
  → 히스토리에 자동 저장 (동일 패턴)
────────────────────────────────────────────────
"""

# ══════════════════════════════════════════════════════════
# [A] 세션 초기화 — st.set_page_config 직후에 삽입
# ══════════════════════════════════════════════════════════

PATCH_A = """
### PATCH START — 히스토리 세션 초기화
if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []   # [{"preset": str, "prompt": str, "platform": str}]
if "hof_batch_result" not in st.session_state:
    st.session_state.hof_batch_result = ""
### PATCH END
"""

# ══════════════════════════════════════════════════════════
# [B] 사이드바 추가 기능 — with st.sidebar: 블록 끝에 삽입
# ══════════════════════════════════════════════════════════

PATCH_B = """
### PATCH START — 사이드바 HOF 기능
    st.markdown("---")
    st.markdown("### 👑 HOF 빠른 실행")

    # ── HOF 랜덤 원클릭 ──
    if st.button("🎲 HOF 랜덤 1개", use_container_width=True, key="sb_hof_random"):
        import random as _random
        _hof_pick = _random.choice(list(HOF_TIER))
        try:
            _hof_preset = load_preset(_hof_pick)
            _overrides = {}
            from core.builders import build_gemini_prompt
            _hof_prompt = build_gemini_prompt(
                {**_hof_preset,
                 "env": list(ENVIRONMENTS.keys())[0],
                 "light": list(LIGHTING.keys())[0],
                 "style": list(STYLES.keys())[0],
                 "model": list(MODEL_TYPES.keys())[0],
                 "outfit": list(OUTFIT_TYPES.keys())[0],
                 "material": list(MATERIALS.keys())[0],
                 "camera": list(CAMERAS.keys())[0],
                 **_hof_preset},
                list(ASPECT_RATIOS.keys())[0],
                True,
            )
        except Exception:
            _hof_prompt = f"[{_hof_pick}] 프리셋을 프리셋 모드 탭에서 선택해 생성하세요."
        st.session_state.preset_selected = _hof_pick
        st.session_state.preset_prompt   = _hof_prompt
        _add_history(_hof_pick, _hof_prompt, global_platform)
        st.success(f"👑 {_hof_pick}")
        st.rerun()

    # ── HOF 배치 생성 ──
    if st.button("📦 HOF 전체 배치 생성", use_container_width=True, key="sb_hof_batch"):
        st.session_state.hof_batch_result = "__GENERATE__"
        st.rerun()
### PATCH END
"""

# ══════════════════════════════════════════════════════════
# [C] 히스토리 헬퍼 함수 — st.set_page_config 직후 (PATCH_A 아래)에 삽입
# ══════════════════════════════════════════════════════════

PATCH_C = """
### PATCH START — 히스토리 헬퍼
def _add_history(preset_name: str, prompt: str, platform: str):
    \"\"\"히스토리에 추가 (최대 20개, 중복 맨 앞으로 이동)\"\"\"
    hist = st.session_state.prompt_history
    # 동일 프리셋 기존 항목 제거
    hist = [h for h in hist if h["preset"] != preset_name]
    hist.insert(0, {"preset": preset_name, "prompt": prompt, "platform": platform})
    st.session_state.prompt_history = hist[:20]
### PATCH END
"""

# ══════════════════════════════════════════════════════════
# [D] 탭1 — 프리셋 프롬프트 생성 후 히스토리 저장
#     기존: st.code(st.session_state.preset_prompt, ...) 바로 다음에 삽입
# ══════════════════════════════════════════════════════════

PATCH_D = """
### PATCH START — 탭1 히스토리 저장
        _add_history(selected_preset, st.session_state.preset_prompt, global_platform)
### PATCH END
"""

# ══════════════════════════════════════════════════════════
# [E] 탭3 — 랜덤 프롬프트 생성 후 히스토리 저장
#     기존: st.code(st.session_state.random_prompt, ...) 바로 다음에 삽입
# ══════════════════════════════════════════════════════════

PATCH_E = """
### PATCH START — 탭3 히스토리 저장
        _add_history("랜덤", st.session_state.random_prompt, global_platform)
### PATCH END
"""

# ══════════════════════════════════════════════════════════
# [F] 히스토리 탭 + 배치 생성 처리 — tab4 정의 부분을 아래로 교체
#
#     기존: tab1, tab2, tab3, tab4 = st.tabs([...])
#     변경: tab1, tab2, tab3, tab4, tab5 = st.tabs([..., "📋 히스토리"])
#     그리고 tab4(영상) 아래에 tab5 블록 추가
# ══════════════════════════════════════════════════════════

PATCH_F_TABS_LINE = """
### PATCH — 탭 선언 교체 (기존 4개 → 5개)
# 기존:
# tab1, tab2, tab3, tab4 = st.tabs(["🎨 프리셋 모드", "🛠️ 수동 조합", "🎲 랜덤 모드", "🎬 영상 프롬프트"])
# 변경:
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎨 프리셋 모드", "🛠️ 수동 조합", "🎲 랜덤 모드", "🎬 영상 프롬프트", "📋 히스토리"
])
"""

PATCH_F_TAB5 = """
### PATCH START — 탭5: 히스토리 + 배치 생성
with tab5:
    st.markdown("### 📋 프롬프트 히스토리")
    st.caption("세션 내 최근 20개 프롬프트. 새로고침하면 초기화됩니다.")

    # ── HOF 배치 생성 처리 ──
    if st.session_state.get("hof_batch_result") == "__GENERATE__":
        st.session_state.hof_batch_result = ""
        _batch_lines = []
        _failed = []
        _progress = st.progress(0, text="HOF 배치 생성 중...")
        _hof_list = sorted(list(HOF_TIER))
        for _i, _name in enumerate(_hof_list):
            try:
                _p = load_preset(_name)
                _prompt = build_gemini_prompt(
                    {
                        "env":      list(ENVIRONMENTS.keys())[0],
                        "light":    list(LIGHTING.keys())[0],
                        "style":    list(STYLES.keys())[0],
                        "model":    list(MODEL_TYPES.keys())[0],
                        "outfit":   list(OUTFIT_TYPES.keys())[0],
                        "material": list(MATERIALS.keys())[0],
                        "camera":   list(CAMERAS.keys())[0],
                        **_p,
                    },
                    list(ASPECT_RATIOS.keys())[0],
                    True,
                )
                _batch_lines.append(f"### [{_i+1}/{len(_hof_list)}] 👑 {_name}\\n{_prompt}\\n")
                _add_history(_name, _prompt, global_platform)
            except Exception as _e:
                _failed.append(_name)
            _progress.progress((_i + 1) / len(_hof_list), text=f"처리 중... {_name}")
        _progress.empty()
        st.session_state.hof_batch_result = "\\n".join(_batch_lines)
        if _failed:
            st.warning(f"⚠️ JSON 없는 프리셋 {len(_failed)}개 건너뜀: {', '.join(_failed)}")
        st.success(f"✅ HOF {len(_hof_list) - len(_failed)}개 배치 생성 완료!")

    if st.session_state.hof_batch_result and st.session_state.hof_batch_result != "__GENERATE__":
        st.markdown("#### 📦 HOF 배치 결과")
        st.text_area("배치 전체 프롬프트", value=st.session_state.hof_batch_result, height=300)
        st.code(st.session_state.hof_batch_result, language=None)
        st.caption("👆 전체 복사 후 메모장에 저장하세요.")
        if st.button("🗑️ 배치 결과 초기화"):
            st.session_state.hof_batch_result = ""
            st.rerun()
        st.markdown("---")

    # ── 히스토리 목록 ──
    hist = st.session_state.prompt_history
    if not hist:
        st.info("아직 생성된 프롬프트가 없어요. 프리셋 모드나 랜덤 모드에서 생성해보세요.")
    else:
        st.markdown(f"**총 {len(hist)}개** (최신순)")
        for _idx, _item in enumerate(hist):
            _label = f"{'👑' if _item['preset'] in HOF_TIER else '🌟' if _item['preset'] in SSS_TIER else '⭐' if _item['preset'] in SS_TIER else '•'} {_item['preset']}"
            with st.expander(f"{_idx+1}. {_label}  `{_item['platform']}`", expanded=(_idx == 0)):
                st.text_area(
                    "프롬프트",
                    value=_item["prompt"],
                    height=120,
                    key=f"hist_ta_{_idx}",
                )
                st.code(_item["prompt"], language=None)
        if st.button("🗑️ 히스토리 전체 삭제"):
            st.session_state.prompt_history = []
            st.rerun()
### PATCH END
"""

# ══════════════════════════════════════════════════════════
# 자동 패치 스크립트
# 실행: python dashboard_feature_patch.py
# ══════════════════════════════════════════════════════════

if __name__ == "__main__":
    import re
    from pathlib import Path

    TARGET = Path("C:/Dev/LumineX/dashboard.py")
    content = TARGET.read_text(encoding="utf-8")
    original = content

    errors = []

    # ── 1. 탭 선언 교체 (4→5) ──
    old_tabs = 'tab1, tab2, tab3, tab4 = st.tabs(["🎨 프리셋 모드", "🛠️ 수동 조합", "🎲 랜덤 모드", "🎬 영상 프롬프트"])'
    new_tabs = 'tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎨 프리셋 모드", "🛠️ 수동 조합", "🎲 랜덤 모드", "🎬 영상 프롬프트", "📋 히스토리"])'
    if old_tabs in content:
        content = content.replace(old_tabs, new_tabs, 1)
        print("✅ [1/7] 탭 선언 교체 완료")
    else:
        errors.append("❌ [1/7] 탭 선언을 찾지 못했습니다.")

    # ── 2. 세션 초기화 + 헬퍼 함수 — set_page_config 직후 삽입 ──
    INIT_BLOCK = '''
# ── 히스토리/배치 세션 초기화 ──
if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []
if "hof_batch_result" not in st.session_state:
    st.session_state.hof_batch_result = ""

def _add_history(preset_name: str, prompt: str, platform: str):
    """히스토리에 추가 (최대 20개)"""
    hist = st.session_state.prompt_history
    hist = [h for h in hist if h["preset"] != preset_name]
    hist.insert(0, {"preset": preset_name, "prompt": prompt, "platform": platform})
    st.session_state.prompt_history = hist[:20]
'''
    anchor = "st.set_page_config("
    # set_page_config 블록 끝 찾기 (닫는 괄호 다음 줄)
    cfg_start = content.find(anchor)
    if cfg_start != -1:
        paren_depth = 0
        i = cfg_start
        while i < len(content):
            if content[i] == "(":
                paren_depth += 1
            elif content[i] == ")":
                paren_depth -= 1
                if paren_depth == 0:
                    break
            i += 1
        insert_pos = content.find("\n", i) + 1
        if "prompt_history" not in content:
            content = content[:insert_pos] + INIT_BLOCK + content[insert_pos:]
            print("✅ [2/7] 세션 초기화 + 헬퍼 함수 삽입 완료")
        else:
            print("⏭️  [2/7] 세션 초기화 이미 존재 — 건너뜀")
    else:
        errors.append("❌ [2/7] set_page_config를 찾지 못했습니다.")

    # ── 3. 사이드바 끝에 HOF 버튼 삽입 ──
    HOF_SIDEBAR = '''
    st.markdown("---")
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
    # 사이드바 블록 끝 탐지: "# ─── 헤더" 또는 tab1 선언 직전
    sidebar_anchor = "# ─── 헤더 ─"
    header_pos = content.find(sidebar_anchor)
    if header_pos == -1:
        sidebar_anchor = "\ntab1, tab2"
        header_pos = content.find(sidebar_anchor)

    if header_pos != -1 and "sb_hof_random" not in content:
        # with st.sidebar: 블록 마지막 줄 (헤더 섹션 바로 앞) 삽입
        # 사이드바 with 블록 끝을 찾기 위해 역방향으로 탐색
        # 가장 안전한 방법: "### 💡 플랫폼 팁" if/elif/else 블록 끝에 추가
        platform_tip_end = content.find('    st.warning("태그 나열 + --파라미터 방식.")')
        if platform_tip_end != -1:
            eol = content.find("\n", platform_tip_end) + 1
            # if global_platform == "Gemini": 블록 찾기
            gemini_block = '    if global_platform == "Gemini":\n'
            gemini_pos   = content.find(gemini_block, platform_tip_end)
            if gemini_pos != -1:
                # Gemini 블록 전체 끝 탐색
                rerun_line = '            st.rerun()\n'
                rr_pos = content.find(rerun_line, gemini_pos)
                if rr_pos != -1:
                    insert_pos = content.find("\n", rr_pos) + 1
                    content = content[:insert_pos] + HOF_SIDEBAR + content[insert_pos:]
                    print("✅ [3/7] 사이드바 HOF 버튼 삽입 완료")
                else:
                    # fallback: st.markdown("---") 마지막 패턴
                    last_sidebar_sep = content.rfind('    st.markdown("---")\n', 0, header_pos)
                    if last_sidebar_sep != -1:
                        insert_pos = content.find("\n", last_sidebar_sep) + 1
                        content = content[:insert_pos] + HOF_SIDEBAR + content[insert_pos:]
                        print("✅ [3/7] 사이드바 HOF 버튼 삽입 완료 (fallback)")
                    else:
                        errors.append("❌ [3/7] 사이드바 삽입 위치를 찾지 못했습니다.")
            else:
                errors.append("❌ [3/7] Gemini 사이드바 블록을 찾지 못했습니다.")
        else:
            errors.append("❌ [3/7] 플랫폼 팁 블록을 찾지 못했습니다.")
    elif "sb_hof_random" in content:
        print("⏭️  [3/7] HOF 버튼 이미 존재 — 건너뜀")
    else:
        errors.append("❌ [3/7] 사이드바 위치를 찾지 못했습니다.")

    # ── 4. 탭1 — 히스토리 저장 (st.code 출력 직후) ──
    TAB1_HIST = "        _add_history(selected_preset, st.session_state.preset_prompt, global_platform)\n"
    tab1_code = "        st.code(st.session_state.preset_prompt, language=None)\n"
    tab1_pos  = content.find(tab1_code)
    if tab1_pos != -1 and "selected_preset, st.session_state.preset_prompt" not in content:
        insert_pos = content.find("\n", tab1_pos) + 1
        content = content[:insert_pos] + TAB1_HIST + content[insert_pos:]
        print("✅ [4/7] 탭1 히스토리 저장 삽입 완료")
    elif "selected_preset, st.session_state.preset_prompt" in content:
        print("⏭️  [4/7] 탭1 히스토리 저장 이미 존재 — 건너뜀")
    else:
        errors.append("❌ [4/7] 탭1 st.code 위치를 찾지 못했습니다.")

    # ── 5. 탭3 — 랜덤 히스토리 저장 ──
    TAB3_HIST = '        _add_history("랜덤", st.session_state.random_prompt, global_platform)\n'
    tab3_code = "        st.code(st.session_state.random_prompt, language=None)\n"
    tab3_pos  = content.find(tab3_code)
    if tab3_pos != -1 and '"랜덤", st.session_state.random_prompt' not in content:
        insert_pos = content.find("\n", tab3_pos) + 1
        content = content[:insert_pos] + TAB3_HIST + content[insert_pos:]
        print("✅ [5/7] 탭3 히스토리 저장 삽입 완료")
    elif '"랜덤", st.session_state.random_prompt' in content:
        print("⏭️  [5/7] 탭3 히스토리 저장 이미 존재 — 건너뜀")
    else:
        errors.append("❌ [5/7] 탭3 st.code 위치를 찾지 못했습니다.")

    # ── 6. tab5 블록 추가 — 파일 끝 footer 바로 앞에 삽입 ──
    TAB5_BLOCK = '''
# ══════════════════════════════════════════════════════════
# 탭 5: 히스토리 & HOF 배치 생성
# ══════════════════════════════════════════════════════════
with tab5:
    st.markdown("### 📋 프롬프트 히스토리")
    st.caption("세션 내 최근 20개. 새로고침하면 초기화됩니다.")

    # HOF 배치 생성 처리
    if st.session_state.get("hof_batch_result") == "__GENERATE__":
        st.session_state.hof_batch_result = ""
        from core.builders import build_gemini_prompt as _bgp2
        _batch_lines = []
        _failed      = []
        _hof_list    = sorted(list(HOF_TIER))
        _prog        = st.progress(0, text="HOF 배치 생성 중...")
        for _i, _name in enumerate(_hof_list):
            try:
                _p = load_preset(_name)
                _prompt = _bgp2(
                    {
                        "env":      list(ENVIRONMENTS.keys())[0],
                        "light":    list(LIGHTING.keys())[0],
                        "style":    list(STYLES.keys())[0],
                        "model":    list(MODEL_TYPES.keys())[0],
                        "outfit":   list(OUTFIT_TYPES.keys())[0],
                        "material": list(MATERIALS.keys())[0],
                        "camera":   list(CAMERAS.keys())[0],
                        **_p,
                    },
                    list(ASPECT_RATIOS.keys())[0],
                    True,
                )
                _batch_lines.append(f"### [{_i+1}/{len(_hof_list)}] 👑 {_name}\\n{_prompt}\\n")
                _add_history(_name, _prompt, global_platform)
            except Exception:
                _failed.append(_name)
            _prog.progress((_i + 1) / len(_hof_list), text=f"처리 중... {_name}")
        _prog.empty()
        st.session_state.hof_batch_result = "\\n".join(_batch_lines)
        if _failed:
            st.warning(f"⚠️ JSON 없는 프리셋 {len(_failed)}개 건너뜀: {', '.join(_failed)}")
        st.success(f"✅ HOF {len(_hof_list) - len(_failed)}개 배치 생성 완료 → 히스토리에 저장됨")

    if st.session_state.hof_batch_result and st.session_state.hof_batch_result != "__GENERATE__":
        st.markdown("#### 📦 HOF 배치 결과")
        st.text_area("배치 전체", value=st.session_state.hof_batch_result, height=300)
        st.code(st.session_state.hof_batch_result, language=None)
        st.caption("👆 전체 복사 후 메모장/노션에 저장하세요.")
        if st.button("🗑️ 배치 결과 초기화"):
            st.session_state.hof_batch_result = ""
            st.rerun()
        st.markdown("---")

    # 히스토리 목록
    hist = st.session_state.prompt_history
    if not hist:
        st.info("아직 생성된 프롬프트가 없어요. 프리셋/랜덤 모드에서 생성해보세요.")
    else:
        col_l, col_r = st.columns([3, 1])
        with col_l:
            st.markdown(f"**총 {len(hist)}개** (최신순)")
        with col_r:
            if st.button("🗑️ 전체 삭제", key="hist_clear"):
                st.session_state.prompt_history = []
                st.rerun()
        for _idx, _item in enumerate(hist):
            _tier = (
                "👑" if _item["preset"] in HOF_TIER else
                "🌟" if _item["preset"] in SSS_TIER else
                "⭐" if _item["preset"] in SS_TIER  else
                "•"
            )
            _label = f"{_tier} {_item['preset']}  `{_item['platform']}`"
            with st.expander(f"{_idx+1}. {_label}", expanded=(_idx == 0)):
                st.text_area(
                    "프롬프트",
                    value=_item["prompt"],
                    height=120,
                    key=f"hist_ta_{_idx}",
                )
                st.code(_item["prompt"], language=None)
                st.caption(f"플랫폼: {_item['platform']}")

'''
    footer_anchor = 'st.markdown(\'<div style="text-align:center'
    footer_pos    = content.rfind(footer_anchor)
    if footer_pos != -1 and "with tab5:" not in content:
        content = content[:footer_pos] + TAB5_BLOCK + content[footer_pos:]
        print("✅ [6/7] 탭5 (히스토리) 블록 삽입 완료")
    elif "with tab5:" in content:
        print("⏭️  [6/7] 탭5 이미 존재 — 건너뜀")
    else:
        errors.append("❌ [6/7] footer anchor를 찾지 못했습니다.")

    # ── 7. 변경사항 저장 ──
    if content != original:
        TARGET.write_text(content, encoding="utf-8")
        print(f"✅ [7/7] dashboard.py 저장 완료")
    else:
        print("⏭️  [7/7] 변경사항 없음")

    # ── 결과 요약 ──
    print("\n" + "="*50)
    if errors:
        print("⚠️  일부 항목 실패:")
        for e in errors:
            print(f"  {e}")
        print("\n실패 항목은 위 PATCH_* 변수를 참고해 수동으로 삽입하세요.")
    else:
        print("🎉 모든 패치 완료! streamlit run dashboard.py 로 확인하세요.")
    print("="*50)
