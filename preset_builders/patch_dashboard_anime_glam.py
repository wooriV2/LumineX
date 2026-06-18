"""
dashboard.py SSS_TIER 애니&글래머 패치
실행: C:\Dev\LumineX\ 루트에서
  python preset_builders/patch_dashboard_anime_glam.py
"""

DASHBOARD = "dashboard.py"

OLD = '''    "maiko_bodypaint",
}'''

NEW = '''    "maiko_bodypaint",
    # 2026-06-16 애니&글래머 SSS 확정 (17종)
    "kunoichi_glam",
    "samurai_bride",
    "oni_warrior",
    "cosmic_warrior_glam",
    "dragon_princess",
    "dark_sorceress_glam",
    "neon_android",
    "android_2b",
    "vampire_seductress",
    "vampirella_dark",
    "manhwa_villainess",
    "dark_elsa",
    "anime_battle_angel",
    "poison_ivy_vines",
    "storm_goddess",
    "jessica_rabbit_glam",
    "barbarella_retro",
}'''

with open(DASHBOARD, "r", encoding="utf-8") as f:
    content = f.read()

if OLD not in content:
    print("[ERROR] 앵커 문자열을 찾지 못했습니다. dashboard.py를 확인하세요.")
else:
    content = content.replace(OLD, NEW, 1)
    with open(DASHBOARD, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] dashboard.py SSS_TIER 패치 완료")

# 검증
import subprocess
result = subprocess.run(
    ["powershell", "-Command",
     "Select-String -Path dashboard.py -Pattern 'barbarella_retro'"],
    capture_output=True, text=True
)
print(result.stdout if result.stdout else "[검증] 항목 미발견 — 패치 실패")
