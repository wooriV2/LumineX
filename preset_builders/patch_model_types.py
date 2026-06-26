"""
LumineX core/data.py MODEL_TYPES 패치
- 수정: 12종 (프롬프트 부정확/중복/불일치)
- 추가: 8종 (빠진 체형)

대상: C:\Dev\LumineX\core\data.py
방식: str.replace 앵커
"""

DATA_PATH = r"C:\Dev\LumineX\core\data.py"

# ══════════════════════════════════════════════════════════
# 수정 항목 (old → new)
# ══════════════════════════════════════════════════════════
FIXES = [

    # ── 🔴 심각 수정 3종 ──────────────────────────────────

    # 1. 비키니 컴페티션 — round athletic hips 제거, 극lean 강조
    (
        '"비키니 컴페티션 — 대회용 극강 근육": "bikini competition model, extremely defined muscles, shredded competition physique, round athletic hips, competition-ready body",',
        '"비키니 컴페티션 — 대회용 극강 근육": "bikini competition model, stage-ready shredded physique, extremely defined muscles with zero body fat, tight flat glutes, angular lean hips, razor-sharp muscle definition, competition-ready body, tanned oiled skin",',
    ),

    # 2. BBW 글래머 — layered 제거
    (
        '"BBW 글래머 — 풍만한 글래머": "BBW glamour model, extremely curvy fashion silhouette, broad hips, thick thighs, soft layered abdomen, luxurious BBW presence, confident couture",',
        '"BBW 글래머 — 풍만한 글래머": "BBW glamour model, extremely curvy fashion silhouette, broad wide hips, very thick thighs, soft full rounded abdomen, abundant voluptuous curves, luxurious BBW presence, confident couture editorial",',
    ),

    # 3. 슈퍼 BBW — body folds 제거
    (
        '"슈퍼 BBW — 극풍만 글래머": "super plus-size runway model, massive voluptuous proportions, very heavy curvy physique, broad hips, thick thighs, soft realistic body folds, abundant body volume, maximalist curvy fashion styling",',
        '"슈퍼 BBW — 극풍만 글래머": "super plus-size runway model, massive voluptuous proportions, very heavy curvy physique, extremely broad wide hips, very thick full thighs, soft rounded abundant belly, maximalist curvy fashion styling, bold confident editorial presence",',
    ),

    # ── 🟡 차별화 수정 5종 ────────────────────────────────

    # 4. 울트라 슬림 — 극세장+쇄골 강조
    (
        '"울트라 슬림 — 하이패션 극세장": "ultra-slim high fashion model, very slender editorial figure, elongated silhouette, fashion week physique",',
        '"울트라 슬림 — 하이패션 극세장": "ultra-slim high fashion model, razor-thin elongated silhouette, visible sharp collarbones, hollow cheeks, waif-like editorial physique, fashion week extreme slenderness, angular delicate frame",',
    ),

    # 5. 슈퍼 슬림 — 마른+미니멀 커브 강조
    (
        '"슈퍼 슬림 — 마른 런웨이": "super slim runway model, thin elegant frame, elongated slender body, editorial fashion model",',
        '"슈퍼 슬림 — 마른 런웨이": "super slim runway model, very thin lean frame, minimal curves, flat chest, boyish slim hips, elongated slender body, androgynous editorial fashion model, breakable delicate silhouette",',
    ),

    # 6. 슬림 런웨이 — 키+다리 길이 강조
    (
        '"슬림 런웨이 — 초장신 늘씬": "tall slim runway model, long legs, slender waist, narrow hips, elongated graceful silhouette",',
        '"슬림 런웨이 — 초장신 늘씬": "tall slim runway model over 180cm, disproportionately long legs dominating silhouette, slender waist, narrow hips, extremely elongated graceful figure, towering editorial presence",',
    ),

    # 7. 핫 글래머 — 수치감 추가
    (
        '"핫 글래머 — 잘록한 허리+볼륨": "hot glamour model, narrow cinched waist, wide round hips, dramatic hourglass figure",',
        '"핫 글래머 — 잘록한 허리+볼륨": "hot glamour model, dramatically cinched narrow waist, va-va-voom wide round hips, 0.65 waist-to-hip ratio, full bust, smoldering hourglass figure, red carpet curves",',
    ),

    # 8. 슈퍼 글래머 — 수치감+핀업 강조
    (
        '"슈퍼 글래머 — 극강 모래시계": "super glamour model, tiny waist, very wide round hips, maximum hourglass silhouette, pinup glamour",',
        '"슈퍼 글래머 — 극강 모래시계": "super glamour model, impossibly tiny corseted waist, 0.55 waist-to-hip ratio, extremely wide round heavy hips, maximum pinup hourglass silhouette, lush full bust, Bettie Page-level curves",',
    ),

    # ── 🟠 이름-프롬프트 불일치 수정 4종 ─────────────────

    # 9. 스포츠 글램 — sports 키워드 추가
    (
        '"스포츠 글램 — 탄탄+볼륨": "sports glamour model, toned athletic body with curves, defined abs, round hips, fit and voluptuous",',
        '"스포츠 글램 — 탄탄+볼륨": "sports glamour model, athletic toned physique with feminine curves, defined six-pack abs, round lifted hips, fit voluptuous energy, gym-to-runway body, powerful yet sensual athletic figure",',
    ),

    # 10. 발레리나 — 발레 특유 근육 추가
    (
        '"발레리나 — 길고 가늘고 우아한": "ballerina physique, slender elongated figure, narrow hips, graceful elegant posture, dancer\'s perfect poise",',
        '"발레리나 — 길고 가늘고 우아한": "ballerina physique, slender elongated figure, defined calf muscles, strong lean back, narrow hips, graceful elegant posture, turned-out feet, dancer\'s poised carriage, visible shoulder blade definition",',
    ),

    # 11. VS 앤젤 — 수치+구체적 표현
    (
        '"VS 앤젤 — 완벽한 VS 글래머": "Victoria\'s Secret Angel body, toned flat abs, long legs, curvaceous yet athletic silhouette, runway perfect",',
        '"VS 앤젤 — 완벽한 VS 글래머": "Victoria\'s Secret Angel body, toned flat abs, model-perfect 34-24-35 proportions, legs over 90cm long, subtle feminine hourglass, runway-ready athletic glamour, glowing healthy skin, wings-ready editorial presence",',
    ),

    # 12. 블랙 글래머 — 힙+실루엣 강화
    (
        '"블랙 글래머 — 극강 모래시계 흑인 체형": "Black beauty hourglass, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, very thick thighs, full heavy round buttocks, abundant voluptuous curves, African goddess proportions",',
        '"블랙 글래머 — 극강 모래시계 흑인 체형": "Black beauty hourglass goddess, impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, very thick powerful thighs, powerfully lifted full round buttocks projecting dramatically, abundant voluptuous curves, African goddess proportions, deep luminous rich skin, statuesque commanding presence",',
    ),

    # ── 🟢 소폭 개선 3종 ──────────────────────────────────

    # 13. K팝 아이돌 — 비율 디테일 추가
    (
        '"🇰🇷 K팝 아이돌 — 슬림+작은 얼굴+긴 다리": "K-pop idol proportions, extremely slim slender figure, small delicate face, disproportionately long legs, 168-172cm idol physique, flat stomach, narrow shoulders, youthful fresh Korean pop star body",',
        '"🇰🇷 K팝 아이돌 — 슬림+작은 얼굴+긴 다리": "K-pop idol proportions, extremely slim slender figure, small delicate face with tiny head-to-body ratio, disproportionately long legs, 168-172cm idol physique, flat stomach, narrow shoulders, delicate wrists and ankles, youthful fresh Korean pop star body, idol-perfect refined proportions",',
    ),

    # 14. 플러스 글램 — 자신감 표현 추가
    (
        '"플러스 글램 — 플러스사이즈 글래머": "plus-size glamour model, soft belly, wide full hips, thick thighs, confident couture presence",',
        '"플러스 글램 — 플러스사이즈 글래머": "plus-size glamour model, soft rounded belly, wide full hips, thick thighs, confidently plus-size bold couture presence, unapologetically curvaceous editorial energy, full-figured runway power",',
    ),

    # 15. 소프트 글램 — 글래머 요소 강화 (내추럴 커브와 차별화)
    (
        '"소프트 글램 — 부드러운 여성미": "soft glamour model, feminine gentle curves, round soft hips, elegant graceful figure, naturally beautiful",',
        '"소프트 글램 — 부드러운 여성미": "soft glamour model, polished feminine curves, subtle waist definition, round soft hips, gentle editorial elegance, naturally beautiful with glamour refinement, graceful sophisticated figure",',
    ),
]

# ══════════════════════════════════════════════════════════
# 추가 항목 — MODEL_TYPES 마지막 항목 뒤에 삽입
# ══════════════════════════════════════════════════════════

# 앵커: MODEL_TYPES 마지막 항목
ADD_ANCHOR = '"🌌 거인 여신 — 현실 불가능한 신화적 스케일": "mythological giant goddess scale, impossibly towering divine proportions, colossal feminine figure, deity-scale body, universe-spanning goddess physique, transcendent scale beyond human",'

NEW_ENTRIES = '''
    # ── 신규 추가 (2026-06-23) ──
    "헬시 내추럴 — 건강하고 보통인 체형": "healthy natural physique, average realistic proportions, relatable everyday womanly figure, soft natural curves, modest bust and hips, comfortable in her own skin, authentic body positive editorial",
    "🇯🇵 J팝 글래머 — 슬림+볼륨 일본 성인 글래머": "Japanese glamour model, slim petite waist with surprisingly full bust and round hips, adult idol proportions, petite yet voluptuous Japanese figure, delicate face with lush curves, J-glamour editorial",
    "🇨🇳 C팝 아이돌 — 중국 아이돌 체형": "Chinese C-pop idol proportions, slim elegant figure, long graceful legs, delicate refined features, subtle feminine curves, porcelain skin editorial, Douyin-era beauty standard physique",
    "🕌 아라비안 글래머 — 중동 볼륨 미인": "Arabian glamour beauty, full curvaceous hourglass figure, warm olive skin, Middle Eastern voluptuous proportions, lush round hips, belly dancer sensual curves, exotic editorial presence",
    "🇲🇽 멕시칸 핫 — 라틴 파이어 볼륨": "Mexican Latina hot glamour, fiery curvaceous figure, dramatic hourglass, round full hips, bronzed warm skin, Telenovela star curves, passionate voluptuous Latin editorial",
    "🏋️ 파워리프터 글램 — 강인한 근육 여신": "powerlifter goddess, extremely muscular powerful build, thick strong legs, broad powerful back, strong defined shoulders, raw physical power with feminine editorial energy, strength sport glamour",
    "🩰 짧고 글래머 — 155cm 미만 풍만 미니 글래머": "petite glamour model under 155cm, compact yet dramatically curvaceous figure, full bust and wide hips on tiny frame, miniature hourglass, doll-like proportions with maximum curves",
    "⚖️ 애슬레틱 커브 — 근육+볼륨 완벽 균형": "athletic curvy model, perfect balance of muscle definition and feminine curves, defined abs with round full hips, toned thick thighs, fit hourglass editorial, the best of both worlds physique",'''

ADD_REPLACEMENT = ADD_ANCHOR + NEW_ENTRIES


def apply_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    fix_count = 0
    skip_count = 0

    # ── 수정 적용 ──
    print("[수정 항목]")
    for old, new in FIXES:
        if old in content:
            content = content.replace(old, new, 1)
            label = old[:50].strip()
            print(f"  [OK] {label}...")
            fix_count += 1
        else:
            label = old[:50].strip()
            print(f"  [SKIP] {label}...")
            skip_count += 1

    # ── 추가 적용 ──
    print("\n[추가 항목]")
    if "헬시 내추럴" in content:
        print("  [SKIP] 이미 추가됨")
    elif ADD_ANCHOR in content:
        content = content.replace(ADD_ANCHOR, ADD_REPLACEMENT, 1)
        print(f"  [OK] 8종 추가 완료")
    else:
        print("  [ERROR] 추가 앵커를 찾을 수 없습니다.")
        print(f"  앵커: {ADD_ANCHOR[:60]}...")

    # ── 저장 ──
    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n[DONE] 저장 완료 → {path}")
        print(f"  수정: {fix_count}종 / 스킵: {skip_count}종")
    else:
        print("\n[INFO] 변경사항 없음")


def verify_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    print("\n[VERIFY] 수정 확인:")
    checks = [
        ("razor-thin elongated silhouette", "울트라 슬림"),
        ("0.65 waist-to-hip ratio", "핫 글래머"),
        ("0.55 waist-to-hip ratio", "슈퍼 글래머"),
        ("stage-ready shredded physique", "비키니 컴페티션"),
        ("soft full rounded abdomen", "BBW 글래머"),
        ("maximalist curvy fashion styling, bold confident", "슈퍼 BBW"),
        ("gym-to-runway body", "스포츠 글램"),
        ("defined calf muscles", "발레리나"),
        ("34-24-35 proportions", "VS 앤젤"),
        ("powerfully lifted full round buttocks", "블랙 글래머"),
        ("tiny head-to-body ratio", "K팝 아이돌"),
        ("unapologetically curvaceous", "플러스 글램"),
        ("헬시 내추럴", "신규: 헬시 내추럴"),
        ("J팝 글래머", "신규: J팝 글래머"),
        ("C팝 아이돌", "신규: C팝 아이돌"),
        ("아라비안 글래머", "신규: 아라비안 글래머"),
        ("멕시칸 핫", "신규: 멕시칸 핫"),
        ("파워리프터 글램", "신규: 파워리프터"),
        ("짧고 글래머", "신규: 짧고 글래머"),
        ("애슬레틱 커브", "신규: 애슬레틱 커브"),
    ]

    all_ok = True
    for pattern, label in checks:
        ok = pattern in content
        mark = "✅" if ok else "❌"
        if not ok:
            all_ok = False
        print(f"  {mark} {label}")

    print("\n✅ 전체 검증 통과!" if all_ok else "\n❌ 일부 누락 — 수동 확인 필요")


if __name__ == "__main__":
    print("=" * 60)
    print("MODEL_TYPES 수정 + 추가 패치")
    print(f"대상: {DATA_PATH}")
    print("=" * 60)
    apply_patch(DATA_PATH)
    verify_patch(DATA_PATH)
    print("\n다음 단계:")
    print("  streamlit run dashboard.py 로 체형 목록 확인")
    print("  git add core/data.py")
    print('  git commit -m "feat: MODEL_TYPES 수정 15종 + 신규 8종 추가"')
    print("  git push")
