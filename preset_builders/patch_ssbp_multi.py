"""
LumineX 통합 패치 스크립트
대상: dashboard.py
내용:
  1) SF&바이오펑크 G3(트랜스휴먼) + G4(바이러스&뮤테이션) 12종 → SSS_TIER 추가
  2) 멀티 바디페인팅 신규 33종 SSS 확정 패치
     - G1 추가: duo_storm_and_calm 미생성 → SSS_TIER/SS_TIER 에서 제거
     - G2 추가: trio_angel_human_demon 미생성 → 제거
     - G3 추가 6종 전원 SSS
     - G4 추가 6종 전원 SSS
     - QUAD 5종 전원 SSS (기존 1종 포함, 나머지 4종 추가)
     - QUINT 4종 전원 SSS
실행: python patch_ssbp_multi.py
결과: dashboard_patched.py 생성 후 원본 백업
"""

import re
from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")
BACKUP    = Path("C:/Dev/LumineX/dashboard_backup_pre_ssbp_multi.py")
OUTPUT    = Path("C:/Dev/LumineX/dashboard_patched.py")

# ──────────────────────────────────────────────
# 1) SF&바이오펑크 G3/G4 SSS 앵커 → SSS_TIER 추가
# ──────────────────────────────────────────────
SF_G3G4_ANCHOR = '    "corset_stockings",'   # 에로틱&페티쉬 G12 마지막 — 이 뒤에 삽입

SF_G3G4_INSERT = '''
    # 2026-06-29 SF&바이오펑크 G3 트랜스휴먼 + G4 바이러스&뮤테이션 12종 SSS
    # G3 트랜스휴먼
    "cyborg_partial_reveal",
    "neural_lace_crown",
    "exoskeleton_stripped",
    "prosthetic_art",
    "spine_tech_implant",
    "synthetic_skin_tear",
    # G4 바이러스&뮤테이션
    "mutation_bloom",
    "toxic_spore_cloud",
    "infection_glam",
    "virus_pattern_body",
    "metamorphosis_editorial",
    "alien_host_glam",'''

# ──────────────────────────────────────────────
# 2) 멀티 바디페인팅 신규 확정 패치
#    - duo_storm_and_calm / trio_angel_human_demon 미생성 제거
#    - QUAD 추가 4종 + QUINT 4종 SSS 추가
#    앵커: 기존 SSS_TIER 안의 QUINT 블록 (이미 있는 quint 4종 바로 뒤)
# ──────────────────────────────────────────────

# 현재 SSS_TIER에서 duo_storm_and_calm / trio_angel_human_demon 제거 대상
REMOVE_SSS = [
    '"duo_storm_and_calm_bodypaint",',
    '"trio_angel_human_demon_bodypaint",',
]

# 현재 SS_TIER에서도 제거
REMOVE_SS = [
    '"duo_storm_and_calm_bodypaint",',
    '"trio_angel_human_demon_bodypaint",',
]

# QUINT 블록 뒤에 "검증 예정" 주석 제거 및 확정 표시 추가
# 앵커: SSS_TIER 안의 quint 마지막 줄
QUINT_SSS_ANCHOR = '    "quint_five_oceans_bodypaint",'   # SSS_TIER 안

QUINT_SSS_REPLACE = '''    "quint_five_oceans_bodypaint",
    # ↑ 2026-06-29 멀티 바디페인팅 QUINT 4종 SSS 확정 (전원 SSS)'''

# ──────────────────────────────────────────────
# 3) SS_TIER 쪽 멀티 바디페인팅 블록 주석 업데이트
#    (# 검증 예정) → (# SSS 확정)
# ──────────────────────────────────────────────

# ──────────────────────────────────────────────
# SF&바이오펑크 SS_TIER 앵커 추가 (SS_TIER에도 G3/G4 포함)
# ──────────────────────────────────────────────
# 기존 SS_TIER 에로틱 G3~G12 블록 마지막 줄 뒤에 삽입
SF_SS_ANCHOR = '    "corset_stockings",'   # SS_TIER 안의 동일 앵커

SF_SS_INSERT = '''
    # 2026-06-29 SF&바이오펑크 G3/G4 SSS→SS 포함
    "cyborg_partial_reveal",
    "neural_lace_crown",
    "exoskeleton_stripped",
    "prosthetic_art",
    "spine_tech_implant",
    "synthetic_skin_tear",
    "mutation_bloom",
    "toxic_spore_cloud",
    "infection_glam",
    "virus_pattern_body",
    "metamorphosis_editorial",
    "alien_host_glam",'''


def apply_patch(content: str) -> str:
    """모든 패치를 순서대로 적용"""

    # ── STEP 1: SSS_TIER에서 미생성 2종 제거 ──
    for token in REMOVE_SSS:
        # SSS_TIER 블록 안의 해당 줄만 제거 (주석 포함 줄 처리)
        # 줄 단위 제거 (앞 공백 포함, 뒤 줄바꿈 포함)
        pattern = r'[ \t]*' + re.escape(token) + r'[ \t]*(#[^\n]*)?\n'
        count = len(re.findall(pattern, content))
        content = re.sub(pattern, '', content)
        print(f"  [SSS 제거] {token.strip()} — {count}개 삭제")

    # ── STEP 2: SS_TIER에서 미생성 2종 제거 ──
    # (이미 STEP 1에서 제거됐으므로 추가 제거는 스킵 — 동일 패턴)

    # ── STEP 3: SSS_TIER에 SF&바이오펑크 G3/G4 12종 추가 ──
    sss_anchor = '    "corset_stockings",'
    # SSS_TIER 블록과 SS_TIER 블록에 각각 존재하므로 첫 번째 출현(SSS)에만 삽입
    idx = content.find(sss_anchor)
    if idx == -1:
        print("  [ERROR] SSS_TIER corset_stockings 앵커를 찾을 수 없습니다!")
        return content
    # 해당 줄 끝 위치 찾기
    line_end = content.find('\n', idx)
    insert_pos = line_end + 1
    content = content[:insert_pos] + SF_G3G4_INSERT + '\n' + content[insert_pos:]
    print(f"  [SSS 추가] SF&바이오펑크 G3/G4 12종 → SSS_TIER")

    # ── STEP 4: SS_TIER에도 SF&바이오펑크 G3/G4 추가 ──
    # SSS 삽입 후 두 번째 corset_stockings 찾기
    second_idx = content.find(sss_anchor, idx + len(sss_anchor) + 100)
    if second_idx == -1:
        print("  [WARN] SS_TIER corset_stockings 앵커를 찾을 수 없습니다 — SS 추가 스킵")
    else:
        line_end2 = content.find('\n', second_idx)
        insert_pos2 = line_end2 + 1
        content = content[:insert_pos2] + SF_SS_INSERT + '\n' + content[insert_pos2:]
        print(f"  [SS 추가] SF&바이오펑크 G3/G4 12종 → SS_TIER")

    # ── STEP 5: 검증 예정 주석 → 확정 주석으로 교체 ──
    replacements = [
        # G1 추가 주석
        ('# G1 추가 (검증 예정)', '# G1 추가 (SSS 확정 — duo_storm_and_calm 미생성 제외)'),
        # G2 추가 주석
        ('# G2 추가 (검증 예정)', '# G2 추가 (SSS 확정 — trio_angel_human_demon 미생성 제외)'),
        # G3 추가 주석
        ('# G3 추가 (검증 예정)', '# G3 추가 (SSS 확정 전원)'),
        # G4 추가 주석
        ('# G4 추가 (검증 예정)', '# G4 추가 (SSS 확정 전원)'),
        # QUAD 주석
        ('# QUAD 4인 (검증 예정)', '# QUAD 4인 (SSS 확정 전원)'),
        # QUINT 주석
        ('# QUINT 5인 (검증 예정)', '# QUINT 5인 (SSS 확정 전원)'),
    ]
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"  [주석 업데이트] {old[:40]}...")
        else:
            print(f"  [WARN] 주석 미발견: {old[:40]}")

    return content


def verify_patch(content: str):
    """패치 결과 검증"""
    print("\n── 검증 ──────────────────────────────────")
    checks = [
        # SF G3/G4 SSS
        ('"cyborg_partial_reveal"', 'SF G3 cyborg_partial_reveal'),
        ('"synthetic_skin_tear"', 'SF G3 synthetic_skin_tear'),
        ('"mutation_bloom"', 'SF G4 mutation_bloom'),
        ('"alien_host_glam"', 'SF G4 alien_host_glam'),
        # 미생성 제거 확인
        ('"duo_storm_and_calm_bodypaint"', '미생성 duo_storm_and_calm (있으면 FAIL)'),
        ('"trio_angel_human_demon_bodypaint"', '미생성 trio_angel_human_demon (있으면 FAIL)'),
        # QUINT 확인
        ('"quint_five_oceans_bodypaint"', 'QUINT quint_five_oceans'),
        ('"quint_five_continents_bodypaint"', 'QUINT quint_five_continents'),
    ]
    for token, label in checks:
        count = content.count(token)
        if '미생성' in label:
            status = '✅ 제거됨' if count == 0 else f'❌ 아직 {count}개 남아있음!'
        else:
            status = f'✅ {count}개' if count > 0 else '❌ 없음!'
        print(f"  {label}: {status}")

    # SSS/SS tier 카운트
    sss_block_start = content.find('SSS_TIER = {')
    sss_block_end   = content.find('\nSS_TIER = {')
    ss_block_end    = content.find('\n# ─── 다크 테마')
    sss_count = content[sss_block_start:sss_block_end].count('"')  // 2
    ss_count  = content[sss_block_end:ss_block_end].count('"') // 2 if ss_block_end > 0 else 0
    print(f"\n  SSS_TIER 토큰 수 (참고): ~{sss_count}")
    print(f"  SS_TIER 토큰 수 (참고): ~{ss_count}")


def main():
    if not DASHBOARD.exists():
        print(f"[ERROR] dashboard.py 없음: {DASHBOARD}")
        return

    print(f"[INFO] 읽기: {DASHBOARD}")
    content = DASHBOARD.read_text(encoding='utf-8')
    original_len = len(content)

    # 백업
    BACKUP.write_text(content, encoding='utf-8')
    print(f"[INFO] 백업 완료: {BACKUP}")

    print("\n── 패치 적용 ──────────────────────────────")
    patched = apply_patch(content)

    verify_patch(patched)

    OUTPUT.write_text(patched, encoding='utf-8')
    print(f"\n[OK] 패치 완료: {OUTPUT}")
    print(f"     원본 {original_len:,}자 → 패치 {len(patched):,}자 (+{len(patched)-original_len:,}자)")
    print("\n다음 단계:")
    print("  1. dashboard_patched.py 내용 확인")
    print("  2. 문제 없으면: copy dashboard_patched.py dashboard.py")
    print("  3. PowerShell 검증:")
    print('     Select-String -Path dashboard.py -Pattern "cyborg_partial_reveal" -Context 1,1')
    print('     Select-String -Path dashboard.py -Pattern "quint_five_oceans_bodypaint" -Context 1,1')
    print('     Select-String -Path dashboard.py -Pattern "duo_storm_and_calm_bodypaint"')
    print("  4. git add dashboard.py && git commit -m '멀티바디페인팅 신규33종+SF바이오펑크G3/G4 SSS확정 패치'")


if __name__ == '__main__':
    main()
