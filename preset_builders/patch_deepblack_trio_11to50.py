# -*- coding: utf-8 -*-
"""
DeepBlack Trio — 이레즈미 11~35번 + 아트스타일 믹스 36~50번
HOF / SSS 패치 스크립트

저장 위치: C:\Dev\LumineX\preset_builders\patch_deepblack_trio_11to50.py
"""

import ast
import shutil
from pathlib import Path

BASE = Path("C:/Dev/LumineX/core")
HOF_FILE = BASE / "hof_tier.py"
SSS_FILE = BASE / "sss_tier.py"

# ═══════════════════════════════════════════════════
# HOF 추가 목록
# ═══════════════════════════════════════════════════
NEW_HOF = [
    # 🔴 이레즈미 11~35번 HOF 15종
    "deepblack_trio_dragon_peony_koi_lotus_phoenix_sakura_goldenvoid",
    "deepblack_trio_koi_wisteria_phoenix_maple_dragon_peony_inkvoid",
    "deepblack_trio_phoenix_peony_dragon_wisteria_koi_lotus_crimsonvoid",
    "deepblack_trio_dragon_wisteria_koi_sakura_phoenix_lotus_bluevoid",
    "deepblack_trio_koi_lotus_dragon_peony_phoenix_maple_jadevoid",
    "deepblack_trio_dragon_sakura_phoenix_peony_koi_wisteria_deepvoid",
    "deepblack_trio_phoenix_lotus_koi_maple_dragon_peony_rosevoid",
    "deepblack_trio_koi_peony_dragon_lotus_phoenix_wisteria_silvervoid",
    "deepblack_trio_koi_sakura_dragon_wisteria_phoenix_peony_magentavoid",
    "deepblack_trio_phoenix_lotus_dragon_peony_koi_sakura_obsidianvoid",
    "deepblack_trio_koi_maple_phoenix_wisteria_dragon_peony_burntvoid",
    "deepblack_trio_dragon_lotus_phoenix_maple_koi_wisteria_midvoid",
    "deepblack_trio_koi_wisteria_phoenix_peony_dragon_maple_goldenvoid",
    "deepblack_trio_phoenix_maple_dragon_lotus_koi_peony_scarletvoid",
    "deepblack_trio_koi_peony_dragon_sakura_phoenix_wisteria_ultimatevoid",
    # 🎨 아트스타일 믹스 36~50번 HOF 13종
    "deepblack_trio_klimt_gogh_mucha_goldvoid",
    "deepblack_trio_thangka_artdeco_polynesian_voidbl",
    "deepblack_trio_minhwa_sumi_aztec_voidbl",
    "deepblack_trio_celtic_mughal_basquiat_voidbl",
    "deepblack_trio_gauguin_egonschiele_rivera_voidbl",
    "deepblack_trio_hokusai_basquiat_celtic_sakuranightbg",
    "deepblack_trio_mughal_polynesian_minhwa_aurorabg",
    "deepblack_trio_schiele_artdeco_rivera_neoncitybg",
    "deepblack_trio_klimt_hokusai_basquiat_voidbl",
    "deepblack_trio_mucha_polynesian_minhwa_voidbl",
    "deepblack_trio_celtic_thangka_artdeco_voidbl",
    "deepblack_trio_mughal_gauguin_schiele_voidbl",
    "deepblack_trio_rivera_aztec_klimt_voidbl",
]

# ═══════════════════════════════════════════════════
# SSS 추가 목록
# ═══════════════════════════════════════════════════
NEW_SSS = [
    # 🔴 이레즈미 11~35번 SSS 10종
    "deepblack_trio_koi_peony_phoenix_wisteria_dragon_sakura_rubyvoid",
    "deepblack_trio_phoenix_sakura_dragon_peony_koi_lotus_sunsetvoid",
    "deepblack_trio_dragon_lotus_koi_peony_phoenix_wisteria_emeraldvoid",
    "deepblack_trio_phoenix_maple_koi_wisteria_dragon_sakura_amethystvoid",
    "deepblack_trio_dragon_maple_phoenix_sakura_koi_peony_coppervoid",
    "deepblack_trio_phoenix_wisteria_koi_peony_dragon_lotus_violenvoid",
    "deepblack_trio_dragon_peony_koi_wisteria_phoenix_sakura_tealvoid",
    "deepblack_trio_phoenix_peony_dragon_sakura_koi_lotus_navyvoid",
    "deepblack_trio_dragon_peony_koi_sakura_phoenix_lotus_purplevoid",
    "deepblack_trio_dragon_maple_phoenix_sakura_koi_peony_coppervoid",
    # 🎨 아트스타일 믹스 SSS 2종
    "deepblack_trio_klimt_aztec_sumi_templebg",
    "deepblack_trio_mucha_thangka_gauguin_lavalakebg",
]


def patch_file(filepath, new_keys, label):
    content = filepath.read_text(encoding="utf-8-sig")
    added = []
    skipped = []

    for key in new_keys:
        if f'"{key}"' in content:
            skipped.append(key)
            continue
        last_brace = content.rfind("}")
        insert_line = f'    "{key}",\n'
        content = content[:last_brace] + insert_line + content[last_brace:]
        added.append(key)

    filepath.write_text(content, encoding="utf-8")

    print(f"\n{'='*55}")
    print(f"✅ {label} 패치 완료 → {filepath.name}")
    print(f"   추가: {len(added)}종 / 스킵(중복): {len(skipped)}종")
    if added:
        for k in added:
            print(f"   + {k}")
    return added


def validate(filepath):
    try:
        ast.parse(filepath.read_text(encoding="utf-8"))
        print(f"  ✅ AST OK: {filepath.name}")
        return True
    except SyntaxError as e:
        print(f"  ❌ AST 오류: {filepath.name} → {e}")
        return False


if __name__ == "__main__":
    print("🖤 DeepBlack Trio 11~50번 패치 시작")

    # 백업
    shutil.copy(HOF_FILE, HOF_FILE.with_suffix(".py.bak"))
    shutil.copy(SSS_FILE, SSS_FILE.with_suffix(".py.bak"))
    print("📦 백업 완료 (.bak)")

    # 패치
    patch_file(HOF_FILE, NEW_HOF, "HOF_TIER (이레즈미 11~35 + 아트믹스 36~50)")
    patch_file(SSS_FILE, NEW_SSS, "SSS_TIER (이레즈미 11~35 + 아트믹스 36~50)")

    # AST 검증
    print(f"\n{'='*55}")
    print("🔍 AST 검증 중...")
    hof_ok = validate(HOF_FILE)
    sss_ok = validate(SSS_FILE)

    if hof_ok and sss_ok:
        print("\n🎉 모든 검증 통과! 아래 명령어로 커밋하세요:")
        print("""
$env:PYTHONUTF8 = "1"
cd C:\\Dev\\LumineX
git add -A
git commit -m "feat: DeepBlack Trio 이레즈미 11~35 + 아트스타일믹스 36~50 HOF/SSS 패치"
git push
""")
    else:
        print("\n⚠️ 검증 실패 — 백업(.bak)으로 복구 후 확인하세요.")
