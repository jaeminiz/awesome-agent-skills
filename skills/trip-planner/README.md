# 🧭 Global Trip Planner

[![skills.sh](https://img.shields.io/badge/skills.sh-trip--planner-black)](https://www.skills.sh/jaeminiz/awesome-agent-skills/trip-planner)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)

**English** | **[한국어](README.ko.md)**

> **Expert AI Travel Planner & Itinerary Architect Skill for Agentic Frameworks.**  
> Covers domestic and worldwide international destinations. Conducts interactive interviews, retrieves live prices and daily exchange rates, and automatically generates master itineraries, **Google My Maps Day-by-Day CSVs & All-in-One KMLs**, and **Apple iPhone (iOS) style card news web applications**.

---

## ⚡ Quick Install

```bash
npx skills add https://github.com/jaeminiz/awesome-agent-skills --skill trip-planner
```

---

## 🌟 Core Features

1. **Interactive Planning First (No Arbitrary Guessing)**
   - Never generates an itinerary blindly. Systematically clarifies duration, party composition, transport preference, accommodation style, and key travel themes through structured dialogues.
2. **Real-Time Data Driven**
   - Researches lowest live airfare and accommodation options using browser search tools, and applies live daily foreign exchange rates (VND, JPY, USD, EUR, etc.) to construct an accurate budget breakdown.
3. **Media-Curated Gourmet & Spots**
   - Curates verified restaurants and scenic cafes along daily transit routes by analyzing travel creators on YouTube, blogs, Instagram, and recent Google Maps reviews.
4. **Minute-by-Minute Timeline Table & Google Maps Integration**
   - Delivers comprehensive 5-column daily timeline tables without abbreviations: minute-level timings, luggage drop-off checkpoints, situational local phrases (native script, pronunciation, and translation), and multi-stop Google Maps route links.
5. **Google My Maps Complete Deliverables**
   - **Day-by-Day 6-Column CSV (`day1_itinerary.csv`, `day2_itinerary.csv`...)**: Standard columns (`Date,Time,Place,GoogleMaps,Description,Transit_Notes`). Supports separate map layer imports with automatic `1, 2, 3...` sequence badge numbering.
   - **All-in-One KML (`[City]_mymaps.kml`)**: A single import into Google My Maps produces day-separated layer folders, numbered pin markers, and themed polyline routes (`Day N Transit Route`) in seconds.
6. **Mobile-Optimized Apple iPhone (iOS) Card News Web App (`[City]_trip_cards.html`)**
   - **Swipeable Card News UI**: White glassmorphic aesthetic, touch swipe gestures, sequence/category badges, and persistent progress checkmarks (`localStorage`).
   - **Native Pronunciation TTS**: One-tap native voice playback using the device's built-in Web Speech API.
   - **Driver & Staff Display Modal**: 36px oversized local script display modal for taxi drivers and restaurant staff.
   - **3 Essential Modals**: Precision expense summary, foodie/shopping wishlist checklist, and quick-call emergency & hotel contacts.

---

## 📋 6-Phase Global Workflow

```
[Phase 1] Initial Interview & Mandatory Questionnaire (Worldwide customization)
       ↓
[Phase 2] Real-time Flight & Hotel Live Pricing & Daily Exchange Rate Report ➔ [User Selection]
       ↓
[Phase 3] Route-Optimized Gourmet & Scenic Spot Curated List ➔ [User Selection]
       ↓
[Phase 4] ⭐ Mandatory Comprehensive Output (Never abbreviated):
          1. Detailed minute-by-minute timeline table (5 columns)
          2. Multi-stop Google Maps transit route links
          3. Daily exchange rate applied precision budget breakdown
       ↓
[Phase 5] Explicit User Confirmation ("Would you like me to generate the Google My Maps CSVs, All-in-One KML, and iOS Card Web App?") ➔ [User Approval]
       ↓
[Phase 6] Final File Generation: Day-by-Day CSVs, [City]_mymaps.kml, and [City]_trip_cards.html
```

---

## 📱 Live Sample Preview

A glimpse of the mobile-optimized Apple iPhone (iOS) style card news web app generated automatically by this skill:

<p align="center">
  <img src="sample_preview.png" alt="iOS Card News Web App Preview" width="340" style="border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);" />
</p>

* 🌐 **Interactive Web App Sample**: [`examples/danang_trip_cards.html`](examples/danang_trip_cards.html)  
  *(Open directly in any mobile or desktop browser to experience card swiping, voice TTS, and timeline search completely offline.)*
* 🗺️ **Google My Maps All-in-One KML**: [`examples/danang_mymaps.kml`](examples/danang_mymaps.kml)  
  *(Import into Google My Maps to instantly view 1–4 day layer folders, numbered pins, and transit routes.)*
* 📊 **Google My Maps Standard 6-Column Integrated CSV**: [`examples/danang_itinerary.csv`](examples/danang_itinerary.csv)
* 📂 **Google My Maps Day-by-Day CSVs**:
  * [`examples/day1_itinerary.csv`](examples/day1_itinerary.csv) (Day 1)
  * [`examples/day2_itinerary.csv`](examples/day2_itinerary.csv) (Day 2)
  * [`examples/day3_itinerary.csv`](examples/day3_itinerary.csv) (Day 3)
  * [`examples/day4_itinerary.csv`](examples/day4_itinerary.csv) (Day 4)

---

## 📂 File Structure

```
trip-planner/
├── SKILL.md                              # Main agent instruction & strict governance rules
├── README.md                             # English skill documentation
├── README.ko.md                          # Korean skill documentation
├── sample_preview.png                    # Mobile card news web app screenshot
├── examples/                             # Production-ready sample deliverables (Da Nang 4-Day)
│   ├── danang_trip_cards.html            # Mobile card news web app
│   ├── danang_mymaps.kml                 # Google My Maps All-in-One KML
│   ├── danang_itinerary.csv              # Google My Maps 6-column combined CSV
│   ├── day1_itinerary.csv                # Day 1 CSV
│   ├── day2_itinerary.csv                # Day 2 CSV
│   ├── day3_itinerary.csv                # Day 3 CSV
│   └── day4_itinerary.csv                # Day 4 CSV
├── references/
│   └── trip_planning_playbook.md         # Regional planning guidelines (Asia, Europe, Americas)
└── resources/
    ├── master_itinerary_template.md      # Master itinerary Markdown template
    ├── budget_template.md                # Multi-currency budget template
    ├── itinerary_template.csv            # Google My Maps 6-column CSV template
    ├── mymaps_template.kml               # Google My Maps All-in-One KML template
    ├── generate_maps_data.py             # Python utility script for CSV & KML builds
    └── ios_card_app_template.html        # Glassmorphic Phosphor Icons & TTS HTML template
```

---

## 🌐 Language Support

The `trip-planner` skill is fully **language-agnostic**:
* When the user converses in **English**, all questionnaire items, timeline tables, budgets, and generated deliverables are rendered in **English** (with native local phrases for destination countries).
* When the user converses in **Korean**, it operates seamlessly in **Korean**.
* Supports any destination worldwide (Japan, Vietnam, France, Italy, USA, Switzerland, Spain, etc.).

---

## 📄 License

MIT License. See [LICENSE](../../LICENSE) for details.
