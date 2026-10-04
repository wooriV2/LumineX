# LumineX · Living Artifact — 인수인계 메모 v6.10 (2026-10-04)

> **v6.10 수정 사항**: 27장 신규 — 다중·복합 바디페인팅의 경계 설계. 등록된 3·4혼합 전원에게 같은 "diagonally" 문구가 들어가 대각선으로 쏠린 원인 확인, 재질 쪽 '다중재질 모양(SH)' 목록 정리(바디페인팅에는 미검증), 기하학 문구 + 희미한 경계 방식의 검증 결과(솔로 30개·확인 10장·듀오/트리오 12개), **Craft Blend 3·4혼합 180개를 새 방식으로 교체 등록(commit `b990556`)**. 합계(6,310)는 덮어쓰기라 변함없음.

> **v6.9 수정 사항**: 26장에 26-7~26-10 보완 — 석재·목재 조합 규칙(석재+목재만의 조합 금지, 검증 결과표), 블렌드 540개 등록(Material Blend 270 + Craft Blend 270, commit `c857eed`)과 검증 때와 달라진 점 2가지, **기존 등록분 점검 결과 2건(미수정)**: 메이크업 설명 속 머리 묘사와 헤어 축 충돌(등록분 약 85%), 중복 색상어("VIVID VIVID" 등). **23장 등록 합계 정정**: v6.7·v6.8의 "약 6,181"은 합산 오류였고, 등록 로그 기준 현재 총합은 6,310개.

> **v6.8 수정 사항**: 26장 신규 추가 — 재질·바디페인팅 분할·혼합 체계. 비늘 동물 간 분할(가로/좌우/4분면 전부 성공, 공작 포함 6종으로 복귀 검토), 재질 간(크리스탈·보태니컬·이레즈미·UV네온·스테인드글라스·금박·흑요암금·왁스·목재·석재) 분할·경계흐림·전신마블링·3재질자유형 전부 성공(목재·석재 전신 첫 성공, 과거 "석재 미해결" 백로그 해소), 전체 축 2/3/4개×솔로/듀오/트리오 매트릭스 89% 성공, 바디페인팅 추상 기하학(동심원·몬드리안·스파이럴·허니콤) 전부 실패 vs 실존 전통 공예명 조합 94% 성공(북엔드 구조 필수 확인) — 핵심 결론: 재질은 분할방식 불문 관대, 바디페인팅은 "전통 공예명 앵커"가 있어야 안정적.

> **v6.7 수정 사항**: 메모리에 있던 v6.5 이후 전체 내용을 16~25장으로 신규 추가 — 바디페인팅 Core Formula 전체 축(16장), 임산부 융합형 트랙(17장), 맥시멀리스트 5종 원문 공식 전체(18장: 이레즈미·UV네온·스테인드글라스·금박·보태니컬), 다트랙 혼합 체계(19장), 버그 수정 이력(20장), 피어싱·쥬얼리 최신 10단계 체계(21장), 보류·폐기 재질 전체 목록(22장), 등록 현황 전체 요약(23장), 헤어 무난한10종(24장), 다음 할 일 종합(25장). 이제 이 파일 하나가 메모리와 동등한 상세도를 가짐 — 앞으로 메모리엔 요약+이 파일 참조만, 상세는 이 파일에 기록.

> **v6.6 수정 사항**: 재질 트랙 15장 신규 추가(약 10일 공백 후 재개, 1~14장은 변경 없음) — 크리스탈(얼음/서리+지오드 통합, 10색), 비늘(Scale, 동물타입 5종 통합, 코드 등록), 흑요암+금(고정 1종), 왁스(3색), 수조 색상 그라데이션 2~4색·무지개 재검증, 듀얼바디 비대칭 다리 첫 테스트(결과 미확인), 프레임 체계 용어 혼선 기록(10-5장과 별개 체계로 추정), 금박·스테인드글라스 자유축 이동 시도 후 폐기, 헤어스타일 31종·헤어컬러 30종 신규 공용 축. 등록 현황 갱신(15-10장 참조).

> **v6.5 수정 사항**: 실사 극단 부피 결론 추가(13-11장) — 1,500과 5,000이 실사에서 체감 차이 없음, 비교 문구 과다 사용 시 역효과(오히려 날씬해짐) 확인. Idol Duo/Solo 174개는 재등록하지 않기로 결정(기존 그대로 유지, 앞으로 만드는 것만 새 규칙 적용). Mountain Mass의 5,000lb 규칙은 Idol Duo/Solo에 통합하지 않기로 결정(별도 카테고리로 유지)

> **v6.4 수정 사항**: 극단 부피 5,000파운드 전면 재확정(13장) — 띠 표현 전면 폐지(원본 짧은 Body Art 형식으로 회귀), 허리 처방, 어깨 처방, 동사 선택 규칙(흐름 동사 금지), 무릎 꿇기 자세 고정 문구, 5,000파운드 듀오 규칙(비교 대상 실험 포함, 팔 프레임 아웃 자동), Idol Duo 50 + Idol Solo 124 등록 및 알려진 띠 표현 잔존 이슈

> **v6.3 수정 사항**: 혼합 출력 전면 확장(14-3장) — 분할 구조 2~5단(3분할이 실사용 상한), 목 경계 구조, 실사 파편 표현, 재질 확장(나무·유리·금속, 실패작 밀랍·산호), 길이 상한(650단어) 확인, 애니+조각 조합, 얼굴 미인 서술, 인종별 이목구비

> **v6.2 수정 사항**: 혼합 출력 확정(14-3장) — 프롬프트 표준 구조 9단계, 흰 계열 재질 권장, 자세 적합도, 얼굴 경계 처리, 경계를 허벅지에서 끝내기

> **v6.1 수정 사항**: 극단 부피(13장) — 무게 5,000파운드까지 확장, 연속형 문양, Body Art 위치 규칙, 비율 기준점, 눕기 체형 적합도. 인물 설정 확장(14장) — 실버폭스 연령, 아이돌 얼굴·헤어, 혼합 출력

> **v6.0 수정 사항**: 조각 재질 13종 확정(얼음 추가), Sculpture 솔로·듀오 프롬프트 84개 작성, 짧은 한국어 지시 원칙(7-7장), 시간 축·겹침 정리

> **v5.9 수정 사항**: 출력 장르 축 신설(12장) — 조각상 계열 확립과 재질 18종, 반투명 재질의 역광 규칙, 회화 장르, 3D 불채택, 임산부 정면 불채택

> **v5.8 수정 사항**: 임산부 변형 추가(11장), 애니 듀오 신규 6체형 확장 방향, 문양 축 불채택

> **v5.7 수정 사항**: 등록 완료 반영(총 1,131개), 녹청 구리 채택과 문양 밀도 규칙(9장), 문양 교체 방식·오일 광택·피어싱과 장신구·부위별 프레임(10장), 한국어 수정 방식 확장(7-7장), 불채택 목록 갱신

> **v5.6 수정 사항**: 실사 듀오 규칙·자세 8종(8장), 압축 템플릿, 재질 불채택 2종 추가, Photo Duo 168개 작성

> **v5.5 수정 사항**: 실사 자세 11종 확정(7-4장), 이미지 첨부 후 한국어 수정 요청 방식(7-7장), Photo Direct 252개로 재작성

> **v5.4 수정 사항**: 실사 직접 생성 템플릿 확립(7장), 자세 규칙·불채택 목록, 질감 문구 중/강, 복부 표현 절충안, 인종·연령 규칙

> **v5.3 수정 사항**: 신규 체형 6종 확정(3-4장), 부위별 자세 규칙·스케일 비례 문장(2-2장), 가슴 강조 계열 규칙과 생성 거부 조건(2-6장), 조각상 변환(5-5장), 프리셋 등록 현황 갱신

> **v5.2 수정 사항**: 체형 결과표를 **애니/실사 두 열로 분리**(3-1장), 머슬 USSBBW·스모·톱헤비 애플 결과 반영, 머슬 USSBBW·스모 체형 블록 추가, 세로 방향 문장 앞뒤 반복, 실사 변환 보정 문장 추가(근육 유지·밝은 재질·소품 유지·금속 선 사진감), 임신 배 주의

> **v5.1 수정 사항**: USSBBW 배 묘사 교체(`apron` 삭제, 살 질감 버전), 배 길이 상한 = 허벅지 중간 확정, 정면/3/4 자세 용도 구분, 극단 체형 후보 목록(3-3장) 추가

> v4 메모(실사 텍스트 프리셋 규칙·체형 블록·등록 절차)의 **후속**. v4 내용은 그대로 유효하고, 이 문서는 오늘 추가된 **애니 스타일 테스트 결과**와 **애니 → 실사 4단계 파이프라인**을 정리한 것.
> 새 창 첨부: ① 이 파일 ② v4 상세 메모 ③ (스크립트 작업 시) patch 스크립트

---

## 0. 한눈에 보기

- **핵심 발견**: 극단 체형은 텍스트로 실사를 직접 뽑으면 실사 모델이 현실 체형으로 되돌린다 → **애니로 형태를 설계하고, 그 이미지를 첨부해 실사로 변환**하면 극단 체형이 그대로 유지됨
- **확정 파이프라인**: 애니 생성 → 실사 변환 → 상체 채우기 → 하체 채우기 (4단계, 5장)
- **검증 범위**: 확정 5개 체형 전부 애니 → 실사 변환 성공. 아워글래스 SSBBW는 4단계 끝까지 완주 (등록 가능 수준)
- **인종**: 흑인(가장 어두운 피부) 고정 유지. 다양화는 추후 과제
- **실사 텍스트 직접 생성(극단 체형)**: 보류. 3D 애니 렌더: 보류 (실제로 3D가 안 나옴)
- **v4 등록 대기 105개(Signature Solo 55 + Duo 50)**: **등록 완료** (총 455개)
- **프리셋 등록 현황 (v5.7 · 전부 등록 완료, commit `0fec4d3`)**

| 카테고리 | 개수 | 비고 |
|---|---|---|
| 🏺 Living Artifact · Anime Blueprint | 215 | 01~70 기존 + 71~95 강화판 + 96~215 신규 6체형 |
| 🏺 Living Artifact · Anime Duo | 50 | |
| 🏺 Living Artifact · Photo Convert | 16 | 변환·채우기 명령어 |
| 🏺 Living Artifact · **Photo Direct** | 252 | 실사 직접 생성 (7체형 × 36) |
| 🏺 Living Artifact · **Photo Duo** | 168 | 실사 2인 (21쌍 × 8자세) |
| 기타 기존 카테고리 | 430 | Signature Solo/Duo, Colossal, DeepBlack Ink 등 |
| **합계** | **1,131** | |

---

## 1. 4단계 파이프라인

| 단계 | 담당 | 도구 |
|---|---|---|
| 1. 애니 생성 | 체형, 3/4 자세, 문양 설계, 얼굴 톤 | 2장 애니 프롬프트 |
| 2. 실사 변환 | 질감, 피부 톤 통일, 살아 있는 얼굴 | 5-1 변환 문구 + 애니 이미지 첨부 |
| 3. 상체 채우기 | 가슴·가슴 사이·가슴 위쪽·팔 커버리지 | 5-2 명령어 + 실사 이미지 첨부 |
| 4. 하체 채우기 | 허벅지 안쪽·무릎·종아리 커버리지 | 5-3 명령어 + 3단계 결과 첨부 |

**운영 원칙**
1. **형태는 애니 단계에서 완성**: 실사는 애니의 체형·문양 배치를 그대로 옮긴다. 애니의 **빈 곳과 얼굴 톤도 그대로 옮겨진다**
2. **실사 문구는 짧게**: 체형을 텍스트로 다시 설명하지 않는다. 길어질수록 현실 체형으로 되돌아감
3. **"더 크게"는 필수**: 실사 변환의 축소 경향을 상쇄
4. **"첨부 애니와 동일한 패턴으로"**: 문양 배치를 고정하는 핵심 문장. 단, 애니의 공백까지 고정됨 → 3·4단계로 해결
5. **"조각품"은 문자 그대로 적용됨**: 실사 변환에서 쓰면 얼굴까지 상감된 조각상이 됨. 사람을 원하면 "옻칠 같은 광택"처럼 질감만 지정
6. **채우기는 상체 → 하체 순서로 2회**: 한 번에 전신을 지시하면 언급한 부위에만 집중함 (가슴을 강조하면 하체가, 생략하면 가슴이 빔)
7. **가슴 커버리지는 필수 항목**: 가슴 부위가 비면 신체 디테일이 드러나 **등록 불가 + 생성 거부**로 직결. 실사 변환 단계에서는 원본 신체 구조를 보존하려 하므로 3단계 명령어로 해결
8. **보정은 한 줄씩 추가**: 무엇이 결과를 바꿨는지 추적 가능하게

---

## 2. 애니 프롬프트 규칙

### 2-1. 공통 줄

**Style (2D만 사용)**
```
Style: A high-quality Japanese anime key visual illustration, clean cel shading, crisp confident line art, vibrant saturated colors, polished professional anime art — not a photograph.
```
- 3D 줄(`stylized 3D anime render ... bold outlines`)은 실제로 3D가 나오지 않음 → 사용 안 함

**피부 (애니 표준)**
```
Deep near-black skin tone, THE ABSOLUTE DARKEST BLACK SKIN ON EARTH, void complexion, not brown, not blue, not lightened, her face exactly as dark as her body.
```
- `blue-black`은 애니에서 남색으로 쏠림 → `near-black` + `not blue`로 교체
- `her face exactly as dark as her body`: 얼굴이 밝으면 실사에서도 얼굴만 밝게 나옴 (매스 몬스터에서 확인)
- 헤비 머슬은 갈색 쏠림이 있어 `cool void complexion, no warm brown tint` 추가

**인물**: `ONE mature adult Black woman in her [나이] with clearly adult facial features` 필수 유지

**신발 (인치 수치는 무시됨 → 신체 기준점으로)**
```
Extreme [색] platform stiletto mules, the platform soles as tall as her ankle bones, the ultra-thin stiletto heels so high her insteps stand nearly vertical.
```

**세로 방향 (v5.2: 앞뒤 반복 필수)** — 끝줄 한 줄만으로는 약함
- 맨 앞: `Image format: a vertical portrait-orientation illustration, 2:3 aspect ratio, taller than it is wide.`
- 맨 끝: `Vertical 2:3 portrait-orientation full-body illustration, taller than it is wide.`

### 2-2. 3/4 자세 (극단 체형 표준)

```
Pose: Standing in a three-quarter view, her body turned about 45 degrees with the front of her body still mostly facing the camera, her face toward the camera, [회전 시 보일 부위], feet planted apart, arms relaxed away from the body, full body head to toe.
```
- **회전 시 보일 부위를 반드시 명시**해야 부피가 커짐 (명시 안 한 콘트라포스토에서는 부피가 줄었음)
- `the front of her body still mostly facing the camera`: 없으면 뒤돌아선 각도로 나옴 (페어에서 확인)
- 체형 블록 끝에 `Her body fills the full width of the frame even in the turned pose.` → 부피 과장에 효과 확인

### 2-2-1. 부위별 자세 규칙 (v5.3)

| 강조할 부위 | 자세 | 이유 |
|---|---|---|
| 배 롤 구조·길이 | 정면 | 층층이 쌓인 롤이 정면으로 드러남 |
| **가슴** | **3/4** | 앞으로 나온 깊이가 옆 윤곽으로 보임. 정면은 폭·길이로만 과장 가능해 상한이 낮음 |
| 히프·측면 부피 | 3/4 | 뒤로 돌출된 곡선이 보임 |
| 근육 | 정면 | 좌우 대칭과 근육 분리선이 보임 |
| 어깨·등 너비 | 정면 | 좌우로 펼쳐질 때 가장 넓어 보임 |
| 단단한 돔형 배(스모) | 정면 | 폭과 앞 돌출이 함께 보임 |

### 2-2-2. 스케일 비례 문장 (v5.3)
부피·키를 키울 때 효과가 확인된 신체 기준점 비교. 체형 블록 끝에 붙임.
```
Her head looks small on top of her massive body, her shoulders span more than four head-widths, each hand is as wide as a normal woman's torso and each thigh thicker than a normal woman's waist.
```
- 어깨 강조 체형은 `more than five head-widths`
- 머리 기준 문구를 2개 이상 겹치면 **몸이 커지는 대신 머리가 작아지는** 쪽으로 갈 수 있음 → 하나만 남기고 관찰

### 2-3. 문양·커버리지

- **롤·곡면마다 재질별 윤곽선**: `a [재질] band along every belly roll` / `bands curving around every roll, fold and curve like contour lines` → 재질 상관없이 부피 강조 효과 (9개 재질에서 확인)
- **밀도와 부피는 상충**: `MAXIMUM DENSITY`를 쓰면 체형이 줄어듦. "Densely filled" 수준 유지, 체형 블록이 재질 섹션보다 길어야 함 (v4 규칙 2 재확인)
- **커버리지 문장 (애니 단계)**
```
The pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly and the calves, covering them as densely as the chest.
```
- 3/4 자세에서 반복적으로 비는 곳: **가슴, 히프 뒤쪽, 아랫배, 무릎 아래**
- 떠 있는 문양 재질(라이롯남, 팔레흐, 나전)은 `[문양] filling the space between every band` 필수
- 목 경계: `from the collarbones to the ankles` (목에 옷깃 선이 생기지 않게)

### 2-4. 부정문 주의 (v4 규칙 7 재확인)
- `no framed medallions`라고 썼더니 메달리온이 더 뚜렷해짐 → 피하고 싶은 개념은 언급하지 않고 긍정문으로 대체
- 옷 관련 단어(bodysuit, suit, leotard 등) 금지
- **`apron` 금지**: `apron belly`가 배를 길게 늘일 때 앞치마·천 자락처럼 그려짐. 배가 짧을 땐 안 드러나다가 길어지면서 드러난 문제

### 2-5. 기타 확인 사항
- **배 길이 상한 = 허벅지 중간** (확정)
  - 텍스트: `past her knees`, `resting on the tops of her knees` 등 모두 허벅지 중간에서 멈춤
  - 롤을 여러 겹 쌓으면 무릎 근처까지 내려가지만 **얇은 평행 주름 = 천 드레이프**처럼 보임
  - `only her knees and lower legs visible below it`처럼 가려지는 부분으로 설명하면 길이는 늘지만, 3/4에서는 다리가 가늘어짐
  - 편집으로 늘리기: 가능은 하지만 허벅지가 배에 흡수되어 풍선 형태가 되거나, 끝이 뾰족한 천 자락이 됨
  - → 무릎까지 늘리는 시도는 텍스트·편집 모두 **불채택**. 자연스러움은 허벅지 중간이 최선
- 이레즈미는 **무네와리(가슴 중앙 비우기)** 관례를 따라 중앙에 검은 띠가 생김. `sōshinbori ... no munewari opening`을 넣으면 레오타드처럼 막힘 → 애니·실사 모두 이레즈미 보류
- 신체 노출 방지: `Her whole body reads as a smooth glazed sculpture, like a porcelain figurine` (애니에서만 사용)

---

### 2-6. 가슴 강조 계열 규칙 (v5.3)
- **노출 강조 문구 금지**: `never covering the bust`, `the full width of the bust visible` 등은 생성 거부를 유발
- **부위 직접 지칭 주의**: `each breast larger than her own head`보다 `each rounded half as tall as her own head` 쪽이 안전
- **가슴이 별개 물체처럼 보이는 것 방지**: `The bust merges smoothly into her chest and shoulders as one continuous body, no gap, no seam.`
- **조각품 문장·메달리온은 가슴에 쓰지 말 것**: 노출 방지에는 효과적이지만 가슴을 평평한 장식면으로 만들어 부피를 죽임
- **생성 거부 조건**: 몸 전체에서 가슴이 차지하는 비중이 클수록 거부. 슬림 + 가슴 극단 + 정면은 거부, 3/4도 재현성 낮음. **하체·전신 볼륨이 있으면 정면도 통과**
- **실사 변환**: 가슴 강조 계열은 사람 실사로 변환 거부 → **조각상 변환(5-5장)** 또는 애니 전용으로 운영

## 3. 체형별 결과와 체형 블록 (3/4 기준)

### 3-1. 결과 요약 (애니 / 실사 분리)

**읽는 법**
- **애니 열** = 그 체형을 쓸 수 있는지 판단하는 기준 (형태가 여기서 결정됨)
- **실사 열** = 실사로 옮길 때 어떤 보정이 필요한지 알려주는 기준 (질감·근육·커버리지·소품 문제)

| 체형 | 애니 | 실사 | 비고 |
|---|---|---|---|
| USSBBW | ◎ | ◎ | 9개 재질 검증. 나전칠기로 4단계 완주. 배 길이는 허벅지 중간까지 |
| 아워글래스 SSBBW | ◎ | ◎ | 자주요로 4단계 완주, 등록 가능 |
| 헤비 머슬 | ◎ | ○ | 라이롯남 실사가 디지털 페인팅 질감 (금속 선 재질) |
| 매스 몬스터 | ◎ | ○ | 근육 유지. 얼굴 톤 불일치(애니 얼굴부터 밝았음), 골반 은선 수영복 윤곽 |
| 머슬 USSBBW | ◎ (정면 + 은입사) | ○ | 정면·은입사는 근육 유지, CG 질감. 3/4(자주요·라이롯남)는 실사에서 근육 소실 |
| 스모 | ◎ | ○ | 실사에서 돔의 둥근 느낌 약화. 3/4 + 동심원은 임신 배처럼 보임 |
| 머슬 아워글래스 BBW | ◎ | △ | 실사에서 가슴 공백 = 노출 → 채우기 필수 |
| 톱헤비 애플 | △ | △ | 애니부터 대비 약함. 정면은 다리 굵어짐, 3/4만 부분 성공(임신 배 경향) |
| 익스트림 페어 | △ | ○ | 애니부터 대비 약함(상체도 커짐). 실사 품질 자체는 좋음 |
| 글래머 아워글래스 | △ | ○ | 애니부터 극단성 부족 |

**결론**
- **"키우기" 방향 체형은 애니에서 전부 ◎**, **"작게" 대비가 필요한 체형(페어·글래머·톱헤비 애플)은 전부 △** — 대비 약점은 **애니 단계의 문제**
- 실사 단계 문제는 체형이 아니라 **변환 품질**: 금속 선 재질의 CG감, 근육 약화, 커버리지 공백 노출, 소품 변동 → 5-1·5-4장 보정 문장으로 대응

### 3-2. 체형 블록

**USSBBW (~1,000lb, 애니 기준) — v5.1 살 질감 버전**
```
USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,000 pounds — an enormous soft belly made of three or four massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, deep creases between each roll, not pregnant, a gigantic bust resting on the top roll, no waist at all, colossal wide hips and an enormous rounded rear jutting far out behind her, colossal thick thighs bulging out on both sides of the belly, huge soft upper arms with rolls, thick heavy calves. Her body fills the full width of the frame.
```
- 3/4 버전은 끝에 `even in the turned pose` 추가
- 조명: 측면광 + `deep soft shadows in the creases where each heavy roll of flesh folds over the next` (천 주름 음영 방지)
- 롤마다 윤곽선: `a [재질] band curving along the deep crease beneath every belly roll`

**자세 용도 구분 (USSBBW)**
| 자세 | 강조 | 보일 부위 문장 |
|---|---|---|
| 정면 | 배의 롤 구조, 좌우 폭 | `feet planted apart, the heavy belly resting on her thighs` |
| 3/4 | 히프 돌출, 측면 부피 | `the stacked belly rolls seen in side profile hanging forward and the enormous rounded curve of her hips and rear jutting out behind her` |

**아워글래스 SSBBW (~650lb)**
```
Hourglass SSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, not a plus-size model, around 650 pounds — a colossal heavy bust, a still-visible cinched waist indentation, a big soft rounded belly below the waistline hanging heavily over the top of her thighs, enormous round hips nearly three times the width of a normal woman's, a gigantic rounded rear jutting far out behind her, gigantic soft thighs pressing together down to the knees, huge soft calves, very thick soft arms, a full round face. Huge, heavy, soft, unmistakably hourglass. Her body fills most of the width of the frame.
```
- 3/4 보일 부위: `the waist indentation and the heavy belly below it seen in partial profile` → USSBBW와 구분되는 핵심

**헤비 머슬 (~600lb)**
```
Heavy muscular physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 600 pounds — gigantic boulder shoulders far wider than her hips, massive arms with huge defined biceps and triceps and thick forearms, a colossal bust, a thick powerful neck and back, no waist at all, the torso a massive column, colossal thighs with enormous defined quads, a huge rounded powerful rear, thick defined calves, and only the belly soft and round, no visible abs. A feminine face with a warm expression, no bodybuilder look. Her shoulders fill most of the width of the frame.
```

**머슬 아워글래스 BBW (~450lb)**
```
Muscular hourglass BBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 450 pounds — a thick soft layer of fat over huge muscle everywhere, enormously broad powerful shoulders, thick heavy arms with rounded biceps under the softness, a colossal soft bust, a cinched waist far narrower than her hips with a soft rounded belly folding slightly over the waistline, gigantic wide hips more than twice the width of her waist, an enormous rounded rear jutting far out behind her, colossal thick thighs with strong quads showing through the softness, thick strong calves. Strong and heavy at the same time, unmistakably hourglass. Her body fills most of the width of the frame.
```
- `a thick soft layer of fat over huge muscle everywhere` + `More soft than hard`가 없으면 근육 쪽으로 기울어짐 (팔레흐에서 확인)

**글래머 아워글래스 (보완 필요)**
```
Glamour hourglass bombshell physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy — a colossal full bust wider than her shoulders, a waist cinched so impossibly tiny it is barely a quarter of the width of her hips, hips flaring out to more than twice the width of her shoulders, an enormous rounded rear curving far out behind her, massive thick thighs pressing together down to the knees, long legs, a smooth flat belly, a dramatic S-curve silhouette seen in the turned pose. Her hips fill most of the width of the frame.
```
- 현재 결과는 비율 지시가 약하게 반영됨 → 다음 보완판에서 과장 강화 필요

---

**머슬 USSBBW (~1,100lb) — 권장: 정면 + 은입사**
```
MUSCULAR USSBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 1,100 pounds of colossal muscle and heavy soft flesh — gigantic cannonball shoulders far wider than her hips, massive arms with huge defined biceps and horseshoe triceps showing through a soft layer, thick powerful forearms, a thick powerful neck, a gigantic bust resting on the top roll, an enormous soft belly made of three or four massive rounded rolls of heavy soft flesh, each roll thicker and rounder than the one above it, the lowest roll hanging heavily down to mid-thigh, the belly flowing seamlessly into her hips and thighs at the sides as one continuous body, deep creases between each roll, not pregnant, no waist at all, colossal wide hips, colossal thighs with enormous defined quads bulging out on both sides of the belly, diamond-shaped calves. The muscle is defined only on the shoulders, arms, thighs and calves; the belly and rolls stay soft and round. A feminine face with a warm expression, no bodybuilder look. Her shoulders and body fill the full width of the frame.
```
- 문양은 **근육 분리선을 따라가게** (`silver lines tracing along every muscle separation on the shoulders, arms and quads`) — 은입사 성공의 핵심. 불꽃 문양처럼 근육과 무관한 배치는 근육을 약하게 만듦
- 골반 둘레 띠는 수영복 윤곽이 되므로 `silver lines on the hips follow the muscle vertically`
- 실사는 근육이 항상 한 단계 약해짐 → 애니에서 충분히 과장 + 5-1 근육 유지 문장

**스모 (~800lb) — 권장: 정면 낮은 자세 + 가로 띠 재질(자주요) / 정면 직립 + 나전**
```
EXTREME SUMO PHYSIQUE THE MOST EXTREME PHYSICALLY POSSIBLE, exaggerated far beyond real anatomy, around 800 pounds of dense solid mass — a colossal round firm belly forming one single smooth taut dome, wider than her shoulders, the belly broader than it is tall, filling the whole torso from just under the bust down to the hips and merging smoothly into her sides, one solid mass with her chest and hips, with no hanging rolls and no folds, not pregnant, massive rounded shoulders, thick powerful arms, a full heavy bust resting on top of the great dome, broad solid hips, pillar-like colossal thighs and thick solid calves. Firm and solid rather than soft, smooth rounded surfaces with no visible muscle definition. Her body fills the full width of the frame.
```
- 문양: `horizontal bands wrapping around the belly and continuing around her sides and back` (동심원은 배를 독립된 구로 강조 → 임신 배처럼 보임)
- 자세: `A low powerful stance facing the camera, feet planted very wide, knees bent outward, hands resting on her thighs`
- 조명: `a strong curved highlight and deep shadow across the great dome of the belly showing its roundness`

**임신 배 주의 (스모·톱헤비 애플 공통)**
- 배가 **위아래로 길고 앞으로 둥글게 돌출**되면 `not pregnant`가 있어도 임신 배로 읽힘
- 대책: `broader than it is tall`, `filling the whole torso from just under the bust down to the hips`, `merging smoothly into her sides` + 가로 띠 문양 + 정면 자세
- 3/4 회전 + 동심원 조합은 비권장

### 3-3. 극단 체형 후보 (애니 → 실사 파이프라인 기준)

**잘 되는 체형의 공통 조건** (오늘 결과에서 도출)
1. **과장 방향이 "키우기"**: 생성기는 부위를 키우는 지시는 잘 따르지만, "여기는 작게" 같은 대비 지시는 약하게 반영함 (페어에서 상체까지 커짐, 글래머에서 허리 대비 약화)
2. **폭으로 표현 가능**: `fills the full width of the frame`처럼 화면 폭으로 과장할 수 있는 체형이 유리. 길이(배를 무릎까지)는 한계가 있음
3. **부위 경계가 뚜렷**: 롤, 근육 분리선처럼 곡면이 나뉘어야 재질 윤곽선이 부피를 강조함
4. **3/4에서 보여줄 부위가 명확**: 히프 돌출, 배 측면, 어깨 등

| 체형 | 상태 | 핵심 과장 | 권장 자세 | 권장 재질 | 메모 |
|---|---|---|---|---|---|
| **USSBBW** | ◎ 확정 | 전신 폭, 배 롤, 히프 | 정면 / 3/4 | 나전, 자주요, 청자 킨츠기, 말라카이트, 포다이트 | 배 길이는 허벅지 중간까지 |
| **아워글래스 SSBBW** | ◎ 확정 | 허리선 아래 처진 배 + 거대한 골반·히프 | 3/4 | 자주요 | 4단계 완주 |
| **매스 몬스터 보디빌더** | ◎ 검증 | 근육 볼륨, 어깨 폭, 근육 분리 | 정면 더블 바이셉스 | 은입사 | 얼굴 톤 일치 문장 필수, 골반 은선은 세로 방향으로 |
| **헤비 머슬** | ◎ 확정 | 바위 같은 어깨·팔·대퇴, 배만 부드럽게 | 3/4 | 라이롯남 | 실사는 `사진처럼` 추가 |
| **머슬 아워글래스 BBW** | ○ 확정 | 근육 위 두꺼운 지방층 + 허리 대비 | 3/4 | 알레브리헤 | 가슴 채우기 단계 필수 |
| **스모** | ◎~○ 검증 | 단단한 돔형 배 + 기둥 같은 다리 | 정면 낮은 자세 / 정면 직립 | 자주요, 나전 | 3-2 블록. 가로 띠 문양, 3/4 + 동심원 비권장 |
| **머슬 USSBBW** | ◎ 검증 (정면) | USSBBW 부피 + 거대한 어깨·팔 근육 | 정면 | 은입사 (칠보 격벽선 등 근육선 재질) | 3/4·라이롯남은 실사에서 근육 소실 |
| **톱헤비 애플** | △ 검증 | 거대한 가슴·배·팔, 가는 다리 | 3/4 (부분 성공) | 칠보 | 정면은 다리 굵어짐. 3/4는 임신 배 경향. 우선순위 낮음 |
| **익스트림 페어** | △ 보완 필요 | 보통 상체 + 거대 하체 | 30도 회전 | 나전 | 가슴을 `a modest average bust`로, 대비 지시 약점 |
| **글래머 아워글래스** | △ 보완 필요 | 극단적 허리 대비 | 3/4 | 피에트라 두라 → 재검토 | 극단성 부족. 허리 대비는 "작게" 지시라 약함 |

**검증 완료 (v5.2)**: 머슬 USSBBW ◎(정면), 스모 ◎~○, 톱헤비 애플 △
- "작게" 대비 지시에 의존하는 체형(페어·글래머·톱헤비 애플)은 이 모델의 약점으로 확정 → 우선순위 낮춤
- 대비를 시도할 때는 절대 크기보다 **다른 부위와 비교**(`her thighs are narrower than her upper arms`)와 **화면 점유 분리**(`legs occupy only the middle third of the frame`)가 그나마 효과 있음

### 3-4. 신규 체형 6종 (v5.3 확정 — 애니 기준)

| 체형 | 핵심 | 권장 자세 | 비고 |
|---|---|---|---|
| **애슬리트 USSBBW** (~1,000lb) | 둥글고 결 없는 근육 + 두꺼운 지방, 스트롱우먼 계열 | 정면 / 3/4 | `no sharp muscle separation`, `broad blunt swells`가 머슬 USSBBW와의 구분점 |
| **콜로설** (~1,000lb) | 전신 균등 확대 + 키, 부위 집중 없음 | 정면 / 3/4 | 스케일 비례 문장 필수. 배가 튀어나오면 USSBBW로 흘러간 것 |
| **텐트폴 USSBBW** (~1,000lb) | 어깨·등 확장 + 골반 동일 폭 | 정면 (팔 벌림 포함) | 어깨만 넓히면 **남성 실루엣** → 골반을 같은 폭으로, `smooth rounded neck`, 가슴이 어깨선보다 앞으로 |
| **아워글래스 USSBBW** (~1,000lb) | USSBBW 롤 + 허리 들어간 곳 유지 | 3/4 / 정면 | 롤이 **허리 아래에서** 시작해야 허리가 묻히지 않음 |
| **톱헤비 아워글래스** (~350lb) | 가슴 극단 + 하체 볼륨 | 3/4 | 하체 볼륨이 있어야 통과. 애니 전용 |
| **바스트 퀸 BBW** (~500lb) | 가슴 극단 + 전신 BBW | 정면 / 3/4 | 정면·3/4 모두 한 번에 통과. 애니 전용 |

**불채택**: 바스트 퀸 슬림 (정면 거부, 3/4도 재시도 잦음, 실사 불가)

**오늘 재확인된 일반 법칙**
> 한 부위만 키우면 막히고, **전신을 키운 뒤 특정 부위를 더 키우면** 통과한다.
> 성공한 체형(USSBBW·머슬 USSBBW·스모·애슬리트·콜로설·텐트폴·바스트 퀸 BBW)은 모두 후자였고,
> 실패한 체형(페어·톱헤비 애플·글래머·바스트 퀸 슬림)은 모두 대비·축소 지시에 의존했다.

## 4. 재질 결과

### 4-1. 실사 변환 적합도: **피부 노출이 적은 재질이 최적**
- 어두운 바탕 재질(나전칠기, 자주요, 마키에, 은입사): 드러난 피부가 바탕과 이어져 가장 어두운 피부 유지
- 전신을 덮는 밝은 재질(청자 킨츠기): 드러난 피부 자체가 적어서 피부 톤 유지. 단, 결과 편차가 큼 (대리석화, 재질 반전, 배경 환각 이력) → 5-1 밝은 재질 문장 필수
- 피부가 바탕인 재질(알레브리헤)이 가장 까다로움
- **금속 선 재질(은입사, 라이롯남)은 실사에서 CG·일러스트 질감** — 선명한 금속 선이 애니 외곽선처럼 작동. 면 재질(자주요, 나전)은 실사감 우수 → 5-4 사진감 보강 문장 필수

| 재질 | 애니 | 실사 | 메모 |
|---|---|---|---|
| 자주요 흑유 척화 | ◎ | ◎ | 실사 최상급. 크림색이 흰 바탕처럼 번지지 않음 |
| 나전칠기 | ◎ | ◎ | 파이프라인 최초 성공 재질. 끊음질 사각 자개가 추가로 생기기도 함 |
| 마키에 | ○ | ◎ | 분위기 최고, 커버리지 가장 성김 (여백 미감) |
| 은입사 | ○ | ○ | **보강안 합격 → 보류 해제**. 실사가 3D 렌더 질감 → `사진처럼` 추가 검토 |
| 라이롯남 | ◎ | ○ | 실사가 디지털 페인팅 질감 |
| 알레브리헤 | ◎ | △ | 피부가 바탕이라 가슴 공백 시 노출. `her near-black skin is the base color` 필수 (`cobalt blue base`는 몸 전체를 파랗게 만듦) |
| 피에트라 두라 | ○ | △ | 실사에서 대리석 결 소실, 꽃 페인팅으로 바뀜 |

### 4-2. 애니 USSBBW 재질 순위 (윤곽·부피 기준)
말라카이트 ≈ 포다이트 > 썬마이 ≈ 알레브리헤 ≈ 칠보 > 나전칠기 > 라이롯남 > 청자 킨츠기 ≈ 청자 상감 > 에브루 > 천목
- **표면 전체형 재질**(말라카이트, 포다이트, 칠보)이 부피 표현에 가장 유리
- **천목**: 검은 유약이 피부와 구분 안 됨. 은색 오일 스팟 + 금갈색 토호문으로 보완하면 재질은 읽히지만 **노출 발생 이력** 있음
- **에브루**: 커버리지 약함
- **청자 상감**: 흰 상감에도 피부 밝아지지 않음. 줄무늬 띠가 소매·옷깃처럼 보이는 경향

---

## 5. 명령어 (확정)

### 5-1. 실사 변환 (애니 이미지 첨부)
```
이 체형 크기보다 더 크게 실사 이미지로 생성해줘. 패턴은 첨부 애니와 동일한 패턴으로. 얼굴부터 발끝까지 피부 전체가 원본처럼 가장 어두운 검은색이고, 얼굴과 몸이 같은 피부로 자연스럽게 이어지게 해줘. 온몸에 [재질] 같은 은은한 광택이 있고, [문양] 문양은 쇄골 아래부터 전신을 채우되 목에는 선 없이 문양만 서서히 사라지게 해줘. 얼굴은 문양 없이 표정이 살아 있는 사람 얼굴로 둬.
```
슬롯 예시: 나전칠기 = `옻칠` / `자개` · 자주요 = `유약` / `긁어낸 모란` · 썬마이 = `옻칠` / `금박과 붉은 연꽃` · 칠보 = `유약` / `금선 칠보`

**상황별 추가 문장 (v5.2)** — 해당될 때만 변환 문구 끝에 추가
| 상황 | 추가 문장 |
|---|---|
| 근육 체형 (머슬 USSBBW, 헤비 머슬 등) | `어깨, 팔, 허벅지의 근육 윤곽과 부피는 첨부 애니처럼 선명하고 단단하게 유지하고, 배와 롤만 부드럽게 해줘.` |
| 밝은 재질 (청자 킨츠기 등) | `재질은 첨부 애니와 같은 [색] 유약으로 유지하고, 배경은 첨부 애니와 같은 단순한 배경으로.` |
| 밝은 재질의 목 경계 | `목에는 선 없이…` 대신 `유약은 쇄골에서 깨끗한 금선 테두리로 마감되고, 그 위로는 얼굴과 같은 검은 피부가 이어지게 해줘.` (그라데이션이 그을음처럼 번짐) |
| 금속 선 재질 (은입사, 라이롯남) | `실제 스튜디오 사진처럼, 피부 결과 모공이 보이고 금속 선은 실제 상감처럼 요철과 반사가 있게 해줘.` |
| 공통 (소품 변동 방지) | `신발, 머리 장식, 액세서리는 첨부 애니와 똑같이 유지하고, 새로운 소품이나 장신구는 추가하지 마.` |

- 소품 변동 이력: 신발 추가(손에 든 한 켤레), 신발 소실(맨발), 목걸이·팔찌 추가, 금색 신발이 브론즈로

변환 문구 발전 과정 (참고)
| 버전 | 결과 |
|---|---|
| "더 크게 실사로"만 | 형태 재현 ○, 피부 갈색, 칠기 바탕 사라짐 (운에 따라 성공) |
| + 피부 검게 + "조각품처럼" | 얼굴까지 상감된 **완전한 조각상** (B 방향 — 별도 시리즈 후보) |
| + "목 아래" + "얼굴은 사람" | 얼굴 갈색, 목에 선 → **터틀넥 수트**처럼 읽힘 |
| + "얼굴부터 발끝까지 같은 피부" + "쇄골 아래, 선 없이" | **완성** (A 방향) |

### 5-2. 상체 채우기 (실사 이미지 첨부)
```
얼굴, 목, 손을 제외한 전신을 첨부 이미지와 동일한 패턴으로 빈틈없이 채워줘. 가슴은 매끈한 곡면 위에 큰 장식 문양 하나씩으로 완전히 덮고, 가슴 사이와 가슴 위쪽까지 문양이 이어지게 해줘. 체형, 자세, 피부색, 얼굴은 그대로 유지해줘.
```

### 5-3. 하체 채우기 (5-2 결과 첨부)
```
상체는 지금 그대로 유지하고, 하체만 첨부 이미지와 동일한 패턴으로 빈틈없이 채워줘. 허벅지 아래쪽, 허벅지 안쪽, 무릎, 무릎 뒤, 종아리, 발목 위까지 검은 맨살이 보이는 곳 없이 문양이 이어지게 해줘. 체형, 자세, 피부색, 얼굴은 그대로 유지해줘.
```
- 부작용: 손등까지 채워질 수 있음 → 원치 않으면 `손은 그대로` 추가
- 하체 문양이 상체보다 잘고 빽빽해질 수 있음 → `상체와 같은 크기와 간격의 문양으로` 추가

### 5-4. 선택 보정 문장
- 실사가 3D 렌더/디지털 페인팅처럼 나올 때: `사진처럼` 추가 (은입사, 라이롯남에서 필요)
- 배경에 소품(도자기 등)이 생길 때: `배경은 단순한 벽으로` (v4 규칙 8 — 같은 재질 소품 금지)
- 갤러리 배경·깨진 글씨 설명판이 생긴 이력 있음 → 배경 명시
- **이미 변환된 실사가 CG처럼 나왔을 때** (편집 명령):
```
이 이미지를 실제 스튜디오에서 촬영한 사진처럼 사실적으로 바꿔줘. 피부에 자연스러운 결과 모공, 미세한 톤 변화가 보이게 하고, 금속 선은 실제 상감처럼 약간의 요철과 반사 변화가 있게 해줘. 조명은 한쪽에서 들어오는 부드러운 스튜디오 조명으로 입체감을 살려줘. 체형, 근육, 자세, 피부색, 얼굴, 문양 배치는 그대로 유지해줘.
```

---

### 5-5. 조각상 변환 (v5.3 신규)
가슴 강조 계열처럼 **사람 실사로는 변환이 거부되는** 체형용. 사람이 아니라 공예품으로 판정되어 통과.
```
이 체형 크기보다 더 크게, 박물관에 전시된 실물 크기 조각상을 촬영한 사진처럼 생성해줘. 패턴은 첨부 애니와 동일한 패턴으로. 전체가 [재질]로 만들어진 하나의 조각으로, 표면은 매끈하고 광택이 있으며 이음매가 없게 해줘. 얼굴과 머리카락도 같은 재질로 조각되어 있고, 체형과 자세, 문양 배치는 첨부 애니 그대로 유지해줘. 배경은 단순한 벽으로.
```
- 얼굴만 사람으로 남기면 어중간해져 오히려 걸릴 수 있음 → 얼굴·머리카락까지 같은 재질로
- USSBBW 계열은 기존 사람 실사(5-1장)가 우선, 가슴 강조 계열은 이쪽이 기본

## 7. 실사 직접 생성 (v5.4 신규)

애니를 거치지 않고 바로 실사를 뽑는 경로. 애니 경유보다 과장은 작지만 질감이 자연스럽다. **용도를 나눠 쓴다.**

| 목적 | 경로 |
|---|---|
| 극단적 과장 | 애니 → 실사 변환 (4단계 파이프라인) |
| 사실적 질감 | 실사 직접 생성 |
| 가슴 강조 계열 | 애니 전용 또는 조각상 변환 |

### 7-1. 확정 템플릿 (효과 확인된 것만)
- **배경**: 무지 배경, 프레임에 인물만. 밝은 피부는 deep-charcoal, 어두운 피부는 mid-grey
- **촬영**: 85mm f/8, 측면 하드 레이킹 라이트 (질감을 살리는 핵심)
- **화면 점유**: `her body so wide that her hips are cut off by the left and right edges of the frame` — 가장 효과가 큰 문구
- **Skin 문단 독립** + 문양이 살 위 물감이라는 전제(`pigment sitting on living skin`)
- **깨짐 방지 2줄**: 곡면마다 윤곽 유지 / 팔다리 비율 유지
- **팔**: `arms held clear of her body with a visible gap of background between each arm and her side` (팔이 몸 앞을 가리면 체형이 죽음)
- 장소 배경(공원·터미널·극장·미술관)을 넣어도 부피는 유지되나 집중도는 낮아짐 → 검증은 스튜디오, 완성작은 장소

### 7-2. 복부 표현 절충안 (겹 + 지방량·무게)
겹 개수만 지정하면 실사에서 두세 겹으로 줄고, 지방량만 쓰면 층이 안 생긴다. **처지면서 겹이 생긴다는 인과로 연결**한다.
```
an immense mass of soft heavy fat sits on her middle, so much of it that it hangs far lower than it projects — sagging down over the tops of her thighs toward the knees under its own weight rather than pushing forward, gathering into three or four heavy rounded folds stacked one above the other as it falls, each fold thicker than the one above it, deep shadowed creases between them, the surface soft and uneven, never taut, never smooth, never round like a drum. It merges seamlessly into her sides, her hips and her thighs with no boundary anywhere, one continuous body rather than a separate mass, not pregnant.
```
- `hangs far lower than it projects` = 임신 배 방지의 핵심 장치
- 아워글래스 계열은 허리를 축소 지시 대신 위치·유일성으로: `a shadowed groove running around her middle, the one place on her body where the outline pulls inward`, 골반은 허리 너비 대비 3배

### 7-3. 질감 문구 (2단계 변환에도 사용)
**중**: 모공·미세 결 + 접힌 곳 주름·음영 + 문양이 굴곡 따라 일그러짐 + 측면 조명 + CG 느낌 배제
**강**: 위 + `큰 체구에 맞게 곡면이 늘어난 부분에는 옅은 튼살 결이 자연스럽게 보여도 좋아` + 접힌 곳에서 문양 갈라짐
- 튼살은 **허용하는 어조**로 쓸 것. `자국까지 보이게`라고 하면 과해진다

### 7-4. 자세 11종 (v5.5 확정)
각도 체계는 **정면 / 3/4 / 옆** 세 가지만 사용. 45도 = 3/4으로 통일.

| # | 자세 | 프레임 | 비고 |
|---|---|---|---|
| 1 | 선 자세 정면 | 세로 2:3 | 배 층 구조·좌우 폭 |
| 2 | 선 자세 3/4 | 세로 2:3 | 배 돌출·히프 곡선 |
| 3 | 걸터앉기 3/4 | 세로 2:3 | 돌 벤치(갤러리). 모서리에 허벅지가 눌려 살이 넘침 |
| 4 | 쪼그려 앉기 정면 | 세로 2:3 | 무릎 사이로 배가 내려앉음. 뒤꿈치는 든 상태 |
| 5 | 쪼그려 앉기 3/4 | 세로 2:3 | — |
| 6 | 무릎 꿇기 정면 | 세로 2:3 | **한쪽 무릎**(한 다리 세움). 정면에서 양 무릎은 쪼그려 앉기로 흘러감 |
| 7 | 무릎 꿇기 3/4 | 세로 2:3 | 양 무릎 |
| 8 | 무릎 꿇기 옆 | 세로 2:3 | 양 무릎. 배가 무릎선보다 앞으로 나온 거리가 보임 |
| 9 | 옆으로 누운 자세 | **가로 3:2** | 히프가 어깨보다 높이 솟음, 아래쪽 눌림. 팔이 몸 앞을 가리지 않게 |
| 10 | 엎드린 자세 | **가로 3:2** | 히프 최대, 등 롤 |
| 11 | 비스듬히 기대앉기 | **가로 3:2** | 배가 비탈을 따라 앞으로 쏟아짐 |

- 가로 자세는 세로 프레임에 넣으면 작아 보임 → 반드시 3:2
- **불채택**: 뒷모습 / 등 대고 눕기(옆·머리맡·발치 모두) / 네 발로 엎드리기 / 중간 각도 세분(22도·67도 — 3/4과 차이 없음) / 문틀 등 외부 기준물 / 광각 앙각
- 참고: 22도는 히프가 덜 보이는 대신 가슴이 잘 나옴 → 가슴 강조 체형 실사 시도 시 후보

### 7-5. 인종·연령
**부피에 영향을 주지 않음.** 결과 편차는 시드 편차. 다양성 확보용 변수로 자유롭게 조합.
- 밝은 피부: 배경을 어둡게, 검은 바탕 재질은 `reading clearly as paint on skin rather than as fabric` 추가
- 연령대별 살 표현(20대 탱탱 / 40~50대 처짐)은 넣되 부피와는 무관

### 7-6. 등록 산출물
`preset_builders/patch_livingartifact_photo_json.py` → `🏺 Living Artifact · Photo Direct` **252개**
(7체형 × 36 = 세로 24 + 가로 12. USSBBW · 아워글래스 USSBBW · 아워글래스 SSBBW · 머슬 아워글래스 BBW · 애슬리트 USSBBW · 콜로설 · 텐트폴 USSBBW)
키: `la_photo_{001..252}_{체형}_{자세}` / 세로 8자세 각 3개 · 가로 3자세 각 4개 / 인종 6 · 연령 4 · 재질 14 · 헤어·신발·네일·귀걸이 각 20
(구 140개 버전은 폐기 — 자세 구성이 3종뿐이라 중복)

### 7-7. 이미지 첨부 + 한국어 수정 요청 (v5.5 신규 / v5.7 확장 확인)
텍스트만으로 처음부터 생성할 때는 안 되던 자세가, **이미 나온 이미지를 첨부하고 한국어로 고쳐달라고 하면** 나온다.
참조 이미지가 있으면 텍스트 지시가 훨씬 잘 먹히는 것 — 애니 경유 파이프라인과 같은 원리.
```
이 이미지에서 자세만 무릎 꿇은 자세로 바꿔줘. 두 무릎을 모두 바닥에 대고 종아리는 뒤로 접혀서 엉덩이가 발뒤꿈치에 닿게 해줘. 체형, 크기, 피부색, 문양, 얼굴, 신발은 그대로 유지해줘.
```
- 불채택한 자세(등 대고 눕기, 네 발 자세)도 이 방식으로는 나올 수 있음 — 미검증, 시도해볼 가치 있음
- **v5.7: 자세뿐 아니라 장신구 추가에도 통하는 것을 확인.** 텍스트만으로 한 번에 다 넣으면 뒷부분이 뭉개지지만, 나온 이미지를 기준으로 하나씩 쌓으면 누적된다
- **작업 분담 (v6.0 확정)**

| 구분 | 항목 |
|---|---|
| 프롬프트로 | 체형 · 재질 · 자세 · 인종 · 연령 |
| 첨부 + 짧은 한국어로 | 다중 노출 겹침 · 장신구 추가 · 조명 연출 · 잡지 커버 스타일 · 세부 자세 조정 |

- **짧은 지시가 긴 프롬프트보다 낫다.** "7겹으로 겹치게 이미지 생성해줘. 8K" 정도면 충분하다. 긴 프롬프트에 다 넣으려 하면 지시끼리 밀어내 체형이 죽고 구조도 흐트러진다
- 겹침은 자세도 장르도 아닌 **후처리 변형**이다. 걷는 자세가 아니어도 되고, 기존 자세 어느 것에나 얹을 수 있다

## 8. 실사 듀오 (v5.6 신규)

### 8-1. 듀오 전용 규칙
- **`the camera set close ... so the two of them fill the frame edge to edge` 필수.** 이 구절을 빼면 카메라가 물러나 인물이 작아진다 (검증됨)
- **화면 배치를 반드시 명시**: 좌/우, 앞/뒤, 머리 방향. 안 하면 한 명이 다른 한 명에 묻힘
- **몸끼리 눌림**: `their hips and sides pressed against each other and the flesh bulging out where they touch` — 듀오에서만 가능한 부피 수단
- **팔 규칙 확장**: 자기 몸도 상대 몸도 가리지 않게
- **키 차이 명시**: 콜로설 같은 큰 체형은 `rises a head above the woman beside her` — 서로가 크기 기준물이 된다 (문틀은 실패했지만 사람은 작동)
- **안 보일 부위는 언급하지 않는다**: 무릎·허벅지에서 "자르라"는 지시는 먹히지 않음(발목 위까지 나옴). 대신 신발·발끝 묘사를 빼면 카메라가 가까워진다
- 듀오는 각자 조금 작아지는 것이 정상 — 화면을 나눠 쓰므로

### 8-2. 자세 8종
| 자세 | 프레임 | 판정 |
|---|---|---|
| 나란히 기대기 (같은 방향, 같은 등받이) | 가로 3:2 | ◎ 부피 최대 |
| 둘 다 걸터앉기 (짧은 돌 벤치) | 세로 2:3 | ◎ |
| 기대기 + 앉기 (높이 차이) | 가로 3:2 | ○ |
| 눕기 + 기대기 (머리 반대) | 가로 3:2 | ○ |
| 눕기 + 걸터앉기 | 가로 3:2 | ○ |
| 둘 다 눕기 (**머리 반대**) | 가로 3:2 | ○ |
| 둘 다 정면 | 세로 2:3 | ○ 무난 |
| 정면 + 3/4 | 세로 2:3 | ○ 무난 |

- **불채택**: 마주 보며 기대기(양끝 등받이), 같은 방향으로 둘 다 눕기(앞사람이 뒷사람을 가림)
- 벤치는 `just long enough for the two of them and no longer` — 길면 카메라가 물러남

### 8-3. 압축 템플릿
듀오에 솔로 템플릿을 그대로 쓰면 800단어를 넘는다. Skin·Body Art·팔 규칙·깨짐 방지를 마지막 `On both:` 한 문단으로 합치고, 재질은 바탕색 + 대표 문양 + 띠 흐름만 남긴다. 표정·나이별 살 표현 등 부피와 무관한 것은 뺀다.
구조: Image format → 촬영·배경(카메라 근접 구절 포함) → Subjects(둘 다 극단, 화면 점유, 눌림) → Left/Right woman → On both → 방향 문구

### 8-4. 등록 산출물
`preset_builders/patch_livingartifact_photoduo_json.py` → `🏺 Living Artifact · Photo Duo` **168개**
(7체형에서 2개씩 고른 21쌍 × 8자세) 키: `la_photoduo_{001..168}_{체형A}-{체형B}_{자세}`
가로 105 · 세로 63 / 인종·연령·재질·헤어는 좌우가 서로 다르게 오프셋을 줘서 배정

## 9. 재질 확장 (v5.7)

### 9-1. 문양 밀도가 생성 여부를 가른다
가장 중요한 발견. **표면에 빈 면이 넓으면 "칠한 맨몸"으로 읽혀 거부된다.**
- 얼룩·질감만 있고 문양이 없는 재질(녹청 구리 첫 시도)은 세 장 모두 거부
- 같은 재질에 새김 문양을 얹자 통과
- **매끈한 체형(콜로설)일수록 문양이 더 필요**하다. 접힘이 많은 체형은 크리스가 대비를 만들어 주지만 매끈하면 그게 없다
- 성공한 기존 14종이 전부 촘촘한 문양을 가진 것도 같은 이유

### 9-2. 조각상으로 흐르는 것 막기 (금속 계열 공통)
문양을 얹으면 이번엔 청동상처럼 보인다. 네 가지를 함께 쓴다.
- 촬영 문장에 `a real photograph of a living woman ... not a statue`
- **Skin 문단을 Body Art 앞으로** 배치
- Body Art 첫머리를 `Over that living skin ...`으로 시작해 순서를 명시
- 끝에 `living flesh under weathered paint, not a bronze statue`
- 은입사·라이롯남처럼 CG·금속 느낌으로 흐르던 재질에도 그대로 적용 가능

### 9-3. 녹청 구리 (신규 채택, 재질 15번째)
```
Over that living skin she is painted with weathered verdigris copper — a blue-green patina ground covering her whole body, ranging from pale mint through turquoise to deep sea-green, pooling thick and dark in the shadow of every crease where rain would gather and thinning to bare warm copper across the high points where weather would have worn it away, so that the drift of the corrosion itself maps the shape of her body. Scattered across it, a few simple chased bands and spiral rosettes in bright copper, worn thin and interrupted by the patina rather than covering it.
```
- 접힘이 많은 체형에서 안정적. 콜로설처럼 매끈한 체형은 문양을 `densely ornamented`로 늘려야 통과

### 9-4. 불채택 재질
이레즈미(생성 거부) / 청자 킨츠기(문양 흐림) / 란각 옻칠 · 다마스쿠스 강 · 흑요석 · 대모 · 라피스라줄리(결과 약함) / **장신구를 재질로 쓰기**(금·구슬 세공·흑금·산호호박 — 옷처럼 보이고 살의 굴곡이 한 겹 가려짐)

---

## 10. 문양·표면·프레임 (v5.7)

### 10-1. 문양 교체 방식
재질(바탕·광택)과 문양(무엇이 그려졌나)을 분리해 갈아끼운다. 나전칠기 고정 + 문양 교체로 검증.
```
Over that living skin she is painted in [재질], a [문양] design — [바탕] + [주 모티프가 곡면에 얹히는 방식] + [크리스에서 촘촘, 볼록면에서 넓게] + [띠가 곡면을 감싸고 사이를 채움]
```
- **문양이 바뀌어도 띠 구조와 크리스 밀도 대비는 유지**해야 한다. 그게 부피를 만든다
- 단일 모티프만 쓰면 원래 재질 문장보다 단조로워진다 → **주제 한 덩어리로** 묶을 것 (바다 = 파도·물보라·물고기·학 / 가을 = 단풍·국화·기러기·달)
- 후보 주제: 바다 · 봄 · 여름 · 가을 · 겨울 · 정원 · 숲 · 밤하늘 · 산호초 · 기하

### 10-2. 오일 광택
```
Her whole body is oiled to a high sheen, so a long bright highlight runs down the swell of every fold, hip and thigh and pools in the deep creases between them.
```
하이라이트가 볼록면을 타고 흐르고 크리스에 고이는 구조라 곡면이 더 드러난다. 과하면 `lightly oiled`로 낮춘다.

### 10-3. 피어싱·장신구 (액세서리로만, 재질로는 불가)
- **Jewellery 문단을 따로** 둔다. Subject에 합치면 얼굴 묘사가 묻힌다
- 최대치로 갈 때는 **부위별로 문단을 나눈다** (이마·눈/뺨·코/입·턱/목·귀). 한 문단에 몰면 뒤쪽이 무시된다
- 크기는 신체 기준점 비교로: `as wide as her mouth`, `the largest brushing her shoulders`
- 무게 표현이 현실감을 만든다: `the lobes pulled long under the plugs`, `the metal pressing very slightly into the skin where it passes through`
- **눈과 입은 반드시 비운다**: `her eyes and mouth the only bare places left`. 없으면 얼굴 전체가 덮여 인물이 사라진다
- 배꼽 피어싱은 배가 매끈한 체형(콜로설·머슬 아워글래스)에서만. USSBBW는 배꼽이 겹에 묻히고, 드러내려다 배가 평평해진다. `the navel itself a deep dimple set in the smooth swell of her belly` 필수
- 바디 체인은 `the links pressing gently into the flesh where they cross it`로 부피 표현에 보탬
- 유두 피어싱은 불가 (노출 판정)
- **인도 계열이 가장 잘 나온다** — 얼굴 장신구 전통이 실제로 발달해 있어 밀도를 올려도 자연스럽다

### 10-4. 극단 플랫폼 힐
```
towering platform stiletto slingbacks built like architecture — a solid slab platform sole a full hand's depth thick under the ball of each foot, and above the heel a needle-thin stiletto twice the height of that platform again, so steep that each instep stands almost vertical, the ankles braced against the strain
```
두께를 신체 기준점(`a full hand's depth`)으로, 힐 높이를 플랫폼의 배수로 지정한다.

### 10-5. 부위별 프레임
전신 외에 상체 / 배꼽 / 히프 / 얼굴 / 얼굴+목 프레임을 쓸 수 있다.
- **프레임 밖 부위는 아예 언급하지 않는다.** 전신 묘사를 남기면 카메라가 물러난다
- `Framing:` 문단을 앞쪽에 두고 어디부터 어디까지인지 명시
- 조리개를 f/5.6~f/4로 열고, 얼굴 클로즈업은 105mm
- 배꼽·히프는 몸이 가로로 누우므로 3:2
- 얼굴 프레임에서는 `a full round face with soft heavy cheeks`로 체급을 남긴다. 단, **이중턱 표현은 남자처럼 보이게 하므로 뺀다** — 대신 `a gently tapering jaw and a delicate chin` + 인종별 이목구비 서술
- 얼굴에는 하드 레이킹 라이트 대신 **소프트 대형 광원 + 필**을 쓴다 (`without hardening it`)
- 화장은 `Makeup:` 문단으로 분리하고 끝에 `the skin still reads as skin`

### 10-6. 나라별 메이크업 특색
| 지역 | 특징 |
|---|---|
| 한국 | 촉촉한 베이스, 일자 눈썹, 눈두덩 글리터, 그라데이션·글로시 립 |
| 중국 | 창백한 베이스, 가늘고 높은 눈썹, 눈꼬리를 길게 올리는 붉은 눈매, 작고 또렷한 립 |
| 일본 | 눈 아래를 넓게 쓰는 아이 메이크업, 눈꼬리를 내리는 라이너, 볼 중앙 핑크 블러셔, 체리 그라데이션 립 |
| 인도 | 콜 아이라이너, 크림슨·골드 섀도, 빈디, 깊은 레드 립 |
| 중동 걸프 | 짙은 콜을 양 수분선에 두껍게, 브론즈·차콜 스모키, 강한 눈썹 |
| 북유럽 | 베이스 최소화로 주근깨를 살림, 톤다운 섀도, 틴티드 밤 |
| 안데스 | 볼 중앙에 넓고 둥근 붉은 홍조, 러스트·테라코타 섀도 |
| 에티오피아 | 브론즈·구리 섀도, 이마·턱의 전통 문신 자국 |

---

## 11. 임산부 변형 (v5.8 신규)

체형 축을 늘리는 것이 아니라 **기존 체형 위에 얹는 변형 옵션**. 애니에서 검증 완료, 실사는 미확인.

### 11-1. 핵심 구조
기존 프롬프트의 `not pregnant`를 빼고 `heavily pregnant`로 바꾼 뒤, **팽팽한 면과 늘어지는 지방이 만나는 경계**를 서술한다. 그 경계가 보여야 두 성질이 한 몸에 있다는 게 읽힌다.
```
At the front of her body a great taut rounded belly of late pregnancy stands high and firm, the skin drawn tight and smooth over it, projecting far forward past everything else. Around it and beneath it the immense mass of soft heavy fat is still there and still hanging: thick rolls of soft flesh gather above the firm curve and press down onto it from the top, more soft flesh banks up at her sides and folds over its edges, and the lowest roll hangs heavily below it down to mid-thigh, so the soft flesh and the taut curve meet in deep shadowed creases all around where one presses into the other.
```
- **위·옆·아래 세 방향**에서 만나게 하는 것이 요령
- 깨짐 방지 문구는 `Every roll and the firm curve of the belly keeps its own clear rounded outline...`로 확장

### 11-2. 문양 처리
팽팽한 면과 늘어지는 면을 문양으로도 구분한다.
- 배 중앙에 **큰 메달리온**, 거기서 **동심원으로 퍼지는 띠**
- 늘어지는 롤에는 기존대로 크리스를 따라가는 띠
- (주의) 동심원은 원래 임신 배로 읽히게 하는 요소라 비권장이었으나, **실제로 임신 배일 때는 오히려 맞다**

### 11-3. 체형별 처리
| 체형 | 처리 |
|---|---|
| USSBBW | 롤이 배를 위·옆·아래에서 감싼다. 기본형 |
| 콜로설 | 롤이 없으므로 균등한 몸에서 배가 솟아나고 옆면 살만 경계에 쌓임 |
| 아워글래스 USSBBW | 허리 아래에 배가 오고 그 주위를 롤이 감쌈 (허리·배·롤 3층) |
| 애슬리트 USSBBW | 배럴 토르소 앞에 배가 붙고 근육은 어깨·팔·허벅지에만 |
| 톱헤비 아워글래스 | 가슴과 배가 맞닿음 → 그 경계를 크리스로 |

### 11-4. 자세와 실사
- **3/4 기본.** 앞으로 나온 깊이가 보여야 팽팽한 배가 드러난다. 정면은 롤에 가려질 수 있음
- 한 손을 배 아래에 받치는 포즈가 자연스럽다
- **실사 버전**은 Skin 문단에서 질감을 둘로 나눈다: 늘어지는 살은 기존대로 모공·주름, 팽팽한 배는 `stretched tight and faintly shining with the pores drawn out and fine silvery stretch marks fanning up its sides and around the navel`. 문양도 `stretched thin over the firm belly and cracking where the soft flesh folds`로 구분

---

## 12. 출력 장르 (v5.9 신규)

지금까지 실사와 애니 두 가지만 썼으나, 세 번째 축으로 **조각상 계열**이 확립됨. 회화 장르도 일부 가능.

### 12-1. 장르별 판정
| 장르 | 결과 |
|---|---|
| 실사 (스튜디오) | ◎ 기존 |
| 애니 | ◎ 기존, 부피 최대 |
| **조각상 렌더** | ◎ **신규 채택** — 공예품으로 판정되어 실사가 막히는 것도 통과 |
| 아르누보 포스터 | ○ 채택 |
| 우키요에 · 아르데코 · 비잔틴 모자이크 · 페르시아 세밀화 · 아메리칸 코믹 · 스테인드글라스 도해 · 밴드 데시네 | 결과 대기 |
| 포토리얼 3D | × 실사와 구분 안 됨 |
| 스타일라이즈드 3D (애니풍) | × 생성 거부 |
| 클레이 스컬프 (무재질) | × 거부 — 맨몸으로 읽힘 |
| 잡지 커버 (패션지·아트지) | × 거부 → 이미지 첨부 후 한국어 요청으로 (7-7장) |

> **3D는 독립 축이 되지 못한다.** 애니와 실사 사이에 자리가 없고, 살아남은 것은 조각상 형식 하나뿐. v5.2의 "3D는 실제로 안 나옴" 기록과 일치.

### 12-2. 조각상 프롬프트 구조
```
Style: A digital sculpture presentation render — a high-resolution sculpt of a [재질] statue, shown with studio HDRI lighting and physically based [재질] shading, every form read through [그 재질에서 형태를 드러내는 방식], the look of a character artist's turntable render. Not a photograph and not an illustration.
```
그 뒤로 Subject(조각상임을 명시) → Physique → **Surface**(재질 물성) → **Carved/Cast/Painted Ornament**(그 재질의 기법으로) → Pose(받침대 위) → Lighting & Environment.

- **재질 물성이 곡면을 드러내는 역할**을 한다. 실사에서 문양 띠가 하던 일을 여기서는 물성이 함
- 문양은 그 재질의 실제 기법으로: 부조(돌·나무) / 주물(금속) / 상감(청자·나전) / 언더글레이즈(자기) / 사그라피토(흑유)
- 문양 밀도 규칙(9-1장)은 여기서도 적용 — 무재질 클레이가 거부된 이유
- **정면은 자제.** 부피가 큰 체형은 3/4 · 걸터앉기 · 옆으로 누운 자세

### 12-3. 조각상 재질 13종 (v6.0 확정)
| 계열 | 재질 | 색 | 문양 기법 |
|---|---|---|---|
| 반투명 5 | 설화석고 | 유백 | 부조 |
| | 비취 | 짙은 녹 | 부조 |
| | 호박 | 호박색 | 부조 |
| | 주조 유리 | 청록 | 주조 부조 + 무광 |
| | **얼음** | 투명·유백 | 부조 (녹는 중) |
| 돌 2 | 흰 대리석 | 순백 | 부조 |
| | 흑요석 | 검정 (경면) | 부조, 무광 절단면 |
| 금속 1 | 청동 (녹) | 어두운 갈색 + 밝은 청록 | 주물, 문양 최소 |
| 도자 4 | 백자 (청화) | 흰색 + 코발트 | 언더글레이즈 |
| | 자주요 흑유 | 검정 + 흰색 | 사그라피토 |
| | 고려청자 상감 | 비색 + 흰 학 | 상감 |
| | 이마리 | 흰색 + 코발트·적·금 | 언더글레이즈 + 오버글레이즈 |
| 기타 1 | 웨지우드 재스퍼 | 무광 하늘색 + 흰 부조 | 스프리그 부조 |

**불채택**: 화강암 / 라피스라줄리 / 금박 목조 / 목조 / 주칠 나전 / 용천요 청자 / 당삼채 / 분청사기 / 이즈니크(이마리와 색 겹침) / 세이지 청자(채색 버전은 보류)

**얼음의 특수성**: 유일하게 **시간이 들어간 재질**. 볼록면에 물이 흐르고 크리스에 고이고, 가슴 아래·배 끝에 물방울이 맺히고, 받침대에 물이 고이고, 새긴 문양선이 녹아 뭉개지기 시작한다.

### 12-6. Sculpture 프롬프트 작성분 (등록 전, 검증 대기)
| 파일 | 내용 | 개수 |
|---|---|---|
| `LumineX_Sculpture_001_042_prompts.txt` | 솔로 — 청화백자·고려청자 상감 × 7체형 × 3자세 | 42 |
| `LumineX_SculptureDuo_001_042_prompts.txt` | 듀오 — 같은 2재질 × 21쌍 × 3자세 | 42 |
- 스크립트: `patch_livingartifact_sculpture_json.py` / `patch_livingartifact_sculptureduo_json.py`
- **프롬프트 파일만 생성**이 기본. 등록은 `--write-presets` 옵션
- 인종 한/중/일 · 연령 아이돌/20대 후반/30대 후반이 순환 배정 (듀오는 두 인물에 다른 오프셋)
- 자세 3종: 3/4 서기 · 걸터앉기 3/4 · 옆으로 누운 자세(가로 3:2). 듀오는 나란히 3/4 서기 · 둘 다 걸터앉기 · 눕기+걸터앉기

### 12-4. 청동 녹 배합 (확정)
어두운 청동이 바탕, 밝은 청록 녹이 **절반 조금 못 되게** 흘러내리는 비율.
- 금속은 `deep near-black brown, almost unlit`
- 녹은 물이 흐르고 고이는 자리에만 — 어깨에서 흘러내리는 세로 줄, 주름 아래 고인 곳, 무릎 뒤·겨드랑이
- 녹줄 사이에 어두운 금속 통로를 남겨야 코팅이 아니라 흘러내린 자국으로 읽힘
- `No brown rust, no flaking` — 갈색 녹과 벗겨짐은 낡아 보임
- 비율은 `A little under half the surface has gone green` 한 줄로 조정

### 12-5. 반투명 재질의 역광 규칙 (중요)
반투명 재질은 **재질 지정만으로는 성질이 드러나지 않는다.** 빛이 어디로 들어와 어디로 나가는지까지 써야 한다.
```
A powerful backlight sits low and directly behind her, aimed through the statue toward the camera, so it drives hard into the [재질] from behind — the whole outline of her body burns [색] and every thin edge blazes, while only a small soft fill from the front keeps the near side readable. The figure is lit far more from within than from without.
```
Surface 문단에도 **얇은 부위를 하나씩 나열**한다: 몸 윤곽선 / 주름이 들리는 가장자리 / 팔 바깥선 / 손등 / 어깨 위 / 히프·허벅지 능선 / 땋은 머리 가닥. 두꺼운 곳은 어두워진다고 함께 명시해 두께 대비를 만든다.

| 재질 | 조명 |
|---|---|
| 호박 · 비취 · 주조 유리 | 역광 관통 (필수, 효과 큼) |
| 설화석고 · 백자 | 역광 관통 (약하게 작동) |
| 대리석 · 화강암 · 청동 · 흑요석 · 도자 일반 | 측면 하드 키 + 후면 림 |

---

## 13. 극단 부피 (v6.1 신규, v6.4 전면 재확정)

애니에서 무게를 1,000 → 5,000파운드까지 밀어 확인한 것. **애니는 파운드 수치를 실제로 반영한다.** 실사는 이 스케일을 따라오지 못한다(13-11 참조).

### 13-1. 무게별 안정 구간
| 무게 | 결과 |
|---|---|
| 1,000~1,200 | 안정적. 기존 프리셋 기준 |
| 1,500~2,000 | 안정적. **실용 상한** |
| 5,000 | 체형은 나오지만 13-2~13-9 조건을 전부 지켜야 함 |

기본은 1,000~1,500, 극단이 필요할 때만 5,000.

### 13-2. Body Art는 원본 짧은 형식 — 띠 표현 전면 폐지 (v6.4 확정, 중요)
v6.1~v6.3에서 시도했던 **띠형**(`wide bands following the deep crease... like contour lines`)과 **연속형**(`no bands and no borders... the drift of the pattern alone maps the shape of her`) 서술은 둘 다 **폐기**한다. 두 방식 모두 극단 체형에서 탱크탑·코르셋처럼 보이는 원인이 됐다(13-6, 13-7 참조).

**앞으로는 예외 없이 원본 짧은 형식만 쓴다:**
```
Body Art: Full body [재질명] body painting on her bare skin from the collarbones to the ankles, [재질 설명 — 색과 문양 소재만, 띠·밴드·등고선 비유 금지]. The pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly and the calves, covering them as densely as the chest.
```
- `bands`, `wrapped`, `curving around... like contour lines`, `belt`, `corset` 계열 단어는 재질 설명에 절대 넣지 않는다
- 이 형식은 1,000파운드든 5,000파운드든 동일하게 쓴다 — 무게에 따라 서술을 늘릴 필요 없음
- Body Art는 여전히 **Subject 다음, Physique 앞**에 둔다(위치 규칙은 13-3에서 유지)

### 13-3. Body Art 위치 규칙 (유지)
**체형 서술이 길어질수록 Body Art를 Physique 앞으로 뺀다.** 뒤에 두면 밀려서 옷으로 읽힌다. 듀오에서 옷 문제가 생겼던 것도 같은 원인(두 인물을 쓰느라 문양이 뒤로 밀림).

### 13-4. 비율 기준점 (숫자보다 효과가 크다)
| 항목 | 1,000~1,500 | 5,000 |
|---|---|---|
| 주름 개수 | 4~5 | 6~7 |
| 가장 아래 주름 | 무릎~정강이 | **바닥에 퍼짐** |
| 히프 배율 | 어깨/허리의 3~4배 | **7배** |
| 허벅지 | 보통 사람 허리보다 굵음 | **보통 사람 키보다 넓음** |
| 머리 | `looks small` | `looks tiny`, **히프 너비의 1/10** |
| 어깨 | 4~5 머리 너비 | **8 머리 너비** |
| 팔 | 옆구리에 못 닿음 | **거의 수평으로 벌어짐** |
| 손 | 보통 사람 몸통 너비 | + **손가락이 보통 사람 팔 굵기** |
| 화면 잘림 | 가장자리에서 잘림 | `cut off well inside the edges` |
| 앉은 자세 | 벤치에 눌림 | **벤치가 몸에 묻혀 안 보임** |
| 서술 | `far beyond any real person` | `beyond anything a living body could be` + `a mountain of a woman` |

- 깨짐 방지 문구(`arms, hands, legs and feet stay in correct proportion to one another`)는 이 배율에서 **더 중요하다.** 손발이 먼저 무너진다
- **콜로설처럼 접힘 없는 체형**은 주름으로 크기를 못 보여주므로 비율 기준점을 4~5개 겹쳐 쓴다

### 13-6. 허리 있는 체형 — 코르셋 착시와 처방 (v6.4 신규)
아워글래스 계열(아워글래스 USSBBW·아워글래스 SSBBW·머슬 아워글래스 BBW·톱헤비 아워글래스)은 5,000파운드에서 **허리 부위가 코르셋이나 벨트처럼 옷으로 읽히는 문제**가 반복됐다. 원인은 애초에 Body Art에 남아 있던 띠 표현(13-2에서 이제 제거)과, 잘록한 허리 자체가 몸을 두른 띠 모양으로 오인되는 것 둘 다였다.

**처방 — 허리를 언급하는 바로 그 자리에 다음 문장을 넣는다:**
```
That inward turn is nothing but the shape of her own flesh, painted exactly as continuously as every other part of her, the pattern simply following the flesh in and out again with no interruption, no closed shape, and no separate piece of anything laid over the skin there.
```
- 솔로·서기 자세에서 가장 불안정했고, **듀오에서는 훨씬 안정적**이었다(옆에 다른 몸이 있어 시선이 분산되는 것으로 추정) — 듀오라면 이 처방만으로 충분
- **눕기 자세는 처방 없이도 안정적**이었다(허리가 몸의 길이 방향으로 나타나 띠 각도가 안 나옴) — 여유가 없으면 눕기로 우회하는 것도 방법
- 허리 없는 체형(USSBBW·콜로설·텐트폴·애슬리트·바스트 퀸)은 이 처방이 필요 없다

### 13-7. 어깨 넓은 체형 — 탱크탑 착시와 처방 (v6.4 신규)
텐트폴 USSBBW·애슬리트 USSBBW처럼 어깨(광배근·삼각근)가 몸통과 별도 덩어리로 튀어나오는 체형은 5,000파운드에서 **어깨선이 탱크탑 끈처럼 읽히는 문제**가 나왔다.

**처방 — 어깨를 언급하는 자리 뒤에 다음 문장을 넣는다:**
```
The same [재질] pattern lies flat and continuous across the top of each shoulder, over each deltoid and down into the chest with no seam, no strap and no separate panel of colour anywhere at the shoulder — the paint simply follows the flesh over that curve exactly as it does everywhere else on her.
```

### 13-8. 동사 선택 — "흐르는" 동사 금지 (v6.4 신규)
`hangs straight down`, `spills forward`, `spread where it meets the stone` 같은 **흐르거나 늘어지는 동사**는 두 가지 부작용을 일으켰다: 살이 옷자락처럼 보이거나, 자세 지시가 다른 자세(무릎 꿇기 → 쪼그려 앉기)로 새어나갔다.

**대신 "쌓이고 눌린 덩어리"로 고정하는 동사를 쓴다:**
- `hangs straight down in front of her` → `sits stacked one above the other in front of her`
- `spread where it meets the stone` → `resting heavy and solid against the plinth` (+ 필요시 `without spilling past it`)

### 13-9. 무릎 꿇기 자세 고정 (v6.4 신규)
동사를 고쳐도 무릎 꿇기가 쪼그려 앉기로 새어나가는 경우가 있었다. Pose 문단에 자세를 **이중으로 못박는다:**
```
Pose: Kneeling upright square to the camera on a low stone plinth, her knees planted directly beneath her body and set apart, not squatting and not crouching, her calves folded flat back beneath her and her weight settled down onto her heels, her spine held straight and vertical, her face to the camera, arms held clear of her body with a gap of background at each side, full body head to toe.
```
`not squatting and not crouching`와 `spine held straight and vertical`가 핵심.

### 13-10. 듀오에서의 5,000파운드 (v6.4 신규)
- 듀오는 솔로보다 조건이 관대하다. 허리 있는 체형도 처방만 넣으면 무리 없이 나옴(13-6 참조)
- **팔이 프레임 밖으로 잘리는 것은 지시할 필요가 없다.** 텐트폴처럼 어깨가 실제로 넓은 체형을 하나라도 섞으면 자동으로 잘려 나간다. 콜로설·바스트 퀸처럼 매끈한 체형끼리면 화면 안에 다 담긴다 — 잘림 여부는 체형 조합이 결정하지 지시가 결정하지 않는다
- 두 사람이 맞닿는 자리는 `Coverage:` 문단을 따로 둬서 처리:
```
Coverage: Where the two women's bodies press together at hip and side, the flesh of each bulges into the gap and presses flat against the other, each woman's own rounded outline still clearly her own on either side of that pressed seam.
```

### 13-11. 실사 5,000파운드 — 한계 확인, 비교 대상 실험 (v6.4 신규)
실사는 5,000파운드에서 애니만큼 극단적으로 나오지 않는다. 실사는 "그럴듯한 사람"으로 수렴하려는 경향이 강해, 비율 지시(히프 7배, 손가락이 팔 굵기 등)가 애니보다 약하게 반영된다.

**비교 대상을 넣어 크기를 체감시키는 시도:**
- **벤치**(같은 화면의 소품) — 어느 정도 효과 있음. `Scale is visible in what stands beside her: the stone bench...` 형태로 Physique 문단에 넣고, 한쪽 팔을 벤치 쪽으로 뻗어 비교가 실제로 보이게 포즈도 조정
- **문틀** — 두 차례 시도(세로·가로) 모두 폐기. 이유 불명, 재시도 비권장

**결론**: 실사 극단은 1,000~1,500선에서 만족하고, 5,000 같은 순수 극단은 애니 전용으로 두는 것이 실용적이다.

**추가 확인 (v6.5)**: 실사는 **1,500과 5,000 사이에 체감 차이가 거의 없다** — 숫자를 올려도 실사가 인체다움 쪽으로 수렴하는 경향이 강해서인 것으로 보인다. 비교 문구(벤치·문틀 등)로 크기를 보강하려 할 때도 **하나만 간단히 넣는 것이 상한**이다. 한 문단에 "보통 여성보다 허벅지가 넓다", "손가락이 팔 굵기다" 같은 비교를 여러 개 몰아넣으면 **오히려 몸이 날씬해지는 역효과**가 났다 — 비교 대상이 많아지면 "극단적으로 큰 한 사람"이 아니라 "보통 체형과 나란한 비교 장면"으로 모델이 읽어, 중간 어딘가로 타협하는 것으로 추정된다. 실사에서 부피를 강조할 때는 무게 숫자를 올리기보다 **비교 문구를 최대 하나로 제한**하는 것이 안전하다.

### 13-12. 옆으로 눕기 체형 적합도
살이 옆으로 쏟아지는 것이 볼거리이므로 접힘이 많고 무른 체형이 유리. **애니가 최적.** 프레임은 가로 3:2.

| 체형 | 판정 | 눕기에서 달라지는 지점 |
|---|---|---|
| USSBBW | ◎ | 배가 앞으로 쏟아져 바닥에 닿고, 위쪽 히프가 어깨(또는 머리)보다 높이 솟음 |
| 아워글래스 SSBBW | ◎ | 가슴·히프가 바닥으로 퍼지고 허리만 안 닿아 **바닥과 몸 사이 틈**이 생김 |
| 바스트 퀸 BBW | ◎ | 가슴 두 쪽이 따로 흘러내림 — 아래쪽은 바닥에 눌려 퍼지고 위쪽이 그 위에 얹힘 |
| 아워글래스 USSBBW | ○ | USSBBW와 비슷하게 보일 수 있음 |
| 톱헤비 아워글래스 | ○ | 가슴은 좋으나 아래가 가벼워 균형이 안 맞음 |
| 머슬 아워글래스 · 애슬리트 | △ | 근육이 받쳐 덜 퍼짐 |
| 콜로설 · 텐트폴 | × | 콜로설은 형태 변화가 없고, 텐트폴은 어깨 너비가 안 보임 |

---

## 14. 인물 설정 확장 (v6.1 신규)

### 14-1. 연령에 실버폭스 추가
듀오에서 **대비 폭**을 넓히는 용도. 아이돌(20대 초반) × 실버폭스 조합이 특히 좋다.
```
a striking silver-haired beauty, ... large calm dark eyes with fine lines at the outer corners, softly arched pale brows, a full head of natural silver-white hair in [헤어], a quiet assured expression with the poise of a woman who has nothing left to prove
```
- 애니는 50대 초중반까지, **실사는 40대 초반까지** — 그 이상은 피부 처짐이 부피 표현과 섞여 지저분해진다
- 실사에서는 `whose hair turned early — her face still young and firm with only the faintest lines at the outer corners of her eyes`로 은발이 이른 것임을 명시
- 은색 계열이 화면에 있으면 조명을 **차가운 쪽**으로

**듀오 대비 네 축**: 나이(20대×50대) · 머리(흑발×은발) · 체형(접힘 많은×매끈한) · 재질(따뜻한 색×차가운 색). 넷이 같은 방향으로 정렬되면 화면이 선명해진다.

### 14-2. 아이돌 얼굴·헤어
| | 한국 | 일본 |
|---|---|---|
| 인상 | `the polished look of a K-pop idol` | `the sweet look of a Japanese idol` |
| 얼굴 | 갸름한 턱, 쌍꺼풀 있는 또렷한 눈, 도톰한 입술 | 둥근 볼, 크고 동그란 눈, 작은 입 |
| 표정 | 쿨하고 정제된 | 밝고 활짝 |

**현대 헤어 10종** (전통 비녀·상투는 시대극처럼 보이므로 뺀다): 롱 스트레이트 + 시스루 뱅 / 턱선 블런트 밥 / 롱 웨이브 + 가운데 가르마 / 애시브라운 웨이브 / 숄더 레이어드 + 아웃컬 / 하이 포니테일 + 잔머리 / 허니브라운 비치웨이브 / 숄더 블런트 + 일자 뱅 / 초장발 스트레이트 / 체스트넛 컬 + 집게핀
30대 이상은 낮은 시뇽 · 커튼 뱅 · 한쪽으로 넘긴 웨이브처럼 차분한 쪽으로.

### 14-3. 혼합 출력 (실사+애니 / 실사+조각 / 애니+조각) — v6.3 확정
한 인물의 몸을 두 개 이상의 매체로 나누는 방식. **경계 처리가 전부다.**

#### 분할 구조 — 3분할이 실사용 상한
| 구조 | 구성 | 판정 |
|---|---|---|
| 2분할 | 몸을 좌우로 둘 | ◎ 안정 |
| **3분할** | 얼굴(실사) + 몸 좌우 둘 | ◎ **이 원형이 실전 상한**. 아래 "확정 원형" 참조 |
| 4분할 세로띠 | 얼굴 + 몸 가운데(애니) + 양옆(조각 2종) | ○ 가운데 띠가 좁아지기 쉬움 |
| 4분할 부위별 | 얼굴 + 몸통 + 왼팔·왼하체 + 오른팔·오른하체, 경계가 목·양어깨·배 아래를 따라감 | ○ 관절 기준이라 자연스러움 |
| 5분할 이상 | 세로 띠를 더 쪼갬 | × 띠가 좁아 재질이 안 보임 |

3분할 이상에서 재질을 이마리·재스퍼처럼 **설명이 긴 것**으로 바꾸면 전체 길이가 늘어 몸 형태가 무너지고 목 경계가 약해진다. 재질을 바꾸더라도 서술 길이는 원형과 같게 유지할 것 — 아래 "재질 서술 길이 제한" 참조.

#### 3분할 확정 원형 (najeon + 흰 대리석, 정면 서기)
반복 검증된 표준형. 약 650단어. 이 길이를 넘기지 않는다.

1. **한 줄 선언** — 얼굴은 실사, 좌우가 각각 애니/재질, 두 경계에서만 파편
2. **Subject** — 인물 서술 (미인 서술은 아래 14-4 참조)
3. **Body Art** — 기존 프리셋 짧은 형식 그대로: `Full body [재질] body painting on her bare skin from the collarbones to the ankles, ...` + `The pattern covers the entire bust densely with no open gaps, and wraps fully around the rear, the lower belly, the knees and the calves, covering them as densely as the chest.` (재질 설명을 별도로 안 늘림)
4. **Physique** — 끝에 `in drawing and in stone alike` 한 마디만
5. **The three territories** — 번호로 셋: 실사(머리·목), 애니(좌반신), 재질(우반신). `The two halves of the body are split near evenly down her centre. Each territory is one unbroken region, and none of the three appears anywhere inside another.`
6. **The living head** — 짧게 2줄
7. **The anime half** — 짧게 2줄
8. **The [재질] half** — `solid carved stone — hard, cold and heavy, with real weight in it` + 재질 핵심 특징 1~2개 + `Continuous tone throughout, shaded by real light falling across a three-dimensional object — no outline, no flat colour, no cel shadow anywhere on it` + `The same dense pattern continues there as shallow relief carving cut into the stone`. **도구 자국·채석 먼지 같은 부가 디테일은 넣지 않는다.**
9. **"Only the left half is drawn" 한 줄** — 나머지는 그림 요소가 없음을 못박음
10. **The first line — head to body** — 목·쇄골을 도는 지그재그, 목젖 아래로 파임
11. **The second line — anime to [재질]** — 목 밑에서 시작해 가슴 중앙→배 중앙으로 내려가다 **가장 아래 주름에서 소멸**. 가로 금지. 윤곽선이 경계에서 끊기고 재질이 이어받음
12. **"The two lines meet at the base of her throat" 한 줄** — 두 선이 만나는 지점 명시 (없으면 목 경계가 약해짐)
13. **The fragments** — 접점에만, 양쪽 성질 하나씩, 작고 촘촘→크고 성김→소멸. **재질별 특수 파단 디테일도 한 줄로 압축**

#### 재질 서술 길이 제한 (중요)
길이가 늘수록 몸 형태 왜곡, 목 경계 약화가 반복 확인됐다. 재질을 교체할 때 지킬 것:
- `The [재질] half:` 문단은 **3문장 이내**로: (물성 한 줄) + (핵심 시각 특징 한 줄) + (무광/유광·색 결론 한 줄)
- 파편 문단의 재질별 디테일도 **한 구절**로 (예: `showing a bright crystalline broken face`) — 문단을 새로 늘리지 않는다
- 이마리·재스퍼처럼 층이 많거나 설명이 필요한 재질은 이 제약 안에서 압축해서 쓸 것. 압축 없이 그대로 서술하면 실패한다 (아래 실패 사례 참조)

#### 얼굴 경계·파편
- 경계가 얼굴을 스치는 편이 낫다: 관자놀이 → 눈썹 바깥 → 눈꼬리(눈 자체는 피함) → 볼 바깥 → 턱선
- 파편을 **실사로 명시**하면 애니 느낌의 깨짐을 막을 수 있다:
  `the breaking itself is photographic — real broken edges with real depth and real shadow, not drawn` + `drawn pieces showing a raw torn edge where the flat colour simply ends with no ink line around the break itself` + `Each lifted piece casts a real photographic shadow with soft falloff`
- 받침이 있는 자세는 재질 쪽이 받침과 만나는 자리에 `stone meets stone`

#### 재질 확장 — 돌 밖으로
돌·나무·유리·금속 네 계열 안에서 짝지으면 안정적이다.

| 재질 | 판정 | 파단 방식 |
|---|---|---|
| 대리석·흑요석·비취·설화석고 등 돌 | ◎ | 결정면을 따라 깨짐, 덩어리(chunks) |
| **나무** (자단·흑단 등) | ◎ | 결을 따라 찢어짐, 섬유질 splinter |
| **유리** (주조) | ◎ | 조개껍질 모양 조가비 파단, 빛을 꺾음 |
| **은** | ◎ | 날카로운 금속 단면, 무거움 |
| 청동(녹) | ◎ | 깨진 단면에 금속 광택 |
| **밀랍** | ✕ | 실패. 무름이 형태를 무너뜨림 |
| **산호** | ✕ | 실패. 부서지기 쉬운 유기 조직이 형태를 무너뜨림 |
| **나무 + 흑요석 조합** | ✕ | 재질 각각은 성공하지만 이 둘을 같은 화면에 짝지으면 실패 — 대비가 너무 크거나 순서(좌우) 문제로 추정, 원인 미확정 |

- 재질 자체를 "새긴 게 아니라 그 자체가 재료"로 만들 때: `her whole body there is not carving applied to a surface — it is the surface: solid [재질], one continuous piece/mass from her shoulder to her toe, ... nothing added and nothing painted. There is no seam anywhere; the [재질] simply is her body.`
- 돌 계열 조합(예: 대리석+흑요석)이 나무나 특이 재질보다 안정적. 처음 시도하는 재질 조합은 돌끼리부터.

#### 자세 적합도
상체가 세워져 경계가 머리에서 세로로 내려갈 수 있어야 한다.

| 자세 | 판정 |
|---|---|
| 정면 서기 | ◎ 가장 안정 |
| 3/4 서기 | ◎ |
| 양 무릎 꿇기 (정면·3/4) | ◎ 배가 수직으로 늘어져 받침에 닿는다 |
| 걸터앉기 3/4 | ○ 좌우가 흐려지므로 부위별 배정을 꼼꼼히, 히프는 다리 쪽으로 |
| 기대고 앉기 | ○ 가로 3:2 |
| **쪼그려 앉기** | **△ 조건부 성공** — 무릎을 양옆으로 크게 밀고(`knees pushed right out to either side`) 배가 그 사이로 완전히 내려와야 함. 경계는 배 아랫면을 따라가게(허벅지를 가로지르지 않음) |
| 옆으로 눕기 | × 세로 분할이 성립하지 않음 |

#### 생성이 어려울 때
조건이 많아 실패가 잦다. 두 갈래로 나눌 것.
- **단계 분할**: 실사 한 장 먼저 → 첨부 + 한국어로 "오른쪽 몸 일부를 흰 대리석 조각으로 바꿔줘. 경계는 관자놀이에서 시작해 세로로 내려오다 허벅지에서 사라지게, 경계선에만 파편"
- **조건 감축**: 영역 배제와 가로 금지만 남기고 나머지를 뺀다
- **원형으로 복귀**: 실패가 반복되면 새 요소를 더하지 말고 검증된 원형(najeon+흰대리석)으로 되돌아가 재질 하나만 교체

**불채택**: 경계 없는 완전 그라데이션 / 파편만 흩뿌리기 / 큰 판이 경계에 오는 배치 / 실사+조각 나란히 서기 / 옆으로 눕기 / 밀랍 / 산호 / 나무+흑요석 조합

### 14-4. 얼굴 미인 서술 · 인종별 이목구비
3분할에서 얼굴이 유일한 실사 구간이라 이목구비가 또렷해야 화면을 잡아준다.

**실사**: `a strikingly beautiful woman with the refined features of a high fashion model — a flawless oval face, high sculpted cheekbones, a clean sharp jawline, large deep-set eyes, a straight elegant nose and full well-defined lips`
**애니**: `drawn as a beautiful anime heroine ... the polished face of a lead character in a high-budget production` — 조연이 아닌 주인공급 얼굴임을 지시

| 인종 | 이목구비 | 화장 |
|---|---|---|
| 인도 | 크고 깊은 아몬드 눈, 짙은 아치 눈썹 | 콜 라이너 + 빈디 + 붉은 립 |
| 중동 걸프 | 깊이 들어간 눈, 높은 콧대 | 콜 + 브론즈 섀도 + 누드 립 |
| 라틴 | 짙은 눈썹, 윤곽 뚜렷한 입술 | 윙라이너 + 테라코타 섀도 + 베리 립 |
| 일본 갸루 | 크고 둥근 눈, 살짝 그을린 피부 | 두꺼운 윙 아이라인, 짙은 속눈썹, 펄 섀도, 하이라이터 |

`The living head:` 문단에 화장이 실사로 어떻게 보이는지 한 줄 추가하면 좋다 (콜이 속눈썹 경계에서 번짐, 립글로스에 실제 반사 등).

한중일 아이돌 얼굴(14-2 참조)에 미인 서술을 더할 수도 있음.

---

## 6. 보류·불채택 업데이트

| 항목 | 상태 |
|---|---|
| 은입사 | **보류 해제** (보강안 `thick bright silver wire covering most of the surface` 합격) |
| 실사 텍스트 직접 생성 (극단 체형) | 보류 → 4단계 파이프라인으로 대체 |
| 3D 애니 렌더 | 보류 |
| 이레즈미 (애니) | 보류 (무네와리 중앙 띠 / 레오타드화) |
| 팔레흐 | 조건부 (메달리온 구성 경향, 부정문 사용 금지) |
| 천목 | 조건부 (재질 약함, 노출 이력) |
| 익스트림 페어 | 보완 필요 (가슴 축소, 정면 쪽 회전) |
| USSBBW 배 무릎까지 늘리기 | **불채택** (텍스트: 천 주름화 / 편집: 풍선화·천 자락화) |
| `apron` 단어 | **사용 금지** (앞치마·천 자락으로 해석) |
| 스모 | **검증 완료** (3-2 블록, 정면 + 가로 띠) |
| 머슬 USSBBW | **검증 완료** (정면 + 은입사). 3/4는 실사 근육 소실 |
| 톱헤비 애플 | △ (대비 약점, 임신 배 경향) — 우선순위 낮음 |
| 바스트 퀸 슬림 | **불채택** (정면 거부 / 3/4 재시도 잦음 / 실사 불가) |
| 흑백 필름 | **불채택** — 색이 없어 문양이 회색끼리 뭉개짐 |
| 시간 축(4D) 전반 | **불채택** — 정지 이미지의 한계 밖 |
| ↳ 연속 변화 한 화면(4단계 나열) | 불채택 — 인물마다 작아져 부피가 죽음 |
| ↳ 걷는 순간의 살 흔들림 | 불채택 — 한 장 안에서 움직임은 표현되지 않음 |
| ↳ 이중 노출(몸+기물/풍경) | 불채택 — 애니는 명암 계조가 없어 성립 안 되고 실사는 거부 |
| **다중 노출 겹침** | **채택** — 단, 프롬프트가 아니라 첨부 후 짧은 한국어 지시로 (7-7장) |
| 남성 체형 | **불채택** — 실사·애니·조각 모두 거부. 체급을 스모 선수급으로 낮추고 샅바를 입혀도 안 됨 |
| 실사+애니 / 실사+조각 혼합 | **조건부 채택** (14-3장) |
| 가슴 강조 계열의 사람 실사 변환 | 불가 → 조각상 변환 또는 애니 전용 |
| 어깨만 넓힌 텐트폴 | 불채택 (남성 실루엣) → 어깨·골반 동시 확장으로 수정 |
| 이레즈미(전신 문신) | **불채택** — 실사 생성 거부 |
| 청자 킨츠기 | **불채택**(실사) — 옅은 바탕 + 가는 선이라 문양이 흐려짐. 애니에서도 편차 컸음 |
| 란각 옻칠 · 다마스쿠스 강 · 흑요석 · 대모 · 라피스라줄리 | **불채택** — 결과 약함 |
| 장신구를 재질로 쓰기 (금·구슬·흑금·산호호박) | **불채택** — 옷처럼 보이고 살의 굴곡이 가려짐. 액세서리로만 사용 |
| 문양 없는 재질 (얼룩·질감만) | **불채택** — 빈 면이 넓으면 생성 거부. 문양을 얹으면 통과 |
| 유두 피어싱 | **불가** (노출 판정) |
| 이중턱 표현 (얼굴 프레임) | 불채택 — 남성적으로 읽힘 |
| 문양을 별도 축으로 분리 | **불채택** — 재질 안에 이미 문양이 있어 축을 늘릴 만큼 차이가 없음. 관리만 복잡해짐 |
| 임산부 변형 | **애니 채택** (11장). 실사는 미확인. **정면 불채택** — 배가 앞으로 나온 깊이가 안 보이고 롤에 가려짐, 3/4 전용 |
| 3D 렌더 (포토리얼·스타일라이즈드·무재질 클레이) | **불채택** (12-1장). 조각상 형식만 통과 |
| 잡지 커버 스타일 (프롬프트 직접) | **불채택** — 이미지 첨부 후 한국어 요청으로 |
| 3/4 + 동심원 문양 (둥근 배) | 비권장 (임신 배로 읽힘) |
| 완전한 조각상 (B 방향) | 별도 시리즈 후보로 보관 |
| 인종 다양화 | 추후 (피부 문장·재질 대비 재검증 필요) |

---

## 7. 다음 할 일

### 신규 생성기 (가장 큰 과제)
지금까지의 체형·재질·자세는 시행착오를 거친 최종판이다. 기존 수동 조합에 끼워 넣으면 엉키므로 **독립된 생성기**로 두기로 함 (가칭 `Living Artifact Studio`).

| 구분 | 축 |
|---|---|
| 주요 (항상 표시) | 체형 7 · 재질 15 · 자세 11 · 인종 6 · 연령 4 · 인원 2(솔로/듀오) · 출력 2(애니/실사) |
| 표면 (부피에 영향) | 신발 · 피부 광택(무광/은은/오일) |
| 장식 (기본 없음 또는 랜덤) | 헤어 · 네일 · 귀걸이 · 목걸이 · 팔찌 · 코걸이 · 피어싱 |

1. `core\data.py`에 생성기용 데이터 추가
2. 프롬프트 조립 함수 작성 — `patch_livingartifact_photo_json.py` / `photoduo_json.py`의 build() 로직이 거의 그대로 쓰인다
3. 문양은 재질 목록을 늘리는 방식으로 (예: "나전칠기", "나전칠기 · 바다") — 축을 늘리지 않음

### 결과 확인
4. Photo Direct 252개 · Photo Duo 168개 실제 생성 결과 확인 후 티어 부여
5. 애니 96~215번 실사(또는 조각상) 변환 후 티어 부여
6. 임산부 변형 실사 결과 확인

### Idol Duo/Solo · Mountain Mass 등록 완료 (v6.5: 결정 완료, 재작업 없음)
7-1. **등록 완료**: `🏺 Living Artifact · Idol Duo` 50개, `🏺 Living Artifact · Idol Solo` 124개 (commit `deb48d5`), `🏺 Living Artifact · Mountain Mass` 30개(솔로 20 · 듀오 10, 5,000lb, commit `7d6a384`). Idol Duo/Solo 인물 풀은 한국/일본/중국 아이돌 + 인도/중동 걸프/라틴 미인 + 실버폭스(흑인 제외, 무작위 혼합), 체형 9종 + 임산부 변형, 재질 14종, 피어싱류 액세서리 무작위.
7-2. **결정 (더 이상 할 일 아님)**: Idol Duo/Solo 174개에는 옛 띠 표현(`wide bands following the deep crease... like contour lines`, 13-2 참조로 이제 전면 폐지)이 남아 있어 옷처럼 보일 수 있으나, **기존 174개는 그대로 두고 재등록하지 않기로 결정**. 수정판 스크립트(`patch_livingartifact_idolduo_json.py` · `idolsolo_json.py`, 띠 표현 제거됨)는 로컬에 남아 있지만 실행하지 않는다. **앞으로 이 두 카테고리에 새로 추가할 때만** 수정판 규칙(띠 없음)을 따른다.
7-3. **결정 (더 이상 할 일 아님)**: Mountain Mass의 5,000파운드 규칙(13-6~13-11)은 Idol Duo/Solo(1,000~1,500lb)에 통합하지 않는다. 두 무게 체계는 별도 카테고리로 유지.

### 애니 듀오 확장
7-4. 기존 Anime Duo 50개는 **구 5체형 기준**. 신규 6체형(애슬리트 USSBBW · 콜로설 · 텐트폴 · 아워글래스 USSBBW · 톱헤비 아워글래스 · 바스트 퀸 BBW)으로 21쌍 신규 작성 검토
7-5. 실사 듀오에서 온 것을 애니 듀오에도 적용: 몸끼리 눌림, 화면 배치 명시, 걸터앉기·나란히 기대기 자세, 가로 3:2 (기존 애니 듀오는 서 있는 자세 위주)

### 조각상
8. **Sculpture 솔로 42 · 듀오 42 검증 후 등록 결정** (12-6장). 통과하면 `--write-presets`로 JSON 생성 → 메타 → 커밋
9. 검증 결과에 따라 재질 확대 (13종 중 2종만 작성된 상태)
10. 회화 장르 결과 확인 후 채택분 정리 (아르누보 채택, 나머지 7종 대기)

### v4에서 이월
11. 트리오 2차 결과 확인 → 트리오·쿼르텟 스크립트화
12. `core\data.py` 체형 옵션 교체 (머슬 BBW → 헤비 머슬)
13. `preset_builders/presets_la_anime_19_50/` 중복 폴더 삭제 권장

---

## 15. 재질 트랙 재개 (v6.6, 2026-10-03)

> v6.6 수정 사항: 돌출형 재질 "크리스탈"로 통합(10색), "비늘(Scale)" 동물타입 5종 통합(코드 등록 완료), 수조(T2) 색상 그라데이션 2~4색·무지개 재검증, 듀얼바디 비대칭 다리 첫 테스트, 금박·스테인드글라스 자유축(바디페인팅) 이동 시도 및 폐기, 헤어스타일 31종·헤어컬러 30종 신규 축 추가(바디페인팅·임산부·재질 전체 공용), **프레임 체계 용어 혼선 기록**(아래 15-7 참조— 본 문서 10-5장의 "부위별 프레임"과 이후 세션에서 쓰인 "프레임 6단계/데미스탯"은 서로 다른 체계일 가능성이 있으며, 확인 중)

> **주의**: 이 섹션은 본 문서(v6.5, 2026-09-23)와 **약 10일 공백 이후**, 다른 대화창에서 진행된 작업을 정리한 것. 재질 트랙에 집중했고, 실사/애니/조각상 파이프라인(1~14장)은 이번 공백 동안 다루지 않음 — 1~14장 내용은 변경 없이 그대로 유효함.

### 15-1. 크리스탈 — 돌출형 재질 통합 (얼음/서리 + 지오드)

기존에 별도로 테스트하던 "얼음/서리 결정"과 "지오드(크리스털 군집)"가 사실상 같은 구조(피부를 뚫고 돋아난 결정, 개별 단차+그림자)였음을 확인하고 하나의 재질 "크리스탈"로 통합. 색상을 독립 축으로 분리해 10종 확정:

```
아이스블루 · 로즈쿼츠핑크 · 자수정바이올렛 · 시트린옐로우 · 에메랄드그린 ·
스모키그레이 · 사파이어블루 · 루비레드 · 토파즈오렌지 · 클리어화이트
```

**재질 서술 원형**:
```
full body [색상명] crystal clusters growing directly out of her own skin
covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION, both legs
FULLY covered to ankles, NO bare skin below neck ANYWHERE — this is not a
garment, not jewelry, not a printed pattern, every crystal point erupting
outward from beneath the surface of her living skin in true three-dimensional
relief, each facet catching its own individual glint and casting its own
small hard shadow onto the skin and onto neighbouring crystals, nothing lying
flat. Dense overlapping clusters — BLAZING [색1] crystal points erupting
across the full torso both legs neck to ankle, VIVID [색2] mineral veins
and undertone glinting through the thinnest points filling every remaining
gap with real depth and texture, each facet sharply faceted and distinct,
NO airbrush NO gradient wash, NO flat printed surface anywhere.
```

듀오2+트리오2(10명)에 10색 전부 배정해 성공 확인. 등록은 보류 중(필요시 진행 — 90개 분량: 솔로30·듀오30·트리오30, `la_crystal_{type}_{번호}`로 실제 등록 완료됨, 카테고리 "🏺 Living Artifact · Crystal Formula").

### 15-2. 비늘(Scale) — 동물타입 5종 통합

나비날개·코이(물고기)·뱀·드래곤·인어를 하나의 "비늘" 재질로 묶고, 동물별 전용 모양 묘사를 코드에 등록(`full_dicts.py`의 `SCALE_ANIMAL_DB`):

| 동물 | 모양 묘사 | 색상 팔레트(일부) |
|---|---|---|
| 나비날개 | 미세한 가루 같은, 기와처럼 겹침 | 블루/블랙, 에메랄드/골드, 바이올렛/마젠타 |
| 코이 | 둥글고 매끈, 성장선 있음 | 크림슨/펄화이트, 블루/오렌지, 골드/플래티넘 |
| 뱀 | 다이아몬드꼴 각진 | 에메랄드/제이드, 브론즈/블랙, 골드/아이보리 |
| 드래곤 | 크고 두꺼운 갑옷판 | 레드/엠버, 골드/앰버, 에메랄드/제이드, 사파이어/코발트, 블랙/퍼플, 실버/페일블루 |
| 인어 | 섬세하고 작음, 무지개빛 | 틸/실버, 바이올렛/펄, 시안/골드 |

**재질 서술 원형**:
```
her own skin itself covered in [모양 묘사] covering EVERY inch of skin from
neck to ankle WITHOUT EXCEPTION, both legs FULLY covered to ankles, NO bare
skin below neck ANYWHERE — this is not fabric, not a garment, not a printed
pattern, this is the real cellular structure of her own skin, each scale
casting its own small shadow on the scales beneath it, nothing lying flat
as one smooth sheet. Dense overlapping fields — BLAZING [색1] scale
formations shifting across the full torso both legs neck to ankle, VIVID
[색2] scale-edge detail filling every remaining gap with real texture,
NO airbrush NO gradient wash, NO flat printed surface anywhere.
```

**중요 — 실명 품종 금지**: 코이를 "코하쿠·쇼와·오곤" 같은 실존 품종명으로 구체화하면 반복 실패(품종명이 기모노·프린트 직물 디자인으로 유명해 "옷"으로 연상되는 것으로 추정). 뭉뚱그린 "iridescent koi-fish scales"처럼 동물명만 쓸 것.

**주황+빨강 조합 주의**: 뱀의 콘스네이크(오렌지/크림슨)만 체형 무관하게 반복 실패 — 애니멀프린트 패션에 흔한 색 조합이라 "옷"으로 더 쉽게 연상되는 것으로 추정. 코이의 골드/브론즈/브라운 계열도 약한 편. 다른 동물(드래곤의 레드/골드 등)은 괜찮았음 — 색 하나만으론 설명 안 되고 "따뜻한 색 전체"가 위험한 건 아닌 것으로 보이나 확신은 낮음.

**환경**: 이레즈미와 반대로 밝은 야외/실내 환경에서도 안정적(검정 배경 고정 불필요) — 구조색(빛을 받아야 발색) 재질이라 빛이 많을수록 유리한 것으로 추정.

**공작 깃털눈무늬**는 구조가 달라(개별 비늘이 아니라 눈 모양 반복 패턴) 비늘 통합에 넣지 않고 별도 취급. 퀸텟 테스트(나비→코이→드래곤→인어→공작 순서)에서 성공 확인했으나 별도 등록은 안 함.

등록 완료: 솔로30·듀오30·트리오30(`la_scale_{type}_{번호}`, 카테고리 "🏺 Living Artifact · Scale Formula").

### 15-3. 흑요암+금빛 이음새 — 고정 1종 유지

```
full body polished obsidian stone fused directly to her own form covering
EVERY inch of skin from neck to ankle WITHOUT EXCEPTION, both legs FULLY
covered to ankles, NO bare skin below neck ANYWHERE — this is not a garment,
not jewelry, not a printed pattern, this is solid glossy black stone curving
to follow her body's true three-dimensional shape, with molten gold seams
running between dozens of fitted stone sections, each seam standing in a
thin raised ridge catching its own bright glint and casting its own small
shadow, nothing lying flat. Dense fitted sections — BLAZING glossy jet-black
obsidian surface across the full torso both legs neck to ankle, VIVID MOLTEN
GOLD seams branching and converging densely with no plain stone section left
ungilded, NO airbrush NO gradient wash, NO flat printed surface anywhere.
```

돌 색상·이음새 금속색을 다양화하는 안을 검토했으나, **킨츠기(도자기+금)와 컨셉이 겹쳐** 확장하지 않고 고정 1종으로 유지하기로 결정. 등록 완료: 솔로20·듀오20·트리오20(`la_obsidian_{type}_{번호}`, 카테고리 "🏺 Living Artifact · Obsidian Gold Formula").

### 15-4. 왁스(촛농) — 3색 고정

```
full body molten wax flowing and set directly over her own skin covering
EVERY inch of skin from neck to ankle WITHOUT EXCEPTION, both legs FULLY
covered to ankles, NO bare skin below neck ANYWHERE — this is not a garment,
not a printed pattern, this is real wax that has flowed down every curve
and hardened in place, each drip and pooled ridge standing in true
three-dimensional relief, casting its own small soft shadow, nothing lying
flat. Dense flowing drips — BLAZING [색1] molten wax streams pooling and
hardening across the full torso both legs neck to ankle, VIVID [색2]
translucent drip-ridges catching the light filling every remaining gap with
real depth and texture, each ridge glossy and rounded exactly like real set
wax, NO airbrush NO gradient wash, NO flat printed surface anywhere.
```

색 팔레트 3종: 크림슨/앰버 · 에메랄드/골드 · 바이올렛/로즈. 등록 완료: 솔로20·듀오20·트리오20(`la_wax_{type}_{번호}`, 카테고리 "🏺 Living Artifact · Wax Formula").

### 15-5. 수조(T2) 색상 그라데이션 재검증

기존 메모(9-4장 이전 버전, 백로그)에서 "다색 그라데이션은 추후 과제"로 남겨뒀던 것을 재개.

**기본 구조**: 전신 프레임, 투명 유리 수조, 발목~허리선까지 액체로 채움(허리선 위는 빈 유리). 아래는 4색 예시:
```
Body: Below the collarbones, her entire body is a single continuous vessel
of clear cast glass, the same glass shaping every curve of her form with
no seam anywhere. From her ankles up to her waistline, the glass vessel is
filled with liquid in four distinct horizontal colour bands, vivid and
highly saturated, each band blending into the next only at its own narrow
edge — a BLAZING ELECTRIC CRIMSON at the ankles, rising through a VIVID
ELECTRIC EMERALD at the calves and knee, then a BLAZING ELECTRIC COBALT BLUE
at the thigh and hip, and finishing in a VIVID ELECTRIC MAGENTA at the
waistline, every colour strong and pure rather than muted, the colours
visible through the clear glass exactly like a layered parfait. Above the
waistline to her collarbones, the glass is simply empty, clear, and
transparent, with nothing inside.
```

**결과**:
| 색 개수 | 결과 |
|---|---|
| 2색 | 안정적(100% 성공, 반복 확인) |
| 3색 | 안정적 |
| 4색 | 성공·실패 혼재(케바케) |
| 무지개(7색) | 자연스럽게 섞임, 성공 |

**색 표현 방식(차분한 색명 vs BLAZING/ELECTRIC 강조어)과 경계 섞임 정도의 관계**: 처음엔 "차분한 색명=자연스럽게 섞임, 강렬한 강조어=경계 뚜렷"으로 보였으나, 반복 시도에서 뒤집히는 경우가 나와 **확정된 규칙은 아님**(케바케). 성공률 자체도 차분/강렬 두 방식 사이에 뚜렷한 차이 없음 — 오늘 전체에서 반복된 "같은 공식도 매번 들쭉날쭉" 패턴과 일치.

**듀오가 솔로보다 안정적**이었던 경향 있음(표본 적어 확정은 아님).

밝은 야외(황혼녘 초원 등)가 투명재질 전반의 기본 환경으로 재확인.

### 15-6. 듀얼바디 — 비대칭 다리 프레임 (첫 테스트)

사용자 기억으로는 과거(아마 v6.5 이후, 또는 더 이전) "한쪽 다리는 힙컷, 한쪽 다리는 쓰리쿼터"처럼 좌우 다리가 서로 다른 프레임 레벨을 갖는 "듀얼바디(L0~L4)"를 여러 번 테스트했다고 하나, **이번 대화에서 과거 세션 검색으로 정확히 일치하는 프롬프트를 찾지 못함**. 본 문서(v6.5)에도 "듀얼바디" 관련 섹션이 없음.

이번 공백 동안 처음으로 "왼쪽 다리=힙부터 전부 유리, 오른쪽 다리=무릎 위부터만 유리(그 아래는 실사)"로 좌우 비대칭 절단선을 둔 솔로 1건을 테스트. 구조:
```
Body: Her two legs are deliberately asymmetric in how far the glass
extends. Her LEFT leg is glass from the hip all the way down... Her RIGHT
leg stays real skin down past the knee — only from a point above her right
knee down to the ankle does the glass begin...
```
결과 미확인(사용자 피드백 받기 전 대화 주제가 전환됨). **듀얼바디 L0~L4의 정확한 원래 정의는 여전히 미확인 상태** — 과거 핸드오프 파일 중 이 문서보다 더 최신 버전이 있다면 거기 기록되어 있을 가능성.

### 15-7. 프레임 체계 용어 혼선 — 기록만 해둠

이번 공백 동안 "프레임 6단계(허리컷·힙컷·데미스탯·쓰리쿼터·앵클컷·전신)"이라는 용어를 사용자가 언급했고, Claude는 이를 "그 지점에서 조각 자체가 끝남(카메라 크롭 아님)"이라는 의미로 이해·정정했음. 그러나 **본 문서(v6.5) 10-5장의 "부위별 프레임"은 상체/배꼽/히프/얼굴/얼굴+목으로 이름 체계가 다르고, 명시적으로 "카메라 프레이밍(크롭)"을 의미함**(`Framing:` 문단, 조리개 수치 지정 등).

**두 체계가 동일한 것인지, 서로 다른 세션에서 만들어진 별개 체계인지 확인되지 않음.** "데미스탯"이라는 이름 자체는 09-28 Glass Face 세션(본 문서보다 5일 뒤, 별도 대화)에서 "머리~무릎 위 절단, 조각 자체가 끝남" 의미로 쓰인 기록이 메모리에 남아 있어, 아마 **v6.5 이후 다른 세션에서 새로 정의된 체계**로 추정되나 확정은 아님. 추후 해당 세션 기록을 더 찾아 확인 필요.

### 15-8. 금박·스테인드글라스 — 자유축(바디페인팅) 이동 시도 및 폐기

맥시멀리스트 전용이던 금박·스테인드글라스를 차분한 바디페인팅 템플릿으로 옮기는 시도. 처음 일부 성공해 "이동 가능"으로 판단했으나, 추가 테스트(다른 체형·듀오)에서 외부 생성기가 "sexually explicit content" 거부를 간헐적으로 반복. 같은 인물(체형·메이크업·포즈 전부 동일)에서 Body Art만 금박→기존 공예(터키 이즈닉)로 교체하자 즉시 성공해, 거부 원인이 **재질 자체**임을 확정. 스테인드글라스도 같은 패턴(동일 공식인데 체형 조합에 따라 성공/실패 혼재) 확인. **결론: 둘 다 바디페인팅 이동 폐기, 맥시멀리스트 전용 유지**로 완전히 마무리.

대신 "맥시멀리스트 틀(ALL CAPS+강한 커버리지 반복+검정배경)은 그대로 두고 피부톤 문장만 교체"하는 시도는 성공 — 금박·스테인드글라스·이레즈미·보태니컬은 포셀린/올리브/아이보리/브론즈 등 다양한 피부톤으로 교체해도 안정적. UV네온만 브론즈(탄) 피부에서 실패(발광 효과가 어두운 피부와 구조적으로 얽혀있는 것으로 추정). 실제 등록 축 추가는 보류.

### 15-9. 신규 공용 축 — 헤어스타일 31종 · 헤어컬러 30종

기존 바디페인팅·임산부 트랙에 헤어스타일 축이 8종뿐이었던 것을 23종 추가해 31종으로 확장(흑인 헤어 전통 스타일 다수 포함: 아프로·락스·콘로우·반투노트 등). 헤어컬러는 기존에 전혀 없던 축이라 30종 신규 생성(제트블랙~비비드 계열~파스텔 계열). 둘 다 `tracker.py`/`full_dicts.py`에 정식 등록, 바디페인팅·임산부·재질 트랙 전체에 기본 랜덤 축으로 적용됨. "무난한 10종" 서브셋도 각각 지정(일상적으로 안 튀는 조합만 쓰고 싶을 때 사용).

### 15-10. 이 공백 동안 등록된 Living Artifact 카테고리 (요약)

본 문서 마지막 등록 현황(0장, 총 1,131개) 이후 진행된 주요 등록들 — 상세 프롬프트 공식은 각 소절 참조, 카테고리/키는 아래:

| 카테고리 | 개수 | 키 접두어 |
|---|---|---|
| Core Formula(바디페인팅, 전 인원대) | 700 | `la_core_` |
| Pregnant Formula(임산부) | 950(일반 혼합 포함) | `la_preg_` / `la_mixed_` |
| Irezumi / UV Neon / Stained Glass / Gold Leaf / Botanical Formula | 각 300 | `la_irezumi_` 등 |
| Mixed-Track Formula(7트랙 랜덤) | 270 | `la_mixed7_` |
| Fixed Combo / Random Combo Formula | 210/120 | `la_mix3_` / `la_mixedrand_` |
| Crystal / Scale Formula | 각 90 | `la_crystal_` / `la_scale_` |
| Wax / Obsidian Gold Formula | 각 60 | `la_wax_` / `la_obsidian_` |

맥시멀리스트 5종(이레즈미·UV네온·스테인드글라스·금박·보태니컬)의 상세 원문 공식·실패 재질 목록(홀로그래픽·코스믹·헤나·하이다 등)은 메모리(`/areas/luminex.md`)에 기록되어 있으며 이 문서엔 중복 기재하지 않음.

### 15-11. 다음 할 일 (이어서)

1. 듀얼바디(L0~L4) 원래 정의 재확인 — 더 최신 핸드오프 파일이 있는지 확인
2. 프레임 체계(15-7) 용어 정리 — 어느 세션에서 "프레임 6단계/데미스탯"이 정의됐는지 확인
3. 수조 비대칭(15-6) 결과 확인 후 필요시 듀얼바디 축 정식화
4. 크리스탈·비늘·왁스·흑요암금 — 이미 등록 완료(15-10 참조), 생성 검증 후 티어 부여
5. 코이·드래곤 전용 색상 세분화(품종명 아닌 색상만) 검토 — 미착수

---

## 16. 바디페인팅 Core Formula (일반 트랙, v6.5 이후 전체 재정비)

v6.5(1~14장)의 애니→실사 파이프라인과는 별개로, **차분한 서술형 바디페인팅 트랙**을 처음부터 다시 확립. 검증 성공 사례를 기준으로 삼은 "북엔드 구조" 포맷:

**문단 순서**: 첫 줄 `Image format: a vertical portrait-orientation photograph, 2:3 aspect ratio` 선언 → 중형 카메라·85mm·f/8·단측광 카메라 문단 → **Subject**(국적·연령·피부톤, "얼굴이 몸과 정확히 같은 톤" 문장 포함) → **Physique**(몸무게 수치+부위별 처짐·주름 개수·방향 묘사+"not pregnant" 명시+"손발은 서로 정상 비례 유지"+"~이 아니다" 부정 대조) → 별도 **Skin** 문단(사실적 모공·질감, 일러스트/CG 아님 재차 명시) → **Body Art**(전통 공예명+턱 아래 전신 부위별 나열식 커버리지+"물감이 살에 얹힌 것" 명시+얼굴은 안 칠함) → **Pose** → **Footwear**(인치수 대신 "발목뼈보다 훨씬 높은, 일반 힐의 3배 두께" 식 생생한 묘사) → 짧은 **Background & Lighting** → 마지막 줄에 첫 줄 형식 선언 재반복.

배경은 칠흑 void가 아니라 `plain seamless mid-grey/deep-charcoal backdrop`.

**생성 실패 원인 확인**: 체형을 딕셔너리 한 줄 요약으로 축약하면 체형이 평균화됨 — 검증된 공식을 그대로 복원해야 재현됨.

### 16-1. 전체 축 최종 확정

**메이크업 48종**: 기존 34종 + 페르시안글램·레바논웨딩글램·걸프아바야글램·파키스탄브라이덜글램·우즈벡실크로드글램·자메이카댄스홀글램·하와이안훌라·스페인플라멩코글램 8종 + Bollywood Glam(India)·Carnival Glam(Brazil)·Ao Dai Glam(Vietnam)·Turkish Glam(Turkey)·German Glam(Germany)·Egyptian Glam(Egypt) 6종. 로리타갸루·인형메이크업·브리티시모드 3종은 "doll" 위험 단어 포함으로 제외.

**체형 14종**: 글래머아워글래스·머슬아워글래스BBW·헤비머슬·USSBBW·아워글래스SSBBW·파워리프터·아마조네스·슈퍼글래머·블랙글래머·레전드바스트·커브드바스트·브라질부티글램·폴리네시안여신·누비안부티빌더. 각 체형 상세 물리 묘사(몸무게+부위별 처짐/근육+부정대조+비례고정) 확정 보유.

**포즈 19종**: 정면와이드스탠스·한쪽무릎꿇기·3/4각도·옆모습·뒷모습3/4·걷는동작·벽에기대기·의자앉기·바닥옆으로기대기·양팔위로·허리손·머리넘기기·런지자세·완전뒷모습·창가기대기·계단에앉기·얼굴감싸기·점프동작·양무릎꿇고정면.

**신발 24종**: 플랫폼 18종 + 논플랫폼 6종(순수스틸레토펌프스·발레힐·니들힐·싸이하이스틸레토부츠·스컬프처럴힐·앵클스트랩스틸레토). 신발 강조문구는 "발목뼈보다 훨씬 높은, 일반 힐의 3배 두께".

**공예 패턴 40종**: 39종("[국가] [기법명]" 형식 통일) + 마키에(일본 금가루 옻칠, 40번째 추가). 공예 5종(HungarianKalocsa·FilipinoYakan·PeruvianNazca·CroatianHvar·EthiopianCrossLattice)이 embroidery/weaving/textile/lace/weave 등 천 연상 단어를 포함해 옷처럼 렌더링되는 원인이었음 — "painted pattern/painted motif" 계열로 전부 교체.

**배경**: 무제한(스튜디오 4색+실내외 다양) — 공예 패턴과는 별개 축.

### 16-2. 그룹샷 길이 규칙

1~6인은 풀디테일 포맷(Subject/Physique/Skin/Body Art 등 문단 전개) 그대로 — 6인(섹스텟) 평균 1912단어까지 안정적. 7인 이상은 풀디테일이 인당 비용 급증(10인 3111~3148단어)해 재시도 多 — "하이브리드" 전환: 체형 문장만 BODY_FULL(풀버전) 유지, 나머지(메이크업·공예·포즈·신발)는 `[메이크업 / 체형]` 라벨+압축 태그 포맷(8인 기준 완전압축 1229·하이브리드 1842·풀디테일 2476단어).

**11인 이상 한계**: 인원수가 요청과 다르게 생성되는 문제(11인→12인, 13인이 한 줄로 안 서는 등). 11인은 재시도하면 대체로 정상, 12인부터 편차 커짐. 체형도 BODY_SHORT로 줄이고 `Exactly N women` 문구 두 번 추가한 압축포맷으로 전환 — 11~14인은 이 압축포맷 기준.

### 16-3. 등록 현황
Core Formula 총 700개(1~14인 전체, 1~10인 하이브리드/풀디테일, 11~14인 압축) — 키 `la_core_{type}_{번호}`.

---

## 17. 임산부 트랙 — 융합형

**체형 13종**: 임산부글래머·임산부콜로설·임산부풀텀트윈즈·임산부USSBBW·임산부아워글래스SSBBW·임산부슈퍼글래머·임산부블랙글래머·임산부레전드바스트·임산부커브드바스트·임산부브라질부티글램·임산부폴리네시안여신·임산부누비안부티빌더·임산부아마조네스. 헤비머슬·파워리프터는 배와 근육 동시표현이 반복 실패해 제외. 머슬아워글래스BBW는 선 자세만 안정적(무릎꿇기 실패).

**핵심 발견**: 체형 분리형(Subject/Physique/Skin/Body Art 문단) 포맷은 13종 중 1종만 성공할 만큼 불안정. **"융합형"**(한 문단으로 융합, 배를 패턴의 중심부로 지정, 포즈가 배/가슴을 직접 감싸거나 떠받치는 동작, Skin 전용문단 삭제, 부정문 최소화) 구조로 전환하자 성공률 대폭 상승 — 13종 전체+피어싱3단계+쥬얼리2단계+익스트림신발+헤어·나이·분위기 포함해도 거의 매번 성공.

배 강조 문구:
```
larger and more dramatically rounded than an ordinary full-term pregnancy,
projecting forward well beyond the line of her own chest
```
추가해도 대부분 체형 안정적, 레전드바스트(가슴+배 동시 강조)만 재시도 필요.

**그룹샷 전체 검증**: 솔로~5인(혼합 포함)·쿼르텟·퀸텟·6~8인(혼합·전원임산부) 전부 안정적 — 6~8인 길이 2000~2600단어로 일반 바디페인팅의 "7인 이상 압축 필요" 기준 넘지만 융합형 자체가 이미 압축적이라 압축 전환 불필요.

**10·12·14인(총36명) 한계 테스트**: 길이 3179~4531단어임에도 36명 중 35명(97%) 성공 — 임산부 트랙은 인원수·길이 무관하게 전 구간 압축 없이 융합형 그대로 사용 확정.

등록: Pregnant Formula 500 + Mixed(일반+임산부 혼합) 450 = 950개. 키 `la_preg_` / `la_mixed_`.

---

## 18. 맥시멀리스트 그룹 (이레즈미·UV네온·스테인드글라스·금박·보태니컬)

### 18-1. 공통 문법 — "HOF 맥시멀리스트"

과거 트랜스크립트에서 찾은 실제 HOF 등록 프롬프트 구조를 그대로 재현:
- ALL CAPS 반복 강조
- `THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky`
- `THE MOST EXTREME PHYSICALLY POSSIBLE`
- 순수 검정 배경 `MANDATORY pure pitch black void background`
- `Extreme high-gloss oil` 피부 마감
- 동적 힙팝 포즈
- `most extreme [체형] silhouette ever displayed` 마무리

**중요한 발견**: 맥시멀리스트 축은 바디페인팅·임산부처럼 자유롭게 축(신발·네일·피어싱·쥬얼리·체형·메이크업·포즈·헤어)을 섞는 방식이 근본적으로 안 맞음 — 신발·네일·피어싱·쥬얼리 4개 전부 추가 시 듀오만 성공(솔로·트리오 실패), 체형·메이크업·포즈·헤어까지 교체한 버전은 전부 실패. **검증된 원문을 한 글자도 바꾸지 않고 그대로 사용**하는 것으로 확정.

**배경 실험(이레즈미)**: 순수 검정 배경은 솔로~10인 14개 중 11개 1회 성공(79%). 같은 체형·문양·강조어법을 유지하고 배경만 환경(석조회랑·야외광장·박물관홀 등)으로 바꾸면 솔로~퀸텟 5개 중 1개만 성공(20%), 의상화·완전실패 다수. 검정 배경이 "피부·잉크·체형 집중"에 핵심적 역할 — 환경이 들어가면 모델이 "장소에 맞는 복장" 연상을 끌고 옴.

**UV네온**: 발광 효과 성립에 검정 배경+블랙라이트 조명(`UV blacklight illumination only — zero white light`)이 이레즈미보다 더 필수적(선택 아닌 구조적 전제조건).

**피부톤 교체**: 맥시멀리스트 틀(ALL CAPS+강한 반복+검정배경)은 그대로 두고 피부톤 문장만 교체하는 건 성공 — 금박·스테인드글라스·이레즈미·보태니컬은 포셀린/올리브/아이보리/브론즈로 교체해도 안정적. UV네온만 브론즈(탄) 피부에서 실패(발광 로직이 어두운 피부와 구조적으로 얽힌 것으로 추정). 등록 축 추가는 보류 중.

### 18-2. 이레즈미 — 문양 풀 26종

6종(기본) + 20종(신규: tiger·hannya mask·fudo myo-o flames·shishi lion-dog·great wave·bamboo forest·iris field·lotus pond·butterfly swarm·pine and crane·water dragon·phoenix solo·temple bell dragon·firefly night·orchid·oni demon mask·tengu feathers·raijin thunder drums·autumn maple storm·koi waterfall climb) = 26종.

```
THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker
than night sky, [나이] goddess, [체형명] physique THE MOST EXTREME
PHYSICALLY POSSIBLE beyond all anatomy limits — [체형상세], [헤어] — full
body [문양명] irezumi covering EVERY inch of skin from neck to ankle
WITHOUT EXCEPTION, both legs FULLY covered to ankles, NO bare skin below
neck ANYWHERE. Bold black ink outlines — [문양잉크상세], NO airbrush NO
gradient wash. Pose: [포즈] — most extreme [체형명] silhouette ever
displayed. Footwear: platform boots 8 inch, extra long stiletto nails to
match.

MANDATORY pure pitch black void background only, absolutely NO studio
backdrop NO texture NO grey NO gradient. Extreme high-gloss oil. 2:3
vertical 8K portrait.
```

### 18-3. UV네온 — 문양 풀 27종

7종(기본) + 20종(신규: aurora curtain·jellyfish bioluminescence·DNA helix·circuit traces·plasma vortex·solar flare·meteor shower·glowing coral reef·electric vein network·supernova burst·magnetic field lines·bioluminescent wave·nebula birth cluster·radio pulse rings·ion storm·geyser plasma eruption·resonance web·event horizon tunnel·fractal energy burst·firefly swarm) = 27종.

이레즈미 구조와 동일하되 `UV neon [문양명] bodypaint` + `Under her own dedicated UV blacklight spot, zero white light reaching her specifically` + `UV blacklight illumination only — zero white light` 배경 지시 추가.

### 18-4. 스테인드글라스

```
full body stained glass covering EVERY inch of skin from neck to ankle
WITHOUT EXCEPTION ... this is solid thick glass fused directly to her
form, not a garment, made of hundreds of small individual panes each no
larger than a coin, densely packed edge to edge, never large sheets, each
tiny pane curving to follow her body's true shape with real physical
thickness, dark lead-line seams webbing between every pane, each seam
standing in a small raised ridge casting its own shadow, never flat.
BLAZING [색1] and VIVID [색2] panes alternating in a dense irregular
mosaic, bright light passing through each tiny pane with sharp refraction
glints, NO airbrush NO gradient wash.
```
"수백 개 동전 크기 모자이크" 명시가 필수 — 큰 판이면 유니폼처럼 보임.

### 18-5. 금박

```
full body applied [색1] leaf covering EVERY inch of skin from neck to
ankle WITHOUT EXCEPTION ... Thin irregular metallic sheets — BLAZING
[색1] leaf with fine natural creases and overlapping seams, VIVID [색2]
undertone glinting through the thinnest points, a soft warm metallic
sheen filling every gap, NO airbrush NO gradient wash.
```
**교훈**: 스테인드글라스에서 효과 봤던 "실제 두께·곡면·단차+부정문 보강"을 그대로 적용하면 오히려 전부 실패 — 원래 성공했던 짧고 간결한 원문(부정문은 `NO airbrush NO gradient wash` 한 번만)으로 되돌리면 재성공. 재질마다 보강 공식이 똑같이 안 통함, 부정문 과다 반복이 역효과 가능성(가설).

### 18-6. 보태니컬

```
full body living [꽃이름] growing directly from her own skin covering
EVERY inch of skin from neck to ankle WITHOUT EXCEPTION ... this is not
a garment, not a printed pattern, not a dress, every stem rooted directly
into her living skin and every petal standing up in true three-dimensional
relief casting its own small shadow, nothing lying flat. BLAZING [색1]
[꽃이름] blossoms in full three-dimensional bloom, VIVID [색2] leaves and
curling tendrils filling every remaining gap with real depth and texture,
NO airbrush NO gradient wash, NO flat printed surface anywhere.
```
"이건 옷도 프린트도 드레스도 아니다, 모든 줄기가 살에 뿌리내렸고 모든 꽃잎이 입체로 솟아 그림자를 드리운다"는 보강 문구(+신발·네일까지 "진짜 꽃이 자라난" 일관성)로 성공.

### 18-7. 전용 포맷 (맥시멀리스트 그룹 밖)

**킨츠기**: 표준 차분한 템플릿 3/3 실패. 실제 성공은 피부톤·체형만 맥시멀리스트+BODY_FULL 상세체형을 쓰는 별도 "Signature" 전용 공식에서만 됨 — 리스크 때문에 공예 랜덤 풀에는 안 넣음, 필요시 수동 포맷으로만 사용.

**몰튼메탈(리퀴드골드/실버)**: 과거 원문은 이레즈미식 ALL CAPS가 아니라 제3의 "럭셔리 에디토리얼" 스타일(간결한 피부톤 한 문장+차분한 체형 묘사, `WITHOUT EXCEPTION` 등 반복강조 없음, `Studio beauty lighting...luxury cosmetics campaign...minimalist composition`으로 마무리). 표준 차분한 템플릿으로는 2/2 실패 — 킨츠기와 같은 패턴. "럭셔리 에디토리얼" 전용 포맷으로만 수동 사용.

### 18-8. 등록 현황
맥시멀리스트 5종(이레즈미·UV네온·스테인드글라스·금박·보태니컬) 각 300개(솔로~데켓 각 30개) = 1,500개. 키 `la_irezumi_` / `la_uvneon_` / `la_stainedglass_` / `la_goldleaf_` / `la_botanical_`.

---

## 19. 다트랙 혼합 체계

**원칙**: "맥시멀리스트는 축을 안 섞는다"는 "한 사람 안에서" 섞는 것에 한정 — "여러 사람이 각자 다른 트랙을 유지한 채 한 이미지에 공존"하는 건 별개로 가능. 각 인물이 자기 트랙의 검증된 구조만 유지하면 몇 명이든(7인까지 검증) 섞을 수 있음. 배경은 맥시멀리스트 요구(순수 검정)로 통일.

**4트랙 쿼르텟** 검증(바디페인팅·임산부·이레즈미·금박): 전부 1회 성공.
**7트랙 셉텟** 검증(전체): 2개 생성, 둘 다 성공(일부 디테일 애매함은 있었음). UV네온은 "자신만의 전용 블랙라이트 스팟, 나머지는 공통 하드키라이트"로 조명 충돌 절충.

### 19-1. Mixed-Track Formula (7트랙 랜덤조합)
듀오~데켓(2~10인) 각 30개 = 270개. 키 `la_mixed7_{type}_{번호}`.

### 19-2. Fixed Combo / Random Combo Formula
**고정조합 7종**(배치는 매번 랜덤 셔플): 3a(바디2+임산부1)·3b(임산부2+바디1)·3c(임산부+금박+보태니컬)·4a(바디+임산부+이레즈미+UV네온)·4b(이레즈미+UV네온+스테인드글라스+금박)·5a(4a+스테인드글라스)·5b(4b+보태니컬) — 각 30개 = 210개. 키 `la_mix3_{조합코드}_{type}_{번호}`.

**완전랜덤조합**(2~5인, 7트랙 중 매번 랜덤 선택+랜덤 배치) 각 30개 = 120개. 키 `la_mixedrand_{type}_{번호}`.

**인물 배치 원칙**: 자유축(바디페인팅·임산부)과 맥시멀리스트(어두운 피부 고정)를 교대 배치해 같은 피부톤 계열이 2명 이상 연속되지 않게 함. 맥시멀리스트만 쓸 때도 매번 트랙 순서를 랜덤 셔플 — "모든 것은 항상 랜덤이 원칙".

---

## 20. 버그 수정 이력

### 20-1. 중복 문장 버그
`bp_block` 템플릿이 `An extraordinarily large woman, far beyond any real person.`을 앞에 붙였는데, BODY_FULL 딕셔너리 자체가 이미 이 문장으로 시작해 같은 문장이 연속 두 번 나오는 버그. Core Formula(500개 중 472개)와 Mixed-Track(270개 중 143개)에 영향 — 둘 다 발견 당일 수정·재등록·재푸시 완료(commit `25b35b2`, `7a948a0`). 11~14인 압축포맷·임산부·맥시멀리스트 5종은 다른 템플릿 구조라 영향 없음.

### 20-2. 문양 겹침 버그
이레즈미·UV네온의 섹스텟~데켓(6~10인)이 구버전 좁은 문양 풀(6/7종)만 순환해, 한 이미지 안에 같은 트랙이 여러 번 나올 때 문양이 겹칠 수 있었음. 문양 풀을 26/27종(18-2, 18-3 참조)으로 확장하고 트랙별 독립 카운터로 중복 방지 — 300개(각 150개) 전부 수정·재등록 완료(commit `46e0e52`).

---

## 21. 피어싱·쥬얼리 최신 체계 (v6.5의 6단계에서 갱신)

**피어싱**: P(개수) **10단계** P0·P3·P5·P8·P15·P25·P50·P100·P150·P200 (v6.5의 P8~P250 6단계에서 P0·P3·P5 추가, P250/P300 폐기); C(참/체인 밀도) 3단계 C0·C1·C2; G(보석) 7종(다이아몬드·진주·오팔·자수정·루비·사파이어·혼합); F(형태) 7종(링/후프·스터드·바·클리커·드롭·세그먼트링·혼합); S(대칭) 2단계 S0(대칭)·S1(비대칭); M(금속색) 7종(골드·로즈골드·실버·코퍼·브라스·브론즈·혼합). 참(체인)은 항상 몸 재질과 같은 색·질감(예: 사파이어 크리스털 몸=사파이어빛 체인).

**쥬얼리**: 종류 JE·JN·JB·JR·JA·JH(귀걸이·목걸이·팔찌·반지·발찌·헤어주얼리); 재질 JMG·JMS·JMR·JMP·JMX; 규모 JS1~JS3; 개수 JQ1~JQ5(1개~10개초과 맥시멀리스트). 피어싱(P축)과 쥬얼리(JQ축)는 독립 축, 숫자 합산 안 함.

---

## 22. 보류·폐기 재질 전체 목록 (v6.5의 6장 "보류·불채택"과는 별개 — 바디페인팅/맥시멀리스트 트랙 전용)

| 재질 | 사유 |
|---|---|
| 글리터 | 검증 이력 없던 가짜 길(→마키에로 대체) |
| 홀로그래픽/이리디센트 | 보강해도 옷처럼 보임 |
| 코스믹 | 깊이감 보강해도 실패 |
| 헤나(멘디) | 차분한 템플릿·맥시멀리스트 둘 다 불안정, 옷처럼 나옴 |
| 진주/자개 · 비눗방울 | "몸에서 기포 올라오는" 느낌 |
| 깃털 | 생성은 성공하지만 옷/그림처럼 보여 미적으로 제외 |
| 산호 | 기술적 성공이지만 "징그럽다"는 취향상 제외 |
| 하이다 폼라인 | 피부톤 무관하게 옷처럼 생성(곡선 덩어리 형태가 원인으로 추정) |
| 사모안 타타우 | 생성 실패 |
| 베르베르·켈틱 | 밝은 피부로 바꿔도 옷처럼 생성(가는 선 디자인이 원인으로 추정) |
| 폴리네시안 트라이벌 · 지오드(크리스탈로 흡수 전) | 솔로는 성공하나 2인 이상 그룹샷에서 비키니 의상 혼입 반복 — 솔로 전용 보너스로만 유지, 추가 등록 안 함 |
| 콘스네이크(오렌지/크림슨, 비늘 계열 중) | 체형 무관 반복 실패(애니멀프린트 연상 추정) |

---

## 23. 등록 현황 전체 요약 (v6.5의 0장 표를 대체·갱신)

| 카테고리 | 개수 | 키 접두어 |
|---|---|---|
| Core Formula(바디페인팅, 1~14인) | 700 | `la_core_` |
| Pregnant Formula + Mixed | 950 | `la_preg_` / `la_mixed_` |
| Irezumi / UV Neon / Stained Glass / Gold Leaf / Botanical Formula | 각 300(계1,500) | `la_irezumi_` 등 |
| Mixed-Track Formula(7트랙 랜덤) | 270 | `la_mixed7_` |
| Fixed Combo / Random Combo Formula | 210 / 120 | `la_mix3_` / `la_mixedrand_` |
| Crystal / Scale Formula | 각 90(계180) | `la_crystal_` / `la_scale_` |
| Wax / Obsidian Gold Formula | 각 60(계120) | `la_wax_` / `la_obsidian_` |
| Material Blend / Craft Blend Formula (v6.9, 2026-10-04) | 각 270(계540) | `la_matblend` / `la_craftblend` |
| 기존 카테고리(Anime·Photo Direct/Duo·Signature·Glass Face계열·Idol·Craft·Colossal 등, 등록 로그 기준) | 1,720 | 각 섹션 참조 |
| **전체 누적 합계** | **6,310** (등록 로그 합산, `presets\la_*.json` 파일 수로 재확인 권장) | |

> **정정(v6.9)**: v6.7·v6.8의 "약 6,181"은 합산 오류였다(그 표의 행을 더하면 5,181이었고, 기준값 1,131은 09-23 시점 값이라 이후 등록분이 빠져 있었음). 330개 등록 시점의 카테고리별 로그(42개 카테고리, 합 5,140개)를 직접 합산하고 이후 등록분(Crystal/Scale 180 + Wax/Obsidian 120 + Blend 540)을 더한 값이 6,310이다. 확인 명령: PowerShell `(Get-ChildItem presets\la_*.json).Count` — 모든 카테고리가 `la_` 접두어를 쓴다면 같은 수가 나와야 한다.

---

## 24. 헤어 "무난한 10종" 서브셋

앞으로 "헤어컬러/헤어스타일 10개만 써서"라고 요청하면 아래 사용:
- **헤어컬러 10종**: 제트블랙·내추럴블랙·다크브라운·체스트넛브라운·초콜릿브라운·애쉬브라운·오번·허니블론드·골든블론드·발레아쥬
- **헤어스타일 10종**: 스트레이트·웨이브·컬·포니테일·업두·하프업·번·보브컷·샤기컷·울프컷

---

## 25. 다음 할 일 (종합, v6.5의 7장을 대체)

### 재질 트랙(15장 관련, 우선순위 높음)
1. 듀얼바디(L0~L4) 원래 정의 재확인 — 더 최신 핸드오프 파일이 있는지 확인
2. 프레임 체계(15-7) 용어 정리
3. 수조 비대칭(15-6) 결과 확인 후 필요시 듀얼바디 축 정식화
4. 코이·드래곤 전용 색상 세분화(품종명 아닌 색상만) 검토

### 맥시멀리스트/혼합(18~19장 관련)
5. 공작 깃털눈무늬 — 성공 확인됐으나 미등록, 별도 등록 검토
6. 크리스탈·비늘·왁스·흑요암금 — 등록 완료, 생성 검증 후 티어 부여

### v6.5에서 이월(여전히 미해결)
7. Photo Direct 252개·Photo Duo 168개 실제 생성 결과 확인 후 티어 부여
8. 애니 96~215번 실사(또는 조각상) 변환 후 티어 부여
9. 임산부 변형 실사 결과 확인(v6.5 11장)
10. Sculpture 솔로42·듀오42 검증 후 등록 결정
11. 트리오 2차 결과 확인 → 트리오·쿼르텟 스크립트화

---

## 26. 재질·바디페인팅 분할·혼합 체계 (v6.8, 2026-10-04)

> **배경**: 15장 작성 이후 같은 대화에서 추가로 진행된 실험. 한 인물(또는 그룹의 각 인물) 몸에 **두 가지 이상의 재질/패턴을 분할하거나 섞어서** 표현하는 기법을 폭넓게 테스트. 결론부터: **재질끼리는 거의 모든 조합·분할 방식이 성공**했고, **바디페인팅은 전통 공예명이 있으면 성공, 이름 없는 추상 기하학이면 실패**하는 뚜렷한 패턴을 발견.

### 26-1. 비늘(Scale) 동물 간 분할 — 전부 성공

코이+드래곤 비늘을 한 몸에 섞는 테스트로 시작, 아래 방식 전부 성공:

| 분할 방식 | 설명 |
|---|---|
| 가로분할(허리 기준) | 상체/하체 서로 다른 동물 비늘, 허리에 단일 수평 경계선 |
| 좌우분할(중앙선) | 좌/우 서로 다른 동물 비늘, 몸 중앙에 단일 수직 경계선 |
| 4분면(2×2) | 가로+세로 경계선 동시 적용, 4구역 각각 다른 동물(최대 4종) |

공작 깃털눈무늬(`peacock`, 15-2에서 비늘 묶음 밖으로 뺐던 것)도 4분면 테스트에 포함해 성공 — **6종(나비날개·코이·뱀·드래곤·인어·공작)으로 사실상 "비늘/눈무늬 묶음"에 복귀해도 되는 수준의 안정성 확인**.

경계선 서술 원형(가로):
```
her upper body (collarbones to waistline) is [재질A]. At her waistline
the material changes: her lower body (waist to ankles) is [재질B]. The
boundary is a single straight line circling her waist, never jagged,
no fabric no seam no garment.
```

### 26-2. 재질 간(다른 종류) 분할·혼합 — 거의 전부 성공

비늘 외에 **크리스탈·보태니컬·이레즈미·UV네온·스테인드글라스·금박·흑요암+금·왁스·목재·석재** 등 성격이 전혀 다른 재질끼리도 교차 테스트. 추가로 아래 2가지 "경계 모호화" 기법도 검증:

**경계흐림(Blurred Boundary)**: 직선 경계 대신, 중앙 몇 인치 폭의 구간에서 두 재질이 서로의 영역에 흩어져 침투하며 밀도가 점점 옅어지는 방식.
```
Rather than a sharp boundary, the two materials interweave and overlap
gradually across a soft, irregular zone a few inches wide running down
the centre of her body — elements of each scattered into the other's
territory, the density of each fading into the other rather than
stopping abruptly.
```

**전신 무작위 마블링(Marbled Whole-Body)**: 좌우·상하 구분 자체를 없애고, 천연석 마블링처럼 두 재질이 몸 전체에 무작위 패치로 흩어지는 방식.
```
her entire body ... is a random intermingled mix of two materials with
no spatial division at all — not left versus right, not top versus
bottom, but irregular patches of each scattered all over her body in a
marbled, organic distribution, exactly like natural mineral veining.
```

**3재질 자유형 경계(대각선 등)**: 재질 3개가 각자 불규칙한 구역(대각선 등 자유 형태)을 차지하고, 인접 구역끼리 부드럽게 섞이는 방식 — 직선 경계가 아예 없음. 2건 테스트 모두 성공.

UV네온이 포함된 조합은 "해당 구역만 전용 블랙라이트, 나머지는 표준 조명"으로 조명을 분리하면 문제없이 공존.

**목재·석재 전신 첫 성공 확인**: 메모리에 "석재 전신 미해결"로 오래 남아있던 항목이, 이 분할·혼합 기법(특히 재질 간 혼합)으로 처음 전신 단위에서 성공 확인됨. 재질 서술 원형:
```
wood: rich dark walnut wood fused directly into her own form, natural
grain lines flowing to follow every curve, BLAZING deep warm-brown grain
with VIVID honey-gold highlight streaks
stone: solid polished white marble fused directly into her own form,
natural grey-gold veining, BLAZING pale marble surface with VIVID golden
vein striations
```

### 26-3. 전체 축 매트릭스 테스트 — 2/3/4개 섞기 × 솔로/듀오/트리오

재질 풀 12종(이레즈미·UV네온·스테인드글라스·금박·보태니컬·크리스탈·드래곤비늘·코이비늘·흑요암금·왁스·목재·석재)에서 매번 랜덤 선택, 매번 랜덤 배치로 1·2·3명 그룹 생성. 결과:

- 1차(각 조합 3개씩, 27개): 대부분 성공(세부 실패 수는 기록 안 됨, 전반적으로 양호하다는 평가)
- 재검증(각 조합 2개씩, 18개): **16/18 성공(89%)** — 3개섞기 듀오 1개, 4개섞기 솔로 1개만 실패

그룹 인원이 늘어나도(트리오까지), 섞는 재질 개수가 늘어나도(4개까지) 성공률이 크게 떨어지지 않음 — **재질 분할·혼합은 오늘 테스트한 축 중 가장 안정적인 축**으로 판단.

### 26-4. 바디페인팅 — 전통 공예명 vs 추상 기하학

**추상 기하학 패턴(이름 없음) 4종 전부 실패**: 동심원(여러 중심에서 퍼지는 고리무늬), 몬드리안(굵은 검정 그리드+원색 블록), 프랙탈 스파이럴(인디고 나선), 허니콤(육각벌집) — 각 2개씩 테스트, 체형·구조(북엔드 포맷 포함)를 바꿔가며 재시도해도 전부 실패.

**추정 원인**: 몬드리안은 1965년 입생로랑의 유명한 "몬드리안 드레스" 디자인과 직결되어 모델이 옷으로 직행했을 가능성. 동심원·스파이럴·허니콤은 특정 디자인과 연결되진 않지만, 패션에서 "원단 프린트"로 워낙 흔히 쓰이는 추상 기하학이라 "문화적 전통 공예"라는 프레이밍 앵커가 없으면 "피부"보다 "옷의 프린트"로 더 쉽게 읽히는 것으로 추정.

**실존 전통 공예명 조합(바디페인팅 공예 39종 풀에서) — 거의 전부 성공**: 처음 조건 없이 섞었을 때(구조를 원래 북엔드 포맷에서 벗어나 한 문단으로 뭉뚱그려 썼을 때)는 "거의 생성이 안 됨" — **원인은 패턴 자체가 아니라 북엔드 구조(Subject/Physique/Skin/Body Art 문단 분리) 이탈**이었음을 확인. 북엔드 구조로 복원하자 2개 섞기 솔로 2/2 즉시 성공.

이어서 **"부피 큰 체형"(USSBBW·슈퍼글래머·아마조네스·블랙글래머·머슬아워글래스BBW·헤비머슬) × 공예 2~4개 섞기 × 솔로/듀오/트리오** 각 2개(18개) 테스트 — **17/18 성공(94%)**. 체형이 극단적으로 크고 섞는 패턴이 4개까지 늘어나도, 북엔드 구조+실존 공예명만 유지하면 안정적임을 확인.

### 26-5. 핵심 결론

| | 결론 |
|---|---|
| **재질(이레즈미~석재) 분할·혼합** | 어떤 조합·분할 방식이든 대체로 안정적 — 가장 관대한 축 |
| **바디페인팅 추상 기하학** | 이름 없는 패턴은 실패(옷/프린트로 연상) — 쓰지 말 것 |
| **바디페인팅 실존 공예 분할·혼합** | 북엔드 구조만 지키면 안정적 — 체형·인원·섞는 개수와 거의 무관 |
| **북엔드 구조(Subject/Physique/Skin/Body Art 분리)** | 바디페인팅에선 분할·혼합 실험에서도 필수 — 한 문단으로 뭉뚱그리면 실패율 급증 |

### 26-6. 다음 할 일 (26장 추가분)

1. 이 분할·혼합 기법으로 300개 단위 정식 등록 검토(재질 쪽 — 안정성 높아 등록 가치 있음)
2. 비늘 묶음에 공작(6종째) 정식 편입 여부 결정
3. 동심원 등 추상 기하학을, "호주 원주민 도트페인팅" 같은 전통 공예 이름을 붙여 재시도(가설 검증)
4. 3개섞기 듀오·4개섞기 솔로 실패 케이스 재시도해 우연인지 패턴인지 확인

### 26-7. 석재·목재 조합 규칙 (v6.9 추가)

| 시도 | 결과 |
|---|---|
| 석재+목재만으로 2/3/4종 혼합 × 솔로·듀오·트리오·쿼르텟 (12개) | 10/12 성공 — 실패 2건(3혼합 쿼르텟, 4혼합 트리오)은 모두 석재+목재만의 조합 |
| 석재 1종 고정 + 목재를 뺀 다른 재질로 2/3/4혼합 × 솔로·듀오·트리오 (9개) | 9/9 성공 |
| 임산부 + 목재 4종만 2/3/4혼합 × 솔로·듀오·트리오 (9개) | 2/9 성공(목재끼리만 섞을 때 약함) |
| 임산부 + 4재질 중 목재 비율 1/2/3개 (솔로 3개) | 3/3 성공 |
| 일반인+임산부+맥시멀리스트 트리오, 각자 목재 비율 다르게 | 성공 |

**규칙**: 석재+목재만으로 이루어진 조합은 쓰지 않는다. 목재는 다른 재질과 섞이거나 비중이 낮으면 문제없었다. 변종: 석재 4(대리석·화강암·로즈쿼츠석·비취석), 목재 4(월넛·오크·마호가니·에보니). 블렌드 번들에서는 석재·목재를 각각 1슬롯으로 취급하고 {석재+목재}만의 2혼합을 제외했다.

**미검증 구간**: 한 인물에 석재+목재+다른 재질(3~4혼합)이 함께 들어가는 경우. 블렌드 번들(A)에서는 허용되어 포함될 수 있으므로, 생성 결과로 확인이 필요하다.

### 26-8. 블렌드 540개 등록 (commit `c857eed`, 2026-10-04)

번들 `la_blend_540_bundle.json` + 패치 `patch_la_blend_1_json.py`. 카테고리 2개 신규. 각 9그룹(2/3/4혼합 × 솔로·듀오·트리오) × 30개.

**A. Material Blend Formula (270)** — 키 `la_matblend{2|3|4}_{solo|duo|trio}_{번호}`
- 맥시멀리스트 골격(ALL CAPS, 순수 검정 배경, 어두운 피부 고정) 유지. 인물마다 재질을 독립 랜덤으로 뽑는다.
- 재질 16종: 이레즈미(문양 26)·UV네온(문양 27)·스테인드글라스·금박·보태니컬·크리스탈(10색)·비늘 6종(나비날개·코이·뱀·드래곤·인어·공작눈무늬)·흑요암금·왁스·목재·석재.
- 경계 방식: 2혼합=좌우 경계흐림(약 60%) 또는 전신 마블링(약 40%), 3·4혼합=자유형 구역(대각선 등). 모두 이번 대화에서 검증된 방식이며, 포즈는 구역이 보이는 정면·측면 계열만 사용.
- UV네온이 들어간 인물에는 해당 구역 전용 블랙라이트 문장을 붙인다.
- 실제 분포: 경계 방식 zones 360·좌우 110·마블링 70, 재질별 87~122회, 공작 포함 81개 프리셋, 단어 수 305~1,235.

**B. Craft Blend Formula (270)** — 키 `la_craftblend{2|3|4}_{solo|duo|trio}_{번호}`
- 바디페인팅 북엔드 구조(Subject/Physique/Skin/Body Art 분리)를 유지. 실존 전통 공예 40종 풀(이름 없는 추상 기하학은 사용하지 않음), 체형은 부피 큰 6종(USSBBW·슈퍼글래머·아마조네스·블랙글래머·머슬아워글래스BBW·헤비머슬).
- 경계 방식: 2혼합=가로(상체/하체) 또는 좌우 경계흐림, 3·4혼합=자유형 구역. 메이크업·나이·분위기·헤어스타일·헤어컬러·네일·포즈·신발은 전체 풀에서 랜덤.
- 같은 이미지 안에서 메이크업·체형·공예가 겹치지 않게 뽑았다. 공예 40종 전부 24~53회 사용, 단어 수 421~1,414.

**검증 때 쓴 프롬프트와 달라진 점 2가지** (등록 후 실제 생성 결과로 확인 필요)
1. **중복 문장 제거**: 검증용 B 프롬프트에는 "An extraordinarily large woman, far beyond any real person."이 한 번 더 붙어 있었다(BODY_FULL이 이미 같은 문장으로 시작). 17/18(94%) 성공률은 중복이 있는 버전으로 측정한 값이다.
2. **메이크업 설명 속 머리 묘사 제거**: 아래 26-9 참조.

등록 후 생성 검증과 티어 부여는 아직 하지 않았다.

※ v6.10: B(Craft Blend)의 3·4혼합 180개는 27장의 새 방식으로 교체되었다(commit `b990556`). 이 장의 B 경계 설명(3·4혼합=자유형 구역)은 2혼합에만 해당한다.

### 26-9. 기존 등록분 점검 결과 (미수정, 재등록 여부 미결정)

**(a) 메이크업 설명 속 머리 묘사와 헤어 축 충돌**
- `face()`가 돌려주는 메이크업 설명 48종 중 33종에 머리 묘사가 이미 들어 있다(예: "long sleek chestnut waves", "long black hair in fine neat braids"). 여기에 헤어스타일·헤어컬러 축을 따로 붙이면 같은 인물에 머리 묘사가 두 번 나와 서로 충돌한다("ash-brown hair styled in a short pixie cut" 등).
- 로컬 번들 기준 등록분 약 2,250개 중 약 1,919개(약 85%)에 해당: Core 282/300(1~6인)·200/200(7~10인)·200/200(11~14인 압축), Pregnant 471/500, Mixed(일반+임산부) 443/450, Fixed/Random Combo 204/330, Mixed7 119/270. 맥시멀리스트·Crystal/Scale·Wax/Obsidian·Blend는 `face()`를 쓰지 않아 해당 없음(Blend B는 제거 처리 완료).
- 이 구조는 헤어 축이 8종이던 시절부터 있었고, 지금까지 이것이 생성 실패의 원인으로 확인된 적은 없다. 다만 오늘 확장한 헤어 31×30 축이 이런 프리셋에서는 의미가 흐려진다.
- 해결안: 번들을 다시 만들 때 `face()` 설명에서 머리 묘사 절만 제거(정규식 `HAIRW`로 32종 절 식별, 제거 후에도 모든 메이크업에 3개 이상의 절이 남음)하고 재등록.

**(b) 중복 색상어**
- "VIVID VIVID"가 Fixed/Random Combo 151개·Mixed7 205개·Crystal/Scale 13개, "BLAZING BLAZING"이 Crystal/Scale 7개에 있다. 색 팔레트 값에 접두어("VIVID GOLD", "BLAZING CRIMSON" 등)가 이미 들어 있는데 템플릿이 또 붙이는 것이 원인(스테인드글라스 팔레트, `SCALE_ANIMAL_DB`의 일부 코이·드래곤 팔레트).
- 보기에만 어색한 수준으로 보이며 수정은 안 했다. 신규 Blend 번들은 접두어를 제거하는 처리로 방지했다.

### 26-10. 다음 할 일 (v6.9 기준)

1. 블렌드 540개 실제 생성 검증 후 티어 부여(특히 위 26-7의 미검증 구간, 26-8의 검증 대비 변경 2건 확인).
2. 기존 등록분의 헤어 충돌(a)·중복어(b) 수정 재등록 여부 결정 — 영향 범위는 26-9 참조.
3. 석재+목재+다른 재질 3~4혼합 검증.
4. 26-6의 이월 항목: 비늘 묶음에 공작 정식 편입, 추상 기하학에 전통 공예명을 붙인 재시도, 3개섞기 듀오·4개섞기 솔로 실패 케이스 재시도.
5. 25장의 이월 항목(Photo Direct/Duo 티어, 애니 96~215번 변환, 임산부 변형, Sculpture 검증 등).


---

## 27. 다중·복합 바디페인팅의 경계 설계 (v6.10, 2026-10-04)

### 27-1. 요약
- 등록된 3·4혼합은 인물마다 "zones arranged diagonally and asymmetrically"라는 같은 문구를 받아서, 구역이 어깨→힙 대각선으로 쏠렸다(27-2).
- 구역마다 신체 부위 이름을 나열하는 방식은 생성 실패가 많았고, 부위 이름 없이 선·중심점·시계 방향으로만 적는 방식은 87%가 3번 안에 생성됐다(27-5).
- 구역 수가 2개일 때만 유독 약했다. 3구역 이상은 22개 전부 3번 안에 성공했다.
- 이 방식으로 Craft Blend 3·4혼합 180개를 교체 등록했다(27-6). 재질 쪽 Material Blend와 2혼합은 그대로다.
- 결과 확인은 성공/실패 번호만 하기로 했다(채움·배치 같은 다항목 체크는 하지 않음).

### 27-2. 대각선 쏠림의 원인
등록 번들(`la_blend_540_bundle.json`)에서 구역형(3·4혼합) 인물은 재질 360명, 공예 360명이었고, 전원에게 문구 `zones arranged diagonally and asymmetrically`가 들어갔다. 구역 위치를 정하지 않고 "대각선으로 비대칭하게"만 말하면 모델이 가장 흔한 배치(어깨→힙)로 수렴한다. 2혼합도 좌우, 가로, 마블링 세 가지뿐이었다.

### 27-3. 재질 쪽 '다중재질 모양(SH)' 목록 (재질 전용 검증, 바디페인팅에서는 검증된 적 없음)
출처: 과거 세션 기록 `/mnt/transcripts`의 `2026-09-30-12-33-23` (session4b)와 `2026-10-01-10-12-34` (session5 system-codification), 통합 문서 `LumineX_Unified_System_BodyPaint_and_Material.md`(B6). 핸드오프 v6.9 이전에는 이 목록이 없었다.

| 코드 | 모양 | 설명 |
|---|---|---|
| SH1 | 동심원 | 배꼽 중심으로 퍼지는 나이테 모양 링 |
| SH2 | 부채꼴 | 가슴 중앙 한 점에서 방사형으로 갈라지는 조각 |
| SH3 | 비대칭 몬드리안 | 불규칙 사각형 + 굵은 검은 격자선 |
| SH4 | 스트라이프 | 가는 가로줄이 재질별로 번갈아 반복 |
| SH5 | 가로 일자 | 한 지점에서 위/아래 수평선으로 분할 |
| SH6 | 세로 반반 | 정중앙 세로선 기준 좌/우 분할 |
| SH7 | 스테인드글라스(4개) | 큰 불규칙 조각 4개, 굵은 납선으로 구분 |
| SH8 | 소용돌이 | 나선형으로 몸을 휘감는 줄무늬 |
| SH9 | 체커보드 | 바둑판 무늬 |
| SH10 | 음양(S자) | 부드러운 S자 곡선 |
| SH11 | 헤링본 | V자 반복 사선 패턴 |
| SH12 | 찢어진 종이 가장자리 | 불규칙하고 유기적인 경계 |
| SH13 | 대각선 | 한쪽 어깨에서 반대쪽 다리로 이어지는 대각선 |
| SH14 | 웨이브(물결) | 작은 물결이 여러 번 반복되는 경계 |
| SH15 | 폴카도트 | 한 재질 바탕에 다른 재질의 동그란 점 |
| SH16 | 셰브론 | 굵고 단순한 V자 지그재그 줄무늬 |
| SH17 | 선버스트 | 중심에서 퍼지는 방사형 선 |
| SH18 | 우키요에 목판화 | 굵은 검은 윤곽선 + 평면 색 |
| SH19 | 해부학적 부위 분할 | 왼팔·오른팔·몸통·왼다리·오른다리 5부위에 재질 자유 배정(앱 등록명 Five-Material Patchwork) |

- **바디페인팅 공예로 이관된 5종**: 클림트 모자이크, 에셔 테셀레이션, 큐비즘 분할, 이슬람 기하학 타일, 바자렐리 옵아트(무늬가 촘촘해서 재질 조각보다 실사 몸에 덧입힌 그림처럼 보임).
- **9월 30일 중간본(14종)과의 차이**: 중간본은 SH1~SH7 확정, SH8~SH14 "탈락 이력"이었다(체커보드는 재질 3개 이상에서 깨짐, 찢어진 종이는 손상처럼 보일 위험, SH14 정규 2×2 격자는 SH3이 더 나아 밀림). 10월 1일 최종본에는 SH1~SH13이 "확정 13종"으로 올라가 있고 SH14는 웨이브로 바뀌었다(2×2 격자는 격자 시스템 GR2로 통합). **탈락 7종의 재시도 결과를 사용자가 확인한 대화는 찾지 못했다** — SH8~SH13이 실제로 안정적인지는 미확인.
- **듀얼바디(DB)**: 같은 통합 문서(B8)에 있다. 재질→실사(다리) 전환이며 기본 5종(L0~L4)과 인접 단계를 섞은 비대칭 5종으로 구성. L0~L4 각 단계의 정확한 정의는 아직 읽지 못했다.
- 가로 2~10줄(SHH)·세로 2~3줄(SHV) 확장안도 논의됐으나 확정 기록은 못 찾았다.

### 27-4. 바디페인팅용 경계 설계 원칙 (어휘집)
1. **모양 이름이 아니라 구조로 분해한다.** 영역 구조(띠, 중심점을 둘러싼 동심 영역, 중심에서 퍼지는 쐐기)와 경계선 모양(매끈, 물결)을 따로 랜덤으로 뽑는다. 목록을 고정하지 않고 위치 숫자(1% 단위)와 방향까지 랜덤으로 둔다.
2. **프롬프트에는 모양 이름을 쓰지 않는다.** 체커보드·헤링본·셰브론·폴카도트·스트라이프는 원단 프린트로 흔해서, 이름 없는 추상 문양 4종이 옷 프린트로 읽혀 전부 실패한 것(26-4)과 같은 위험이 있다. 모양 이름은 제목·메타에만 쓴다. 구역 안은 실존 전통 공예명으로 채운다.
3. **신체 부위 이름을 구역마다 나열하지 않는다.** chest·belly·sternum·pelvis·inner thighs 같은 부위어는 최소화하고, "figure의 중심", 위에서 몇 % 높이, 시계 방향 같은 기하학 표현만 쓴다. (부위어 2~9개를 쓴 레이아웃 15개 테스트는 생성 실패가 많았고, 성공했던 분할 문구는 0~2개였다. 직접 비교 실험은 아니라 추정이다.)
4. **경계는 전부 희미하게.** 문구 원형:
```
The boundaries between regions are hazy and feathered — there is no visible
line at all. Each transition zone is about a hand's width wide, and across it
the neighbouring patterns dissolve into each other, motifs from one thinning
out as motifs from the other appear, density fading rather than stopping
abruptly, never a hard edge. Each transition zone follows a smooth, even,
straight course.   (물결이면: ...follows a gently undulating wave, rising and
falling softly, rather than a straight course.)
Even inside a transition zone the skin is never left bare: at every point one
pattern, or a mixture of the two, fully covers it.
```
5. **구조 문장 형식 예** (대각 띠 3구역): `Her figure is divided into 3 diagonal bands by 2 parallel hazy transition zones running from the upper left to the lower right as seen by the camera, crossing the centre line of her figure about 35% of the way down her figure from the top and about 75% of the way down her figure from the top.` 이어서 `Region 1 is everything on the upper side of the first diagonal transition zone: it is painted in {공예}...` 식으로 구역마다 서술.
6. **구조 5종과 위치 범위**: 가로·세로·대각 띠(구역 수-1개의 전환 구간, 위치 15~85% 범위에서 간격 15~20% 이상, 대각은 두 방향 랜덤), 동심원(중심 40~60%, 반경 20~85% 간격 15% 이상), 부채꼴(중심 40~60%, 광선을 시계 방향 위치로 지정, 쐐기 폭은 최소 2시간). 좌우는 인물 기준("her left")이라 화면에서는 반대로 보일 수 있다.
7. **시험은 위험도 순서**: 1단계(가로·세로·대각 띠, 물결 경계, 부채꼴, 동심원)는 이번에 검증 완료. 2단계 후보는 비대칭 몬드리안, 스테인드글라스형 큰 조각 4개, 폴카도트, 굵은 스트라이프(4줄 이하), 셰브론. 3단계(보류)는 체커보드, 헤링본, 소용돌이, 음양, 찢어진 종이, 가는 줄무늬(재질 쪽에서도 불안정 기록이 있었거나 프린트·손상 연상이 강함).

### 27-5. 검증 결과
**(a) 희미한 경계 솔로 33개** (구조 5종 × 경계선 2종 × 3개 = 테스트 30개 + 대조군 3개, 생성은 최대 3회 시도)
- 테스트 30개: 1회 21개(70%), 3번 안 26개(87%).

| 구조 | 1회 | 3번 안 | 개수 |
|---|---|---|---|
| 가로 띠 | 4 | 6 | 6 |
| 세로 띠 | 4 | 5 | 6 |
| 대각 띠 | 5 | 5 | 6 |
| 동심원 | 3 | 4 | 6 |
| 부채꼴 | 5 | 6 | 6 |

| 구역 수 | 1회 | 3번 안 | 개수 |
|---|---|---|---|
| 2구역 | 4 | 4 | 8 |
| 3구역 | 6 | 10 | 10 |
| 4구역 | 11 | 12 | 12 |

- **실패 4개가 전부 2구역**(우연일 확률 약 0.3%). 3구역 이상은 22개 전부 3번 안에 성공(1회 17개, 77%). 동심원이 약했던 것도 2구역이어서였다(3구역 이상은 4/4).
- **경계선 모양**: 3구역 이상에서는 차이가 없다(1회 기준 물결 9/11, 매끈 8/11). 2구역에서는 매끈 3/4, 물결 1/4이었으나 표본이 작다.
- **대조군**: 좌우 2혼합(3회), 허리 가로 2혼합(2회), 기존 등록 방식 3혼합(3번 모두 실패). 2구역 전체(테스트+대조군)는 1회 4/10, 3번 안 6/10.

**(b) 확인용 10장** (사용자가 다시 생성해서 확인, 이미지는 저장하지 않음): 배치 10/10 O, 구역 수 10/10 O, 경계 O 7·△ 2·X 1, 채움 O 3·△ 6·X 1. 빈 곳은 팔, 안쪽 다리, 종아리~발목, 목, 가슴, 겨드랑이처럼 늘 비슷한 부위였다. 경계 △/X 3장에서 전환 구간에 살이 띠처럼 비친다는 보고가 있어 27-4의 마지막 보호 문장("never left bare")을 추가했다(효과는 미확인). **사용자 결정: 채움은 케바케로 보고 크게 신경 쓰지 않으며, 앞으로 결과 확인은 성공/실패 번호만 한다.**

**(c) 듀오·트리오 12개** (새 방식 9개: 듀오 4·트리오 5, 3~4구역 / 등록분 직접 대조군 3개)

| 구분 | 1회 | 3번 안 | 평균 단어 수 |
|---|---|---|---|
| 새 방식 9개 | 4 (44%) | 8 (89%) | 1,633 |
| 등록분 3개 | 1 (33%) | 3 (100%) | 1,013 |

- 길이와 시도 횟수의 상관은 -0.47로, 길이가 해롭다는 신호는 없었다. 팔·다리 맨살은 짧은 등록분(02·04번)에서도 보고돼 방식이나 길이의 문제가 아니라 원래 약한 부위로 판단했다. 트리오 6개는 전부 팔·다리 맨살이 보고됐고 듀오는 절반이었다(인원이 늘어 인물이 작아지는 영향으로 추정, 길이와 겹쳐서 완전히 구분되지는 않음).
- 실패 1개(10번: 듀오 3구역, 대각 띠·물결 + 세로 띠·물결)는 원인 불명.
- 표본이 작아 "새 방식이 등록분과 비슷하다" 수준의 결론만 낼 수 있다.

### 27-6. 교체 등록 (commit `b990556`)
- 대상: `la_craftblend{3|4}_{solo|duo|trio}_{01~30}` 180개를 같은 키로 덮어씀. 번들 `la_craftblend_geo_180_bundle.json`, 패치 `patch_la_craftblend_geo_1_json.py`. 카테고리·키가 같아 메타 등록은 필요 없다.
- 인물마다 구조 5종 × 경계선 2종에서 랜덤(한 이미지 안에서 구조 중복 없음), 위치 숫자 1% 단위. 구조 문장 360개 중 321개가 서로 다르다(89%).
- 기존과 달라진 점: 프롬프트가 약 40~50% 길어짐(예: 트리오 4혼합 1,838~2,039단어, 기존 1,249~1,385). 포즈는 구역이 보이는 정면 계열만 사용(기존은 뒷모습 포함 19종). 보호 문장 추가. 메이크업 설명 속 머리 묘사 제거(26-9)는 이전과 동일.
- 바꾸지 않은 것: 2혼합 90개, Material Blend 270개. 등록 합계 6,310은 그대로.

### 27-7. 알려진 한계·미결정
- **2혼합**: 2구역이 약하다는 결과가 있어서 새 방식으로 다양화하지 않았다. 등록된 2혼합(공예 90 + 재질 90)이 같은 약점을 가졌는지는 미확인.
- **Material Blend 3·4혼합(180개)**: 여전히 "diagonally" 문구를 쓴다. 새 방식은 바디페인팅에서만 검증됐고, 재질 맥시멀리스트 골격에서는 처음 만든 레이아웃 15개가 많이 실패했다(부위어 가설). 재질용은 소규모 확인 후에 교체 여부를 정한다.
- **기존 등록분의 헤어 충돌·중복 색상어**(26-9)는 수정하지 않았다.
- **채움**(팔·다리·종아리~발목 맨살)은 원래 약한 부위로 두기로 했다.
- SH8~SH13 재시도 결과와 듀얼바디 L0~L4 정의는 아직 확인하지 못했다(27-3).

### 27-8. 다음 할 일
1. Material Blend 3·4혼합을 새 방식으로 바꿀지 판단하기 위한 소규모 확인(솔로·듀오·트리오 9개 정도).
2. 2혼합(공예 90 + 재질 90)을 어떻게 할지 결정.
3. SH 2단계 모양(비대칭 몬드리안, 스테인드글라스형 큰 조각 4개, 폴카도트, 굵은 스트라이프, 셰브론)의 바디페인팅용 구조 후보 검토.
4. 기존 등록분의 헤어 충돌·중복어 수정 및 재등록 여부 결정.
5. 듀얼바디 L0~L4 정의와 SH8~SH13 재시도 결과를 과거 세션 기록에서 찾기.
