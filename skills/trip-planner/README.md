# 🧭 Global Trip Planner

[![Version](https://img.shields.io/badge/version-v1.5.1-emerald)](https://github.com/jaeminiz/awesome-agent-skills/releases/tag/v1.5.1)
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
   - **Day-by-Day 8-Column CSV (`day1_itinerary.csv`, `day2_itinerary.csv`...)**: Standard columns (`Date,Time,Place,Latitude,Longitude,GoogleMaps,Description,Transit_Notes`). Explicit Latitude and Longitude columns ensure 1-second instant pinpointing in Google My Maps, with automatic `1, 2, 3...` sequence badge numbering.
   - **All-in-One & Day-by-Day KML (`[City]_mymaps.kml`, `[City]_DayN.kml`)**: 100% compliant with Google My Maps parser requirements with XML entity escaping (`&amp;`) and validated flat placemark architecture for error-free multi-layer imports.
   - 🗺️ **User Guide for Importing into Google My Maps**:
     * **[Method A: CSV Import - Recommended]**: Go to [Google My Maps](https://www.google.com/maps/d/) ➔ [Create a new map] ➔ Click [Import] ➔ Upload CSV ➔ Confirm auto-detected `Latitude` and `Longitude` ➔ Choose `Place` as marker title ➔ Set [Sequence of numbers] style with [Place] label for automatic `1, 2, 3...` chronological pin badges.
     * **[Method B: KML Import - One-Click]**: [Create a new map] ➔ [Import] ➔ Drag & drop `.kml` ➔ Instant numbered pins and popup descriptions with zero XML parse errors.
     * 💡 **Troubleshooting**: If an import error modal appears due to previous session caching, simply hit **F5 (Refresh)** in your browser and re-import into a new layer.
6. **Mobile-Optimized Apple iPhone (iOS) Card News Web App (`[City]_trip_cards.html`)**
   - **Strict Layout & Schema Preservation**: Uses [`resources/ios_card_app_template.html`](resources/ios_card_app_template.html) verbatim without altering HTML DOM IDs, CSS styles, modal layouts, or the `const itineraryData = [{ id, day, time, title, category, description, phraseKo, phraseJa, phraseMeaning, cost, mapQuery }]` JS engine.
   - **Swipeable Card News UI**: White glassmorphic aesthetic, touch swipe gestures, sequence/category badges, and completion checkmarks.
   - **Native Pronunciation TTS & Staff Fullscreen Modal (`#modalShowJapanese`)**: One-tap native voice playback via Web Speech API and oversized fullscreen local script display for staff/drivers.
   - **3 Essential Top Modals (Fixed Layout)**:
     * **`#modalBudget`**: Blue-indigo gradient total highlight box + 3 structured breakdown sections (Food, Transport, Tickets/Tours).
     * **`#modalShopping`**: Day-badged (`D1`, `D2`, `D3`) wish achievement cards with sequence numbers (`#seq`).
     * **`#modalEmergency`**: Dark (`bg-slate-900`) Hotel Taxi Card & Airport Taxi Card with one-click `copyToClipboard` buttons + Emergency Contact Numbers box.

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
  <img src="dual_preview.png" alt="Dual Mobile Web App Styles: Pocket Guide & iOS Card News Preview" width="760" style="border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.12);" />
</p>

### 🌐 Live Interactive Demos (Instant Browser Test)
Test the generated mobile web applications directly in your smartphone or desktop browser:
* 📱 **[Style 1: Mobile Pocket Guide Demo (Da Nang 4-Day)](https://jaeminiz.github.io/awesome-agent-skills/skills/trip-planner/examples/danang_pocket_guide.html)** — *Recommended ⭐ (4 native bottom tabs, live search, task checkmarks, Apple/Google Maps, TTS voice, dynamic exchange rate calculator)*
* 🗂️ **[Style 2: Apple iOS Card News Demo (Da Nang 4-Day)](https://jaeminiz.github.io/awesome-agent-skills/skills/trip-planner/examples/danang_trip_cards.html)** — *(Swipe gesture card deck, white glassmorphic design, 4 top utility modals)*