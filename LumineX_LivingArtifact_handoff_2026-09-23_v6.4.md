# LumineX · Living Artifact — 인수인계 메모 v6.4 (2026-09-23)

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

### Idol Duo/Solo 등록 완료, 후속 조치 필요 (v6.4 신규)
7-1. **등록 완료**: `🏺 Living Artifact · Idol Duo` 50개, `🏺 Living Artifact · Idol Solo` 124개 (commit `deb48d5`). 인물 풀은 한국/일본/중국 아이돌 + 인도/중동 걸프/라틴 미인 + 실버폭스(흑인 제외, 무작위 혼합), 체형 9종 + 임산부 변형, 재질 14종, 피어싱류 액세서리 무작위.
7-2. **알려진 이슈**: 등록된 174개는 재질 딕셔너리에 옛 띠 표현(`wide bands following the deep crease... like contour lines`)이 남아 있어 옷처럼 보일 수 있음(13-2 참조로 이제 전면 폐지된 형식). `preset_builders/patch_livingartifact_idolduo_json.py` · `idolsolo_json.py`는 띠 표현을 제거한 수정판이 로컬에 있으나 **`--force`로 아직 재등록하지 않음**. 재등록 시 seed 고정(idolduo=4271, idolsolo=9311)이라 동일 파일명으로 덮어써진다.
7-3. 5,000파운드 조합(13-6~13-11)은 Idol Duo/Solo에는 아직 반영되지 않은 별도 실험. 필요하면 이 규칙을 담은 고무게 하위 세트를 추가 검토.

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
