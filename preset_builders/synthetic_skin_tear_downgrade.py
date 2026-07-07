# synthetic_skin_tear_downgrade.py
# SSS_TIER에서 synthetic_skin_tear 제거 (SS 유지)
# 실행: python preset_builders/synthetic_skin_tear_downgrade.py

from pathlib import Path

target = Path("C:/Dev/LumineX/dashboard.py")
content = target.read_text(encoding="utf-8")

# SSS_TIER 내 해당 라인 제거
old = '    "synthetic_skin_tear",\n'

count = content.count(old)
print(f"발견된 항목 수: {count}개")

new = content.replace(old, "", 1)  # 첫 번째만 제거

if new == content:
    print("❌ 패치 실패 — 해당 문자열을 찾지 못했습니다.")
else:
    target.write_text(new, encoding="utf-8")
    print("✅ SSS_TIER에서 synthetic_skin_tear 제거 완료")
    print("   SS_TIER에는 그대로 유지됩니다.")

# 검증
verify = target.read_text(encoding="utf-8")
sss_count = verify.count('"synthetic_skin_tear"')
print(f"\n📊 패치 후 잔존 항목 수: {sss_count}개 (SS_TIER 1개 정상)")