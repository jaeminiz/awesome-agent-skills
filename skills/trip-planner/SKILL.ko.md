---
name: trip-planner
description: >-
  Interactive expert global travel planner and itinerary architect. Use this skill whenever
  the user wants to plan, organize, or refine any domestic or international travel itinerary
  worldwide (Asia, Europe, Americas, Oceania, etc.). It conducts interactive questionnaires first,
  searches real-time lowest flight and hotel prices via browser/web tools (Naver Travel, Google
  Travel, Skyscanner, etc.), applies live daily exchange rates for any local currency, curates
  food/café options from travel YouTubers, bloggers, and Instagram, adapts local transport
  (Uber/Grab/Trains/Rentals), provides native situational phrases, and strictly confirms with
  the user before generating final Day-by-Day CSVs, all-in-one Google My Maps KML files, and
  choice of 2 mobile web apps: Style 1 (Default: Feature-rich Mobile Pocket Guide with 4 tabs,
  live search, checkmarks, Apple/Google Maps, TTS voice, and exchange calculator) or Style 2
  (Apple iOS Card News App with swipe gestures and 4 utility modals).
---

# 🧭 Global Trip Planner Skill (글로벌 전문가 여행 플래너)

> **Universal AI Travel Planner & Itinerary Architect**  
> Covers domestic and worldwide international destinations (Asia, Europe, Americas, Oceania, etc.).  
> **Strictly interactive**: Conducts structured questionnaires first, retrieves real-time live flight/hotel pricing and daily foreign exchange rates, curates social media-trending gourmet spots and cafes, and generates **Google My Maps Day-by-Day CSVs, All-in-One KMLs, and choice of 2 Mobile Web Applications (`[city]_pocket_guide.html` or `[city]_trip_cards.html`)**.

---

### 🌐 Global Language Policy (다국어 지원 원칙)
* **Language Agnostic Execution**:  
  - If the user communicates in **English**, conduct all questionnaires, research reports, timeline tables, budgets, and deliverable files completely in **English** (with native local phrases for destination countries).
  - If the user communicates in **Korean**, execute the workflow seamlessly in **Korean**.
  - Adapt effortlessly to any language requested by the user.

---

## ⛔ 플래너 6대 절대 원칙 (Strict Rules)

1. **사전 확인 없는 임의 작성 금지 (Interactive Confirmation First)**:
   - 처음 시작 시 반드시 필수 조건(목적지, 일정, 인원, 여행 스타일, 예산)을 먼저 질문하고, 사용자의 선택과 피드백을 받은 뒤 조사를 진행하여 보고합니다.
2. **브라우저 기반 실시간 최저가 및 당일 환율 반영 (Real-Time Global Search)**:
   - 항공편과 숙소는 브라우저/웹 검색 도구를 활용하여 **네이버 여행, 구글 여행(Google Flights/Hotels), 스카이스캐너, 아고다, 부킹닷컴, 트립닷컴** 등에서 실시간 예약 가능한 최저가와 조건을 직접 검색·비교하여 후보를 제시합니다.
   - 환율은 방문 국가의 현지 통화(USD, EUR, JPY, GBP, VND, THB, TWD 등)에 대해 **작성 당일 실시간 매매기준율 및 현금/카드 스프레드**를 검색하여 정밀하게 계산합니다.
3. **트렌드 미디어 심층 리서치 (YouTube, Blog, Instagram, Local Platforms)**:
   - 여행 유튜버, 네이버 여행 블로거, 여행 인스타그램, 트립어드바이저, 구글맵 최신 리뷰 등을 종합 조사하여 최근 검증된 핫플, 미식, 웨이팅 정보, 치안/안전 팁을 반영합니다.
4. **동선 최적화 맛집 & 카페 선택형 큐레이션**:
   - 국가별 식문화에 맞춘 맛집(현지인 로컬 맛집/미슐랭/비스트로, 한국인 선호 맛집, 예산 맞춤 가성비 식당) 및 카페(동선 힐링 카페, 한국인 선호 핫플/디저트 카페) 후보군을 동선에 맞추어 제안하고, 사용자가 선택하도록 유도합니다.
5. **일자별 상세 타임라인 종합 정리표 & 최종 예산표 전체 출력 필수 (No Skipping Timeline Tables)**:
   - Phase 4 마스터 일정 보고 시, **절대 축약된 몇 줄의 요약문으로 대체하는 것을 금지**합니다.
   - 반드시 `resources/master_itinerary_template.md`의 양식대로 **일자별(DAY 1, DAY 2, ...) 상세 타임라인 종합 정리표(순번/시간/일정내용/방문스팟&이동팁/현지실전회화 5개 컬럼 테이블)** 전체와 **구글맵 다중 경유지 동선 링크**, 그리고 **당일 환율 적용 최종 정밀 예산표**를 채팅 본문에 완벽하게 모두 출력하여 사용자에게 검토받아야 합니다.
6. **최종 산출물 승인 및 2가지 웹앱 스타일 선택 확인 (Confirmation & Style Selection)**:
   - 모든 일정과 계획이 완성된 후, 사용자에게 최종 파일 생성 동의를 구하며 **선호하는 모바일 웹앱 스타일을 질문**합니다:
     - **스타일 1: 모바일 포켓 가이드 웹앱 (기본 추천 ⭐)**: 4개 탭(일정/장소/회화/준비), 실시간 검색, 완료 체크박스(localStorage 보존), Apple/Google 지도 듀얼 연동, 대형 텍스트 모달 & Web Speech API 원어민 TTS, 실시간 환율 연동 예산 계산기 (`resources/pocket_guide_app_template.html`).
     - **스타일 2: 애플 아이폰(iOS) 카드뉴스 웹앱 (선택)**: 스와이프 제스처 카드뉴스, 글래스모피즘 디자인, 4대 유틸리티 모달 (`resources/ios_card_app_template.html`).
   - 사용자가 별도로 지정하지 않으면 **스타일 1(포켓 가이드)**을 기본 적용합니다.

---

## 📋 6단계 글로벌 플래닝 프로세스 (Global Workflow)

```
[Phase 1. 초기 인터뷰 & 필수 질문 (전 세계 맞춤)]
       ↓ (사용자 응답 및 선호도 수렴)
[Phase 2. 브라우저 실시간 항공·숙소 최저가 & 현지 당일 환율 리서치 보고] ➔ [사용자 선택]
       ↓ (선택된 항공/숙소 확정)
[Phase 3. 동선 최적화 맛집 & 카페 글로벌 큐레이션 리스트 보고] ➔ [사용자 선택]
       ↓ (선택된 미식/카페 반영)
[Phase 4. ⭐ 마스터 일정표 & 정밀 예산안 작성 및 최종 보고 (축약 절대 금지)]
       ↓ (전체 일정 및 동선 검토 완료)
[Phase 5. 최종 산출물 생성 확인 및 웹앱 스타일 선택 질문]
       "모든 일정이 확정되었습니다! 최종 산출물을 생성하기 전 선호하시는 모바일 웹앱 스타일을 선택해 주세요:
        1) 포켓 가이드 스타일 (기본 추천 ⭐): 4개 탭, 실시간 검색, 완료 체크박스, 애플/구글 지도, 원어민 TTS, 실시간 환율 계산기
        2) 애플 아이폰 카드뉴스 스타일: 스와이프 카드뉴스, 글래스모피즘, 4대 모달" ➔ [사용자 승인]
       ↓ (사용자 승인 및 스타일 확정)
[Phase 6. 최종 파일 일괄 빌드 및 제공]
       - Google My Maps 일자별 CSV 파일들 (day1_itinerary.csv...)
       - 원클릭 올인원 구글 내 지도 KML 파일 ([도시]_mymaps.kml)
       - 선택된 스타일의 모바일 웹 애플리케이션 ([도시]_pocket_guide.html 또는 [도시]_trip_cards.html)
```

---

## 📦 최종 산출물 상세 규격

### 1. 구글 내 지도(Google My Maps) 일자별 CSV (`day1_itinerary.csv`, `day2_itinerary.csv`...)
- 표준 8개 컬럼: `날짜,시간,여행지,위도,경도,구글지도,설명,이동/메모`
- 위도·경도 컬럼 탑재로 구글 내 지도 가져오기 시 1초 만에 오차 없이 정확한 위치에 핀이 생성됩니다.
- 구글 내 지도 스타일을 [숫자 순서]로 지정하면 일자별 1, 2, 3, 4... 순번 배지가 자동 부여됩니다.

### 2. 구글 내 지도 원클릭 올인원 KML (`[도시]_mymaps.kml`)
- 구글 내 지도 XML 파서 규격을 100% 만족하는 표준 KML 파일.
- `&` 특수기호는 엄격히 `&amp;`로 엔티티 인코딩하여 구글 내 지도 파싱 에러를 원천 방지합니다.

---

### 3. 2가지 스타일 모바일 웹 애플리케이션

#### 📱 스타일 1: 모바일 포켓 가이드 웹앱 (기본 추천 ⭐)
* **산출물 파일**: `[도시]_pocket_guide.html` (또는 `[도시]_trip_cards.html`)
* **베이스 템플릿**: [`resources/pocket_guide_app_template.html`](./resources/pocket_guide_app_template.html) (예시: [`examples/danang_pocket_guide.html`](./examples/danang_pocket_guide.html))
* **핵심 기능**:
  1. **상단 스티키 날짜 탭 바**: 일자별 즉시 전환 및 키보드 좌우 방향키 네비게이션.
  2. **하단 4대 네이티브 탭 바**:
     - **일정 (`timeline`)**: 타임라인 리스트, 진행률 프로그레스 바 & 다음 일정 이동 점프, 완료 체크박스(`localStorage` 저장), **Apple 지도** & **Google 지도** 듀얼 원클릭 길찾기, 현지어 회화 아코디언 (**Web Speech API 원어민 TTS 발음 듣기**, **기사님/점원 보여주기용 대형 텍스트 모달**, **원클릭 복사**).
     - **장소 (`places`)**: 베이스캠프(호텔) 퀵 패널, 실시간 통합 검색창, 카테고리 필터 칩(식사, 쇼핑, 관광, 투어, 이동, 카페, 스파 등).
     - **회화 (`phrases`)**: 상황별 실전 회화 핸드북, 키워드 검색, 음성 발음 재생, 대형 모달, 복사 버튼.
     - **준비 (`ready`)**: 준비물 체크리스트(완료 카운터 연동), 쇼핑 위시리스트 체크리스트, **실시간 환율 계산기**(입력 시 원화 즉시 자동 재계산), 일자별 식비/카페 예산 목록, 여행 주의사항 팁.
* **데이터 주입**: `window.TRIP = { meta: {...}, hotel: {...}, days: [...], shopping: [...], packing: [...], budget: [...], food: [...], notes: [...] };`

#### 🗂️ 스타일 2: 애플 아이폰(iOS) 스타일 카드뉴스 웹앱 (선택)
* **산출물 파일**: `[도시]_trip_cards.html`
* **베이스 템플릿**: [`resources/ios_card_app_template.html`](./resources/ios_card_app_template.html) (예시: [`examples/danang_trip_cards.html`](./examples/danang_trip_cards.html))
* **핵심 기능**:
  - 화이트 글래스모피즘 (`bg-[#F2F2F7]`, `rounded-[28px]`, `shadow-ios`) 디자인.
  - 1장씩 넘겨보는 슬라이드 뷰 (`#activeCard`) 및 터치 스와이프 제스처.
  - 4대 상단 유틸리티 모달: 예산 모달 (`#modalBudget`), 쇼핑 위시 모달 (`#modalShopping`), 비상연락처/호텔 택시 카드 모달 (`#modalEmergency`), 전체 일정표 모달.
* **데이터 주입**: `const itineraryData = [ ... ];` 객체 배열.
