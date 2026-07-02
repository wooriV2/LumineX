"""
LumineX dashboard.py 패치
🌀 환경 일체 바디페인팅 22종 추가

- PRESET_CATEGORIES에 신규 카테고리 추가
- SSS_TIER에 검증 완료 종 등록
- SS_TIER에 SSS 포함 전체 등록

실행: python preset_builders/patch_merge_bodypaint.py
"""

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

# ── 카테고리 목록 ──
MERGE_CATEGORY = '''    "🌀 환경 일체 바디페인팅": [
        # G1 패턴/직물 (6종 SSS)
        "merge_butterfly_fabric",
        "merge_floral_wallpaper",
        "merge_leopard_fabric",
        "merge_mandala_carpet",
        "merge_toile_pattern",
        "merge_tartan_plaid",
        # G2 자연환경 (5종 SSS/SS)
        "merge_salt_flat_sky",
        "merge_autumn_leaves_floor",
        "merge_coral_reef_water",
        "merge_sand_dunes",
        "merge_moss_stone_ground",
        # G3 건축/소재 (5종 SSS)
        "merge_clockwork_gears",
        "merge_marble_column_wall",
        "merge_islamic_tile_wall",
        "merge_stained_glass_window",
        "merge_circuit_board",
        # G4 예술/회화 (6종 SSS)
        "merge_klimt_gold_mural",
        "merge_vangogh_starry",
        "merge_ukiyo_wave_print",
        "merge_mondrian_grid",
        "merge_pollock_splatter",
        "merge_byzantine_mosaic",
    ],'''

# ── SSS tier 추가 항목 ──
SSS_NEW = '''    # 2026-07-02 환경 일체 바디페인팅 SSS (20종)
    # G1 패턴/직물
    "merge_butterfly_fabric",
    "merge_floral_wallpaper",
    "merge_leopard_fabric",
    "merge_mandala_carpet",
    "merge_toile_pattern",
    "merge_tartan_plaid",
    # G2 자연환경
    "merge_autumn_leaves_floor",
    "merge_coral_reef_water",
    "merge_sand_dunes",
    # G3 건축/소재
    "merge_clockwork_gears",
    "merge_marble_column_wall",
    "merge_islamic_tile_wall",
    "merge_stained_glass_window",
    "merge_circuit_board",
    # G4 예술/회화
    "merge_klimt_gold_mural",
    "merge_vangogh_starry",
    "merge_ukiyo_wave_print",
    "merge_mondrian_grid",
    "merge_pollock_splatter",
    "merge_byzantine_mosaic",'''

# ── SS tier 추가 항목 (SSS 20종 + SS 전용 2종) ──
SS_NEW = '''    # 2026-07-02 환경 일체 바디페인팅 SS (22종 전체)
    "merge_butterfly_fabric",
    "merge_floral_wallpaper",
    "merge_leopard_fabric",
    "merge_mandala_carpet",
    "merge_toile_pattern",
    "merge_tartan_plaid",
    "merge_salt_flat_sky",
    "merge_autumn_leaves_floor",
    "merge_coral_reef_water",
    "merge_sand_dunes",
    "merge_moss_stone_ground",
    "merge_clockwork_gears",
    "merge_marble_column_wall",
    "merge_islamic_tile_wall",
    "merge_stained_glass_window",
    "merge_circuit_board",
    "merge_klimt_gold_mural",
    "merge_vangogh_starry",
    "merge_ukiyo_wave_print",
    "merge_mondrian_grid",
    "merge_pollock_splatter",
    "merge_byzantine_mosaic",'''

# ── 앵커 ──
# PRESET_CATEGORIES 마지막 카테고리 끝 (🧬 SF & 바이오펑크 뒤)
CAT_ANCHOR = '''    "🧬 SF & 바이오펑크": ['''

CAT_ANCHOR_END = '''}


# SSS tier'''

# SSS_TIER 닫는 } 앞 앵커
SSS_ANCHOR = '''    "joseon_boudoir",

}

# SS tier'''

# SS_TIER 닫는 } 앞 앵커
SS_ANCHOR = '''    # 2026-06-29 멀티 바디페인팅 SS (57종 전체)'''


def apply_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # ── 중복 체크 ──
    if "🌀 환경 일체 바디페인팅" in content:
        print("[SKIP] 이미 패치됨 (환경 일체 바디페인팅 존재)")
        return

    # ── 1. PRESET_CATEGORIES에 카테고리 추가 ──
    # SF&바이오펑크 카테고리 전체 블록 뒤에 삽입
    # 닫는 }, 를 찾아서 그 뒤에 새 카테고리 추가
    SF_BLOCK_END = '''        "alien_host_glam",
    ],

}'''

    NEW_CAT_BLOCK = f'''        "alien_host_glam",
    ],

{MERGE_CATEGORY}

}}'''

    if SF_BLOCK_END not in content:
        # 대안: PRESET_CATEGORIES 닫는 } 바로 앞에 삽입
        ALT_ANCHOR = "\n}\n\n\n# SSS tier"
        if ALT_ANCHOR not in content:
            print("[ERROR] PRESET_CATEGORIES 앵커를 찾을 수 없습니다.")
            print("수동으로 다음 내용을 PRESET_CATEGORIES } 바로 앞에 추가하세요:")
            print(MERGE_CATEGORY)
            return
        content = content.replace(
            ALT_ANCHOR,
            f"\n{MERGE_CATEGORY}\n}}\n\n\n# SSS tier"
        )
        print("[OK] PRESET_CATEGORIES 대안 앵커로 카테고리 추가")
    else:
        content = content.replace(SF_BLOCK_END, NEW_CAT_BLOCK)
        print("[OK] PRESET_CATEGORIES 카테고리 추가")

    # ── 2. SSS_TIER에 추가 ──
    if '"joseon_boudoir",' in content:
        content = content.replace(
            '    "joseon_boudoir",',
            f'    "joseon_boudoir",\n\n{SSS_NEW}'
        )
        print("[OK] SSS_TIER 추가")
    else:
        print("[WARN] SSS_TIER 앵커 미발견 — 수동 추가 필요")
        print(SSS_NEW)

    # ── 3. SS_TIER에 추가 ──
    SS_ANCHOR_STR = '    # 2026-06-29 멀티 바디페인팅 SS (57종 전체)'
    if SS_ANCHOR_STR in content:
        content = content.replace(
            SS_ANCHOR_STR,
            f"{SS_NEW}\n\n    # 2026-06-29 멀티 바디페인팅 SS (57종 전체)"
        )
        print("[OK] SS_TIER 추가")
    else:
        print("[WARN] SS_TIER 앵커 미발견 — 수동 추가 필요")
        print(SS_NEW)

    # ── 저장 ──
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ 패치 완료: {path}")


def verify(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        ("🌀 환경 일체 바디페인팅", "PRESET_CATEGORIES 카테고리"),
        ("merge_butterfly_fabric", "G1 첫 번째 프리셋"),
        ("merge_byzantine_mosaic", "G4 마지막 프리셋"),
        ("merge_autumn_leaves_floor", "SSS/SS 등록"),
    ]
    print("\n=== 검증 ===")
    for keyword, label in checks:
        count = content.count(keyword)
        status = "✅" if count >= 1 else "❌"
        print(f"{status} {label}: {count}회 발견")


if __name__ == "__main__":
    print("🌀 환경 일체 바디페인팅 dashboard.py 패치")
    print(f"대상: {DASHBOARD_PATH}")
    print()
    answer = input("패치 진행할까요? (y/n): ")
    if answer.lower() == "y":
        apply_patch(DASHBOARD_PATH)
        verify(DASHBOARD_PATH)
    else:
        print("취소됨")
