"""
patch_20260628_korean_history_g5b_g8.py

대상: 한국 역사&궁중 글래머 G5 후반부~G8 검증분 SSS/SS 패치
검증 결과:
  G5 후반부 (6종): SSS 6/6
  G6 민속&세시풍속 (8종): SSS 7 / SS 1 (haenyeo_wet_glam)
  G7 여전사&무인 (8종): SSS 8/8
  G8 근대&퓨전 (8종): SSS 8/8

총계: SSS 29종 신규 추가 / SS 1종 (haenyeo_wet_glam — SSS_TIER 제외, SS_TIER만)
커밋 대상: dashboard.py
"""

import re
from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")

# ──────────────────────────────────────────────
# 1. SSS_TIER 패치
# ──────────────────────────────────────────────

SSS_ANCHOR = '    # G5 신화&정령 전반부 — SSS 6종\n    "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",\n    "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",'

SSS_REPLACEMENT = '''\
    # G5 신화&정령 전반부 — SSS 6종
    "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",
    "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",
    # G5 신화&정령 후반부 — SSS 6종
    "seonnyeo_descent", "haenyeo_mermaid", "baeksa_serpent",
    "chamsuri_ghost", "taoist_fairy_korea", "nine_tail_dominatrix",
    # G6 민속&세시풍속 — SSS 7종 (haenyeo_wet_glam은 SS 전용)
    "dano_festival_glam", "ganggangsullae_night",
    "mudang_fire_ritual", "mudang_trance_glam", "namsadang_acrobat",
    "jeju_shaman_sea", "korean_harvest_goddess",
    # G7 여전사&무인 — SSS 8종
    "joseon_female_assassin", "goryeo_archer_queen", "silla_female_hwarang",
    "joseon_damo_noir", "tiger_huntress_korea", "wonhyang_warrior",
    "goguryeo_fire_warrior", "joseon_spy_sheer",
    # G8 근대&퓨전 — SSS 8종
    "joseon_modern_fusion", "gisaeng_cyberpunk", "hanbok_latex_queen",
    "joseon_noir", "gisaeng_opium_den", "korean_vamp_modern",
    "hanbok_wet_editorial", "joseon_boudoir",'''

# ──────────────────────────────────────────────
# 2. SS_TIER 패치 — 기존 한국 역사 블록에 신규 29+1종 추가
# ──────────────────────────────────────────────

SS_ANCHOR = '''\
    "seonnyeo_descent", "haenyeo_mermaid", "baeksa_serpent",
    "chamsuri_ghost", "taoist_fairy_korea", "nine_tail_dominatrix",
    "haenyeo_wet_glam", "dano_festival_glam", "ganggangsullae_night",
    "mudang_fire_ritual", "mudang_trance_glam", "namsadang_acrobat",
    "jeju_shaman_sea", "korean_harvest_goddess",
    "joseon_female_assassin", "goryeo_archer_queen", "silla_female_hwarang",
    "joseon_damo_noir", "tiger_huntress_korea", "wonhyang_warrior",
    "goguryeo_fire_warrior", "joseon_spy_sheer",
    "joseon_modern_fusion", "gisaeng_cyberpunk", "hanbok_latex_queen",
    "joseon_noir", "gisaeng_opium_den", "korean_vamp_modern",
    "hanbok_wet_editorial", "joseon_boudoir",'''

# SS_TIER의 기존 한국 역사 블록은 dashboard.py에 이미 78종 전체가 있음.
# G5 후반부~G8이 아직 없으면 아래 앵커로 추가.

SS_ANCHOR_CHECK = '"gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",'

SS_NEW_BLOCK = '''\
    "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",
    "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",
    "seonnyeo_descent", "haenyeo_mermaid", "baeksa_serpent",
    "chamsuri_ghost", "taoist_fairy_korea", "nine_tail_dominatrix",
    "haenyeo_wet_glam", "dano_festival_glam", "ganggangsullae_night",
    "mudang_fire_ritual", "mudang_trance_glam", "namsadang_acrobat",
    "jeju_shaman_sea", "korean_harvest_goddess",
    "joseon_female_assassin", "goryeo_archer_queen", "silla_female_hwarang",
    "joseon_damo_noir", "tiger_huntress_korea", "wonhyang_warrior",
    "goguryeo_fire_warrior", "joseon_spy_sheer",
    "joseon_modern_fusion", "gisaeng_cyberpunk", "hanbok_latex_queen",
    "joseon_noir", "gisaeng_opium_den", "korean_vamp_modern",
    "hanbok_wet_editorial", "joseon_boudoir",'''


def patch():
    text = DASHBOARD.read_text(encoding="utf-8")
    original = text

    # ── SSS_TIER 패치 ──
    if SSS_ANCHOR in text:
        text = text.replace(SSS_ANCHOR, SSS_REPLACEMENT)
        print("[SSS_TIER] G5후반부~G8 29종 추가 완료")
    else:
        print("[SSS_TIER] 앵커를 찾지 못했습니다. 수동 확인 필요.")

    # ── SS_TIER 패치 ──
    # G5 전반부 라인이 SS_TIER에 있고 후반부가 없으면 교체
    if SS_ANCHOR_CHECK in text:
        # 이미 후반부가 포함되어 있는지 확인
        if '"seonnyeo_descent"' not in text.split(SS_ANCHOR_CHECK, 1)[1][:500]:
            text = text.replace(
                '    "gumiho_latex", "gumiho_red_moon", "samshin_goddess_glam",\n    "dragon_daughter_sea", "imoogi_seduction", "dokkaebi_girl",',
                SS_NEW_BLOCK
            )
            print("[SS_TIER] G5후반부~G8 30종(SSS 29+SS 1) 추가 완료")
        else:
            print("[SS_TIER] 이미 패치되어 있습니다.")
    else:
        print("[SS_TIER] SS_ANCHOR_CHECK를 찾지 못했습니다. 수동 확인 필요.")

    if text != original:
        DASHBOARD.write_text(text, encoding="utf-8")
        print("\n✅ dashboard.py 저장 완료")
    else:
        print("\n⚠️  변경 없음 — 이미 패치되어 있거나 앵커 불일치")


if __name__ == "__main__":
    patch()
