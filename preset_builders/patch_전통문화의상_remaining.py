"""
전통&문화의상 Remaining Groups SS_TIER 패치 스크립트
대상: C:\Dev\LumineX\dashboard.py
커밋 기준: 44fe008

SSS_TIER는 이미 완료 (ao_dai_sheer 등 19종 확인)
이 스크립트는 SS_TIER에 동일 19종 추가만 수행
"""

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

SS_PRESETS = [
    "ao_dai_sheer",
    "ao_dai_glamour",
    "thai_temple",
    "balinese_goddess",
    "kebaya_java",
    "harem_goddess",
    "odalisque",
    "moroccan_kaftan",
    "kaftan_sheer",
    "persian_court",
    "sari_goddess",
    "saree_draped_sensual",
    "indian_bridal",
    "belly_dancer",
    "yoruba_glamour",
    "dashiki_glam",
    "scottish_corset",
    "flamenco_dress",
    "dirndl_glam",
]

# SS_TIER 마지막 항목 (dashboard.py 확인 완료)
SS_ANCHOR = '"tropical_storm",'


def build_entries(preset_list, indent=4):
    pad = " " * indent
    return "\n".join(f'{pad}"{p}",' for p in preset_list)


def apply_patch(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if SS_ANCHOR not in content:
        print(f"[ERROR] 앵커를 찾을 수 없습니다: {SS_ANCHOR}")
        return

    # 이미 패치됐는지 확인
    if '"ao_dai_sheer",' in content[content.find(SS_ANCHOR):content.find(SS_ANCHOR)+500]:
        print("[SKIP] SS_TIER 이미 패치됨")
        return

    new_entries = build_entries(SS_PRESETS)
    replacement = f'{SS_ANCHOR}\n{new_entries}'
    content = content.replace(SS_ANCHOR, replacement, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] SS_TIER 패치 완료 — {len(SS_PRESETS)}종 추가")


def verify_patch(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # SS_TIER 블록 내에서 확인 (864번 줄 이후)
    lines = content.split("\n")
    ss_start = next((i for i, l in enumerate(lines) if "SS_TIER = {" in l), 0)
    ss_block = "\n".join(lines[ss_start:])

    print("\n[VERIFY] SS_TIER 포함 여부:")
    all_ok = True
    for p in SS_PRESETS:
        ok = f'"{p}"' in ss_block
        mark = "✅" if ok else "❌"
        if not ok:
            all_ok = False
        print(f"  {mark} {p}")

    print("\n✅ SS_TIER 검증 통과!" if all_ok else "\n❌ 일부 누락")


if __name__ == "__main__":
    print("=" * 60)
    print("전통&문화의상 SS_TIER 패치")
    print("=" * 60)
    apply_patch(DASHBOARD_PATH)
    verify_patch(DASHBOARD_PATH)
    print("\n다음 단계:")
    print("  git add dashboard.py")
    print('  git commit -m "feat: 전통문화의상 remaining groups SS tier (19종)"')
    print("  git push")
