`trip-planner`는 Google Antigravity, Claude Code, OpenAI Codex 등 최신 AI 코딩 에이전트 환경에서 동작하는 오픈소스 **여행 기획 및 일정 아키텍처 스킬(Agent Skill)**입니다.

단순 텍스트 나열에 그쳤던 기존 AI 여행 일정 생성 방식에서 벗어나, 인터랙티브 인터뷰를 통한 취향 분석, 실시간 최저가·환율 검색, 그리고 **구글 내 지도(Google My Maps) 올인원 KML과 스마트폰 오프라인 카드뉴스 웹앱**을 자동으로 생성합니다.

---

## 📌 주요 특징

* **인터랙티브 사전 인터뷰 (Interactive First):** 일정을 임의로 바로 짜지 않고, 사용자의 목적지, 일정, 인원 구성, 숙소 선호, 이동 수단 등을 사전에 체계적으로 파악한 뒤 플래닝을 시작합니다.
* **실시간 데이터 탐색:** 브라우저/웹 검색 도구를 활용하여 항공권 및 숙소의 실시간 최저가를 조회하고, 여행 대상국의 당일 실시간 환율을 반영하여 정밀 예산을 계산합니다.
* **미디어 트렌드 큐레이션:** 유튜브, 여행 블로그, 인스타그램, 구글맵 최신 리뷰를 기반으로 검증된 동선별 맛집과 카페를 큐레이션합니다.
* **분 단위 타임라인 마스터 테이블:** 축약 없이 시간대, 장소, 동선 팁, 현지 실전 회화가 포함된 5개 컬럼의 상세 일정표를 제공합니다.
* **다국어 지원 (Language-Agnostic):** 한국어 사용자는 물론 영문 사용자에게도 완벽하게 대응합니다.

---

## 📦 최종 산출물 규격

일정 협의가 완료되면 에이전트가 직접 아래의 실전 파일들을 빌드하여 제공합니다:

| 산출물 | 파일 형식 | 주요 기능 및 특징 |
| :--- | :---: | :--- |
| **구글 내 지도 올인원 KML** | `[도시]_mymaps.kml` | 구글 내 지도(My Maps)에 단 1번 가져오기로 **일자별 레이어 폴더 분리 + 1, 2, 3번 번호 핀 + 일차별 이동 경로 폴리라인(LineString)** 자동 생성 |
| **표준 6컬럼 분리 CSV** | `day1_itinerary.csv` ... | `날짜,시간,여행지,구글지도,설명,이동/메모` 표준 6컬럼으로 구성되어 구글 지도 레이어별 가져오기 및 엑셀 관리 가능 |
| **iOS 스타일 카드뉴스 웹앱** | `[도시]_trip_cards.html` | 스마트폰 Safari/Chrome에서 오프라인 동작하는 화이트 글래스모피즘 웹앱. **터치 스와이프, Web Speech TTS 원어민 발음듣기, 36px 기사님 보여주기 모달, 원클릭 구글맵 연동, 경비/위시/비상 연락망 모달** 탑재 |

---

## 🚀 설치 방법

글로벌 에이전트 스킬 표준 규격(`skills`)을 준수하여 터미널에서 명령어 한 줄로 설치할 수 있습니다.

### 1. Universal CLI 설치 (추천)

```bash
npx skills add https://github.com/jaeminiz/awesome-agent-skills --skill trip-planner
```

*(Google Antigravity, Claude Code, Codex, Cursor, Cline 등 지원 환경에 자동 구성됩니다.)*

### 2. 저장소 직접 등록 (수동 설치)

```bash
# Antigravity 글로벌 스킬 경로로 복사 (Windows PowerShell)
Copy-Item -Path "awesome-agent-skills\skills\trip-planner" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force
```

---

## 🛠️ 플래닝 워크플로우 (6-Phase)

1. **Phase 1 (초기 인터뷰):** 여행 기간, 인원(아이/부모님/친구), 선호 이동 수단, 숙소 스타일 수렴
2. **Phase 2 (실시간 리서치):** 브라우저 기반 실시간 항공·숙소 최저가 및 당일 환율 보고 ➔ 사용자 선택
3. **Phase 3 (동선 큐레이션):** 권역별 검증된 맛집 및 카페 후보군 제시 ➔ 사용자 선택
4. **Phase 4 (상세 타임라인 보고):** 분 단위 5컬럼 일정표, 다중 경유지 구글맵 링크, 정밀 예산표 전체 출력
5. **Phase 5 (산출물 확인):** KML, CSV, 모바일 웹앱 파일 생성 여부 사용자 최종 승인
6. **Phase 6 (파일 빌드):** `[도시]_mymaps.kml`, Day별 CSV, `[도시]_trip_cards.html` 생성 완료

---

## 💬 실제 실행 대화 예시

스킬을 설치한 후 에이전트에게 여행 계획을 요청하면 아래와 같이 체계적으로 문답이 진행됩니다:

> **사용자:**  
> "11월에 부모님 모시고 3박 4일 도쿄 효도 여행 가려고 해. 일정 짜줘."
>
> **에이전트 (trip-planner 가동):**  
> "부모님과의 도쿄 여행 일정을 기획하겠습니다. 편안한 동선과 맞춤형 플래닝을 위해 먼저 5가지를 여쭙겠습니다:  
> 1. 원하시는 항공편 시간대(오전 출발/저녁 복귀 등)  
> 2. 선호하시는 숙소 위치(긴자, 신주쿠, 도쿄역 등 온천/대욕장 필요 여부)  
> 3. 하루 보행량 및 이동 수단(지하철 위주 vs 택시/프라이빗 밴 병행)  
> 4. 식사 스타일(웨이팅 없는 예약제 고급 식당, 가이세키, 스시 등)  
> 5. 꼭 방문하고 싶으신 핵심 명소나 위시리스트"

위 문답을 거친 뒤 실시간 최저가 검색 ➔ 동선 최적화 맛집 큐레이션 ➔ 구글 내 지도 KML 및 스마트폰용 카드뉴스 웹앱 빌드까지 원스톱으로 이어집니다.

---

## 🔗 관련 링크

* **공식 GitHub 저장소:** [https://github.com/jaeminiz/awesome-agent-skills](https://github.com/jaeminiz/awesome-agent-skills)
* **skills.sh 등록 페이지:** [https://www.skills.sh/jaeminiz/awesome-agent-skills/trip-planner](https://www.skills.sh/jaeminiz/awesome-agent-skills/trip-planner)
* **실제 다낭 4일 생성 샘플:** [저장소 예시 폴더(examples/) 바로가기](https://github.com/jaeminiz/awesome-agent-skills/tree/main/skills/trip-planner/examples)
* **라이선스:** MIT License (자유로운 개인 및 상용 활용 가능)
