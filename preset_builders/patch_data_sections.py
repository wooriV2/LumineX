"""
LumineX core/data.py 5개 섹션 보완 패치
1. SPECIAL_EFFECTS — 6종 추가 (10→16)
2. PROPS — 7종 추가 (11→18)
3. MAKEUP — 5종 추가 (13→18)
4. ENVIRONMENTS — 5종 추가
5. COLOR_GRADES — 4종 추가 (11→15)

대상: C:\Dev\LumineX\core\data.py
방식: str.replace 앵커
"""

DATA_PATH = r"C:\Dev\LumineX\core\data.py"

PATCHES = [

    # ══════════════════════════════════════════════════════
    # 1. SPECIAL_EFFECTS — 마지막 항목 뒤에 추가
    # ══════════════════════════════════════════════════════
    (
        '"시간 정지 — 주변만 멈춘": "time freeze effect, everything frozen mid-motion around model, only subject in motion, surreal editorial",',
        '"시간 정지 — 주변만 멈춘": "time freeze effect, everything frozen mid-motion around model, only subject in motion, surreal editorial",\n'
        '    "홀로그램 — 홀로그램 프로젝션": "holographic projection effects, iridescent light grid patterns, translucent hologram layers surrounding model, sci-fi editorial",\n'
        '    "매트릭스 코드 — 디지털 레인": "matrix digital rain effect, green cascading code falling around model, cyberpunk digital reality, dark editorial",\n'
        '    "버블 — 비누방울 가득": "soap bubble cloud surrounding model, hundreds of floating iridescent bubbles, rainbow reflections in each bubble, whimsical editorial",\n'
        '    "크리스탈 성장 — 몸에서 크리스탈 자라는": "crystals growing from body and surroundings, gemstone formations erupting, magical mineral growth effect, fantasy editorial",\n'
        '    "중력 역전 — 물체가 위로": "gravity reversal effect, objects and fabric floating upward, everything defying gravity around model, surreal editorial",\n'
        '    "오로라 커튼 — 오로라 빛이 드리워지는": "aurora borealis curtain of light surrounding model, ethereal northern lights ribbons, magical atmospheric glow, mystical editorial",',
    ),

    # ══════════════════════════════════════════════════════
    # 2. PROPS — 마지막 항목 뒤에 추가
    # ══════════════════════════════════════════════════════
    (
        '"테니스 라켓 — 테니스 포즈": "holding tennis racket, tennis court editorial, athletic chic",',
        '"테니스 라켓 — 테니스 포즈": "holding tennis racket, tennis court editorial, athletic chic",\n'
        '    "악기 — 바이올린/첼로/기타": "holding elegant musical instrument violin cello or guitar, artistic musician glamour",\n'
        '    "책 — 다크아카데미아 분위기": "holding vintage leather-bound book, dark academia aesthetic, intellectual glamour editorial",\n'
        '    "와인잔 — 레드와인 럭셔리": "holding crystal wine glass with red wine, luxury lifestyle editorial, sophisticated glamour",\n'
        '    "향수병 — 뷰티 캠페인": "holding luxury perfume bottle, beauty campaign editorial, fragrance advertisement style",\n'
        '    "마스크 — 베네치아 가면": "holding ornate Venetian masquerade mask, mysterious glamour, masquerade ball editorial",\n'
        '    "폰/셀피 — 거울 셀피 컨셉": "holding smartphone taking mirror selfie, social media glamour, modern editorial",\n'
        '    "우산 파라솔 — 레이스 파라솔": "holding delicate lace parasol, vintage elegance, sun-dappled romantic editorial",',
    ),

    # ══════════════════════════════════════════════════════
    # 3. MAKEUP — 마지막 항목 뒤에 추가
    # ══════════════════════════════════════════════════════
    (
        '"홀로그램 — 아방가르드 미래적": "holographic makeup, iridescent highlights, avant-garde editorial",',
        '"홀로그램 — 아방가르드 미래적": "holographic makeup, iridescent highlights, avant-garde editorial",\n'
        '    "글래스 스킨 — K뷰티 유리 피부": "glass skin K-beauty makeup, ultra-luminous transparent skin, mirror-like dewy finish, Seoul beauty standard",\n'
        '    "블러드 립 — 다크 고딕 레드": "blood red dark lip makeup, deep crimson burgundy lips, gothic glamour, vampire editorial",\n'
        '    "브론저 글로우 — 태닝+브론저": "bronzer glow makeup, sun-kissed bronzed skin, warm contoured glow, beach goddess editorial",\n'
        '    "화이트 아이 — 아방가르드 흰 눈": "white eye makeup, avant-garde white eyeshadow, dramatic editorial, fashion week bold look",\n'
        '    "노 메이크업 글로우 — 완벽한 피부만": "no-makeup glow, skin-only perfection, flawless bare skin with inner luminosity, natural beauty editorial",',
    ),

    # ══════════════════════════════════════════════════════
    # 4. ENVIRONMENTS — 마지막 항목 뒤에 추가
    # ══════════════════════════════════════════════════════
    (
        '"테니스 코트 — 클래식 테니스 클럽": "tennis court, classic tennis club, athletic glamour editorial",',
        '"테니스 코트 — 클래식 테니스 클럽": "tennis court, classic tennis club, athletic glamour editorial",\n'
        '    "라스베가스 스트립 — 카지노 야경": "Las Vegas Strip at night, neon casino signs, gambling capital glamour, electric night editorial",\n'
        '    "홍콩 구룡 네온 — 홍콩 야경": "Hong Kong Kowloon neon streets at night, dense neon signs, cyberpunk Asian city editorial",\n'
        '    "이비자 클럽 비치 — 지중해 파티": "Ibiza beach club, Mediterranean party scene, DJ booth, luxury summer nightlife editorial",\n'
        '    "부다페스트 야경 — 세체니 다리": "Budapest Chain Bridge at night, Danube River reflection, illuminated castle, Eastern European glamour",\n'
        '    "런던 빅벤 — 클래식 영국 야경": "London Big Ben and Westminster Bridge at night, iconic British landmark, classic European editorial",',
    ),

    # ══════════════════════════════════════════════════════
    # 5. COLOR_GRADES — 마지막 항목 뒤에 추가
    # ══════════════════════════════════════════════════════
    (
        '"세피아 — 따뜻한 앤티크": "sepia tone, warm antique finish, nostalgic editorial",',
        '"세피아 — 따뜻한 앤티크": "sepia tone, warm antique finish, nostalgic editorial",\n'
        '    "네온 팝 — 형광색 과포화": "neon pop color grade, hyper-saturated fluorescent colors, maximum vibrancy, editorial pop art",\n'
        '    "듀오톤 — 두 가지 색 그라데이션": "duotone color grade, two-color gradient wash, graphic design aesthetic, bold editorial",\n'
        '    "오렌지 팝 — 필름 오렌지 레트로": "orange pop color grade, warm film orange tones, retro photography feel, analog editorial",\n'
        '    "그린 매트릭스 — 녹색 디지털 무드": "green matrix color grade, deep cool green tones, digital dystopia mood, cyberpunk editorial",',
    ),
]


def apply_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    success = 0
    failed = []

    for old, new in PATCHES:
        if old in content:
            content = content.replace(old, new, 1)
            success += 1
        else:
            # 앵커 일부만 확인
            anchor_preview = old[:40]
            failed.append(anchor_preview)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] {success}개 섹션 패치 완료")
        if failed:
            print(f"[WARN] {len(failed)}개 앵커 미발견:")
            for f_ in failed:
                print(f"  - {f_}...")
    else:
        print("[INFO] 변경사항 없음")
        for f_ in failed:
            print(f"  앵커 미발견: {f_}...")


def verify_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        # SPECIAL_EFFECTS
        ("홀로그램 — 홀로그램 프로젝션", "SPECIAL_EFFECTS: 홀로그램"),
        ("매트릭스 코드", "SPECIAL_EFFECTS: 매트릭스"),
        ("버블 — 비누방울", "SPECIAL_EFFECTS: 버블"),
        ("크리스탈 성장", "SPECIAL_EFFECTS: 크리스탈"),
        ("중력 역전", "SPECIAL_EFFECTS: 중력역전"),
        ("오로라 커튼", "SPECIAL_EFFECTS: 오로라커튼"),
        # PROPS
        ("악기 — 바이올린", "PROPS: 악기"),
        ("책 — 다크아카데미아", "PROPS: 책"),
        ("와인잔", "PROPS: 와인잔"),
        ("향수병", "PROPS: 향수병"),
        ("마스크 — 베네치아", "PROPS: 마스크"),
        ("폰/셀피", "PROPS: 폰"),
        ("우산 파라솔", "PROPS: 파라솔"),
        # MAKEUP
        ("글래스 스킨", "MAKEUP: 글래스스킨"),
        ("블러드 립", "MAKEUP: 블러드립"),
        ("브론저 글로우", "MAKEUP: 브론저"),
        ("화이트 아이", "MAKEUP: 화이트아이"),
        ("노 메이크업 글로우", "MAKEUP: 노메이크업"),
        # ENVIRONMENTS
        ("라스베가스 스트립", "ENV: 라스베가스"),
        ("홍콩 구룡 네온", "ENV: 홍콩"),
        ("이비자 클럽", "ENV: 이비자"),
        ("부다페스트 야경", "ENV: 부다페스트"),
        ("런던 빅벤", "ENV: 런던"),
        # COLOR_GRADES
        ("네온 팝 — 형광색", "COLOR: 네온팝"),
        ("듀오톤", "COLOR: 듀오톤"),
        ("오렌지 팝", "COLOR: 오렌지팝"),
        ("그린 매트릭스", "COLOR: 그린매트릭스"),
    ]

    print("\n[VERIFY]")
    all_ok = True
    for pattern, label in checks:
        ok = pattern in content
        mark = "✅" if ok else "❌"
        if not ok:
            all_ok = False
        print(f"  {mark} {label}")

    print(f"\n✅ 전체 검증 통과! (27종)" if all_ok else "\n❌ 일부 누락")


if __name__ == "__main__":
    print("=" * 60)
    print("core/data.py 5개 섹션 보완 패치")
    print("  SPECIAL_EFFECTS +6 / PROPS +7 / MAKEUP +5")
    print("  ENVIRONMENTS +5 / COLOR_GRADES +4")
    print("=" * 60)
    apply_patch(DATA_PATH)
    verify_patch(DATA_PATH)
    print("\n다음 단계:")
    print("  git add core/data.py")
    print('  git commit -m "feat: data.py 5개 섹션 보완 (SPECIAL_EFFECTS/PROPS/MAKEUP/ENV/COLOR +27종)"')
    print("  git push")
