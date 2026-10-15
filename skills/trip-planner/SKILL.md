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
  mobile-optimized Apple iPhone (iOS) style card news web applications.
---

# 🧭 Global Trip Planner

**Universal AI Travel Planner & Itinerary Architect for Agentic Frameworks.**  
Covers domestic and worldwide international destinations (Asia, Europe, Americas, Oceania, etc.).  
**Strictly interactive**: Conducts structured questionnaires first, retrieves real-time live flight/hotel pricing and daily foreign exchange rates, curates social media-trending gourmet spots and cafes, and generates **Google My Maps Day-by-Day CSVs, All-in-One KMLs, and mobile-optimized Apple iPhone (iOS) style card news web applications (`[city]_trip_cards.html`)**.

---

## 🌐 Multilingual & Language-Agnostic Execution Policy

This skill automatically adapts to the user's preferred language:
* **English Conversation**: Conducts all questionnaires, pricing reports, detailed timeline tables, budget breakdowns, and deliverable files in **English** (with native local phrases for destination countries).
* **Korean Conversation (한국어 대응)**: 사용자가 한국어로 질문하거나 요청할 경우, 모든 문답과 마스터 일정표, 예산안, 산출물을 **한국어**로 정밀하게 작성합니다.
* **Any Other Language**: Adapts effortlessly to Spanish, Japanese, Chinese, French, German, etc.

---

## ⛔ 6 Strict Planner Rules

1. **Interactive Confirmation First (No Arbitrary Guessing)**:
   - Clarify essential conditions (destination, duration, travel party composition, travel style, and budget) through structured dialogue before drafting any itinerary.
2. **Real-Time Global Search (Live Pricing & Daily Exchange Rates)**:
   - Use browser search tools to inspect real-time bookable flight/hotel options on platforms like Google Flights, Skyscanner, Agoda, Booking.com, and Naver Travel.
   - Apply live daily exchange rates (USD, EUR, JPY, GBP, VND, THB, TWD, etc.) for accurate multi-currency budget calculations.
3. **Media-Driven Deep Trend Research (YouTube, Blogs, Instagram, Google Reviews)**:
   - Conduct cross-platform trend analysis to curate verified local hotspots, food scenes, waiting time estimates, and safety tips.
4. **Route-Optimized Gourmet & Cafe Curation**:
   - Provide selective options tailored to daily travel paths (authentic local eateries, Michelin/bistros, traveler favorites, and scenic healing cafes) and let the user pick their favorites.
5. **Mandatory 5-Column Detailed Timeline Table & Precision Budget (No Abbreviations)**:
   - When presenting the Master Itinerary (Phase 4), **never provide a summarized or shortened overview**.
   - Output full minute-by-minute timeline tables (`No. | Time | Activity Details | Spots & Transit Tips | Situational Local Phrases`) along with multi-stop Google Maps route links and complete budget breakdowns.
6. **Explicit User Confirmation Before File Generation**:
   - Before writing any final files, explicitly ask:  
     `"All itinerary details are confirmed. Would you like me to generate the Google My Maps Day-by-Day CSV files, the One-Click All-in-One KML file, and the mobile Apple iPhone (iOS) style card news web app?"`  
   - Only generate the files after the user gives explicit approval.

---

## 📋 6-Phase Global Workflow

```
[Phase 1] Initial Interview & Mandatory Questionnaire (Customized by destination)
       ↓
[Phase 2] Real-Time Flight & Hotel Live Pricing & Daily Exchange Rate Report ➔ [User Selection]
       ↓
[Phase 3] Route-Optimized Gourmet & Scenic Spot Curated List ➔ [User Selection]
       ↓
[Phase 4] ⭐ Comprehensive Master Output (Never abbreviated):
          1. Detailed minute-by-minute timeline table (5 columns per day)
          2. Multi-stop Google Maps transit route links
          3. Daily exchange rate applied precision budget breakdown
       ↓
[Phase 5] Explicit User Confirmation ("Would you like me to generate CSVs, KML, and iOS Card Web App?") ➔ [User Approval]
       ↓
[Phase 6] Final File Generation: Day-by-Day CSVs, [City]_mymaps.kml, and [City]_trip_cards.html
```

---

## 📦 Multi-Modal Deliverables

### 1. Google My Maps Day-by-Day CSVs (`day1_itinerary.csv`, `day2_itinerary.csv`...)
* Standard 6-column format: `Date,Time,Place,GoogleMaps,Description,Transit_Notes`.
* When imported into Google My Maps and styled with [Sequence of numbers], pins are automatically marked `1, 2, 3...` in chronological order.

### 2. All-in-One KML File (`[City]_mymaps.kml`)
* A single drag-and-drop into Google My Maps generates:
  - Separate layer folders for each day (`Day 1`, `Day 2`...)
  - Chronological numbered pins (`#1`, `#2`...)
  - Colored transit route polylines connecting daily spots (`Day N Transit Route`)

### 3. Apple iPhone (iOS) Style Card News Web App (`[City]_trip_cards.html`)
* **Glassmorphic UI**: SF Pro typography, Phosphor Icons, and white glassmorphism design.
* **1-Card-at-a-Time View**: Sequence badge (`#1`), Day badge, time range, transit tips, and local situational phrase box.
* **Native TTS Voice**: Tap the speaker icon to play native pronunciation using the device's Web Speech API.
* **Driver Display Modal**: 36px oversized local script display modal for taxi drivers and restaurant staff.
* **3 Essential Modals**: Precision expense summary, foodie/shopping wishlist checklist, and quick-call emergency & hotel contacts.

---

## 📂 Templates & Resources
* [Master Itinerary Template](./resources/master_itinerary_template.md): Global standard Markdown master itinerary structure.
* [Budget Template](./resources/budget_template.md): Multi-currency budget template with taxes & tips.
* [Google My Maps CSV Template](./resources/itinerary_template.csv): Standard 6-column CSV header.
* [All-in-One KML Template](./resources/mymaps_template.kml): KML schema with layers, pins, and routes.
* [Maps Data Generator](./resources/generate_maps_data.py): Automated Python script for CSV & KML builds.
* [iOS Card App Template](./resources/ios_card_app_template.html): Standalone mobile web app template.
* [Global Planning Playbook](./references/trip_planning_playbook.md): Regional transit and safety guidelines.

---

## 📄 License
MIT License. See [LICENSE](../../LICENSE) for details.
