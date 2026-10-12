# 🧭 Global Trip Planner (글로벌 맞춤형 여행 플래너)

> **Antigravity AI 전문 여행 플래너 및 일정 아키텍트 스킬**  
> 전 세계 모든 국내외 여행지를 아우르며, 인터랙티브 문답을 통해 실시간 최저가·환율·트렌드를 반영한 정밀 마스터 일정표, 구글맵 연동 CSV, 그리고 **애플 아이폰(iOS) 스타일 카드뉴스 웹 애플리케이션**을 자동 생성합니다.

---

## 🌟 주요 특징 (Core Features)

1. **인터랙티브 맞춤형 플래닝 (Interactive Planning First)**
   - 일방적으로 일정을 작성하지 않고, 여행 기간, 인원 구성, 이동 방식, 숙소 선호, 여행 테마를 문답을 통해 파악합니다.
2. **실시간 검색 기반 정밀 데이터 (Real-Time Search)**
   - 브라우저 검색을 통해 실시간 항공권/숙소 최저가를 조사하고, 당일 환율(VND, JPY, USD, EUR 등)을 적용해 정밀 예산을 산출합니다.
3. **트렌드 미디어 심층 큐레이션 (Curated Gourmet & Spots)**
   - 여행 유튜버, 블로그, 인스타그램, 미슐랭 가이드 등을 분석하여 검증된 맛집과 감성 카페를 동선별로 큐레이션합니다.
4. **일자별 상세 타임라인 종합 정리표 & 구글맵 연동**
   - 분 단위 동선, 쇼핑 후 짐 정리 타이밍, 현지 맞춤 실전 회화(한글 발음, 원문, 뜻), 구글맵 다중 경유지 원클릭 동선 링크를 완벽 제공합니다.
5. **모바일 최적화 애플 아이폰(iOS) 스타일 카드뉴스 웹앱 (`[도시]_trip_cards.html`)**
   - **1장씩 넘겨보는 카드뉴스 UI**: 화이트 글래스모피즘, 터치 스와이프 제스처, 순번/카테고리 뱃지, 완료 체크 기능 (`localStorage` 연동).
   - **현지어 발음듣기 (TTS)**: 기기 내장 Web Speech API로 원어민 발음 음성 즉시 재생.
   - **기사님/직원 보여주기 모달**: 36px 대형 텍스트 풀스크린 모달.
   - **3대 필수 모달**: 정밀 경비표, 미식/쇼핑 위시리스트 체크리스트, 호텔 주소 복사 & 긴급 연락망 원클릭 전화.
6. **스프레드시트 & 구글 내 지도 연동 CSV (`[도시]_Itinerary.csv`)**
   - 표준 6개 컬럼(`날짜,시간,구분,장소/일정,상세내용,교통/비고`) 호환 파일 생성.

---

## 📋 6단계 글로벌 플래닝 프로세스 (Global Workflow)

```
[Phase 1] 초기 인터뷰 & 필수 질문 (전 세계 맞춤)
       ↓
[Phase 2] 브라우저 실시간 항공·숙소 최저가 & 현지 당일 환율 리서치 보고 ➔ [사용자 선택]
       ↓
[Phase 3] 동선 최적화 맛집 & 카페 글로벌 큐레이션 리스트 보고 ➔ [사용자 선택]
       ↓
[Phase 4] ⭐ 필수 상세 출력 (축약/생략 금지):
          1. 일자별 상세 타임라인 종합 정리표 (테이블 5개 컬럼)
          2. 구글맵 다중 경유지 동선 링크
          3. 당일 환율 적용 최종 정밀 예산표
       ↓
[Phase 5] 최종 산출물 생성 확인 질문 ("CSV와 iOS 카드뉴스 웹앱을 생성해드릴까요?") ➔ [사용자 승인]
       ↓
[Phase 6] [도시]_Itinerary.csv 및 [도시]_trip_cards.html 최종 생성
```

---

## 📂 파일 구조 (Structure)

```
trip-planner/
├── SKILL.md                              # 스킬 메인 명세 및 6대 절대 원칙 가이드라인
├── README.md                             # 스킬 소개 및 사용 가이드
├── references/
│   └── trip_planning_playbook.md         # 권역별(일본/동남아/유럽/미주) 플래닝 플레이북
└── resources/
    ├── master_itinerary_template.md      # 마스터 일정표 표준 Markdown 템플릿
    ├── budget_template.md                # 다통화 환율 및 정밀 예산안 템플릿
    ├── itinerary_template.csv            # 구글 내 지도 및 스프레드시트 호환 CSV 템플릿
    └── ios_card_app_template.html        # Phosphor Icons & TTS 탑재 모바일 웹앱 템플릿
```

---

## 🚀 설치 및 사용법 (Installation)

### 1. Antigravity 글로벌 스킬로 설치
본 저장소를 클론하여 사용자의 Antigravity 글로벌 스킬 디렉터리에 배치합니다:

```bash
# Windows
git clone https://github.com/jaeminiz/awesome-agent-skills.git
Copy-Item -Path "awesome-agent-skills\skills\trip-planner" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force

# macOS / Linux
git clone https://github.com/jaeminiz/awesome-agent-skills.git
cp -r awesome-agent-skills/skills/trip-planner ~/.gemini/config/skills/
```

### 2. 프로젝트 전용 스킬로 설치
특정 워크스페이스에서만 사용할 경우 프로젝트 루트의 `.agents/skills/`에 배치합니다:

```bash
cp -r awesome-agent-skills/skills/trip-planner .agents/skills/
```

### 3. 실행 방법
Antigravity 에이전트와 대화 시 언제든 자연어로 요청하세요:
- *"다낭 3박 4일 여행 계획 세워줘"*
- *"도쿄 4박 5일 맛집 중심 일정 짜줘"*
- *"파리·런던 7박 8일 신혼여행 플랜 작성해줘"*

---

## 📄 라이선스 (License)

MIT License. 누구나 자유롭게 수정 및 확장하여 사용하실 수 있습니다.
