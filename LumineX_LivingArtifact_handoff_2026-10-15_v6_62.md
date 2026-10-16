# LumineX · Living Artifact — 인수인계 메모 v6.62 (2026-10-15)

> **v6.62 수정 사항**: 60장 신규 — **Male Face Female Body Formula 100 등록**(`la_malefacefemale_solo_001~050`·`duo_001~025`·`trio_001~025`, 새 카테고리 1개, commit `c8dad166`, 실측 `(Get-ChildItem presets\la_*.json).Count` = **16320**). 얼굴 축 결론(미소년만 쓰면 여성 얼굴로 나옴 → 남성 특징 아이돌 65% + 미소년·중성 35%), **linework 패턴 3종 제외**, 체형 10종(바스트·허리·힙 강조), 남성 체형 미소년 샘플 결과, 트리오 세로 문구.

> **v6.61 수정 사항**: 59장 신규 — **이번 세션 시험 전체 기록**: 철사·철근(격자 소재) 프레임 컷 실패와 철근 전신 성공, 물체 몸 바닥 접지 문장(Floor-rest) 성공, **등록된 Core 바디아트 문구가 정면 성공의 핵심**이라는 발견("밴드" 문구 + 부위 나열 목록), 피어싱 석상×Core 중단, **남성 바디페인팅**(측면 6/6, 정면은 등록 문구로 3/3), **남성 얼굴 + 여성 Core 체형**(야외+여성 포즈 5/5), 남성 야외 40인치 슈즈 5/5, 남성 얼굴에 여성 헤어·눈 메이크업(5번 패턴 교체 후 성공), **여성 체형+남성 얼굴 듀오·트리오**, 혼합 트리오, 트리오 세로 문구. 등록한 것은 없음(합계 16,220 그대로).

> **v6.60 수정 사항**: 58장 신규 — **세 축 용어 확정**(바디페인팅 축=실제 몸에 얹음, 소재 축=몸 자체가 재질, 의상 축; 피어싱 등은 공통 옵션), **소재 쪽 프레임 컷 정의 재확인**, **Core Body 19**(제외 2종·최상급 표현이 약하게 나오는 교훈·힐 relative 모드 버그), **Material Blend 결정**(옛 Blend 틀, 2~4혼합, 돌출 재질 5종 제외, 곡선 경계 문구, 은색 띠 원인 "transition zone"), **Core Blend 270 번들 등록**(카테고리 9개, 합계 **16,220**, commit `a8cc91b4`), **소재 축 새 영역 탐색**(모래시계·철사·전구와 물체 몸: 시계·랜턴·향수병·바이올린·청자 매병·종이접기·구체관절 인형 채택, 원소·설탕·해파리·장구·기타·지구본 실패), 생성기 백업 `..._2026-10-15b.zip`.

> **v6.59 수정 사항**: 57장 신규 — **의상 없는 쪽 새 재질 6종 채택**(얼음·서리·깃털·회로·사이버·진주층·곤충 날개·거울 파편 모자이크 모두 1차 성공, 헤나·메헨디는 실패로 제외), **그룹 샘플 8개**(같은 재질 2~5인·섞은 재질 2~5인 모두 정상), **추가 색 6개 확인 통과**, **새 재질 번들 300 생성·등록**(`la_{ice,feather,circuit,nacre,wing,mirror}_` 각 30 + `la_m6mix_` 120, 새 카테고리 7개, commit `37be7961`, 합계 **15,950** 확인), legendary bust 체형 코스튬 3개 시험, 생성기 백업 `..._2026-10-15.zip`.

> **v6.58 수정 사항**: 56장 신규 — **성인 코스튬 시험 전 과정**(28종 채택, 닌자 재시험 성공), **체형 그룹 매핑**(근육질·바스트·허리·힙·부피 큰 체형)과 얇은 체형 제외, **팔 포즈(팔짱·얼굴 감싸기) 제외 확정 + 등록된 의상 59개 교체**, 극단 체형은 **서 있는 포즈 시험 후 원래대로(앉은 자세 70%) 유지**, 의상·코스튬 **그룹 2~5인 시험 모두 정상**, **코스튬·의상 그룹 번들 310 등록**(`la_costume_*` 215 + `la_clothes_{duo..quintet}_` 95, 합계 **15,650**, commit `4bf14a73`).

> **v6.57 수정 사항**: 52~55장 신규 — **새 영역 4종 채택·제외 결정과 400 번들**(크롬·라인스톤·프로젝션·스플래시 + 4요소 믹스, 주얼리 규칙 `jewel_fam`), **Wet Look 240 + 새 영역 400 등록**(합계 **14940**, commit `17f000c2`)과 **제목 교체 390 + 1,202**(commit `8e196ef8`), **크롭 시험(보류)**, **의상(B-track) 시험 전 과정**(수영복·플런지·컷아웃·슬릿·상체 가리개·밴도/벨트/띠 류), **의상 번들 400 등록**(`la_clothes_*`, 6카테고리, 합계 **15340**, commit `96e66693`), 생성기 백업 `LumineX_generators_backup_2026-10-14.zip`.

> **v6.56 수정 사항**: 51장 신규 — **성운·용암·블록 3종 등록**(`la_nebula_`·`la_lava_`·`la_brick_` 각 60, 합계 180, commit `cdcd3aab`, 새 카테고리 3개, 실측 `(Get-ChildItem presets\la_*.json).Count` = **14300**), **제외 영역**(털실·펠트, 수묵·서예, 라텍스·비닐 풍선), **접두어 표 2종**, **제목 규칙 적용 누락 진단**(새 번들 390 + Face Sculpt 1,202, 교체는 "집이야" 때 진행), **젖은 광택(Wet Look) 전 과정**(시험 결과·채택/제외 규칙·메이크업 풀 확장·머리/얼굴 젖음 3모드·그룹 구성)과 **Wet Look Formula 240 번들 작성**(`la_wet_240_bundle.json` + `patch_la_wet_1_json.py`, **등록 대기** — 사용자가 "등록하자"라고 하면 진행, 예상 개수 **14540**). 옛 핸드오프(v6.55 이하)는 **지우지 않았다**(나중에 정리).

> **v6.55 수정 사항**: 50장 신규 — **인형 듀오 30 등록**(`la_dolljoint_duo_001~030`, 기존 Doll Joint 카테고리, commit `bd071c75`, 실측 `(Get-ChildItem presets\la_*.json).Count` = **14120**), **미니어처 불채택**(사용자 "별로"), **인형 트리오 보류 유지**. 49-5·49-8의 미니어처·인형 듀오 항목은 이 장으로 갱신됐다. 옛 핸드오프(v6.54 이하)는 **지우지 않았다**(나중에 정리).

> **v6.54 수정 사항**: 49장 신규 — **신규 영역 3종 등록**: 오토마톤(`la_automaton_001~060`)·먹는 재질(`la_edible_001~060`)·인형 관절(`la_dolljoint_001~060`) 각 60개, 합계 180개(commit `2be1773c`, 새 카테고리 3개, 실측 `(Get-ChildItem presets\la_*.json).Count` = **14090**). 시험에서 얻은 규칙(관절 대비색·어두운 색은 묻힘·피부색 비슷한 몸은 실사로 돌아감·딱딱한 구조 문구가 부드러운 재질을 죽임)과 **주얼리 '배꼽 펜던트' 문장이 맨살 배꼽을 만드는 문제**(새 번들은 수정, 등록분 일괄 교체는 미정)를 기록했다. 인형 듀오·트리오, 미니어처는 확인 전. 옛 핸드오프(v6.52 이하)는 **지우지 않았다**(나중에 정리).

> **v6.53 수정 사항**: 48장 신규 — **Face Sculpt 확장 4종 등록**: 혼합 연령 300 · 실버폭스 300(commit `f9f93286`), **그룹 140**(2~5인, 인물마다 다른 귀 장식, commit `dd97de06`), **동종 그룹 162**(바비·브랫츠·서큐버스·인어·눈/입술/러시안 립 자매·유형 섞기, commit `684502d0`). 신규 902개. 47장(애니 피어싱)의 쪼개진 얼굴 프리셋화는 사용자가 보류. 레포 루트의 옛 핸드오프(v6.52 이하)는 **지금은 지우지 않고** 나중에 정리하기로 함.

> **v6.52 수정 사항**: 46-1 등록 현황 갱신 — **Face Sculpt v2 300 등록 완료**(commit `baa1e553`, `la_facesculpt_*` 300개 확인, 메타 재등록 불필요). 47장 신규 — **애니 피어싱 트랙**(실사+애니 한 얼굴 혼합: 단일 이미지 불가 → 좌우 2분할 → **쪼개진 얼굴(균열) 형식** 확정, 귀·귀걸이·코·러시안 립 보정 결과). v6.51(46-x 고무 피부 원인·수정, `gen_fs5/6.py`)을 포함한다.

> **v6.50 수정 사항**: 46장 신규 — **Face Sculpt Formula 전체 기록**(v6.49까지 핸드오프에 없던 얼굴 컷 작업): 확정 사양·결정 이력, v1 300 등록(commit `c02d217b`)과 **v2 300 번들(엄니 제외·입술 17종·귀 스타일·추가 축) 등록 대기**, 귀 스타일·구멍 수 규칙, 입술 12 계열(신규 6종 채택), 듀오·트리오·4·5인 규칙과 샘플, 그룹 "추는 항상 무쇠" 결함 수정, 제미나이 교훈. 확정 사양 최신본은 `LumineX_FaceAxes_Spec_v2.md`.

> **v6.49 수정 사항**: 45장 신규 — **테마 그룹 바디페인팅**(한 장면 2~7명, 사람마다 테마 색 하나: 무지개·오행·사계절·삼원색·사신·불·물·해·달). 단색 + 이름 없는 추상 문양은 전부 의상으로 읽혀 실패 → **Core 번들 원문 + 테마 색 바탕의 실존 공예 앵커 + 테마에 맞는 모티프 + 보통 체형**으로 확정. 7개 테마 시험 중 6개 통과, 등록은 미결정(집에서).

> **v6.48 수정 사항**: 44장 신규 — **수조 그룹 5인 시험**(듀얼바디 전신 5인 성공, 프레임 힙컷 5인은 #1이 발목컷으로 불안정해 제외), **등록 전 확인 시험**(짧은 방식 2·3인 4개: 프레임 힙컷 2인은 1차 발목컷·2차 성공, 나머지 3개 1차 성공), **Tank Body Formula 210개 등록**(`la_tank_210_bundle.json` + `patch_la_tank_1_json.py`, 생성기 `master/gen_tank_bundle.py`). 합계 12,318 → **12,528**(등록 스크립트 출력 12528 확인, commit `1d65b057`).
> **v6.47 수정 사항**: 43장 신규 — **듀얼바디 재질을 투명 3종(단일 투명·투명 수조·내용물 투명)으로 정리**(상체 페인트/하체 재질이 없는 구성에서만 석재 허용, **목재 듀얼바디는 L1·L3 모두 실패로 제외**), **얇은 벽 투명 수조 + 수위 단계(100/50/25/0, 75%는 가슴 높이라 제외)**, 겨드랑이 일자 경계, 가는 선 뒷배경, 물 색 선명화, 수조 한 통 연결 문장, 프레임 힙컷 그룹(2·3·4인)과 컷 끝 바닥 접촉 문구, **4인 프롬프트 길이 줄이기(동일 문장 1회만) 성공**. 상체 페인트/하체 재질의 하체 재질 1~4종 구성, 신발·메이크업 랜덤화 규칙, 테스트 프롬프트 기본 랜덤 규칙도 기록. 등록 변경 없음.

> **v6.46 수정 사항**: 42장 신규 — **재질 쪽 몸 구성 5종 정리**(프레임 컷·듀얼바디·상체 페인트/하체 재질·재질 혼합·크롭 프레임)와 **혼합 구조 트리오 시험**: 프레임 컷은 등록 문구 그대로, 받침 높이 규칙, 체형 문장에서 다리 단어 제거, 상체 실사는 의상 없이 페인트 재질로, **상체 페인트/하체 재질은 발끝까지 재질(전신)** 확정과 **경계 위치 3종(허리 컷·힙컷·허벅지 상단 컷)** 결과, 단순화 규칙(인물당 재질 하나, 듀얼바디 양다리 단계 통일). 임산부 허리컷·힙컷 샘플과 컷별 피어싱 한도 답변 기록. 등록 변경 없음.

> **v6.45 수정 사항**: 41장 신규 — **극단 체형 A/B 표현**(첨부 프롬프트 검토·A/B/C 비교 시험), **새 생성 규칙 4개**(페인트 재질 연동 A/B 60:40, 극단 체형 솔로 앉은 자세 70%, 극단 체형 하이앵글 제외, 듀오 이상 극단 포즈 7개 제외)를 `master/gen_master_v2.py`에 반영. 번들은 아직 만들지 않음(등록 변경 없음, 합계 12,318 그대로).

> **v6.42 수정 사항**: 38장 신규 — **등록 완료**: 눈썹 링+스터드 교체·목재/석재 신발 문구 C(commit `87813bef`), 극단 힐 292 + Material Mix 300 + Persona Mix 300(commit `b09bb520`). 합계 10,706 → **11,598**. 32-5·33-4·35-4·37-3의 '집에서 실행' 항목은 모두 끝남.

> **v6.41 수정 사항**: 37장 신규 — **카메라 앵글 시험**(하이앵글 70도·로우·측면·3/4 확정, 45도 하이앵글은 케바케라 제외)과 **Persona Mix 300 번들**(`la_personamix_300_bundle.json`, 미등록). 36장(컨셉·포즈·헤어)은 번들에 반영됨.

> **v6.40 수정 사항**: 36장 신규 — **컨셉(재질 짝짓기)·포즈 확장·헤어 확장 시험**(6개 모두 1차 정상, 메두사 뱀 머리 재시험 2개 정상). 번들 반영은 아직 하지 않음(허벅지 안쪽 비어 보임은 케바케로 판단해 문구 추가 안 함).

> **v6.39 수정 사항**: 34장 신규 — **배경 라이브러리 v1(70곳)**(`bg_library.py`, 시험 8곳 모두 정상)과 **새 재질 6종 시험·전체 재질 섞기 시험**(옥·도자기·청동·옻칠·호박·산호/진주조개 모두 통과, 섞기 4건 중 5인 1건 실패 → 원인 분리 시험에서 배경·트랙 어느 쪽도 단독 원인 아님, 케바케). 35장 신규 — **Material Mix Formula 300개**(`la_matmix_300_bundle.json` + `patch_la_matmix_1_json.py`, 카테고리 `🏺 Living Artifact · Material Mix Formula`, 키 `la_mm_*`, **repo 등록 대기**). 등록하면 합계 10,998 → **11,298**. 25장에 14i를 추가했다.

> **v6.38 수정 사항**: 33장 신규 — **극단 힐 추가 번들 292개**(`la_xheel_300_bundle.json` + `patch_la_xheel_1_json.py`, 카테고리 `🏺 Living Artifact · Extreme Heels Body-Art`, 키 `la_xheel_{트랙}_{그룹}_NN`, **repo 등록 대기**). 4~5인 힐·옵시디언 시험 통과(4개 모두 정상, 신발 색 일치). 등록하면 합계 10,706 → **10,998**. 25장에 14h를 추가했다.

> **v6.37 수정 사항**: 32장 신규 — **바 피어싱 노출 시험**(피어싱이 많을 때 바 중간이 노출되는 문제: 문구 A·B·C 시험, 눈썹 바는 실패가 많고 코 바는 양호 → **눈썹은 링+스터드로 교체 결정**), **눈썹 링+스터드 교체 패치**(`patch_la_brow_ringstud_1.py`, 대상 907개, 번들 사본 시험 통과·**repo 실행 대기**), **4~5인 힐 숫자 시험**(40인치 표기가 더 높음), **신발 문구 A/B/C 시험**(다리 길이 vs 체형 부피 → **C 채택**)과 **목재·석재 신발 문구 교체 패치**(`patch_la_woodstone_shoe_c_1.py`, v2 840개 + 옵션 v1 221개, **repo 실행 대기**). 합계는 10,706 그대로(교체만). 25장에 14g를 추가했다.

> **v6.36 수정 사항**: 31장 신규 — **목재·석재 포뮬러 v2 600 + 목재+석재 혼합 v2 240 등록**(commit `ef7672f5`·`b8b5a783`, 합계 9,866 → **10,706**, `(Get-ChildItem presets\la_*.json).Count`로 10466·10706 확인)과 **힐 높이·신발 색·주얼리 시험 결론**(듀오 이상 40인치 표기 유리, 몸에 그리는 4개 트랙은 숫자 효과 거의 없음, 신발 색은 패턴 색으로 직접 지정, 몸 주얼리 통과). 23장 합계 보정과 25장 할 일 14f를 갱신했다. 기존 등록분 신발 문장 교체 여부는 미결(31-5).

> **v6.35 수정 사항**: 29장 신규 — **실버폭스 Structure Pack 120 · Piercing Frame 120 · Quartz 120 등록**(commit `2ce96ba5`·`8d4a1cac`·`a695f455`)과 **한중일 얼굴 컷(CJK Face) 120 등록**(commit `14792f5c`). 합계 8,786 → **9,266**(`(Get-ChildItem presets\la_*.json).Count`로 확인 완료). 23장 합계 보정과 25장 할 일을 갱신했다. 가슴 3개 시험은 불채택으로 기록(29-7). 30장 신규 — **목재·석재 단독 포뮬러 600 등록**(commit `468e6adc`, 합계 9,266 → **9,866**).

> **v6.34 수정 사항**: 27-18 신규 — **은색 띠·선의 원인과 경계 문장 교체**: "흐릿한 전환 구역" 문장(손 한 뼘 폭)과 효과 미확인이던 보호 문장이 은색 선·띠를 만든다는 시험 결과(등록본에서도 재현)와 **맞물림 문장(변형 C)** 채택, 기존 블렌드 계열 **1,560개 직접 교체**(`patch_boundary_interlock.py`, commit `af5217a1`, 합계 불변). 28-11 신규 — **실버폭스 Material Blend 180개 등록 완료**(K 90 + 국제 90, commit `838a9071`, 합계 8,606 → **8,786**). 27-4의 4번(경계는 전부 희미하게)은 **폐기**로 표시, 23장 합계 보정과 25장 할 일을 갱신했다.

> **v6.33 수정 사항**: 28장 신규 — **Silver Fox Formula 600개 등록 완료**(K-Silverfox 300 + Silverfox 300, commit `f508ad66`, 합계 8,006 → **8,606**). 결정 사항·틀·번들 구성·시험 결과·피부 톤 B/C/D·**K 피부 금박 허용**·재현 순서·열린 과제를 기록했고, 4~10인 확장 시험에서 이레즈미 26종·UV 27종을 썼다는 안내는 **등록 프리셋의 6종/7종만 쓴 것**으로 정정했다. 23장에 8,006 이후 합계 보정 문단(피어싱·실버폭스 포함)을 추가, 25장에 실버폭스 후속 과제를 추가했다.

> **v6.32 수정 사항**: 21-3-7 신규 — 쓰리쿼터 보강·흑요암 시험 결과(보강 A·이음새 1단계 채택)와 **피어싱 확장 번들 120개 등록 완료**(commit `7e06fc78`, 합계 7,900 → 8,020).

> **v6.31 수정 사항**: 21-3-6 신규 — **피어싱 신규 번들 2종 등록 완료**(commit `b1452dd2`, 600개, 합계 7,900 예정)와 **확장 시험 4종 결과**(한도 3칸·맥시멀리스트 메이크업·앉기 앵클컷·새 재질). 앉기 계열 번들 제외, 이레즈미 조각 폐기.

> **v6.30 수정 사항**: 21-3-5 신규 — **듀오·트리오 피어싱 시험 6/6 모두 1회 성공**(재질 프레임 3·실사 크롭 3). 샌드박스 초기화 사고와 복원·백업 방법 기록.

> **v6.29 수정 사항**: 21-3-4 신규 — **임산부·맥시멀리스트 피어싱 프레임 시험**(6/6 한 번에 성공), **검은 피부 얼굴 컷 9/9**(P3~P200 × 금속·보석·쥬얼리 전 종류), **피부톤 축**(블루블랙·에보니 브라운·올리브·포셀린·알라바스터)과 알라바스터의 단계 제한(P50 이하). 등록 변경 없음.

> **v6.28 수정 사항**: 21-3-3에 **비키니 상의 버전 3/3 성공**(전환선 비키니 아래·허리·힙, 아쿠아마린) 추가. 가슴 의상 컨셉은 체형(가슴) 지정이 필요하다는 참고 기록.

> **v6.27 수정 사항**: 21-3-3 신규 — **경계 위치 시험**(쇄골 위/현재/겨드랑이 V자: 모두 좋아 보임 → 무작위 축), **상체 실사 + 하체 재질 시험**(바디페인팅 위쪽은 폐기, 크롭탱크 6/6·밴도탑 6/6 한 번에 성공, 전환선은 해부학 표지에 맞춰짐). 듀얼바디와의 관계 정리. 등록 변경 없음.

> **v6.26 수정 사항**: 21-3-2 신규 — **피어싱 + 쥬얼리 함께 쓰기 시험**(6/6, 맥시멈 가능)과 **포즈 시험**(6/6, 앉기·기대기·귀 보이기 통과, 다리를 뻗으면 앵클컷으로 생성됨). 등록 변경 없음.

> **v6.25 수정 사항**: 21-3-1 신규 — 재질 프레임 컷의 단일 재질 시험, **목재 실패 원인 진단**(살 색에 가까운 목재가 원인, 위험 단어 가설 폐기), **경계 시험 결과**(금속 칼라 불채택, 어깨 끝 틈 효과 불명 → 현재 경계 유지), **살 실사성 문장 B 채택**, 성공 기준. 등록 변경 없음.

> **v6.24 수정 사항**: 21-3 신규 — **재질 프레임 컷(조각이 허벅지·무릎에서 매끈하게 끝나는 방식) + 피어싱** 시험 결과 18개(힙컷·데미스탯·쓰리쿼터 × 5재질 혼합·몸통 3조각). 모두 통과, 프레임별 한도는 시험한 최고 단계까지 확인(힙컷 P200, 데미스탯 P150, 쓰리쿼터 P100). 문장 구조·재질 정의·배정 규칙 기록. 21-2의 크롭 방식 힙컷 계획은 이 방식으로 대체.

> **v6.23 수정 사항**: 21-2 신규 — 프레임별(얼굴·가슴·허리 컷) 피어싱 시험 결과, 개수 세는 규칙, 방식 비교(정의형·개수만·비대칭 집중형), 프레임별 단계 한도, 새로 쓴 단계 문단(P3·P5·P8·P15·P25, 집중형)과 프레임 문장. 등록 변경 없음(합계 7,300).

> **v6.22 수정 사항**: 21-1 신규 — 피어싱 P축 변천(9/28~10/01)과 **P0부터 시작하는 10단계 정의표**, 21장의 오류("v6.5의 P8~P250 6단계") 정정. 27-17 신규 — 등록 후 결정(이레즈미 꽃 문양 유지, 티어 방식)과 집에서 등록할 대기 패치(제목 720개, `la_wax_duo_01`). 등록 변경 없음(합계 7,300).

> **v6.21 수정 사항**: 27-16 신규 — 등록 후 점검 결과(금박 포함 일반·임산부 혼합 8개, 헤어 reroll 6개, Wax Formula 듀오·트리오 6개, 금박 색 혼합 쿼르텟 6개, 앱 카테고리 확인). 모두 통과했고 문제는 `la_wax_duo_01` 1개뿐. 등록 변경 없음(합계 7,300).

> **v6.20 수정 사항**: 27-15 신규 — 촛농 단일 재질 시험(솔로 1/1, 새로 작성한 듀오·트리오 5/6)과, **등록된 Material Blend 3·4혼합 중 꽃·수정·촛농이 들어간 134개 교체(commit `f140457d`)**. 합계 7,300 변화 없음.

> **v6.19 수정 사항**: 27-14 신규 — SH 2단계 구조 5종을 실제 환경(맥시멀리스트·임산부·일반인, 솔로~트리오)에서 시험(6개 중 5개 3번 안 성공)해 전부 채택하고, 구조 5종만 쓰는 **Structure Pack Formula 120개 등록(commit `3fbe489f`)**. **합계 7,180 → 7,300.** 27-13의 남은 과제 2번(SH 2단계 구조 반영) 완료.

> **v6.18 수정 사항**: 27-13 신규 — 2026-10-05 등록 완료(2혼합 교체 180 `198c90a8`, 신규 카테고리 4종 + Pregnant Blend Formula 2혼합 포함 690개 `c97a55a6`). **합계 6,490 → 7,180.** 메타 스크립트가 "🏺 Living Artifact"로 시작하는 카테고리만 받는다는 것을 발견했고, 이모지 때문에 메타에서 빠져 있던 기존 Pregnant Blend Formula 180개를 이번에 고쳐 등록했다. 23장 표 갱신.

> **v6.17 수정 사항**: 27-12 신규 — 2026-10-05 시험 결과 전체(임산부·일반인·맥시멀리스트 재질 혼합, 트랙 혼합, 2혼합, 금박 색 혼합)와 재질 선택 규칙, **등록 대기 번들 5종 + 만들 번들 1종**, 집에서 할 순서. 등록 변경 없음(합계 6,490 유지).

> **v6.16 수정 사항**: 27-11 신규 — 임산부 바디페인팅에도 새 경계 방식 적용(시험 12개 결과, **Pregnant Blend Formula 180개 신규 등록, commit `23d20cbf`**). 23장 합계 6,310 → 6,490.

> **v6.15 수정 사항**: 27-10 신규 — **연속 중복 단어 수정 완료(commit `1a77c80a`, 851개)**. 26-9 (b) 해결, 원인 중 일부가 이번 세션에서 만든 번들의 템플릿 오류였음을 기록. 27-8 갱신.

> **v6.14 수정 사항**: 27-9 신규 — **헤어 충돌 수정 완료(commit `5d52fde`, 1,919개)**. 26-9 (a) 해결, 27-8 갱신. 실제 레포 점검으로 la_* 총 6,310개가 확인돼 23장 합계 정정(6,310)이 맞았음을 검증.

> **v6.13 수정 사항**: 27-5 (e) 추가 — SH 2단계 모양(비대칭 몬드리안·큰 조각 4개·폴카도트·굵은 스트라이프·셰브론) 바디페인팅 시험 18개 결과와 구조 풀 반영 규칙. 27-7·27-8 갱신. 등록 변경 없음.

> **v6.12 수정 사항**: 27장에 재질 블렌드 확인 결과(27-5 d)와 **Material Blend 3·4혼합 180개 교체 등록(commit `500e707`)** 반영, 27-1·27-6·27-7·27-8 갱신. 이제 3·4혼합은 공예·재질 모두 새 방식이고, 2혼합 180개(공예 90 + 재질 90)만 기존 방식이다.

> **v6.11 수정 사항**: 27-3 보완 — **듀얼바디(DB) L0~L4 정의 확정**(출처: 세션 dualbody-session4, 정리 파일 v4의 15-6 계열; 다리에서 재질→실사로 바뀌는 지점 5단계 + 좌우 독립 선택 코드), SH8~SH13 재시도 결과는 **기록상 확인 근거가 없음**을 명시. 27-7·27-8 갱신(재질 블렌드 새 방식 확인용 12개 대기).

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

**피어싱**: P(개수) **10단계** P0·P3·P5·P8·P15·P25·P50·P100·P150·P200 (9/29 6단계 P8~P200 → 9/30 P15 추가 7단계 → 10/01 P0·P3·P5 추가 10단계. P250은 경계라 실험용, P300은 제외 — 변천과 정의표는 21-1); C(참/체인 밀도) 3단계 C0·C1·C2; G(보석) 7종(다이아몬드·진주·오팔·자수정·루비·사파이어·혼합); F(형태) 7종(링/후프·스터드·바·클리커·드롭·세그먼트링·혼합); S(대칭) 2단계 S0(대칭)·S1(비대칭); M(금속색) 7종(골드·로즈골드·실버·코퍼·브라스·브론즈·혼합). 참(체인)은 항상 몸 재질과 같은 색·질감(예: 사파이어 크리스털 몸=사파이어빛 체인).

**쥬얼리**: 종류 JE·JN·JB·JR·JA·JH(귀걸이·목걸이·팔찌·반지·발찌·헤어주얼리); 재질 JMG·JMS·JMR·JMP·JMX; 규모 JS1~JS3; 개수 JQ1~JQ5(1개~10개초과 맥시멀리스트). 피어싱(P축)과 쥬얼리(JQ축)는 독립 축, 숫자 합산 안 함.

### 21-1. 피어싱 P축 변천과 단계 정의 (2026-10-06 정리, 출처: 9/28~10/01 세션 기록)

**변천**

| 시점 | 체계 | 비고 |
|---|---|---|
| 9/28 오전 (옛 체계, 폐기) | 9단계 시험 후 7단계 안 **P3·P5·P9·P18·P50·P100·P150** (P35·P80 예비), 참 대용 K1·K2 | P3·P5가 이때 처음 시험됨. 사용자가 숫자를 쉽게 "5·10·25·50·100·150·200"으로 하자고 제안 |
| 9/28~29 | **6단계 P8·P25·P50·P100·P150·P200** | 옛 P3·P5·P9·P18·K1·K2 폐기. P250은 경계(실험용), P300 제외. 참은 별도 축 C로 분리 |
| 9/30 | **7단계: P15 추가** | P8→P25의 약 3배 점프를 메움. 동시에 C 3단계, G 6종, F 6종, S 2단계 확정(코드 GD·GP·GO·GA·GR·GS, FH·FS·FB·FC·FD·FG), "참은 항상 몸 재질과 같은 색·질감" 고정 |
| 10/01 | **10단계: P0·P3·P5 추가** | 쥬얼리와 같이 쓸 때 피어싱을 "살짝만" 넣으려고. 피어싱(P)과 쥬얼리(J)는 합산하지 않는 독립 축 |
| 이후 | G 7종·F 7종(각 "혼합" 추가, GX·FX), M 금속색 7종 | 추가 시점은 기록에서 못 찾음 |

**현재 P축: P0부터 10단계**

| 단계 | 정의 | 출처·비고 |
|---|---|---|
| **P0** | 피어싱 없음 (실사 몸 계열 문구: `ears bare, no piercings`) | 10/01 |
| **P3** | 아주 소량. 옛 정의: 귀 큰 링 | 옛 정의는 9/28. 정의표는 새로 만들지 않았음 |
| **P5** | 소량. 옛 정의: 귀 + 콧구멍 + 눈썹 바 | 옛 정의는 9/28 |
| **P8** | 귀 위주 | 9/29 확정 |
| **P15** | P8과 P25 사이 (**부위 정의 기록 없음**) | 9/30 추가 |
| **P25** | 귀 8, 코 4, 눈썹 바 4, 메두사, 입술 링 4, 턱 2, 턱선 2 | 9/29 확정 |
| **P50** | P25 + 볼 스터드 한 줄, 체인 2줄 | 9/29 확정 |
| **P100** | 이마·관자놀이, 광대뼈, 귀 10점씩, 체인 8줄, 밀도 문장 | 9/29 확정 |
| **P150** | 이마 세 줄, 광대뼈 두 줄, 목 스터드 열, 귀 12점씩, 체인 10줄, 밀도 문장 | 9/29 확정 |
| **P200** | P150 + 이마·광대뼈·턱선·목 열 증가, 어깨·위팔·손가락·쇄골 아래 몸 피어싱, 체인 추가 | 9/29 확정(실사 가슴 몸에서 "괜찮음") |

- **참(C)**: C0 없음, C1 참 약 10개(귀 후프·아랫입술 후프·코 링·턱 링에 매닮, **P100 이하**), C2 참 약 20개 + 턱선 체인 커튼 + 머리 위 체인(**P150 이하**). **P200에는 참을 얹지 않는다**(얼굴이 꽉 차서 산만). 참 규칙: 일반 모양만(저작권 캐릭터 금지), 눈·눈썹 근처에 매달지 않음, 쇄골보다 아래로 늘어지지 않음.
- **폐기**: P250(될 듯 말 듯, 실험용), P300(제외), 옛 P9·P18·P35·P80, K1·K2.
- **표기**: 얼굴 클로즈업 계열 키 접미어 `_p{단계}_c{0~2}` (예: `la_realface_p100_c1_012`).

**쓰임이 두 가지로 갈린다**
1. **얼굴 클로즈업 계열**(Real Face Piercing `la_realface_` 30, Glass Face 등): 위 부위별 정의와 밀도 문장, C축을 쓴다.
2. **실사 몸·임산부 계열**(Core, Pregnant, Mixed 등): 부위 정의 없이 한 문장 `{개수} {형태} piercings set with {보석} in {금속}-toned metal`(예: `15 hoops piercings set with diamonds in gold-toned metal`)만 쓰고, P0은 `ears bare, no piercings`. C축은 쓰지 않는다. 쥬얼리(J)는 별도 문단/문구.

**구 체계 프리셋 후보**: `la_pierce8mix_`(6개), `la_vesselpierce8_`(8개). 키의 "8"은 단계 수가 아니라 당시 **8개 세트**(P8·P25·P50·P100·P150·P200 + P100·C1 + P150·C2)를 가리키는 것으로 보이며(대화 맥락상 추정), 현재 10단계·G·F·M·J 축과 무관하게 만든 구 체계일 가능성이 있다. 정리 여부 미정.


### 21-2. 프레임별 피어싱 시험 결과 (2026-10-06, 사용자가 이미지를 생성해 개수를 직접 센 결과)

**개수 세는 규칙**: 떨어져 있는 피어싱 하나하나가 1개(좌우 쌍도 2개). 눈썹 바 하나는 1개. 체인·참·박힌 보석은 개수에 넣지 않는다.

| 시험 | 결과 |
|---|---|
| 얼굴 컷 6개(정면, P3·P5·P8·P15·P25·P8 가림형) | 6/6 생성. 센 개수(지시): P3 4(3), P5 6(5), P8 11(8), P8 가림형 10(8), P15 16(15), P25 24(25). 측면(30도) 컷은 양쪽 귀가 안 보여 **정면 컷으로 교체**. 가림형 헤어에 "귀 뒤로 넘김" 문장을 붙이면 귀를 가리는 문제가 거의 없었다(표본 1) |
| 개수 방식 비교(P8·P25 × 정의형·개수만·비대칭 집중형, 같은 얼굴) | P8: 11·11·7, P25: 22·21·22. **정의형≈개수만**(위치 정의가 개수 정확도를 올리지 못함). 비대칭 집중형은 오른쪽을 비우라고 하면 개수를 덜 얹어 P8에서 가장 정확했고 집중도도 지시대로 나옴("왼쪽"은 피사체 기준이라 정면 화면에서는 오른쪽) |
| 가슴 컷 6개(정면, 피어싱만) | 6/6. P8 집중형 10, P25 집중형 24, P50·P100·P150·P200 성공(P200의 쇄골·어깨·위팔 피어싱도 통과) |
| 가슴 컷 + 몸 처리 6개(공예 혼합·단일, 재질 혼합·단일) | 6/6. P8 11, P25 22, P50~P200 성공 |
| 허리 컷 + 몸 처리 6개(배꼽 바로 아래까지) | P8 12(배꼽 없음), P25 22~23·23, P50 성공, P100 성공, **P150 실패**. 배꼽 링을 넣은 4개 모두 배꼽 링이 보임 |

**결론**
- **방식**: 낮은 단계(P8·P25)는 **비대칭 집중형**(총 개수 + 한쪽 몰림), P50 이상은 **정의형**(부위·밀도). 개수만 쓰는 방식은 장점이 없어 폐기.
- **개수는 대략**: 집중형 기준 P8은 지시보다 평균 +2(7·10·11·12), P25는 평균 -2(22·24·22·22.5·23). 정의형 P3~P15는 +1~3. P50 이상은 개수가 아니라 밀도로 구분.
- **프레임별 한도**: 얼굴 컷 P3~P200, 가슴 컷 P8~P200(몸 처리 병용 가능), **허리 컷 P8~P100**(P150은 얼굴이 작아져 실패, 1건). **배꼽 링은 허리 컷에서도 가능**(프레임을 배꼽 바로 아래까지, 배가 매끈한 체형만, `the navel itself a deep dimple set in the smooth swell of her belly` 필수).
- **몸 처리 병용**: 얼굴·귀·목은 실사 살, 목선 아래부터 몸 처리. 금박·UV네온 제외. 프롬프트 1,000단어 이하 유지(P150 이상은 몸 처리 단일).

**새로 쓴 단계 문단**(`{M}`=금속색, 정의형 귀 부품은 형태 F에 따라 hoop·stud·bar 등)
- **P3**: A thick polished {M} hoop on each ear and one small {M} stud above the left one.
- **P5**: A big {M} hoop on each ear with a small {M} stud above it on the left; a small {M} ring passes through the left nostril; a thin {M} bar passes through the outer end of the left eyebrow.
- **P8**: On each ear three pieces: a big {M} hoop in the lobe, a smaller {M} ring above it and a small {M} stud at the top; a small {M} stud sits in the left nostril; a thin {M} bar passes through the outer end of the left eyebrow.
- **P15**(초안): 귀 4개씩(8) + 콧구멍 링 양쪽(2) + 눈썹 바 양쪽(2) + 아랫입술 후프 1 + 턱 라브렛 스터드·링 2.
- **P25**: 귀 4개씩(8), 코 4(중격 링·양 콧구멍 링·콧등 바), 눈썹 바 4, 메두사 1, 입술 4(아랫입술 후프·양옆 스네이크바이트·윗입술 링), 턱 2, 턱선 2.
- **집중형 P8**: "All eight piercings gather on the left side of her face and ear, and the right side stays bare" + 왼쪽 귀 5(가슴 컷은 huge hoop·ear cuff·작은 링 2·스터드) + 왼쪽 눈썹 바 2 + 왼쪽 콧구멍 링 1.
- **집중형 P25**: "All twenty-five piercings gather mostly on the left side ... the right side stays almost bare" + 왼쪽 귀 8, 오른쪽 귀 1, 왼쪽 눈썹 바 4, 콧구멍 링 2 + 중격 1, 입술 왼쪽 3, 메두사 1, 턱 2, 왼쪽 턱선 3.
- P50·P100·P150: 가슴 컷용 `gen18.py`의 T50·T100·T150 문단(귀 장식 대형화 BIGEAR 포함)을 금속색만 바꿔 사용. **P200** = P150 + "about two hundred", 목·어깨까지 덮음 + 쇄골 줄 6개씩, 어깨 스터드, 위팔 줄 5개 + 체인 12줄.
- 공통 문장: 상처 방지·눈 거리(CARE), 밀도 문장(P100 이상)은 9/28 확정 문구 그대로.

**프레임 문장**
- 얼굴 컷: `ONE woman, facing the camera straight on in a perfectly frontal portrait, her head level, both ears clearly visible on either side of her face, framed tightly from the very top of her head down to the base of her neck and the tops of her collarbones, the frame cutting off there.`
- 가슴 컷: `bust shot ... framed from the very top of her head to just below her chest, the frame cutting off beneath the chest. Her face sits large and sharp in the upper half of the frame, and her ear pieces are oversized so they read clearly at this distance.`
- 허리 컷: `waist shot ... framed from the very top of her head down to just below her navel, the frame cutting off across her lower belly. Her face sits in the upper part of the frame, large enough to read every piercing, and her ear pieces are oversized ...`

**랜덤 규칙**: 메이크업 48·헤어컬러 30은 완전 랜덤, 헤어스타일은 귀가 드러나는 노출형 16종(+ 가림형 스트레이트·웨이브·컬·샤기·울프에 "귀 뒤로 넘김" 문장), 금속색은 머리색과 대비되게(밝은 웜 머리 → 은·혼합, 밝은 쿨 머리 → 골드·로즈골드·구리·청동·황동). 아프로·락스·박스브레이드는 귀를 넘기면 부자연스러워 제외.

**남은 과제**: 힙 컷(골반뼈·허리 옆 코르셋 열 등 몸 피어싱) 시험, 얼굴·가슴·허리 3분할 합성 시험, 허리 컷 P125 같은 중간 한도 확인, 프리셋 등록 여부(카테고리·키 접두어) 결정.


### 21-3. 재질 프레임 컷 + 피어싱 (2026-10-06, 힙컷·데미스탯·쓰리쿼터)

**용어(사용자 정정)**: 재질 쪽 프레임 사다리(허리컷·힙컷·데미스탯·쓰리쿼터·앵클컷·전신)는 **카메라가 자르는 크롭이 아니다.** 몸 전체가 재질로 대체된 조각이 그 지점에서 둥글게 마감된다("조각 자체가 끝남"). 실제 생성 길이는 힙컷=허벅지 일부, 데미스탯=허벅지 중간, 쓰리쿼터=무릎 위. 얼굴·귀·목만 실사 살. 21-2의 크롭 방식 시험(얼굴·가슴·허리)과 별개 체계이며, 21-2에서 계획한 크롭식 힙 컷은 이 방식으로 대체한다. 재질 "혼합"은 한 몸 안에서 **석재·목재·단일 투명·수조 투명·내용물 투명**을 섞는 것(5재질 패치워크 구조).

**시험 결과 18개, 전부 통과**

| 라운드 | 구성 | 결과 |
|---|---|---|
| 1 | 5재질 혼합(몸통 단일): 힙컷 P50·P100, 데미스탯 P25·P50, 쓰리쿼터 P8·P25 | 6/6. 집중형 개수: 데미스탯 P25 23~25, 쓰리쿼터 P8 8~9, 쓰리쿼터 P25 24 내외(지시 대비 ±2) |
| 2 | 5재질 혼합: 힙컷 P150·P200, 데미스탯 P100·P150, 쓰리쿼터 P50·P100 | 6/6 |
| 3 | 몸통 3조각 분할(양팔·양허벅지는 각자 재질): 2라운드와 같은 6칸 | 6/6(쓰리쿼터 P100만 2회). 프롬프트 1,570~1,740단어 |

**결론**
- **프레임별 단계 한도**: 시험한 최고 단계까지 모두 통과 — 힙컷 P200, 데미스탯 P150, 쓰리쿼터 P100. 한도 자체는 아직 못 찾음(미시험: 데미스탯 P200, 쓰리쿼터 P150·P200). 크롭 방식(허리 컷 P150 실패)보다 피어싱이 잘 읽힘 — 프레임 문장의 "her face in natural scale with her body".
- **개수 정확도**: 집중형이 P8 8~9, P25 23~25로 크롭 방식(7~12)보다 정확.
- **길이**: 1,740단어까지 영향 없음(기록의 "1,000단어 초과 시 약화" 우려는 이 구조에서 확인되지 않음).
- **몸통 3조각 분할**: 조각 사이는 흐릿한 전환이 아니라 **깔끔한 이음매**. 위치는 부위 이름이 아니라 선의 방향·위치(%)(가로 3단 2개 이음매 28~78% 구간, 세로 3등분, 대각 3조각).

**문장 구조**(전체 프롬프트 ≈ 첨부 데미스탯 프리셋 구조 + 5재질 패치워크)
1. 도입: `Professional fashion photograph, {hip-cut|demi|three-quarter} multi-material portrait: real face and neck, and a sculpted body made of different materials — {부위별 재질 요약}. ONE woman, angled 45 degrees toward the camera, framed so her whole sculpted form is visible from the top of her head down to two individually rounded, deliberately carved tips {POS}, her face in natural scale with her body — never an oversized close-up crop of just the face. Where her sculpted form comes to an end at her {thighs|knees}, it is because the sculpture itself ends there, not because a camera frame happens to cut her off.` POS: 힙컷 `a short way down her thighs, just below the hip line`, 데미스탯 `a little further below the middle of her thighs`, 쓰리쿼터 `right at the knee, where the leg would bend`.
2. Subject(실사 얼굴) → Piercings(단계 문단 + 안전 문구 `All jewelry is real {metal}, sitting in real, calm, healthy skin — no redness, no swelling, no irritation ...`) → Piercing depth 문단(봉은 피부 속을 지나 양끝 스터드만 보임, 스티커처럼 붙지 않음) → Physique(+부위별 재질 요약 문장).
3. Boundary(언더암 높이 가로선 위는 실사 살, 아래는 서로 다른 재질이 어깨·엉덩이 관절과 몸통 이음매에서 맞닿음, 재질 가장자리가 살 위로 작게 솟은 단) → 부위별 문단(왼팔·오른팔·몸통(단일 또는 3조각)·왼허벅지·오른허벅지) → 이음매 문장(`sit flush against each other with a thin, clean seam ... never jagged, torn or blended`) → Setting(두 색 조명 배경 + 광택 바닥) → Pose → Lighting(투명 부위는 빛이 통과, 불투명 부위는 반사만).
4. 허벅지 끝: 고체 `ends in its own smooth, deeply polished rounded tip, finished the way a carved sculpture is finished`, 수조 `seals shut into its own smooth, rounded, closed tip`.

**재질 정의(시험에 사용)**: 석재 4(라피스라줄리·화이트 마블·블랙 그래나이트·제이드), 목재 4(파덕·월넛·에보니·마호가니), 단일 투명 12(레진·얼음·빙하·시트린·아쿠아마린·루비색·코발트·에그글라스·로즈핑크·자수정·사파이어·스모키), 수조(몸통은 단색 맑은 물, 허벅지는 물 + 벚꽃잎·반딧불이·백합 중 하나), 내용물 투명(사파이어·코발트·자수정·시트린 + 나비 또는 수정 조각이 박힘). 원본 스크립트는 `gen_demifig_pierce.py`(T1_solid·T2_vessel·T3_combined)와 5재질 패치워크 v1·v2(9/29).

**배정 규칙**: 5재질 혼합 — 팔은 석재·목재·단일 투명 중, 수조·내용물은 몸통·허벅지에만, 5종이 한 몸에 하나씩. 몸통 3조각 — 팔은 석재·목재·단일 투명, 허벅지 하나는 수조 + 나머지 하나는 석재·목재·단일 투명·내용물 중, 몸통 조각은 석재·목재·단일 투명·내용물 중 서로 다른 3종. 금박·UV네온·꽃·수정(보태니컬)·촛농은 이 계열에서 쓰지 않음. 피어싱: P8·P25는 비대칭 집중형, P50 이상은 정의형, P200은 팔이 재질이라 상완 열을 빼고 목·쇄골·어깨 줄만 늘림.

**남은 과제**: 한도 확정(데미스탯 P200, 쓰리쿼터 P150·P200), 허리컷·앵클컷·전신 프레임 확장, 프리셋 등록(카테고리·키 접두어·개수 결정), 크롭 방식(21-2)과 재질 프레임 방식(21-3)을 한 카테고리에 둘지 둘로 나눌지 결정.


### 21-3-1. 재질 프레임 컷 — 단일 재질·목재 진단·경계·살 실사성 시험 (2026-10-06)

**단일 재질 1라운드(P50 정의형, 6개)**: 단일 투명(아쿠아마린·얼음) 성공, 수조(백합 들판) 성공, 내용물 투명(코발트 유리+수정 조각) 성공, 석재(라피스라줄리, 힙컷) 2회째, **목재(파덕, 힙컷) 실패**. 투명 계열은 모든 프레임에서 안정적, 불투명 단일 재질이 어렵다.

**목재 실패 원인 진단**
- 힙컷에서 목재 4종(월넛·에보니·파덕·마호가니) × 경계 방법(현재·금속 칼라·나뭇결 맞춤 가장자리) 6개: **전부 실패**.
- **위험 단어 가설은 폐기**: 사용자가 보낸 성공본(데미스탯·웽에·P150, 2회 모두 성공)에 `snake-bite`·`swelling`·`real tissue`·`embedded`·`jagged`·`Shards`가 모두 들어 있었다(9/29 기록의 위험 단어 blood·wound·crack·fracture·spike·bite는 그때 목재 문장 안의 것이 원인이었음).
- 성공본에서 **한 가지씩만** 바꾼 6개: 쓰리쿼터 성공, **힙컷 3회째**, 제 템플릿 문장으로 교체 성공, P50 피어싱 2회째, 에보니 2회째, **파덕 실패**.
- **결론**: ① **살 색에 가까운 목재(파덕 붉은 주황, 마호가니)가 원인** — 몸 전체를 살로 읽는다. 살과 확실히 다른 어두운 색(웽에·에보니·퍼플하트)만 쓴다. ② 불투명 재질은 **힙컷에 약하다**(목재 3회째, 석재 2회째) — 단일 재질 목재·석재는 데미스탯·쓰리쿼터에서 쓰고 힙컷은 투명 재질에 쓴다. ③ 어려운 요소(힙컷·P50·붉은 목재 등)가 **겹치면 성공 확률이 곱으로 떨어진다**. ④ **5재질 혼합·몸통 3조각 구조에서는 목재 부위가 18/18 성공** — 새 피어싱 카테고리 계획에는 영향 없음.
- 웽에 문장: `dark wenge wood, a deep near-black wood finely striped with narrow gold-tan pinstripes running through it, polished to a hard satin sheen, completely opaque`, 퍼플하트: `deep violet purpleheart wood, a dense hardwood of rich purple with fine straight grain, polished to a hard satin sheen, completely opaque`.

**경계(살-재질) 시험**
- **금속 칼라(목 밑동 초커)**: 투명 재질은 영향 없음, 불투명에서 성공률 하락(웽에 실패, 석재 4회째) → **표준 경계로 채택하지 않음**.
- **어깨 끝 실루엣의 미세한 틈**(`the material's rim curves very slightly away from the skin, leaving a hairline reveal gap along the outline ... like the fitted gap between a watch case and its bezel`): 6개 성공(석재 4회째·내용물 2회째·나머지 성공), 틈 굵기 지시는 케바케(연필선 굵기와 머리카락 굵기가 크게 안 달랐음), 사용자 판단으로 단차를 키우면 "살 위에 재질이 덮여 씌워진 것" 같아 보임 → **기본 문장에서 제외**.
- **현재 경계(작은 단차 + 또렷한 그림자) 유지.** 미세 질감·미세 틈 지시는 모델이 뭉개므로 더 다듬지 않는다. "다른 재질이 합쳐진 느낌"은 경계선 하나가 아니라 **부위별 재질 구조**(5재질 혼합·몸통 분할)에 맡긴다.

**살 실사성 문장 B 채택**(6/6 통과, A는 웽에 2회째·아쿠아마린 1회, B는 둘 다 성공; 사용자 직감은 B 쪽 약간 선호, 이미지 판단은 확신 못 함) — Subject 문단 끝에 추가:
`Her neck, the hollows above her collarbones and the tops of her shoulders carry the same real living skin as her face: visible pores and fine skin grain, a soft sheen of natural skin oils on the highest planes, faint fine peach-fuzz hairs catching the rim light along the neck and shoulder line, gentle tonal variation with a natural warm flush at the base of the neck and across the collarbones, and the fine natural creases of a real neck — never airbrushed, never smooth like plastic. Like any real person she is slightly asymmetrical: a few small natural beauty marks and freckles scattered unevenly, one side of her neck and shoulder very slightly warmer and more freckled than the other.`

**성공 기준(사용자와 합의)**: 제미나이 생성이 케바케라 "한 번에 완벽"이 아니라 **3번 안에 생성되고 재질이 읽히면 통과**.

**Piercing Statue Formula 반영 규칙**: 몸은 5재질 혼합(몸통 하나)·몸통 3조각 분할(기존 계획), 목재는 어두운 색만, 경계는 현재 방식, Subject에 살 문장 B 추가. 단일 재질 변형을 넣는다면 목재·석재는 데미스탯·쓰리쿼터에서만.


### 21-3-2. 피어싱 + 쥬얼리, 포즈 시험 (2026-10-06, 데미스탯·5재질 혼합·살 문장 B)

**피어싱 + 쥬얼리 함께 쓰기 6/6** (프롬프트 1,530~1,726단어): 적절히 섞기 — P8 집중형 + JQ4(목걸이·팔찌 7~10점) 성공, P50 + JQ3(목걸이·반지 4~6점) 성공, P100 + JQ2(목걸이·팔찌 2~3점) 2회째(1회째 듀얼바디); 맥시멈 — P100 + JQ5, P150 + JQ5(목걸이·팔찌·반지·헤어 장식 전부 10점 넘는 극단), P150 + JQ4 모두 성공.
- **결론**: 피어싱과 쥬얼리를 **둘 다 극단으로 써도 된다**(서로 제한하는 규칙 불필요). **귀걸이(JE)만 제외**(귀 피어싱과 같은 자리). 10/01에 만든 P0·P3·P5는 "쥬얼리가 많을 때 피어싱은 살짝"이라는 선택지로 유지.
- **쥬얼리 문장**: `Jewelry: besides the piercings she wears {JQ} of {metal} necklaces and chains resting on her neck, collarbones and upper chest; {JQ} of {metal} bracelets and bangles on both wrists; {JQ} of {metal} rings on her fingers; {JQ} of {metal} hair ornaments set in her hair, all of it real, sitting on and over the material of her body and her real neck and hair without covering her eyes, her face or her piercings.` 위치는 Piercing depth 문단 뒤, Physique 앞. JQ1 a single piece · JQ2 two to three pieces · JQ3 four to six pieces, layered · JQ4 seven to ten pieces, heavily stacked · JQ5 well over ten pieces, an extreme maximalist stack. 금속 JMG gold · JMS silver · JMR rose-gold · JMP platinum · JMX mixed-metal. 종류 JN 목걸이 · JB 팔찌 · JR 반지 · JH 헤어 장식(JA 발찌는 데미스탯에서 안 보임).

**포즈 시험 6/6**(같은 얼굴·몸·P50, 포즈만 변경): 서기(기준), 앉기 1(긴 의자에 상체를 세우고 다리를 일자로), 앉기 2(의자 끝에서 상체를 앞으로 기울이고 팔을 허벅지 위에), 앉기 3(창가 턱에 앉아 한 손을 턱에), 기대기(바닥에 앉아 두 손으로 뒤를 짚음), 귀 보이기(서서 한 손으로 머리를 귀 뒤로 넘김) 모두 성공.
- **관찰(사용자)**: **다리를 앞으로 뻗는 앉기 계열은 주로 발목 컷으로 생성된다** — "허벅지 끝이 둥근 끝으로 끝난다"는 문장을 따르지 않고 종아리·발목까지 이어서 그린다. → **앉기·기대기는 앵클컷 프레임(복숭아뼈~종아리에서 끝남)으로 다루고, 문장도 발목 끝으로 쓰는 것이 글과 그림이 일치한다.** 서기 포즈는 힙컷·데미스탯·쓰리쿼터, 다리를 뻗는 포즈는 앵클컷.
- **앉기 문장**(허벅지 끝 기준으로 시험한 버전, 앵클 끝 문장으로 바꿔 재시험 필요): 도입 `framed so her whole seated sculpted form is visible ... tips at the ends of her thighs, which extend forward`, 이음매 문단 `Both thighs extend forward and stay clearly separate along their whole length, never merging into a single mass, each ending in its own rounded, polished tip that stops cleanly in front of her — a finished sculpture's end, never cut off.`, 소품 `The seat is a separate object, clearly distinct from her body, and her sculpted form does not merge into it.`(긴 의자 `a long, low black lacquered bench`, 의자 `a simple black wooden chair`, 창가 `a deep stone window ledge, with a tall window behind her letting in cool light`, 바닥 `directly on the glossy dark floor`). 귀 보이기 `her right hand gently tucking a lock of hair back behind her right ear so the ear and its piercings show clearly`.

**열린 과제**: 앉기 계열을 앵클컷 문장으로 바꿔 시험하고 얼굴이 작아지는 구도에서 피어싱 한도 확인(P8·P25·P50), 경계 위치 시험(쇄골 위 / 현재 쇄골선 / 겨드랑이 높이 V자 — 마네킹 같아지는지), Piercing Frame/Statue Formula 번들 생성.


### 21-3-3. 경계 위치와 상체 실사 컷 시험 (2026-10-06, 데미스탯·단일 재질·P50)

**경계 위치 시험**(쇄골 위 / 현재 쇄골선 / 겨드랑이 높이 V자, 아쿠아마린·웽에): 사용자 판단 "모두 좋아 보이고 나름 매력이 있다" → **셋 다 번들의 무작위 축**으로 쓴다(단일 재질 몸). 5재질 혼합·몸통 3조각 구조는 팔이 재질별로 어깨 관절에서 맞닿는 구조라 겨드랑이 높이 가로선 경계만 쓴다.

**상체 실사 + 하체 재질**(전환선 위는 실사 살, 아래는 재질, 가로선 하나) — 듀얼바디(다리에서 재질→실사, L0~L4)와 **같은 전환부 기법이지만 위치(몸통 높이)와 방향(위 실사, 아래 재질)이 반대**라 중복이 아니라 같은 축의 반대쪽. 합치면 "실사 상체 + 재질 가운데 + 실사 다리" 구성도 가능(미시험).
- **바디페인팅 버전**(위쪽 실사 + 공예 바디페인팅, 가슴 밑·허리·힙 × 아쿠아마린·웽에): 6/6 생성(아쿠아마린 가슴 밑만 4회째)이지만 **맨살이 안 보여 "그냥 2재질 구분한 느낌"** → **폐기**. 교훈: 맨살이 보여야 살과 재질의 대비가 생긴다.
- **크롭탱크 버전**(상체 맨살, 가슴만 검은 무광 크롭탱크, 전환선 허리·힙, 힙 선에 배꼽 링 변형): **6/6 모두 한 번에 성공, 경계 좋음.** 아쉬운 점은 의상이 있다는 것 → 나중에 하나의 카테고리로 만들 후보("상체 실사 컷").
- **밴도탑 버전**(어깨끈 없는 검은 무광 밴도탑, 전환선 밴도탑 바로 아래 / 손바닥 폭 아래 / 허리): **6/6 모두 한 번에 성공.** 전환선은 지시한 간격이 아니라 **해부학 표지에 맞춰 나뉨** — 밴도탑 바로 아래 지시는 밴도탑 근처(목재가 조금 더 위), "손바닥 폭 아래"는 배꼽 근처, 허리(배꼽 위)는 배꼽 근처 또는 배꼽 위. → 전환선은 간격 대신 **표지 3개**(옷 아래 가장자리 / 배꼽 위 / 배꼽 근처)로 정한다. (어깨 끝 틈 시험의 "굵기 지시는 케바케"와 같은 현상.)
- **비키니 상의 버전**(검은 무광 삼각 비키니 상의, 목과 등에 가는 끈, 전환선 비키니 바로 아래 / 허리(배꼽 위) / 힙(배꼽 아래), 아쿠아마린): **3/3 모두 정상 성공.** 크롭탱크·밴도탑·비키니 세 가지 모두 안정적. **참고(사용자)**: 가슴 쪽 의상(비키니·밴도탑) 컨셉을 본격적으로 쓰려면 **체형(가슴 크기·모양) 문장을 넣을 필요**가 있다 — 지금 Physique는 허리·배·힙 중심. 가능하다는 정도로만 기록, 필요할 때 시험.
- **문장**: Body `Above that line, her neck, shoulders, both arms and hands [and the bare skin of her upper belly] are her own completely bare real living skin with nothing painted on it, and only her chest is covered by a plain black matte {strapless stretch bandeau top | stretch crop tank top with thin straps} — the one garment she wears. Below that line, the rest of her body — everything from the line down to the tips of both thighs — is not painted, covered or clothed but physically made of one solid {transparent material | opaque wood} ... with no seam and no skin anywhere below the line.` Boundary `a clean, straight horizontal line runs all the way around her body {위치} — her real skin above, the sculpted material immediately below. This line is not the hem of a garment: the {bandeau|crop tank} is a separate piece of clothing sitting on her chest, and this line is where her own body changes from living skin into the carved material. At that line, the material's edge rises in a small raised step above her skin, casting a crisp shadow ...` 위치 문장: 허리 `at the narrowest part of her waist, just above her navel`, 힙 `at her hip line, just below her navel`, 옷 아래 `directly beneath her chest, a hair's width below the lower edge of the {옷}`.


### 21-3-4. 임산부·맥시멀리스트 피어싱 프레임과 피부톤 축 (2026-10-06)

**임산부·맥시멀리스트 정면 크롭 6/6 모두 1회 성공**: 임산부 허리 컷(배가 보이는 컷, 공예 바디페인팅 단일 + 배를 따라 패턴이 감김, 배꼽 링 없음) P25 집중형·P50·P100, 맥시멀리스트 얼굴 컷 P50·가슴 컷 P100(이레즈미)·허리 컷 P50(스테인드글라스). 맥시멀리스트는 검은 피부 문장 + 검은 배경 + 정면 크롭 + 안전 문구로 새로 조립했는데도 통과(기록의 "맥시멀리스트는 원문 그대로가 안정적"이라는 주의는 전신 프레임 기준이었음).

**검은 피부 얼굴 컷 9/9 모두 1회 성공**: 피어싱 P3·P5·P8·P15·P25·P50·P100·P150·P200을 하나씩, 같은 9개 안에서 피어싱 금속 7종·보석 7종·쥬얼리 개수 JQ1~JQ5·쥬얼리 금속 5종을 돌려 배정(쥬얼리는 목걸이+헤어 장식), 헤어스타일은 노출형 16종·헤어컬러 30종 랜덤. **블루블랙 피부가 피어싱과 가장 잘 맞는다**(사용자).

**피부톤 비교**(같은 P100 + JQ4 혼합 금속·혼합 보석·같은 헤어): 블루블랙이 가장 좋고 **에보니 브라운·올리브·포셀린도 괜찮음**, 마호가니·골든 브론즈는 선택되지 않아 보류.

**알라바스터(북유럽식 초백색)**: P50에서는 잘 받았으나 **P100·P150에서는 톤이 어두워짐**(피어싱 문단이 길수록 피부톤 지시의 영향이 줄어드는 것으로 추정). 톤 고정 문장(A: `Between and around the piercings her skin stays the same extremely pale alabaster white ... never darkened, greyed or shadowed by the metal.`)과 하이키 정면 조명(B)을 더해도 톤이 거의 달라지지 않음 → **알라바스터는 P50 이하에만 쓴다.**

**피부톤 축(맥시멀리스트 문장 구조 안의 피부 구절만 교체)**

| 톤 | 문장 | 쓸 수 있는 단계 |
|---|---|---|
| 블루블랙 | `THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky` | P3~P200 |
| 에보니 브라운 | `DEEP EBONY BROWN SKIN, a rich dark complexion with warm brown undertones` | P3~P200(P100 확인) |
| 올리브 | `WARM OLIVE SKIN, a smooth golden-olive complexion` | P100 확인 |
| 포셀린 | `FLAWLESS PORCELAIN PALE SKIN, a luminous fair complexion with a cool rosy undertone` | P100 확인 |
| 알라바스터 | `ALABASTER SNOW-WHITE SKIN, an extremely pale, almost translucent Nordic complexion with a cool pink undertone` | P3~P50 |
- 보류: 따뜻한 마호가니(`RICH WARM MAHOGANY SKIN, a deep reddish-brown complexion`), 골든 브론즈(`GOLDEN BRONZE SKIN, a warm sun-kissed medium-brown complexion`). 이 축은 Piercing Frame Formula의 맥시멀리스트 얼굴 컷에 랜덤 축으로 넣는다. 맥시멀리스트 얼굴 컷 문장: `Subject: A real photograph of a striking adult woman — {피부톤}, {age} goddess, {physique} physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — {desc}, {hair}. Real pores and fine skin grain on her skin, a soft sheen of natural oils, large eyes with bright real catchlights, full lips, a bold, commanding expression ...` + 검은 배경 `MANDATORY pure pitch black void background only, absolutely NO studio backdrop NO texture NO grey NO gradient` + 부드러운 정면광과 얇은 차가운 림 라이트.


### 21-3-5. 듀오·트리오 시험과 도구 복원 (2026-10-06)

**듀오·트리오 6/6 모두 1회 성공**: 재질 프레임 듀오 데미스탯(아쿠아마린 P25 집중형 + 석재 라피스 P50)·듀오 쓰리쿼터(웽에 P8 집중형 + 수조 P50)·트리오 데미스탯(아쿠아마린 P25 + 웽에 P25 + 내용물 투명 P50, 프롬프트 1,920단어), 실사 크롭 듀오 얼굴 컷(일반 P25 + P100)·듀오 가슴 컷(일반 P50 공예 + 맥시멀리스트 P50 이레즈미)·트리오 가슴 컷(일반 P25 공예 + 일반 P50 이레즈미 + 맥시멀리스트 P100 스테인드글라스). **인원수가 어긋나지 않았고 피어싱·재질 구조가 그룹에서도 유지됨** — 인물마다 재질 종류와 피어싱 단계가 달라도 된다.
- **그룹 문장 구조**: 도입(`{TWO|THREE} women standing side by side, each angled 45 degrees ...`, 간격 `Generous spacing so every figure reads clearly, nobody's arms crossing a neighbour.`) → 인물별 문단(`#1: ... #1 Piercings: ... #1 Physique: ... #1 Body: ...`) → **공통 문단은 한 번만**(`All piercings:` 안전 문구, Piercing depth, `Boundary for each woman: ...`, Setting, Pose, Lighting). 조명은 `the glowing backdrop floods every transparent body from behind, tinting it, while the opaque bodies block it completely and are lit by two large softboxes ...`. 화면비 듀오 3:4·트리오 4:5. 크롭 그룹에 맥시멀리스트가 한 명이라도 있으면 배경은 검은 void 문장.
- **결론**: 번들에 듀오·트리오를 넣어도 된다(재질 프레임·크롭 모두). 쿼르텟 이상은 미시험.

**도구 복원 사고(참고)**: 이 세션 중 샌드박스(`/home/claude`)가 초기화되어 생성 스크립트와 데이터가 사라졌고(`outputs`·`/mnt/transcripts`는 무사), 대화 기록에서 복원했다. 방법: `/mnt/transcripts`의 도구 호출(bash heredoc·create_file·str_replace·sed·cp·`python3 -c` JSON 생성)을 시간순으로 다시 실행(`extract.py` → `replay6.py`, 출력 경로는 임시 폴더로 바꿔 outputs를 보호), 빠진 번들 JSON은 outputs에서 복사. 일부 옛 데이터 JSON(`register_*_*.json` 등 무작위 배정 데이터)은 다시 생성한 것이라 원본과 값이 다를 수 있으나 시험 생성에는 영향 없음. **백업**: `LumineX_generators_backup_2026-10-06.zip`(outputs)에 생성 스크립트와 복원 도구를 저장했다 — 다음에 초기화되면 이 zip을 풀고 부족한 JSON을 outputs에서 복사한다.


### 21-3-6. 피어싱 번들 등록과 확장 시험 (2026-10-06)

**등록 완료**: Piercing Frame Formula 300(`la_pframe_{solo|duo|trio}_NNN`)과 Piercing Statue Formula 300(`la_pstatue_{solo|duo|trio}_NNN`), 번들 `la_pframe_geo_300_bundle.json`·`la_pstatue_geo_300_bundle.json`, 스크립트 `patch_la_pierce2_1_json.py` → `patch_livingartifact_2_meta.py` → git, **commit `b1452dd2`**, 합계 7,300 → 7,900(메타 출력과 앱 표시는 사용자 확인 대기). 구성: Frame = 일반 얼굴 30·가슴 30·허리 30 + 임산부 허리 50 + 맥시멀리스트 얼굴 30(피부톤 5종, 알라바스터는 P50 이하)·가슴 20·허리 20 + 듀오 60 + 트리오 30; Statue = 단일 재질 70·5재질 혼합 70·몸통 3조각 70(어두운 목재만, 단일 석재·목재는 힙컷 제외, 단일은 P100 이하) + 듀오 60 + 트리오 30. 생성기 `gen_bundle_frame.py`·`gen_bundle_statue.py`는 백업 zip에 포함.

**확장 시험 결과**
- **한도 3칸**(5재질 혼합, 살 문장 B): 데미스탯 P200 통과, 쓰리쿼터 P200 통과, 쓰리쿼터 P150은 2회째 통과(1회째 맨살 다리 일부 생성) → **힙컷·데미스탯·쓰리쿼터 모두 P200까지 통과.**
- **맥시멀리스트 메이크업 축**(검은 피부 얼굴 컷, 메이크업 6종, 기존 메이크업 문장에서 피부색 구절(`skin|complexion|tanned|porcelain|fair|pale|olive|bronze`을 포함하는 절)을 제거하고 눈·입술·블러시 절만 붙임): **6/6 모두 1회 성공, 피부색 유지**(파키스탄 브리덜 글램·블루블랙·P100만 살짝 옅음). 피부톤 4종(블루블랙·에보니 브라운·올리브·포셀린) × P50·P100에서 확인.
- **앉기 앵클컷**(5재질 혼합, 앵클컷 문장 `just above her ankle bones`, 두 다리가 앞으로 뻗어 둥근 끝): 5/6 생성(앉기 2 P25만 실패, 같은 포즈 P50은 1회 통과), 그러나 **앉기·기대기 표현이 잘 안 나옴** → **재질 프레임 번들에 앉기 계열은 넣지 않는다**(서기·귀 보이기만). 재시도하려면 포즈를 첫 문장에 올리고 프레임 문장을 줄인 판으로.
- **새 재질**(데미스탯·쓰리쿼터, 단일 재질 P50): 비늘 3종(용·잉어·인어)·스테인드글라스 1회 성공, **흑요암+금빛 이음새는 생성되나 금빛 이음새가 너무 적음**(이음새 문장 강화 필요), **이레즈미(흰 대리석 위 문양)는 생성 안 됨 → 폐기.**
- **쓰리쿼터 맨살 다리 현상**: 한도 시험 쓰리쿼터 P150 1회째와 새 재질 쓰리쿼터 인어에서 맨살 다리가 생성됨(데미스탯에서는 없음). "무릎에서 끝남" 문장이 모호해서 다리를 그리는 것으로 추정 — 쓰리쿼터 문장에 `nothing below the knee, no real skin legs`를 더 강하게 넣는 보강을 후보로 둔다.

**확장 번들 후보(미생성)**: ① Statue 확장 — 새 재질 단일(스테인드글라스·비늘 3종, 데미스탯·쓰리쿼터)과 한도 P200 반영 ② Frame 확장 — 맥시멀리스트 메이크업 얼굴 컷 ③ 흑요암 금빛 이음새 강화 시험, 쓰리쿼터 맨살 다리 보강 시험.


### 21-3-7. 쓰리쿼터 보강·흑요암 시험과 확장 번들 등록 (2026-10-06)

**시험 결과(6개)**: 흑요암 금빛 이음새 강화 1·2단계 모두 이음새가 확실히 늘어남 → **1단계를 표준**으로 채택. 쓰리쿼터 맨살 다리는 **약한 보강 A**로 두 경우(인어 비늘 단일, 5재질 혼합 P150) 모두 안 나옴, 강한 보강 B는 인어에서 1건 재발 → **A를 표준**으로 채택.
- **흑요암 문장(1단계)**: `polished black obsidian stone carved as a mosaic of many large fitted sections, divided by wide, bright molten-gold seams about the width of a finger running between every section, a dense network of gold lines covering her whole body from the collarbones to the thigh tips` (2단계는 뒤에 `; the gold seams glow and catch the light as strongly as the black stone does, so the gold reads clearly from far away and makes up about one fifth of the whole body's surface`).
- **쓰리쿼터 보강 A**: 단일 재질은 `nothing continues below either tip` 뒤에 `(no shins, no ankles and no real skin legs of any kind — below each rounded tip there is only the glossy floor)`, 혼합·몸통 분할은 마지막 문단 뒤에 `Below each rounded tip there is nothing at all — no shins, no ankles, no feet and no real skin legs; only the glossy floor.`

**확장 번들 등록 완료**: `la_pstatue_ext_001~060`(Statue 확장: 새 재질 단일 36 = 스테인드글라스 8·비늘 잉어/용/인어 21·흑요암 7, P200 반영 혼합 24 = 5재질 혼합 18·몸통 3조각 6, 쓰리쿼터 33개 전부 보강 A) + `la_pframe_maxmk_001~060`(Frame 확장: 맥시멀리스트 메이크업 얼굴 컷, 블루블랙 30·에보니 브라운·올리브·포셀린 각 10, P25~P100, 파키스탄 브리덜 메이크업 제외), 스크립트 `patch_la_pierce3_1_json.py` → `patch_livingartifact_2_meta.py` → git, **commit `7e06fc78`**, 합계 7,900 → **8,020**. 기존 카테고리에 키만 추가(새 카테고리 없음). 생성기 `gen_bundle_ext.py`는 백업 zip에 포함.

**남은 후보**: 앉기 재시험(포즈를 첫 문장에 올린 판), 상체 실사 컷 카테고리(크롭탱크·밴도탑·비키니 + 체형 문장), 신규 카테고리 티어(HOF/SSS, 사용자가 키를 텍스트로 알려주면 패치), 레포 루트 핸드오프 파일 정리(v6.9~v6.30 누적), 이전 세션 재질 카테고리 꽃·수정·촛농 점검, 구 체계 피어싱 프리셋(`la_pierce8mix_` 6·`la_vesselpierce8_` 8) 처리.

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
| Pregnant Blend Formula (v6.16 3·4혼합 180 + v6.18 2혼합 90) | 270 | `la_pregblend` |
| Pregnant Material Blend Formula (v6.18) | 180 | `la_pregmat` |
| General Material Blend Formula (v6.18) | 180 | `la_genmat` |
| Track Mix Material Formula (v6.18, 일반·임산부·맥시멀리스트) | 120 | `la_trackmix` |
| Gold Leaf Color Mix Formula (v6.18, 검은 피부 맥시멀리스트) | 120 | `la_leafmix` |
| Structure Pack Formula (v6.19, 2단계 구조 5종) | 120 | `la_s2pack` |
| 기존 카테고리(Anime·Photo Direct/Duo·Signature·Glass Face계열·Idol·Craft·Colossal 등, 등록 로그 기준) | 1,720 | 각 섹션 참조 |
| **전체 누적 합계** | **7,300** (7,180 + Structure Pack 120, 등록 로그 합산 기준) | |

> **정정(v6.9)**: v6.7·v6.8의 "약 6,181"은 합산 오류였다(그 표의 행을 더하면 5,181이었고, 기준값 1,131은 09-23 시점 값이라 이후 등록분이 빠져 있었음). 330개 등록 시점의 카테고리별 로그(42개 카테고리, 합 5,140개)를 직접 합산하고 이후 등록분(Crystal/Scale 180 + Wax/Obsidian 120 + Blend 540)을 더한 값이 6,310이다. 확인 명령: PowerShell `(Get-ChildItem presets\la_*.json).Count` — 모든 카테고리가 `la_` 접두어를 쓴다면 같은 수가 나와야 한다.

> **v6.33 합계 보정**: 위 표의 7,300 이후 등록분 — 피어싱 Piercing Frame Formula 300 + Piercing Statue Formula 300(commit `b1452dd2`) + 피어싱 확장 120(`7e06fc78`) = **8,020**, 구 피어싱 후보 14개 삭제(`350b39b4`) = **8,006**, **Silver Fox Formula 600**(`la_ksilverfox_` 300 + `la_silverfox_` 300, `f508ad66`) = **8,606**. 2026-10-07 `(Get-ChildItem presets\la_*.json).Count` = 8606 확인.
> 주의: 위 표의 행은 7,300 시점이며, 피어싱·실버폭스 행은 표에 넣지 않고 이 보정 문단으로 대신한다.

> **v6.35 합계 보정**: 실버폭스 Structure Pack 120(`la_ksilverfox_s2pack_` 60 + `la_silverfox_s2pack_` 60, `2ce96ba5`) + Piercing Frame 120(`la_ksilverfox_pframe_` 60 + `la_silverfox_pframe_` 60, `8d4a1cac`) + Quartz 120(`la_ksilverfox_quartz_` 60 + `la_silverfox_quartz_` 60, `a695f455`) + 한중일 얼굴 120(`la_cjkface_` kr·cn·jp 40씩, `14792f5c`) = 480 → **9,266**. 등록 전 8,786도 같은 명령으로 확인했다(위 v6.34 문단의 "계산값"은 확정).

> **v6.35 합계 보정(2)**: 목재·석재 단독 포뮬러 600(`la_wood_` 300 + `la_stone_` 300, `468e6adc`) = **9,866**(`(Get-ChildItem presets\la_*.json).Count`로 확인).

> **v6.36 합계 보정**: 목재·석재 포뮬러 v2 600(`la_wood2_` 300 + `la_stone2_` 300, `ef7672f5`) = **10,466**(확인), 목재+석재 혼합 v2 240(`la_wsmix_` 듀오·트리오·4인·5인 각 60, `b8b5a783`) = **10,706**(확인).

> **v6.37 합계 보정**: 변동 없음. 32장의 교체 패치 2종은 기존 파일만 고치므로 합계는 **10,706** 그대로다(실행 전후 `(Get-ChildItem presets\la_*.json).Count` 동일해야 한다).

> **v6.34 합계 보정**: 실버폭스 Material Blend 180(`la_ksilverfox_blend_` 90 + `la_silverfox_blend_` 90, `838a9071`) = **8,786**(계산값; 확인 명령 `(Get-ChildItem presets\la_*.json).Count`는 아직 실행 전). 경계 문장 교체 1,560개(`af5217a1`)는 기존 파일만 고쳐서 합계에 영향이 없다.

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

### 실버폭스(28장 관련, v6.33)
12. 얼굴 사실감 짝 비교 → 효과가 있으면 K·국제 600개 후처리 치환 여부 결정
13. 피어싱(클로즈업 프레임에 실버폭스 인물), 쥬얼리, 석영 단일 섹션 시험
14. 후기 40대 상한, 한중일 세트 여부, 신규 카테고리 티어(사용자 키 전달 대기)
14a. **실버폭스 Structure Pack**: 맥시멀리스트 인물만 있는 기존 소스가 31개(솔로 18·듀오 5·트리오 8)뿐이라 변환만으로는 부족 → 구조 5종(스트라이프·셰브론·몬드리안·폴카도트·큰 조각)을 맥시멀리스트 인물로 새로 생성한 뒤 맞물림 문장(27-18)으로 만든다. 28-11 참조.
14b. **재질 설명 문장이 이미지에 글자로 나오는 현상**(블렌드 시험에서 변형 B·C 모두 일부) — 재시도로 해결되는지, 문장 위치 조정이 필요한지 관찰.
14c. **(v6.35) 한중일 얼굴 컷 후속**: 생성 결과(정상/이상) 확인, 티어 부여(사용자 키 전달 대기), 바 피어싱이 살 속으로 들어가지 않고 전체가 노출되는 문제 개선 시험(\"보이는 결과\"를 묘사하는 문구 2샘플 시험 제안, 미결정), 주근깨 비중(현재 1개), 5·6갈래 혀(번들 미포함), 가부키·조선 궁중 메이크업 포함 여부.
14e. **(v6.35) 목재·석재 600 후속**: 생성 검증(정상/이상)과 티어 부여, 4~5인 정상 비율 확인, 작은 카테고리 정리·보강 후보(`la_fix_photoreal` 1·`la_fill` 2·`la_vessel` 3·`la_duostatue` 4·`la_ceramic` 10·`la_convert` 13은 용도 미확인, `la_ussbbw` 20·`la_hgussbbw` 30·`la_muscle` 29는 체형 계열로 추정).
14d. **(v6.35) 실버폭스 3종 후속**: Structure Pack·Piercing Frame·Quartz 생성 검증과 티어 부여.
14f. **(v6.36) 31장 후속**: ① 바디페인팅·이레즈미·UV네온·왁스(+혼합 트랙) 기존 등록분의 신발 문장 처리 결정(31-5; 권고는 "새 것에만 적용 + 추가 번들") ② 목재·석재 v2 840개 생성 검증(정상/이상)·티어 ③ 솔로 힐 숫자 표기 유무의 효과 반복 확인(케바케) ④ 아직 받지 못한 시험 결과: `LumineX_WoodStone_BBW_MakeupOnly10.md`, `ExtremeHeels_Tracks6`, `ExtremeHeels_Bright3`, `WoodStone_AllAxes6`, `Registered_Sample6`, `Groups6`, `Face_Random4` ⑤ 옵시디언 트리오 힐 시험은 왁스와 같은 문법이라 생략했다(필요하면 추가).
14i. **(v6.39) 34·35장 후속**: ① `patch_la_matmix_1_json.py` 실행·등록(35-4) ② 검증 샘플 6개(`LumineX_MaterialMix_Verify6.md`)는 **6/6 정상 생성**(등록 전 번들에서 직접 뽑은 것) ③ 배경 라이브러리를 기존 번들에도 쓸지(기존 등록분은 건드리지 않음) ④ 극단 힐 번들(33장)과 이 번들의 생성 검증·티어.
14h. **(v6.38) 33장 후속**: ① `patch_la_xheel_1_json.py` 실행·등록(33-4) ② 생성 검증(정상/이상)과 티어 ③ 이레즈미·UV네온 솔로 원본 프롬프트가 30개 중 8개뿐(중복)이라 번들은 각 8개.
14g. **(v6.37) 32장 후속**: ① 집(repo)에서 교체 패치 2종 실행·커밋(32-5; 순서와 확인 방법 있음) ② 아직 받지 못한 결과: 목재·석재 v2 검증 샘플 8개(`LumineX_WoodStone_v2_Verify8.md`), 바 피어싱 2차의 3번(P150 문구 A), 그리고 14f④의 옛 시험 파일들 ③ 새 프리셋 규칙: 눈썹은 링+스터드(바 금지), 목재·석재 신발은 문구 C, 바디페인팅·이레즈미·UV네온·왁스 신발은 인물별 패턴 색 지정(31-3) ④ 극단 힐 추가 번들(바디페인팅·이레즈미·UV네온·왁스 + 신발 색 일치)은 아직 만들지 않았다 ⑤ 솔로 힐 숫자는 케바케라 40인치 표기와 숫자 없음을 섞어 쓴다 ⑥ 옵시디언 트리오 힐 시험은 생략(왁스와 같은 문법).
15. 피어싱 정리 때 삭제된 옛 백업 5개(`core/builders.py.bak`·`hof_tier.py.bak`·`presets_meta.py.bak`·`sss_tier.py.bak`, `dashboard.py.bak`) 복구 여부 — 복구 명령 `git checkout 7e06fc78 -- core/builders.py.bak core/hof_tier.py.bak core/presets_meta.py.bak core/sss_tier.py.bak dashboard.py.bak`

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
- 이 방식으로 Craft Blend 3·4혼합 180개(commit `b990556`)와 Material Blend 3·4혼합 180개(commit `500e707`)를 교체 등록했다(27-6). 2혼합은 그대로다.
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
- **9월 30일 중간본(14종)과의 차이**: 중간본은 SH1~SH7 확정, SH8~SH14 "탈락 이력"이었다(체커보드는 재질 3개 이상에서 깨짐, 찢어진 종이는 손상처럼 보일 위험, SH14 정규 2×2 격자는 SH3이 더 나아 밀림). 10월 1일 최종본에는 SH1~SH13이 "확정 13종"으로 올라가 있고 SH14는 웨이브로 바뀌었다(2×2 격자는 격자 시스템 GR2로 통합). 탈락 7종의 재시도 프롬프트를 만든 직후(약 9분 뒤) 사용자가 다른 주제(가로·세로 확장)로 넘어갔고, **재시도 결과를 보고하거나 확정한 대화는 세션 기록에 없다.** 최종 목록이 SH1~SH13 확정으로 기록된 것은 이의가 없었기 때문으로 보이며, SH8~SH13이 실제로 안정적인지는 기록상 확인되지 않는다.
- **듀얼바디(DB)** — 재질 몸에서 *다리의 어느 지점까지 재질이고 그 아래부터 실사인지*를 정하는 축(재질 전용, 바디페인팅과 무관). 출처: 세션 `2026-09-30-05-02-45` (dualbody-session4), 정리 파일 `LumineX_body_pose_makeup_material_pool_v4.md`의 15-6 계열(15-6l 상단 경계 확정, 15-6m 단계표), 통합 문서 B8.

| 단계 | 실사 범위 | 재질 범위 |
|---|---|---|
| L0 | 없음 | 발끝까지 전부 재질(기존 Demi Statue 전신과 동일, 기준점) |
| L1 | 허벅지부터 신발까지 | 힙~허벅지 위쪽만 재질 |
| L2 | 무릎부터 신발까지 | 힙~무릎 위까지 재질 |
| L3 | 복숭아뼈부터 신발까지 | 힙~종아리 끝까지 재질 |
| L4 | 발톱 너비만큼, 발가락 끝만 | 힙~발·신발 전체가 재질(신발도 유리) |

  - 코드 `DB-[왼다리]-[오른다리]`: 두 다리의 단계를 각각 독립적으로 고른다. 같으면 대칭, 다르면 비대칭이라 별도 대칭 코드는 필요 없다. 기본 5종은 DB-L0-L0·L1-L1·L2-L2·L3-L3·L4-L4. 비대칭은 인접 단계끼리 5종이 확인됐다(DB-L0-L1·L1-L2·L2-L3·L3-L4·L4-L0, 예: 왼다리는 무릎부터 실사, 오른다리는 발끝까지 재질). 이론상 5×5=25가지 중 나머지 15개는 미검증.
  - 같은 전환부 기법이 팔(아래팔+손), 좌우 반쪽, 손 하나 같은 특정 부위에도 성공해서 "다리 전용 표기"지만 몸 어느 부위에나 적용 가능하다.
  - L4에서 얻은 교훈: (1) 재질로 확정할 부위는 소속 목록뿐 아니라 내용물이 흐르는 문단에도, 최소 두 곳에 반복해서 적는다. (2) 아주 작은 실사 비율은 "아주 작게" 같은 막연한 표현 대신 "발톱 너비만큼" 같은 구체적 크기 비유나 "복숭아뼈" 같은 정확한 해부학적 지점으로 쓴다.
  - 스타킹·바디페인팅 다리는 불안정해서 보류, 맨다리+신발 다양화가 안전한 결론.
  - **프레임 6단계**(조각 자체가 그 지점에서 끝남, 15-7)와 DB(다리에서 재질→실사로 전환)는 서로 다른 축이다.
- 가로 2~10줄(SHH)·세로 2~3줄(SHV) 확장안도 논의됐으나 확정 기록은 못 찾았다.

### 27-4. 바디페인팅용 경계 설계 원칙 (어휘집)
1. **모양 이름이 아니라 구조로 분해한다.** 영역 구조(띠, 중심점을 둘러싼 동심 영역, 중심에서 퍼지는 쐐기)와 경계선 모양(매끈, 물결)을 따로 랜덤으로 뽑는다. 목록을 고정하지 않고 위치 숫자(1% 단위)와 방향까지 랜덤으로 둔다.
2. **프롬프트에는 모양 이름을 쓰지 않는다.** 체커보드·헤링본·셰브론·폴카도트·스트라이프는 원단 프린트로 흔해서, 이름 없는 추상 문양 4종이 옷 프린트로 읽혀 전부 실패한 것(26-4)과 같은 위험이 있다. 모양 이름은 제목·메타에만 쓴다. 구역 안은 실존 전통 공예명으로 채운다.
3. **신체 부위 이름을 구역마다 나열하지 않는다.** chest·belly·sternum·pelvis·inner thighs 같은 부위어는 최소화하고, "figure의 중심", 위에서 몇 % 높이, 시계 방향 같은 기하학 표현만 쓴다. (부위어 2~9개를 쓴 레이아웃 15개 테스트는 생성 실패가 많았고, 성공했던 분할 문구는 0~2개였다. 직접 비교 실험은 아니라 추정이다.)
4. **경계는 전부 희미하게.** *(v6.34: 이 문구는 은색 선·띠를 만든다는 것이 확인돼 폐기하고 27-18의 맞물림 문구로 교체했다. 아래는 이력용으로만 남긴다.)* 문구 원형:
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

**(d) 재질 블렌드 확인 12개** (새 방식 9개: 솔로 3·듀오 3·트리오 3, 3~4구역 / 등록분 직접 대조군 3개). 사용자가 보낸 결과의 라벨이 전부 "새 방식"이어서 번호 기준으로 다시 집계했다(대조군은 03·06·07번).

| 구분 | 보고 | 1회 | 3번 안 |
|---|---|---|---|
| 새 방식 | 7개 | 5 (71%) | 6 (86%) |
| 등록분 | 3개 | 3 (100%) | 3 (100%) |

- 새 방식 인원별(1회/3번 안/보고): 솔로 2/2/2, 듀오 2/3/3, 트리오 1/1/2. 11번(트리오 3구역)과 12번(솔로 4구역) 결과는 받지 못했다.
- 실패 1개(04번, 트리오 3구역)는 인물 3명 중 2명에 목재가 들어 있었다. 원인 불명.
- 표본이 작아 두 구분 사이의 차이는 가릴 수 없었고, 정해둔 기준(눈에 띄게 낮지 않으면 교체)에 따라 교체를 진행했다. 팔·다리 맨살은 등록분(03·07번)에서도 보고돼 방식의 문제가 아니라 원래 약한 부위로 본다.

**(e) SH 2단계 모양 바디페인팅 시험 18개** (솔로, 2단계 5종 × 3개 = 15개 + 검증된 1단계 구조 대조군 3개, 생성은 3회까지 시도하되 그 이상 시도한 경우는 별도 기록)

| 구조 | 1회 | 3번 안 | 개수 | 판정 |
|---|---|---|---|---|
| 굵은 스트라이프 | 3 | 3 | 3 | 채택 |
| 셰브론 | 2 | 3 | 3 | 채택 |
| 비대칭 몬드리안 | 2 | 2 | 3 | 조건부(4구역까지) |
| 폴카도트 | 1 | 2 | 3 | 조건부(3~4구역까지) |
| 큰 조각 4개 | 2 | 2 | 3 | 보류 |
| 대조군(1단계) | 2 | 2 | 3 | — |

- 2단계 15개 전체: 1회 10개(67%), 3번 안 12개(80%), 4번 시도까지 13개.
- **서로 다른 패턴이 5종인 시험 2개가 가장 약했다**: 몬드리안 5구역은 4회째에 성공, 폴카도트 5구역(패치 4개)은 실패. 패턴 5종을 5줄 스트라이프에 반복 배치한 경우는 패턴 3종이어서 1회 성공(구역 수가 아니라 서로 다른 패턴 수가 문제로 보임). 5종을 제외한 13개는 1회 10개(77%), 3번 안 12개(92%).
- 큰 조각 4개의 실패 1건은 분기 위치가 27/41%(간격 14%)로, 성공한 36/54%·25/50%(간격 18%·25%)보다 좁았다. 작은 조각이 생겨서일 수 있다는 가설뿐이다(표본 1개).
- 대조군 중 이전에 5/5로 안정적이던 부채꼴 3구역이 4회째에 성공했다. 모양당 3개 표본에서 2/3와 3/3의 차이는 이 정도 변동 안에 있어서 확정적이지 않다.
- 경계가 맨살로 보였다는 보고 3건(몬드리안 1, 스트라이프 1, 대조군 1)은 대조군에서도 나와 2단계 구조만의 문제가 아니다. 채움은 이전 결정대로 크게 보지 않는다.
- **구조 풀 반영 규칙(다음에 3·4혼합을 다시 만들 때 적용, 지금 교체 등록은 하지 않음)**: 서로 다른 패턴은 4종까지. 스트라이프(가로·세로·대각, 4~5줄, 패턴 2~3종 반복)와 셰브론(3~4구역)은 채택, 몬드리안은 4구역만, 폴카도트는 3~4구역만, 큰 조각은 분기 간격 20% 이상으로 제한한 뒤 재시험하고 그 전까지 보류. 구조 문장 형식은 `LumineX_SH_Stage2_Test_18.md`의 프롬프트를 따른다.

### 27-6. 교체 등록 (commit `b990556`: Craft Blend, commit `500e707`: Material Blend)
- 대상: `la_craftblend{3|4}_{solo|duo|trio}_{01~30}` 180개를 같은 키로 덮어씀. 번들 `la_craftblend_geo_180_bundle.json`, 패치 `patch_la_craftblend_geo_1_json.py`. 카테고리·키가 같아 메타 등록은 필요 없다.
- 인물마다 구조 5종 × 경계선 2종에서 랜덤(한 이미지 안에서 구조 중복 없음), 위치 숫자 1% 단위. 구조 문장 360개 중 321개가 서로 다르다(89%).
- 기존과 달라진 점: 프롬프트가 약 40~50% 길어짐(예: 트리오 4혼합 1,838~2,039단어, 기존 1,249~1,385). 포즈는 구역이 보이는 정면 계열만 사용(기존은 뒷모습 포함 19종). 보호 문장 추가. 메이크업 설명 속 머리 묘사 제거(26-9)는 이전과 동일.
- 바꾸지 않은 것: 2혼합(공예 90, 재질 90). 등록 합계 6,310은 그대로.

**Material Blend 교체 (commit `500e707`)**
- 대상: `la_matblend{3|4}_{solo|duo|trio}_{01~30}` 180개를 같은 키로 덮어씀. 번들 `la_matblend_geo_180_bundle.json`, 패치 `patch_la_matblend_geo_1_json.py`. 메타 등록은 필요 없다.
- Craft Blend와 같은 구조 문장·희미한 경계·보호 문장을 쓰고, 재질 문장은 `Region N is ...: it carries {재질}.` 형식. 재질 16종(공작눈무늬 포함)에서 인물마다 랜덤(66~93회씩 사용), 구조 5종 × 경계선 2종은 인물 360명이 31~42명씩 고르게 배정, 구조 문장 360개 중 321개가 서로 다름.
- **석재와 목재는 한 인물에 같이 넣지 않는다**(3~4혼합에서는 미검증 조합이라 제외, 기존 번들에는 포함돼 있을 수 있었음). UV네온이 들어간 인물 81명에는 해당 구역 전용 블랙라이트 문장이 붙는다.
- 기존과 달라진 점: 프롬프트가 약 35% 길어짐(예: 트리오 4혼합 1,541~1,697단어, 기존 1,100~1,235), 포즈는 정면 계열만 사용, 보호 문장 추가.
- 되돌리려면 이 커밋만 `git revert`한다. 옛 `patch_la_blend_1_json.py`를 다시 돌리면 Craft Blend 교체분까지 옛 버전으로 덮어쓰므로 쓰지 않는다.

### 27-7. 알려진 한계·미결정
- **2혼합**: 2구역이 약하다는 결과가 있어서 새 방식으로 다양화하지 않았다. 등록된 2혼합(공예 90 + 재질 90)이 같은 약점을 가졌는지는 미확인.
- **Material Blend 3·4혼합(180개)**: 확인 12개(27-5 d) 후 새 방식으로 교체했다. 재질 쪽에서 새 방식의 검증은 7개(3번 안 6개 성공) 규모로 작고, 11·12번 결과가 없다. 교체분의 실제 성공률은 평소 사용하면서 확인한다.
- **기존 등록분의 헤어 충돌·중복 색상어**(26-9)는 수정하지 않았다.
- **채움**(팔·다리·종아리~발목 맨살)은 원래 약한 부위로 두기로 했다.
- SH8~SH13의 안정성은 기록상 확인되지 않는다(27-3). 듀얼바디 L0~L4 정의는 27-3에서 확인했다.

### 27-8. 다음 할 일
1. **2혼합(공예 90 + 재질 90) 처리 결정.** 2구역이 약하다는 결과(27-5)가 있어 새 방식으로 다양화하지 않았다. 등록된 2혼합이 같은 약점을 가졌는지는 미확인.
2. (시험 완료) SH 2단계 모양 결과는 27-5 (e). 풀에 넣을 구조(스트라이프, 셰브론, 몬드리안 4구역, 폴카도트 3~4구역)를 3·4혼합 재생성 시 반영할지, 별도 카테고리로 추가할지 결정. 큰 조각은 분기 간격 가드레일 후 재시험.
3. (완료) 헤어 충돌(27-9)과 연속 중복 단어(27-10)는 모두 수정했다. 기존 등록분 정리는 끝났다.
4. 교체한 3·4혼합 360개와 신규 임산부 블렌드 180개(27-11)의 사용 중 성공/실패 피드백 반영(재질 시험 트리오 실패 04번의 원인, 11·12번 미수신 결과 포함).
5. SH8~SH13은 기록상 재시도 결과가 없어서, 바디페인팅 구조 후보로는 3단계 보류 상태로 두고 필요할 때 시험.
6. 레포 루트에 핸드오프 v6.9·v6.10·v6.11이 모두 올라가 있음 — 최신본만 남기고 정리할지 결정.

### 27-9. 헤어 충돌 수정 (commit `5d52fde`, 2026-10-04)
- **문제**(26-9 a): 메이크업 설명 48종 중 33종에 머리 묘사가 이미 들어 있는데, 별도 헤어 문구가 또 붙어 한 인물의 머리가 두 번 서로 다르게 적혀 있었다. 구 헤어 문구는 "wavy hair", "low bun hair"처럼 스타일만 있는 8종뿐이라 머리 색 축이 없었다.
- **수정**: `preset_builders/patch_hair_conflict_fix.py`(모드 `remove`/`reroll`, `--apply`가 없으면 점검만). 이번에는 `reroll`로 적용했다. 충돌 문장(메이크업 속 머리 문장 32종 절)을 지우고, 구 헤어 문구 8종을 새 축("`{색상 30종} hair styled in {스타일 31종}`")으로 교체한다. 같은 프리셋 안의 모든 인물에게 적용, 키를 시드로 써서 재실행해도 결과가 같고 이미 수정된 파일은 다시 바뀌지 않는다. HOF/SSS 티어 파일에 올라 있는 키는 건너뛰는 옵션이 있으나 이번에는 해당 키가 없었다.
- **결과**: 1,919개 수정 — Core 682, Fixed Combo 134, Random Combo 70, Mixed7 119, Mixed(일반+임산부) 443, Pregnant 471. 다른 카테고리 4,060개는 변경 없음(그중 371개는 머리 묘사가 하나뿐이라 충돌이 아니어서 제외).
- **점검 중 발견한 결함**: 시험용 번들(2,250개)에 없던 다른 카테고리(Five-Material Patchwork 등) 263개에서, 머리 묘사가 하나뿐인 프리셋을 충돌로 오인했다(적용했다면 그 프리셋의 유일한 머리 묘사가 지워졌을 것). "별도 헤어 문구가 함께 있을 때만 충돌"이라는 조건을 넣어 해결했다. 교훈: 시험 데이터에 없던 카테고리는 실제 레포에서 점검 실행으로 먼저 확인한다.
- 이 수정의 효과는 생성 성공률로 검증하지 않았다(모순된 문장 제거가 목적이며, 제미나이의 케바케가 커서 소규모 시험으로는 효과를 가릴 수 없음). 되돌리려면 이 커밋을 `git revert`한다.
- 앞으로 `face()` 메이크업 설명을 쓰는 번들을 새로 만들 때는 머리 묘사 절을 제거한 버전(`face_nohair`, 정규식 `HAIRW`)을 써야 같은 충돌이 다시 생기지 않는다.
- 같은 점검 출력에서 la_* 프리셋이 총 6,310개로 확인됐다(23장의 정정된 합계와 일치).

### 27-10. 연속 중복 단어 수정 (commit `1a77c80a`, 2026-10-04)
- **문제**(26-9 b 확장): 프롬프트 안에 같은 단어가 연달아 두 번 나오는 문구. 점검 스크립트 `preset_builders/patch_duplicate_words_fix.py`(기본은 점검만, `--apply`로 수정)로 다섯 가지를 한 단어로 줄였다.
- **결과**: 851개 수정 — `VIVID VIVID` 2,043회(스테인드글라스 300개, Fixed/Random Combo, Mixed7, Scale 포함), `extreme extreme` 149회, `dense dense` 74회, `BLAZING BLAZING` 8회, `formations formations` 1회. 접두어별: Core 27, Craft Blend 2혼합 49·3혼합 44·4혼합 52, Material Blend 3혼합 1, Fixed Combo 92, Random Combo 61, Mixed7 205, Scale 20, Stained Glass 300. 나머지 카테고리는 변경 없음. 수정은 연속 중복 한 단어만 지우도록 단어 단위로 검증했다(중복 외 변경 0, 재실행 시 변경 0).
- **원인**: (1) 이전에 만든 색 팔레트 값에 `VIVID`·`BLAZING` 접두어가 이미 들어 있는데 템플릿이 또 붙임. (2) **이번 세션에서 만든 번들의 템플릿 오류**: 신발 문구가 `Footwear: extreme {shoe}`인데 신발 설명이 이미 "extreme platform ..."으로 시작("extreme extreme"), 공예 문구 `dense {fill}`의 fill이 이미 "dense ..."로 시작("dense dense"), UV 문양명이 이미 "... formations"로 끝나는데 `{문양명} formations in {색}`으로 붙임.
- **교훈**: 템플릿에 값을 끼워 넣을 때 그 값이 같은 단어를 이미 포함하는지 확인한다. 번들을 만든 뒤에는 연속 중복 단어 스캔(`\b(\w+) \1\b`)을 검증 항목에 넣는다. 번들 생성기를 다시 쓸 때는 위 세 가지(신발·공예 fill·UV 문양명)와 색상 접두어 제거(`strip_pref`)를 반영해야 한다.
- 되돌리려면 이 커밋을 `git revert`한다. 이 수정으로 등록 합계(6,310)는 변하지 않았다.

### 27-11. 임산부 블렌드 (commit `23d20cbf`, 2026-10-04)
- **시험 12개**(새 방식 9개: 솔로 3·듀오 3·트리오 3, 패턴 3~4종 / 등록된 임산부 프리셋 대조군 3개). 새 방식은 **전부 3번 안에 생성**(1회 6개 = 67%, 2회 3개, 실패 0). 대조군은 솔로가 첫 시도에 의상으로 나와 2회째에 정상, 트리오는 1회, 듀오는 결과를 받지 못했다. 패턴과 경계는 새 방식 전부에서 좋다고 보고됐고, 팔·다리 맨살은 등록분에서도 보고돼 방식의 문제가 아니라 원래 약한 부위로 본다(이전 결정대로 크게 보지 않음).
- **문장 구조**: 등록된 임산부 문장 구조를 그대로 유지(체형 문단, 얼굴, 피어싱·쥬얼리, 포즈, 배경·조명)하고, 공예 1종 문장만 "패턴 3~4종 + 구조 문장 + 구역별 서술 + 희미한 경계 + 보호 문장"으로 교체했다. 배는 `The bands of every pattern curve fully around her belly like contour lines circling a globe, the rounded surface of her belly staying fully covered as part of whichever region it falls in, with the same density continuing in full strength over her bust` 문장으로 어느 구역에 속하든 끝까지 덮이게 했다. 구조 문장 자체에는 부위 이름이 없다.
- **데이터**: 체형은 임산부 안정 11종(근육형 제외), 피어싱·쥬얼리·나이·분위기·신발은 기존 등록 분포에서 추출, 헤어는 새 축(색 30 × 스타일 31)이고 메이크업 설명 속 머리 묘사는 제거, 포즈는 등록분의 정면 5종. 같은 이미지 안에서 구조·체형·메이크업이 겹치지 않는다.
- **등록**: 신규 카테고리 `🤰 Living Artifact · Pregnant Blend Formula`, 키 `la_pregblend{3|4}_{solo|duo|trio}_{01~30}` 180개(2혼합은 2구역 약점 때문에 제외). 인물 360명이 구조×경계선 10가지에 32~43명씩 고르게 배정, 구조 문장 360개 중 321개가 서로 다름. 기존 Pregnant Formula(공예 1종)는 그대로. 번들 `la_pregblend_geo_180_bundle.json`, 패치 `patch_la_pregblend_1_json.py`(+ 메타 등록 스크립트).
- 프롬프트가 등록분보다 약 1.7~2배 길다(솔로 653~828단어 vs 436, 듀오 1,278~1,595 vs 789, 트리오 1,872~2,218 vs 1,049). 시험 범위에서는 길이가 문제로 보이지 않았다.
- 등록 합계: 6,310 → 6,490.
- 미적용: 임산부 몸에 **재질**(크리스탈·비늘 등)을 섞는 방식, 임산부 2혼합.

### 27-12. 2026-10-05 시험 결과와 등록 대기 번들

**공통 규칙(신규 번들부터 적용)**
- 혼합 재질에서 **꽃(보태니컬)·수정(크리스탈)·촛농(왁스)은 쓰지 않는다**(사용자 결정: 돌출형은 빈 공간이 많고 가짜 같으며, 촛농은 단독은 잘 되지만 혼합에서는 중간에 끊겨 보인다). 이미 등록된 Material Blend 3·4혼합 180개는 일단 유지(해당 재질이 들어간 프리셋 105/270, 원하면 나중에 교체).
- 이미지당 **UV네온 인물은 1명**까지, UV네온은 맥시멀리스트에게만. 석재+목재는 한 인물에 같이 넣지 않는다.
- **팔 올린 자세는 새 번들에서 뺀다**(증거는 약하나 비용이 작음). 프롬프트의 오타(`it., no fabric`, `chest,,`)와 연속 중복 단어를 생성 단계에서 고친다.
- 시험 확인은 **기본 6개 규모**, 성공/실패 번호만 받는다(최대 3회 시도).

**시험 결과**

| 시험 | 결과 | 결론 |
|---|---|---|
| 임산부 + 재질 12(새 방식 9 + 대조군 3) | 새 방식 9/9 3번 안(1회 8), 대조군 3/3 1회 | 임산부 재질 혼합 가능. 꽃·수정 포함 프롬프트 5개 모두, 미포함 4개 중 2개에서 팔·다리 맨살 보고 |
| 트랙 완전 혼합 12(일반인은 별도 문단 구조) | 3번 안 9/12, 실패 3개 모두 일반인 포함, 일반인 솔로 1/3, 의상처럼 나온 사례 | 일반인 문장 형식이 문제(아래 재도전에서 확인) |
| 임산부·맥시멀리스트 혼합 12 | 3번 안 11/12(1회 5), 실패 1개는 UV네온 인물 2명 이미지 | UV 이미지당 1명 규칙 |
| 임산부 2혼합 6 + 일반인 재질 재도전 6(일반인도 임산부 융합 문장 구조 사용) | 임산부 2혼합 6/6 3번 안(1회 4), 일반인 재질 6/6 1회 | 일반인 보류 해제: 실패 원인은 트랙이 아니라 문장 형식 |
| 일반인 포함 트랙 혼합 6 | 6/6 3번 안(1회 5, 2회 1) | 트랙 혼합 번들에 일반인 포함 |
| 금박 색 혼합 10(맥시멀리스트 틀) | 3번 안 7/10. 솔로 2·4·6색 3/3 1회, 듀오 5색·트리오 2·4색 1회, 쿼르텟 3색 2회. 실패: 듀오 3색, 트리오 6색, 쿼르텟 5색 | 한도: 이미지 전체 구역 수(인원×색 수) 12 이하 — 솔로·듀오 2~6색, 트리오 2~4색, 쿼르텟 2~3색 |
| 임산부 금박 6 | 3번 안 2/6(트리오만 2회 성공) | 접음 |
| 일반인 금박 3 | 솔로 3색 3회, 솔로 5색 2회(금박 엉성), 듀오 3색 실패 | 접음 |
| 금박 + 피부톤 교체(맥시멀리스트 틀 유지) | 앞 3개 중 솔로 5색 2회 성공, 듀오 3색·솔로 3색 실패(남은 3개는 하지 않음) | 접음 |

→ **금박은 검은 피부 맥시멀리스트 문장 구조에서만 쓴다**(15-8의 "재질 자체가 거부 원인" 기록과 일치).

**일반인 재질 문장 구조**: 일반인 몸 재질 혼합은 별도 문단(Subject/Physique/Skin/Body) 구조에서 약했고, 임산부 융합형 구조(한 문단, "fused with N materials instead of ordinary skin below the collarbones ... one continuous second skin", 비임산부 체형·포즈 사용)로 바꾸자 6/6 1회 성공.

**등록 대기 번들(번들 파일과 패치 스크립트는 만들어 둠, 사용자가 집에서 하나씩 등록)**

| 번들 | 개수 | 키 / 카테고리 | 비고 |
|---|---|---|---|
| 2혼합 교체 v2 | 180(공예 90 + 재질 90) | `la_craftblend2_*`, `la_matblend2_*` 덮어쓰기 | 패턴·재질 2종을 3~4구역에 번갈아 배치, 메타 등록 불필요 |
| 임산부 재질 블렌드 | 180 | `la_pregmat{3|4}_*` / 신규 Pregnant Material Blend Formula | 메타 등록 필요 |
| 트랙 혼합 | 120 | `la_trackmix{3|4}_{duo|trio}_*` / 신규 Track Mix Material Formula | 일반·임산부·맥시멀리스트 3트랙, 메타 등록 필요 |
| 임산부 2혼합 | 90 | `la_pregblend2_*` / 기존 Pregnant Blend Formula에 키 추가 | 메타 등록 필요 |
| 일반인 재질 블렌드 | 180 | `la_genmat{3|4}_*` / 신규 General Material Blend Formula | 메타 등록 필요 |
| 금박 색 혼합(만들 번들) | 약 120 | 신규 카테고리 | 사용자가 집에서 "해줘" 하면 생성. 검은 피부 맥시멀리스트, 솔로·듀오·트리오·쿼르텟 각 30개, 위 구역 한도 |

등록이 모두 끝나면 합계는 6,490 + 180 + 120 + 90 + 180 + 금박 약 120 = 약 7,180(2혼합은 덮어쓰기라 변화 없음).

**집에서 할 순서**: ① 금박 번들 생성 요청("해줘") → ② 번들을 하나씩 등록(덮어쓰기인 2혼합 교체 먼저) → ③ 등록이 끝날 때마다 알려주면 마지막에 핸드오프 합계 갱신 → ④ 선택: 레포 루트에 쌓인 핸드오프 파일(v6.9~) 정리.

**남은 선택 과제**: SH 2단계 구조(스트라이프·셰브론 채택, 몬드리안 4구역까지·폴카도트 3~4구역까지 조건부, 큰 조각 보류)는 다음에 3·4혼합을 다시 만들 때 풀에 반영. 등록된 Material Blend 3·4혼합의 꽃·수정·촛농 포함분 교체 여부. 등록된 프리셋 전체의 생성 확인·티어 부여는 아직 하지 않았다.

### 27-13. 2026-10-05 등록 완료 (commit `198c90a8`, `c97a55a6`)

| 커밋 | 내용 |
|---|---|
| `198c90a8` | 2혼합 교체 180개(공예 90 `la_craftblend2_*` + 재질 90 `la_matblend2_*`) 덮어쓰기. 패턴·재질 2종을 3~4구역에 번갈아 배치, 재질은 꽃·수정·촛농·팔 올린 자세 제외 |
| `c97a55a6` | 신규 690개: Pregnant Material Blend 180(`la_pregmat{3|4}_*`), Pregnant Blend Formula 2혼합 90(`la_pregblend2_*`), General Material Blend 180(`la_genmat{3|4}_*`), Track Mix Material 120(`la_trackmix{3|4}_{duo|trio}_*`), Gold Leaf Color Mix 120(`la_leafmix_{solo|duo|trio|quartet}_*`). 메타 등록 결과 `categories added=5, keys added=870`(870 = 신규 690 + 아래 정정분 180) |

**메타 스크립트 규칙(중요)**: `patch_livingartifact_2_meta.py`는 카테고리명이 **"🏺 Living Artifact"로 시작하는 프리셋만** 받고 다른 이모지는 `[WARN] skipped (category not Living Artifact)`로 건너뛴다. 앞서 `23d20cbf`로 등록한 Pregnant Blend Formula 180개는 내가 🤰를 써서 파일만 만들어지고 앱 카테고리 메타에서 빠져 있었다. `patch_la_new5_1_json.py`가 기존 `la_pregblend3_*`·`la_pregblend4_*`의 이모지를 🏺로 고치고 신규 번들도 🏺로 만들어서, 이번 메타 실행으로 한꺼번에 등록됐다(Pregnant Blend Formula는 270개). **교훈**: 새 카테고리는 반드시 🏺로 만들고, 등록 때 메타 출력의 `[WARN]` 줄을 확인한다. 등록 전에는 번들·패치 파일이 `preset_builders\`에 있는지 먼저 확인한다(`Get-ChildItem preset_builders\...`) — 첫 시도는 파일이 없어서 실행되지 않았다.

**신규 번들 규칙 요약**: 구조 5종(가로·세로·대각 띠, 동심원, 부채꼴) × 경계선(매끈/물결)을 인물마다 랜덤(한 이미지 안에서 구조 중복 없음), 위치 숫자 1% 단위, 희미한 경계 + 보호 문장. 재질은 꽃·수정·촛농 제외, 석재+목재 동시 제외, UV네온은 맥시멀리스트에게만 이미지당 1명, 팔 올린 자세 제외, 오타·연속 중복 단어는 생성 단계에서 제거. 일반인·임산부는 임산부 융합형 문장 구조, 맥시멀리스트는 대문자 문장 구조. 금박은 검은 피부 맥시멀리스트만, 이미지 전체 구역 수(인원×색 수) 12 이하(솔로·듀오 2~6색, 트리오 2~4색, 쿼르텟 2~3색).

**등록 합계**: 6,490 → **7,180**.

**남은 과제(모두 선택 사항)**
1. 등록된 Material Blend 3·4혼합 180개 중 꽃·수정·촛농이 들어간 프리셋(105/270) 교체 여부.
2. SH 2단계 구조(스트라이프·셰브론 채택, 몬드리안 4구역까지·폴카도트 3~4구역까지 조건부, 큰 조각 보류)를 3·4혼합 재생성 때 풀에 반영할지.
3. 레포 루트에 쌓인 핸드오프 파일(v6.9~v6.17)을 최신본만 남기고 정리할지.
4. 등록된 프리셋 전체의 생성 확인·티어 부여는 아직 하지 않았다. 새로 등록한 카테고리를 쓰다가 안 되는 번호가 생기면 알려주기.

### 27-14. SH 2단계 구조 실제 환경 시험과 Structure Pack 등록 (commit `3fbe489f`, 2026-10-05)

**시험 6개**(2단계 구조 5종을 맥시멀리스트·임산부·일반인 문장 구조의 재질 혼합에서 솔로·듀오·트리오로 확인, 큰 조각은 분기선 간격 20% 이상으로 제한): **3번 안 5/6(1회 3, 2회 2, 실패 1)**.

| 번호 | 구성 | 결과 |
|---|---|---|
| 01 | 트리오(맥시 3명: 큰 조각·셰브론·폴카도트) | 1회 |
| 02 | 트리오(일반·임산부·맥시: 스트라이프·몬드리안·셰브론) | 실패 |
| 03 | 듀오(일반 2명: 몬드리안·스트라이프) | 2회 |
| 04 | 솔로(맥시: 스트라이프) | 1회 |
| 05 | 듀오(임산부 2명: 셰브론·폴카도트) | 1회 |
| 06 | 솔로(임산부: 큰 조각) | 2회 |

- 실패한 02번의 구조 3개는 모두 다른 이미지에서 성공했다. 세 트랙이 섞인 트리오이고 프롬프트가 1,936단어로 가장 길어서 구조보다 그쪽이 원인일 가능성(표본이 작아 확정 못 함) → 새 번들의 트리오는 트랙을 최대 2종까지만 섞는다.
- **큰 조각 4개**: 분기선 간격을 20% 이상으로 제한하자 2개 모두 성공(01번 1회, 06번 2회). 보류를 풀고 채택.
- **채택 조건**: 굵은 스트라이프(4줄, 재질 2~3종 반복), 셰브론(3~4구역), 비대칭 몬드리안(4구역), 폴카도트(3~4구역), 큰 조각 4개(분기선 간격 20% 이상). 서로 다른 재질은 4종까지.

**Structure Pack Formula 등록**: 신규 카테고리 `🏺 Living Artifact · Structure Pack Formula`, 키 `la_s2pack_{solo|duo|trio}_{01~40}` 120개(번들 `la_s2pack_geo_120_bundle.json`, 패치 `patch_la_s2pack_1_json.py`). 메타 결과 `categories added=1, keys added=120`, `[WARN]` 없음. 인물 240명의 구조 분포는 비대칭 몬드리안 58·큰 조각 51·굵은 스트라이프 49·폴카도트 44·셰브론 38, 트랙은 맥시멀리스트 98·일반인 79·임산부 63(트리오는 트랙 1종 19개, 2종 21개). 이미지 안에서 구조가 겹치지 않고 꽃·수정·촛농·팔 올린 자세·오타는 0개, UV네온은 이미지당 1명 이하. 이미 등록된 번들은 바꾸지 않았다. **등록 합계 7,180 → 7,300.**

**남은 과제(모두 선택 사항)**: ① 등록된 Material Blend 3·4혼합 180개 중 꽃·수정·촛농이 들어간 105/270개 교체 여부 ② 레포 루트에 쌓인 핸드오프 파일(v6.9~v6.18) 정리 ③ 등록된 프리셋 전체의 생성 확인·티어 부여(미실시) ④ 새 카테고리를 쓰다가 안 되는 번호가 생기면 알려주기.

### 27-15. 촛농 단일 재질 시험과 Material Blend 134개 교체 (commit `f140457d`, 2026-10-05)

**촛농 단일 재질 시험**(사용자 의견: 촛농은 단독은 잘 되지만 혼합에서는 중간에 끊겨 보인다)
- 등록된 Wax Formula 솔로 1개: 1회 성공. 등록된 듀오 1개: 생성 안 됨(해당 프롬프트에는 한 명에게 뒤돌아선 자세와 몸 부위 나열 표현, 촛농인데 "untattooed skin"이라는 어긋난 마지막 문장이 있었다. 원인이 이것인지는 불명).
- 새로 작성한 듀오 3개·트리오 3개(정면 계열 포즈만 사용, "full torso both legs" 같은 부위 나열 표현 제거, 마지막 문장 "NO bare skin visible anywhere"로 정리): **3번 안 5/6** — 듀오 3/3(1회 1, 2회 2), 트리오 2/3(1회 2, 실패 1).
- 결론: 촛농은 **단일 재질로는 그룹에서도 대체로 된다.** 혼합에서는 제외 유지. 새 문장이 등록분보다 낫다는 것은 표본이 작아 확정하지 못했다. 등록된 Wax Formula 60개(`la_wax_*`)는 바꾸지 않았다.

**Material Blend 3·4혼합 교체**
- 등록된 `la_matblend{3|4}_{solo|duo|trio}_*` 180개 중 꽃(보태니컬)·수정(크리스탈)·촛농이 들어간 프리셋이 **134개**(인물 기준 꽃 72, 수정 74, 촛농 86)였다. 이 134개를 새로 만들어 **같은 키로 덮어썼다**(번들 `la_matblend_replace_134_bundle.json`, 패치 `patch_la_matblend_replace_1_json.py`, 메타 등록 불필요). 해당 재질이 없던 46개는 그대로 둔다.
- 새 프리셋: 꽃·수정·촛농·팔 올린 자세 제외, 석재+목재 동시 제외, UV네온 이미지당 1명 이하, 문장부호 오타 제거. 재질 13종이 62~91회씩 고르게 쓰였고 꽃·수정·촛농 잔존 0, 프롬프트 길이는 기존과 비슷(솔로 468~591, 듀오 921~1,151, 트리오 1,404~1,680단어).
- 등록 합계 7,300 변화 없음(덮어쓰기).

**남은 과제(모두 선택 사항)**: ① 교체하지 않은 3·4혼합 46개와 기존 번들 일부에 남아 있는 문장부호 오타(`it., no fabric`)·팔 올린 자세를 문자열 패치로 정리할지 ② Wax Formula 듀오·트리오 40개를 새 문장으로 바꿀지 ③ 레포 루트에 쌓인 핸드오프 파일(v6.9~v6.19) 정리 ④ 등록된 프리셋 전체의 생성 확인·티어 부여(미실시).

### 27-16. 등록 후 점검 결과 (2026-10-05, 사용자가 앱에서 직접 생성)

| 점검 | 결과 | 결론 |
|---|---|---|
| 금박이 들어간 일반·임산부 재질 혼합 8개(`la_genmat3_duo_02`, `la_genmat3_solo_11`, `la_genmat3_trio_04`, `la_pregmat3_trio_21`, `la_pregmat4_solo_08`, `la_s2pack_solo_01`, `la_trackmix4_duo_13`, `la_s2pack_duo_33`) | 3번 안 8/8(1회 6, 2회 1, 3회 1), 금박은 모두 정상 생성 | 금박은 혼합 속 한 구역으로는 일반·임산부에서도 문제없다. 해당 프리셋 269개의 금박 제거 교체는 **불필요**(단독·다색은 여전히 접음) |
| 헤어 reroll로 바뀐 프리셋 6개(`la_core_trio_32`, `la_preg_quartet_20`, `la_mixed_quintet_03`, `la_mix3_3b_preg2bp1_08`, `la_mixedrand_duo_22`, `la_mixed7_decet_03`) | 6/6(1회 5, 2회 1), 헤어 모두 정상 | reroll(27-9) 문제 없음 |
| Wax Formula 듀오·트리오 6개(`la_wax_duo_01·07·18`, `la_wax_trio_04·11·20`) | 5/6(1회 4, 2회 1), 실패는 `la_wax_duo_01` 1개 | 그룹 전체 교체는 불필요. `la_wax_duo_01`은 앞선 시험에서도 실패한 같은 프리셋(뒤돌아선 자세 포함)이라 이 1개만 문제 — 원하면 새 문장으로 개별 교체 |
| 금박 색 혼합 쿼르텟 6개(`la_leafmix_quartet_01·10·15·21·26·29`) | 6/6 모두 1회 | 쿼르텟(구역 합 12 이하) 안정적 |
| 앱에서 새 카테고리 목록 확인(`la_pregblend{2|3|4}_`, `la_pregmat{3|4}_`, `la_genmat{3|4}_`, `la_trackmix{3|4}_`, `la_leafmix_`, `la_s2pack_`) | 모두 확인 완료 | 메타 등록·이모지 수정 정상 |

**열린 과제**
1. 이레즈미 문양 26종 중 꽃 문양 8종(koi sakura, chrysanthemum, wisteria, plum crane, peony, iris field, lotus pond, orchid)을 혼합에서 유지할지 결정(제외한 것은 돌출형 보태니컬뿐이며, 이레즈미는 평면 잉크라 유지를 권고).
2. 재질명이 제목에 없는 번들(`la_pregmat`, `la_genmat`, `la_trackmix`, `la_s2pack`)의 제목 개선(프롬프트 문구에서 재질을 읽는 문자열 패치로 가능).
3. 이전 세션 재질 카테고리(`la_grid_`, `la_shape_`, `la_5mat_`, `la_dualbody*_`)에 꽃·수정·촛농이 몇 개 들어 있는지 점검.
4. 목재·석재 단독 포뮬러(`la_wood6_` 6개, `la_stone5_` 5개)가 얇음.
5. `la_wax_duo_01` 개별 교체 여부.
6. 점검을 통과한 신규 카테고리의 HOF/SSS 티어 부여, 레포 루트 핸드오프 파일(v6.9~v6.20) 정리.

### 27-17. 등록 후 결정과 대기 중인 패치 (2026-10-06)

**사용자 결정**
- 이레즈미 문양 26종 중 꽃 문양 8종(koi sakura, chrysanthemum, wisteria, plum crane, peony, iris field, lotus pond, orchid)은 혼합에서 **유지**(평면 잉크라 돌출형 보태니컬 제외 원칙과 별개).
- **티어(HOF/SSS) 부여**: 100개 넘는 프리셋의 사진을 Claude에게 보여줄 수 없으므로 사진 검토 방식은 쓰지 않는다. 사용자가 앱에서 쓰다가 마음에 드는 프리셋의 **키를 텍스트로** 알려주면 티어 파일 패치를 만든다(한꺼번에 하지 않아도 되고 모일 때마다 가능).

**대기 중인 패치(집에서 등록, 아직 미등록)**
1. 제목에 재질명 추가 720개: `la_titles_patch_bundle.json` + `patch_la_titles_1_json.py`(`la_pregmat`·`la_genmat`·`la_trackmix`·`la_s2pack` 600개는 재질명, `la_leafmix` 120개는 금박 색 이름). 프롬프트는 건드리지 않고 `title`만 바꾼다. 메타 등록 불필요, 실행 후 커밋.
2. `la_wax_duo_01` 교체: 교체용 프롬프트를 시험해 **정상 생성** 확인. `la_wax_duo01_replace_bundle.json` + `patch_la_wax_duo01_1_json.py`(1개 덮어쓰기, 키·카테고리·제목·메타는 기존 그대로). 위 1번과 함께 한 번에 실행·커밋하기로 함.

**남은 선택 과제**: 구 체계 피어싱 프리셋(`la_pierce8mix_`, `la_vesselpierce8_`) 처리, 이전 세션 재질 카테고리(`la_grid_`, `la_shape_`, `la_5mat_`, `la_dualbody*_`)의 꽃·수정·촛농 포함 수 점검, P15·P3·P5 부위 정의 필요 여부, 레포 루트 핸드오프 파일 정리.

---

### 27-18. 은색 띠·선의 원인과 경계 문장 교체 (2026-10-07~08, commit `af5217a1`)

**발단**: 실버폭스 재질·구조 혼합 시험 6개가 모두 생성됐으나 사용자가 "경계가 은색 띠처럼 보이고 맨살이 비친다"고 보고. 등록본에서도 같은 현상인지 대조했다.

**대조 결과(사용자 보고, 성공/실패 번호 외에 현상 설명 포함)**
- 실버폭스로 바꾸기 **전 원본(등록본) 4개**(`la_matblend3_solo_16`·`la_matblend4_solo_06`·`la_matblend3_duo_24`·`la_matblend3_trio_01` 틀)에서도 후광·배꼽 주변 방사형 빛(동심원 틀), 경계 주위 눈썹 모양, 은색 띠가 나왔다 → **실버폭스 변환의 문제가 아니다**(원본에는 "silver"라는 단어가 없다).
- 등록본 3개(`la_matblend4_solo_10`·`la_matblend3_duo_11`·`la_matblend4_trio_13`): 솔로는 **경계와 무관하게 몸을 3등분하는 가로 일직선 은색 선**(몸 밖까지), 트리오도 경계마다 은색 선, 듀오는 거의 경계 없이 좋음. 사용자는 "등록 때는 이런 기억이 없다"고 했다.
- **기록 대조**: 27-5(b)의 희미한 경계 확인 10장은 경계 O 7·△ 2·X 1이고 3장에서 살이 띠처럼 비친다는 보고가 있어 **보호 문장**("Even inside a transition zone the skin is never left bare ... a mixture of the two, fully covers it")을 추가했는데 효과는 확인한 적이 없다. 이후 (c)(d) 확인은 생성 여부와 재질 판독만 봤고 경계는 보지 않았다(경계 체크리스트는 하지 않기로 한 사용자 결정). 즉 **보호 문장과 "손 한 뼘 폭의 흐릿한 전환 구역" 문장은 둘 다 경계 모양이 검증된 적이 없다.**

**실패한 시도**: 경계를 "또렷하고 정확히 맞물린 가장자리, 머리카락 굵기의 자연스러운 선 하나"로 바꾼 crisp판 — 사용자 판단: "일부러 실선을 만드는 건 별로, 재질끼리 맞물려서 자연스러운 경계면이 나와야지 띠처럼 선을 넣는 게 아니다" → **폐기**(선 문구 금지).

**A/B 시험 4개**(등록본 `la_matblend4_solo_10` 솔로, `la_matblend3_duo_11` 듀오 × 변형 B·C)
| 변형 | 내용 | 솔로 | 듀오 |
|---|---|---|---|
| B | 보호 문장만 삭제 | 가로 일직선 은색 선 + 재질 설명 문장이 이미지에 나옴 | 경계마다 은색 선 |
| C | B + 전환 구역 문장을 맞물림 문장으로 교체 | 경계 자연스럽고 패턴 좋음(재질 설명 문장은 나옴) | 은색 선 없음, 경계 라인만 살짝 진함 |
→ 보호 문장만 빼는 것으로는 부족하고 **전환 구역(손 한 뼘 폭, 서로 녹아든다) 문장이 은색 선을 만든다**는 쪽이 유력하다(추정; 각 틀 1회 생성이라 확정은 아님).

**C 시험**: 실버폭스 6개(동심원 2·부채꼴 2·은색 선이 심했던 트리오 틀 포함) 중 5개 은색 띠가 사라지고 아주 가는 자연스러운 경계 라인만 남았으며, 1개(국제 듀오, 띠 구조만)는 경계가 희미해지고 살이 약간 보였다. 기존 카테고리 6개(Craft·Pregnant Material·General Material 트리오·Structure Pack 폴카도트·Gold Leaf Mix·Pregnant Blend 2혼합) **6/6 성공, 은색 띠 보고 없음**(일부 어깨~팔 맨살은 케바케로 수용).

**채택한 문구(변형 C)** — 재질/패턴/금박 색/패치에 따라 4가지:
```
Where two regions meet, the materials interlock naturally: elements of one reach into the other
and the two materials simply touch, so the boundary is made only of the two neighbouring
materials, each in its own colours, with no gap between them.
```
- 패턴판: `the patterns ... motifs of one ... the two patterns ... neighbouring patterns, each in its own colours`
- 금박 색판: `the leaf colours ... flakes of one ... the two colours ... neighbouring colours, with no gap between them`
- 패치판(Structure Pack 폴카도트·큰 조각): `Where a patch meets the background, the two materials interlock naturally: ... so the edge of every patch is made only of the patch's material and the background material, each in its own colours, with no gap between them.`
- 삭제한 문장: "The boundaries between regions are hazy and feathered ...", "Each transition zone is about a hand's width wide ... never a hard edge.", 보호 문장 전부. 유지한 문장: 구조 문장("parallel hazy transition zones ...")과 "Each transition zone follows a smooth, even course / gently undulating wave ..."(시험한 C도 이 둘을 남겼다).

**교체 등록**: 교체용 번들 대신 `preset_builders/patch_boundary_interlock.py`로 레포의 프리셋 파일을 **직접 고쳤다**(재질명 제목 패치 720개·중복 단어 수정 851개 등 레포에만 있는 수정을 되돌리지 않기 위해). 시험 실행(기본)과 `--apply`, 이미 바뀐 파일은 건너뜀(재실행 안전), 바꾼 파일은 `meta.boundary = "interlock-v1"`. 대상 **1,560개**: Craft Blend 270·Material Blend 270·Pregnant Blend 270·General Material Blend 180·Pregnant Material Blend 180·Gold Leaf Color Mix 120·Structure Pack 120·Track Mix Material 120·Piercing Frame 30. 모의 레포로 먼저 시험(1,560개 전부 교체, 2회차 0개), 실제 시험 실행·적용 모두 1,560개·실패 0개. 합계 불변.

**새 규칙**: 앞으로 만드는 구역 혼합 번들은 **맞물림 문장**을 쓴다(흐릿한 전환 구역·보호 문장·선 문구 금지). 생성 후 검사에 "hand's width / dissolve / hazy and feathered 없음"을 넣는다.

**알려진 한계**: 재질 설명 문장이 이미지에 글자로 나오는 현상(B·C 모두, 이전에도 가끔), 어깨~팔 맨살, 표본이 작음(모두 1회 생성 기준), 원인은 가설. 이전 규칙(27-4의 4번)을 믿고 만든 이후 번들이 없도록 위 새 규칙을 우선한다.

**부수 발견**: 원본 번들 `la_matblend3_solo_26`에 "formations formations" 중복이 있었다(레포 파일은 27-10 중복 수정에서 이미 처리됐는지 미확인; 실버폭스 쪽은 고쳐서 생성).

---

## 28. Silver Fox Formula (v6.33, 2026-10-07)

새 실버폭스 시리즈. 옛 SF·KSF(`sf_`, `ksf_` 등)와 별개의 **Living Artifact 카테고리 2종**으로, K(한국)와 국제(블루블랙)에 같은 패턴 풀을 쓴다. **등록 완료**(commit `f508ad66`, 600개, 합계 8,006 → **8,606**, PowerShell `(Get-ChildItem presets\la_*.json).Count`로 확인).

### 28-1. 결정 사항 (사용자)

- 접두어·개수: `la_ksilverfox_`(K) 300 + `la_silverfox_`(국제) 300 = 600. 카테고리명 `🏺 Living Artifact · K-Silverfox Formula` / `🏺 Living Artifact · Silverfox Formula`(메타 스크립트가 🏺로 시작하는 것만 받으므로 필수).
- 옛 실버폭스 접두어 구분(사용자 파악): `ksf_`, `sf_`, `korean_silverfox_`, `silverfox_`는 실버폭스 계열, `mature_korean_silver_`는 의상 컨셉이라 제외. 옛 시리즈는 삭제하지 않고 그대로 둔다.
- **전 시리즈 의상 없음**: 몸은 바디페인팅·재질이 덮고 신발·손톱만 있다. 옷이 나오면 실패로 본다.
- 인물: 은발 통일, 실버폭스 연령 40대 초반~50대 초반(early 40s·mid 40s·late 40s·early 50s; 40대 후반 상한 여부는 나중에), 분위기는 아름답고 예쁘고 섹시하고 우아하게. 국제형은 가장 잘 되는 **블루블랙 피부**.
- 대비 인물: 그룹의 약 30%에 **20대만**(early/mid/late 20s) 1명(6인 이상은 1~2명), 20대 헤어컬러는 **랜덤**(은발 계열 제외, 30색 중 24색).
- 한 섹션만 쓰는 그룹은 **바디페인팅·이레즈미·UV네온 세 가지**만(전체의 약 30%). 나머지 섹션(스테인드글라스·금박·식물·해태)은 혼합 그룹에서만.
- 패턴 풀은 K와 국제에 **동일**(일본 스타일을 일본형에만 넣지 않듯 해태도 K 전용 아님). 금박은 처음엔 국제 전용이었으나 **K도 허용**(28-6).
- 피어싱·쥬얼리·석영·얼굴 사실감은 이번 번들에서 제외하고 별도 트랙.

### 28-2. 틀 (문법)

- **기준 틀 = HOF/맥시멀리스트 문법**(Core 틀은 실버폭스에서 의상·맨살이 나와 폐기). 사용자가 제공한 성공 HOF 실버폭스 4개(트리오·듀오 등)를 뼈대로 값만 교체.
- 등록된 맥시멀리스트 번들(`la_maximalist_bundle.json`)의 인물 블록에서 **나이/피부/헤어 절**과 **패턴 절**만 바꾸는 치환 방식. 프레임: `Professional fashion photograph, full body shot. N women standing side by side.` → 인물 `#k: ...` + `#k: {신발·손톱 줄}` → `Environment: MANDATORY pure pitch black void ...` + `All: ... 8K {비율}`. 솔로는 라벨 없음. 6~10인은 16:9("significantly wider than it is tall"). UV 전원 그룹은 블랙라이트 틀(`UV blacklight illumination only ...`).
- 헤더: 국제 `THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion darker than night sky, {나이} silver fox goddess, {체형} physique THE MOST EXTREME ...`, K `Korean silver fox goddess {피부 문구} elegant silver-era maturity, {나이}, {체형} physique ...`, K 20대 `Korean idol goddess {피부 문구} youthful fresh glow, {나이}, ...`.
- 체형은 등록 풀 8종(super hourglass, wide hip narrow, BBW bombshell, curvy petite, amazon bombshell, latina curves, hourglass bombshell, powerlifter bombshell).
- 확장 축: 신발 24종(패턴 색과 맞춤; 스테인드글라스·식물·금박은 `ink_of`로 색을 뽑아 맞춤), 은발 스타일 16종, 손톱 모양 3종(stiletto·coffin·almond) × 마감 5종(glossy·matte·chrome·glittery·holographic).

### 28-3. 번들 구성 (600)

| 인원 | 솔로 | 듀오 | 트리오 | 쿼르텟 | 퀸텟 | 6인 | 7인 | 8인 | 9인 | 10인 |
|---|---|---|---|---|---|---|---|---|---|---|
| 카테고리당 | 60 | 50 | 50 | 40 | 30 | 20 | 15 | 15 | 10 | 10 |

- 제목 형식: `K-Silverfox Duo #06 (한국 · 실버폭스 1 + 20대 1 · 혼합(스테인드글라스·바디페인팅) · 체형 super hourglass/BBW bombshell)` (체형·섹션 포함 — 사용자 선호). 이 틀에는 메이크업 축이 없어 메이크업은 제목에 없다.
- 메타: `group_size, aspect_ratio, format:"silverfox", kind:"K"/"I", sections, contrast_20s, single_section`.
- 규칙: UV네온은 혼합 이미지에서 1명(UV 전원 그룹은 블랙라이트 틀), 꽃·수정·촛농은 혼합에 쓰지 않음(석영은 단일 섹션으로 따로), 금박 전원 그룹은 **4인까지**(금박 색이 보라·에메랄드·크림슨·마젠타 4가지뿐이라 5인 전원은 구조상 불가), 혼합 그룹의 금박은 1명. 금박이 들어간 그룹: K 96, 국제 88.
- 패턴 풀: 이레즈미 26종(실사용 25), UV 27종, 바디페인팅 공예 41종 + 해태 1종(공예 풀 안의 한 항목; 처음엔 인물의 약 8%가 해태여서 15/2310 비중으로 낮춤), 스테인드글라스, 식물, 금박(4색).
- 자체 검증(0 오류): 600개 모두 고유, 인원 수, 한글 없음, 연속 중복 단어 없음(`VIVID VIVID`는 치환으로 제거), UV 규칙, 20대 수와 메타 일치, 국제형은 블루블랙 문구·K는 없음.

### 28-4. 시험 결과 (모두 사용자 보고, 성공/실패 번호)

| 단계 | 내용 | 결과 |
|---|---|---|
| 뼈대 재현 | K 솔로·듀오·트리오, 국제 솔로·트리오 | 5/5 성공(K 솔로 3회째, K 듀오 2회째, 트리오는 1회째 상단에 체형 영단어가 나왔고 2회째 정상). 국제 블루블랙이 가장 좋음 |
| 영단어 확인 | 트리오 이름 제거판 | K 1회째 영단어, 2회째 없음 / 국제 1회째 없음 → 이름 제거로 해결 안 됨, 원문 마무리 유지 |
| 4~5인 확장 | 금박·식물 등 혼합 7개 | 7/7 성공(`#1~#4`·나이 영단어는 1회째만) |
| 확장 비교 | 기본 vs 확장(신발·헤어·손톱) 4쌍 | 확장판이 프레임을 더 채움, 신발이 패턴 색과 어울림, 헤어 확장 좋음, 손톱은 기본이 더 길게 나옴 → 손톱 모양을 stiletto/coffin/almond로 제한 |
| 6~10인 | 국제 6·K 7·국제 8·K 10 | 4/4 성공(K 10인은 두 번 9명으로 생성, 3회째 10명) |
| 20대 대비 | 듀오~8인 6개 | 6/6 성공 |
| 한 섹션 그룹 | UV 전원·바디페인팅 전원·이레즈미 전원·해태 혼합 등 6개 | 6/6 성공(`#1~#n` 글자는 퀸텟 1회째만) |
| 번들 샘플 | 8개(`la_ksilverfox_solo_01`, `la_silverfox_solo_04`, `la_ksilverfox_duo_06`, `la_silverfox_trio_01`, `la_ksilverfox_quartet_02`, `la_silverfox_quintet_02`, `la_ksilverfox_octet_01`, `la_silverfox_decet_01`) | 8/8(7개 1회, 1개 2회) |

> **정정**: 4~10인 확장 시험 안내에 "이레즈미 26종·UV 27종을 썼다"고 적었으나 실제로는 등록 프리셋의 **이레즈미 6종·UV 7종**만 쓰였다(7명 전원 이레즈미를 만들다 실패하면서 발견). 전체 풀(26/27)은 번들에서 처음 쓰였고, 번들 샘플 8개로 맥시멀리스트 틀에서도 통과를 확인했다.

### 28-5. 알려진 생성 습관 (재시도로 처리)

- `#1~#N`, 나이, 체형 영단어가 이미지 위쪽에 글자로 나오는 현상이 **1회째에만** 가끔 나오고 재생성하면 사라진다(4~6인 중심). 이름 제거 시도는 효과 없었다.
- 10인이 9명으로 생성되는 경우가 있다(재생성).
- 얼굴이 그림·CG 같다는 사용자 관찰이 있어 **얼굴 사실감 문장**을 짝 비교로 따로 시험하기로 했다(28-8).

### 28-6. K 피부 금박 (2026-10-07)

- 등록된 규칙은 "금박은 검은 피부 맥시멀리스트 틀에서만"(2026-10-05)이었으나, 실버폭스 맥시멀리스트 틀에서 한국 피부 금박 시험이 모두 성공했다: 금박 전원 솔로·듀오·트리오 3/3(1회), 쿼르텟 금박 전원·쿼르텟 혼합·퀸텟 혼합 2종 4/4(영단어는 1회째만, 퀸텟 혼합 1개는 2회째 성공, 금박이 의상처럼 생성된 사례가 있었음). 6~10인은 번들 샘플로 확인(28-7).
- 이에 따라 K 혼합 그룹에도 금박을 넣었다. 국제형 300개는 바뀌지 않았다. **이전 규칙(금박=검은 피부 맥시멀리스트 한정)은 실버폭스 틀에 한해 완화**되었고, 일반·임산부 틀은 그대로 접어 둔다.

### 28-7. 피부 톤 (K 전용, 2026-10-07)

- 처음 K 문구 `luminous warm golden-olive complexion`은 사용자가 보내준 성공 HOF 트리오에서 가져온 것이었으나 **너무 황금빛이고 오일을 바른 것 같다**는 평가(전 K 인물 1,155명 동일 문구).
- 비교 시험 8개(솔로 4·트리오 4, 같은 인물·패턴, 피부 문구만 다름): A(기존)는 황금톤·오일 느낌, **B·C·D 모두 채택**(B가 C보다 약간 밝음, 한중일 모두에 쓸 만한 톤이라는 사용자 평가).
  - B: `luminous fair porcelain complexion with a neutral-rose undertone and clear glass-skin glow`
  - C: `luminous light-neutral complexion with a soft peach-beige undertone`
  - D: `luminous milky ivory-fair complexion with a cool-neutral undertone and smooth dewy skin`
- K 번들의 모든 인물에 B/C/D 중 하나를 **인물별 무작위**(키 시드)로 배정(B 379·C 384·D 392). 20대 인물도 같은 세 톤에 `youthful fresh glow` 유지. 피부 톤 3종을 한 명씩 가진 트리오 2개도 사용자가 "3개 다 매력 있다, 한국인 피부색은 사람마다 다르다"고 평가.
- 최종 확인 샘플(K 금박 포함 4개 중 6인·10인): 모두 성공.
- 한중일 확장은 후보: 얼굴 특징은 프롬프트의 `Korean`이 정하므로 `Chinese`/`Japanese`로 바꿔 별도 세트를 만들 수 있으나 **얼굴이 실제로 달라지는지 미시험**.

### 28-8. 열린 과제 (실버폭스)

1. **얼굴 사실감**: 28-10에 결과와 적용 범위 기록(한국형 솔로·듀오 110개에만 적용 완료·등록 대기). 국제형(블루블랙)과 한국형 트리오 이상은 미적용.
2. **피어싱**: 실버폭스에는 미시험. 피어싱은 클로즈업 프레임 계열(얼굴·가슴·허리, 조각상 힙·데미·쓰리쿼터 솔로~트리오)에서만 쓰이므로 이 프레임에 실버폭스 인물 축을 입히는 별도 트랙.
3. **쥬얼리**: `Jewelry:` 줄은 실버폭스 틀에서 미시험(의상으로 읽힐 위험을 먼저 확인).
4. **석영(크리스탈)**: 단일 섹션 솔로·듀오로 먼저 시험(혼합에서는 꽃·수정·촛농 제외 원칙).
5. 후기 40대 상한(late 40s까지 / early 50s까지) 결정, 한중일 세트 여부, HOF/SSS/SS 티어(사용자가 마음에 든 키를 텍스트로 알려주면 패치).

### 28-9. 생성기와 재현

- 모든 스크립트는 `LumineX_generators_backup_2026-10-06.zip`에 있다: `sfv2/`(시험용 `gen_sf_v2~v7.py`, `sfv2_lib.py`, `roundtrip.py`, `pasted_trio.txt`, `pasted_duo.txt`)와 zip 최상위의 **최신** `gen_sf_bundle.py`(K 금박 허용판; `sfv2/gen_sf_bundle.py`는 금박이 국제 전용이던 옛 판), `apply_skin_k.py`.
- 번들 재생성 순서: `gen_sf_bundle.py` 실행(결과를 `la_silverfox_600_bundle.json`으로 출력) → 그 파일을 `bundle_v2_preskin.json`으로 복사 → `apply_skin_k.py`(K 인물의 피부 문구를 B/C/D로 교체해 같은 번들 이름으로 출력). 국제형 300개는 두 단계 모두에서 변하지 않는다.
- 등록: `patch_la_silverfox_1_json.py`(번들 → `presets/*.json`, 기존 파일 덮어쓰기 시 개수 출력) → `patch_livingartifact_2_meta.py` → `git add`(프리셋 두 접두어 + `core/presets_meta.py` + 번들·스크립트) → commit → push. 메타 출력: `categories added=2, keys added=600`.
- 생성 시 지켜야 할 점: 생성 후 한글 / 연속 중복 단어 스캔, K에서 "DARKEST BLACK" 없음, UV 1명 규칙, 20대 수와 메타 일치 검증.

### 28-10. 얼굴 사실감 문장 (2026-10-07)

- **문제**: 얼굴이 그림·CG처럼 보임(사용자 관찰). **해결 시도**: 각 인물 단락의 ` Pose: ` 앞에 `Face: a real photograph of a real woman's face, not an illustration and not a CG render — visible pores and fine skin grain, {나이 표현}, faint peach-fuzz hairs catching the light, natural tonal variation with a soft flush on the cheeks, a few small natural beauty marks, slight natural asymmetry, eyes with real wet catchlights and individual lashes, lips with real vertical texture — never airbrushed, never smooth like plastic.` 한 줄을 추가. 실버폭스는 `{나이 표현}` = `the fine natural expression lines of her age around the eyes and mouth`, 20대는 `youthful, smooth, fresh skin with no visible wrinkles`.
- **짝 비교 6개**(A 등록본 / B 문장 추가; K 솔로·K 트리오·국제 솔로): 사용자 평가 "많이 리얼해졌다, 살짝 넣었는데 진짜 같다". 단 국제(블루블랙)는 **너무 늙어 보임**.
- **국제 완화판 시험**(나이 표현을 `smooth, firm, youthfully elastic skin with only the faintest natural expression lines`로 약화, 볼 홍조 대신 광대 광택): 블루블랙 솔로는 여전히 너무 늙어 보이고 트리오는 기본과 비슷하게 돌아갔으며, 사용자 판단으로 **블루블랙의 색감이 사라지는 것 같아** 국제형에는 쓰지 않기로 함(이 시리즈의 국제형은 전부 블루블랙).
- **한국 듀오·트리오 시험**: 듀오는 많이 반영, 트리오는 별로 반영 안 됨(사용자: 제미나이 케바케, 인원이 많을수록 얼굴 하나당 비중이 줄고 얼굴도 작아짐). 프롬프트 길이도 인물당 약 80단어 늘어난다.
- **결정**: 한국형 **솔로·듀오(110개)에만 적용**, 트리오 이상(190개)과 국제형 300개는 그대로. 20대 인물은 주름 없는 문장. 적용 후 솔로 2개 + 듀오 2개 샘플과 미적용 솔로 2개를 비교해 사용자가 "한국형은 반영하자"고 결정.
- **재현**: `apply_face_k.py`(zip 최상위; `apply_bundle`이 K·group_size ≤ 2만 처리, 재적용하면 `Face:`가 중복되므로 **미적용 번들에 한 번만**). 순서: `gen_sf_bundle.py` → `apply_skin_k.py` → `apply_face_k.py`. 키·카테고리·제목·메타는 그대로이고 프롬프트만 바뀌므로 등록은 `patch_la_silverfox_1_json.py`만 다시 실행(메타 등록 불필요).

### 28-11. 실버폭스 Material Blend 180 (2026-10-08, commit `838a9071`)

- **카테고리 2개**: `🏺 Living Artifact · K-Silverfox Material Blend Formula`(`la_ksilverfox_blend_{solo|duo|trio}_NN`, 90) · `🏺 Living Artifact · Silverfox Material Blend Formula`(`la_silverfox_blend_{solo|duo|trio}_NN`, 90). 솔로·듀오·트리오 각 K 30 + 국제 30, 3혼합/4혼합 각 15, 종횡비 2:3·3:4·4:5 각 60. 합계 8,606 → **8,786**.
- **소스**: 등록 Material Blend 3·4혼합 180개(`la_matblend_geo_180_bundle.json` + 134개 덮어쓰기 `la_matblend_replace_134_bundle.json`)는 전부 맥시멀리스트 인물이라 1:1로 변환(원본 키는 `meta.source`). 제목은 `K-Silverfox Material Blend 3-Mix Solo #01 (한국 · 구조 | 재질들)` 형식.
- **변환**: 인물 머리부(피부·나이·체형 앞 문구)와 헤어만 치환 — 40대 초~50대 초, 은발 16종, 국제는 블루블랙·K는 피부 B/C/D, K 솔로·듀오 60개에 얼굴 사실감 `Face:` 문장(28-10과 같은 규칙). 경계는 **맞물림 문장(27-18)**. 20대 대비 인물·단일 섹션은 해당 없음(재질별 구역 구조).
- **시험 이력**: 흐릿한 경계 6개(전부 생성, 은색 띠 보고) → 원본 대조 4개(원본에서도 재현 = 실버폭스 원인 아님) → 선 문구 crisp 4개(거부) → 등록본 3개·A/B 4개(변형 C 채택) → 실버폭스 C 6개(5개 은색 띠 사라짐, 국제 듀오 1개 경계 희미·살 보임). 제외 규칙은 본 카테고리에 없음(꽃·수정·촛농은 소스에서 이미 제외).
- **검증**: 180개 모두 한글 없음·연속 중복 단어 없음·`her body carries` 수 = 인원·K에 "DARKEST BLACK" 없음·국제만 "DARKEST BLACK"·`Face:` 수(K ≤ 2인만)·"hazy and feathered/Even inside" 없음·"Where two regions meet" 수 = 인원. 프롬프트 길이: K 솔로 558~696, 듀오 1,114~1,328, 트리오 1,382~1,696단어; 국제 솔로 473~615, 듀오 937~1,155, 트리오 1,415~1,683.
- **재현**: zip에 `sf_blend_lib.py`, `gen_sf_blend.py`, `apply_interlock_sf.py` 추가. 순서: `gen_sf_blend.py`(번들 `la_silverfox_blend_180_bundle.json` 출력, 이 때 경계는 아직 흐릿한 문장) → `apply_interlock_sf.py`(맞물림 문장으로 교체, `meta.boundary="interlock-v1"` 추가). 등록: `patch_la_silverfox_blend_1_json.py` → `patch_livingartifact_2_meta.py` → git. 이번 메타 스크립트 출력은 "all 90 keys present ... Done. no changes needed"였고 `core/presets_meta.py` 3608행에 키가 이미 있어 정상으로 판단했다(등록이 두 스크립트 어느 쪽에서 이뤄졌는지는 확인하지 못했다).
- **다음**: 실버폭스 **Structure Pack**(25장 14a), 이후 피어싱·쥬얼리·석영, 한중일 세트, 티어. 번들 `la_silverfox_blend_180_bundle.json`의 이전(흐릿한 경계) 버전은 샌드박스에서만 백업했다(`blend180_hazy_backup.json`, 재생성 가능).

---

## 29. 실버폭스 3종 + 한중일 얼굴 컷 등록 (v6.35, 2026-10-09)

### 29-1. 등록 요약
| 번들 | 개수 | 키 | 카테고리(모두 `🏺 Living Artifact ·`) | commit |
|---|---|---|---|---|
| Silverfox Structure Pack | 120 (K 60 + 국제 60) | `la_ksilverfox_s2pack_{solo|duo|trio}_NN`, `la_silverfox_s2pack_…` | K-Silverfox / Silverfox Structure Pack Formula | `2ce96ba5` |
| Silverfox Piercing Frame | 120 (K 60 + 국제 60) | `la_ksilverfox_pframe_solo_NN`, `la_silverfox_pframe_solo_NN` | K-Silverfox / Silverfox Piercing Frame Formula | `8d4a1cac` |
| Silverfox Quartz | 120 (K 60 + 국제 60) | `la_ksilverfox_quartz_{solo|duo}_NN`, `la_silverfox_quartz_…` | K-Silverfox / Silverfox Quartz Formula | `a695f455` |
| 한중일 얼굴 컷 v3 | 120 (한국 40 + 중국 40 + 일본 40) | `la_cjkface_{kr|cn|jp}_solo_NN` | Korean / Chinese / Japanese Face Formula | `14792f5c` |

합계 8,786 → **9,266**(확인 완료). 등록 순서는 각각 `$env:PYTHONUTF8="1"` → `python preset_builders\patch_<이름>_1_json.py` → `python preset_builders\patch_livingartifact_2_meta.py` → `git add presets preset_builders core/presets_meta.py` → commit(attribution 줄 포함) → push. 메타 스크립트가 인식하는 카테고리는 \"🏺 Living Artifact\"로 시작해야 한다. `presets_meta.py`의 경로는 레포 루트가 아니라 **`core/presets_meta.py`**다(루트로 적으면 `git add` 실패).

### 29-2. 실버폭스 3종 번들 구성(번들 메타 기준)
- **Structure Pack 120**: 솔로·듀오·트리오 각 40, 종횡비 2:3·3:4·4:5 각 40, K 60 + 국제 60. 구조 8종 조합(굵은 스트라이프·셰브론·비대칭 몬드리안·폴카도트·큰 조각 4개 × 매끈/물결 경계). 경계는 맞물림 문장(`meta.boundary="interlock-v1"`, 27-18).
- **Piercing Frame 120**: 솔로, 프레임 얼굴 80·가슴 20·허리 20, 피어싱 P3~P150(P50 42·P100 32·P25 30 등), 쥬얼리 44개, 나이 early 40s~early 50s, K 60 + 국제 60(국제에 `nat: R1` 메타 60개).
- **Quartz 120**: 솔로 60 + 듀오 60, 종횡비 2:3·3:4 각 60, 재질 crystal, 색 amethyst·ruby·rose quartz·sapphire·topaz·emerald·smoky quartz·clear quartz·citrine·ice 등.

### 29-3. 한중일 얼굴 컷 구조
등록된 Piercing Frame 클로즈업(얼굴 컷)을 소스로 쓴 프롬프트다. 구조: 머리 문단(정면·양 귀 보임·머리 위~쇄골 프레임) → `Subject:` 문단(피부·연령군·아워글래스 체형·머리·\"Real pores… large eyes with bright real catchlights, full lips,\" 뒤에 메이크업+포인트, 표정, \"a photograph of a real {국적} woman's face ({FE})\") → `Piercings:` → `Piercing depth:` → (있으면) `Jewelry:` → `Lighting:`. P0은 피어싱 문단 전부 제거. **국적 앵커 R1은 등록본에 적용하지 않았다.** 국적별 얼굴 특징 문구(FE)와 연령군(아이돌·20대·30대)은 생성기에 있다.
- **메이크업**: 사다리형(코갸루 2~6단계, 마이코·경극·혼례·둔황·글래스 스킨 2~5단계, 블랙립 5스타일 강함·극한, 레드립 5스타일 강함·극한)과 오리지널 13스타일(포인트/강화 두 모드, 강화는 \"extremely heavy, fully saturated and bold, never subtle, faded or blended away:\" 접두). 코갸루·야마바·만바·반바는 태운 피부. P100/P150은 어두운 메이크업에만. 얼굴 페인트(경극·마이코·혼례·둔황)는 피어싱·렌즈만 허용. 메이크업에 lens/sticker/forehead 표현이 있으면 충돌 포인트 제외. 메이크업 없음 12개.
- **포인트(최대 4개로 확대, v6.35)**: 피어싱·렌즈·마이크로더멀·스티커·헤나(이마만). 피어싱과 혀 내밀기는 1개로 센다. 개수 분포 0·1·2·3·4 = 10·30·49·22·9(가중치 .06/.22/.36/.26/.10). 마이크로더멀은 \"Strong\" 문장(숨은 금속 베이스가 피부를 누름), 모양 하트·별·네잎클로버·초승달·나비·라운드, 색 7종. 렌즈 11색 × 동공 6종, 20% 오드아이, \"fully opaque… no natural brown showing through… darker limbal ring\".
- **표정 14종**: 기존 11종 + 놀란·호기심 어린·광기 어린(눈 크게 뜨는 계열, 시험 통과) + 혀 내밀기 4종(발랄·도발·관능·광기).
- **혀(18개)**: 갈라진 혀 기준. 2갈래 16개(링·스터드·검은 혀 변형), **3갈래·4갈래는 특별할 때만 각 1개**(`la_cjkface_jp_solo_07` 3갈래, `la_cjkface_kr_solo_04` 4갈래). 사용자 결정: 혀 갈래는 최대 4개, 2갈래 위주. 현실적 길이(\"tip reaching just below the lower lip\", 갈라짐은 뒤쪽 약 2/3). 극단 형태(혀 끝까지 갈라짐 등)는 ChatGPT가 거부하는 경우가 있다.
- **각도(36개)·점(37개), v6.35 신규**: 각도 = 고개 살짝 기울임 16·숙이고 올려보기 12·3/4 회전 왼쪽·오른쪽 각 4. 3/4 회전은 피어싱이 없는 프리셋에만(한쪽 귀가 가려짐), 도도한 표정에는 숙이고 올려보기 제외, 3/4 회전 시 조명 문구를 key light로 교체. 점 = 눈물점+입술 위 점 29·+광대점 7·주근깨 1. 얼굴 페인트 메이크업 제외, 마이크로더멀·스티커가 있으면 광대점·주근깨 제외. 각도·점은 포인트 개수에 세지 않는다. 혀 내밀기 프리셋은 정면 유지. 메타에 `angle`, `mole`.
- **한글 병기**: 제미나이에서 효과 없어 제거(2026-10-08). 프롬프트에 한글 없음.

### 29-4. 생성기별 차이(사용자 시험)
- **ChatGPT**: 색감이 좋고 피어싱·귀걸이·귀 장식이 화려하게 나온다. 3~6갈래 혀 모두 성공. 의상 없는 이미지는 생성하지 않는다. 얼굴 컷은 문제 없음.
- **Gemini**: 혀 3~6갈래는 한글 병기로도 실패. 한글로 따로 요청하면 성공한 적이 있다. 네온 가슴 3개는 생성했으나 바디페인팅·이레즈미는 생성하지 않았다.
- 렌즈: 진한 색이 잘 보이고 세로 동공(고양이눈)이 잘 나온다. 레드립은 뚜렷하게 나오나 아주 강하지는 않다(그대로 둠). 바 피어싱은 가끔 전체가 노출된다(케바케).

### 29-5. 시험 결과 요약(사용자 보고)
렌즈 색·모양 라운드 정상, 마이크로더멀 강한 버전 채택, 놀란·광기 어린 정상(호기심 어린도 가능), 혀 피어싱·갈라진 혀 정상, 4갈래는 ChatGPT에서 한 번에 성공, 극단 혀는 일부 ChatGPT 거부(제미나이에서 시험 예정), 각도 2·점 2 시험 4/4 정상. 각도·점을 섞은 랜덤 4개 조합(`LumineX_Face_Random4_AngleMole.md`)은 결과를 아직 보고받지 못한 채 등록했다.

### 29-6. 재현
생성기는 백업 zip(`LumineX_generators_backup_2026-10-06.zip`)에 있다: `cjk_face_lib.py`, `ladder_pool.py`, `gen_cjk_v2.py`(`make()`), `face_axes.py`(각도·점), `gen_cjk_bundle3.py`(번들 생성, 시드 20261008). 출력 `la_cjk_face_120_bundle.json` → `patch_la_cjk_face_1_json.py`. 혀·표정 시험 생성기(`gen_tongue*.py`, `gen_expr_wide3.py`, `gen_lens3.py`)와 각도·점 시험(`gen_angle_mole4.py`, `gen_face_random4.py`)도 포함.

### 29-7. 불채택: 가슴 3개
\"가슴 3개\" 시험(바디페인팅·이레즈미·UV네온 및 석영·얼음·플로럴·스테인드글라스·금박)은 **불채택**. 가운데(셋째) 가슴이 두 가슴 아래에 작게 그려지고, 위치를 가로 한 줄로 바꾸는 시도도 실패했다. 어떤 프리셋에도 반영하지 않았다.

### 29-8. 열린 과제
25장 14c·14d 참조. 그 밖에 흉부 컷 가슴 노출, 등록된 클로즈업의 \"Mid 20s.\" 태그, 임산부·가장 어두운 피부 마무리 문구, 40대 후반 상한, HOF/SSS 티어는 기존 보류 항목이다.

---

## 30. 목재·석재 단독 포뮬러 600 (v6.35, 2026-10-09)

### 30-1. 배경과 결정
- 등록 후 접두어별 개수 점검(2026-10-09, 합계 9,266 일치)에서 목재(`la_wood6_` 6 + `la_grid_woodonly` 9)·석재(`la_stone5_` 5 + `la_grid_stoneonly` 9) 단독이 왁스·흑요암(각 60)보다 얇다는 것이 드러나 보강했다. 사용자 결정: **4·5인 포함, 숫자를 많이 늘리기, 부피 큰 체형 위주, 얼굴 문장 없음, 다른 소재 다양화**.
- 사용자 보고: 이 틀(왁스·흑요암 틀: 블루블랙 피부, 목에서 발목까지 소재, 순수 검정 또는 밝은 배경)에서 목재·석재가 예쁘게 나온다.

### 30-2. 번들 구성(600, commit `468e6adc`)
- 카테고리 2개: `🏺 Living Artifact · Wood Formula`(`la_wood_{solo|duo|trio|quartet|quintet}_NN`, 300) · `🏺 Living Artifact · Stone Formula`(`la_stone_…`, 300). 각 소재 솔로·듀오·트리오·4인·5인 60개씩, 종횡비 2:3 / 3:4 / 4:5 / 4:5 / 5:4.
- 소재 40종(목재 20: 에보니·월넛·마호가니·파다욱·퍼플하트·제브라우드·로즈우드·부빙가·웬지·튤립우드·올리브·체리·코아·보코테·코코볼로·마카사르 에보니·레이스우드·버즈아이 메이플·아프리칸 블랙우드·티크 / 석재 20: 대리석·화강암·비취·라피스·말라카이트·로도나이트·오닉스·타이거아이·라브라도라이트·터키석·카넬리안·소달라이트·마노·트래버틴·문스톤·아주라이트·유나카이트·로도크로사이트·크리소프레이스·라리마). 한 그룹 안에서 인물마다 다른 소재.
- 체형: 부피 큰 5종만(BBW bombshell·amazon bombshell·latina curves·super hourglass·hourglass bombshell), 그룹 내 중복 없음. 파워리프터는 남성적으로 나와 제외.
- 신발·배경: 극단 힐 221개(30·32·36·40인치 표현), 나머지는 일반 플랫폼 부츠. 배경 검정 293·밝은 곳 307(갤러리·야외 테라스·아트리움·바닷가 산책로·하얀 안뜰·미니멀 로프트·도시 광장·대리석 홀, 크기 비교용 문·난간·계단 포함). 밝은 배경+극단 힐이면 "허리 높이 전신 와이드샷" 문장 추가, 검정 배경+극단 힐이면 낮은 앵글 문장 추가.
- 메타: `group_size, aspect_ratio, format:"woodstone", material, species, physiques, background, extreme_heel`. 제목에 소재·체형·배경·극단 힐 표시. 길이 274~1,748단어, 600개 고유, 한글·안전 단어 없음.
- 틀 출처: `gen_120_wax_obsidian.py`(백업 zip `glassface/`)의 소재 문장을 목재/석재용으로 바꾼 것. 안전 단어 목록(blood·wound·fracture·spike·bite·doll·spalt·rot·decay·fungus·worm·gash·crack 등)을 `check()`로 확인.
- 재현: 백업 zip의 `gen_woodstone_600.py`(시드 20261009), 패치 `patch_la_woodstone_1_json.py` → `patch_livingartifact_2_meta.py` → git.

### 30-3. 시험에서 알게 된 것
- **얼굴 문장 추가는 불채택**: 메이크업·표정·포인트를 얼굴에 넣은 샘플은 시험했으나, 사용자 판단으로 번들에는 넣지 않았다("얼굴엔 아무 것도 추가하지 말고"). 전신에서는 **피어싱이 어울리지 않는다**(최소 또는 없음). 파워리프터 체형은 남성적으로 보여 제외.
- **힐 높이의 한계**: 숫자를 30인치에서 84인치까지 키워도 그림에서는 약 30cm 높이에서 멈춘다(사용자 확인). 그래서 30~40인치 표현으로 정리했다. 높이를 더 보이게 하려면 숫자 대신 몸·주변 물건과의 비교 표현이 후보지만 시험하지 않았다. 밝은 배경에 크기 비교용 물건을 두는 방식은 번들에 반영했다.
- 바디페인팅·이레즈미·UV네온 솔로/듀오의 극단 힐 시험(`LumineX_ExtremeHeels_Tracks6.md`)과 최대 높이 밝은 배경 시험(`LumineX_ExtremeHeels_Bright3.md`)의 정상/이상 결과는 아직 받지 못했다.

---

## 31. 목재·석재 v2 · 힐/신발/주얼리 시험 결론 (v6.36, 2026-10-09)

### 31-1. 등록 요약
| 번들 | 개수 | 키 | 카테고리(모두 `🏺 Living Artifact ·`) | commit | 합계 |
|---|---|---|---|---|---|
| 목재·석재 포뮬러 v2 | 600 (목재 300 + 석재 300, 소재마다 솔로~5인 각 60) | `la_wood2_{solo|duo|trio|quartet|quintet}_NN`, `la_stone2_…` | Wood Formula v2 / Stone Formula v2 | `ef7672f5` | 9,866 → **10,466** |
| 목재+석재 혼합 v2 | 240 (듀오·트리오·4인·5인 각 60) | `la_wsmix_{duo|trio|quartet|quintet}_NN` | Wood-Stone Mix v2 | `b8b5a783` | 10,466 → **10,706** |

등록 순서는 29-1과 같다(`patch_la_woodstone2_1_json.py`, `patch_la_wsmix2_1_json.py` → 메타 스크립트 → `git add presets preset_builders core/presets_meta.py` → commit → push). 기존 `la_wood_`·`la_stone_` 600은 그대로 남아 있다(v1). 단일 소재 v2는 인물 전원이 같은 소재, 혼합은 한 프리셋에 목재와 석재가 항상 함께 있다(목재 인원 1~n-1명, 무작위 배치).

### 31-2. v2 구성(v1과의 차이)
- **v1(30장)**: 블루블랙 피부 고정, 배경 검정/밝음 반반, 극단 힐 35%(30~40인치), 얼굴·주얼리 없음. **v2**: 모든 축을 쓴 틀.
- **체형**: 부피 큰 5종, 가중치 BBW bombshell .34 · amazon bombshell .20 · latina curves .16 · super hourglass .14 · hourglass bombshell .16, 그룹 내 중복 없음. 나이: 기존 `AGES`. 자세: 기존 `POSES` + 7종 추가. 머리: 스타일 13 × 색 16 무작위.
- **인종/피부(10)**: blue-black · ebony · Korean · Chinese · Japanese · Latina · Indian · Middle Eastern · Slavic · Polynesian — 인물마다 피부 문구 + 얼굴 특징 문구(`cjk_face_lib.FE` 일부), 한 그룹 안에서 중복 없음.
- **얼굴 줄**: `Face:` "her face and ears are NOT carved — real living flesh with real pores…, 얼굴 특징, an unmistakably feminine face with a calm, composed expression, makeup: …". **메이크업만** 넣는다(`gen_cjk_v2.pick_makeup`: 안전 목록 11스타일 + 국가별 로컬 1종 40%; 태닝·얼굴 페인트·렌즈·스티커·위험 단어 제외, 어두운 피부에는 pale 계열 제외). 렌즈·마이크로더멀·스티커·헤나·표정 변화는 전신에서 불채택, 피어싱도 없음.
- **소재 표면 패턴 8종**(금 상감선·자개 꽃·은 세공·덩굴 부조·격자 부조·황동 상감선·파도 부조·작은 보석 박음), **네일**(가장 긴 네일, 모양 5 × 길이 4, 같은 소재로 조각), **신발 형태 5종**(허벅지 부츠·스트랩 샌들·펌프스·레이스업 부츠·발레 부츠, 같은 소재로 조각).
- **몸 주얼리**: 인물당 3개(긴 목걸이·허리 체인·금 팔찌·바디체인·팔 밴드·진주 초커+긴 진주·배꼽 체인·허벅지 체인·반지 중), 문장 끝에 "Jewelry is metal and pearl only, worn on the body, nothing added to her face or ears." 얼굴·귀에는 아무것도 달지 않는다.
- **힐**: 듀오 이상은 전부 **"razor-thin tapered heel a full forty inches tall and a twelve-inch hidden front platform"** + 발끝 포인트(BODYLIFT). 솔로는 40인치 표기 65 / 숫자 없음 55("taller than her entire shin from ankle to knee and a towering hidden front platform"). 숫자는 30cm 안팎에서 멈추므로 표기 자체는 "신호"일 뿐이다(30-3).
- **배경**: 전부 밝은 곳(8곳, 크기 비교용 문·난간·계단) + 허리 높이 전신 와이드샷 문장. 검정 배경 없음.
- **메타**: `group_size, aspect_ratio, format("woodstone2"|"woodstone_mix2"), material, species, physiques, ethnicity, background, heel_mode("forty"|"relative"), jewelry`(혼합은 `kinds`도). 제목에 소재·체형·인종·메이크업 라벨·배경·힐·몸 주얼리를 넣었다. 길이: 단일 567~2,633단어, 혼합 1,063~2,630단어(퀸텟은 2,600단어대로 길다).
- **재현**: `gen_woodstone2_600.py`(시드 20261016), `gen_wsmix2_240.py`(시드 20261017). 두 생성기는 `gen_woodstone_trio2.py`의 머리부를 exec 하고, 그것이 `gen_woodstone_full10.py` → `gen_woodstone_600.py`(소재 목록·SETS·CAM) → `gen_woodstone_groups6.py`로 이어진다. 모두 백업 zip(`LumineX_generators_backup_2026-10-06.zip`, 202개)에 있다.

- **(v6.37 갱신)** 위 v2의 신발 문장 속 "her legs stretched impossibly long and her whole body lifted far above the ground on them as if standing on stilts"는 32-4의 시험에서 체형을 깎는 것으로 보여 **문구 C로 교체하기로 했다**(패치 대기). 새로 만드는 프리셋은 처음부터 C를 쓴다.

### 31-3. 시험 결과(사용자 보고)
- **목재·석재 힐 숫자**: 솔로 1차는 차이 없음, 2차는 숫자 없는 쪽이 더 높아 보임 → **케바케**. 듀오(2회)·트리오·4~5인 모두 **40인치 표기가 더 높음**(확실). 같은 듀오에 10·20·30·40인치를 넣으면 **20인치가 가장 길게** 나왔다(한 번씩이라 결론 불가, 단조 증가 아님). → 듀오 이상은 40인치 표기, 솔로는 둘 다 허용.
- **몸 주얼리**: 솔로·듀오(5·6번) 목걸이·배걸이 잘 나옴 → 기본으로 채택.
- **바디페인팅·이레즈미·UV네온·왁스 트리오 A/B(40인치 vs 숫자 없음)**: 네 쌍 모두 큰 차이 없음. 단 **40인치 표기 쪽은 바디페인팅 1번을 빼고 신발이 모두 어두운 색**으로 나왔다. 바디페인팅은 인물마다 신발 색을 따로 적었기 때문에 유지된 것. → 이 트랙에서는 숫자를 쓰지 않아도 된다.
- **신발 색 일치(해결)**: 인물별 몸 패턴 색(대문자 색 구절, 예 "BLAZING ELECTRIC GOLD", "VIVID CRIMSON")을 신발 색으로 지정하고 "NOT black, NOT dark, NOT plain — bright, saturated, glossy colour taken straight from her own body art"를 넣으면 이레즈미·UV네온·왁스 트리오 3개 모두 **유사한 색**으로 나왔다(`LumineX_Trio_HeelColor3.md`). 왁스는 "heels entirely coated in the same hardened wax drips in {색}" 형태.
- **참고**: 소재 40종 + 몸 주얼리 + 인종 + 메이크업을 모두 넣은 v2의 생성 검증(정상/이상)은 아직 없다.

### 31-4. 시험 파일(모두 outputs)
`LumineX_WoodStone_BBW_MakeupOnly10.md`(솔로5·듀오5, 결과 미보고) · `HeelNumber_Jewelry6` · `HeelAB_Round2_4` · `Duo2_Heel40_Jewelry` · `Duo2_HeelNoNumber_Jewelry` · `Trio_HeelAB_Jewelry2` · `Duo_Heel10_20_30_40` · `Quartet_Quintet_HeelAB4` · `Trio_HeelAB_Tracks8` · `Trio_HeelColor3`(모두 `LumineX_` 접두).

### 31-5. 미결: 기존 등록분에 신발 색 일치를 반영할지
- 사용자 질문: "앞으로 꺼에만 반영할까, 교체할까?" 영향 범위(번들 기준): `platform boots 8 inch` 문장이 맥시멀리스트 `la_maximalist_bundle` 1,200개(이레즈미·UV네온 등), `la_fix_ire_uv` 300, 혼합·실버폭스 번들 700여 개에 있고, 왁스 `extreme platform heels entirely coated…` 문장이 60개다. 이들은 8인치 부츠라 "40인치 표기 때문에 어두워지는" 문제가 확인된 대상이 아니다.
- **권고**: 교체하지 않고 **새 것에만 적용**한다. 기존 프리셋의 신발 색은 시험한 적이 없고(교체 효과 미확인), 약 2천 개를 바꾸면 되돌리기 어렵다. 극단 힐이 필요하면 기존을 건드리지 않는 **추가 번들**(이레즈미·UV네온·왁스·바디페인팅 극단 힐 + 신발 색 일치)로 만든다. 사용자 결정 대기.

### 31-6. 열린 과제
25장 14f 참조.

---

## 32. 바 피어싱 노출 · 신발 문구 시험 (v6.37, 2026-10-09)

### 32-1. 바 피어싱 노출 시험
- **문제**: 얼굴 컷에서 피어싱이 많을 때 바가 피부 속에 묻히지 않고 **바 중간이 통째로 노출**되는 경우가 있다(케바케). 기존 "피어싱 깊이" 문단의 첫 문장은 "every bar and surface bar is embedded in the skin — its middle runs beneath the skin so only its two end studs show…"(구조 설명)이다.
- **시험 문구** (모두 "피어싱 깊이" 첫 문장 또는 눈썹·콧등 문장만 교체, 나머지는 등록본과 동일)
  - **A**: "every bar is drawn as exactly TWO small separate metal ends sitting on the skin, a short gap apart, with plain unbroken bare skin between the two ends and NO metal visible in that gap — the bar's middle is hidden under the skin…"
  - **B**: "every bar is drawn like a surface piercing in a close-up photograph: two tiny round metal studs set into the skin with a small warm shadow at each, joined by nothing visible — only a smooth, faintly raised ridge of skin runs between them… Show ONLY the two end studs and the skin bridge, never the whole bar lying on the skin."
  - **C**(눈썹·콧등 전용): 눈썹 바 = 곡선 바벨, 눈썹 바로 위 구슬 1개 + 바로 아래 구슬 1개, 사이는 눈썹털과 피부 / 콧등 바 = 코 양옆 구슬 1개씩, 사이는 피부. 눈썹 바 문장도 "curved barbells in a row along the outer half of each eyebrow, each showing one ball just above and one just below the brow"로 고침.
- **결과(사용자 보고)**

| 시험 | 내용 | 결과 |
|---|---|---|
| 1차 | P15 `la_cjkface_kr_solo_01`, P50 `la_cjkface_kr_solo_03` × A·B | 50개까지는 문제 없음 |
| 2차 P100 | `la_pframe_solo_061` A / B | 둘 다 바 중간 노출 |
| 2차 P150 | `la_pframe_solo_100` A / B | A 결과 미수신 / B 정상 |
| 2차 P200 | `la_pframe_solo_046` A / B | A 첫 시도 노출·2회째 정상 / B 첫 시도 성공 |
| 3차 | #061 C(개수 그대로) | 노출 |
| 3차 | #061 눈썹 9개씩·콧등 3개 + C | 정상 |
| 3차 | #061 같은 개수 + B | 노출 |
| 3차 | #046 C | 눈썹 7개 중 5개 바 노출 |
| 링 샘플 | #061·#046의 눈썹 바 → 링+스터드 번갈아 | 링이 완벽하진 않지만 바보다 잘 됨 |

- **결론**: 코 바는 잘 되고 **눈썹 바는 문구로 못 잡는다**(구슬 문구를 눈썹 전용으로 써도 실패가 많다). → **눈썹은 바 대신 작은 링과 둥근 구슬 스터드를 번갈아 배치**한다. 귀·코·입술의 바는 그대로. "피어싱 깊이" 문단도 그대로 둔다(A·B가 확실히 낫다는 근거 없음, 케바케). 새 프리셋은 처음부터 링+스터드를 쓴다.
- 시험 파일: `LumineX_BarPiercing_Exposure4.md`(1차) · `…_Exposure_P100_150_200.md`(2차) · `…_Exposure_BrowNose4.md`(3차) · `…_BrowRingStud2.md`(링 샘플).

### 32-2. 눈썹 바 → 링+스터드 교체 패치(repo 실행 대기)
- 스크립트: `preset_builders\patch_la_brow_ringstud_1.py`. `presets\la_*.json` 전체를 훑어 **"Piercings:" 문단(Piercing depth: 앞) 안의 눈썹 바 문장 5종만** 교체하고 개수를 유지한다(N개 → 링/스터드 합계 N개). 여러 번 실행해도 안전.

| 변형 | 바꾼 문장 | 바꾼 곳 |
|---|---|---|
| thick-each | "N thick M bars stacked through the outer half of each eyebrow" → "N M pieces in a row along the outer half of each eyebrow, alternating small rings that pass through the brow skin with the skin visible through each loop and small round ball studs sitting on the skin" | 676 |
| thin-half-left | "N thin M bars pass through the outer half of the left eyebrow" → 같은 형식(left) | 291 |
| thin-end-left | "N thin M bars pass through the outer end of the left eyebrow" → 같은 형식 | 146 |
| one-end-each | "a thin M bar passes through the outer end of each eyebrow" → "a small M ring passes through the outer end of each eyebrow, with the skin visible through the loop" | 28 |
| one-end-left | "a thin M bar passes through the outer end of the left eyebrow" → "a small M ring … left eyebrow, …" | 6 |

- **대상 907개**(번들 사본 시험): `la_pframe_` 292 · `la_pframe_maxmk_` 60 · `la_pstatue_` 300 · `la_pstatue_ext_` 60 · `la_ksilverfox_pframe_` 59 · `la_silverfox_pframe_` 60 · `la_cjkface_` kr 29·cn 25·jp 22. 시험: 번들에서 만든 사본 9,000개 파일에 적용 → 907개 교체, 재실행 시 0개, **눈썹 바 문장이 남은 파일 0개**, 바뀐 항목은 `prompt` 필드뿐.
- 주의: 이 패치는 번들이 아니라 **repo의 실제 파일을 직접 고친다**(등록 후 다른 패치로 바뀐 내용을 되돌리지 않기 위해). 되돌리기는 `git revert` 또는 `git checkout <커밋> -- presets`.

### 32-3. 4~5인 힐 숫자 시험(`LumineX_WoodStone_Quartet_Quintet_HeelAB4.md`)
- 쿼텟·퀸텟에서도 **40인치 표기가 숫자 없는 쪽보다 높게 나왔다**(사용자 보고). 따라서 목재·석재는 듀오~5인 모두 40인치 표기가 맞다(31-3의 솔로 케바케는 그대로). 바디페인팅·이레즈미·UV네온·왁스는 숫자 효과가 거의 없어 신발 색 지정(31-3)이 우선.

### 32-4. 신발 문구 A/B/C 시험 — 다리 길이 vs 체형 부피
- 의문: 힐 문구가 세질수록 다리만 길어지고 체형이 깎이는가. 원인 후보는 신발 문장 끝의 "her legs stretched impossibly long … as if standing on stilts".
- **문구**
  - A(등록본): "…like a dancer on pointe, her legs stretched impossibly long and her whole body lifted far above the ground on them as if standing on stilts"
  - B: "…like a dancer on pointe, her whole body lifted far above the ground on them, while her body keeps its full original proportions — thick heavy thighs, wide full hips and a huge bust exactly as massive as before, and only the heels add height"
  - C(채택): "…like a dancer on pointe, her whole body lifted far above the ground on them as if standing on stilts, while her body keeps its full original proportions — thick heavy thighs, wide full hips and a huge bust exactly as massive as before"
- **결과(사용자 보고)**: A→B는 체형이 조금 더 크게 나왔으나(솔로·듀오 모두 "살짝") 듀오 힐이 살짝 낮아짐. C(듀오 2개): 1번(A·B와 같은 듀오)은 왼쪽 힐이 살짝 높아지고 오른쪽만 슬림해짐, 2번은 체형이 꽤 잘 반영됨 → **C 채택**. 파일: `LumineX_WoodStone_LegLength_AB4.md` · `…_LegLength_C2.md`.
- **교체 패치**: `preset_builders\patch_la_woodstone_shoe_c_1.py` — A의 "her legs stretched impossibly long and her whole body… stilts"를 C로 교체. 기본 대상 `la_wood2_`·`la_stone2_`·`la_wsmix_` **840개**(2,640곳, 인물마다 1곳), 옵션 `--v1`이면 기존 `la_wood_`·`la_stone_` 중 극단 힐 문장이 있는 **221개**(693곳)도 교체(합계 1,061개). 번들 사본 시험 통과(재실행 0개).

### 32-5. 집에서 실행할 순서(등록 불가 상황이라 대기 중)
```powershell
$env:PYTHONUTF8="1"
python preset_builders\patch_la_brow_ringstud_1.py
python preset_builders\patch_la_woodstone_shoe_c_1.py        # v1(221개)도 바꾸려면 끝에 --v1
git add presets preset_builders
git commit -m "Replace eyebrow bars with ring+stud mix (907) and wood/stone shoe phrase C (840)" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01EfxHdG33JLZFYhLaETecV3"
git push
(Get-ChildItem presets\la_*.json).Count      # 10706 그대로
```
첫 줄 출력은 "완료: 907개 파일…", 둘째 줄은 "완료: 840개 파일, 2640곳…"(--v1이면 1,061개 파일)이어야 하고, 첫 스크립트의 마지막 줄은 "눈썹 바 문장이 남은 파일: 0개 (정상)"이어야 한다. 두 스크립트와 `preset_builders` 폴더 위치는 기존 패치와 같다.

### 32-6. 생성기 · 파일
- `gen_woodstone_test6/test4/duo2/duo2b/heel4/trio2/q45/leg4/legC2.py`, `gen_heel_ab_tracks8.py`, `gen_heel_color3.py` — 백업 zip에 있음. 바 피어싱 시험은 등록 번들에서 직접 문장을 치환해 만들었다(별도 생성기 없음; 문구 A·B·C는 32-1).
- 새 프리셋 규칙 요약: ① 눈썹은 링+스터드(바 금지) ② 목재·석재 신발은 문구 C ③ 몸에 그리는 트랙의 신발 색은 인물별 패턴 색 + "NOT black, NOT dark, NOT plain" ④ 힐 숫자는 목재·석재 듀오~5인에서 40인치 표기, 솔로는 케바케.

### 32-7. 열린 과제
25장 14g 참조.

---

## 33. 극단 힐 추가 번들 (v6.38, 2026-10-09)

### 33-1. 시험 (Heel_Big4, 4개 모두 정상)
이레즈미 4인·UV네온 5인(힐 40인치 + 신발 색을 인물별 몸 패턴 색으로 지정), 바디페인팅 4인(힐 40인치, 인물별 신발 색은 원문 그대로), 옵시디언 3인(힐 40인치, 검정 유리 신발 그대로). 결과: 정상 생성, 신발이 패턴과 잘 맞음. → 트리오에서 확인한 색 지정 방식이 4~5인에도 통한다.

### 33-2. 번들 구성 (292개)
- 바디페인팅(`bodypaint`, 원본 `la_core_*`)·이레즈미(`irezumi`)·UV네온(`uvneon`): 솔로~5인 × 각 12개. 단 이레즈미·UV네온 솔로는 원본 프롬프트가 30개 중 서로 다른 것이 8개뿐이라 각 8개.
- 왁스(`wax`)·옵시디언(`obsidian`): 솔로~트리오 × 각 20개(원본에 4인 이상이 없음, 20개 전부 변형).
- 원본은 등록 번들에서 서로 다른 프롬프트만 균등 간격으로 골랐다(`meta.source`에 원본 키). 왁스 듀오 01은 교체본 사용.
- 신발: 이레즈미·UV네온·왁스 = 인물별 몸 패턴 색 지정 + "NOT black, NOT dark, NOT plain"; 바디페인팅 = 원문 색 유지; 옵시디언 = 검정 유리 신발 유지. 힐은 듀오 이상 전부 40인치, 솔로는 40인치/숫자 없음 혼합(약 55:45). 낮은 카메라 문장 추가.
- 신발 몸 들어올리기 문장은 시험을 통과한 원래 문구(A)를 썼다. 목재·석재의 문구 C(체형 유지 문장)는 이 번들에 아직 적용하지 않았다(필요하면 후속).
- 메타: group_size, aspect_ratio, format `extremeheel`, track, heel_mode(forty/relative), shoe(matched/original/black), source. 제목에 트랙·체형(또는 바디페인팅 구성)·힐·신발 색 표기.

### 33-3. 생성기
`gen_xheel_300.py`(스크래치패드 → 백업 zip에 포함). 외부 의존: 등록 번들 `la_core_bundle.json`, `la_maximalist_bundle.json`, `la_120_bundle.json`, `la_wax_duo01_replace_bundle.json`.

### 33-4. 등록 순서 (집에서)
```
$env:PYTHONUTF8="1"
python preset_builders\patch_la_xheel_1_json.py
python preset_builders\patch_livingartifact_2_meta.py
git add presets preset_builders core/presets_meta.py
git commit -m "Add extreme heel body-art bundle (292 presets)" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01EfxHdG33JLZFYhLaETecV3"
git push
(Get-ChildItem presets\la_*.json).Count
```
`la_xheel_300_bundle.json`을 `preset_builders\`에 먼저 넣을 것. 개수 확인은 **10998**이어야 한다(교체 패치 2종은 개수를 바꾸지 않음).

---

## 34. 배경 라이브러리와 새 재질 시험 (v6.39, 2026-10-10)

### 34-1. 카메라·배경 현황 정리
- 목재·석재 v2·혼합 v2: 밝은 배경 8곳 + 허리 높이 전신 와이드샷 문장. 극단 힐 추가 번들: "아주 낮은 앵글" 문장. 기존 등록분(core·이레즈미·UV네온·왁스 등)은 앵글 문장 없음. 이레즈미·UV네온은 검정 배경이 기본(UV는 블랙라이트 때문에 구조적으로 필수).
- 몸에 붙는 재질(목재·석재·새 재질)은 "수십 개의 맞물린 조각 + 이음새 융기선" 문장이라 조각을 붙인 느낌이 난다. 몸이 재질로 변하는 통짜 표현은 프레임(`la_pframe_`·`la_pstatue_`)·듀얼바디(`la_duostatue`) 계열이 담당하므로 계열 차이로 둔다(사용자 확인).

### 34-2. 배경 라이브러리 v1 (`bg_library.py`, 70곳)
- 분류: 기존 8, 계절 8, 교통 4, 문화 6, 유적 11, 자연 11, 도시 6, 건축 4, 정원 4, 패션 2, 스포츠 3, 산업 3. 목록은 `LumineX_BG_Library_v1.md`.
- 규칙: 모든 장면에 정상 크기의 문·난간·계단(힐 높이 기준물), 공통 접미 "밝고 고른 조명 · 다른 사람 없음 · 읽히는 글씨 없음 · 같은 재질 소품 없음 · 검정 배경 없음". 날씨 4종(화창·흐림·황금빛 오후·비 갠 뒤)은 날씨 허용 실외 장면에만. 분류별 가중치(유적 약 10% 이하). 폭이 좁은 곳(`NARROW`: 만리장성·페트라·지하철·대나무·숲길·정글·폭포·얼음 동굴·협곡·해안 절벽·계단식 논·대교)은 4인 이상에서 제외(`pick(rng, n)`).
- 현재 사용 중인 예배 장소(성당·모스크·사찰)·추모 장소·인파가 본질인 곳·야간 네온 거리는 제외했다.
- 위험 장소 시험 8곳(지하철·공항·공연장·박물관·콜로세움·타지마할·런웨이·겨울 광장) **모두 정상 생성**(`LumineX_BG_Test8.md`).

### 34-3. 새 재질 시험
- 솔로 6종(옥·도자기·청동·옻칠·호박·산호/진주조개) 모두 정상. 산호는 처음에 살에 직접 붙던 문제가 있었으나 이번에는 진주조개 조각이 먼저 감싸고 그 위에 산호가 붙는 표현이라 채택.
- 재질 섞기: 듀오(옥+도자기)·트리오(청동+옻칠+호박)·4인·5인(목재·석재 포함) 4건 모두 정상. 전체 트랙 섞기(바디페인팅·이레즈미·UV네온 포함) 4건 중 1~3번 정상, 4번(5인, 이레즈미·바디페인팅·청동·호박·목재, 만리장성) 실패. 분리 시험: 같은 인물에 배경만 도시 광장으로 바꾼 것 정상, 몸에 그리는 트랙 없이 재질 5명+만리장성 정상 → 단독 원인 아님(케바케). 안전장치로 좁은 곳을 4인 이상에서 제외.
- UV네온 인물은 밝은 장면에서도 "자기 전용 블랙라이트 조명을 받고 다른 빛은 닿지 않는다" 문장으로 섞였다(3번 통과).

---

## 35. Material Mix Formula 300개 (v6.39, 2026-10-10)

### 35-1. 구성
- 솔로 60: 새 재질 6종 × 10(재질당 변종 3~4개: 옥 제왕녹·라벤더·백옥·적옥 / 도자기 청화·청자·분채·홍유 / 청동 녹청·금빛·검붉은 / 옻칠 주홍·흑칠·조각 주칠·금분 / 호박 꿀색·붉은·녹색·푸른 / 산호 분홍·붉은·백·복숭아). 힐은 40인치 31 · 숫자 없음 29.
- 듀오~5인 각 60 = 240: 인물마다 서로 다른 종류를 뽑는다. 종류 풀 11가지(바디페인팅·이레즈미·UV네온·목재·석재·새 재질 6종), 그룹마다 새 재질 최소 1. 힐 40인치, UV네온은 한 그룹에 최대 1명(같은 종류 중복 없음).
- 인물마다: 인종·체형(BIG5 가중)·나이·포즈·헤어·메이크업만 얼굴·몸 주얼리 3점·네일·신발. 바디페인팅·이레즈미·UV네온 인물은 얼굴이 칠해지지 않은 맨얼굴이고 신발은 몸 패턴 색(바디페인팅은 원문 신발 색). 배경은 라이브러리(68곳 사용), 공통 접미로 사람·글씨·같은 재질 소품 금지.
- 메타: group_size, aspect_ratio, format `materialmix`, kinds, physiques, ethnicity, background, weather, heel_mode, jewelry. 길이 598~2,618단어.

- 검증: 번들에서 뽑은 6개(솔로 2·듀오·트리오(UV 포함)·4인·5인) **모두 정상 생성**.

### 35-2. 생성기
`gen_matmix_bundle.py`(체인: gen_matmix_all4 → gen_matmix4 → gen_woodstone_full10 → …, 외부 `bg_library.py`와 등록 번들 `la_core`·`la_maximalist`·`la_120`). 시험용 `gen_newmat6.py`·`gen_matmix4.py`·`gen_matmix_all4.py`·`gen_matmix_4fix.py`도 백업 zip에 있다.

### 35-3. 규칙(새 프리셋)
눈썹은 링+스터드(바 금지), 목재·석재 신발은 문구 C(이 번들은 원래 문구 A 사용, 후속 가능), 힐 숫자는 듀오 이상 40인치, 배경은 라이브러리에서만.

### 35-4. 등록 순서 (집에서)
```
$env:PYTHONUTF8="1"
python preset_builders\patch_la_matmix_1_json.py
python preset_builders\patch_livingartifact_2_meta.py
git add presets preset_builders core/presets_meta.py
git commit -m "Add material mix bundle (300 presets)" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01EfxHdG33JLZFYhLaETecV3"
git push
(Get-ChildItem presets\la_*.json).Count
```
`la_matmix_300_bundle.json`을 `preset_builders\`에 먼저 넣을 것. 극단 힐 번들(33-4)까지 등록했다면 개수는 **11298**이어야 한다(극단 힐 번들 전이면 10,706 + 300 = 11,006).


---

## 36. 컨셉 · 포즈 · 헤어 확장 시험 (v6.40, 2026-10-10)

### 36-1. 시험 내용 (`gen_persona6.py` → `LumineX_PersonaPoseHair6.md`, 6개 모두 1차 정상)
- 컨셉: 재질별 신화 인물을 '여신' 자리에 이름+한 줄 소개로만 삽입(의상·날개·갑옷 묘사 없음), 인종도 컨셉에 맞춤. 옥=용녀/선녀(Chinese/Korean), 도자기=항아/낙신(Chinese), 청동=발키리(Slavic)/아마조네스(Latina), 옻칠=경국지색(Japanese), 호박=오슌(ebony)/클레오파트라(Middle Eastern), 산호·조개=예마야(blue-black), 석재=메두사(Slavic).
- 포즈: 새 서 있는 포즈 11종(런웨이 워킹, 뒷모습, S커브, 팔 올리기, 기둥 기대기, 바람에 머리 날리기, 옆모습, 기도 포즈 등).
- 헤어: 흑인(ebony·blue-black) 인물은 보호 스타일 8종(콘로우, 박스 브레이드, 브레이드 크라운, 아프로, 트위스트 아웃 등).
- 허벅지 안쪽 패턴 비어 보임: 케바케로 판단, 프롬프트 변경 없음.

### 36-2. 메두사 (`gen_medusa2.py` → `LumineX_Medusa2.md`, 2개 모두 정상)
컨셉 이름만으로는 뱀 머리가 안 나옴. 메두사(석재)일 때만 헤어를 "같은 석재로 조각한 굵은 뱀 수십 마리가 머리를 감싸 등 뒤로 늘어짐(뱀이 머리카락), 얼굴은 진짜 살"로 덮어씀. 목재·석재는 별도 인물 빌더(`orig_person`)를 거치므로 정규식으로 헤어 구절을 치환함.

### 36-3. 번들 반영 전 남은 결정
컨셉 짝짓기 on/off 비율, 새 포즈 11종과 기존 포즈 혼용, 보호 스타일 헤어 적용, 환경·분위기·날씨·조명 확장(수동 조합 검토 결과). 반영하려면 새 번들로 만들어 시험 6개 확인 후 등록.


---

## 37. 카메라 앵글 확정 + Persona Mix 300 (v6.41, 2026-10-10)

### 37-1. 앵글 시험 결과
- 하이앵글: 처음 문구("머리 위에서 내려다봄")는 광각으로 가까이서 찍혀 사람이 찌그러짐. 망원 렌즈·먼 거리·구체적 각도 문구로 고침. 45도(2층 발코니)는 3번째 생성에서 나옴(케바케, 제외), **70도(거의 위에서, 망원)는 한 번에 성공 → 확정**.
- 로우앵글(바닥에서 올려다봄), 측면, 3/4(좌우 대각선, 기본 샷과 차이가 작지만 남김) 모두 시험 6개에서 정상.
- 번들 앵글 비율: 솔로~트리오 기본 38·하이 20·로우 15·측면 15·3/4 12, 4~5인은 기본 55·하이 30·측면 15. 기본이 아닌 앵글에서는 등 돌리기·카메라 향해 걷기 포즈 제외.

### 37-2. Persona Mix 300 (`gen_personamix_bundle.py`)
- 솔로~5인 각 60 = 300. 카테고리 `🏺 Living Artifact · Persona Mix Formula`, 키 `la_pm_{solo|duo|trio|quartet|quintet}_NN`, format `personamix`.
- 컨셉(재질별 신화 인물, 인종 연동)은 해당 재질일 때 80% 확률, 인종이 겹치면 생략. 메두사는 석재 뱀 머리(40개). 흑인 인물은 보호 스타일 헤어. 새 포즈 11종. 힐·주얼리·배경 라이브러리는 Material Mix와 같음.
- 검증: 컨셉 치환·앵글 문구·포즈 필터 이상 없음(스크립트 검사). 같은 구성의 시험 6개(`LumineX_Mix6.md`)는 모두 정상 생성. 번들 전체의 실제 생성 시험은 아직 안 함.

### 37-3. 등록 순서 (집에서)
```
$env:PYTHONUTF8="1"
python preset_builders\patch_la_personamix_1_json.py
python preset_builders\patch_livingartifact_2_meta.py
git add presets preset_builders core/presets_meta.py
git commit -m "Add persona mix bundle (300 presets)" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01EfxHdG33JLZFYhLaETecV3"
git push
(Get-ChildItem presets\la_*.json).Count
```
`la_personamix_300_bundle.json`을 `preset_builders\`에 먼저 넣을 것. 극단 힐(33-4)과 Material Mix(35-4)까지 등록했다면 개수는 **11598**이어야 한다.


---

## 38. 등록 완료 (v6.42, 2026-10-10)

- 눈썹 링+스터드 교체: 로컬은 이미 일부(약 485개)가 바뀐 상태라 첫 실행에서 422개가 바뀌었고, 규칙 누락 3건(재질 이름 없는 `n thick bars`, 복수형 `n thin … bars … outer end of each eyebrow`)을 규칙에 추가해 3개를 더 교체. 최종 "남은 파일 0개". 검증 함수는 코 브릿지 바(`bridge of the nose`)를 눈썹 바로 세지 않도록 고침. 수정판 `patch_la_brow_ringstud_1.py`가 최신.
- 목재·석재 신발 문구 C: 840개 파일 2,640곳 교체(`--v1` 221개는 미적용).
- 번들 등록: `patch_la_xheel_1_json.py`(292), `patch_la_matmix_1_json.py`(300), `patch_la_personamix_1_json.py`(300) → 메타 등록 `categories added=3, keys added=892`.
- 확인: `(Get-ChildItem presets\la_*.json).Count` = **11598**. commit `87813bef`(교체 2건), `b09bb520`(번들 3개 + 메타).
- 새 카테고리 3개: `🏺 Living Artifact · Extreme Heels Body-Art`, `… Material Mix Formula`, `… Persona Mix Formula`.
- 열린 과제: Persona Mix 전체의 실제 생성 시험(시험 6개는 정상), 4~5인에서 앵글(로우·3/4) 미시험, `--v1` 221개 적용 여부, 배경 라이브러리를 기존 번들에 적용할지, 접두어 표.


---

## 39. Light Mix · 신발 결론 · Master Mix 300 (v6.43, 2026-10-11)

### 39-1. 등록 이력
- Light Mix Formula 등록: commit `7884c782`, 합계 **11,898**.
- Master Mix Formula 300 등록: commit `4dd6bbf3`, 카테고리 `🏺 Living Artifact · Master Mix Formula`, 키 `la_mx_{solo|duo|trio|quartet|quintet}_NN`(각 60), 메타 `categories added=1, keys added=300`, `(Get-ChildItem presets\la_*.json).Count` = **12,198**. 같은 커밋에 핸드오프 v6.34~42와 생성기 백업 zip도 함께 올라감.
- 번들 `preset_builders\la_mastermix_300_bundle.json`, 등록 스크립트 `patch_la_mastermix_1_json.py`.

### 39-2. 규칙: 번들은 정의된 축 전체를 기본 랜덤으로 (강한 결정)
- 새 번들을 만들 때 직전 번들 생성기(체인)를 이어받지 않는다. 체형·포즈·신발·헤어 스타일/컬러·네일·주얼리·앵글·배경·나이·재질·2인 구도 등 **원본 정의 파일의 목록 전체**를 랜덤 풀로 쓴다. 예외는 호환 문제(체형↔앵글·배경 등)나 그 번들에 명시한 제외뿐이며 이전 번들의 제외는 이어지지 않는다.
- 이전 Shoe Mix·Mat Mix 체인은 재질(바디페인팅·이레즈미·UV네온·스테인드글라스·금박·보태니컬·크리스탈·비늘·흑요암·왁스 등)과 2인 가로 구도(8종 Photo Duo)를 통째로 빠뜨렸고, 이를 사용자가 지적해 독립 마스터 생성기로 다시 만들었다.
- 확정된 결정: 전신 프롬프트에 피어싱 없음, 얼굴 렌즈 연출 없음, 주얼리는 몸 주얼리만, 의상 없는 컨셉. 임산부 체형은 섞는다.

### 39-3. 마스터 생성기 (`master/` 폴더, 백업 zip `LumineX_generators_backup_2026-10-11.zip`)
- `mdefs.py`: 원본 정의(glassface/full_dicts·body_full·gen_fix_ire_uv_6to10·gen_cjk_v2·gen_blend_540·gen_goldleaf_test·gen_matmix_bundle·gen_woodstone_trio2·bg_library)에서 AST로 풀을 읽음. `defs_woodstone.json`·`defs_persona.json`은 한 번 덤프한 값.
- `mrecipes.py`: 재질 18종 `mat_spec` + `person()`(몸/신발/네일/주얼리/얼굴), `gen_master.py [seed]`: 균형 랜덤(`BRandom`: 덜 쓰인 값 우선, 채택된 프롬프트만 집계, 60% 최소 사용값 · 40% 가중), 검증(한글 없음·연속 중복 단어 없음·"forty" 없음·Jewelry 수=인원·중복 없음).
- 결과(seed 20261201): 체형 36/36, 포즈 44/44, 나이 12/12, 인종 10/10, 재질 종류 18/18, 재질 변종 195/195, 배경 70/70, 조명 12/12, 시간대 7/7, 분위기 12/12, 앵글 5/5, 듀오 구도 9/9, 신발 종류 35/35. 신발 클래스 스틸레토 195·일반 90·발레 15. 단어 수 약 585~3,000(4~5인이 길다).
- 바디페인팅 변종 1개(najeon)가 "dense dense" 중복으로 계속 탈락하던 것을 고쳐 100% 달성.
- 이 번들에 **들어가지 않은 것**: 재질 혼합·구역 시스템(26~27장), 구조 팩, 조각상·특수 프레임, 표정·네일 마감·얼굴 추가, 소품.

### 39-4. 신발 결론 (사용자 시험 확정)
- 재질 트랙의 신발은 몸 문양과 같은 색 계열의 단색 진짜 신발(어둡지 않게). 페인트 트랙(바디페인팅·이레즈미·UV네온)은 "몸 위 색과 똑같은 색".
- 힐 문구는 B안: "very tall razor-thin tapered heel and a hidden front platform, a natural relaxed stance". 발끝으로 서는 pointe·스틸트·"forty inches"는 스틸레토·일반 신발에서 제거(발레 제외).
- 부츠 착용자: 몸 문양 범위를 "down to the top edge of her boots"로 적음(시험 모두 성공).
- 바닥 포즈(무릎·앉기·기대기·점프)는 FLIFT 문장, 2인 구도는 ARR_FLOOR 문장.
- 이미지가 인형처럼 보인다는 우려: 포즈는 원인이 아님(44종 고르게 분포), 힐을 부드러운 문구로 낮춘 것이 도움.

### 39-5. 열린 과제
- Master Mix 샘플 3개(솔로 스테인드글라스·트리오 금박/흑요암/글라스·듀오 기대기+걸터앉기) 사용자가 "잘 됐어"로 확인, 번들 전체 생성 시험은 미실시.
- 이미 등록된 Mat Mix·Persona Mix·Light Mix(와 xheel)를 5패턴 IR/UV와 제한된 공예 풀 기준으로 교체할지.
- 4~5인 프롬프트 길이(약 3,000단어): 체형 문구 단축(BODY_SHORT_FULL) 여부 사용자 결정 대기.
- 신규 카테고리 티어(HOF/SSS), `.bak` 5개 복구 여부, `--v1` 221개 적용 여부.


---

## 40. 킨츠기 · 리퀴드 메탈 (v6.44, 2026-10-11)

### 40-1. 등록
- Kintsugi Liquid Metal Formula 120(`la_kl_{solo|duo|trio|quartet|quintet}_NN`, 각 24): commit `71f912a9`(첫 시도는 번들 파일을 `preset_builders`에 저장하지 않아 0개 등록 → 저장 후 재실행), 합계 **12,318**. 번들 `la_kintsuliquid_120_bundle.json`, 스크립트 `patch_la_kintsuliquid_1_json.py`, 생성기 `master/gen_kintsu_bundle.py`.
- 솔로는 새 재질 4종(킨츠기 붙임·킨츠기 그림·리퀴드골드·리퀴드실버) 각 6개, 그룹은 새 재질 중심(60%)에 기존 18재질을 섞음. 체형 36·포즈 44·배경 70·2인 구도 9·신발 35 전부 사용.

### 40-2. 시험 결과 (사용자 판정)
- 킨츠기 붙임(코발트, 금 이음새를 손가락 폭으로 넓게 넣은 조각 구조)·리퀴드골드 붙임(굳은 금속)·킨츠기 그림(바디페인팅식)·리퀴드골드 그림 모두 한 번에 생성. 같은 인물로 그림 vs 붙임 비교: **리퀴드는 붙임이 좋음, 킨츠기는 둘 다 사용 가능** → 킨츠기는 붙임·그림 둘 다, 리퀴드는 붙임만 번들에 사용.
- 그룹(리퀴드실버 솔로·트리오·쿼르텟 재질 혼합): "패턴이 덜 생성되는 경우는 있지만 생성은 됨" → 통과.
- 이전 기록(18-7)의 "킨츠기/몰튼메탈은 표준 틀에서 실패"는 얇은 선·옅은 바탕 문제였고, 흑요암식 넓은 금 이음새 구조와 왁스식 굳은 금속 구조로 마스터 틀에서 해결됨. 그림 킨츠기의 유약은 검정 제외(신발 "검정 금지" 규칙과 충돌).

### 40-3. 등록분 오류 목록 (아직 미수정, 미미함)
Master Mix 300 중 약 20개: 배경 문법(`beach at with` 8, `a open-air` 3, `a autumn` 3)과 신발 문구(`metallic platinum metallic leather` 6). 생성기(master/gen_master.py, mrecipes.py)는 이미 고쳐져 새 번들에는 없음. 필요하면 정규식 패치로 수정.


---

## 41. 극단 체형 A/B 표현 · 새 생성 규칙 (v6.45, 2026-10-11)

### 41-1. 첨부 프롬프트 20개 검토
- 사용자가 가져온 "실버폭스 SuperBBW 킨츠기" 20개(무한 거울방·지오드 동굴·유리 바닥 전망대·소금평원 등). 형식은 Subject/Physique/Body Art/Pose/Footwear/Nails/Background, 20개 모두 체형 문장·바디아트 문장·마감 문장("Extreme high-gloss ceramic finish. 2:3 vertical 8K portrait")이 동일하고 전부 맨발, 주얼리·메이크업·인종 변주 없음.
- 평가: 장소 아이디어만 쓸 만함(로마 지하 물탱크·터렐 스카이스페이스·유리공방 용광로는 우리 풀에 없어 보임). 프리셋 틀로는 부적합(축이 랜덤이 아님, 체형 문장이 형용사 위주, 안료 왜곡 문장 없음, 줌인·카메라 지시 없음, 사람이 작아지는 장소가 많음, 몸을 가리는 장소(해바라기·양귀비·증기·양치류·수중) 포함). 배경 풀 후보로만 검토할 수 있음(가림 장소는 체형 제한 필요).

### 41-2. 체형 문장 A/B/C 시험 (사용자 판정)
- **A**(첨부식): `heavily oversized SuperBBW physique THE MOST EXTREME PHYSICALLY POSSIBLE beyond all anatomy limits — overwhelmingly massive bust, maximum hip expansion, heavy thighs, profound physical volume dominating the frame`. 정돈된 캐릭터 느낌, 체형은 B보다 작음, 복부 주름은 페인트 재질에서만 잘 나옴(스테인드글라스에서는 주름이 묻힘).
- **B**(우리 표현): USSBBW/hourglass SSBBW 기존 정의 + `every fold and curve keeps its own clear rounded outline … never merging into one shapeless mass, the sheer weight of the flesh visible in how it spills forward and settles[, her body so wide that her hips nearly touch the left and right edges of the frame — 솔로만]; real photographic skin with visible pores …, faint stretch marks …` + (페인트 재질이면) `; the pigment sits on living skin so it distorts slightly over every bulge and cracks a little where the skin folds`. 체형이 더 크고 입체적, 처짐이 강한 정의라 2B에서 한때 "너무 쳐짐"이라는 평가.
- **C**(A 뼈대 + B의 윤곽·무게·피부, 처짐 제거): 2C는 A와 B의 중간, 3C는 두 번째 시도에서 생성, 11C(스카이스페이스) 생성 안 됨(장면 원인 추정). **C는 중간이라 불필요 → 폐기**, 극단은 A와 B 두 가지만 쓰기로 결정.
- 3B: 하이앵글이라 체형이 작게 나옴 → **큰 체형은 하이앵글 부적합**. 듀오(2번)·트리오(3번) 샘플에서 체형이 작게 나온 것은 구도(한 프레임 인원) 때문.
- 페인트 A/B 앉은 자세 솔로 2쌍(바디페인팅 USSBBW 1A/1B, 이레즈미 hourglass SSBBW 2A/2B): **두 쌍 모두 B가 체형이 더 큼**. 이레즈미는 한 번에 안 되지만 결국 생성, 허벅지 패턴 일부 약함은 재질 한계(케바케).

### 41-3. 확정 규칙 (사용자 확정: "B 60 : A 40 좋아, 앉은 자세 70%, 하이앵글 제외, 듀오 이상 극단 포즈 제외, 재질 연동")
1. **극단 체형** = USSBBW, hourglass SSBBW(임산부 변형 제외). 페인트 재질(바디페인팅·이레즈미·UV네온·킨츠기 그림)이면 B 60 : A 40으로 교대(`AB = [B,B,B,A,A]` 균형 랜덤), 그 밖의 재질(유리·돌·도자기 등)은 **B 고정**.
2. 극단 체형 **솔로**는 앉은 자세 70%(발레 신발 제외). 앉은 포즈 11종(`SEAT`: 등받이 없는 돌 벤치, 등받이 높은 나무 벤치, 낮은 돌담, 돌 턱, 석재 의자, 나무 안락의자, 갤러리 벤치, 등받이 높은 나무 의자, 계단, 나무 스툴, 푹신한 벤치). 헤더는 "ONE woman seated". 나머지 30%는 기존 포즈 풀.
3. 극단 체형이 하나라도 있으면 **하이앵글 제외**(앵글 후보에서 high만 빠짐).
4. **듀오 이상**은 극단 포즈 7개 제외: 점프(17), 한쪽 무릎 꿇고 다른 다리 들기(1), 런지(12), 극단 엉덩이 아치 좌·우(19·23), 전신 뻗기(38), 바람에 날리는 역동 포즈(40). 솔로는 전체 44개 사용. 2인 구도(ARR) 자체 포즈는 점검 결과 극단 동작 없음.
5. v2에서 새 재질 4종(킨츠기·킨츠기 그림·리퀴드골드·리퀴드실버)을 `ALL_KINDS`에 포함(재질 종류 22).
- 피어싱 없음·얼굴 렌즈 연출 없음·몸 주얼리만(39-2)은 그대로.

### 41-4. 구현과 검증
- `master/gen_master_v2.py`(기존 `gen_master.py`는 보존, 등록된 Master Mix 재현용). 출력은 시험용 `mastermix_v2_test.json`(등록 안 함). 메타에 `physique_variant`, `seated_solo` 추가.
- 시험 생성(seed 20261211, 300개): 규칙 위반 0 — 극단 체형 포함 50개에서 하이앵글 0, 듀오 이상 극단 포즈 0, 한글·중복 단어·관사 오류 0, Jewelry 수=인원, 프롬프트 300개 모두 고유. 축 커버: 체형 36/36, 재질 22/22, 배경 70/70, 앵글 5/5, 구도 9/9, 신발 35/35, 포즈 43/44(미사용 1개는 38번 전신 뻗기: 듀오 이상 제외라 솔로에서만 가능).
- **주의**: 기본 랜덤 300개에서는 극단 체형 솔로가 겨우 2개라 A/B·앉은 자세 규칙이 거의 작동하지 않음(극단 체형 51명 중 A 4, B 47). 이 규칙이 의미 있으려면 "극단 체형 전용 번들"이 필요함(미작성).
- 시험 스크립트(백업 zip의 `master/`): `gen_abtest.py`(샘플 3개), `gen_abpaint.py`(페인트 A/B 앉은 자세 2쌍), `gen_usseat.py`·`gen_usspace.py`·`gen_ussolo2~6.py`(USSBBW 솔로 시험).

### 41-5. 열린 과제
- 극단 체형 전용 번들(USSBBW/hourglass SSBBW 솔로 중심, 앉은 자세 70%, 페인트 A/B 교대) 작성 여부 사용자 결정 대기.
- 새 마스터 번들 작성 시 `gen_master_v2.py` 사용(키 접두어·카테고리 이름 새로 정할 것).
- 킨츠기 "fine crack lines" 대신 굵은 이음새 문구가 더 안정적(40-2)이지만 첨부 프롬프트 비교에서는 미변경.
- 첨부 프롬프트의 새 장소 3곳(물탱크·스카이스페이스·유리공방)을 배경 풀(bg_library)에 추가할지.
- 등록된 Master Mix의 문법·신발 오류 약 20개 패치(40-3), 3인 이상에서 극단 체형 비중 축소 여부(구도상 체형이 작아짐), 티어(HOF/SSS), `.bak` 5개, `--v1` 221개.

### 41-6. 임산부 적용은 보류 (사용자 판정: "임산부는 일단 패스")
- 임산부 극단 체형(pregnant USSBBW·pregnant hourglass SSBBW)에 A/B를 적용해 샘플 2쌍(`LumineX_Pregnant_AB_Seated.md`)을 시험했으나 "체형이 잘 반영되지 않는다"는 평가 → **보류, 생성기에서는 되돌림**(`EXTREME`은 USSBBW·hourglass SSBBW 두 개만). 임산부 체형은 기존 정의 그대로 쓰며, 일반 규칙(하이앵글·극단 포즈)도 임산부에는 적용하지 않음.
- 추정 원인: 임산부 정의가 "팽팽하게 구분된 둥근 배"를 강조해 모델이 보통 크기의 만삭 여성으로 그려 거대한 체격 문장이 묻힘. 재시도 방향 후보: ① 거대한 체격 문장을 앞에 두고 임신은 맨 뒤 한 구절로, ② 배와 아래 접힌 살의 경계를 B 문장으로 보강, ③ 임산부는 A/B 구분 없이 기존 정의 유지.
- 코드: `a_variant()`(임산부용 A형 문장)는 `gen_master_v2.py`·`gen_abpreg.py`에 남겨 둠. 재개 시 `EXTREME`에 임산부 두 종을 다시 넣으면 됨.

## 42. 재질 쪽 몸 구성 · 혼합 구조 트리오 시험 (v6.46, 2026-10-11)

### 42-1. 재질 쪽 몸 구성 5종 (정리)
1. **재질 프레임 컷**: 조각 자체가 그 지점에서 끝남(카메라 크롭 아님). 사다리 허리컷·힙컷·데미스탯·쓰리쿼터·앵클컷·전신 중 번들에 등록된 것은 **힙컷·데미스탯·쓰리쿼터**. 앵클컷은 앉기 포즈로만 시험(번들 제외).
2. **듀얼바디**: 좌우 다리가 서로 다른 단계(L0~L4)로 유리→실사 전환. 이번 트리오에서는 **양쪽 다리 단계를 통일**(L1/L1·L2/L2·L3/L3)하고 "Both legs" 한 번으로 설명을 합침(`both_legs()`).
3. **상체 페인트 / 하체 재질**(아래 42-4): 위 = 페인트 재질(바디페인팅·이레즈미·UV네온), 아래 = 조각 재질. 의상 없음.
4. **재질 혼합**: 5재질 혼합, 몸통 3조각 분할(프레임 컷 위에 얹는 방식).
5. **크롭 프레임**: 얼굴·가슴·허리·힙을 카메라가 자르는 방식(별개 체계).

### 42-2. 임산부 허리컷·힙컷 + 얼굴 재료 샘플, 컷별 피어싱 한도 (답변 기록)
- 샘플 4개 `LumineX_Pregnant_Cut_Samples.md`(`preg/gen_preg_cut.py`, 등록된 임산부 허리컷 50개 기준으로 허리컷·힙컷에 얼굴 재료(피어싱·렌즈·마이크로 젬·스티커·헤나) 랜덤 배정). **사용자 정상/이상 판정은 아직 없음.**
- 한도(시험 기록): 크롭 얼굴 P3~P200, 가슴 P8~P200, 허리 P8~P100(P150은 1회 실패), 임산부 허리 P25·P50·P100 통과, 크롭 힙은 미확인. 재질 프레임 힙컷·데미스탯·쓰리쿼터는 P200까지 통과. P50 이상 프롬프트는 1,000단어 이하 권장.

### 42-3. 프레임 컷 + 실사/듀얼바디 혼합 트리오: 결과와 규칙
- 이번에 처음 만든 혼합이며, 이전에 검증된 그룹은 **전원 프레임 컷 듀오·트리오**(6/6)뿐이었다.
- **받침**: 프레임 컷 조각은 받침 블록 위에 올리고 윗면을 옆에 서 있는 인물의 같은 컷 지점에 맞춘다(힙=엉덩이, 데미스탯=허벅지 중간, 쓰리쿼터=무릎). 데미스탯+허벅지 중간 높이는 머리 높이가 맞았고, 허리 높이 받침은 조각이 살짝 높게 나옴. "low plinth"라고 쓰면 전신으로 나옴 → "tall plain pale stone plinth block".
- **컷 문단은 등록된 문구 그대로** 쓴다(내가 새로 쓴 "평평한 단면"·"끝이 뾰족"은 틀렸고 무릎 아래까지 생성됨). 등록 문구: "two individually rounded, deliberately carved tips…", "because the sculpture itself ends there, not because a camera frame happens to cut her off", "no calves, no feet, nothing continues below either tip", "The rounded tip is the material's own carved finish… never the edge of a photograph", 유리는 "curves inward and seals shut into its own smooth, rounded, closed tip". 표면 문구만 받침 윗면으로 바꿈.
- **모순 문구 제거 필수**: 조각 인물의 체형 문장에서 "sagging down toward her knees", "thick heavy calves", "legs and feet stay in correct proportion"을 삭제(`b_cut()`). 마무리의 "Full-length wide shot… 모두 머리 높이 동일"도 컷 인물이 있으면 쓰지 않는다.
- **혼합은 어렵다**: 실사·듀얼바디와 섞으면 컷 위치가 흔들림. 결정: ① 프레임 컷은 가능하면 전원 프레임 컷 그룹에서 쓴다 ② 섞을 때는 **인물당 재질 하나**(5재질 혼합·3조각은 솔로나 같은 구조 그룹에서만) ③ 프레임 컷과 컷형 상체 페인트 구조를 한 프롬프트에 같이 쓰지 않는다 ④ 프레임 컷+실사를 꼭 섞으려면 책상 위 상반신 조각 등 별도 시험(미시험).
- 길이: 혼합 트리오 2,300~3,650단어(등록 트리오 1,000~2,200). 3,200대는 대체로 잘 나왔고 2,700대에서 컷 이상이 나온 사례가 있어 길이만이 원인은 아님. 줄이는 후보(인물별 체형 문장 합치기, 듀얼바디 전환부 압축)는 미적용.

### 42-4. 상체 실사 / 하체 재질 (의상 없음 버전)
- 21-3-3의 밴도탑·크롭탱크·비키니 버전은 "**전 시리즈 의상 없음**" 규칙(28장·39장)에 어긋나 사용하지 않는다. 대신 **상체를 페인트 재질(바디페인팅·이레즈미·UV네온)로 칠하고, 경계선 아래는 조각 재질**로 한다(`gen_trio_mix2.py`의 `adapt()`가 페인트 문구를 상체 한정으로 바꿈: 몸 전체·다리·발목 단어 제거).
- **컷형(허벅지 끝에서 끝나고 받침 위)은 실패 위험**: 하체 투명 유리+왼쪽 배치가 전체컷(난쟁이)으로 나왔고 키 보강 문장을 넣어도 무릎 아래에서 평평한 단면으로 컷이 됨. 불투명 목재 하체 오른쪽 배치는 성공(표본 작음). 추정: 투명 재질 안에 다리를 그려 넣음.
- **결정(사용자): 발끝까지 재질로 하는 전신형으로 간다.** 경계선에서 발가락 끝까지 같은 불투명 조각 재질(발목·발·발가락 포함), 하이힐은 신음. 하체는 우선 불투명(목재·석재 13종)만 쓰고 투명은 재시험 대기.
- **경계 위치 3종 결과**(같은 인물·재질·배경, 경계 문장만 변경, 사용자 판정 "이 정도면 잘 나옴"): 허리 컷 = 배꼽 살짝 위, 힙컷 = 배꼽 약 4cm 아래, 허벅지 컷 = 엉덩이 바로 아래 허벅지 상단(문구 "엉덩이 주름과 무릎 중간"보다 높게 나옴). **이 세 위치(`waist`·`hip`·`thigh`)를 경계 위치 랜덤 축으로 확정**(`chest`=가슴 아래도 생성기에 있으나 이번 비교에는 포함 안 함). 문구: 허리 `at the narrowest part of her waist, just above her navel`, 힙 `at her hip line, just below her navel`, 허벅지 `halfway down her thighs, midway between the hip crease and the knee`(결과는 상단).
- 진짜 허벅지 중간·무릎 위 경계는 "무릎 바로 위 손 한 뼘 위"처럼 무릎 기준 문구로 바꿔야 할 것으로 예상(미시험).

### 42-5. 샘플 파일과 판정 현황
- `LumineX_Trio_Real_FrameCut_DualBody_Vertical.md`(실사+유리 프레임 컷+듀얼바디), `LumineX_Trio_Plinth_Height_Compare_v3.md`(받침 높이 3종: 모두 정상 생성, 1안이 높이 일치), `LumineX_Trio_StructureMix_3.md`(1번 정상, 2번 상체 이레즈미/하체 투명이 전체컷, 3번 대체로 정상), `LumineX_Trio_UR_Fix.md`(컷 아래 무릎에서 평평하게 컷, 실패), `LumineX_Trio_UR_Center.md`(결과 미보고), `LumineX_Trio_Simplified_3.md`(프레임 컷이 어렵다는 평가, 번호별 판정 미보고), `LumineX_Trio_UR_FullBody_3.md`(발목 위까지 재질 버전, 판정 미보고), `LumineX_Trio_UR_FullBody_Boundary3.md`(경계 위치 3종, 위 42-4).
- 생성기: `master/gen_trio_mix.py`(첫 트리오), `master/gen_trio_mix2.py`(실사·프레임 컷 단일/5재질/3조각·듀얼바디·상체 페인트/하체 재질 컷형·전신형 조합, `URFPOS`·`URMODE`·`URKINDS` 전역으로 시험 조건 지정), `preg/gen_preg_cut.py`. 모두 시험용이며 등록하지 않았다.

### 42-6. 열린 과제
- 전신형 상체 페인트/하체 재질을 번들 카테고리로 만들지(경계 위치 3종 × 페인트 3종 × 불투명 재질 13종), 인물 수·구성(솔로·듀오·트리오)과 체형 규칙은 사용자 결정 대기.
- 하체 투명 재질 전신형 재시험, 허벅지 중간·무릎 위 경계 시험, 프레임 컷 + 실사 혼합(책상 위 상반신 조각) 시험, 트리오 길이 줄이기 A/B.
- 41-5의 열린 과제는 그대로(극단 체형 전용 번들, 새 배경 3곳, Master Mix 오류 약 20개 패치, HOF/SSS 티어, `.bak` 5개, `--v1` 221개).

## 43. 듀얼바디 투명 계열 · 수조 수위 · 그룹 수조 시험 (v6.47, 2026-10-11)

### 43-1. 앞 장(42) 이후 추가 규칙
- **상체 페인트/하체 재질(전신형)의 하체 재질 개수**: 1종(기본) 외 2·3·4종 구성 시험. 2종 = 몸 중앙 세로 이음선으로 그림 기준 좌/우, 3종 = 하체 몸통 + 왼쪽 다리 + 오른쪽 다리, 4종 = 하체 몸통 좌/우 + 각 다리. 재질은 등록된 불투명 7종 풀(`EXT`)에서 서로 다르게, 근흑색 재질은 1개 이하. 생성기 전역 `URFN`(1~4). 결과(`LumineX_Trio_UR_MultiMaterial_2_3_4(_Shoes).md`)는 판정 미보고.
- **신발 랜덤화**: 프롬프트 단위로 스틸레토 42 : 플랫 18, 3인 구성에서는 발레 플랫 제외, 부츠는 듀얼바디·상체 페인트/하체 재질에서 제외(`pick_shoe`·`db_shoe`). 페인트 트랙 신발 색은 바디아트 색을 따름. 메이크업은 `R.face()` 랜덤(얼굴 페인트·렌즈·스티커 제외).
- **테스트 프롬프트도 기본 랜덤**(체형·포즈·신발·네일·주얼리·헤어·메이크업·앵글·배경·나이 전부). 유형 하나를 고정하는 시험에서도 나머지 축은 랜덤으로 둔다(사용자 재확인).

### 43-2. 듀얼바디 재질 규칙
- 듀얼바디 재질은 **단일 투명 / 투명 수조 / 내용물 투명** 3종(등록된 단일 재질 문구에서 추출, `DB_SOLID`·`DB_CONTENT`). 상체 페인트/하체 재질(불투명 하체)이 **같은 프롬프트에 있으면 투명 3종만** 쓴다(위아래만 뒤집힌 같은 구조로 보여 구분이 흐려짐). 없는 구성(솔로·듀오·듀얼바디끼리·실사와만)에서는 **석재까지 허용**(석재 L3 1인·듀오 정상). 
- **목재 듀얼바디는 제외**: L1(허벅지 맨 위) 실패, L3(발목 위까지) 재시험도 실패 → 단계 문제가 아니라 재질 문제. 프레임 컷의 목재(파덕 힙컷) 실패와 같은 방향. `DBTYPE="wood"`로 지정할 때만 생성되고 랜덤 풀에서는 빠져 있다.
- 투명 3종 + 상체 페인트/하체 재질 + 실사 트리오(`LumineX_Trio_DualBody_TransparentTypes_3.md`): 3개 모두 정상. 단일 투명·내용물 투명은 전환부 단면 문구를 "투명 재질이 단면에 보임"으로 바꿈, 석재는 "불투명 단면이 매끈하고 속이 비지 않음".
- 생성기를 1·2인도 지원하도록 일반화(3인 고정 문구 → 인원별 문구), 4인 문구 추가(`pos_ko`·`NUMW`·`allp`·`cam`).

### 43-3. 투명 수조(얇은 벽)와 수위
- **수조는 얇은 벽의 투명 용기**. 문구: "머리카락처럼 얇고 투명한 껍질, 거의 보이지 않고 반사·가장자리 굴절선으로만 드러남, 뒷배경과 조명이 거의 왜곡 없이 비침." 유리에는 **옅은 색조**를 줄 수 있다(표면 중앙은 투명, 가장자리·곡면 모서리에서만 약간 진해짐). 이전의 "thick glass" 표현은 폐기.
- **수위 단계**: 비움 / 반 / 4분의 3 / 가득을 시험한 뒤, **75%는 수면이 가슴 높이라 표현이 어렵고(수면 위 빈 공간에 몸이 그려짐)** 제외하고 **100 / 50 / 25 / 0%**로 확정. 2인 100/0, 3인 100/50/0, 4인 100/50/25/0.
  - 프레임 힙컷: 50% = 허리(배꼽 바로 위), 25% = 엉덩이 높이. 듀얼바디 L3: 50% = 허벅지 높은 곳(엉덩이 주름 바로 아래), 25% = 무릎 높이.
- **수면 위 빈 부분**에는 "이 용기가 곧 그녀의 몸이다. 안에 사람 몸·피부·살·뼈·장기가 없다. 수면 위는 맑은 공기뿐이고 뒷배경이 그대로 보인다" 문장을 넣는다(없으면 빈 부분에 몸이 그려졌음).
- **물 색은 선명하게**(유리 색조보다 훨씬 진하게) + 수면은 "또렷하고 밝은 선" + 수면 위는 "맑고 색 없음". 이렇게 하니 물 경계가 잘 드러났다(사용자 확인). 물 색은 사람마다 다르게.
- **수조는 막힘 없는 한 통**: "겨드랑이 선에서 허벅지(듀얼바디는 발목 위) 끝까지 막힘 없는 하나의 빈 공간, 벽·칸막이·밀봉 없음, 물은 가장 아래부터 차올라 다리를 먼저 채운 뒤 하나의 수평 수면까지 오른다, 몸통에 물이 있는데 다리가 비는 일은 없다." (4인 프레임 컷에서 "다리는 비고 몸통만 찬" 이미지가 나온 것이 계기.) 100% 등록 내용물 문구의 "가슴 쪽이 촘촘하고 허벅지 쪽은 성김"은 "허벅지까지 고르게 퍼짐"으로 교체.
- **내용물**: 등록된 3종(백합 들판·장미 정원·반딧불이 밤)에 4인용으로 벚꽃잎(**문구는 새로 쓴 미등록**). 100%는 등록 문구, 부분 수위는 "물속에만 있고 수면 위로 뜨지 않음". 0%는 내용물 없음.

### 43-4. 경계 · 뒷배경 · 컷 끝
- **경계는 겨드랑이 높이의 일자선**(몸을 한 바퀴 도는 수평선, 가슴·등·위팔 윗부분을 가로지름). 그 위(얼굴·귀·목·어깨·상체 윗부분·위팔 윗부분)만 실제 피부. 쇄골선 경계보다 가슴 표현 문제가 줄었다. 듀얼바디·프레임 힙컷 모두 정상 생성(등록 경계는 쇄골선·겨드랑이 V자뿐이라 새 경계).
- **뒷배경 선**: 빈 수조 너머로 선·머리카락이 비치면 투명 표현이 좋아지지만, **굵은 흑백 줄무늬는 혼란** → **손 한 뼘 간격의 아주 가는 선 몇 줄**(세로·가로·성긴 격자 랜덤)로 변경. 수조 너머로 선이 살짝 휘어 보이고 몸 뒤로 내려온 머리카락이 비치도록 문장 추가.
- **프레임 컷 끝이 공중에 뜸**(받침 문구를 뺀 첫 힙컷 그룹) → "모든 조각이 자기 두 둥근 끝 위에 바닥에 직접 서 있고(받침대 없음), 끝 아래에 틈이 없고 접촉 그림자가 지며 허공에 뜨지 않는다" 문장을 몸 문단과 맨 앞 틀 문단에 넣어 해결.

### 43-5. 프레임 힙컷 그룹 틀
- **등록된 프레임 그룹에는 힙컷이 없다**(데미스탯·쓰리쿼터만). 등록 데미스탯 듀오/트리오의 틀(맨 앞 문단·인물 블록·경계·설정·조명)을 그대로 쓰고 컷 문구만 "허벅지를 조금 내려간 엉덩이선 바로 아래"로 바꿔 힙컷 그룹을 만든다. 몸 문단만 수조로 교체. 4인은 다른 등록 트리오의 1명을 #4로 붙임(국적 중복 회피). 등록 틀은 피어싱 문단을 포함(짧은 버전에서는 제외).

### 43-6. 4인 프롬프트 길이 줄이기 (성공)
- 긴 v4(프레임 힙컷 3,780단어 · 듀얼바디 전신 4,964단어)에서 수위 표현이 흔들렸다. **짧은 버전**(`run_tankfill_v5.py`): 사람마다 똑같은 90자 이상 문장은 한 번만 쓰고, 맨 앞에 "나머지는 #1과 동일, 달라지는 건 수위·물 색·내용물·유리 색조뿐" 문장 추가. 단 **수조 연결 문장·꼭 닫히는 끝 문장·바닥 접촉 문장·평평한 컷 단면 문장은 사람마다 유지**. 프레임 힙컷은 피어싱 문단 제외. 결과 3,021→2,218 / 4,808→3,722단어.
- **결과: 짧은 버전에서 프레임 힙컷 4인은 1차에, 듀얼바디 전신 4인은 2차에 물 조절이 잘 나옴.** 물 색 구분도 좋음. **3~4인 그룹은 이 짧은 방식을 기본으로 한다.** 길이가 유일한 원인이라는 증거는 아니지만 효과는 확인됨.

### 43-7. 샘플 파일 판정 현황
- 정상: `..._DualBody_TransparentTypes_3.md`(3/3), `..._DualBody_Opaque_Test_3.md`의 1번(석재)·3번(듀오), `..._Trio_AllDualBody_TankFill_v2.md` 계열(가득·비움 정상, 4분의 3은 몸이 보여 문장 수정), `..._HipFrame_TankFill_Thin.md`(대체로 정상, 가슴 쪽 표현 어려움), `..._TankFill_A/B_..._v3.md`(듀얼바디 전부 성공, 프레임 컷은 끝이 공중에 뜸 → 수정), `..._TankFill_A/B_..._4_short.md`(성공).
- 실패: `..._DualBody_Opaque_Test_3.md` 2번(목재 L1), `..._DualBody_Wood_L3_Test.md`(목재 L3).
- 판정 미보고(이전부터): UR 다층 재질 2/3/4종(신발 포함) 2개 파일, Simplified_3, UR_FullBody_3, UR_Center, 임산부 컷 샘플, USSBBW 사진 스타일 3.
- 생성기(`master/`): `gen_trio_mix2.py`(DB 유형·수위·겨드랑이 경계·4인·`SHORTMODE`), `gen_hipframe_tank.py`·`gen_hipframe_tank2.py`(프레임 힙컷 수조 그룹), `run_tankfill_v3.py`·`v4`·`v5`(시험 실행). 백업: `LumineX_generators_backup_2026-10-11.zip` 갱신. 모두 시험용, 등록 안 함.

### 43-8. 열린 과제
- **등록 계획**: 듀오·트리오를 먼저 등록, 4~5인은 시험 후 추가. 5인은 미시험. 등록 시 구조 조합(실사·듀얼바디·UR·프레임 컷)은 검증된 것만, 길이는 짧은 방식 기본.
- 수조 듀얼바디 그룹을 번들 카테고리로 만들지(수위 4단계 × 내용물 4종 × 유리 색조 6종 × 물 색 6종), 2인 100/0 · 3인 100/50/0 · 4인 100/50/25/0 구성은 사용자 결정 대기. 벚꽃잎 내용물 문구는 미등록 상태에서 정상 확인 필요.
- 불투명 듀얼바디(석재) 추가 시험, 목재용 단면 문구 재작성 여부, 프레임 컷 + 실사 혼합 시험, 하체 투명 재질 UR 재시험.
- 42-6과 41-5의 열린 과제는 그대로(Master Mix 오류 약 20개 패치, 극단 체형 번들, HOF/SSS 티어, `.bak`, `--v1` 221개).

## 44. 수조 그룹 5인 시험 · Tank Body Formula 210 등록 (v6.48, 2026-10-11)

### 44-1. 시험 결과
- 짧은 방식(동일 긴 문장은 첫 사람에게만, NOTE 문장 + KEEP 문장은 사람마다 유지, 피어싱 문단 제거, 사람별 유리 색조 한 줄)으로 4·5인 시험.
- **듀얼바디 전신 5인**: 1차 성공, 물 조절 양호. **프레임 힙컷 5인**: #1이 발목컷으로 반복 → 불안정, 등록 제외. 4인 프레임은 성공.
- 등록 전 확인(2·3인 각 1개): 프레임 힙컷 2인은 1차 발목컷·2차 힙컷 성공, 프레임 3인·듀얼바디 2·3인은 1차 성공. 프레임 힙컷이 가끔 발목컷으로 새는 경향(2·4·5인에서 관찰)은 알고 등록(보강 문장은 넣지 않기로 결정).

### 44-2. 등록 번들 (Tank Body Formula, 카테고리 `🏺 Living Artifact · Tank Body Formula`)
- 파일: `la_tank_210_bundle.json`, `patch_la_tank_1_json.py`, 생성기 `master/gen_tank_bundle.py`(`gen_trio_mix2.py`, `gen_hipframe_tank2.py` 사용, 시드 20261011).
- 키: `la_tank_db_{duo|trio|quad|quint}_NN`(듀얼바디 전신 L3, 각 30 = 120), `la_tank_hip_{duo|trio|quad}_NN`(프레임 힙컷, 각 30 = 90).
- 수위: 2인 100/0, 3인 100/50/0, 4인 100/50/25/0, 5인은 4단계 + 1명(100/50/25 중 랜덤), 순서 랜덤. 내용물 5종(백합 들판·장미 정원·반딧불이 밤·벚꽃잎·물고기와 수초) 사람마다 다르게, 0%는 없음. 유리 색조 6종, 물 색 6종 랜덤. 벚꽃잎·물고기와 수초 문구는 이번 등록에서 처음 포함.
- 제목에 수위·체형(USSBBW)·메이크업·물 색·내용물·유리 색조를 포함. 평균 단어 수: 듀얼바디 2000/2950/3770/4560, 프레임 1360/1870/2270.
- 메타: group_size, aspect_ratio, format(`tank-dualbody`/`tank-hipframe`), fills, water_colors, contents, glass_tints.
- 등록 결과: 메타 스크립트 `categories added=1, keys added=210`, `(Get-ChildItem presets\la_*.json).Count` = **12528**, commit `1d65b057`(첫 `git add`는 `presets_meta.py` 경로가 `core/presets_meta.py`라 실패 → 경로 수정 후 성공).

### 44-3. 등록 프리셋 문법·중복 오류 패치 (commit `56bc2c0b`)
- `patch_la_textfix_1.py`(`--dry` 지원, 여러 번 실행해도 안전): `beach at with`→`beach at midday with` 9곳, `a open-air`→`an open-air` 5곳, `a autumn`→`an autumn` 4곳, `metallic platinum metallic leather`→`metallic platinum leather` 6곳. 대상 24개 파일(Master Mix `la_mx` 17 + Light Mix `la_lm` 7, 같은 배경 라이브러리 사용). 재실행 시 0개 확인. 합계 변화 없음(12,528).
- 이로써 40-3·41-5·42-6의 'Master Mix 오류 약 20개 패치' 과제는 완료.

### 44-4. Extreme Body Formula 180 등록 (commit `340a366e`)
- 카테고리 `🏺 Living Artifact · Extreme Body Formula`, 키 `la_xb_solo_001~120`, `la_xb_duo_01~30`, `la_xb_trio_01~30`. 번들 `la_extreme_180_bundle.json`, 스크립트 `patch_la_extreme_1_json.py`, 생성기 `master/gen_extreme.py`(`gen_master_v2.py` 복사본: 체형은 USSBBW·hourglass SSBBW만, 중복 허용, 나머지 축 전부 기본 랜덤, 시드 20261012).
- 41-3 규칙 적용: 페인트 재질 B 60 : A 40(그 밖은 B 고정), 솔로 앉은 자세(120개 중 74개), 하이앵글 0, 듀오 이상 극단 포즈 제외. 임산부 제외.
- 시험 3개: 솔로 A(3차 성공), 솔로 B 앉은 자세(1차), 듀오(1차). 합계 12,528 → **12,708**.

### 44-5. 제목 공통 틀 교체 (commit `88e19b0b`)
- 틀: `시리즈 인원 #번호 · 체형 · 재질 · (솔로만 포즈) · 배경 · 메이크업`. 메이크업 꼬리표(강함·강화·포인트·N단계) 제거, 포즈는 영어 문장 44개+앉기 11개를 한글 짧은 라벨로 변환, 3인 이상은 `외 N`. 수조는 `Tank DB|Hip 인원 #번호 · 듀얼바디 L3|프레임 힙컷 · 수위 · USSBBW · 수조+내용물 · 메이크업`. 제목은 한글/영어 혼용(체형 이름·재질 변종은 영어 원문 유지, 한글 이름표는 보류).
- 길이: 평균 74자(중앙값 70, 최대 138). 예전 Master Mix 394자·Shoe Mix 438자.
- 대상 12개 시리즈 2,850개 중 실제 변경 **2,550개**: la_mx·lm·pm·mm·wood2·stone2·wsmix·xb·kl·tank_db·tank_hip. **la_sm(Shoe Mix 300)은 repo에 등록된 적 없어 건너뜀**. 스크립트 `patch_la_retitle_1.py`(`--dry` 지원), 매핑 `la_retitle_map.json`, 옛 제목 백업 `retitle_old_titles_backup.json`(되돌리기용), 공통 함수 `master/retitle.py`.
- 새 번들을 만들 때는 `master/retitle.py`의 `retitle()`/`retitle_tank()` 규칙으로 제목을 만들 것. 번호만 있는 시리즈(Core·Maximalist·Mixed·Pregnant 등 약 3,000개)와 Blend 계열은 미적용.

### 44-6. 제목 공통 틀 2차 (commit `21fa533b`)
- 번호만 있던 시리즈 3,450개 교체: Core(솔로~14인) 700, Mixed 450, Pregnant 500, Maximalist 5종(Irezumi 300·UV 300·Goldleaf 300·Stainedglass 300·Botanical 300 중 해당분) 및 Wax 60·Obsidian 60·Crystal 90·Scale 90. 스크립트 `patch_la_retitle_2.py`는 **repo의 등록 파일(prompt·meta)에서 직접 항목을 뽑아** title만 교체(번들과 등록분이 달라도 안전, 재실행 0개 확인), 백업 `retitle2_old_titles_backup.json`.
- 틀: Core `Core 솔로 #NN · 체형 · 패턴 · 인물(인종/글램)`, Mixed `· 체형 · 패턴`, Pregnant `· 임산부 체형 · 패턴`, Maximalist `· 체형 · 모티프 · 포즈(솔로만)`. **6인 이상은 패턴/모티프 + 외 N만**. 헤드는 Solo→솔로 … Sextet→6인, `11-Woman`→`11인`. 금박은 `금박 Electric Crimson`, 스테인드글라스는 `스테인드글라스`로 표기.
- 미적용(이미 설명적이거나 항목이 부족): Blend 계열, Piercing/Silverfox 계열, Mix3·Random 330개, Mixed7, 극단 힐(xheel), CJK Face, Shoe Mix(미등록). 극단 체형 시리즈는 체형이 거의 super hourglass 하나라 제목에서 구분되는 건 재질·포즈 정도.

### 44-7. 열린 과제
- 프레임 힙컷 5인 안정화(원인 미상: 기본 트리오 템플릿 또는 5인 밀집), 프레임 힙컷 발목컷 경향, 등록 후 샘플 점검.
- 남은 과제: HOF/SSS 티어, `.bak` 5개, `--v1` 221개, 미보고 판정(UR 다중 재질, Simplified_3, UR_FullBody_3, UR_Center, 임산부 컷, USSBBW 사진풍 3).

## 45. 테마 그룹 바디페인팅 — 사람마다 테마 색 하나 (v6.49, 2026-10-12)

### 45-1. 개념과 시험 결과
- 한 장면에 2~7명이 서 있고 각자 테마 항목 하나(색 + 모티프)를 맡는다. 예: 무지개 7, 오행 5, 사계절 4, 사신 4, 삼원색 3, 불·물 2, 해·달 2.
- 최종 공식으로 시험한 결과(시도 횟수는 처음 성공까지):

| 테마 | 인원 | 결과 |
|---|---|---|
| 사계절 (봄 로즈말링·여름 델프트·가을 쿠타니·겨울 그젤) | 4 | 1~3회 차 성공 |
| 오행 (목 용천 청자·화 조칠·토 나스카·금 은입사·수 이탈라) | 5 | 1~3회 차 성공, 일부 인물 팬티 모양으로 칠해짐(케바케로 보류) |
| 불·물 (조칠·이탈라) | 2 | 1회 차 성공, 팬티 모양 1건 |
| 무지개 (조칠·나스카·쿠타니 노랑·청자·볼레스와비에츠·이탈라·청나라 가지색 유약) | 7 | 2회 차 성공 |
| 삼원색 (조칠·쿠타니 노랑·볼레스와비에츠) | 3 | 1회 차 성공 |
| 사신 (청룡 청자·백호 징더전·주작 조칠·현무 은입사) | 4 | 3회 차 성공 |
| 해·달 (쿠타니 노랑·이탈라 보름달) | 2 | 1회 차 성공 (초승달·별 문양일 때는 6회 모두 실패) |

### 45-2. 실패 원인 정리 (시험 20여 건)
- **단색 + 이름 없는 추상 문양**(점·물결선·별·격자·핀스트라이프·소용돌이 등) → 의상으로 읽힘. 26-4의 "전통 공예명 앵커 필수·모양 이름 금지"와 같은 현상.
- **부정 설명**("not clothing / not a bodysuit / bare skin / no neckline") → 생성 거부(무지개 v4).
- **색 이름 대문자 태그**(`[RED — …]`, `THE RED WOMAN`) → 화면에 영단어가 찍힘. 태그에 색 이름을 넣지 말 것.
- **마스터 생성기(la_ 재질 시리즈) 기반**: flat paint 문구와 임신·극단 문구 → 의상/실패. 이후 Core 번들(`la_core_*`) 기반으로 전환.
- **Core 7인 틀에서 4명만 뽑기**: 의상(한 명이 크게 그려질수록 의상으로 읽힘).
- **문양 밀도**: 4인은 light scatter로 통과했으나 5인은 light·moderate 모두 의상. dense(원본 문구)로 복원하면 페인트로 나온다.
- **체형**: 2~5인에서 극단 체형("extraordinarily large")이면 생성 막힘이 늘어남(큰 체형 + 세로 표기 0/2, 큰 체형 + 가로 표기 3회 차, 보통 체형 + 세로 표기 1회). 가슴 강조 체형만 빼는 가설은 틀렸음.
- **초승달 + 별 모티프**(종교/국기 상징 가능성) → 해·달 6회 모두 실패, 보름달 원반·구름으로 바꾸자 1회 성공(표본 작음).
- **청나라 황유(imperial yellow) 앵커** → 해·달 실패, 폐기. 노랑은 쿠타니 도자기의 노란 바탕으로 교체.
- **가로/세로**: Core 2~4인 머리말이 `landscape-orientation … 3:4/4:5`로 비율과 충돌해 가로로 나오는 경우가 있음. 보통 체형이면 `vertical portrait-orientation … taller than it is wide`와 끝줄 `portrait 8K`로 교정 가능, 큰 체형과 겹치면 실패. 5인은 5:4 가로가 원래 설계.

### 45-3. 확정 공식
1. 베이스 = Core 번들 프롬프트(2~5인 `la_core_{duo|trio|quartet|quintet}_NN`, 7인 `la_core_septet_NN`). 사람마다 **세 문단만 교체**: 몸 그림(body art)·신발(footwear)·체형(physique, 2~5인).
2. 몸 그림은 원본 Core 구조 유지: `painted in {공예명} — {테마 색 바탕 + 테마 모티프}, wide {band} bands following every deep crease, {dense … filling the space between bands}, pigment on living skin, covering her whole body below the jaw — her neck, shoulders, bust, belly, hips, rear, both arms down to the fingertips and both legs down to the ankles — with no bare skin anywhere, face unpainted, pattern fading at the neck.`
3. 공예명은 실존 전통 공예(기존 풀 39종 + 신규 앵커). 모양 이름·천 연상 단어 금지. 주황·노랑은 "피부색보다 진하고 불투명" 문구.
4. 2~5인 체형은 보통 비율 5종(운동형·아워글래스·슬렌더·근육형·풍만형)에서 랜덤, 극단 체형 문장은 삭제. 7인은 septet 원문 유지.
5. 신발: 같은 색 플랫폼 스틸레토 샌들 + "칠한 다리가 엉덩이부터 발목까지 끊김 없이 샌들로 이어진다".
6. 테마 줄 1줄(`Theme: … each woman's whole body one clearly different colour.`), 색 이름 대문자 라벨 금지.
7. 2·3·4인은 portrait 표기(보통 체형일 때만), 5·7인은 원본 표기.
8. 7인: septet 사람 문단의 `Painted in … covering …` 문장과 `Shoes:`만 교체.

### 45-4. 색별 공예 앵커
- 빨강: Chinese carved cinnabar lacquer(불꽃·구름 / 봉황), Swedish Dalarna kurbits
- 주황: Peruvian Nazca(테라코타 주황), Japanese Kutani(러셋 주황 + 단풍잎)
- 노랑: Japanese Kutani(황금빛 노란 바탕)
- 초록: Norwegian rosemaling(봄꽃), Chinese Longquan celadon(대나무·소나무 / 용)
- 파랑·남: Polish Bolesławiec, Dutch Delft(파도·조개), Finnish Iittala(물결·보름달)
- 보라: Chinese Qing aubergine glaze(무지개 7인에서 통과)
- 흰색: Russian Gzhel(눈송이), Chinese Jingdezhen(호랑이·대나무)
- 검정·은: Korean eunipsa silver inlay(거북·뱀·파도)
- 풀에 없는 색(분홍 등)은 미해결.

### 45-5. 산출물
- 생성 라이브러리 `master/theme_lib.py`(+ `craft_pool.json`, `gen_theme_base.py`, `gen_theme.py`), 시험 파일 `LumineX_Theme_*`(무지개 v4~v9, 사계절 v1~v7, 오행 v1~v3, 삼원색 v1, 공예앵커 v1·v2·Duo, 샘플 7종, 샘플 v2 3종). 백업 `LumineX_generators_backup_2026-10-12.zip`.

### 45-6. 열린 과제
- **등록 설계 미결정**(사용자가 회사라 집에서): 후보 테마 7종, 테마당 개수, 제목에 테마명 포함(`시리즈 인원 #번호 · 테마 · 체형 · …`), 베이스 선택 규칙, 2·3·4인 portrait 표기 적용 여부.
- 테마 후보 추가: 4원소, 12지·10간, 분홍 앵커 탐색.
- 불확실: 해·달 달 문양 가설(n=1), 부위 목록의 팬티 모양 억제 효과 미확인, 쿠타니 노랑 반복 확인, 5인 수율이 낮음, 무지개 7인의 청나라 가지색 유약 반복 확인.
- 보류: `LumineX_TankContents_New_3.md`(수조 새 내용물) 판정 3건과 새 내용물 문구 등록.
- 44-7의 열린 과제는 그대로.


## 46. Face Sculpt Formula — 얼굴 성형 축 · 귀 스타일 · 입술 12종 · 그룹 (v6.50, 2026-10-13)

> 이 장은 v6.49까지 핸드오프에 없던 얼굴 컷(Face Sculpt) 작업 전체의 기록이다. 확정 사양의 최신본은 `LumineX_FaceAxes_Spec_v2.md`(이 문서와 같이 보관)이며, `LumineX_FaceAxes_Spec_v1.md`·`LumineX_FaceAxes_Confirmed.md`의 엄니·크기 항목은 폐기됐다. 판정은 제미나이 기준·사용자 정상/이상 번호 보고 방식이다.

### 46-1. 개요와 등록 현황
- 얼굴 컷 새 카테고리 `🏺 Living Artifact · Face Sculpt Formula`(키 `la_facesculpt_NNN`, 300개: 눈 120 + 입술 120 + 얼굴 유형 60).
- **v1 300 등록 완료**: 번들 `la_facesculpt_300_bundle.json` + `patch_la_facesculpt_1_json.py` → 메타 `patch_livingartifact_2_meta.py`(categories added=1, keys added=300) → commit `c02d217b`. 앱 카테고리 표시는 확인 대기.
- **v2 300(엄니 제외 · 입술 17종 반영) 등록 완료(2026-10-13, commit `baa1e553`, 파일 300개 확인, 앱 카테고리 표시는 확인 대기)**: 아래는 당시 절차 기록 — `la_facesculpt_300_bundle_v2.json` + `patch_la_facesculpt_2_json.py`. 같은 키(`la_facesculpt_001~300`)를 덮어쓰므로 메타 재등록 불필요. 등록 절차: 두 파일을 `C:\Dev\LumineX\preset_builders\`에 둔다 → `$env:PYTHONUTF8="1"` → `python preset_builders\patch_la_facesculpt_2_json.py` → `(Get-ChildItem presets\la_facesculpt_*.json).Count`로 300 확인 → `git add -A` / `git commit` / `git push` 각각 한 줄(커밋 메시지 끝에 Co-Authored-By·Claude-Session 줄).
- v2 통계: P5 40·P15 45·P25 42·P50 68·P100 78·P150 9·P200 18, 추가 축 0개 25·1개 101·2개 150·3개 24, 귀 모드 혼합 85·귀걸이 77·철 58·단일 47·혼합형 33, 구멍 1개 75·2개 161·3개 64, 단어 수 833~2,147(평균 약 1,587), 한글·연속 중복 없음.

### 46-2. 결정 이력 (2026-10-12~13)
- **방향**: 눈·입술·코·턱선 축은 프롬프트의 일부일 뿐, 기본 랜덤 틀(귀 추·피어싱·렌즈·헤나·스티커) 위에 얹는다. 주인공 부위 주변 피어싱은 최소화.
- **귀 추**: 한 구멍에 다 달면 처짐이 과해 2구멍으로 나누기 시작 → 2구멍 고정은 부자연스럽다는 의견으로 **1~3구멍, 구멍별 숫자 없이 귀당 총 개수만**. 처짐은 자연스럽고 약하게, 쇄골 높이를 넘지 않고 공중에 매달리게. 추 크기는 "최소 주먹만큼, 귓볼보다 훨씬 큼"(작게 나온 샘플 지적 후 문구 추가).
- **귀 스타일 변주**: 항상 철 추면 변주가 없다는 사용자 지적 → 모드 5종(철 추 25·혼합 금속 35·단일 금속 15·대형 귀걸이 15·혼합형 10). 그룹은 혼합형 제외.
- **새 축 시험(File1~6)**: 슬롯·피부톤·눈썹 대용·치아·배경·매크로·얼굴 유형 4종·목/쇄골 컷 등. 질문한 항목 외에는 모두 정상 생성. 결정: 눈썹 대용은 헤나 최상 + 맨살·보석 라인·스터드 줄·작은 링 줄·스파이크·진주·참·산호(바 피어싱 제외), 배경은 실내/실외 아웃포커스·스튜디오 색의 차가운 중간~어두운 톤(피부톤과 비슷하거나 밝은 색 금지), 검은 피부는 밝은 금속·보석.
- **랜덤 풀 한도**(풀이 넓어져 검토): P≤25 총 3(물건 축 2) · P50~P100 총 2(물건 축 1) · P≥150 테마 팩만 물건 축, 피부톤·배경 가능. 매크로·목/쇄골·귀 연구는 별도 프레임이라 풀 제외.
- **눈 트임**: 비교 시험에서 코 쪽 안쪽은 거의 같고 바깥쪽만 살짝 길어져 "이 정도면 테스트 된 듯" → 단계 3·4·6·8배로 단순화, 코 쪽 문장 삭제, 라이너는 메이크업 색 따름(메이크업 없음이면 없음).
- **엄니 제외**: 흑요석·상아·무쇠 엄니가 크게 나오고 굵기·길이·"코 폭 이내" 문구를 줄여도 거의 안 변함(크기 문구 무효) → 사용자 제안으로 Face Sculpt에서 제거. 코·엄니 별도 시리즈로 나중에.

### 46-3. 듀오·트리오 (샘플 v3→v5)
- 규칙: 조 단위 귀 모드·구멍 수, 공유 Ear weights 문단 + 인물별 피어싱 문단, 전원 같은 배경 하나, 얼굴 피어싱 N은 듀오 12·트리오 10, 귀당 추 듀오 6·트리오 4, 물건 추가 축은 길이 때문에 제외.
- **v3→v4**: "다른 공간에서 찍은 사진처럼 나뉘어 보인다" 지적 → 어깨가 닿게 붙여 세우기, "한 대의 카메라·한 순간의 한 장·콜라주 아님", 전원에게 같은 방향·같은 색 조명 하나, 구분선·다른 배경 없음 문구. 이후 **2~3인은 모두 1회에 성공**(사용자 보고).
- **v5**: 입술이 든 조는 정면/45도를 섞는다(항상 45도는 아님). 10개 중 입술 든 조 6개에서 4개가 45도.
- **결함(2026-10-13 발견·수정)**: 그룹 번들의 혼합·단일 금속 모드에서도 인물별 문장에 "추는 항상 검은 무쇠"가 남아 있어 샘플이 무쇠처럼 보였을 가능성이 크다 → 해당 모드에서 삭제. 낮은 N에서 귀 연골 개수가 0일 때 "above them sit zero ..." 문장이 생기던 오류도 수정(문장 삭제).
- 번들 구성안(미생성): 듀오 60 + 트리오 40.

### 46-4. 입술 12 계열 (신규 6종 채택)
- 기존 11종 항목(러시안 립 6단계·체리 립 +1·키홀 퓨트 +1·큐피드 보우·립 플립·립 리프트) 외에 모양으로 후보 12종을 발굴해 극단/일반 비교 시트(`LumineX_LipShapes_Compare_12.md`·`_normal.md`)로 시험 → 일반 표현은 "특징이 약하다". 윤곽이 확실히 달라지는 6종만 극단 표현으로 채택: **덕 립·드롭 립·바르도 립·와이드 립·오(O) 립·고양이 입(ω)**. 3인 풀 프롬프트 2장(A 45도 덕·드롭·바르도 / B 정면 와이드·오·고양이)과 단일 컷 4개 샘플은 모두 정상.
- 제외/이관: 하트·푸딩(겹침), 스마일 코너 리프트·처진 입꼬리(표정 축 후보), 게이샤·클라라 보우(메이크업 모양 후보).
- v2 번들 입술 120 배분: 기존 11종 68(러시안 6×6, 체리 8, 키홀 8, 큐피드 6, 플립 5, 리프트 5) + 신규 6종 52(덕·드롭·바르도·와이드 각 9, 오·고양이 각 8). 입술 단일 컷은 45도라 와이드·오·고양이도 45도로 나온다.

### 46-5. 4·5인 샘플 (판정 대기)
- 파일 `LumineX_FaceSculpt_4to5_Samples_6.md`(4인 3·5인 3, 전부 랜덤). 얼굴 피어싱 N 4인 8·5인 6, 귀당 추 4, 16:9, 5인은 정면만, 4인은 입술 든 조에 한해 정면/45도. 인물별 추 목록·"실제 살" 문장을 삭제해 길이 감축: 4인 2,628~2,949단어, 5인 3,377~3,616단어(길이 위험). 국적 3종뿐이라 중복 허용, 메이크업은 한 조 안에서 서로 다르게(메이크업 없음 최대 1, 유형 고유 메이크업 제외).

### 46-6. 생성기 구조와 백업
- 체인: `gen_facesculpt.py`(기본 단일 컷·축 정의) → `mk_file7.py`(랜덤 풀 샘플러·BGS/BROWS/TEETH/SKINS/SLOTS 공용) → `gen_fs2.py`(v2 번들: `CAN2`·`fix_canthus`·`base2`·`draw2`·`build2`, 엄니 `tusk_set=set()`로 비활성) → `gen_fs3.py`(입술 17종 반영 최종 번들) / 그룹은 `mk_group2.py`→`mk_group3.py`(듀오·트리오 v3~v5)→`mk_group5.py`(2~5인 일반화, 신규 입술 NEWLIP 텍스트 포함). `mk_group4.py`: 신규 입술 3인 시트. `mk_fs_new.py`: 신규 입술 단일 컷 샘플.
- 백업: `LumineX_generators_backup_2026-10-13.zip`(작업 폴더 `bk/` 전체). 샌드박스 초기화에 대비해 outputs에 둔다.
- 검증 습관: 한글 문자·연속 중복 단어 스캔, 키 유일성, 단어 수 분포, 문장 교체 후 `assert`.

### 46-7. 교훈 (제미나이 기준)
1. **크기 단어는 안 먹힌다**(엄니·트임·입술 폭): 문구로 줄이거나 키워도 거의 변하지 않음. 실루엣·구조가 달라지는 항목(덕·드롭·와이드·오 립)만 효과가 있다.
2. 일반 강도 표현은 특징이 약해 보인다 — 새 항목은 극단 표현으로 먼저 시험.
3. 그룹은 "한 장의 사진·같은 조명 하나·붙여 세우기" 문구가 필요하고 5인에서는 길이가 한계에 가깝다(3,400단어 이상 위험).
4. 번들 샘플은 손으로 배정하지 말고 번들과 같은 확률로 뽑는다(샘플 쏠림 방지).
5. 폭주를 막는 문장 교체는 한 군데 고치면 다른 모드(그룹·단일)에도 같은 결함이 있는지 확인한다.

### 46-8. 열린 과제
- (완료) v2 등록 — 앱에서 Face Sculpt 카테고리 표시 확인만 남음.
- 4·5인 샘플 판정, 듀오·트리오(·4·5인) 번들 생성·등록(카테고리 예: Face Sculpt Duo/Trio Formula; 🏺로 시작해야 메타 스크립트가 받음).
- 엄니·코 별도 시리즈, 표정·립 메이크업 모양 후보 검토, 피어싱 테마 팩 확장·재질·문화권 주얼리, Piercing Frame v2 후보(기존 360 유지), 티어(HOF/SSS), `.bak` 5개 복구 여부.
- 이전 보고 대기였던 듀오·트리오 v2, EarStyles v3, NewAxes File 1·2는 사용자가 "질문한 것 외에는 다 잘 생성"이라고 한 범위에서 정상으로 본다.


### 46-x. 고무 느낌(실사 저하) 원인과 수정 (2026-10-13 오후)

- **증상**: Face Sculpt 샘플 전반(브랫츠·바비 유형과 옆 일반 인물)에서 피부가 고무·마네킹처럼 나옴. 예전 대조 프롬프트(귀걸이 얼굴 컷, 920단어)는 잔털·주름·입술 결이 나옴.
- **찾은 원인**: ① 유형 문단(브랫츠·바비·서큐버스·인어)에 `doll`·`airbrushed`·`high-gloss`·`poreless`·`luminous` 같은 장난감/그림 단어가 있고 모공 문장이 약함. ② 프롬프트가 너무 김: 얼굴 컷 단독 약 1,900단어 중 피어싱·귀 추 문단이 약 1,300단어이고, 귀 추 20개 문장에서 재질 설명(`rough-cast matte yellow gold with a hammered… raw gold ingot`)이 20번 반복됨. ③ 배경(비 오는 밤 네온)은 원인이 아님(순흑으로 바꿔도 잔털 안 나옴). ④ 다인 컷은 얼굴이 작아져 질감이 약해짐(한계).
- **A/B 결과(사용자)**: 대조 틀 + 브랫츠·바비 → 주름·입술 결·바비 잔털. 길이·배경 3종: 귀 추 반복 압축만(2번)·압축+순흑(3번)은 잔털·주근깨 보임, 배경만 순흑(1번)은 잔털 없음 → **압축이 효과**. 압축 번들 샘플 4개: 1인 브랫츠·1인 일반 잔털 있음, 듀오(바비) 잔털 몇 개, 트리오(브랫츠) 아주 드물게 몇 가닥.
- **수정(생성기)**: `ear_styles.py`의 `items()` — 단일 금속은 재질 설명을 문두에 한 번만, 혼합은 `SHORTM`(짧은 금속명), 사슬은 `chain`으로 압축(헤더에 `each hanging on its own thick heavy chain of the same metal [as the weight]`). 유형 문단은 `gen_fs4.py`의 `SW` 치환(인형 단어 제거 + `real visible pores` + 끝에 `Her whole face, ears and neck are real living flesh with real pores…`). **문장은 더하지 않고 줄임**(평균 1,587 → 1,472단어, 최대 2,147 → 1,869).
- **미결**: 일반 인물의 `surgically sculpted … override her natural features` 문장 교체(A/B/C) 결과는 사용자가 아직 보고하지 않음. 그룹(듀오·트리오)의 귀 추 문단은 압축 대상이 아니라 아직 김(듀오 약 2,100, 트리오 약 2,600단어).
- **번들 교체**: `la_facesculpt_300_bundle_v2.json`을 위 수정본으로 교체(이전은 `…_v2_prev2.json` 샌드박스 백업). 키·카테고리·제목·메타 분포는 동일(입술 17종·귀 모드·구멍 수·피어싱 단계 개수 일치) → 등록 절차는 그대로(`patch_la_facesculpt_2_json.py`, 메타 스크립트 불필요).
- **스크립트**: `ear_styles.py`(압축 반영), `gen_fs4.py`(v3 후보 = 최종 v2 생성), `mk_trio_arch.py`·`mk_n_compare.py`·`mk_bratz_len.py`·`mk_samples_v3.py`(시험 생성기).

- **일반 인물 사실감 문장 B 채택(46-x 후속)**: A/B/C 비교(각 1회, 사용자) — 얼굴 입체는 C가 가장 좋고 A는 너무 깔끔, 0번도 괜찮음. A(`surgically sculpted` 교체)는 제외하고 **B만 채택**: 일반 인물(눈·입술 240개)의 `Her whole face, ears and neck are real living flesh…` 문장을 `…real living skin with visible pores and faint peach-fuzz hairs, slightly asymmetrical, never airbrushed and never smooth like plastic, real wet catchlights in the eyes, individual hair strands catching the light.`로 교체(길이 거의 동일, 단독 컷에 있던 마침표 누락도 해결). 유형 60개는 별도 구조라 그대로. `gen_fs5.py`가 최종 생성기(번들 평균 1,477단어, 최대 1,875), 듀오·트리오 시험 생성기(`mk_trio_arch.py`의 `real()`)에도 같은 교체 반영.

- **피부 문구 교체 + 점·주근깨 (46-x 후속 2, 2026-10-13 저녁)**: 한국인 강남언니 3인 시험 — 20대 포함 전원 마네킹 피부, 나이를 30대로 바꿔도 마네킹(나이가 핵심이 아님). 브랫츠 3인(부드러운/인간적인 메이크업)은 실사 느낌 → 차이는 피부 문구(브랫츠는 `real visible pores`, 일반 인물은 `luminous … porcelain … clear glass-skin glow`/`smooth dewy skin`)와 눈·입술 강조 인물의 `surgically sculpted` 문장. **일반 인물 피부 문구 교체** 후 "조금은 인간 피부 같다, 주근깨·작은 반점·적당한 주름·잔털, 특히 입술 주름이 실사 느낌을 좌우"(사용자). 적용(`gen_fs6.py`): `luminous fair porcelain complexion … clear glass-skin glow`→`fair complexion … real visible pores`, `luminous light-neutral …`→`… and real visible pores`, `luminous milky ivory-fair … smooth dewy skin`→`milky ivory-fair … real visible pores`, `pale porcelain skin … soft natural glow`→`pale skin … real visible pores`, `warm glossy sheen`→`warm natural sheen and real visible pores`, `a glass-skin highlight`→`a soft highlight`, `luminous `(렌즈 앞) 삭제, 사실감 문장 B에 `with a few small natural beauty marks and freckles` 추가(약 +10단어). 번들 평균 1,484단어(최대 1,887). 키·카테고리·메타 동일.
- **강남언니 메이크업 자체**(`sculpted contour with a satin highlight`, `glossy rose-coral lips`)의 광택 단어와 `surgically sculpted` 문장은 그대로 둠(검토 대상). 입술 주름은 사실감 문장의 `lips with real vertical texture`(28-10)로 보강 가능하나 길이 때문에 미적용.

## 47. 애니 피어싱 트랙 — 실사+애니 한 얼굴 혼합 (v6.52, 2026-10-13)

> 목표: 피어싱 얼굴 컷에서 얼굴은 애니, 금속은 실사로 섞기. 판정은 제미나이 기준·사용자 정상/이상 번호 보고. 생성기는 `mk_anime6.py`(단일), `mk_anime_split.py`(좌우 2분할), `mk_anime_crack.py`·`mk_anime_crack2.py`·`mk_anime_crack3.py`·`mk_anime_crack4.py`(쪼개진 얼굴), 모두 백업 zip `bk/`에 있다.

### 47-1. 단일 이미지는 실패
- 한 장면 프롬프트(애니 스타일 단계 6종, 영어·한국어 강화)는 제미나이가 스타일을 하나로 맞춰 **얼굴이 완전 그림체, 금속도 그림**으로 나왔다. 이어 붙이는 수정 문장(첨부 후 편집)도 금속 질감이 안 살았다. 1~4번은 차이를 못 느꼈고 5~6번은 3~4번과 동일했다(사용자).
- 결론: 스타일을 한 이미지 안에서 섞으려면 **영역을 나누고 경계를 명시**해야 한다(기존 혼합 출력 장에서 확인된 원리와 같음).

### 47-2. 좌우 2분할 → 쪼개진 얼굴
- 좌우 2분할(얼굴 정중앙 직선, 목 아래까지)은 "새롭다"는 평가였으나 직선이 부자연스러워 **쪼개지는 느낌**으로 바꾸기로 함. 얼굴만 나누고 목 이하는 전부 실사.
- **쪼개진 얼굴 형식**(`mk_anime_crack.py`): HEAD(쪼개진 얼굴 사진 한 컷) → STYLE(전체가 실사 사진, 얼굴 일부만 유리 균열처럼 갈라져 그 안이 애니; 균열은 턱 끝에서 끝나고 목으로 이어지지 않음) → SUBJ(실사 쪽/애니 쪽 설명) → PIERCE(실사 쪽 금속은 실물, 애니 쪽은 그려진 것) + SAFE → FRAG(파편: 이마 쪽은 작고 촘촘, 뺨은 크고 성김, 턱에서 사라짐; 깨지는 모서리와 그림자는 사진, 그려진 조각은 잉크선 없는 찢긴 단면) → LIGHT.
- 1차 3종(무쇠 추·Y2K 에나멜 12·금 17): 1·2번은 실사/애니 구분이 한 번에 됨, 3번은 쪼개지는 부분이 애니 쪽으로 약간 넘어감. 3개 모두 쪼개진 느낌 좋음.

### 47-3. 확장 시험과 보정 (피어싱 많음 · 진한 메이크업 · 러시안 립)
- 확장 3종(`LumineX_FaceCrack_Heavy_3.md`): 금 피어싱 갑옷 약 100개 / 비주얼계 블랙립 5단계(극한) / 러시안 립 극한. 문제: 애니 쪽 귀·귀걸이가 가끔 실사, 코·입술이 한쪽(주로 실사)으로 치우침, 러시안 립은 실사로만 나옴(입술을 실사 쪽에 온전히 둔 설계 탓).
- v2(`mk_anime_crack3.py`): 균열을 **얼굴 정중앙(코 뿌리·코끝·입술 가운데·턱 가운데)** 으로 옮기고, 애니 쪽의 귀·고리·스터드·바·사슬·추는 전부 셀 음영 그림이라고 명시, FRAG의 "애니 쪽에 금속만 실사 예외" 문구 삭제. 결과: 귀 3/3 애니, 입술 반반 1·2번, 코는 매번 달라짐, 2번 귀걸이만 실사(무쇠 추 설명의 `blackened cast iron` 같은 사진 재질 단어가 당김), 3번 입술은 실사만.
- v3(`mk_anime_crack4.py`): **코 전체를 애니 쪽에 두는** 경로(코의 실사 쪽 바깥 옆을 따라 내려오다 입술 정중앙에서 합류), 추 재질 단어 교체(`blackened cast iron`→`dark iron`), 러시안 립은 애니 쪽 입술을 `flat glossy cel-shaded pink with painted white highlights and crisp outlines, just as tall and plump as the real half`로 명시하고 `made real` 삭제. 길이 874·807·912단어(v1과 동급, 늘리지 않음). **결과(사용자): 귀와 귀걸이 3/3 애니, 입술 반반 3/3(러시안 립 포함), 코는 2번만 거의 반반, 1·3번은 실사 쪽으로 약간 치우침.**

### 47-4. 교훈
- 작은 중앙 부위(코)는 "정중앙을 지나라"로는 위치가 안 맞고 매번 달라진다. 큰 부위(입술, 귀)는 영역 지시를 따른다. 코를 더 맞추려면 설명을 늘려야 하는데 길이 방침과 맞지 않아 **현재 수준에서 확정**.
- 재질 단어(`cast iron`, `real metal`)가 영역 지시를 이길 수 있다 — 그려져야 하는 쪽 사물에서는 사진 재질 단어를 제자리 교체한다(문장 추가 없이).
- 극단 볼륨 입술(러시안 립)은 한 덩어리로 보고 스타일을 통일하려 하지만, 애니 쪽 입술을 셀 음영·윤곽선·같은 볼륨으로 명시하면 반반이 된다.

### 47-5. 열린 과제
- 쪼개진 얼굴 형식의 프리셋화(카테고리·개수·축: 피어싱 테마 3종 수수/화려/귀여움 × 애니 눈 종류 × 헤어 색 × 메이크업 단계)는 **미결정**. 코 쏠림은 감수하고 틀을 확정하는 방향(사용자 판단 대기).
- 이전부터 열린 것: 혼합 연령·실버폭스 Face Sculpt 번들(새 카테고리, 연령 4단계 축, 문장 추가 없이), 듀오·트리오(·4·5인) 번들(귀 추 문단 단축 선행; 듀오 약 2,100·트리오 약 2,600단어), 바비·브랫츠 동종 그룹 번들(샘플 승인 후), 입술 주름 문장 `lips with real vertical texture`(길이 때문에 미적용), 강남언니 광택 단어, 엄니·코 별도 시리즈, 표정 축, Piercing Frame v2, 티어(HOF/SSS), `.bak` 5개 복구 여부.

## 48. Face Sculpt 확장 — 혼합 연령 · 실버폭스 · 그룹 · 동종 그룹 (v6.53, 2026-10-13 저녁)

> 이 장은 46장(Face Sculpt v2)과 47장(애니 피어싱 트랙) 이후 같은 날 이어서 등록한 번들 4종의 기록이다. 판정은 제미나이 기준·사용자 정상/이상 번호 보고 방식이다.

### 48-1. 등록 현황 (모두 push 완료, 앱 카테고리 표시는 확인 대기)
| 카테고리 | 키 | 개수 | commit | 비고 |
|---|---|---|---|---|
| Face Sculpt Formula (v2 덮어쓰기) | `la_facesculpt_NNN` | 300 | `baa1e553` | 메타 재등록 불필요 |
| Face Sculpt Mixed-Age Formula | `la_facesculpt_mix_NNN` | 300 | `f9f93286` | 신규 카테고리, 메타 등록 |
| Face Sculpt Silverfox Formula | `la_facesculpt_sf_NNN` | 300 | `f9f93286` | 신규 카테고리, 메타 등록 |
| Face Sculpt Group Formula | `la_facesculpt_grp_NNN` | 140 | `dd97de06` | 2인 60 · 3인 40 · 4인 25 · 5인 15 |
| Face Sculpt Same-Type Group Formula | `la_facesculpt_same_NNN` | 162 | `684502d0` | 신규 카테고리, 메타 등록 |
- 신규 프리셋 합계 +902(300+300+140+162). 전체 합계는 `(Get-ChildItem presets\la_*.json).Count`로 재확인할 것(이 장은 숫자를 추정하지 않음).
- 등록 절차는 모두 같았다: 번들 JSON + `patch_*_json.py`를 `preset_builders\`에 둔다 → `$env:PYTHONUTF8="1"` → 패치 스크립트 → (신규 카테고리면) `patch_livingartifact_2_meta.py`(categories added·keys added 확인) → 개수 확인 → `git add presets preset_builders core/presets_meta.py` → commit(attribution 줄) → push. 메타 스크립트가 만드는 `core/presets_meta.py.bak_livingartifact`는 커밋하지 않는다.
- 핸드오프 정리: 루트의 v5.2~v6.47 28개를 한 번에 삭제하고 v6.52만 남겼다(commit `29716118`). 이번에 v6.53을 추가하며 **v6.52는 지금은 지우지 않기로**(사용자: 나중에 지우자).

### 48-2. 혼합 연령 300 · 실버폭스 300 (생성기 `mk_fs_age.py`)
- 연령 4단계(아이돌 early 20s · 20대 후반 late 20s · 30대 후반 late 30s · 실버폭스 early 40s~early 50s + 은발)를 균등하게 랜덤. 나이 숫자와 머리색만 교체하고 문장은 더하지 않았다(`set_age`, `SILV`, 표정은 아이돌→아이돌 표정, 20대→20대, 30대·실버폭스→30대 표정 표를 쓰도록 `GRPFORCE` 훅으로 강제).
- **혼합 연령 300** = 눈 120 + 입술 120(연령 4단계 각 60) + 유형 60(바비·브랫츠·서큐버스·인어는 원래 나이·머리 유지, 라벨 "유형(원래 나이)").
- **실버폭스 300** = 눈 150 + 입술 150, 전원 실버폭스. **유형 60개는 넣지 않았다**(원래 나이·머리가 정체성이라 실버폭스와 맞지 않음, 그 몫을 눈·입술에 +30씩). 입술 종류 개수는 비례 확대(`scale`).
- 실수와 수정: 피부 단어 교체(`airbrushed→natural`)를 사실감 문장 B1 **뒤**에 돌렸더니 `never airbrushed`가 `never natural`로 깨졌다 → 교체를 B1 **앞**에 두도록 순서 변경. 검증: B1 마지막 구절·`never natural` 0개·한글 0·연속 중복 0·실버폭스 은발 300/300·남은 옛 머리색 0.
- 길이: 혼합 평균 약 1,520, 실버폭스 약 1,530단어(v2와 동급).

### 48-3. 그룹 140 — 인물마다 다른 귀 장식 (생성기 `mk_group_v2.py`의 `group5`)
- **문제**: 2인 샘플에서 두 사람의 귀걸이가 같거나 같은 종류였다. 원인은 귀 스타일(철 추·혼합 금속 추·단일 금속 추·대형 귀걸이)과 구멍 수를 **장면 전체에 하나만** 뽑아 모두에게 적용한 것(대형 귀걸이 모드만 인물별로 다른 모양).
- **수정**: `pick_ears`가 인물마다 귀 모드를 서로 다르게 뽑는다(2~4인은 전원 다른 종류, 5인은 하나 겹칠 수 있음), 구멍 수 1·2·3(75:161:64)도 인물별, 단일 금속은 인물마다 금속이 다르며 철 모드와 같은 장면에 철 단일 금속을 같이 두지 않는다. 공통 "Ear weights" 문단은 금속·구멍 수에 관계없는 일반 문장으로 바꾸고(`All {W} weights hang from her iron rings in staggered columns`, 금속은 "인물 문단에 적힌 금속"), 금속은 인물 문단 끝에 한 문장(혼합: 여덟 금속 중 서로 다른 금속 / 단일: 해당 금속)으로 넣었다. 대형 귀걸이가 섞이면 "Earrings:" 문단을 따로 둔다. 인물 문단의 추 모양 나열은 삭제(`WT_RE`)하고 개수는 공통 문단에 한 번(`six`/`four`).
- **줄이기**(문장 추가 없음): 공통 문단의 반복 문장("크기가 줄지 않는다·몇 킬로 무게·한눈에 무겁다")을 한 줄로 압축(`BIG_RE`). 2·3인 약 −250~270단어.
- **실사 문구**: 일반 인물에 1인 번들과 같은 피부·사실감(잔털·주근깨·비대칭·`never airbrushed`·젖은 반사광, `CX` 교체), 유형 인물은 단어 교체(`SW`)만 — 유형에는 잔털 문장이 없다. 4·5인에도 같은 문구를 넣었다(이전 4·5인 샘플은 이 문장을 뺐었음).
- 구성: 2인 60 · 3인 40 · 4인 25 · 5인 15. 길이 2인 평균 약 1,950(1,575~2,246) · 3인 약 2,540(2,216~2,869) · 4인 약 3,150(2,757~3,428) · 5인 약 3,710(3,268~3,945). 정면 127 · 45도 13(입술 주인공이 든 4인의 약 절반). 2~4인 125개 전부 귀 종류가 서로 다름.
- 사용자 평가: 2~5인 샘플 4개 **모두 1차 성공**, 귀걸이는 인물마다 다양하게 생성. 4·5인으로 갈수록 피부 실사감이 약해지지만 "어쩔 수 없다", 주근깨 같은 요소가 있으면 더 실사 같다. 2·3인은 잔털이 거의 안 보인다(프롬프트에는 있으나 한 장면에 여럿이 들어가 얼굴이 작아 미세 질감이 약해짐) → 지금 수준으로 등록, 필요하면 나중에 새 프리셋으로 조정(후보: `faint peach-fuzz hairs`→`visible peach-fuzz hairs catching the light on her cheeks and upper lip`, 약 +8단어/인).
- **5인 초과**: 인물당 약 +500~600단어, 얼굴이 더 작아져 피어싱·주인공 특징·피부가 약해질 것으로 보고 이번에는 제외. 6·7인 시험 1개씩은 사용자가 원할 때.

### 48-4. 동종 그룹 162 (생성기 `mk_same_bundle.py`, 시험 `mk_same_v2/v3/v4.py`)
- 한 장면에 같은 유형·같은 주인공 부위끼리 모은 번들. 인물 간 구분은 머리 색·줄무늬/렌즈 색·강도 단계·메이크업·피어싱 테마·귀 장식으로 만든다.
- 구성(개수): 바비만 2·3인 16 · 브랫츠만 2~5인 22 · 서큐버스만 22 · 인어 세이렌만 22 · 눈 주인공 자매 18 · 입술 주인공 자매(러시안 립 제외 11종 중) 18 · 러시안 립 자매(6단계 중) 14 · 유형 섞기 15 · 유형+부위 섞기 15. 인원별 2인 49 · 3인 49 · 4인 41 · 5인 23.
- 제약: 바비는 머리 색이 3종(금발·갈색·핑크)뿐이라 3인까지만. 브랫츠는 줄무늬 색과 렌즈 색이 인물마다 겹치지 않게. 서큐버스는 머리색 팔레트가 4종이라 5인은 한 색만 겹침 허용, 인어는 5종. 메이크업은 그룹 안에서 서로 다르게(없음 최대 1명, 유형은 제외). 피어싱 테마는 3종 중 3명 이상일 때 최소 3가지. 눈/입술 자매는 서로 다른 항목만. 입술 자매는 45도, 나머지는 정면. 귀 장식은 인물마다 다른 종류(2~4인 139개 전부).
- 길이: 2인 평균 약 1,780 · 3인 약 2,300 · 4인 약 2,790 · 5인 약 3,270, 최대 4,096단어(눈 자매 5인 부류).
- 사용자 평가: 서큐버스만 4인 · 인어만 4인 · 러시안 립 자매 4인 **모두 정상 성공**(러시안 립은 지난번 얼굴 컷에서 실사로만 나오던 문제와 달리 입술 자매에서는 문제없음), 같은 주인공 부위끼리·섞기 샘플 4개(눈 자매 4인 · 입술 자매 4인 · 유형 섞기 4인 · 유형+부위 5인) **모두 정상 성공**. 바비만 2·3인 / 브랫츠만 4·5인 샘플은 별도 번호 보고 없이 다음 단계로 진행(통과로 취급).
- 교훈: 동종 그룹에서도 "인물 간 차이"를 만드는 변수가 팔레트에 충분히 있는지 먼저 센다(바비 머리 3종, 서큐버스 머리 4종). 부족하면 인원 상한이나 허용 중복을 정한다.

### 48-5. 보류·열린 과제
- **쪼개진 얼굴 애니 피어싱 프리셋화**: 사용자가 보류("나중에 하자"). 틀은 47장에서 확정, 개수·축(피어싱 테마 3종 × 애니 눈 × 헤어 색 × 메이크업 단계)은 미정.
- 6·7인 얼굴 컷 시험(원할 때), 유형 인물에 잔털·주근깨 문장 추가 여부, 입술 주름 문장 `lips with real vertical texture`, 다인 잔털 강조 문구(위 후보), 4·5인 피부 실사감 개선.
- 앱에서 Face Sculpt 카테고리 4종(Mixed-Age · Silverfox · Group · Same-Type) 표시 확인.
- 레포 루트의 옛 핸드오프(v6.52 이하) 삭제는 나중에, `.bak` 5개 복구 여부, 티어(HOF/SSS), 엄니·코 별도 시리즈, 표정 축, Piercing Frame v2, 연령 축 4단계의 다른 카테고리 확대.

### 48-6. 생성기·파일 (백업 `LumineX_generators_backup_2026-10-13.zip` 안의 `bk/`)
- `mk_fs_age.py`(혼합 연령·실버폭스), `mk_group_v2.py`(`group5`·`pick_ears`·`real2`·`shorten`·`sample`), `mk_group_short.py`, `mk_group_v2_samples.py`, `mk_group_bundle.py`(그룹 140), `mk_same_v2.py`/`mk_same_v3.py`/`mk_same_v4.py`(동종 시험), `mk_same_bundle.py`(동종 162), 쪼개진 얼굴 `mk_anime_crack3.py`·`mk_anime_crack4.py`.
- 번들·패치: `la_facesculpt_mix_300_bundle.json`·`la_facesculpt_sf_300_bundle.json`·`patch_la_facesculpt_age_1_json.py`, `la_facesculpt_grp_140_bundle.json`·`patch_la_facesculpt_grp_1_json.py`, `la_facesculpt_same_162_bundle.json`·`patch_la_facesculpt_same_1_json.py`.
- 시험 파일: `LumineX_FaceSculpt_DuoTrio_Short_4.md`, `LumineX_FaceSculpt_Group_EarMix_4.md`, `LumineX_SameType_Group_2to5_4.md`, `LumineX_SameType_Group_Succubus_Mermaid_Ru_3.md`, `LumineX_SameStar_Mixed_4.md`, `LumineX_FaceCrack_Fix_3.md`, `LumineX_FaceCrack_Fix_v3_3.md`.

## 49. 신규 영역 3종 — 인형 관절 · 오토마톤 · 먹는 재질 (v6.54, 2026-10-13 밤)

> 48장 이후 같은 날 밤에 시작한 완전 새 영역 3개의 기록이다. 사용자가 "핸드오프에 없는 완전 새로운 것"을 요청해 후보 6개(먹는 재질 · 인형 관절 · 오토마톤 · 종이 공예 · 미니어처 · 프로젝션 매핑)를 제시했고(핸드오프 검색으로 미중복 확인, '이중 노출'은 36장에서 불채택 기록이 있어 제외), 인형 관절 → 오토마톤·미니어처 → 먹는 재질 순으로 시험했다. 반쪽 얼굴 재질 변환은 사용자 말로 이전에 해 본 적이 있어 제외했다.

### 49-1. 등록 현황 (push 완료)
| 영역 | 카테고리 | 키 | 개수 | 단어 수 | commit |
|---|---|---|---|---|---|
| 오토마톤 | 🏺 Living Artifact · Automaton Formula | `la_automaton_001~060` | 60 | 736~800 | `2be1773c` |
| 먹는 재질 | 🏺 Living Artifact · Edible Formula | `la_edible_001~060` | 60 | 587~682 | `2be1773c` |
| 인형 관절 | 🏺 Living Artifact · Doll Joint Formula | `la_dolljoint_001~060` | 60 | 623~707 | `2be1773c` |
- 접두어는 사용자 제안으로 `la_auto_`가 아니라 **`la_automaton_`**(auto는 자동차와 혼동). 다른 접두어와 충돌 없음(레포 사본 검색 0건).
- 등록 절차(이전과 동일): 번들 JSON 3개 + `patch_la_newthree_1_json.py`를 `preset_builders\`에 → `$env:PYTHONUTF8="1"` → 패치(180개) → `patch_livingartifact_2_meta.py`(결과: `categories added=3, keys added=180`, `.bak_livingartifact` 생성은 커밋 제외) → 개수 확인 → `git add presets preset_builders core/presets_meta.py` → commit(attribution 줄) → push. 등록 후 실측 합계 **14090**(등록 전은 계산상 13,910).
- 핸드오프: v6.53(commit `e6144259`)을 추가하며 **옛 버전은 지우지 않았다**. 이번 v6.54도 추가만 한다. 옛 버전 삭제는 사용자가 나중에 하자고 함.

### 49-2. 인형 관절 (BJD·마리오네트·마네킹·분라쿠)
- **6종**: 도자기 BJD · 레진 BJD · 마리오네트(줄이 프레임 위로 올라감) · 목각 마네킹 · 킨츠기 BJD(금 이음선) · 분라쿠 인형. 몸은 인형 몸 + 둥근 볼 조인트(목·어깨·팔꿈치·손목·엉덩이·무릎·발목), 얼굴·귀는 실사 살.
- **1차 결과**: 마리오네트(3)·분라쿠(6)가 가장 인형 관절 같고, 도자기(1)·레진(2)·마네킹(4)은 자세히 봐야 관절이 보이고, 킨츠기(5)는 그냥 몸 같음. → **관절에 대비색을 줘야 한다**(분라쿠의 주홍 관절이 모범).
- **2차**: 검정 관절(도자기)·흑칠 관절(킨츠기)은 어두운 틈 그림자와 섞여 안 보임, 와인레드(레진)·월넛브라운(마네킹)은 잘 보임 → **관절색은 중간 밝기의 선명한 색**(코발트블루·에메랄드그린 등)으로. 3차(코발트·에메랄드): "확실히 좋네, 다 채택".
- **마리오네트**도 관절을 별도 색(청록)으로 — 사용자 요청. 이전 홀로 샘플은 황동 핀만 있었다.
- **그룹(듀오·트리오) 시험은 통과 못 함**: 듀오에서 레진 하체가 종종 실사, 목재 짝은 관절이 몸과 같은 색(내 구성 실수: 짝 재질에 관절색 문구가 없었음), 트리오 4건 중 옥(2)·도자기(2) 인물의 팔·다리가 실사로. **트리오는 보류, 듀오는 인형끼리만 재시험**. 레진 BJD의 크림핑크 몸이 피부색과 비슷해 팔다리가 살색으로 돌아간다고 보고 **민트그린**으로 교체(와인레드 관절 유지)했으나 **듀오 재시험 결과는 사용자가 피로로 확인하지 못함**(미확정). 번들 레진 변형은 민트·라일락·버터옐로(피부색 계열 제외).
- 번들 변형(종류당 3~4): 도자기 BJD(흰+코발트 / 파우더블루+코랄 / 라벤더+금), 레진 BJD(민트+와인레드 / 라일락+금 / 버터옐로+틸), 마리오네트(벚나무+청록 / 월넛+아쿠아 / 흰 자작+주홍 / 흑단+금), 마네킹(자작+월넛 / 메이플+크림슨 / 회색+오렌지), 킨츠기(상아+에메랄드 / 청자+주홍 / 하늘색+보라), 분라쿠(주홍 / 인디고 / 초록 관절).

### 49-3. 오토마톤 (태엽·기계 인형)
- **6종**: 황동 · 도자기(금 기어) · 흑칠(은 기어) · 로즈골드 · 강철+구리 기어 · 터키석 에나멜. 앞 3종은 1차, 뒤 3종은 확장 요청("3종 더")으로 추가, 6종 모두 채택.
- **조정 이력**: ① 작은 베어링이 많으면 "무늬"처럼 보임 → 창 하나를 크게(가슴·배에 걸친 몸통 너비의 둥근 창), 베어링은 중심에 큼직하게. ② 태엽은 처음 작게 → 팔뚝 길이로(거대 태엽은 시험 후 기어 쪽으로 방향 전환). ③ 기어는 "거대 2개"보다 **빽빽한 큰·중·작 기어 + 코일 스프링 + 강철 축**이 좋음. ④ 창 안을 **깊고 속이 빈 공간, 층층이 다른 깊이, 속은 어둡지 않게 안쪽에서 부드럽게 빛남, 층 사이는 옅은 금빛**으로 → 사용자: "안 쪽이 밝으니 진짜 오토마톤 같다". ⑤ 관절은 몸과 대비색.
- **배꼽 문제**: 3번(흑칠) 샘플에서 배꼽이 맨살로 나옴. 원인은 공통 주얼리 풀의 `a gold belly chain with a small pendant at her navel`(배꼽 피어싱으로 읽힘). → 새 번들은 `a small pendant resting on her belly plate`로 치환(`ns2["jewel"]` 훅). **이미 등록된 프리셋(Material Mix 등)에 같은 문장이 있을 가능성이 높다 — 확인·일괄 교체는 미정**(가짜 확신 금지: 이번 시험에서는 오토마톤 1건만 확인).
- 번들 변형(종류당 3): 황동(녹청/로열블루/크림슨 관절), 도자기(구리빛 붉은/코발트/모란+에메랄드), 흑칠계(흑칠+금 / 미드나이트블루+금 / 버건디+은 관절), 로즈골드(에메랄드/사파이어/보라), 건메탈(금/터키석/스칼렛), 터키석계(터키석+코랄 / 스칼렛+아이보리 / 에메랄드+아이보리 관절).

### 49-4. 먹는 재질 (초콜릿·꿀·사탕·젤리·아이스크림·케이크)
- **1차 실패**: 6종 모두 "일반 딱딱한 재질처럼" 생성. 원인은 석재·옥용 공통 틀의 딱딱한 문구(`solid …`, `divided into dozens of fitted … sections, each joint standing in a thin raised ridge`, `nothing lying flat`, `completely opaque`)가 부드러운 재질을 단단한 조각으로 만든 것. 꿀이 흘러내리지 않은 것도 같은 이유.
- **수정(기존 구절 교체, 문장 추가 없음)**: 딱딱한 구조 문구를 재질별로 교체 — 초콜릿(녹아 리본처럼 흘러내려 발 앞에 고임) · 벌집 꿀(칸에서 긴 줄기로 흘러내림) · 젤리(몸을 통과한 빛, 속의 과일 조각) · 아이스크림(녹는 덩어리·흘러내림) · 케이크(짜 올린 크림이 입체로 솟고 스펀지 단면). 반투명 재질(꿀·사탕·젤리)은 `completely opaque`를 `richly saturated in colour`로. 패턴 풀도 `sections` 언급 없는 표면형 문구로 교체.
- **결과(2차)**: 초콜릿 흘러내림 · 꿀 떨어짐 · 젤리 빛 비침 · 아이스크림 녹아 흘러내림 · 케이크 입체 크림과 스펀지 단면 — 의도대로. **캔디**는 딱딱한 사탕은 흘러내리지 않아 "일반 재질"로 보여 **녹은 사탕**(시럽이 끈적하게 늘어지며 흘러내림)으로 교체, "사탕 흘러 내림" 확인.
- 번들 변형: 초콜릿(다크/밀크/화이트), 벌집 꿀(황금/짙은 호박색/연한 레몬골드), 녹은 사탕(빨강/분홍/청록/오렌지), 젤리(라즈베리/라임/오렌지/포도), 아이스크림(딸기 바닐라/민트 초코칩/블루베리 바닐라), 케이크(분홍/민트 버터크림/화이트 웨딩/초콜릿 가나슈).

### 49-5. 미니어처 (스노우볼·오르골·테라리움) — 확인 전
- 작은 그녀(10~12cm)가 유리 용기 안에 선 접사 사진. 몸은 검증된 재질(청동·호박·산호), 구도만 접사로(`LumineX_Miniature_Sample_3.md`: 스노우볼+청동 / 오르골+호박 / 테라리움+산호). 힐은 상대 높이(숫자 없음). **사용자 확인 결과 없음** — 번들화 보류.

### 49-6. 번들 생성기 (`mk_new_bundles.py`, 백업 zip 안 `bk/`)
- Material Mix 틀 그대로(체형 BIG5 = 부피 큰 5종, 인종 10, 나이·포즈·헤어·네일·주얼리·배경 70곳·힐은 55% 40인치/45% 상대 높이, 얼굴·귀는 실사 살+메이크업만)에 재질 문장만 교체. 종류 × 변형 표를 `DOLLS`/`AUTOS`/`EDIBLES`에 두고 종류당 10개를 라운드로빈(10번 반복 × 6종 = 60개, 변형 3~4를 순환).
- 검증: 중복 프롬프트 0, 한글·연속 중복 단어·`navel`·`pierc` 0, 배경 38~42곳, 인종 10, 체형 5. (문구 검사의 `ridge` 22건은 `nose bridge`의 부분 문자열 오탐.)
- **결정 대기**: 체형이 5종으로 제한된 Material Mix 틀을 그대로 상속했다. "모든 축 전체 랜덤" 원칙과 다르므로 PH0 전체 목록으로 넓힐지 사용자에게 물었으나 답이 없어 그대로 등록했다. 넓히려면 새 번들로.
- 시험 파일(참고): `LumineX_DollJoint_Sample_6/v2_4/v3_2`, `LumineX_DollJoint_Duo_3/v2_3`, `LumineX_DollJoint_ResinSolo_1`, `LumineX_DollJoint_ResinDuo_3`, `LumineX_DollJoint_Group_4`, `LumineX_Edible_Solo_6/v2_6`, `LumineX_Edible_CandyMelt_1`, `LumineX_Automaton_Sample_3/v2_3`, `LumineX_Automaton_BigKey_1/BigGear_1/ComplexGear_1/ComplexGear_2/Depth_3/Bright_3/Bright_v2_3/Final_3/New3`, `LumineX_Miniature_Sample_3`.

### 49-7. 이번에 얻은 규칙
1. 인형·기계 재질은 **관절/부품을 몸과 대비되는 중간 밝기의 선명한 색**으로. 검정·아주 어두운 색은 그림자에 묻힌다.
2. **몸 색이 피부색과 비슷하면**(크림핑크 등) 그룹에서 팔다리가 실사로 돌아간다. 비피부색(민트·라일락·파우더블루 등)으로.
3. 부드러운 재질(먹는 재질)에 석재용 **딱딱한 구조 문구를 쓰지 말고** 재질별 문구(흘러내림·녹음·비침)로 교체.
4. 작고 많은 장식은 "무늬"로 읽힌다. **크게, 두세 곳**이 낫다. 속 빈 공간은 안쪽에서 밝게.
5. 주얼리 풀의 **'배꼽' 표현은 맨살 배꼽**을 만든다.
6. 그룹(특히 트리오)은 사람 수가 늘수록 몸 처리가 약해진다 — 인형은 솔로 먼저, 듀오는 인형끼리만.
7. 사용자가 시험 확인에 지칠 때는 개수를 줄이고 한 번에 한두 파일만. 대비색·문구 조정은 같은 시드로 다시 뽑아 비교.

### 49-8. 열린 과제
- 인형 듀오(마리오네트 청록, 레진 민트그린)·미니어처 3개 확인 → 통과 시 `la_dolljoint_duo_` / `la_miniature_` 번들. 인형 트리오는 보류.
- 등록된 프리셋의 **배꼽 펜던트 문장 일괄 교체**(대상: `a small pendant at her navel`를 포함한 `presets\la_*.json`; 먼저 개수부터 확인).
- 체형 전체 목록으로 넓힌 번들 여부.
- 종이 공예·프로젝션 매핑(후보 중 미시험), 앱에서 새 카테고리 7종 표시 확인(Face Sculpt 4 + 이번 3), 옛 핸드오프 삭제(나중), 48-5의 보류 항목(쪼개진 얼굴 애니 피어싱, 6·7인 얼굴 시험 등), `.bak` 복구 여부.

---

## 50. 인형 듀오 등록 · 미니어처 불채택 (v6.55, 2026-10-14 새벽)

> 49장 이후 이어진 정리 작업이다. 49-8의 열린 과제 중 인형 듀오와 미니어처를 닫았다.

### 50-1. 결정
- **미니어처(스노우볼·오르골·테라리움)**: 사용자 판단 "별로" → **불채택, 번들 만들지 않음**. (49-5 참고, `la_miniature_` 접두어는 쓰지 않는다.)
- **인형 듀오**: 사용자 "인형듀오는 등록하면 되고" → 등록. 단, 지난 시험에서 확인하지 못한 **레진 민트그린·마리오네트 청록 조합의 듀오 결과는 미확인 상태로 등록**했다(인형끼리만 짝지어 실사 몸·같은 색 관절 문제를 피하도록 구성).
- **인형 트리오**: 시험 4건 중 옥·도자기 인물의 팔다리가 실사로 나와 **계속 보류**.
- 사용자는 "배꼽 펜던트는 인형에서 교체했잖아?"라고 짚었다 — 맞다. 새 번들(오토마톤·먹는 재질·인형 관절·듀오)은 모두 `a small pendant resting on her belly plate`로 치환되어 있다. 문제는 **그 이전에 등록된 프리셋**뿐이다.

### 50-2. 등록 현황 (push 완료)
| 영역 | 카테고리 | 키 | 개수 | 단어 수 | commit |
|---|---|---|---|---|---|
| 인형 관절 듀오 | 🏺 Living Artifact · Doll Joint Formula (기존) | `la_dolljoint_duo_001~030` | 30 | 1135~1291 (평균 1198) | `bd071c75` |
- 결과: 패치 후 메타 등록 `categories added=0, keys added=30`, 개수 **14090 → 14120**, push `e7661e20..bd071c75`.
- 구성: 인형 종류 15쌍(6종 조합) × 2회, 시드 20261110으로 섞음. 종류별 변형은 `CUR_VAR[("#1","doll")]` / `("#2","doll")`로 사람마다 다른 색을 줌. 힐은 40인치 모드 고정(그룹 규칙). 배경 26곳·프롬프트 30개 모두 고유. 메타 필드: `format:"dolljoint_duo"`, `group_size:2`.
- 두 인형 모두 몸 재질 문장 끝에 "같은 재질의 소품·조각상이 없다"는 문구를 붙여 소품이 같은 재질로 나오는 것을 막았다.
- 생성기: `mk_dolljoint_duo.py`(→ `la_dolljoint_duo_30_bundle.json` + `patch_la_dolljoint_duo_1_json.py`). `mk_doll3.py`의 인형 변형과 `mk_new_bundles.py`의 인형 구간(`HEAD`·`DJ`·`doll()`·`BJDacc()`·`DOLLS`)을 재사용한다. 백업 zip(`LumineX_generators_backup_2026-10-13.zip`)에는 이 파일까지 포함되어 있다.

### 50-3. 합계
- 14,120 = 14,090(49장 시점) + 30. 카테고리는 새로 늘지 않았다.

### 50-4. 열린 과제 (49-8 갱신)
- 인형 듀오 실제 생성 품질은 샘플 외 **미검증**(민트 레진·청록 마리오네트 조합). 문제 보고가 오면 변형 색부터 조정.
- 인형 트리오: 보류.
- 등록된 프리셋의 **배꼽 펜던트 문장 일괄 교체**: 대상 `a small pendant at her navel`를 포함한 `presets\la_*.json`. 먼저 개수부터 확인(미실행).
- 체형 전체 목록으로 넓힌 번들 여부(답 없음, 등록분은 BIG5 5종).
- 종이 공예·프로젝션 매핑 등 미시험 후보, 앱에서 새 카테고리 7종 표시 확인, 옛 핸드오프 삭제(나중), 48-5의 보류 항목, `.bak` 복구 여부.

---

## 51. 성운·용암·블록 등록 · 제목 규칙 점검 · 젖은 광택(Wet Look) 번들 (v6.56, 2026-10-14)

> 50장 이후 이어진 작업이다. (1) 새 영역 탐색 결과와 3종 등록, (2) 접두어 정리와 제목 규칙 누락 발견, (3) 젖은 광택 시험 전 과정과 번들 작성. 사용자 표현으로 시험 결과는 모두 "N번 1회 성공"처럼 번호별로만 받았다.

### 51-1. 새 영역 탐색 → 등록 3종, 제외 3종
| 영역 | 결과 | 비고 |
|---|---|---|
| 우주·성운 (nebula/galaxy) | **채택·등록** | 성운 3 + 은하 3 변형을 순환 |
| 용암·마그마 (basalt/obsidian) | **채택·등록** | 현무암 3 + 흑요석 3 변형 |
| 블록 조립 (multi/mono) | **채택·등록** | 원색·파스텔·네온 3 + 단색 4(터키석·빨강·검정·핫핑크) |
| 털실·펠트 공예 | 제외 | 사용자 "제외" (사유 미기록) |
| 수묵·서예 | 제외 | 사용자 "제외" (사유 미기록) |
| 라텍스·비닐 풍선 | 제외 | 사용자 "제외" (사유 미기록) |
| 미니어처 | 제외 | 50장에서 이미 불채택 |
- 사용자 입력 원문: "1, 2번 우주·성운: 채택 / 3, 4번 용암·마그마: 채택 / 5, 6번 털실·펠트: 제외 / 7, 8번 수묵·서예: 제외 / 블록 조립: 선택 / 라텍스·비닐 풍선: 제외".
- 등록: 카테고리 `🏺 Living Artifact · Nebula Formula` / `Lava Formula` / `Brick Formula`, 키 `la_nebula_001~060`·`la_lava_001~060`·`la_brick_001~060`. 결과 `categories added=3, keys added=180`, 개수 **14120 → 14300**, push `bd071c75..cdcd3aab`. 패치 `patch_la_newthree2_1_json.py`, 생성기 `mk_new3b.py`(→ `la_{nebula,lava,brick}_60_bundle.json`, 시드 20261121/22/23). 템플릿 `T_NEB`·`T_LAVA`는 `mk_new4.py`, 블록 템플릿 `BT`는 `mk_block.py`.
- **이 180개의 제목은 옛 긴 형식**이다(51-3 참고).

### 51-2. 접두어 표 (산출물)
- `LumineX_Preset_Prefix_Map_2026-10-14.md`(카테고리·한글 설명·접두어·개수, LA 총 14,300 + 레거시 576), `LumineX_LA_Prefix_KoEn_2026-10-14.md`(LA 카테고리 93종, 접두어순 영문/한글 이름·개수).
- 정정: Five-Material Patchwork의 접두어는 `la_`가 아니라 **`la_5mat_`**. 수정본이 두 파일에 반영되어 있다. Shoe Mix `la_sm_`는 등록된 적 없음.

### 51-3. 제목 규칙 적용 누락 (진단 완료, 교체는 보류)
- 규칙(44-5·44-6장): `시리즈 인원 #번호 · 체형 · 재질 · (솔로만 포즈) · 배경 · 메이크업`, 약 74자, 메이크업 꼬리표(강함·강화·포인트·N단계) 제거, 공통 함수 `master/retitle.py`.
- 누락 대상: 오토마톤·먹는 재질·인형 관절 180, 인형 듀오 30, 성운·용암·블록 180 = **390개**(평균 111~194자). Face Sculpt 5종 **1,202개**(평균 155자)는 얼굴 컷용 틀이 없었다. CJK Face는 규칙 이전 등록이라 제외.
- 사용자 결정: **1(새 번들 390) + 2(Face Sculpt 1,202) 모두 초안 그대로 진행**. 회사라서 못 하고, 집에서 **"집이야"** 하면 `LumineX_Retitle_Plan_2026-10-14.md`를 다시 보여준 뒤 `patch_la_retitle_3.py`(390)·`patch_la_retitle_4.py`(Face Sculpt)를 만든다(제목만 교체, `--dry`, 옛 제목 백업 JSON, 재실행 0개 변경). 프롬프트·키·카테고리는 안 건드리므로 메타 재등록은 불필요(실행 후 확인).
- **Wet Look(51-4 이후)은 처음부터 이 규칙으로 제목을 만들었으므로 교체 대상이 아니다.**

### 51-4. 젖은 광택(Wet Look) — 개념과 템플릿
- 사용자 요청: 의상 없는 이미지에서 더 섹시한 새 영역. 젖은 광택은 의상이 아니라 **몸에 액체 코팅이 입혀진 것**(의상 없음 확인 질문에 답함).
- 템플릿 `T_WET`(`mk_wet10.py`): `LEAD`("body curving to follow her body's true three-dimensional shape, ") + `a continuous glossy wet-look coating over her entire body, thick sheets and streams of liquid running down every curve in glistening rivulets, countless beads and droplets clinging to the surface and dripping from her chin, fingertips, hips and knees, razor-sharp bright specular highlights along every curve, nothing lying flat. Dense wet surface — {base}, {acc}, {fin}, completely opaque, NO airbrush NO gradient wash, NO flat printed surface anywhere`. 앞머리는 기존 `HEAD`(`solid="wet-look"`).
- 변형 정의: `V(tag, desc, solid, nmw, T, base, acc, fin)`(**mk_wet 계열의 V는 dict를 돌려준다** — `mk_doll3` 계열의 8-튜플 V와 다르다. 섞어 쓰면 언패킹 오류).
- `base` = 색 문장 + `, {how}`(예: `BLAZING deep jet-black pigment across the full torso both legs neck to ankle, soaked by pouring rain`), `acc` = 액체 묘사(VIVID …), `fin` = 마감(`mirror-wet glossy` / `dewy glossy` / `creamy glossy` / `sticky glossy`), `nmw` = `glistening wet {색}`(신발·네일 재질).

### 51-5. 시험 이력과 결과 (정리)
| 시험 | 내용 | 결과 |
|---|---|---|
| Sample3 | 브론즈 오일·크림슨 샤워·블랙 빗속(보통 체형) | 3개 모두 1회 성공 |
| Big3 / Muscle3 | 부피 큰 체형 / 근육 체형 | Big3: 1번만 실패 · Muscle3: 1번 3회, 2번 2회, 3번 1회. "약간 바디슈트 느낌" 지적 |
| Muscle v2 | 문구를 "wet liquid pigment poured over her bare skin…"으로 교체 | 3번만 1회, 1번 4회 → **개선 없음, 불채택** |
| BlackRain3 · Dark3 | 어두운 색(블랙·미드나이트 블루·딥 에메랄드·버건디) × 빗속·샤워·오일 | **모두 1회 성공** |
| Test9 | 밝은 색 3 · 중간 색 3 · 새 액체 3 | 밝은 색 1~3·코발트 1회, 바이올렛·틸 및 새 액체(풀사이드·물 튀김·파도 물보라)는 1회 실패 |
| Test9_mk(립색 메이크업 맞춤) | 같은 9개에 메이크업 맞춤 | 8/9 1회(1번만 2회). 단, 축을 다시 뽑은 비교라 확정적이진 않음 |
| Liquids5 | 샴페인·안개이슬·얼음 녹은 물·우유·꿀(스타일 메이크업) | 5개 모두 1회 성공(사용자 입력 "1, 2, 3, 4. 5"를 5개로 읽음) |
| NewMakeup8 | 신규 메이크업 8종 | 1~6·8 1회, **7(한복 화보) 2회** |
| Paint3 | 젖은 광택 × 이레즈미·UV네온·전통 공예 타일(솔로) | 이레즈미·UV 3회, 공예 타일 2회 → **패턴 솔로는 불채택** |
| PaintGroup4 | 사람마다 다른 패턴을 입은 젖은 그룹 2~5인 | 정상(사용자 입력 "1, 2, 3, 4, 5" — 파일은 4개, 시도 횟수 미확인) → 번들에는 **넣지 않음** |
| SolidGroup8 | 단색끼리 2~5인 4개 + 일반 바디페인팅과 혼합 4개 | 1~4·6~8 1회, **5(혼합 듀오: 젖은 브론즈+일반 이레즈미) 생성 실패** |
| WetHair4 | 머리만 젖음 2 + 머리·얼굴 젖음 2 | 모두 정상 성공 |
| Mode4 | 3모드 랜덤 혼합 듀오 2·단색 트리오·혼합 4인 | 1·3·4 1회, **2(일반 UV네온 + 젖은 크림슨) 실패** → UV네온은 비·젖음과 안 맞는다는 사용자 판단으로 **혼합에서 제외** |
| Duo2b | 젖은 + 일반 바디페인팅 / 젖은 + **석영(로즈쿼츠)** | 2개 모두 1회 성공 |
| MatMix3 | 젖은 사람 + 옥·도자기 / 청동·옻칠·호박 / 산호·목재·석재 | 1·3 1회, 2번(4인) 3회 |
| Duo3_BLA | 2번의 청동·옻칠·호박을 하나씩 젖은 사람과 듀오로 | 3개 모두 1회 → **4인 구성이 원인, 8재질 모두 채택** |
- 반증된 가설: "밝은 색이라 불안정", "부피가 커서 불안정" — 시험으로 모두 기각. 어두운 색 + 다양한 액체는 안정적이다.

### 51-6. 확정 규칙 (번들 반영)
- **색 7종**(1회 성공 이력): 블랙(`jet-black`), 미드나이트 블루, 딥 에메랄드, 버건디, 코발트, 크림슨, 브론즈. 바이올렛·틸은 제외.
- **액체 11종**: 기본 3(빗속 `soaked by pouring rain`, 샤워 `soaked under a running shower`, 오일 `drenched in thick clear body oil`)은 7색 전부, 나머지 8(풀사이드·물 튀김·파도 물보라·샴페인·안개·이슬·얼음 녹은 물·우유·꿀)은 **어두운 5색**(블랙·미드나이트·에메랄드·버건디·코발트)만.
- **배경 호환**: 빗속=실외+겨울 제외+날씨 흐린 낮/비 갠 뒤(시험에선 날씨를 안 좁혔으나 비와 맞지 않아 추가), 풀사이드=옥상 테라스·야외 테라스·여름 해변·하얀 안뜰, 물 튀김=실외, 파도 물보라=해안 4곳, 안개·이슬=숲길·대나무 숲·정글 보드워크·폭포 전망대·라벤더 들판·봄 정원 테라스, 얼음 녹은 물=겨울 눈 광장·설원·얼음 동굴. 나머지는 70곳 전체.
- **머리·얼굴 3모드**(젖은 인물마다 1/3씩): ① 머리+얼굴 젖음 — 헤어 끝에 `, soaking wet, slicked and clinging in wet strands`, 얼굴의 `a soft sheen of natural oils`를 `water droplets beading across her skin and a wet glistening sheen`으로 교체 ② 머리만 젖음 ③ 안 젖음(원래대로). 사용자 질문 "머리랑 얼굴은 안 젖어?"에서 출발 — 원래는 얼굴·머리가 의도적으로 몸 재질 밖이었다.
- **체형**: 임산부를 뺀 `D.BODIES` **22종**을 전부 랜덤. 극단 체형(USSBBW·hourglass SSBBW)은 B 변형(`B_INS`, 솔로에만 가장자리 문구)+솔로 앉은 자세 70%. ※ 시험은 일부 체형(BIG5·근육·SSBBW)만 했고 22종 전체는 미검증.
- **힐**: 솔로 40인치 55%·상대 45%, **그룹은 항상 40인치**(기존 Material Mix 그룹 규칙. 처음에 그룹도 두 모드로 뽑았다가 `forty inches` 개수 불일치로 고침).

### 51-7. 메이크업 풀
- 메이크업 사전은 **두 갈래**: `pick_makeup`(`gen_cjk_v2`, STYLES 29: 스타일 17 + 립색·블랙립 12) / 글래스페이스 사전(`glassface/gen.py` `add(...)` 37종, 히메갸루·오네에갸루·로리타 갸루·야미카와·데코라·웨이쉰·한복 화보·브리티시 모드·지역 글램류 등).
- 글래스페이스 사전은 한 항목에 메이크업+헤어+표정+피어싱이 섞여 있어 **메이크업만 잘라**(`mk_newmakeup.py` `NEW_MK`) 풀에 추가: 히메갸루·오네에갸루·로리타 갸루·야미카와·데코라·웨이쉰·한복 화보·브리티시 모드. 추가로 **피부색 단어(fair·pale·porcelain)를 모두 제거**했고(어두운 피부 인종과 충돌해 `face()` 필터가 거름), "doll"→"large round eyes", 스티커→"그린 별·하트"로 교체, 렌즈 문구 삭제.
- `face()` 필터(woodstone 계열): `BANNED`(blood·doll·rot·crack …), `lens`·`sticker` 포함, 얼굴 페인트 4종(마이코·경극·둔황·혼례), 태닝(코갸루 일부 단계·만바·야마바·반바), PALE 단어+어두운 피부를 거른다. **실제 나오는 스타일 15종**: 강남언니·인스타글램·구풍·홍콩풍·글래스 스킨·걸크러시·아게하·코갸루(일부)·히메갸루·오네에갸루·로리타 갸루·야미카와·데코라·웨이쉰·브리티시 모드. 아마갸루·지뢰계는 렌즈 문구 때문에 항상 걸러진다.
- **한복 화보는 2회 성공이라 풀에서 제외**. 지역 이름이 붙은 글램류(하베샤·요루바·노르딕 발키리·슬라브·락혼·파케앙트·텔레노벨라 등)는 인종 연결 장치가 필요해 **2단계로 보류**.
- 사용자: "흑인에 히메갸루 메이크업이 조금 웃겨. 뭐 변주로선.." → 인종별 제외 없이 **변주로 랜덤 유지**.

### 51-8. 그룹 구성 (혼합 규칙)
- 틀: `gen_matmix_bundle.py`의 `build3`(Material Mix 그룹), 인물 훅은 `person_nv` 래핑(`mk_wet13` 이후): 키 `wetpaint`(젖은 인물, `MODEMAP`으로 모드 전달), `crystalp`(석영).
- **단색 그룹**: 한 장면은 같은 액체(빗속·샤워·오일), 사람마다 다른 색.
- **혼합 그룹**: 액체는 **오일만**(비·샤워면 마른 인물이 어색). 젖은 인물 1~(n−1)명 + 마른 파트너. 파트너 풀 11: 일반 이레즈미·일반 바디페인팅(공예)·석영(로즈쿼츠·스모키쿼츠)·옥·도자기·청동·옻칠·호박·산호·목재·석재. **UV네온은 제외**. 금박·스테인드글라스는 Material Mix 틀에 없어 이번엔 못 넣음. ※ 석영은 로즈쿼츠만 시험했고 스모키쿼츠는 같은 템플릿으로 추가(미검증).
- 파트너가 청동이면 젖은 색에서 브론즈를 뺀다.

### 51-9. Wet Look Formula 240 번들 (작성 완료, 등록 대기)
- 파일: `la_wet_240_bundle.json`(240개, 약 2.2MB), `patch_la_wet_1_json.py`, 생성기 `mk_wet_bundle.py`(의존: `mk_wet12` 계열 헤더 체인, `mk_wet10.py`의 VD, `mk_wet7.py`의 P3, `mk_newmakeup.py`, `master/gen_extreme.py`, `master/retitle.py`). 시드 20261210.
- 카테고리 `🏺 Living Artifact · Wet Look Formula`, 키 `la_wet_{solo/duo/trio/quartet/quintet}_NNN`.
- 구성: 솔로 120(기본 액체 3종 각 20 + 나머지 8종 각 7~8) / 듀오 40 / 트리오 40 / 쿼르텟 20 / 퀸텟 20. 그룹은 단색:혼합 = 1:1(듀오·트리오 20:20, 4인·5인 10:10, 번갈아 배치).
- 제목: `Wet 솔로 #001 · latina curves · 꿀 블랙 · 머리 넘기기 · 바닷가 산책로 · 홍콩풍`. 그룹은 체형 `A / B` 또는 `A 외 N`, 재질 `오일 크림슨+딥 에메랄드 + 호박 붉은 호박`. 길이 49~99자, 평균 73자. 메이크업 꼬리표 없음.
- 검수 결과(이상 0건): 한글 섞임·중복 단어·배꼽 문구·주얼리 개수·`forty inches` 개수·젖은 인물 수·머리/얼굴 모드 개수·렌즈/스티커/피어싱 문구·프롬프트/키 중복·빗속 날씨. 단어 수: 솔로 636~910, 듀오 1191~1492, 트리오 1654~2122, 4인 2250~2662, 5인 2591~3131. 체형 22종·인종 10종·배경 66곳·모드 각 135회 등장.
- **등록 절차(사용자가 "등록하자"라고 하면 안내)**: 두 파일을 `preset_builders\`에 둔 뒤 `$env:PYTHONUTF8="1"` → `python preset_builders\patch_la_wet_1_json.py` → `python preset_builders\patch_livingartifact_2_meta.py`(새 카테고리 1개) → `(Get-ChildItem presets\la_*.json).Count`(예상 **14540** = 14300 + 240) → `git add presets preset_builders core/presets_meta.py` → 커밋(attribution 줄) → push. `.bak_livingartifact`는 커밋하지 않는다.
- 백업 zip(`LumineX_generators_backup_2026-10-13.zip`)에 `mk_wet.py`~`mk_wet19.py`, `mk_wet_bundle.py`, `mk_newmakeup.py` 추가됨.

### 51-10. 교훈 (스크립트 작업용)
- `face()` 필터가 메이크업 문장을 조용히 거른다 — 새 메이크업을 넣을 때 스타일별로 몇 번 통과하는지 먼저 센다(단일 스타일만 허용하면 "fail face"로 종료).
- 한글이 프롬프트에 섞이는 원인은 `desc`에 한글 액체명을 넣은 경우였다(영문 `LIQE` 사용).
- 그룹 힐은 항상 40인치 모드로 고정.
- 사용자의 시험 입력은 가끔 번호가 파일 개수보다 많거나 끊겨 오므로, 어떻게 읽었는지 답에 적어 둔다.

### 51-11. 열린 과제
- **Wet Look 240 등록**("등록하자" 대기), **제목 교체 390 + 1,202**("집이야" 대기) — 둘을 한 번에 이어서 안내하기로 했다.
- Wet Look 미검증: 22개 체형 전체, 극단 체형 그룹, 스모키쿼츠, 파트너가 함께 젖는 변형("일반 바디페인팅·산호도 비를 맞게" — 사용자 질문, 시험 안 함), 지역 글램류(인종 연결), 금박·스테인드글라스 파트너.
- 보류: 인형 트리오, 체형을 BIG5 너머로 넓힌 번들(Wet Look은 22종으로 넓혔다), 오래된 프리셋의 배꼽 펜던트 문구 일괄 교체(개수부터), A-track 후보(크롬·홀로그램, 라인스톤, 파우더·스플래시, 프로젝션 매핑), B-track 의상(라텍스·새틴 쿠튀르, 시어·메쉬, 드레스, 갑옷), 앱에서 새 카테고리 표시 확인(성운·용암·블록 + Wet Look), 옛 핸드오프 삭제(나중), `.bak` 복구 여부.

## 52. 새 영역 4종 채택·제외 · 새 영역 400 번들 · 등록 (v6.57, 2026-10-14)

> 51장 이후 이어진 작업. 시험 결과는 모두 번호별 "정상/이상·N회 성공"으로만 받았다.

### 52-1. 새 영역 결정
| 영역 | 결과 | 비고 |
|---|---|---|
| 크롬(chrome) | **채택** | 은색·로즈골드 등. 부피 큰 체형 솔로·듀오 정상 |
| 라인스톤(rhinestone) | **채택(문구 교체)** | 처음 "의상처럼 보임" → 듬성듬성 붙인 느낌 → 문구 `thousands of tiny faceted rhinestone crystals packed tightly together directly onto her skin with no skin showing between them, stones overlapping at random angles in thick layers …`로 확정("이 정도면 괜찮아") |
| 프로젝션 매핑(projection) | **채택** | 솔로·듀오 정상 |
| 스플래시(splash) | **채택** | 파우더와 함께 시험, 문구 `thick wet paint splashed and splattered over her entire body in overlapping layers until no skin shows, a continuous glossy coat of vivid paint over every curve` 로 정상 |
| 홀로그램 | 제외 | 솔로도 의상처럼 나오고 듀오 실패 |
| 파우더 | 제외 | 문구를 고쳐 재시험했으나 생성 안 됨 |
- 사용자 원문: "홀로그램만 제외하자 / 파우더는 안되니 제외, 스플래스는 잘 생성되니 채택."

### 52-2. 주얼리 논의 결과
- 문제: 바디페인팅류에서 목, 배꼽 주위 복부가 주얼리 때문에 종종 맨살로 나옴. 사용자: "특히 라인스톤이 그런데 라인스톤도 정상 생성. 다른 건 배꼽 피어싱 외엔 괜찮을 듯하기도 해. 완전 없애긴 아쉽네."
- 확정 규칙 `jewel_fam(p)`: **라인스톤 인물**은 팔다리 풀 `JW_LIMB`(뱅글·암밴드·허벅지 체인·손가락 반지), **그 외 인물**은 `JW_NONAVEL`(9종 목록에서 **배꼽 체인 제외**). 그룹은 인물마다 적용. 전신 프롬프트의 피어싱 없음·얼굴 렌즈 없음은 그대로.
- 샘플 파일: `LumineX_Jewelry_Limb4.md`.

### 52-3. 새 영역 400 번들(`la_area4_400_bundle.json`)
- 패치 `patch_la_area4_1_json.py`, 생성기 `mk_area4_bundle.py`(시드 20261401). 헤더 체인: mk_holo1 ← mk_area8 ← mk_new_bundles ← mk_doll3 ← gen_matmix_bundle. 변형 정의는 `AV()`/`XV()` dict, 인물 종류 `areap`(`CUR_VAR[(label,"areap")]`).
- 구성: Chrome·Rhinestone·Projection·Splash 각 **솔로 60 + 듀오 30**(360) + 4요소 믹스(Mix4) **트리오 14·쿼르텟 13·퀸텟 13**(40) = **400**.
- 카테고리 5개: `🏺 Living Artifact · Chrome Formula` / `Rhinestone Formula` / `Projection Formula` / `Splash Formula` / `Four-Element Mix Formula`. 키 접두어 `la_chrome_`·`la_rhine_`·`la_proj_`·`la_splash_`·`la_a4mix_`(예 `la_chrome_solo_001`, `la_a4mix_trio_001`).
- 변형: 크롬 7(은 가중 0.5·로즈골드·골드·구리·건메탈·블랙·코발트), 라인스톤 8(오로라·핫핑크·젯블랙·다이아몬드·골드·루비·에메랄드·로열블루), 프로젝션 7(사이버 그리드·만화경·물결 반사광·은하·불꽃·오로라 리본·모자이크), 스플래시 7.
- 체형 22종(임산부 제외) 전부 랜덤, 극단 체형(USSBBW·hourglass SSBBW)은 솔로 앉은 자세 70%, 배경 69~70곳(`BGL.pick`), 그룹 힐 항상 40인치·솔로 55%.
- 검수(이상 0건): 한글 혼입·중복 단어·`navel` 없음. 단어 수 솔로 617~885, 듀오 1155~1521, 5인 최대 3118.
- **미보고 시험**: `LumineX_Area4_NewColor_Check8.md`(크롬 블랙·건메탈, 라인스톤 다이아몬드·에메랄드, 프로젝션 은하·불꽃, 스플래시 레드블랙·라임퍼플 — 새 색 8개 솔로)는 사용자가 결과를 보고하지 않았다. 번들에는 이미 들어 있다.

### 52-4. 등록 이력
| 단계 | 내용 | 결과 |
|---|---|---|
| 1 | Wet Look 240 + 새 영역 400 등록(`patch_la_wet_1_json.py`, `patch_la_area4_1_json.py`, 메타 패치) | `categories added=6, keys added=640`, 개수 **14300 → 14940**, push `cdcd3aab..17f000c2` |
| 2 | 제목 교체: `patch_la_retitle_3.py`(390) + `patch_la_retitle_4.py`(Face Sculpt 1,202) | `--dry` 후 실행, 재실행 시 변경 0/0, push `17f000c2..8e196ef8` |
- 등록은 사용자가 "등록하자"를 말한 시점에 진행. 명령은 `Move-Item`이 이미 `preset_builders`에 있는 파일에서 실패했지만 무해했다.
- 제목 교체 도구는 `retitle_tools/`(common.py·r3.py·r4.py·test.py·assemble.py)와 `patch_la_retitle_3/4.py`. 자체 완결, 등록된 프리셋의 제목·프롬프트·메타를 읽어 제목만 교체, `--dry`·`--undo`·백업 JSON·재실행 안전.
- 이 시점 51-11의 열린 과제 중 **Wet Look 등록·제목 교체는 완료**.

## 53. 크롭(가슴·허리·힙·무릎컷) 시험 — 보류 (v6.57)

- 사용자 요청: 전신 위주이므로 가슴컷·허리컷·힙컷·무릎컷을 시험. 구성은 듀오(한 명은 단일 재질, 한 명은 혼합 재질; 체형은 일반 1 + 부피 큰 체형 1).
| 버전 | 결과 |
|---|---|
| v1 | 가슴컷인데 허벅지까지 / 허리컷이 무릎 위까지 / 힙컷이 무릎까지 / 무릎컷이 발목까지 |
| v2 | 가슴컷=힙 끝(가로) / 허리컷=허벅지 중간(가로) / 힙컷=무릎 위(세로) / 무릎컷=무릎 아래(세로) |
| v3 | 가슴컷=힙 중간 / 허리컷=힙 끝 / 힙컷 생성 실패 / 무릎컷=무릎 바로 위 |
| v4 | 가슴컷=힙 중간 / 허리컷=힙 중간 / 힙컷 생성 안 됨 |
- 결론: 제미나이는 요청보다 **1~2단계 아래까지** 그린다. 무릎컷은 "hip line"으로 요청하면 근접. **상체 컷(가슴·허리·힙)은 현재 틀(체형 설명량 큼, 힙 팝 포즈)로는 불가 → 보류.** 사용자: "이건 보류할까? 의상있는 쪽 한번 해볼까?"
- 시험 중 Gemini 사용량이 걸려 **Claude 챗**으로도 시험했고, 챗은 신발 높이를 거의 그대로 표현했다.
- 생성기: `mk_crop4.py`. 샘플: `Crop4_Duo_Single_Blend`(v1~v3), `Crop3_Duo_v4`.
- Material Blend(1인 몸에 여러 재질) + 새 영역 솔로/듀오/트리오 샘플(`PaintMix_New_Solo_Duo_Trio3`, `MatBlend_New4_Solo_Duo_Trio3`)은 "뭐 잘 생성돼. 이건 나중에 다시 등록하자" → **번들화·등록은 나중**(생성기 `glassface/mk_blendnew.py`, `mk_mixnew3.py`, `cores8.json`).

## 54. 의상(B-track) 시험 전 과정 (v6.57)

> 사용자가 의상 없는 쪽만 하다 의상 쪽을 보고 "확실히 심심하긴 하다"며 시작. 공통: 의상 사람 종류 `clothp`(의상 문구가 재질 문구 자리), 솔로는 `build3(["clothp"],[None],[phys],[age],[pose],eth,scene)`. 후처리로 `Pattern density MAXIMUM…` → `Extreme macro detail on the fabric texture, the skin and the shadows.`, `no props or statues made of the same material as her.` → `no props or statues.`. 전부 기본 랜덤.

### 54-1. 수영복·원피스 계열 (결과)
| 항목 | 결과 | 생성기 |
|---|---|---|
| 비키니 4종(하이웨이스트 코랄 레드·골드 스트링·크롬·젖은 블랙 홀터) | 솔로 4개 정상 | mk_bikini4 |
| 마이크로 비키니 3종(블랙·골드 메탈·레드 젖음) | 블랙·골드 성공, **레드 젖음 1차 실패·2차 성공**. 가슴 특화 체형으로 재시험 시 3개 모두 1차 성공 | mk_micro3, mk_microbust3 |
| 라텍스 캣슈트·시어 메시·컷아웃 | "좋아" | mk_cloth5 |
| 새틴 슬릿 드레스 | 컷아웃 쪽으로 흡수하면 됨 | mk_satin2 |
| 컷아웃 롱·미니·초미니 | 하면 될 듯(화이트·레드·블랙 계열) | mk_cutlen3 (결과 번호별 미보고) |
| 플런지(클리비지) 배꼽/골반까지 | 3개 성공, **배꼽 깊이까지만** 렌더 → 문구는 `belly button`(골반 요청도 배꼽까지) | mk_plunge2/3 |
| 슬릿 미니 5단계(블랙 레더, 밴도탑) | "1번이 생성됐으니 나머지는 괜찮을 듯" | mk_slit5 |
| 초미니 초하이 슬릿 + 상의 4색(블랙 레더·화이트 새틴·레드 라텍스·골드 시퀸) | 1·2·3 한 번에 성공(4번 골드 시퀸 미보고) | mk_umtop4 |
- 근육질 큰가슴(CUSTOM `muscular big bust`, `amazon big bust`) 허벅지 강조: 1·2번 1회 성공. 사용자: "여기에 성공한 상의를 랜덤으로 섞으면 될 듯." (`mk_musbust2b.py`)
- 체형 특화 시험(`BodySpecial6`, `BodySpecial8_ExtremeOutfit`, 극초미니·극초하이슬릿·플런지 골반까지 × 바스트/근육질/초 아워글래스/USSBBW) 및 `PlungeUltraMini2` 결과는 **번호별 미보고**.

### 54-2. 상체 가리개 정리(확정)
- BustTops4 피드백: ①코르셋 → 배까지 가려 별로 ②하네스 → 가슴 노출 적음 ③마이크로 비키니 스타일로 하면 괜찮을 듯 ④플런지 코르셋(레드 새틴) 좋음. BustTops3 재시험: ①코르셋 여전히 아래를 가림 ②마이크로 비키니 크기로 좋아짐 ③마이크로 비키니 탑이 탑. 코르셋 브라: ①3D 피규어 느낌 ②무난. 버스티에와 얇은 밴드 코르셋 브라는 불채택.
- **언더붑**(끈 나시/셔츠/플런지/티셔츠 변형 5가지 시험): 사용자가 원한 건 "티셔츠를 잘라서 유두 부근만 덮이는" 형태였으나 시험들은 비키니나 상반신 가림으로 나옴 → **보류**. UnderbustCami4의 1·3번(끈 나시)은 좋다고 했으나 정의하지 못함.
- **마이크로 플런지 코르셋 최종 정의**("이건 이 정도로 정의하자"): 마이크로 비키니 하의(`a minimal red satin micro bikini bottom of one tiny low-rise opaque triangle on thin side strings tied at the hips, the small opaque piece fully covering her`) + 상의 `a minimal red satin corset-style top reduced to two small opaque molded cups noticeably smaller than normal cups on thin straps, leaving more of the curve of her bust visible around them, short and ending just below her bust, with an extremely wide plunging V neckline that spreads as far apart as possible across her chest and runs down to the bottom of the corset, where its bottom tip stays closed and joined in a neat point right under her bust with no split or gap at the bottom, no boning or band below that point, the small opaque cups still fully covering what they cover, her whole stomach bare below it`. 거치며 확인: 코르셋 끝이 **터지면(split)** 이상하게 생성 → 끝은 닫고 최대한 벌어진 V로. 배꼽에서 벌어지게는 불채택. 컵은 작게(표현 케바케).
- 확정 상의(가슴 특화 체형 `legendary bust`·`curved bust`로 시험): ①플런지 코르셋(레드 새틴) ②미니멀 하네스 브라(블랙 레더, 실버 링) ③마이크로 비키니 탑(골드 시퀸 삼각 컵) ④발코네트 코르셋 브라(블랙 레더, 레이스업) ⑤초소형 밴도(손가락 2개 폭, 54-4). 삼각 유두만 탑은 54-3. `Bust3Tops_Solo`: 1~3번 1차 성공. 문구 원문은 mk_bust3tops.py.

### 54-3. 마이크로 비키니 크기 탐색(유두·유륜·원형·네모)
| 시험 | 결과 |
|---|---|
| 마이크로 비키니 "유두만 가리는" 표현 2개 시험 | 사용자 요청으로 시작, 이후 원형 컵 등으로 크기 탐색 (개별 결과 번호는 기록 없음) |
| 원형 컵(유두만) | 생성 실패. "유륜까지만"도 실패 |
| 유두/유륜 × 원형 + 미니스커트 | 일부 성공(1~2번) 후 `roundcup skirts4` **4개 전부 실패** → **원형 포기** |
| 삼각 컵 유두/유륜 × 하의 6종(`tricup bottoms6`) | 1(2회)·2(2회)·3(1회)·4(2회)·5(2회)·6(2회) 성공 |
| 네모 컵(`squarecup2`) | 1번 실패, 2번 1차 성공·2~3차 실패 → **네모 불채택** |
| 가슴 특화 체형 마이크로 비키니 3종(`microbikini bust3`) | **1·2·3 모두 1차 성공** |
| 삼각 유두만 탑(`micronippletop2`: 골드 시퀸·블랙 레더) | 1번 실패, **2번(블랙 레더) 1회 성공** |
| 유두만 3색(`NippleTop3Colors`: 레드·화이트·딥 퍼플 레더) | 레드 실패, **화이트·퍼플 1회 성공** |
| 최소화 문구 2개(`NippleTopMin2`: "smallest possible … exactly the size of her nipple") | 블랙 1회 성공, **화이트 실패** → 최소화 문구 불채택 |
- 결론: 유두만과 유륜만은 생성되는 크기가 **거의 같다**(최소 크기 하한이 있는 듯, 제미나이 한계로 추정 — 미확인). 작게 보이게 하는 최선책은 **문구가 아니라 가슴 큰 체형**(상대적으로 작아 보임). 유두만 삼각 탑은 **블랙·화이트·딥 퍼플 레더**만 채택(골드 시퀸·레드 레더 제외). 유두 크기 컵은 안정성이 낮아 일반 마이크로 비키니 비중을 크게 둔다.

### 54-4. 밴도(bandeau)·벨트·띠 류
- **밴도 확정**: `손가락 2개 폭`(narrowest possible strip only two fingers tall)이 안정적. 폭 3단계 시험에서 1(손가락 2개)·3번 성공, 중간 폭 2번은 2회 만에 성공 → **1번 확정**. 색 변형 2개 모두 성공. 부피 큰 체형 2·가슴 큰 체형 2·누비안 부티빌더·black glamour·브라질 부티글램 **7체형 모두 1회 성공**(체형-인종 연결 `D.BODY_LINK` 적용).
- **벨트**: 가슴 벨트 3종 시험에서 1번 실패, 2번은 밴도와 거의 같아 차별성 없음, **3번(진짜 벨트) 1회 성공**. 벨트 스커트(한 뼘)·마이크로 미니 하의와 조합: **마이크로 미니 수영복 하의는 케바케, 미니스커트는 안정적**.
- **띠 류 새 시험**: 새틴 리본 랩 1(2회 성공), 레이스 밴도 2(1회)·실크 스카프 3(1회)·튜브 4(별로). 레이스는 약간 시스루라 폭이 넓게 표현. 스카프 매듭을 **옆구리 또는 한쪽 가슴 옆**으로 바꿔 재시험 → 1번만 성공, 방향은 확정("매듭은 옆구리나 한쪽 가슴 옆쪽").
- **추가 재질**: 메탈 밴드(골드) 실패 / 넥타이 랩(레드 실크) 실패 / 진주 밴드(화이트) 실패 / **퍼 밴도(화이트) 1회 성공** / 크레이프 종이 밴도(레드) 1회 / **포장지 밴도**(넓게 펴졌지만 1회 성공). 크레이프 종이는 일반 밴도와 이미지가 비슷하고 더 넓어 **제외**. 확정 후보: 스카프 랩·퍼 밴도·포장지 밴도(전부 손가락 2개 폭 문구) + 일반 밴도 + 벨트.
- 규칙: 면이 양쪽에 걸쳐 이어진 불투명 띠(밴도·벨트·스카프·퍼)는 성공, **작은 개별 조각**(원형·네모 컵)과 **얇은 금속 띠·진주 줄·가는 넥타이·시스루 레이스**는 실패하거나 넓게 렌더. 손가락 폭 기준 문구가 폭을 통제하나, 무늬·질감 재질은 넓게 나온다.
- 생성기: mk_bust3tops → mk_bustband → mk_bandw3 → mk_bandretry → mk_bandcol2 → mk_band7 → mk_belt3/belt2/beltswim2 → mk_bandnew4 → mk_lacescarf2 → mk_scarfknot2 → mk_bandmat4 → mk_paper2.

## 55. 의상 번들 400 · 등록 (v6.57, 2026-10-14)

### 55-1. 파일·등록
- `la_cloth_400_bundle.json` + `patch_la_cloth_1_json.py`(AST OK), 생성기 `mk_cloth_bundle.py`(시드 20267001 변형 섞기·20267002 추출), 머리부는 `mk_musbust2b.py` 복사.
- 키 접두어: **`la_clothes_<패밀리>_solo_NNN`**(사용자 제안: 처음 `la_of_`에서 변경). 카테고리 6개: `🏺 Living Artifact · Bust Outfit Formula` / `Swimwear Formula` / `Latex & Mesh Formula` / `Gown Formula` / `Skirt Outfit Formula` / `Band & Belt Formula`.
- 등록: `categories added=6, keys added=400`, 개수 **14940 → 15340**, push `8e196ef8..96e66693`.
- 제목: `Bust 솔로 #001 · curved bust · 발코네트 코르셋 브라 블랙 레더 · 옆모습 · 인도 궁전 안뜰 · 구풍`(최대 92자, 대부분 80자 이내). 포즈는 `pose_ko`.

### 55-2. 구성(모두 솔로, 체형·나이·포즈·인종·배경·힐·네일·주얼리·메이크업 기본 랜덤)
| 패밀리 | 키 접두어 | 개수 | 내용 / 체형 / 배경 |
|---|---|---|---|
| Bust | `la_clothes_bust_` | 50 | 가슴 특화 체형 2종(legendary/curved bust) × 상의 5종(플런지 코르셋·하네스·마이크로 탑 골드 시퀸·발코네트·초소형 밴도) 각 10, 하의는 마이크로 비키니 |
| Bandeau | `la_clothes_bandeau_` | 30 | 손가락 2개 폭 밴도(블랙 레더·레드 새틴·화이트 레더) 각 10 × 22체형 |
| MicroBikini | `la_clothes_microbik_` | 30 | **일반 20**(블랙 7·골드 메탈 7·레드 젖음 6) + **유두만 10**(블랙 4·화이트 3·딥 퍼플 3 레더), **가슴 특화 체형만**; 일반은 시험한 배경 5곳(옥상 테라스·야외 테라스·여름 해변·하얀 안뜰·바닷가 산책로), 유두만은 전체 |
| Bikini | `la_clothes_bikini_` | 30 | 코랄 레드 8·골드 스트링 8·크롬 7·젖은 블랙 7 (배경 5곳) |
| Latex | `la_clothes_latex_` | 30 | 캣슈트 5색(크림슨·젯 블랙·화이트·코발트·딥 퍼플) 각 6 |
| Mesh | `la_clothes_mesh_` | 30 | 시어 메시 보디수트(블랙 8·화이트 8·딥 레드 7·네이비 7) |
| Cutout | `la_clothes_cutout_` | 40 | 컷아웃 롱(화/블/아이보리)·미니(레드/화이트/코발트)·초미니(블랙/레드/화이트) + 새틴 슬릿 드레스 |
| Plunge | `la_clothes_plunge_` | 30 | 배꼽까지 딥 플런지 롱 15·미니 15 |
| Slit | `la_clothes_slit_` | 30 | 슬릿 미니 5단계(블랙 레더·레드 라텍스·화이트 새틴) × 채택 상의 랜덤 |
| UltraMini | `la_clothes_umini_` | 30 | 초미니 초하이 슬릿 4색(블랙 레더·화이트 새틴·레드 라텍스·골드 시퀸) × 상의 랜덤 |
| MuscleBust | `la_clothes_musc_` | 20 | CUSTOM 근육질 큰가슴 10 + 아마존 큰가슴 10(허벅지 강조) × 상의 랜덤(버스티에·홀터 포함) |
| Belt | `la_clothes_belt_` | 30 | **블랙 레더만**: 벨트 세트 15 + 가슴 벨트 + 마이크로 미니스커트 15 |
| Band | `la_clothes_band_` | 20 | 실크 스카프 8(에메랄드·크림슨·아이보리·미드나이트, 매듭 옆구리/가슴 옆)·퍼 밴도 6·포장지 밴도 6 |
- 상의 풀(슬릿·초미니·근육질에서 랜덤): 밴도·크롭탑·하네스 브라·발코네트 브라·마이크로 탑·플런지 코르셋(+근육질은 버스티에·홀터).
- 검수: 키·프롬프트 400개 중복 없음, 한글·`foil/lens/sticker/doll`·`navel` 없음, 체형 24종(22+CUSTOM 2), 인종은 `BODY_LINK` 적용, 단어 수 451~780(평균 약 580), `forty inches`·`Jewelry:` 개수 일치.

### 55-3. 사용자 결정 이력(번들 확정까지)
- 접두어: "la_clothes_microbik~ 이렇게 하면 어때?" → `la_clothes_` 채택.
- "마이크로 비키니 상의는 우리가 정리한 대로 넣은거지?" → 일반 3종 문구는 시험 원문 그대로, 가슴 특화 체형 한정은 Bust 패밀리만이었음을 알림 → 사용자: "그거 유두 크기의 비키니 아니었어?" → 유두만 변형 추가 결정("난 이걸로 하고 싶은데") → "**일반 20개 유두 10개로 정리**".
- Belt: 샘플 `Belt 솔로 #001 · legendary bust · 벨트 세트 레드 레더`가 **생성 실패** → 레드 레더(유두만 시험에서도 실패)와 미시험 화이트 벨트를 빼고 **블랙 레더만** 남김. 나머지 샘플 12개 패밀리는 문제 보고 없음.

### 55-4. 미검증 변형(번들에 들어 있음, 필요 시 샘플 점검)
- 라텍스 딥 퍼플·화이트·코발트(크림슨만 시험), 메시 딥 레드·네이비, 컷아웃 코발트·아이보리, 플런지 아이보리·블랙 미니, 슬릿 단계×레드 라텍스·화이트 새틴, 스카프 크림슨·아이보리·미드나이트 블루, 퍼 밴도 블랙·핑크(화이트만 시험), 포장지 실버 + 파란 리본, 벨트 세트 블랙의 배색.
- 체형 22종 전체 검증은 없음(시험은 일부 체형 중심). 근육질·아마존 허벅지 강조는 상의 풀 일부(버스티에·홀터)가 `musbust2b` 시험분.

### 55-5. 교훈
- 번들 생성기 본문에서 **한 글자 전역 이름(D, G 등)을 리스트로 덮어쓰지 말 것** — exec로 이어 붙인 머리부가 모듈 `D`(BODY_LINK)·`G`(메이크업 `gen_cjk_v2`)를 전역으로 쓴다. 패밀리 리스트는 `F_A`처럼 접두어를 붙인다(이번에 `AttributeError: 'list' object has no attribute 'pick_makeup'`/`BODY_LINK`로 발생).
- 제목에 상의 이름만 쓰고 색은 치마 색과 같으므로 생략하면 길이가 74~80자로 줄어든다.
- 시험 결과가 "N회 성공"으로 오면 **1차 성공만 채택**하는 원칙을 유지한다(2회 성공이던 한복 화보는 풀에서 제외했던 것과 같은 기준). 레드 젖음 마이크로 비키니처럼 처음 2회 성공이던 문구는 가슴 특화 체형으로 재시험해 1차 성공을 확인한 뒤 채택했다.

### 55-6. 열린 과제 (v6.57 기준)
- **Material Blend + 새 영역 번들**(생성·등록 대기, "이건 나중에 다시 등록하자").
- 미보고 시험 결과: NewColor_Check8, CutoutLen3, PlungeUltraMini2, BodySpecial6/8, UltraMiniTop4 #4, MicroBottom4 일부. 새틴 리본 랩은 보류, 퍼 밴도 색 변형·다른 미시험 색(55-4)은 샘플 확인 필요.
- 보류: 크롭 시리즈(53장), 언더붑(54-2), 젖은 마이크로 비키니, 인형 트리오, 지역 글램 메이크업 인종 연결, 옛 프리셋 배꼽 펜던트 문구 일괄 교체, 22체형 전체/극단 체형 그룹 검증, 앱에서 새 카테고리 표시 확인, **오래된 핸드오프 삭제는 나중**(지금은 삭제하지 말 것).
- 백업: `LumineX_generators_backup_2026-10-14.zip`(529개 파일)에 이번 구간의 `mk_*` 생성기 56개(밴도·벨트·의상·마이크로 비키니·플런지·언더붑·크롭·`mk_cloth_bundle.py` 등), `retitle_tools/`, `patch_la_wet_1_json.py`·`patch_la_area4_1_json.py`·`patch_la_cloth_1_json.py`·`patch_la_retitle_3/4.py`, README 추가분 포함. 사용법: `export PYTHONPATH=master`.
- 등록 현황: 합계 **15,340**(LA) + 레거시 576. 마지막 push `96e66693`.

## 56. 성인 코스튬 · 그룹 번들 · 팔 포즈 제외 (v6.58, 2026-10-14 밤)

> 55장 이후 이어진 작업. 시험 결과는 번호별 "정상/N회 성공"으로만 받았다. 사용자가 말한 "샘플"은 문맥에 따라 다른 파일을 가리켜서 두 번 되물었다(56-9).

### 56-1. 코스튬 틀과 문구
- 사용자 요청: "코스튬(성인)을 최대한 노출 의상으로 표현해봐 / 바스트 체형 위주로" → 이후 "다른 체형도 섞어봐, 섹시한 체형 위주로".
- 틀: 의상 번들과 같은 `clothp`(의상 문구가 재질 문구 자리, 신발·네일은 `nmw`). 문구 구조는 **작은 불투명 컵 + 마이크로 미니스커트(또는 하이컷 하의) + 소품**, 끝문장 `fully opaque and covering only what it must, her stomach bare`. 닌자·바니걸은 하의 구조가 다르다(생성기 파일에 원문).
- 후처리는 의상 번들과 동일(55장). 생성기: `mk_costume5.py`(5종 원본), `mk_costume9.py`(9종), `mk_costume6new.py`, `mk_costume2dt.py`, `mk_costume8more.py`, 문구 모음 `cost_pool.json`(번들용 28종).

### 56-2. 시험 이력과 결과
| 시험 | 내용 | 결과 |
|---|---|---|
| Costume5 | 바니걸·메이드·간호사·경찰관·산타(가슴 특화 체형) | **5개 모두 1차 성공** |
| Costume9 | 악마(super hourglass)·천사(Brazilian booty glam)·마녀(legendary bust)·해적(hourglass bombshell)·카우걸(latina curves)·레이싱 퀸(curved bust)·치어리더(Nubian booty builder)·닌자(super glamour)·여전사(black glamour) | **닌자만 실패**, 나머지 8 성공 |
| Costume3_Big | 바니걸 BBW bombshell · 간호사 hourglass SSBBW · 악마 USSBBW | 모두 1차 성공 |
| Costume2_Muscle | 여전사 amazoness · 경찰관 powerlifter bombshell | 모두 1차 성공 |
| Costume2_DocTeacher | 의사(legendary bust)·선생(curved bust, 성인 교사) | "프롬프트가 괜찮았다" → 채택 |
| Costume6_New | 승무원(legendary bust)·인어(super hourglass)·벨리 댄서(Brazilian booty glam)·여왕(hourglass bombshell)·복서(heavy muscle)·소방관(curved bust) | **모두 한 번에 성공** |
| Costume8_More | 닌자 재시험 A·B, 이집트 여왕(black glamour), 뱀파이어(curved bust), 요정(curvy petite), 군인(amazon bombshell), 훌라(Polynesian goddess), 서퍼(latina curves) | **8개 모두 정상** |
| Bandeau2F_Bust2 | 손가락 2개 폭 밴도(블랙 레더·레드 새틴, 가슴 특화) | 별도 보고 없음(전체 "모두 성공" 보고에 포함으로 간주, 개별 확인 안 함) |
- 닌자 원 문구는 `얼굴 마스크를 목에 내림 + 팔 가드` 때문으로 추정(미확인). 재시험 A(마스크·팔 가드 없음, 머리띠+허리 sash)와 B(손가락 2개 폭 밴도 띠 + 마이크로 미니) 모두 성공. **번들에는 A만 닌자로 사용**.
- 유두만 가리는 마이크로 비키니(55장)의 색 시험 결과와 최소화 문구 실패도 이 구간의 작업이다(54-3에 기록).
- 의사·선생·밴도 요청 등 사용자 문구: "선생, 의사는 밴도 말고 위에 프롬프트가 괜찮았어. 뭐 사실 랜덤이지 뭐, 그치?" — 한 번의 시험은 확률이라는 점을 인정하고, 패밀리 단위 일관성(5/5, 8/9)으로 판단하기로 함.

### 56-3. 코스튬 28종과 체형 그룹 매핑
- **채택 28종**: 바니걸·메이드·간호사·경찰관·산타·악마·천사·마녀·해적·카우걸·레이싱 퀸·치어리더·닌자·여전사·승무원·인어·벨리 댄서·여왕·복서·소방관·의사·선생·이집트 여왕·뱀파이어·요정·군인·훌라·서퍼. (대화 중 "29종"이라 했던 것은 오기, 정확히 28종.)
- 사용자 제안: "전사 쪽은 근육질 몸매, 의사·간호사·학교 선생 같은 느낌은 바스트 체형, 그다음 아워글래스·블랙글래머·브라질 부티 글램 같이 힙·허리가 강조되는 체형, 부피 큰 체형."
- 번들 매핑: **근육질**(amazoness·powerlifter bombshell·heavy muscle·muscular hourglass BBW·amazon bombshell·powerlifter) = 여전사·경찰관·해적·레이싱 퀸·닌자·복서·군인 / **바스트**(legendary bust·curved bust) = 간호사·의사·선생·메이드·마녀·승무원·소방관·뱀파이어 / **허리·힙**(super hourglass·hourglass bombshell·glamour hourglass·black glamour·Brazilian booty glam·latina curves·Nubian booty builder·super glamour·Polynesian goddess) = 바니걸·악마·천사·카우걸·치어리더·산타·인어·벨리 댄서·여왕·이집트 여왕·요정·서퍼, 훌라는 Polynesian goddess 고정 / **부피 큰**(BBW bombshell·hourglass SSBBW·USSBBW) 15%.
- 코스튬마다 **주 체형 그룹 60% / 부피 큰 체형 15% / 나머지 25%** 확률. 실측 부피 큰 체형 비율 17.1%.
- 사용자: "코스튬마다 체형을 지정하긴 했는데, 확실히 얇은 체형은 좀 밋밋한 것 같아." → 제안대로 **curvy petite·wide hip narrow를 코스튬·의상 그룹 번들에서 제외**(사용자 이의 없이 진행, 명시적 확인은 없음). 요정의 주 체형은 petite에서 허리·힙 계열로 변경. 얇은 체형을 소량 남길지는 미결정.

### 56-4. 팔 포즈 제외 확정과 교체 패치
- 사용자: "가슴 가리는 팔은 하지 말자." → 후보 중 **팔짱(`arms crossed under her bust`)과 얼굴 감싸기(`both hands framing the face`) 둘 다 제외**("둘다"). 기본 포즈 14종에서 12종이 남는다.
- 등록된 의상 400개 중 영향: 팔짱 31 + 얼굴 감싸기 28 = **59개**. 처음엔 패치 적용을 보류했다가("1은 안하기로 했잖아?" 질문에 기록 부재를 알림) 사용자가 "변경하자"로 결정.
- `patch_la_pose_1.py`: 대상 `presets/la_clothes_*.json`, 프롬프트 `Pose: … —` 문장·제목의 포즈 표기·meta.poses만 교체. 새 포즈는 키 md5로 7종(서 있기·걷기·양팔 들기·머리 넘기기·옆모습·기대기·손 허리) 중 고정, `--dry`/`--undo`(`pose_swap_backup.json`), 재실행 0개. 샌드박스 확인: 교체 59, 재실행 0, 복구 59.
- 앞으로 모든 샘플·번들에서 두 포즈 제외(메모리에도 반영됨). 코스튬·의상 그룹 시험은 포즈를 뺀 버전으로 다시 만들었다.

### 56-5. 극단 체형(USSBBW·hourglass SSBBW) 포즈
- 사용자 질문 "극단 체형을 왜 앉은 자세로 한거지?" → 41장 확정 규칙의 이유(큰 몸이 서면 한 프레임에 작아지고 윤곽이 뭉개짐, 앉으면 퍼지고 접힘이 보여 더 커 보임)를 설명하고 코스튬 번들만 비율을 낮출지 물음.
- 사용자: "극단 체형을 서 있는 포즈로 해보자" → 시험 4개(`ExtremeStanding4`: USSBBW 바니걸·hourglass SSBBW 여왕·USSBBW 라텍스 캣슈트·hourglass SSBBW 컷아웃 롱, `mk_extstand4.py`) → 결과 보고 전에 사용자: **"그냥 원래대로 하자."** → **솔로 앉은 자세 70% 규칙 유지**, 서 있는 포즈 시험 결과는 미보고.
- 번들 실측: 극단 체형 솔로 17개 중 앉은 자세 12개(70.6%).

### 56-6. 그룹 시험(2~5인)
- 사용자가 지적: "아니 코스튬 말고 위에 한거." — 이미 등록한 **의상 400개(솔로)** 가 2~5인 그룹으로 섞인 적이 없어 등록 전에 시험이 필요하다는 뜻. (등록된 의상 400개는 모두 솔로였다.)
- 의상 그룹 시험(`mk_clothgroup4.py`, 사람마다 다른 패밀리, 22체형 랜덤)과 코스튬 그룹 시험(`mk_costumegroup4.py`): **2·3·4·5인 모두 정상**("5인까지 잘 생성됨", "코스튬 샘플 2~5인도 정상 생성"). 가슴 특화로만 시험한 Bust·MicroBikini·MuscleBust 패밀리는 그룹 풀에서 제외(체형 조건이 다름).
- 그룹은 힐 40인치 고정, 사람별 라벨 `#1…`을 `CUR_VAR[(f"#{i}","clothp")]`로 전달(solo는 label None).

### 56-7. 코스튬·의상 그룹 번들 310 (등록 완료)
- 파일: `la_costume_310_bundle.json` + `patch_la_costume_1_json.py`, 생성기 `mk_costume_bundle.py`(시드 20267501, `mk_cloth_bundle.py`의 FAM을 exec해서 의상 풀 사용).
- 구성: **코스튬 솔로 140**(28종×5, 키 `la_costume_solo_001~140`) + **코스튬 그룹 75**(듀오 25·트리오 20·쿼르텟 15·퀸텟 15, `la_costume_{duo,trio,quartet,quintet}_NNN`) = 215 → 카테고리 `🏺 Living Artifact · Costume Formula`; **의상 그룹 95**(듀오 30·트리오 25·쿼르텟 20·퀸텟 20, `la_clothes_{duo,trio,quartet,quintet}_NNN`) → 카테고리 `🏺 Living Artifact · Outfit Group Formula`.
- 사람마다 다른 코스튬/의상(의상 그룹은 서로 다른 패밀리), 체형은 서로 다름, 얇은 체형 0, 팔 포즈 제외, 극단 체형 솔로 앉은 자세 70%, 인종은 `BODY_LINK` 적용, 솔로 힐 40인치 55%, 그룹 40인치.
- 제목: 코스튬 `Costume 솔로 #001 · super hourglass · 악마 · 손 허리 · 중국 정원 · 오네에갸루`, 그룹 `Costume 듀오 #011 · BBW bombshell / USSBBW · 마녀 / 간호사 · 하얀 안뜰 · 홍콩풍 / 로리타 갸루`, 의상 그룹은 길이를 줄이려고 **패밀리 이름만**(`OutfitGroup 듀오 #001 · amazoness / BBW bombshell · 딥 플런지 / 밴도 · …`). 최대 104자.
- 검수: 키·프롬프트 310개 중복 없음, 한글·금지 단어·`navel`·`Pattern density` 0, 단어 수 솔로 487~728, 듀오 891~1205, 트리오 1345~1720, 쿼르텟 1722~2179, 퀸텟 2191~2632, 체형 20종, 인물 수와 `Jewelry:`·`forty inches` 개수 일치.
- 등록: 포즈 패치 `포즈 교체 59개` + 번들 `categories added=2, keys added=310`, 개수 **15,340 → 15,650**, push `96e66693..4bf14a73`.

### 56-8. 미검증·주의
- 코스튬 28종 중 닌자 A, 이집트 여왕 등 새 6종은 특화 체형 1개로만 시험했고, 번들에서는 다른 체형(부피 큰·랜덤)과 섞인다.
- 의상 그룹의 Slit/UltraMini 상의 조합, 비키니(배경 5곳 한정) 등은 개별 시험 없이 그룹 시험 1개씩으로 확인.
- 극단 체형의 서 있는 포즈 결과는 없음. 얇은 체형 소량 포함 여부 미결정.
- 가슴 특화 체형으로만 시험한 의상(Bust·MicroBikini·MuscleBust)은 그룹에 넣지 않았다.

### 56-9. 교훈
- 사용자가 "샘플", "위에 한거", "1" 같은 지시어를 쓸 때 가리키는 대상이 모호하다. "샘플 모두 정상"을 추가 8종으로 읽었다가 취소했고, "코스튬 말고 위에 한거"로 정정받았다. **결과 보고가 오면 어느 파일의 결과인지 한 줄로 되짚어 확인**한다.
- 사용자가 결정하지 않은 항목(포즈 패치 적용)을 제안만 하고 진행하면 "안 하기로 했다"는 반응이 나온다. 선택지는 한 번에 하나만 묻고 답을 기록한다.
- 번들을 만들 때 의상별 `bgs`(배경 한정)와 `bodies`(체형 한정)는 그룹 합성에서 같이 처리해야 한다(`mk_costume_bundle.py`의 `gen(..., bgs_list)` 참고).
- 단일 글자 전역 이름 충돌(55-5)은 이번 생성기(F_ 접두어)에서도 유지.

### 56-10. 열린 과제 (v6.58 기준)
- **Material Blend + 새 영역 번들**(생성·등록 대기).
- 미보고 시험: NewColor_Check8, CutoutLen3, PlungeUltraMini2, BodySpecial6/8, UltraMiniTop4 #4, ExtremeStanding4, Bandeau2F_Bust2.
- 보류: 크롭 시리즈, 언더붑, 젖은 마이크로 비키니, 인형 트리오, 지역 글램 메이크업 인종 연결, 옛 프리셋 배꼽 펜던트 문구 일괄 교체, 22체형 전체 검증, 앱에서 새 카테고리 표시 확인, **옛 핸드오프 삭제는 나중**.
- 코스튬 다음 후보(미시험): 비서, 셰프, 사이버펑크, 발레리나, 플라멩코, 격투가, 비치발리볼; 재질 쪽 후보: 얼음·서리, 깃털, 헤나·메헨디, 회로·사이버, 진주층·곤충 날개, 거울 파편 모자이크.
- 백업: `LumineX_generators_backup_2026-10-14.zip`(544개 파일, 코스튬·그룹 생성기와 패치 포함으로 갱신).
- 등록 현황: 합계 **15,650**(LA) + 레거시 576. 마지막 push `4bf14a73`.


## 57. 새 재질 6종 · 그룹 시험 · 번들 300 · 등록 (v6.59, 2026-10-15)

> 56장 이후 이어진 작업. 사용자는 계속 번호별 "1회 성공/실패"만 알려준다. 56-6, 56-9처럼 지시어가 모호해지는 경우를 줄이려고 결과를 받을 때마다 어느 파일의 결과인지 되짚었다.

### 57-1. 출발점: "의상 없는 쪽에서 안 해본 게 뭐가 있을까?"
- 사용자 질문: "Material Blend는 의상 없는 쪽?" → **예**. Material Blend는 한 사람의 몸을 부위별로 나눠 부위마다 다른 재질을 입히는 방식이라 의상·코스튬 번들과 별개다. 새 영역(크롬·라인스톤·프로젝션·스플래시)을 넣은 Blend 번들은 **아직 미생성·미등록**("이건 나중에 다시 등록하자").
- 이어서 "의상 없는 쪽에서 우리가 안해본게 뭐가 있을까?" → 재질 후보 6종(얼음·서리, 깃털, 헤나·메헨디, 회로·사이버, 진주층·곤충 날개, 거울 파편 모자이크)과 구성 후보(상태가 변하는 그라데이션, 부분 덮기)를 제시. 사용자: **"새 재질 영역 하나씩 샘플 줘봐."**

### 57-2. 샘플 7개 (`LumineX_NewMat7_Solo.md`)
- 진주층과 곤충 날개는 성격이 달라 **따로 나눠 7개**로 만들었다. 모두 솔로, 전 축 기본 랜덤(체형 `BIG5`, 나이, 포즈, 인종, 배경, 힐, 네일, 주얼리, 메이크업). 포즈는 팔짱·얼굴 감싸기 제외(첫 생성에서 얼굴 감싸기가 나와 `POSES` 필터를 추가하고 다시 뽑았다).
- 틀: 새 영역 4종 때의 `mk_area8.py`와 같은 구조(`HEAD` + 템플릿 `T_*` + `base`/`acc`/`fin`), 템플릿 7개와 변형은 `scratch_up/newmat_defs.py`. 헤나는 몸 위에 "그려진" 무늬라 `HEAD_H`(`drawn directly onto`, `not a sticker`)를 따로 썼다. 생성기는 `mk_newmat7.py`(= `build_mk7.py`가 `mk_area8.py`를 읽어 만든다).
- 사용자 보고: **1회 성공 1·2·4·5·6·7, 실패 3(헤나·메헨디)**. 헤나는 사전에 "정교한 문양이라 실패 확률이 높다"고 예상했던 그대로였고 **제외**.
- 채택 6종: 얼음·서리(글레이셔 블루), 깃털(레이븐 블랙), 회로·사이버(블랙 + 골드 트레이스 + 시안 LED), 진주층(펄 화이트), 곤충 날개(잠자리 그린골드), 거울 파편 모자이크(실버).

### 57-3. 그룹 구성 논의와 시험 8개 (`LumineX_NewMat6_Group8.md`)
- 사용자 질문: "듀오 트리오는 섞는건가?" → 지금까지의 듀오·트리오는 **사람마다 다른 재질**(Material Mix 방식)이고, Blend(한 몸을 부위별로 나눔)와는 다르며, 같은 재질을 여러 명이 입는 방식(`mk_same_*`)도 따로 있다고 설명.
- 사용자 결정: **"같은 종끼리 2~5종, 섞어서 2~5종 랜덤으로 섞어서 하면 좋을 듯."**
- 시험: 같은 재질 2·3·4·5인 4개 + 섞은 재질 2·3·4·5인 4개(재질 6종에서만, 기존 크롬 등과는 섞지 않음). 생성기 `mk_newmat_grp.py`(시드 20261403). 사용자 보고: **"다 잘 생성돼."**

### 57-4. 번들 구성 합의와 추가 색 확인
- 제안 후 사용자 **"만들자."**: 총 300 = 솔로 60(재질당 10) + 같은 재질 2~5인 120(재질당 인원별 5) + 섞은 재질 2~5인 120(인원별 30).
- 재질마다 색 변형을 하나 더 넣었다(통과한 색 + 새 색). 새 색은 등록 전에 6개 확인 샘플(`LumineX_NewMat6_ColorCheck6.md`)로 시험: 얼음·서리 딥 사파이어, 깃털 스노우 화이트, 회로·사이버 화이트 세라믹, 진주층 블랙 타히티, 곤충 날개 모르포 블루, 거울 파편 골드 틴트. 사용자 보고: **"다 생성 잘 돼. 일부 맨살은 케바케니까."** → 6색 모두 채택, 제외 없음.

| 재질 | 통과 색 | 새 색 |
|---|---|---|
| 얼음·서리 | 글레이셔 블루 | 딥 사파이어 |
| 깃털 | 레이븐 블랙 | 스노우 화이트 |
| 회로·사이버 | 블랙 골드 | 화이트 세라믹 |
| 진주층 | 펄 화이트 | 블랙 타히티 |
| 곤충 날개 | 잠자리 그린골드 | 모르포 블루 |
| 거울 파편 | 실버 | 골드 틴트 |

### 57-5. 번들 `la_newmat6_300_bundle.json`
- 파일: `la_newmat6_300_bundle.json` + `patch_la_newmat6_1_json.py`(`patch_la_area4_1_json.py`와 같은 구조, 번들 1개). 생성기 `mk_mat6_bundle.py`(시드 20261501 확인 샘플, 20261502 번들; `mk_area4_bundle.py` 앞부분 exec + `newmat_defs.py` 읽기). 제외할 색은 `mat6_excl.json`(`["ice|딥 사파이어", ...]`)로 지정하면 다시 생성할 수 있다(이번엔 파일 없음).
- 키·카테고리: `la_ice_`·`la_feather_`·`la_circuit_`·`la_nacre_`·`la_wing_`·`la_mirror_` + `solo_001~010`, `duo/trio/quartet/quintet_001~005` → 카테고리 `🏺 Living Artifact · {Ice,Feather,Circuit,Nacre,Wing,Mirror} Formula` 각 30개. 섞은 재질은 `la_m6mix_{duo,trio,quartet,quintet}_001~030` → `🏺 Living Artifact · Six-Material Mix Formula` 120개. 접두어 충돌 없음(확인).
- 같은 재질 그룹은 사람마다 그 재질의 두 색 중 하나를 랜덤으로(같은 색이 반복될 수 있음), 섞은 재질 그룹은 서로 다른 재질 n개에서 색 랜덤.
- 규칙: 체형 `BODIES22`에서 **얇은 체형(curvy petite·wide hip narrow) 제외한 20종**(코스튬 번들과 같은 정책), 포즈 팔짱·얼굴 감싸기 제외, 극단 체형(USSBBW·hourglass SSBBW) 솔로 앉은 자세 70%, 주얼리는 배꼽 항목 제외(`jewel_fam`), 인종은 기존 `one()` 규칙, 솔로 힐 40인치 55%·그룹 40인치, 솔로 후처리 `Pattern density MAXIMUM — zero bare skin` 문장 유지(통과한 샘플과 동일).
- 제목은 `Mirror 쿼르텟 #003 · 체형 … · 거울 파편 실버×2+골드 틴트 · 배경 · 메이크업`처럼 같은 색은 `×n`으로 묶어 **최대 103자**(처음엔 110자라 줄임).
- 검수: 키·프롬프트 300개 중복 없음, 한글·`navel` 0, `Jewelry:` 개수=인원, 힐 40인치 개수=인원(40인치 모드), 섞은 재질은 재질 종류 수=인원, 솔로 힐 40인치 38 / 숫자 없음 22.

### 57-6. 등록
- 사용자가 `preset_builders\`에 두 파일을 넣고(`했어`) 아래 순서로 실행: `$env:PYTHONUTF8="1"` → `patch_la_newmat6_1_json.py` → `patch_livingartifact_2_meta.py` → `(Get-ChildItem presets\la_*.json).Count` → `git add presets preset_builders core/presets_meta.py` → 커밋(속성 줄 포함) → `git push`.
- 실측(사용자 출력): `Done. AST OK. categories added=7, keys added=300`, 백업 `presets_meta.py.bak_livingartifact`, `(Get-ChildItem presets\\la_*.json).Count` = **15950**(15,650 + 300), 커밋 `[main 37be7961] … 303 files changed, 24768 insertions(+)`(CRLF 경고만 있고 문제 없음), push `4bf14a73..37be7961  main -> main`. 앱에서 새 카테고리 7개 표시는 미확인.

### 57-7. 부수 작업: legendary bust 체형 코스튬 3개
- 사용자: "Luminex costume2 docteacher에 성인 코스튬 · 의사 · 바스트 특화 · 체형 legendary bust · 인종 ebony · 배경 버스 터미널 · 힐 40인치의 체형 프롬프트가 좋은 것 같아." → 등록된 코스튬 번들에서 이미 의사 등 바스트 그룹(간호사·의사·선생·메이드·마녀·승무원·소방관·뱀파이어)이 `legendary bust`/`curved bust`임을 확인해 알려줌.
- 이어서 "요 체형으로 3개 정도 줘볼래?" → 의사·선생·간호사를 legendary bust로 고정해 `LumineX_LegendaryBust_Costume3.md`(`mk_leg3.py`). 사용자 답 "1, 2" → **1·2 성공, 3(간호사)은 성공하지 못한 것으로 이해**했으나 사용자가 3번 결과를 따로 확정하지 않았고, 곧바로 새 재질 7개 결과 보고로 넘어갔다. **간호사 결과는 미확정**(원인 미확인).

### 57-8. 교훈
- `exec`로 다른 생성기의 앞부분을 불러올 때 그쪽 파일이 같은 이름의 변수(`_src`)를 이미 덮어쓴다 → 내 변수는 `_A4`처럼 겹치지 않는 이름을 쓴다(55-5의 전역 이름 충돌과 같은 계열). 생성기는 `PYTHONPATH=../master:.`을 주고 `bk` 폴더에서 실행해야 한다(스크립트 위치만 보면 모듈을 못 찾는다).
- 새 재질을 번들로 만들기 전 **색 변형 확인 샘플을 따로 받는 순서**(area4의 NewColor_Check8과 같은 방식)가 효과적이었다: 번들은 항상 "통과 색 + 새 색"으로 만들고, 새 색만 확인받는다.
- 그림처럼 "그려진" 재질(헤나)은 입체감이 없어 안 나온다. 입체 질감이 있는 재질만 채택한다.
- 사용자가 "다 잘 생성돼"만 말할 때는 어느 파일 결과인지 직전에 보낸 파일 기준으로 읽는다.

### 57-9. 열린 과제 (v6.59 기준)
- **Material Blend + 새 영역 번들**(크롬·라인스톤·프로젝션·스플래시 + 오늘의 새 6종까지 넣을지 결정). 샘플은 통과, 생성·등록 대기.
- 앱에서 새 카테고리 7개 표시 확인(등록 개수 15,950은 실측 확인 완료).
- 미보고 시험: NewColor_Check8, CutoutLen3, PlungeUltraMini2, BodySpecial6/8, UltraMiniTop4 #4, ExtremeStanding4, Bandeau2F_Bust2, 간호사(legendary bust) 결과.
- 보류: 크롭 시리즈, 언더붑 스타일, 젖은 마이크로 비키니, 인형 트리오, 지역별 글램 메이크업 인종 연결, 옛 프리셋 배꼽 펜던트 문구 일괄 교체, 22체형 전체 검증, **옛 핸드오프 삭제는 나중**.
- 코스튬 후보(미시험): 비서, 셰프, 사이버펑크, 발레리나, 플라멩코, 격투가, 비치발리볼.
- 백업: `LumineX_generators_backup_2026-10-15.zip`(552개 항목, 새 생성기·`scratch_up/` 포함). 이전 백업과 핸드오프는 삭제하지 않았다.
- 등록 현황: 합계 **15,950**(LA, 실측) + 레거시 576. 마지막 push `37be7961`.


---

## 58. 세 축 용어 정리 · Core Body 19 · Core Blend 270 · 소재 축 새 영역(물체 몸) (v6.60, 2026-10-15)

> 57장 이후 이어진 작업. 사용자는 계속 번호별 "1회 성공/실패"만 알려준다. 이 장은 **용어 정리 → 체형 풀 확정 → Blend 번들 → 소재 축 새 영역 탐색** 순서로 기록한다.

### 58-1. 축 용어 (사용자 확정, 앞으로 이 단어로만 말한다)
몸을 어떻게 다루느냐 기준으로 **세 축**이다. "재질"이라고만 하면 둘이 섞여 매번 헷갈렸기 때문에 이 이름으로 고정한다.

| 축 | 정의 | 포함 |
|---|---|---|
| **바디페인팅 축** (= 실사 축) | **실제 몸이 남고 그 위에 무엇을 얹는** 쪽. 의상은 없고 신발·손톱만 있다 | 일반·임산부·맥시멀리스트·자유축 트랙, 공예·이레즈미·UV네온·금박, Material Mix/Blend, Core Blend 270, 피어싱 프레임(얼굴·가슴·허리 컷) |
| **소재 축** | **몸 자체가 재질**인 쪽 (실제 몸이 재질로 대체됨) | 석고상·조각상 프레임 컷, 듀얼바디, 이번에 찾은 물체 몸 |
| **의상 축** | 실제 몸에 **옷·코스튬**을 입히는 쪽 | 의상 번들, 성인 코스튬(54~56장) |

- 판정 기준: "실제 몸에 얹으면 바디페인팅, 몸이 재질로 대체되면 소재". 사용자 말: "소재는 몸 자체가 재질이야. 그게 가장 큰 차이점."
- **공통 옵션**(어느 축에나 붙이는 독립 옵션): 피어싱(P축), 쥬얼리, 메이크업, 헤어, 신발, 손톱, 피부톤, 연령(실버폭스). 피어싱은 실제 얼굴에 달리므로 별도 축이 아니라 이 옵션이다. 카테고리는 몸 처리 기준으로 나눈다(Piercing Frame → 바디페인팅 쪽, Piercing Statue → 소재 쪽).
- **미정**: Face Sculpt(눈·입술 주인공 얼굴 컷)는 몸이 아니라 얼굴이 주인공이라 3축에 딱 안 들어간다. 바디페인팅의 얼굴 컷으로 둘지 4번째 "얼굴 축"으로 둘지는 다음에 정한다.
- 용어 혼동 사례: 어시스턴트가 처음엔 "재질 쪽"이라는 말로 공예·이레즈미까지 묶어 헷갈렸고, 의상 축을 빠뜨렸다가 사용자가 짚었다.

### 58-2. 소재 쪽 프레임 컷 정의 (재확인)
- **카메라 크롭이 아니다.** 몸 전체가 재질로 대체된 조각이 허벅지·무릎에서 매끈한 둥근 끝으로 마감되는 형식이다. 목·얼굴·어깨 윗부분만 실제 피부.
- 실제 길이: **힙컷**=허벅지 일부, **데미스탯**=허벅지 중간, **쓰리쿼터**=무릎 위, **발목컷**=앉은 포즈용(21-3-2: 다리를 앞으로 뻗는 앉기 포즈는 허벅지 끝 문장을 무시하고 발목 컷으로 생성됨).
- 두 허벅지는 끝까지 따로 둥글게 끝나며 합쳐지지 않는다.

### 58-3. Core Body 19 (새 번들의 기본 체형 풀)
- 가슴: legendary bust · curved bust · siren bust hourglass
- 허리: glamour hourglass · hourglass bombshell · black glamour · apex siren
- 힙: violin hip hourglass · latina curves · Brazilian booty glam
- 키 큰 쪽: amazon bombshell · towering hourglass · amazoness
- 복부: muscular hourglass BBW · hourglass SSBBW · USSBBW
- 근육: Nubian booty builder · powerlifter bombshell · Nubian bust builder
- **제외**: super hourglass(최상급 표현이 많아 약하게 나옴), BBW bombshell.
- 교훈: **구체적인 형태 묘사는 강하게, 최상급 수식어는 약하게** 렌더된다. 사용자가 "가장 강하게 적었는데 전체적으로 약하게 나왔다?"라고 짚은 데 대한 답. 사용자 관찰: 브라질리언 부티 글램은 힙 강조, 글래머 아워글래스는 균형 잡힌 허리 강조 쪽이 맞는 듯.
- 처음 18개로 세었으나 실제는 19개였다. 이름은 사용자 제안 "Core Body"로 확정.
- **힐 "relative" 모드 버그**: 바디페인팅 솔로 틀의 신발 줄에 "a full forty inches tall and a twelve-inch hidden front platform"이 항상 들어간다. 제자리 교체 "taller than her entire shin from ankle to knee and a towering hidden front platform"는 작동. 옛 Blend 틀에는 힐 숫자가 없다. (힐 없는 샘플은 `LumineX_BodyPaint_GlamourNoHeel1.md`)

### 58-4. Material Blend 결정과 Core Blend 270 번들
- 새 Mix 틀로 만든 Blend 샘플은 **팔·다리 맨살이 너무 많았다**(경계가 아니라 사지 전체). 원인 추정: 최근 바디페인팅 틀이라서. **옛 Blend 틀(검은 피부·검은 배경)로 되돌리자 해결.**
- Mix 틀과 옛 Blend 틀을 비교: Mix 틀로 만든 샘플은 팔·다리 맨살이 많았고(팔·다리 덮는 문구를 더해도 부족), 옛 Blend 틀로는 솔로가 해결됐다.
- **돌출형 재질 5종 제외**: 크리스탈 · 보태니컬 · 얼음 · 거울 파편 · 공작눈무늬 비늘(17재질 풀에서). 사용자: "블랜드엔 돌출된 재질은 안쓰는게 어때?"
- **2~4혼합만 사용.** 5~7혼합은 생성은 되지만 몸 부피가 엄청 커졌다(사용자). 구조 헬퍼 `spaced()`는 4구역까지만 지원(5~7은 패치 필요, 쐐기형은 6구역 이하).
- **경계 문장**: "전환 구간(transition zone)"·"흐릿함(hazy)" 표현이 **은색 띠**의 원인이었다. 경계를 언급하지 않으면 별로였고, 중간안도 별로였고, **곡선 문구**("gently undulating curves로 나뉜다", "dividing curve N")가 가장 나았다("이게 그나마 제일 나은 듯"). 코드: `4c`/`curve3`의 후처리(`curve(p)` 정규식)는 "경계가 흐릿하다…완전히 덮는다" 문단을 빼고 "transition zone"을 "dividing curve"로 바꾼다.
- **번들 `la_coreblend_270_bundle.json`**: 키 `la_coreblend{2,3,4}_{solo,duo,trio}_001~030` → 카테고리 9개 `🏺 Living Artifact · Core Blend {n}-Mix {Solo|Duo|Trio} Formula`(각 30). 제목 ≤103자, 메타 포맷 `core-blend`, 레이아웃 `geometry-curve-v1`, 경계 `curve-v1`. 체형은 Core Body 19 전체를 기본 랜덤, 전 축 기본 랜덤. 생성기 `mk_coreblend_bundle.py`(시드 20261950; `pick_mats`를 REC로 감싸고 `curve(p)` 후처리, 중복 제거, 제목 폴백 ≤103자).
- **등록 완료(2026-10-15 집)**: `patch_la_coreblend_1_json.py` → `patch_livingartifact_2_meta.py`(`Done. AST OK. categories added=9, keys added=270`, 백업 `presets_meta.py.bak_livingartifact`) → `(Get-ChildItem presets\la_*.json).Count` = **16220**(15,950 + 270) → push **`a8cc91b4`**(`37be7961..a8cc91b4`).
- 앱에서 새 카테고리 9개 표시 확인은 사용자 대기.

### 58-5. 소재 축 새 영역 탐색 — 질문과 방향
- 사용자 질문: 소재 축은 석고상 프레임 컷과 듀얼바디 정도인데 **새 영역**이 있을까? 수조·석재·목재는 해봤고 **와이어·철근·튜브처럼 몸 자체가 선인 것**, **용기 몸 확장(모래시계)**이 새 영역이라고 사용자가 정리. 이어서 "모래시계처럼 **모양이 몸체**인 걸 더 찾아봐, 전구도 전구 자체가 몸", "투명한 쪽이 좋다, 불투명은 듀얼바디·블렌드에 쓰면 된다".
- 구조: 프레임 컷 틀에서 피어싱은 없고, 목 아래 몸통이 물체로 대체. **Physique 대신 Silhouette 줄**(가슴·허리·엉덩이 덩어리만)과 `Below the collarbones there is no human torso at all: in its place her entire torso is …`.

### 58-6. 선 몸 · 모래시계 · 전구 · 라바 램프 (초반 시험)
- **모래시계**: 확정(좋음). 위쪽 구는 "upper bulb is her bust"로 평범하게 쓰면 된다. 돔 모양으로 가슴을 묘사하면 오히려 **몸 안에 사람 몸(모래시계 속 사람)**이 그려져 되돌렸다. 허리는 모래시계만, 뒤에 몸이 없게.
- **철사(와이어)**: 철사를 "더 촘촘히/채운 형태"로 쓰라고 하면 **살이 돌아온다**. 연필 굵기 철사를 엉킨 고리로 낙서처럼 감은 "scribbled wire sculpture"에 "no real limb, chest or skin"을 명시한 것이 한 번 통했다(Redo3). Redo5는 결과 미보고 — 살이 케바케로 나오면 첫 시도 성공 기준상 채택 보류.
- **전구**: 전구 모양 자체가 몸통이어야 하는데 전구가 몸통 위에 얹힌 것으로 나온 적이 있어 문구 재조정. **라바 램프**: 처음엔 투명 수조 버전처럼 보여 색 액체·밀랍 덩어리·황동 캡을 추가.
- 철근·네온 튜브는 결과 미보고(보류).

### 58-7. 물체 몸(모양이 곧 몸) — 핵심 구조와 시험 결과
**확정 구조(시계에서 완성):**
1. Silhouette 줄(공용 SIL 문구에서 `glass neck`·`bulb` 등 유리 단어를 물체에 맞게 치환 — 안 하면 황동/나무에 유리 단어가 새어 들어감)
2. Body 줄: "no human torso at all: in its place her entire torso is [물체]" + 해부 용어 나열 금지
3. **어깨·팔·허벅지를 몸통과 같은 재질로 명시**하고, 허벅지도 "thighs of the same …"로 못 박는다(해파리에서 허벅지 재질을 안 적었더니 팔·다리가 실제 몸으로 나왔다)
4. **목 경계는 원래 문구**(들쭉날쭉한 선, 위는 피부·아래는 재질). 시계 위쪽 테두리를 경계로 바꾸는 안도 시험했으나 채택하지 않고 원복(사용자: 목 주위 경계는 그대로 살리고 목 아래 어깨·팔은 다리 소재와 같게).
5. 투명 물체는 Transmission 줄, **불투명 물체는 Material(밀도 높은 고체) 줄**.

**확정 샘플(성공):**
- **시계**: **둥근 시계 하나가 세로로 길게 늘어난 몸**(가슴=쇄골 높이에서 넓게 부풀고, 허리 잘록, 엉덩이 부풀음), 문자판은 몸 전체 길이로 늘어나고 숫자는 테두리를 따라 위에서 아래로, 바늘은 허리 높이 중심, 톱니·스프링 노출. **어깨·팔·허벅지는 광택 청동**, 유리는 문자판 크리스털에만. 최고는 **힙컷·글래머 아워글래스**(2번), 차선 힙컷·사이렌 바스트 아워글래스(3번). 데미스탯·레전더리 바스트(1번)는 성공으로 안 침. 사용자 이해 정리: "원형 시계를 사람의 몸처럼" = 시계가 인체처럼 만들어진 것, 시계 안에 사람 몸이 있는 게 아님. 둥근 시계 두 개를 8자로 쌓는 안·큰 시계 하나(케이스형) 안은 시험했으나 "하나의 시계가 세로로 늘어난" 안으로 확정.
- **허리케인 랜턴**: 속이 빈 유리 몸 한가운데 **굵고 긴 실제 흰 초 한 자루가 공중에 떠 있고 촛농이 흘러내림**("됐어"). 처음의 "불꽃 하나" 문구로는 초 여부가 정해지지 않았음.
- **향수병**: 2번(힙컷·글래머 아워글래스) 가슴 표현 좋음, 3번 약간, 1번은 성공 아님. 변주(병 모양·액체 색·장식)가 많지만 사용자가 "이 정도면 충분".
- **공예 조각상**: 종이접기 · 구체관절 인형 **채택**(설탕 유리는 투명으로 다시 줘도 드롭).
- **불투명 물체**: **바이올린 · 청자 매병 좋음**. 바이올린은 위 몸통=가슴, C자 허리, 아래 몸통=엉덩이로 몸 모양과 가장 잘 맞음.

**변주로만 기록**(모래시계/수조 계열이라 새 영역 아님): 스노우 글로브 · 증류 플라스크 · 유리 호리병(조롱박) · 아르누보 꽃병.
**약함**: 비눗방울(1번만 그나마).
**실패/드롭**:
- **원소 몸(불·물·연기·번개)** — 모델이 사람 몸 실루엣을 먼저 그리고 그 위에 원소를 덧입힘(번개만 그나마). 시도: 공용 Transmission 줄의 "transparent material" 문구 제거(불꽃이 유리 몸 안팎에 피어오르는 그림이 나온 원인), Physique→Silhouette, "outline이 곧 원소", "all the way through", Pose의 `(solid material)`·Boundary의 `raised step` 제거, 원소 덩어리 두 개로 대체 — **모두 실패, 사용자 "원소는 포기".** 교훈: 정해진 모양이 없는 것은 사람 몸 윤곽이 먼저 나온다.
- 설탕 유리(투명으로 다시 줘도 드롭) · 해파리("그냥 투명 치마") · 장구(탈락) · 기타(탈락) · 지구본("그냥 재질 느낌", 늘리면 구 모양이 사라지고 지도 무늬만 남음).
- 첼로는 바이올린과 차별점이 없어 시험 안 함.

**판단 규칙(사용자와 합의):**
- 늘려도 알아볼 **부품**이 있는 물체만 된다(시계=문자판·바늘·톱니, 바이올린=f자 구멍·현·브리지, 랜턴=초, 향수병=향수 액체). 표면 무늬뿐인 물체(지구본)는 재질 느낌이 된다.
- 둥근 물체를 시계처럼 늘리는 틀은 "시계 자리에 다른 물건"일 뿐이라 **새 영역이 아니라 물건 목록 확장**이다. 번들을 만들 땐 시험에 통과한 목록(시계·바이올린·청자 매병·랜턴·향수병 + 종이접기·구체관절 인형)만 쓴다. 카메라 렌즈·압력계·나침반·선박 키는 후보일 뿐 미시험.
- 두 덩어리를 좁은 목으로 잇는 모양(스노우 글로브·플라스크·호리병)은 구조가 모래시계라 새 영역으로 안 친다.

### 58-8. 생성기와 실수 기록
- 생성기: `mk_statue_new6~13.py`(선 몸·모래시계 초반), `mk_statue_obj11.py`(물체 11종), `mk_statue_elem4~4d.py`(원소 몸 4세대), `mk_statue_clock1/clock8/clockst/clockrim/clockbz.py`(시계 5세대), `mk_statue_craft3/sugar1/snow3/lantern3~3c/perfume3/vase3/bubble3/jelly3~3b/opaque3/guitar3/globe3.py`. 실행은 `zx/glassface`에서 `PYTHONPATH=../../master:.`, 석고상 베이스 `gen_pierce_statue.py`(`def build(` 앞까지 exec). `la_blend_540_bundle.json`을 `zx/glassface`에 복사해 둬야 한다.
- 실수: ① `\"\\n\"` 이스케이프로 md 파일이 줄바꿈 없이 깨짐(실제 개행 사용). ② `str.replace(a, b, 1)`이 다른 물체 항목에 먼저 걸려 해파리 허벅지 수정이 안 들어감(항목 지정 치환). ③ `"narrow glass neck"`를 `narrow narrow`로 치환해 반복 단어 검사에 걸림. ④ `pkill -f` 패턴이 자기 셸 명령과 겹쳐 종료(144). ⑤ 사용자 질문 "시계 몸" 선택지를 잘못 해석해 "큰 시계 하나(케이스형)"를 만들었으나 의도는 "둥근 시계가 몸처럼 늘어난 것"이었음 — 의도가 모호하면 한 번 묻고, 틀리면 바로 되돌린다.
- 샘플 결과 보고 방식: 번호별 성공/실패와 한 줄 이유만. 물체는 한 종류씩 3개(같은 틀, 체형·프레임 컷 랜덤)로 보낸다.

### 58-9. 열린 과제 (v6.60 기준)
- 앱에서 Core Blend 새 카테고리 9개 표시 확인(개수 16,220은 실측 확인 완료).
- **물체 몸 번들**: 확정 구성(시계·바이올린·청자 매병·랜턴·향수병·종이접기·구체관절 인형)으로 새 카테고리를 만들지 결정(미생성). 만들 때 모든 축 기본 랜덤, 어깨·팔·허벅지 같은 재질 명시, 목 경계 원문 유지.
- 미보고: 철사 Redo5, 철근·네온 튜브 결과, 바이올린·청자 매병 외 불투명 후보(분청 호리병 등), 카메라 렌즈 등 둥근 물체 후보.
- 보류: Core × 석고상 프레임 컷 샘플, 새 재질을 석고상 프레임에 넣기, 앉기 앵클컷 재시험, 상체 실사/하체 재질 카테고리, 돌/목재/스테인드글라스 Formula 축 확인, Face Sculpt의 축 위치, 신규 카테고리 HOF/SSS 티어.
- 백업: `LumineX_generators_backup_2026-10-15b.zip`(597개 항목, 이번 세션 생성기 42개 추가). 이전 백업과 옛 핸드오프는 삭제하지 않았다.
- 등록 현황: 합계 **16,220**(LA, 실측) + 레거시 576. 마지막 push `a8cc91b4`.

---

## 59. 격자 소재 · 접지 문장 · 남성 바디페인팅 · 남성 얼굴+여성 체형 · 듀오/트리오 (v6.61, 2026-10-15)

> 58장 이후 이어진 작업. 사용자는 번호별 "N차 성공/실패"만 알려준다(실패는 한 줄 이유). **이 장은 등록 없이 시험만 한 구간**이라 새 번들은 없다. 합계 `la_` **16,220** 그대로(마지막 push `b11c503e`, v6.60 핸드오프).

### 59-1. 격자(오픈 라티스) 소재는 프레임 컷이 안 된다
- 철사(가는 선)·철근·네온 튜브처럼 **속이 뚫린 격자 몸**은 허벅지 끝이 닫히지 않아 다리가 계속 이어지거나 맨살 다리가 나온다. 힙/데미/쓰리쿼터 컷 모두 실패(철사: 쓰리쿼터·발목·무릎 컷이 섞여 나오고 살 다리 출현, 철근: 무릎/발목 컷이 케바케).
- **전신으로 하면**: 철사는 가는 선 때문에 맨살 다리가 나와 실패, **철근 전신은 성공**(전신 카테고리 후보지만 보류). 네온 튜브는 미시험.
- **닫힌·솔리드 끝 재질**(유리, 수조, 석재)은 프레임 컷이 잘 된다. 사용자 말: "투명재질, 투명 수조재질 같은 것은 그래도 잘 나왔던 것 같은데."
- 생성기: `bk/mk_statue_wire4.py`, `mk_statue_wire4b.py`(→ `LumineX_Material_WireRebar4/4b.md`), 전신 변환 `WireRebarFull2.md`.

### 59-2. 문장 A와 접지 문장 (프레임 컷 보강)
- **문장 A**(쓰리쿼터 보강): `no shins, no ankles and no real skin legs of any kind — below each rounded tip there is only the glossy floor`.
- **접지(Floor-rest) 문장**: `both rounded tips resting directly on the polished floor with a soft contact shadow` → 물체 몸 Mix 3c에서 **전원 바닥에 닿아** 공중 부양 문제 해결(사용자 "다 바닥에 닿은 듯").
- **물체 몸 번들은 등록하지 않기로 결정**(사용자: "이건 등록하지 말자. 왠지 뭔가 아쉬워."). 종이 변형은 앞서 성공한 것으로 확정.

### 59-3. 피어싱 시도
- `gen_pierce_hip.py` → `Pierce_Hip_Body4.md`: 큰 체형(5번)은 힙 쪽 살이 나오고 얼굴이 작아 피어싱이 잘 안 보임. 생성 자체는 성공.
- `mk_pstatue_core.py`(Core 체형 × 피어싱 석상) → "피어싱 특화인데 피어싱이 잘 안 보여서 그닥" → **중단**. 얼굴 컷 피어싱은 **얼굴이 큰 크롭 프레임**에서만 효과가 있고 석상 전신에서는 얼굴이 작아 무의미.
- `mk_pface_new4.py`(머리 재질 MW/MN/MP + ARCH 문장, 얼굴 새 시도)는 미시험로 보류.
- 다른 AI가 준 아이디어(피어싱 2·3번, 얼굴 주얼리 10개·20개 프롬프트)는 **참고만**: 피어싱이라기보다 주얼리 쪽이고, 우리 재질 교체와 크게 다르지 않다는 판단.

### 59-4. 핵심 발견: 등록된 Core 바디아트 문구가 정면 성공을 좌우한다
- **정면 포즈 실패의 원인은 "누드 필터"가 아니었다**(내가 잘못 설명했다). 원인은 바디아트 **문구**였다.
  - 부위 앵커링 목록(가슴·배·허벅지 등을 나열)을 쓴 초기 문구: 정면 **0/7 실패**.
  - **등록 문구**로 교체: 남성 정면 **3/3**(양손 허리·머리 쓸기), 여성 정면 2/4.
- **등록된 Core 솔로 단락 구조**: Image format → 카메라/배경 줄 → Subject → Physique → Skin → Body Art → Pose → Footwear → Background & Lighting → 마무리 형식 줄.
- **바디아트 문구(고정)**: `wide {cb} bands following every deep crease and curving around the hips and thighs like contour lines, dense {cf} filling the space between every band` + 커버리지 목록 `shoulders, upper arms, forearms, backs of {her/his} hands, sides, back, rear, lower belly, knees, calves and the tops of {her/his} feet`. **가슴·배·허벅지를 직접 나열하지 않는다.** 마지막 문장은 `Her face is left unpainted and the pattern fades out at the neck with no hard line.`
- 비정면 포즈는 처음 문구에서도 성공했었다.

### 59-5. 남성 바디페인팅
- 요청: "남성 의상없는 바디페인팅", 얼굴은 한중일 아이돌·20~30대 모델, 체형 8종(V자 보디빌더·린 애슬레틱·키 큰 슬렌더·파워리프터·대형 헤비·클래식 머슬·스트롱맨·중년 실버 애슬레틱).
- 결과: 솔로 6개 중 **2·4·6번 성공 → 전부 측면 샷**, 이어 측면/비정면 6/6 성공(1번만 3회차). 정면 3개 실패 → 여성 부피큰/근육질 체형 정면 4개도 실패 → **등록 문구로 바꾸자 정면 성공**(59-4 참조).
- 여성 신발을 남성에게: 힐 → 싸이하이 부츠 → **40인치 표현**(`razor-thin tapered heel a full forty inches tall and a twelve-inch hidden front platform`)으로 확정. 40인치 표기는 듀오 이상에서 효과가 확실하고 솔로는 케바케.
- **남성 야외 40인치 슈즈 5/5**(`LumineX_Male_BodyPaint_Outdoor5_40in.md`, `bk/mk_male_outdoor5.py`): 체형 5종, 포즈 5종(정면·워킹·뒷모습 3/4·옆모습 한 팔 올리기·와이드), 신발 5종(싸이하이 부츠·펌프스·니들힐·앵클스트랩), 배경은 `bg_library` 야외 44개 중 랜덤. 2번만 2차 성공.
- 남성 솔로 번들(약 100개)은 **제안만 하고 미결정**.

### 59-6. 남성 얼굴 + 여성 Core 체형
- 구조: 남성 얼굴(`FACEM`: 각진 턱·굵은 눈썹·광대 / 넓은 턱·깊은 눈·강한 이마 / 사각 턱·굵은 목 / 넓은 턱·아담스 애플) + 수염(`BEARDM`: 가벼운 수염·짧은 정리 수염·콧수염·5시 그림자) + 한중일 피부톤, 머리는 자연색(`NATHC`: HCJB·HCNB·HCDB·HCCB·HCAB)과 남성 스타일 4종. Subject 템플릿: `ONE real adult {natm} person with a handsome man's face on a full, curvaceous female body — a man {agem}, ...`.
- 어두운 스튜디오 + 정면 고정 포즈에서는 실패가 많았고, **야외 배경 + 여성 포즈 + 가장 여성스러운 체형(레전더리 바스트·사이렌 바스트 아워글래스·글래머 아워글래스·커브드 바스트·아워글래스 밤쉘)으로 바꾸자 5/5 성공**(1번만 2차). 생성기: `bk/mk_masculineoutdoor5.py` → `LumineX_Female_BodyPaint_MasculineFaceOutdoor5_40in.md`.
- 여성 포즈 5종: S커브(한 손 허리·한 손 머리), 런웨이 워킹, 뒤돌아보기 3/4, 다리 교차 양손 허리, 와이드 스탠스 양손 허리.
- 이전 단계 파일: `MaleFaceFemaleBody3(_40in)`, `MaleFaceBustHourglass3_40in`, `MasculineFaceBustHourglass3_40in`(결과 미보고).

### 59-7. 남성 얼굴에 여성 축 얹기 (헤어·눈 메이크업)
- 질문: "신발 말고 남자의 얼굴에 추가할 만한 여성의 축?" → 헤어 스타일·컬러·메이크업·주얼리. **위험은 메이크업**(립·블러셔 계열은 얼굴이 여성처럼 읽힘). 남성 얼굴 문장(각진 턱·수염)은 그대로 유지, 메이크업은 **눈 위주 5종**(블랙 스모키 윙·골드 글리터·그래픽 블루 라인·플럼 스모키·실버 포일)만 사용.
- 헤어는 여성 계열(웨이브·번·브레이드·포니테일 등), 컬러는 전체 풀.
- 결과 `LumineX_Male_BodyPaint_HairMakeup5.md`(`bk/mk_male_hairmakeup5.py`): **1~4번 성공, 얼굴 여성화 없음. 5번 실패**(키 큰 슬렌더 + 와이드 + **Croatian Hvar filigree linework**). 패턴만 면 채움 계열(Thai Benjarong)로 바꿔 재시험 → **1차 성공** → 원인은 **가는 선 위주 패턴**일 가능성(1회 결과).
- 생성기 부수 수정: `HK` 라벨 슬라이스(`re.sub(r"^[A-Z]+", "", hk)`), 배경 문구의 `her`는 남성 프롬프트에서 `his`로 치환.

### 59-8. 듀오·트리오
- `bk/mk_masculine_duotrio4.py` → `LumineX_Female_BodyPaint_MasculineFace_DuoTrio4.md`: 사람마다 **남성 얼굴 + 여성 Core 체형 + 서로 다른 패턴 + 주얼리**, 40인치 싸이하이 부츠, 야외 한 장소. 듀오 2(4:5 세로)·트리오 2(3:2 가로). 결과: **1·2·4번 1차 성공, 3번 2차 성공**, 트리오는 **가로로 나옴**.
- 주얼리 문구(문법 수정): `JQ_SHORT`를 `{m} {s}/{p}` 포맷으로 — 예: `a single platinum necklace`, `an extreme maximalist stack of well over ten silver earrings`. 종류 6(귀걸이·목걸이·팔찌·반지·발찌·헤어 장식), 금속 5(금·은·로즈골드·플래티넘·혼합).
- 사람 블록 구조: `LEFT/CENTER/RIGHT:` Subject → `Physique:` → `Body Art:` → `Pose:` → `Footwear:`, 공통 `Skin (everyone):` 과 `Background & Lighting:`. 배경 문구는 `completely empty of other people` → `empty of any people other than the subjects`, `same material as her` → `as them`.
- **혼합 트리오**(`bk/mk_mixed_trio3.py` → `LumineX_BodyPaint_MixedTrio3_40in.md`): 여성(여성 얼굴+메이크업) / 남성 얼굴+여성 체형 / 남성 체형을 한 화면에, 전원 바디페인팅, 신발은 여성 신발 40인치. 프롬프트 약 1,200단어.
- **트리오 세로화**(`LumineX_Trio5_Vertical.md`): 이미지 포맷 줄을 `a vertical portrait-orientation photograph, 2:3 aspect ratio, taller than it is wide`로 바꾸고, `THREE people standing close side by side, shoulder to shoulder in a single row`, `the whole row filling the width of the tall frame`, 마무리 줄 `Vertical 2:3 portrait-orientation full-body photograph, taller than it is wide, all faces toward the camera.` 결과: **1~4번 모두 1차 성공, 1번만 가로로 나옴**(5번 미보고). 세로 문구가 대체로 먹히며 나머지는 케바케.

### 59-9. 교훈
- 정면이 안 되면 포즈·필터를 탓하기 전에 **바디아트 문구(부위 나열)** 부터 확인한다.
- 남성 얼굴 + 여성 체형은 **야외·여성 포즈·여성스러운 체형**에서 안정적이다. 어두운 스튜디오 + 정면 고정은 불리하다.
- 남성 바디페인팅은 **가는 선 패턴을 피한다**(1회 결과).
- 격자(속이 뚫린) 소재는 프레임 컷 불가, 닫힌 솔리드 끝 재질만 가능.
- 트리오는 방향 문구를 명시해야 한다(안 쓰면 가로로 나옴).
- 나(어시스턴트)의 오진 기록: 철사/철근을 둘 다 실패라고 한 것(철근 전신은 성공), 남성 정면 실패를 누드 필터로 설명한 것, "1번 해보자"와 "다른 AI 의견"을 잘못 읽은 것.
- 생성기 실수: `build_new`가 파일에 세 번 나와서 치환이 안 먹음(항목별 후처리로 해결), `str.replace`가 exec 줄의 구분자에 걸림, `s.index("def build(")`가 exec 줄에 걸림(→ `"\ndef build(bkey"` 사용).

### 59-10. 열린 과제 (v6.61 기준)
- 미보고: `FrontHeels3`, `FrontThighBoots3(_40in)`, `MaleFaceFemaleBody3(_40in)`, `MaleFaceBustHourglass3_40in`, `MasculineFaceBustHourglass3_40in`, 트리오 세로 5번.
- 결정 필요: 남성 바디페인팅 솔로 번들(약 100), 남성 얼굴+여성 체형 번들, 혼합 듀오/트리오 번들, 남성-남성 듀오 시험, 남성 얼굴 헤어·눈 메이크업 번들화(눈 메이크업 5종 + 가는 선 패턴 제외).
- 보류: Core × 소재 프레임 컷(피어싱 없이), 실버폭스 확장, 철근 전신 카테고리, 네온 튜브, Face Sculpt 축 위치, 티어(HOF/SSS), 앉기 앵클컷 재시험, 4인 이상 피어싱 그룹.
- 등록 현황 변화 없음: `la_` **16,220** + 레거시 576. 이전 핸드오프·생성기 백업은 삭제하지 않았다.

---

## 60. Male Face Female Body Formula 100 등록 · 얼굴 축 · linework 제외 (v6.62, 2026-10-15)

> 59장 직후 같은 날 이어진 작업. 사용자는 번호별 "N차 성공/실패"와 얼굴 평가(남성/중성/여성)만 알려준다.

### 60-1. 등록 결과
- 번들 `la_malefacefemale_100_bundle.json`(솔로 50·듀오 25·트리오 25), 키 `la_malefacefemale_{solo|duo|trio}_NNN`, 새 카테고리 1개 `🏺 Living Artifact · Male Face Female Body Formula`.
- 등록 스크립트 `patch_la_malefacefemale_1_json.py` → `patch_livingartifact_2_meta.py`(categories added=1, keys added=100, 백업 `presets_meta.py.bak_livingartifact`) → 실측 **16320** → commit `c8dad166`(push 완료, 이전 `b11c503e`).
- 생성기: `bk/mk_malefacefemale_bundle.py`. 제목 형식 `Male Face Female Body {Solo|Duo|Trio} #NNN · {한글 체형} · {공예}`(103자 이내).

### 60-2. 번들 구조 (전 축 기본 랜덤)
- **체형 풀 10종**(사용자 제안: "힙강조, 허리강조, 가슴강조"): 바스트 3(legendary bust·curved bust·siren bust hourglass), 허리 4(glamour hourglass·hourglass bombshell·black glamour·apex siren), 힙 3(violin hip hourglass·latina curves·Brazilian booty glam). **제외**: 키 큰 계열 3, 부피 큰 계열(BBW·SSBBW·USSBBW) 3, 근육 계열 3. 사유: 부피 큰 체형은 "여성 체형에 남성 얼굴"이라는 느낌이 확 떨어진다(사용자). 체형은 셔플 덱으로 균등 배분(각 17~18회).
- **포즈**: `POSE_19`에서 얼굴 감싸기 제외(솔로 18종), 그룹은 안전 6종(정면와이드스탠스·3/4각도·뒷모습3/4·걷는동작·허리손·머리넘기기).
- **신발**: `SHOES_24` 전체. 플랫폼 계열은 플랫폼 문구, 비플랫폼 6종은 40인치 표기(`razor-thin tapered heel a full forty inches tall and a twelve-inch hidden front platform`).
- **헤어**: `T.HAIR_STYLE` 31종에서 트윈테일·스페이스번 제외, 컬러 30종 전체. **손톱**: 긴 모양×마감 전체. **주얼리**: 5수량×5금속×6종(`JQ_SHORT` 포맷 문구). **메이크업**: 솔로만 눈 위주 5종 + 없음, 그룹은 없음.
- **공예**: `T.CRAFTS_39`에서 **CroatianHvar·FinnishIittala·UkrainianPysanka 제외**. **배경**: `bg_library` 야외 44개. 방향: 솔로 2:3, 듀오 4:5, 트리오 2:3 세로 문구.
- 사람 블록: `LEFT/CENTER/RIGHT:` Subject → `Physique:` → `Body Art:` → `Pose:` → `Footwear:`, 공통 `Skin (everyone):`·`Background & Lighting:`.

### 60-3. 얼굴 축 시행착오와 결론
1. 남성적 얼굴(각진 턱·수염)만: "아저씨들이 나오니 영"(사용자). 
2. 남성 특징 아이돌형(7종) + 수염 옅게 + 나이 20대: 5e **5/5 성공**, 단 "미소년·아이돌이 아니던데"(사용자 지적: 잘생긴 청년에 가까움).
3. **미소년·아이돌 문구 6종만**(`BOYISH`): 여성 체형 위에서는 **거의 전부 여성 얼굴**(1~3번 여성, 4번 한 명 여성, 5번 중성 한 명). 여성 체형 + 긴 헤어 + 주얼리 + 긴 손톱이 겹쳐 얼굴이 끌려간다.
4. **최종: 남성 특징 아이돌형(`MALEIDOL` 6종) 약 65% + 미소년·중성형(`BOYISH` 6종) 약 35%**(실측 38%), 나이 20대 초·중·후반, 수염 없음~아주 옅은 그루터기. 확인 샘플 5g: 5개 모두 1차 성공(1번 옆모습 애매, 2·3번 남성, 4번 남성 1+중성 1, 5번 남성 2). **여성 얼굴로 나오는 것은 변주로 본다**(사용자 방침).
- 사용자 용어: "미소년·아이돌", 중성적인 이미지도 허용.

### 60-4. 남성 체형에 여성 축 얹기 (남성 얼굴 + 남성 체형)
- 답: 40인치 여성 신발 · 여성 헤어 스타일/컬러 · 눈 메이크업 · 주얼리 · 긴 손톱이 현실적. **피어싱은 전신에서는 불가**(얼굴이 작아 안 보임, 얼굴이 큰 크롭 프레임이 필요).
- `bk/mk_male_boyidol5.py` → `LumineX_Male_BodyPaint_BoyIdol5.md`: 얼굴은 미소년·아이돌 6종만, 수염 없음, 나이 20대. 결과 **2~4번 1차 성공, 1·5번 실패** — 실패 둘 다 **Finnish Iittala glass-inspired linework** 패턴.
- 이름에 "linework"가 들어가는 선 위주 공예(Croatian Hvar·Finnish Iittala·Ukrainian Pysanka)는 맨살이 많이 남아 실패하는 쪽으로 보여 **번들에서 제외**(3회 결과, 확정 아님). 같은 이유로 남성 번들을 만들 때도 제외한다. Ukrainian Pysanka는 미시험.
- 남성 체형 미소년 번들은 아직 없음(제안 단계).

### 60-5. 트리오/혼합 트리오 후속
- 트리오 세로 문구 결과: 1~4번 1차 성공(1번만 가로로 나옴), 5번 미보고. 혼합 트리오(`mk_mixed_trio3.py`, 여성 / 남성 얼굴+여성 체형 / 남성)는 성공으로 확인, 번들화는 미정.
- 번들의 트리오는 `THREE people standing close side by side, shoulder to shoulder in a single row` + `the whole row filling the width of the tall frame` + `Vertical 2:3 …` 문구를 포함한다.

### 60-6. 교훈
- 얼굴 문구는 남성 체형이 아닌 **여성 체형 위에서** 훨씬 쉽게 여성화된다(체형·헤어·주얼리·손톱이 함께 끌어당김). 남성 앵커(굵은 눈썹·턱선·목젖·옅은 수염)가 필요하고, 미소년 문구는 일부만 변주로 둔다.
- 체형 풀은 "여성 체형으로 읽히느냐"가 기준이다. 부피가 큰 체형은 남성 얼굴과 조합하면 성별 느낌이 약해진다.
- 조합 샘플은 반드시 번들에서 그대로 뽑아 시험한다(5b~5g 모두 번들 추출분).
- 어시스턴트 실수: 샘플 파일 헤더의 개수 표기를 실제와 다르게 쓴 것(솔로·듀오·트리오 수 불일치, 수정함), 트리오 샘플 구성이 의도와 다르게 뽑힌 것(인덱스 선택 후 재추출). 샘플 추출 후에는 `key`로 구성을 확인한다.
- 생성기 부수 수정: `IDOLF` 중복 정의를 정리, `rnd.sample` 대신 셔플 덱으로 체형 균등화, `her` → `his` 치환.

### 60-7. 열린 과제 (v6.62 기준)
- 앱에서 `Male Face Female Body Formula` 카테고리 표시·100개 확인.
- 남성 체형 번들(미소년·아이돌 + 40인치 힐 + 헤어 + 눈 메이크업 + 주얼리 + 긴 손톱, linework 3종 제외) 개수·구성 결정. 혼합 듀오/트리오(여성/남성얼굴 여체/남성) 번들 여부.
- 보류(변동 없음): Core × 소재 프레임 컷, 실버폭스 확장, 철근 전신 카테고리, 네온 튜브, Face Sculpt 축 위치, 티어(HOF/SSS), 앉기 앵클컷 재시험, 4인 이상 피어싱 그룹, 피어싱용 얼굴 크롭 프레임.
- 미보고(건너뛰기로 함): `FrontHeels3`, `FrontThighBoots3(_40in)`, `MaleFaceFemaleBody3(_40in)`, `MaleFaceBustHourglass3_40in`, `MasculineFaceBustHourglass3_40in`, 트리오 세로 5번.
- 백업: `LumineX_generators_backup_2026-10-15c.zip`(이전 세션분). 이후 생성기(`mk_malefacefemale_bundle.py`, `mk_male_boyidol5.py` 등)는 다음 백업에 포함한다. 이전 핸드오프·백업은 삭제하지 않았다.
- 등록 현황: `la_` **16,320** + 레거시 576. 마지막 push `c8dad166`.
