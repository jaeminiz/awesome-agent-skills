# ⚡ Awesome Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/jaeminiz/awesome-agent-skills/pulls)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/jaeminiz/awesome-agent-skills)

> **Google Antigravity 및 차세대 AI 코딩·에이전트 환경을 위한 고성능 프로덕션급 에이전트 스킬(Agent Skills) 모음집**  
> 복잡한 실무 작업, 여행 기획, 데이터 분석 등을 전문 에이전트 수준으로 자동화하는 재사용 가능한 스킬들을 중앙에서 체계적으로 관리합니다.

---

## 📚 스킬 디렉터리 (Skills Directory)

| 카테고리 | 스킬 이름 | 설명 | 바로가기 |
| :--- | :--- | :--- | :---: |
| 🧭 **Travel & Lifestyle** | **`trip-planner`** | **글로벌 전문가 여행 플래너 & 일정 아키텍트**<br>• 인터랙티브 단계별 문답 및 실시간 최저가·당일 환율 검색<br>• 동선 최적화 맛집 & 카페 큐레이션<br>• **일자별 상세 타임라인 종합 정리표(5개 컬럼)** 및 정밀 예산표<br>• 구글맵 연동 CSV 및 **애플 아이폰(iOS) 스타일 카드뉴스 웹앱** 자동 생성 | [보러가기](skills/trip-planner) |

---

## 🌟 대표 스킬 소개 (Featured Skills)

### 🧭 [trip-planner](skills/trip-planner) — 글로벌 전문가 여행 플래너

전 세계 모든 국내외 여행지를 아우르는 전문 여행 플래너이자 일정 아키텍트 스킬입니다.

* **6대 절대 원칙 (Strict Rules)**: 사전 확인 없는 임의 작성 금지, 브라우저 기반 실시간 최저가·환율 반영, 일자별 상세 타임라인 종합 정리표 & 최종 예산표 전체 출력 필수, 최종 산출물 생성 전 사용자 승인 필수.
* **핵심 산출물**:
  1. `[도시]_Itinerary.csv`: 스프레드시트 및 구글 내 지도(Google My Maps) 100% 호환 파일.
  2. `[도시]_trip_cards.html`: 스마트폰 Safari/Chrome에서 오프라인으로 동작하는 애플 iOS 스타일 글래스모피즘 카드뉴스 웹 애플리케이션 (Web Speech TTS 원어민 발음듣기, 기사님 보여주기 모달, 구글지도 원클릭 연동, 경비/위시/비상 모달 탑재).

```
awesome-agent-skills/
└── skills/
    └── trip-planner/
        ├── SKILL.md                          # 스킬 메인 명세 및 6대 절대 원칙
        ├── README.md                         # 스킬 상세 가이드
        ├── references/
        │   └── trip_planning_playbook.md     # 권역별 플래닝 가이드라인
        └── resources/
            ├── master_itinerary_template.md  # 마스터 일정표 Markdown 템플릿
            ├── budget_template.md            # 정밀 예산표 템플릿
            ├── itinerary_template.csv        # 구글맵 연동 CSV 템플릿
            └── ios_card_app_template.html    # Phosphor Icons & TTS 탑재 모바일 웹앱 템플릿
```

---

## 🚀 설치 및 사용 가이드 (Installation)

### 1. 전체 저장소 클론
```bash
git clone https://github.com/jaeminiz/awesome-agent-skills.git
```

### 2. Antigravity 글로벌 스킬로 등록
원하는 스킬 폴더를 Antigravity 글로벌 스킬 경로로 복사합니다:

```bash
# Windows
Copy-Item -Path "awesome-agent-skills\skills\trip-planner" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force

# macOS / Linux
cp -r awesome-agent-skills/skills/trip-planner ~/.gemini/config/skills/
```

### 3. 특정 프로젝트 전용 스킬로 등록
현재 작업 중인 프로젝트 워크스페이스에만 적용하고 싶은 경우:

```bash
# 프로젝트 루트의 .agents/skills/ 경로에 배치
mkdir -p .agents/skills
cp -r awesome-agent-skills/skills/trip-planner .agents/skills/
```

---

## 🛠️ 새로운 스킬 기여 방법 (Contributing)

새로운 유용한 에이전트 스킬 추가를 언제나 환영합니다!

1. 본 저장소를 Fork 합니다.
2. `skills/<스킬-이름>/` 디렉터리를 생성하고 필수 명세 파일(`SKILL.md`)을 작성합니다.
   ```
   skills/my-awesome-skill/
   ├── SKILL.md            # YAML frontmatter (name, description) 및 상세 행동 지침
   ├── README.md           # 스킬 소개 및 사용 예시
   └── resources/          # 필요한 템플릿, 스크립트, 에셋
   ```
3. 루트 `README.md`의 [스킬 디렉터리](#-스킬-디렉터리-skills-directory) 테이블에 새 스킬을 등록합니다.
4. Pull Request(PR)를 제출해 주세요!

---

## 📄 라이선스 (License)

이 프로젝트는 [MIT License](LICENSE)에 따라 자유롭게 사용 및 배포할 수 있습니다.
