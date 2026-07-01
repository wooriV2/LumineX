# ============================================================
# LumineX G5/G6 제거 패치 + geisha→duo 전환
# 저장 위치: C:\Dev\LumineX\preset_builders\
# 실행: PowerShell (C:\Dev\LumineX\ 에서)
# ============================================================

$BASE = "C:\Dev\LumineX"
$PRESETS = "$BASE\presets"
$DASH = "$BASE\dashboard.py"

# ============================================================
# STEP 1: 제거 대상 JSON 파일 삭제 (총 12종)
# ============================================================

$REMOVE_FILES = @(
    # G5 미생성 4종
    "duo_lightning_rainbow_bodypaint.json",
    "duo_shark_whale_bodypaint.json",
    "duo_sistine_hands_bodypaint.json",
    "duo_map_east_west_bodypaint.json",
    # G5 인체/철학 미생성 1종
    "duo_shadow_light_figure_bodypaint.json",
    # G6 미생성/제거 6종
    "trio_past_present_future_self_bodypaint.json",
    "trio_dawn_noon_dusk_bodypaint.json",
    "trio_earth_water_sky_bodypaint.json",
    "trio_neon_pastel_dark_bodypaint.json",
    "trio_predator_prey_scavenger_bodypaint.json",
    "trio_geisha_odalisque_gisaeng_bodypaint.json"
)

Write-Host "=== STEP 1: JSON 파일 삭제 ===" -ForegroundColor Cyan
foreach ($f in $REMOVE_FILES) {
    $path = "$PRESETS\$f"
    if (Test-Path $path) {
        Remove-Item $path -Force
        Write-Host "  삭제: $f" -ForegroundColor Green
    } else {
        Write-Host "  없음(스킵): $f" -ForegroundColor Yellow
    }
}

# ============================================================
# STEP 2: duo_odalisque_gisaeng JSON 생성
# ============================================================

Write-Host "`n=== STEP 2: duo_odalisque_gisaeng JSON 생성 ===" -ForegroundColor Cyan

$NEW_JSON = @'
{
  "id": "duo_odalisque_gisaeng_bodypaint",
  "label": "오달리스크 & 기생 바디페인팅",
  "category": "멀티 바디페인팅",
  "subcategory": "G5 연결형 듀오",
  "tier": "SSS",
  "outfit": "Body fully painted with: LEFT FIGURE — Ottoman odalisque bodypaint, Iznik blue tilework floral arabesques covering entire body, deep cobalt and turquoise geometric medallions, gold filigree accents, henna-style hand motifs on arms, NO clothing NO fabric; RIGHT FIGURE — Joseon gisaeng bodypaint, magnolia and plum blossom motifs in soft pink and white covering entire body, traditional Korean dancheong color accents, elegant brushwork calligraphy details on legs, NO clothing NO fabric",
  "background": "Split composition: LEFT — Ottoman harem chamber, mosaic tile arches, hanging lanterns, warm amber light; RIGHT — Joseon gisaeng pavilion, cherry blossom garden, moonlit paper screens, silk lanterns",
  "mood": "Elegant cultural contrast, refined aesthetic duality",
  "pose": "Both figures standing facing each other in profile, mirroring pose, barefoot",
  "negative": "NO kimono NO hanbok NO clothing NO fabric on body NO dress",
  "tags": ["duo", "odalisque", "gisaeng", "bodypaint", "cultural", "contrast", "ottoman", "joseon"]
}
'@

$NEW_JSON | Set-Content -Path "$PRESETS\duo_odalisque_gisaeng_bodypaint.json" -Encoding UTF8
Write-Host "  생성: duo_odalisque_gisaeng_bodypaint.json" -ForegroundColor Green

# ============================================================
# STEP 3: dashboard.py — 제거 프리셋을 SSS_TIER / SS_TIER / PRESET_CATEGORIES에서 삭제
# ============================================================

Write-Host "`n=== STEP 3: dashboard.py 수정 ===" -ForegroundColor Cyan

$content = Get-Content $DASH -Raw -Encoding UTF8

# --- SSS_TIER에서 제거 ---
$SSS_REMOVE = @(
    '"duo_lightning_rainbow_bodypaint"',
    '"duo_shark_whale_bodypaint"',
    '"duo_sistine_hands_bodypaint"',
    '"duo_map_east_west_bodypaint"',
    '"duo_shadow_light_figure_bodypaint"',
    '"trio_past_present_future_self_bodypaint"',
    '"trio_dawn_noon_dusk_bodypaint"',
    '"trio_earth_water_sky_bodypaint"',
    '"trio_neon_pastel_dark_bodypaint"',
    '"trio_predator_prey_scavenger_bodypaint"',
    '"trio_geisha_odalisque_gisaeng_bodypaint"'
)

foreach ($item in $SSS_REMOVE) {
    # 쉼표 뒤에 오는 경우
    $content = $content -replace "$item,\s*`n", ""
    # 쉼표 앞에 오는 경우 (마지막 항목)
    $content = $content -replace ",\s*$item", ""
    # 단독 줄
    $content = $content -replace "\s*$item\s*`n", ""
}

# --- PRESET_CATEGORIES의 멀티 바디페인팅 리스트에서도 제거 ---
$CAT_REMOVE = @(
    '"duo_lightning_rainbow_bodypaint"',
    '"duo_shark_whale_bodypaint"',
    '"duo_sistine_hands_bodypaint"',
    '"duo_map_east_west_bodypaint"',
    '"duo_shadow_light_figure_bodypaint"',
    '"trio_past_present_future_self_bodypaint"',
    '"trio_dawn_noon_dusk_bodypaint"',
    '"trio_earth_water_sky_bodypaint"',
    '"trio_neon_pastel_dark_bodypaint"',
    '"trio_predator_prey_scavenger_bodypaint"',
    '"trio_geisha_odalisque_gisaeng_bodypaint"'
)

foreach ($item in $CAT_REMOVE) {
    $content = $content -replace "$item,\s*`n", ""
    $content = $content -replace ",\s*$item", ""
    $content = $content -replace "\s*$item\s*`n", ""
}

# duo_odalisque_gisaeng를 PRESET_CATEGORIES 멀티 바디페인팅에 추가
# (trio_geisha_odalisque_gisaeng 자리를 대체)
$content = $content -replace '("duo_ink_wash_split_bodypaint")', '$1,' + "`n            `"duo_odalisque_gisaeng_bodypaint`""

$content | Set-Content $DASH -Encoding UTF8
Write-Host "  dashboard.py 제거/추가 완료" -ForegroundColor Green

# ============================================================
# STEP 4: 검증
# ============================================================

Write-Host "`n=== STEP 4: 검증 ===" -ForegroundColor Cyan

Write-Host "  [제거 확인] dashboard.py에 삭제 항목 잔존 여부:"
foreach ($item in $SSS_REMOVE) {
    $clean = $item -replace '"', ''
    $found = Select-String -Path $DASH -Pattern $clean -Quiet
    if ($found) {
        Write-Host "  !! 잔존: $clean" -ForegroundColor Red
    } else {
        Write-Host "  OK 제거됨: $clean" -ForegroundColor Green
    }
}

Write-Host "`n  [신규 확인] duo_odalisque_gisaeng:"
$newFound = Select-String -Path $DASH -Pattern "duo_odalisque_gisaeng_bodypaint" -Quiet
if ($newFound) {
    Write-Host "  OK dashboard.py에 등록됨" -ForegroundColor Green
} else {
    Write-Host "  !! dashboard.py 등록 실패 — 수동 추가 필요" -ForegroundColor Red
}

$jsonExists = Test-Path "$PRESETS\duo_odalisque_gisaeng_bodypaint.json"
if ($jsonExists) {
    Write-Host "  OK JSON 파일 존재" -ForegroundColor Green
} else {
    Write-Host "  !! JSON 파일 없음" -ForegroundColor Red
}

Write-Host "`n=== STEP 1~4 완료. 다음: patch_g5g6_sss_tier.ps1 실행 ===" -ForegroundColor Cyan
