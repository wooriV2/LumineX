"""
SPECIAL_EFFECTS 6종 추가 패치
앵커: 네온 빛줄기 (실제 마지막 항목)
"""

DATA_PATH = r"C:\Dev\LumineX\core\data.py"

ANCHOR = '    "네온 빛줄기 — 네온 레이저 빛": "neon laser light beams, colorful light rays cutting through",\n}'

REPLACEMENT = '''    "네온 빛줄기 — 네온 레이저 빛": "neon laser light beams, colorful light rays cutting through",
    "홀로그램 — 홀로그램 프로젝션": "holographic projection effects, iridescent light grid patterns, translucent hologram layers surrounding model, sci-fi editorial",
    "매트릭스 코드 — 디지털 레인": "matrix digital rain effect, green cascading code falling around model, cyberpunk digital reality, dark editorial",
    "버블 — 비누방울 가득": "soap bubble cloud surrounding model, hundreds of floating iridescent bubbles, rainbow reflections in each bubble, whimsical editorial",
    "크리스탈 성장 — 몸에서 크리스탈 자라는": "crystals growing from body and surroundings, gemstone formations erupting, magical mineral growth effect, fantasy editorial",
    "중력 역전 — 물체가 위로": "gravity reversal effect, objects and fabric floating upward, everything defying gravity around model, surreal editorial",
    "오로라 커튼 — 오로라 빛이 드리워지는": "aurora borealis curtain of light surrounding model, ethereal northern lights ribbons, magical atmospheric glow, mystical editorial",
}'''


def apply_patch(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "홀로그램 — 홀로그램 프로젝션" in content:
        print("[SKIP] 이미 패치됨")
        return

    if ANCHOR not in content:
        print("[ERROR] 앵커 미발견")
        # 디버그: 실제 마지막 부분 출력
        idx = content.find("네온 빛줄기")
        if idx > 0:
            print(f"[DEBUG] 주변 텍스트:\n{repr(content[idx:idx+200])}")
        return

    content = content.replace(ANCHOR, REPLACEMENT, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] SPECIAL_EFFECTS 6종 추가 완료")


def verify_patch(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        "홀로그램 — 홀로그램 프로젝션",
        "매트릭스 코드",
        "버블 — 비누방울",
        "크리스탈 성장",
        "중력 역전",
        "오로라 커튼",
    ]
    print("\n[VERIFY]")
    all_ok = True
    for c in checks:
        ok = c in content
        mark = "✅" if ok else "❌"
        if not ok: all_ok = False
        print(f"  {mark} {c}")
    print("\n✅ 완료!" if all_ok else "\n❌ 누락")


if __name__ == "__main__":
    print("=" * 50)
    print("SPECIAL_EFFECTS 6종 추가 패치")
    print("=" * 50)
    apply_patch(DATA_PATH)
    verify_patch(DATA_PATH)
    print("\n다음 단계:")
    print("  git add core/data.py")
    print('  git commit -m "feat: SPECIAL_EFFECTS 6종 추가"')
    print("  git push")
