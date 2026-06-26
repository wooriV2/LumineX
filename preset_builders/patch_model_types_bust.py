"""
LumineX core/data.py MODEL_TYPES 가슴 특화 체형 10종 추가
대상: C:\Dev\LumineX\core\data.py
방식: str.replace 앵커
"""

DATA_PATH = r"C:\Dev\LumineX\core\data.py"

# 앵커: 직전 패치에서 추가된 마지막 항목
ADD_ANCHOR = '"⚖️ 애슬레틱 커브 — 근육+볼륨 완벽 균형": "athletic curvy model, perfect balance of muscle definition and feminine curves, defined abs with round full hips, toned thick thighs, fit hourglass editorial, the best of both worlds physique",'

NEW_ENTRIES = '''
    # ── 가슴 특화 체형 (2026-06-23) ──
    "💎 바스트 퀸 — 압도적 가슴+잘록한 허리": "bust queen goddess, impossibly large full heavy bust dramatically dominating silhouette, deep dramatic cleavage, paired with extremely narrow cinched waist, average hips, top-heavy buxom editorial, chest as ultimate focal point",
    "🌺 소프트 바스트 — 크고 부드러운 자연 가슴": "soft buxom natural beauty, very full soft natural bust, generously rounded chest with natural weight and movement, gentle feminine curves throughout, naturally voluptuous upper body, soft buxom editorial presence",
    "⚡ 피트니스 바스트 — 탄탄한 몸+볼륨 가슴": "fitness bust goddess, shredded defined abs combined with surprisingly full lifted perky bust, sporty yet buxom impossible combination, gym goddess proportions, toned flat stomach below full chest, athletic buxom editorial",
    "👑 레전드 바스트 — 신화적 극강 가슴": "legendary bust goddess, mythologically enormous full bust completely dominating entire silhouette, Rubenesque upper body, maximalist buxom editorial, larger-than-life chest presence, divine feminine abundance, awe-inspiring bust scale",
    "🎀 슬림 바스트 — 마른 몸+극강 가슴 대비": "slim bust contrast model, razor-thin slender body with shockingly large full bust creating maximum contrast, waif-like slim frame below impossibly voluptuous chest, dramatic top-heavy contrast editorial, extreme bust-to-body size ratio",
    "🔥 탑헤비 글래머 — 상체 지배 실루엣": "top-heavy glamour goddess, powerful full bust and broad shoulders dramatically overshadowing slim lower body, inverted pyramid with maximum chest volume, buxom shoulder-dominant silhouette, top-heavy fashion editorial presence",
    "🌙 동양 바스트 — 슬림 동양 체형+풍만 가슴": "Asian bust contrast beauty, delicate slim East Asian physique with unexpectedly very full and heavy bust, petite frame with generous chest creating stunning contrast, exotic buxom Asian editorial, refined face with voluptuous upper body",
    "💫 핀업 바스트 — 1950s 핀업 가슴+허리": "pin-up bust glamour, 1950s Bettie Page era full lifted bust, high and round classic pin-up chest, paired with cinched corseted waist, retro buxom bombshell proportions, vintage glamour photography style bust",
    "🏆 바스트 애슬레트 — 수영선수 체형+가슴": "swimmer bust goddess, broad powerful athletic shoulders and long torso of competitive swimmer combined with surprisingly full lifted bust, sporty buxom proportions, streamlined athletic body with generous chest, aquatic goddess editorial",
    "🌊 커브드 바스트 — 가슴+힙 동시 극강": "curved bust full figure, simultaneously extremely full heavy bust and very wide round hips, both chest and hips maximally voluptuous without narrow waist, natural full-figured abundance, hourglass without cinching, generous curves top and bottom equally",'''

ADD_REPLACEMENT = ADD_ANCHOR + NEW_ENTRIES


def apply_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "바스트 퀸" in content:
        print("[SKIP] 이미 패치됨")
        return

    if ADD_ANCHOR not in content:
        print("[ERROR] 앵커를 찾을 수 없습니다.")
        return

    content = content.replace(ADD_ANCHOR, ADD_REPLACEMENT, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] 가슴 특화 체형 10종 추가 완료")


def verify_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        ("바스트 퀸", "💎 바스트 퀸"),
        ("소프트 바스트", "🌺 소프트 바스트"),
        ("피트니스 바스트", "⚡ 피트니스 바스트"),
        ("레전드 바스트", "👑 레전드 바스트"),
        ("슬림 바스트", "🎀 슬림 바스트"),
        ("탑헤비 글래머", "🔥 탑헤비 글래머"),
        ("동양 바스트", "🌙 동양 바스트"),
        ("핀업 바스트", "💫 핀업 바스트"),
        ("바스트 애슬레트", "🏆 바스트 애슬레트"),
        ("커브드 바스트", "🌊 커브드 바스트"),
    ]

    print("\n[VERIFY]")
    all_ok = True
    for pattern, label in checks:
        ok = pattern in content
        mark = "✅" if ok else "❌"
        if not ok:
            all_ok = False
        print(f"  {mark} {label}")

    print("\n✅ 전체 검증 통과!" if all_ok else "\n❌ 일부 누락")


if __name__ == "__main__":
    print("=" * 60)
    print("MODEL_TYPES 가슴 특화 체형 10종 추가")
    print(f"대상: {DATA_PATH}")
    print("=" * 60)
    apply_patch(DATA_PATH)
    verify_patch(DATA_PATH)
    print("\n다음 단계:")
    print("  git add core/data.py")
    print('  git commit -m "feat: MODEL_TYPES 가슴 특화 체형 10종 추가"')
    print("  git push")
