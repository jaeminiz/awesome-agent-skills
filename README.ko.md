# 🌟 Awesome Agent Skills

[![Version](https://img.shields.io/badge/version-v1.4.2-emerald)](https://github.com/jaeminiz/awesome-agent-skills/releases/tag/v1.4.2)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/jaeminiz/awesome-agent-skills/pulls)
[![skills.sh](https://img.shields.io/badge/skills.sh-trip--planner-black)](https://www.skills.sh/jaeminiz/awesome-agent-skills/trip-planner)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/jaeminiz/awesome-agent-skills)

**[English](README.md)** | **한국어**

> **Google Antigravity 및 차세대 AI 에이전트 환경을 위한 프로덕션급 에이전트 스킬(Agent Skills) 모음**  
> 실전 업무 자동화, 여행 기획, 데이터 분석 등 에이전트의 역량을 극대화하는 검증된 스킬을 체계적으로 제공합니다.

---

## 🧭 스킬 디렉터리 (Skills Directory)

| 카테고리 | 스킬 이름 | 버전 | 핵심 설명 | 바로가기 |
| :--- | :--- | :---: | :--- | :---: |
| ✈️ **Travel & Lifestyle** | [`trip-planner`](skills/trip-planner) | `v1.4.2` | **글로벌 전문가 여행 플래너 & 일정 아키텍트**<br>• 인터랙티브 단계별 문답 & 브라우저 실시간 최저가·환율 탐색<br>• 미디어 트렌드 맛집 & 카페 큐레이션<br>• **일자별 상세 타임라인 종합 정리표(5개 컬럼)** & 정밀 예산표<br>• **구글 내 지도(Google My Maps) 표준 8컬럼 Day별 CSV & 올인원 KML** 자동 생성<br>• **애플 아이폰(iOS) 스타일 카드뉴스 웹앱 (표준 템플릿 레이아웃 100% 고정)** 자동 빌드 | [바로가기](skills/trip-planner) |

---

## 🏆 대표 스킬 소개 (Featured Skills): `trip-planner` (`v1.4.2`)

### 🧭 [trip-planner](skills/trip-planner) — 글로벌 전문가 여행 플래너

전 세계 모든 국내외 여행지를 아우르는 전문 여행 플래너 및 일정 아키텍트 스킬입니다.

* **6대 절대 원칙 (Strict Rules)**: 사전 확인 없는 임의 작성 금지, 브라우저 기반 실시간 최저가 및 당일 환율 반영, 트렌드 미디어 심층 리서치, 일자별 상세 타임라인 종합 정리표 & 최종 예산표 전체 출력 필수, 최종 산출물 생성 전 필수 사용자 확인, iOS 카드뉴스 웹앱 표준 템플릿 양식·레이아웃·4대 모달·`itineraryData` 스키마 절대 보존.
* **3대 핵심 산출물**:
  1. **구글 내 지도(Google My Maps) Day별 분리 8컬럼 CSV (`day1_itinerary.csv`, `day2_itinerary.csv`...)**:  
     표준 8컬럼(`날짜,시간,여행지,위도,경도,구글지도,설명,이동/메모`) 호환. 정밀 위도/경도 좌표를 포함해 구글 내 지도가 1초 만에 위치를 자동 감지하며, [숫자의 순서] 스타일 선택 시 행 순서대로 `1, 2, 3...` 번호 뱃지 마커가 자동 부여됩니다.
  2. **원클릭 올인원 KML 파일 (`[도시]_mymaps.kml`)**:  
     구글 내 지도(My Maps) 웹 파서에 100% 호환되도록 XML 엔티티(`&amp;`) 정제 및 문법 검증을 마친 KML로 파싱 에러 없이 번호 마커와 상세 팝업이 즉시 등록됩니다.
  3. **애플 아이폰(iOS) 스타일 카드뉴스 웹 애플리케이션 (`[도시]_trip_cards.html`)**:  
     [`resources/ios_card_app_template.html`](skills/trip-planner/resources/ios_card_app_template.html)의 HTML/CSS/4대 모달/JS 엔진(`const itineraryData = [{ id, day, time, title, category, description, phraseKo, phraseJa, phraseMeaning, cost, mapQuery }]`)을 단 1%도 변경하지 않고 그대로 복제하여 생성하는 오프라인 모바일 웹앱 (Web Speech TTS 원어민 발음듣기, 점원 보여주기 대형 모달 `#modalShowJapanese`, 경비 그라데이션 박스+3섹션 `#modalBudget`, 일차 뱃지 위시 카드 `#modalShopping`, 다크 슬레이트 숙소/공항 택시 주소 원클릭 복사 `#modalEmergency` 탑재).

#### 🗺️ 구글 내 지도(Google My Maps) 등록 표준 매뉴얼
* **[방법 A: CSV로 등록 - 권장]**: [구글 내 지도](https://www.google.com/maps/d/) 접속 ➔ **[+ 새 지도 만들기]** ➔ **[가져오기]** 클릭 ➔ `day1_itinerary.csv` (또는 통합 `danang_itinerary.csv`) 업로드 ➔ 자동 감지된 `위도`/`경도` 확인 ➔ 마커 제목 열로 **`여행지`** 선택 ➔ **[기본 스타일]**을 **[숫자의 순서]** + **[라벨: 여행지]**로 변경하면 `1, 2, 3...` 번호 마커 자동 생성.
* **[방법 B: KML로 등록 - 원클릭]**: **[+ 새 지도 만들기]** ➔ **[가져오기]** ➔ `danang_mymaps.kml` 드래그앤드롭 ➔ 파싱 에러 없이 전 일정 핀과 팝업 즉시 등록. *(팁: 이전 세션 캐시로 인한 오류 팝업 발생 시 브라우저를 **F5 새로고침** 후 재시도)*

<p align="center">
  <img src="skills/trip-planner/sample_preview.png" alt="iOS Card News Web App Preview" width="320" style="border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.12);" />
</p>

* 🌐 **[실제 다낭 여행 카드뉴스 웹앱 체험](skills/trip-planner/examples/danang_trip_cards.html)**
* 🗺️ **[구글 내 지도 올인원 KML 샘플](skills/trip-planner/examples/danang_mymaps.kml)**
* 📊 **[구글 내 지도 표준 8컬럼 CSV 샘플](skills/trip-planner/examples/danang_itinerary.csv)**
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