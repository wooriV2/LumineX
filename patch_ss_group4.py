"""
patch_ss_group4.py
====================
럭셔리 글래머 그룹4 — 소재/디테일 특화 처리
1. SS_TIER에 6종 추가
   feather_cascade, feather_trim_mini, cobweb_drape,
   petal_goddess, goddess_draped, sheer_overlay
2. veil_goddess JSON 삭제
3. dashboard.py 버전 업데이트

실행: python patch_ss_group4.py
"""

import re
import os
from pathlib import Path

DASHBOARD = Path("dashboard.py")
PRESETS_DIR = Path("presets")

# ── 1. 현재 상태 확인 ──────────────────────────────────────
print("=" * 50)
print("patch_ss_group4.py 시작")
print("=" * 50)

content = DASHBOARD.read_text(encoding="utf-8")

# ── 2. SS_TIER 추가 ────────────────────────────────────────
NEW_SS = [
    "feather_cascade",
    "feather_trim_mini",
    "cobweb_drape",
    "petal_goddess",
    "goddess_draped",
    "sheer_overlay",
]

# 이미 등록된 것 필터링
already = []
to_add = []
for p in NEW_SS:
    if f'"{p}"' in content:
        # SS_TIER 블록 안에 있는지 확인
        ss_match = re.search(r'SS_TIER\s*=\s*\{([^}]+)\}', content, re.DOTALL)
        if ss_match and p in ss_match.group(1):
            already.append(p)
        else:
            to_add.append(p)
    else:
        to_add.append(p)

if already:
    print(f"이미 SS_TIER에 있음 (스킵): {already}")

if to_add:
    # SS_TIER 블록의 마지막 항목 뒤에 추가
    new_entries = "\n" + "\n".join(f'    "{p}",' for p in to_add)
    
    # SS_TIER = { ... } 패턴에서 닫는 } 직전에 삽입
    pattern = r'(SS_TIER\s*=\s*\{[^}]+?)(^\s*\})'
    
    def insert_ss(m):
        return m.group(1) + new_entries + "\n" + m.group(2)
    
    new_content = re.sub(pattern, insert_ss, content, flags=re.MULTILINE | re.DOTALL)
    
    if new_content == content:
        print("❌ SS_TIER 패턴 매칭 실패 — 수동 확인 필요")
    else:
        content = new_content
        print(f"✅ SS_TIER 추가 완료: {to_add}")
else:
    print("추가할 SS 항목 없음")

# ── 3. veil_goddess JSON 삭제 ──────────────────────────────
veil_json = PRESETS_DIR / "veil_goddess.json"
if veil_json.exists():
    veil_json.unlink()
    print("✅ veil_goddess.json 삭제 완료")
else:
    print("⚠️  veil_goddess.json 없음 (이미 삭제됐거나 경로 확인 필요)")

# dashboard.py에서 veil_goddess 참조 제거
if '"veil_goddess"' in content:
    content = content.replace('"veil_goddess",\n', '')
    content = content.replace('"veil_goddess",', '')
    content = content.replace('"veil_goddess"', '')
    print("✅ dashboard.py에서 veil_goddess 참조 제거")
else:
    print("ℹ️  dashboard.py에 veil_goddess 참조 없음")

# ── 4. 버전 업데이트 ───────────────────────────────────────
# 현재 버전 찾기
ver_match = re.search(r'v(\d+\.\d+)', content)
if ver_match:
    old_ver = ver_match.group(0)
    # 마이너 버전 +1
    parts = old_ver[1:].split(".")
    parts[-1] = str(int(parts[-1]) + 1)
    new_ver = "v" + ".".join(parts)
    content = content.replace(old_ver, new_ver, 1)
    print(f"✅ 버전 업데이트: {old_ver} → {new_ver}")

# ── 5. 저장 ───────────────────────────────────────────────
DASHBOARD.write_text(content, encoding="utf-8")
print("✅ dashboard.py 저장 완료")

# ── 6. 검증 ───────────────────────────────────────────────
print("\n[ 검증 ]")
verify = DASHBOARD.read_text(encoding="utf-8")
ss_match = re.search(r'SS_TIER\s*=\s*\{([^}]+)\}', verify, re.DOTALL)
if ss_match:
    ss_block = ss_match.group(1)
    for p in NEW_SS:
        status = "✅" if p in ss_block else "❌"
        print(f"  {status} {p}")
else:
    print("  ❌ SS_TIER 블록을 찾을 수 없음")

print(f"\n  veil_goddess.json 존재: {veil_json.exists()}")

# SS 총 개수 카운트
ss_count = len(re.findall(r'"[\w_]+"', ss_block)) if ss_match else 0
print(f"\n  SS_TIER 총 항목 수: {ss_count}개")
print("\n완료! 커밋 메시지 예시:")
print('  git add -A')
print('  git commit -m "v32-fix: 럭셔리 글래머 그룹4 SS 6종 등록, veil_goddess 삭제"')
print('  git push')
