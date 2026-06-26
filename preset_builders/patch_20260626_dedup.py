"""
patch_20260626_dedup.py
중복 프리셋 21종 제거 패치

제거 대상:
1. 🌿 자연 & 원소에서 전통의상 19종 제거 (👘 전통 & 문화의상에 정식 소속)
2. 🌿 자연 & 원소에서 monsoon_goddess 제거 (🌋 엘리멘탈 갓데스에 정식 소속)
3. 🍬 팝 & 카와이 내부 kdrama_villain_queen 중복 1개 제거
"""

TARGET = r"C:\Dev\LumineX\dashboard.py"

# ── 자연 & 원소에서 제거할 20종 ──
REMOVE_FROM_NATURE = [
    "ao_dai_sheer", "ao_dai_glamour", "thai_temple", "balinese_goddess",
    "kebaya_java", "harem_goddess", "odalisque", "moroccan_kaftan",
    "kaftan_sheer", "persian_court", "sari_goddess", "saree_draped_sensual",
    "indian_bridal", "belly_dancer", "yoruba_glamour", "dashiki_glam",
    "scottish_corset", "flamenco_dress", "dirndl_glam",
    "monsoon_goddess",
]

# ── str.replace 앵커 방식 ──
# 자연 & 원소 블록에서 전통의상 라인 전체 제거
# dashboard.py에서 해당 블록은 아래 패턴으로 묶여 있음

OLD_NATURE_BLOCK = '''    "ao_dai_sheer",
    "ao_dai_glamour",
    "thai_temple",
    "balinese_goddess",
    "kebaya_java",
    "harem_goddess",
    "odalisque",
    "moroccan_kaftan",
    "kaftan_sheer",
    "persian_court",
    "sari_goddess",
    "saree_draped_sensual",
    "indian_bridal",
    "belly_dancer",
    "yoruba_glamour",
    "dashiki_glam",
    "scottish_corset",
    "flamenco_dress",
    "dirndl_glam",'''

NEW_NATURE_BLOCK = ""  # 전체 제거

# monsoon_goddess — 자연&원소 블록 내 단독 라인
OLD_MONSOON = '    "santorini_lightning",\n        "smoke_veil",'
NEW_MONSOON = '    "santorini_lightning",\n    "smoke_veil",'

# 좀 더 안전한 방식: monsoon_goddess 줄만 제거
OLD_MONSOON2 = '"dirndl_glam","santorini_lightning",'
# → dirndl_glam 제거 후 남은 구조에서 monsoon_goddess 찾기

# kdrama_villain_queen 팝&카와이 내부 중복
# 코드상 두 번 나타남:
#   "kdrama_villain_queen","kdrama_chaebol_heir","kdrama_villain_queen","gangnam_luxury_glam"
OLD_KPOP_DUP = '"kdrama_villain_queen","kdrama_chaebol_heir","kdrama_villain_queen","gangnam_luxury_glam"'
NEW_KPOP_DUP = '"kdrama_villain_queen","kdrama_chaebol_heir","gangnam_luxury_glam"'


def patch():
    with open(TARGET, "r", encoding="utf-8") as f:
        src = f.read()

    original_len = len(src)
    changes = 0

    # ── 1. 자연 & 원소 블록에서 전통의상 19종 제거 ──
    # 블록이 어떤 형태로 있는지 확인 후 제거
    # 실제 코드에서 해당 라인들을 줄 단위로 제거
    lines = src.split('\n')
    new_lines = []
    
    # 자연 & 원소 카테고리 블록 범위 감지
    in_nature_block = False
    nature_block_started = False
    
    # 제거할 라인들 (자연&원소 블록 내에서만)
    remove_keys = set(REMOVE_FROM_NATURE)
    
    i = 0
    nature_start_idx = None
    nature_end_idx = None
    
    # 자연 & 원소 블록 찾기
    for idx, line in enumerate(lines):
        if '"🌿 자연 & 원소"' in line or "'🌿 자연 & 원소'" in line:
            nature_start_idx = idx
        if nature_start_idx and idx > nature_start_idx:
            # 다음 카테고리 시작 감지
            if ('"🌃' in line or "'🌃'" in line) and idx > nature_start_idx + 5:
                nature_end_idx = idx
                break
    
    if nature_start_idx and nature_end_idx:
        print(f"✅ 자연&원소 블록 감지: line {nature_start_idx}~{nature_end_idx}")
        
        # 해당 블록에서 remove_keys 포함 라인 제거
        result_lines = []
        for idx, line in enumerate(lines):
            if nature_start_idx < idx < nature_end_idx:
                # 이 라인에 제거 대상 key가 있는지 확인
                should_remove = False
                for key in remove_keys:
                    if f'"{key}"' in line:
                        should_remove = True
                        print(f"  제거: line {idx}: {line.strip()}")
                        changes += 1
                        break
                if not should_remove:
                    result_lines.append(line)
            else:
                result_lines.append(line)
        
        lines = result_lines
    else:
        print("⚠️ 자연&원소 블록 자동 감지 실패 → 전체 라인 스캔으로 대체")
        # 폴백: 전체에서 자연&원소 특유 라인들만 제거
        # (전통&문화의상에도 있으므로 첫 번째 occurrence만 제거)
        result_lines = []
        removed_keys = set()
        
        # 자연&원소 블록 범위를 다시 찾기
        in_nature = False
        nature_done = False
        
        for idx, line in enumerate(lines):
            if '🌿 자연' in line:
                in_nature = True
            elif in_nature and ('🌃 도시' in line or '🎬 에디토리얼' in line):
                in_nature = False
                nature_done = True
            
            if in_nature and not nature_done:
                should_remove = False
                for key in remove_keys:
                    if f'"{key}"' in line and key not in removed_keys:
                        should_remove = True
                        removed_keys.add(key)
                        print(f"  제거(폴백): {key}")
                        changes += 1
                        break
                if not should_remove:
                    result_lines.append(line)
            else:
                result_lines.append(line)
        
        lines = result_lines

    src = '\n'.join(lines)

    # ── 2. 팝&카와이 kdrama_villain_queen 내부 중복 제거 ──
    # 실제 코드 패턴 확인 후 제거
    # "kdrama_villain_queen","kdrama_chaebol_heir","kdrama_villain_queen","gangnam_luxury_glam"
    # → 공백 포함 다양한 패턴 대응

    import re
    
    # 팝&카와이 블록에서 kdrama_villain_queen 두 번째 occurrence 제거
    kpop_pattern = r'("kdrama_villain_queen",\s*"kdrama_chaebol_heir",\s*)"kdrama_villain_queen",\s*("gangnam_luxury_glam")'
    kpop_replacement = r'\1\2'
    
    new_src, n_sub = re.subn(kpop_pattern, kpop_replacement, src)
    if n_sub > 0:
        src = new_src
        print(f"✅ kdrama_villain_queen 중복 제거: {n_sub}건")
        changes += n_sub
    else:
        # 다른 패턴 시도
        old_dup = '"kdrama_villain_queen","kdrama_chaebol_heir","kdrama_villain_queen","gangnam_luxury_glam"'
        new_dup = '"kdrama_villain_queen","kdrama_chaebol_heir","gangnam_luxury_glam"'
        if old_dup in src:
            src = src.replace(old_dup, new_dup, 1)
            print("✅ kdrama_villain_queen 중복 제거 (exact match)")
            changes += 1
        else:
            print("⚠️ kdrama_villain_queen 중복 패턴 미발견 — 수동 확인 필요")

    # ── 저장 ──
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(src)

    print(f"\n📝 저장 완료: {TARGET}")
    print(f"   총 변경: {changes}건")
    print(f"   파일 크기: {original_len} → {len(src)} bytes (Δ{len(src)-original_len:+d})")


if __name__ == "__main__":
    patch()
