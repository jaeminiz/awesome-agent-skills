# 🌟 Awesome Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/jaeminiz/awesome-agent-skills/pulls)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/jaeminiz/awesome-agent-skills)

> **Google Antigravity 및 차세대 AI 에이전트 환경을 위한 프로덕션급 에이전트 스킬(Agent Skills) 모음**  
> 실전 업무 자동화, 여행 기획, 데이터 분석 등 에이전트의 역량을 극대화하는 검증된 스킬을 체계적으로 제공합니다.

---

## 🧭 스킬 디렉터리 (Skills Directory)

| 카테고리 | 스킬 이름 | 핵심 설명 | 바로가기 |
| :--- | :--- | :--- | :---: |
| ✈️ **Travel & Lifestyle** | [`trip-planner`](skills/trip-planner) | **글로벌 전문가 여행 플래너 & 일정 아키텍트**<br>• 인터랙티브 단계별 문답 & 브라우저 실시간 최저가·환율 탐색<br>• 미디어 트렌드 맛집 & 카페 큐레이션<br>• **일자별 상세 타임라인 종합 정리표(5개 컬럼)** & 정밀 예산표<br>• **구글 내 지도(Google My Maps) 표준 6컬럼 Day별 CSV & 올인원 KML** 자동 생성<br>• **애플 아이폰(iOS) 스타일 카드뉴스 웹앱** 자동 빌드 | [바로가기](skills/trip-planner) |

---

## 🏆 대표 스킬 소개 (Featured Skills)

### 🧭 [trip-planner](skills/trip-planner) — 글로벌 전문가 여행 플래너

전 세계 모든 국내외 여행지를 아우르는 전문 여행 플래너 및 일정 아키텍트 스킬입니다.

* **6대 절대 원칙 (Strict Rules)**: 사전 확인 없는 임의 작성 금지, 브라우저 기반 실시간 최저가 및 당일 환율 반영, 트렌드 미디어 심층 리서치, 일자별 상세 타임라인 종합 정리표 & 최종 예산표 전체 출력 필수, 최종 산출물 생성 전 필수 사용자 확인.
* **3대 핵심 산출물**:
  1. **구글 내 지도(Google My Maps) Day별 분리 CSV (`day1_itinerary.csv`, `day2_itinerary.csv`...)**:  
     표준 6컬럼(`날짜,시간,여행지,구글지도,설명,이동/메모`) 호환. 구글 내 지도에서 [숫자의 순서] 스타일 선택 시 행 순서대로 `1, 2, 3...` 번호 뱃지 마커 자동 부여.
  2. **원클릭 올인원 KML 파일 (`[도시]_mymaps.kml`)**:  
     구글 내 지도(My Maps)에서 단 1번의 [가져오기]로 **일자별 레이어 폴더 분리 + 1,2,3번 번호 마커 + 일차별 동선 연결선(`N일차 이동 경로`, LineString 테마 색상)**까지 1초 만에 한 방에 자동 완성.
  3. **애플 아이폰(iOS) 스타일 카드뉴스 웹 애플리케이션 (`[도시]_trip_cards.html`)**:  
     스마트폰 Safari/Chrome에서 오프라인으로 완벽 동작하는 글래스모피즘 모바일 웹앱 (Web Speech TTS 원어민 발음듣기, 36px 기사님 보여주기 모달, 구글지도 원클릭 연동, 경비/위시/비상 3대 모달 탑재).

<p align="center">
  <img src="skills/trip-planner/sample_preview.png" alt="iOS Card News Web App Preview" width="320" style="border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.12);" />
</p>

* 🌐 **[실제 다낭 여행 카드뉴스 웹앱 체험](skills/trip-planner/examples/danang_trip_cards.html)**
* 🗺️ **[구글 내 지도 올인원 KML 샘플](skills/trip-planner/examples/danang_mymaps.kml)**
* 📊 **[구글 내 지도 표준 6컬럼 CSV 샘플](skills/trip-planner/examples/danang_itinerary.csv)**
* 📖 **[trip-planner 스킬 상세 안내 및 활용법](skills/trip-planner/)**

---

## 🚀 설치 및 사용 가이드 (Installation)

### 1. 저장소 클론
```bash
git clone https://github.com/jaeminiz/awesome-agent-skills.git
```

### 2. Antigravity 글로벌 스킬로 등록
원하는 스킬 폴더를 Antigravity 글로벌 스킬 경로로 복사합니다:

```bash
# Windows (PowerShell)
Copy-Item -Path "awesome-agent-skills\skills\trip-planner" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force

# macOS / Linux
cp -r awesome-agent-skills/skills/trip-planner ~/.gemini/config/skills/
```

### 3. 특정 프로젝트 전용 스킬로 등록
특정 작업 공간(프로젝트 워크스페이스)에서만 적용하고 싶을 때:

```bash
# 프로젝트 루트의 .agents/skills/ 경로에 배치
mkdir -p .agents/skills
cp -r awesome-agent-skills/skills/trip-planner .agents/skills/
```

---

## 🤝 새로운 스킬 기여 안내 (Contributing)

새로운 고품질 에이전트 스킬 추가 기여를 언제나 환영합니다!

1. 본 저장소를 Fork 합니다.
2. `skills/<스킬-이름>/` 디렉터리를 생성하고 필수 명세서(`SKILL.md`)를 작성합니다.
   ```
   skills/my-awesome-skill/
   ├── SKILL.md            # YAML frontmatter (name, description) 및 상세 행동 지침
   ├── README.md           # 스킬 소개 및 사용법 안내
   ├── references/         # (선택) 상세 참조 가이드 및 플레이북
   └── resources/          # (선택) 템플릿, 자동화 스크립트, 데이터 에셋
   ```
3. 루트 `README.md`의 [스킬 디렉터리](#-스킬-디렉터리-skills-directory) 테이블에 해당 스킬을 등록합니다.
4. Pull Request(PR)를 제출해 주세요!

---

## 📄 라이선스 (License)

본 프로젝트는 [MIT License](LICENSE)에 따라 자유롭게 사용 및 기여하실 수 있습니다.