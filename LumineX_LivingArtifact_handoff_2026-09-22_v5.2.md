# LumineX · Living Artifact — 인수인계 메모 v5.2 (2026-09-22 밤)

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
- **v4 등록 대기 105개(Signature Solo 55 + Duo 50)**: 여전히 대기 중

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
| 3/4 + 동심원 문양 (둥근 배) | 비권장 (임신 배로 읽힘) |
| 완전한 조각상 (B 방향) | 별도 시리즈 후보로 보관 |
| 인종 다양화 | 추후 (피부 문장·재질 대비 재검증 필요) |

---

## 7. 다음 할 일

### 오늘 과제 이어서
1. **글래머 아워글래스** 과장 강화 보완판 → 4단계 적용
2. **머슬 아워글래스 BBW** 실사에 5-2 → 5-3 채우기 적용 (피부가 바탕인 재질에서도 통하는지 확인)
3. **헤비 머슬** 실사를 `사진처럼` 추가해 재변환 → 4단계 적용
4. **USSBBW**(나전칠기·자주요 등)도 3·4단계 채우기로 등록 가능 버전 완성
5. 머슬 USSBBW 정면·은입사 실사에 **채우기(배 중앙)** + 사진감 보강 → 등록 가능 버전
5-1. 스모 자주요·나전 실사에 5-1 상황별 문장(소품 유지) 적용해 재변환
6. 페어·글래머 보완판 (선택, "작게" 대비 지시 약점 있음)

### LumineX 반영
7. 등록 구조 설계: 애니 프롬프트는 기존처럼 프리셋 등록, 변환·채우기 명령어는 별도 카테고리(예: `🏺 Living Artifact · Photo Convert`)에 재질 슬롯 템플릿으로
8. 애니 프리셋 키 규칙 검토 (예: `la_anime_{체형}_{재질}_34`)

### v4에서 이월
9. 집에서 **Signature Solo 55 + Duo 50 등록** (v4 요약 3장 명령어) → 총 455개
10. 트리오 2차 결과 확인 → 트리오·쿼르텟 스크립트화
11. 신규 재질 다인 검증, HOF/SSS 티어 부여, `core\data.py` 체형 옵션 교체 (머슬 BBW → 헤비 머슬)
