# ============================================================
# LumineX G5/G6 SSS/SS 티어 패치
# 저장 위치: C:\Dev\LumineX\preset_builders\
# 반드시 patch_g5g6_remove_and_convert.ps1 실행 후 진행
# ============================================================

$DASH = "C:\Dev\LumineX\dashboard.py"
$content = Get-Content $DASH -Raw -Encoding UTF8

Write-Host "=== G5/G6 SSS/SS 티어 패치 ===" -ForegroundColor Cyan

# ============================================================
# SSS_TIER 추가 목록 (G5 SSS 23종 + G6 SSS 29종 + duo_odalisque SSS 1종)
# ============================================================

$SSS_NEW = @(
    # G5 연결형 듀오 SSS 확정
    "duo_aurora_bodypaint",
    "duo_ocean_bodypaint",
    "duo_golden_desert_bodypaint",
    "duo_cyberpunk_bodypaint",
    "duo_jungle_tribal_bodypaint",
    "duo_latex_color_block",
    "duo_latex_storm_opposites",
    "duo_dark_latex_power",
    "duo_flamenco_latex_fusion",
    "duo_smoke_noir",
    "duo_infinity_pool_contrast",
    "duo_pool_bodypaint_micro",
    "duo_wet_glass_divide",
    "duo_bodypaint_vs_latex",
    "duo_fire_and_ice",
    "duo_angel_devil",
    "duo_chrome_future",
    "duo_skeleton_bloom_bodypaint",
    "duo_odalisque_gisaeng_bodypaint",
    # G6 시간/역사 SSS 4종
    "trio_ancient_medieval_modern_bodypaint",
    "trio_stone_bronze_iron_bodypaint",
    "trio_past_present_future_bodypaint",
    "trio_sunrise_sunset_moonrise_bodypaint",
    # G6 원소/자연 SSS 5종
    "trio_fire_water_earth_bodypaint",
    "trio_lightning_ocean_earthquake_bodypaint",
    "trio_sand_ice_magma_bodypaint",
    "trio_sky_earth_underground_bodypaint",
    "trio_fog_rain_snow_bodypaint",
    # G6 색/빛 SSS 5종
    "trio_rgb_trinity_bodypaint",
    "trio_primary_colors_bodypaint",
    "trio_black_white_gray_bodypaint",
    "trio_gold_silver_bronze_bodypaint",
    "trio_infrared_visible_uv_bodypaint",
    # G6 신화/종교 SSS 5종
    "trio_heaven_earth_hell_bodypaint",
    "trio_creator_preserver_destroyer_bodypaint",
    "trio_fate_three_bodypaint",
    "trio_medusa_sphinx_hydra_bodypaint",
    "trio_creation_of_adam_bodypaint",
    # G6 문명/지역 SSS 5종
    "trio_amazon_sahara_arctic_bodypaint",
    "trio_east_west_south_bodypaint",
    "trio_viking_samurai_spartan_bodypaint",
    "trio_nile_amazon_yangtze_bodypaint",
    "trio_rome_babylon_aztec_bodypaint",
    # G6 감정/철학 SSS 5종
    "trio_love_war_peace_bodypaint",
    "trio_fear_anger_joy_bodypaint",
    "trio_order_chaos_void_bodypaint",
    "trio_id_ego_superego_bodypaint",
    "trio_thesis_antithesis_synthesis_bodypaint"
)

# SS_TIER 추가 목록 (SS 확정 1종)
$SS_NEW = @(
    "duo_ink_wash_split_bodypaint"
)

# ============================================================
# SSS_TIER set에 삽입
# 앵커: SSS_TIER = { 블록 내 마지막 항목 뒤에 추가
# ============================================================

Write-Host "  SSS_TIER 항목 추가 중..." -ForegroundColor Yellow

$SSS_INSERT = ($SSS_NEW | ForEach-Object { "    `"$_`"," }) -join "`n"

# SSS_TIER set의 닫는 } 앞에 삽입
# 앵커: "bioluminescent",  (파워&엣지 마지막 확정 항목)
$ANCHOR_SSS = '"bioluminescent",'
if ($content -match [regex]::Escape($ANCHOR_SSS)) {
    $content = $content -replace [regex]::Escape($ANCHOR_SSS), "$ANCHOR_SSS`n$SSS_INSERT"
    Write-Host "  OK SSS_TIER 앵커 적용 완료" -ForegroundColor Green
} else {
    Write-Host "  !! SSS_TIER 앵커 못찾음 — 수동 추가 필요" -ForegroundColor Red
    Write-Host "     추가할 항목 목록:" -ForegroundColor Yellow
    $SSS_NEW | ForEach-Object { Write-Host "     `"$_`"," -ForegroundColor White }
}

# ============================================================
# SS_TIER set에 삽입
# ============================================================

Write-Host "  SS_TIER 항목 추가 중..." -ForegroundColor Yellow

$SS_INSERT = ($SS_NEW | ForEach-Object { "    `"$_`"," }) -join "`n"

# 앵커: SS_TIER 블록 내 기존 마지막 바디페인팅 항목
$ANCHOR_SS = '"duo_rain_neon_soaked",'
if ($content -match [regex]::Escape($ANCHOR_SS)) {
    $content = $content -replace [regex]::Escape($ANCHOR_SS), "$ANCHOR_SS`n$SS_INSERT"
    Write-Host "  OK SS_TIER 앵커 적용 완료" -ForegroundColor Green
} else {
    Write-Host "  !! SS_TIER 앵커 못찾음 — 수동 추가 필요" -ForegroundColor Red
    Write-Host "     추가할 항목: `"duo_ink_wash_split_bodypaint`"," -ForegroundColor Yellow
}

# SSS_TIER에도 SS 항목 포함 (SSS는 SS_TIER에도 포함 원칙)
# SS는 SSS_TIER에 포함하지 않음 — 기존 원칙 유지

$content | Set-Content $DASH -Encoding UTF8

# ============================================================
# 검증
# ============================================================

Write-Host "`n=== 검증 ===" -ForegroundColor Cyan

$CHECK_SSS = @(
    "trio_ancient_medieval_modern_bodypaint",
    "trio_creator_preserver_destroyer_bodypaint",
    "trio_rome_babylon_aztec_bodypaint",
    "trio_order_chaos_void_bodypaint",
    "duo_skeleton_bloom_bodypaint",
    "duo_odalisque_gisaeng_bodypaint"
)

foreach ($item in $CHECK_SSS) {
    $found = Select-String -Path $DASH -Pattern $item -Quiet
    if ($found) {
        Write-Host "  OK SSS 등록: $item" -ForegroundColor Green
    } else {
        Write-Host "  !! 미등록: $item" -ForegroundColor Red
    }
}

$ssFound = Select-String -Path $DASH -Pattern "duo_ink_wash_split_bodypaint" -Quiet
if ($ssFound) {
    Write-Host "  OK SS 등록: duo_ink_wash_split_bodypaint" -ForegroundColor Green
} else {
    Write-Host "  !! SS 미등록: duo_ink_wash_split_bodypaint" -ForegroundColor Red
}

Write-Host "`n=== SSS/SS 패치 완료. 다음: Git 커밋 ===" -ForegroundColor Cyan
Write-Host "  cd C:\Dev\LumineX" -ForegroundColor White
Write-Host "  git add -A" -ForegroundColor White
Write-Host "  git commit -m `"G5/G6 멀티 바디페인팅 검증 완료: 제거 12종, SSS 52종, SS 1종 패치`"" -ForegroundColor White
Write-Host "  git push origin main" -ForegroundColor White
