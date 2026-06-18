"""
LumineX v28 전통문화 바디페인팅 Tier 패치 스크립트 v3
앵커 방식 (str.replace) — 정규식 없음
실행: python preset_builders/patch_v28_tiers.py
"""

from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")

NEW_SSS = [
    "kabuki_bodypaint", "joseon_bodypaint", "tibetan_bodypaint",
    "byzantine_bodypaint", "mayan_bodypaint",
    "geisha_bodypaint", "ming_bodypaint", "thai_bodypaint",
    "ottoman_bodypaint", "flamenco_bodypaint", "sumerian_bodypaint",
    "maori_bodypaint", "balinese_bodypaint", "persian_bodypaint",
    "mughal_bodypaint", "hopi_bodypaint", "haida_bodypaint",
    "polynesian_bodypaint", "korean_shaman_bodypaint",
    "noh_bodypaint", "hanbok_bodypaint", "tang_dynasty_bodypaint",
    "moroccan_bodypaint", "batik_bodypaint", "ikat_bodypaint",
    "dirndl_bodypaint", "ninja_bodypaint", "kebaya_bodypaint",
    "scottish_bodypaint",
    "voodoo_bodypaint", "scythian_bodypaint", "olmec_bodypaint",
    "odalisque_bodypaint", "harem_bodypaint", "shaman_bodypaint",
    "kimono_bodypaint", "samurai_bodypaint", "geisha_white_bodypaint",
    "hanfu_bodypaint", "qipao_bodypaint", "cheongsam_bodypaint",
    "gisaeng_bodypaint", "hanbok_modern_bodypaint",
    "ao_dai_bodypaint", "zulu_bodypaint", "kente_bodypaint",
    "dashiki_bodypaint", "belly_bodypaint",
]

NEW_SS_ONLY = ["sari_bodypaint", "yoruba_bodypaint", "maiko_bodypaint"]
NEW_SS_ALL = NEW_SS_ONLY + NEW_SSS

GROUP_MAP = [
    ("1차 SSS", ["kabuki_bodypaint","joseon_bodypaint","tibetan_bodypaint","byzantine_bodypaint","mayan_bodypaint"]),
    ("2차 SSS", ["geisha_bodypaint","ming_bodypaint","thai_bodypaint","ottoman_bodypaint","flamenco_bodypaint","sumerian_bodypaint"]),
    ("3차 SSS", ["maori_bodypaint","balinese_bodypaint","persian_bodypaint","mughal_bodypaint","hopi_bodypaint","haida_bodypaint"]),
    ("4차 SSS", ["polynesian_bodypaint","korean_shaman_bodypaint","noh_bodypaint","hanbok_bodypaint","tang_dynasty_bodypaint"]),
    ("5차 SSS", ["moroccan_bodypaint","batik_bodypaint","ikat_bodypaint","dirndl_bodypaint","ninja_bodypaint","kebaya_bodypaint","scottish_bodypaint"]),
    ("6차 SSS", ["voodoo_bodypaint","scythian_bodypaint","olmec_bodypaint","odalisque_bodypaint","harem_bodypaint","shaman_bodypaint"]),
    ("7차 SSS", ["kimono_bodypaint","samurai_bodypaint","geisha_white_bodypaint","hanfu_bodypaint","qipao_bodypaint","cheongsam_bodypaint","gisaeng_bodypaint","hanbok_modern_bodypaint"]),
    ("8차 SSS", ["ao_dai_bodypaint","zulu_bodypaint","kente_bodypaint","dashiki_bodypaint","belly_bodypaint"]),
    ("SS 전용",  ["sari_bodypaint","yoruba_bodypaint","maiko_bodypaint"]),
]


def find_set_block(content, set_name):
    """set_name = { 시작 인덱스와 닫는 } 인덱스 반환"""
    start_marker = set_name + " = {"
    start = content.find(start_marker)
    if start == -1:
        return -1, -1
    # 중괄호 짝 맞추기
    depth = 0
    for i, ch in enumerate(content[start:], start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return start, i  # i = 닫는 } 위치
    return start, -1


def get_items_in_block(content, start, end):
    block = content[start:end]
    items = set()
    i = 0
    while i < len(block):
        if block[i] == '"':
            j = block.find('"', i + 1)
            if j != -1:
                items.add(block[i+1:j])
                i = j + 1
                continue
        i += 1
    return items


def build_insert(to_add):
    lines = ["    # v28 전통문화 바디페인팅 패치 (" + str(len(to_add)) + "종)"]
    for gname, items in GROUP_MAP:
        grp = [x for x in items if x in to_add]
        if grp:
            lines.append("    # " + gname)
            for item in grp:
                lines.append('    "' + item + '",')
    return "\n" + "\n".join(lines)


def patch_set(content, set_name, new_items):
    start, end = find_set_block(content, set_name)
    if start == -1 or end == -1:
        print("  [" + set_name + "] 블록을 찾지 못했습니다!")
        return content, 0

    already = get_items_in_block(content, start, end)
    to_add = [x for x in new_items if x not in already]

    if not to_add:
        print("  [" + set_name + "] 추가할 항목 없음")
        return content, 0

    insert = build_insert(to_add)
    # 닫는 } 바로 앞에 삽입
    new_content = content[:end] + insert + "\n" + content[end:]
    print("  [" + set_name + "] " + str(len(to_add)) + "종 추가 완료")
    return new_content, len(to_add)


def main():
    print("=" * 60)
    print("LumineX v28 Tier 패치 v3 (str.replace 방식)")
    print("=" * 60)

    if not DASHBOARD.exists():
        print("파일 없음: " + str(DASHBOARD))
        return

    content = DASHBOARD.read_text(encoding="utf-8")
    DASHBOARD.with_suffix(".py.bak").write_text(content, encoding="utf-8")
    print("백업 완료\n")

    print("SSS_TIER 패치...")
    content, sss_n = patch_set(content, "SSS_TIER", NEW_SSS)

    print("SS_TIER 패치...")
    content, ss_n = patch_set(content, "SS_TIER", NEW_SS_ALL)

    DASHBOARD.write_text(content, encoding="utf-8")
    print("\n저장 완료")

    # 검증
    verify = DASHBOARD.read_text(encoding="utf-8")
    s1, e1 = find_set_block(verify, "SSS_TIER")
    s2, e2 = find_set_block(verify, "SS_TIER")
    sss_items = get_items_in_block(verify, s1, e1)
    ss_items  = get_items_in_block(verify, s2, e2)

    missing_sss = [x for x in NEW_SSS if x not in sss_items]
    missing_ss  = [x for x in NEW_SS_ONLY if x not in ss_items]

    print("\n검증...")
    if missing_sss:
        print("  SSS 누락: " + str(missing_sss))
    else:
        print("  SSS " + str(len(NEW_SSS)) + "종 확인 완료")

    if missing_ss:
        print("  SS 누락: " + str(missing_ss))
    else:
        print("  SS sari/yoruba/maiko 확인 완료")

    print()
    print("PowerShell 검증:")
    print('  Select-String -Path "C:\\Dev\\LumineX\\dashboard.py" -Pattern "kabuki_bodypaint|ao_dai_bodypaint|sari_bodypaint"')
    print()
    print("커밋:")
    print('  git add dashboard.py')
    print('  git commit -m "feat: v28 전통문화 바디페인팅 52종 tier 패치 (SSS 49종+SS 3종)"')
    print("=" * 60)


if __name__ == "__main__":
    main()
