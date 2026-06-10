"""
patch_power_presets.py
=======================
cage_fighter / sculpted_power / power_curve JSON 수정
- 스포츠/피트니스 키워드 완전 제거
- 패션 에디토리얼 방향으로 재정의

실행: python patch_power_presets.py
"""

import json
from pathlib import Path

PRESETS = {
    "cage_fighter": {
        "tag": "Cage Fighter",
        "subject": "a fierce glamorous warrior woman",
        "body": "powerful commanding figure, strong physique, intense gaze, full body shot",
        "outfit": "avant-garde cage-inspired fashion armor, metal mesh bodysuit, structural harness, razor-sharp geometric panels",
        "material": "polished metal mesh, industrial chrome hardware, sculpted black leather panels",
        "environment": "dramatic underground arena, dark industrial space, cage structure silhouette, smoke and dramatic light beams",
        "lighting": "hard dramatic spotlight from above, deep shadows, high contrast noir atmosphere",
        "style": "dark fashion editorial, Alexander McQueen aesthetic, high-fashion warrior photography",
        "quality": "shot on Sony A7R V, high contrast, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "sculpted_power": {
        "tag": "Sculpted Power",
        "subject": "a powerful goddess-like woman with commanding presence",
        "body": "statuesque figure, strong elegant silhouette, full body shot",
        "outfit": "sculptural avant-garde gown, architectural fabric panels, body-sculpting couture silhouette",
        "material": "structured bonded fabric, matte black couture, architectural pleating",
        "environment": "dramatic art museum, classical sculpture gallery, marble columns and dramatic shadows",
        "lighting": "dramatic chiaroscuro, single strong side light, deep sculptural shadows",
        "style": "sculptural fashion editorial, Versace power aesthetic, high-fashion architecture photography",
        "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
    },
    "power_curve": {
        "tag": "Power Curve",
        "subject": "a powerful curvaceous glamour model",
        "body": "powerful hourglass figure, commanding presence, full body shot",
        "outfit": "sleek latex hourglass gown, extreme curve-sculpting silhouette, thigh-high slit",
        "material": "high-gloss latex, curve-defining second-skin fabric, mirror-finish panels",
        "environment": "dramatic penthouse rooftop, city skyline at night, glass and steel architecture",
        "lighting": "dramatic neon city light reflections, high contrast glamour lighting, power shadows",
        "style": "power glamour editorial, luxury fashion photography, high-fashion curve aesthetic",
        "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"
    }
}

DANGER_WORDS = ["athletic", "fitness", "gym", "sports bra", "mma", "octagon",
                "performance fabric", "compression", "workout", "training"]

print("=" * 50)
print("patch_power_presets.py 시작")
print("=" * 50)

for name, new_data in PRESETS.items():
    path = Path(f"presets/{name}.json")

    # 백업
    if path.exists():
        bak = Path(f"presets/_bak_{name}.json")
        old = json.loads(path.read_text(encoding="utf-8"))
        bak.write_text(json.dumps(old, ensure_ascii=False, indent=2), encoding="utf-8")

    # 저장
    path.write_text(json.dumps(new_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 위험 키워드 체크
    content = json.dumps(new_data).lower()
    found = [w for w in DANGER_WORDS if w in content]
    status = f"⚠️  위험 키워드 잔존: {found}" if found else "✅ 위험 키워드 없음"
    print(f"\n[{name}] 수정 완료 — {status}")

print("\n완료! 커밋:")
print('  git add -A')
print('  git commit -m "fix: cage_fighter/sculpted_power/power_curve 스포츠 오염 수정"')
print('  git push')
