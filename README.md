# 🌟 Awesome Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/jaeminiz/awesome-agent-skills/pulls)
[![skills.sh](https://img.shields.io/badge/skills.sh-trip--planner-black)](https://www.skills.sh/jaeminiz/awesome-agent-skills/trip-planner)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/jaeminiz/awesome-agent-skills)

**English** | **[한국어](README.ko.md)**

> **Curated collection of production-ready AI agent skills for Google Antigravity, Claude Code, Codex, and modern Agentic Frameworks.**  
> Boost your AI coding agents with battle-tested workflows, structured methodologies, and multi-modal deliverables.

---

## ⚡ Instant Installation (One-liner)

Install directly to any supported agent environment using the universal `skills` CLI:

```bash
# Install specific skill (e.g. trip-planner)
npx skills add https://github.com/jaeminiz/awesome-agent-skills --skill trip-planner

# Or inspect available skills without installing
npx skills add https://github.com/jaeminiz/awesome-agent-skills --list
```

---

## 🧭 Skills Directory

| Category | Skill Name | Description | Link |
| :--- | :--- | :--- | :---: |
| ✈️ **Travel & Lifestyle** | [`trip-planner`](skills/trip-planner) | **Global Expert Travel Planner & Itinerary Architect**<br>• Interactive step-by-step questionnaire & live pricing/exchange rate lookup<br>• Media-curated gourmet & cafe recommendations (YouTube, Instagram, Blogs)<br>• **Detailed minute-by-minute timeline (5-column table)** & precision budget<br>• **Google My Maps standard 6-column Day-by-Day CSV & All-in-One KML**<br>• **Mobile-optimized Apple iPhone (iOS) style card news web app** | [Explore](skills/trip-planner) |

---

## 🏆 Featured Skill: `trip-planner`

### 🧭 [trip-planner](skills/trip-planner) — Global Travel Planner & Itinerary Architect

A production-grade AI agent skill designed for both domestic and worldwide international travel planning.

* **6 Strict Rules**: Never guess or arbitrarily finalize plans without user alignment; retrieve real-time flight/hotel prices and current exchange rates via browser tools; conduct deep multi-source trend research; output full 5-column daily timeline tables without abbreviations; obtain explicit user confirmation before generating final file artifacts.
* **3 Multi-modal Deliverables**:
  1. **Google My Maps Day-by-Day CSVs (`day1_itinerary.csv`, `day2_itinerary.csv`...)**:  
     Standard 6-column layout (`Date,Time,Place,GoogleMaps,Description,Transit_Notes`). Easily imported into Google My Maps layers with automatic `1, 2, 3...` sequence badge numbering.
  2. **One-Click All-in-One KML (`[City]_mymaps.kml`)**:  
     Single drag-and-drop import into Google My Maps that creates separate layer folders per day, numbered pin markers, and themed route polylines (`Day N Transit Route`) in seconds.
  3. **Apple iPhone (iOS) Style Card News Web App (`[City]_trip_cards.html`)**:  
     A standalone, glassmorphic offline web application. Features swipeable gesture cards, native speech synthesis (Web Speech API TTS) for local phrases, large 36px driver-display modals, one-click Google Maps links, and 3 essential modals (expenses, wishlist checklist, and hotel/emergency contacts).

<p align="center">
  <img src="skills/trip-planner/sample_preview.png" alt="iOS Card News Web App Preview" width="340" style="border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);" />
</p>

* 🌐 **[Live Demo: Da Nang 4-Day Trip Card Web App](skills/trip-planner/examples/danang_trip_cards.html)**
* 🗺️ **[Google My Maps All-in-One KML Sample](skills/trip-planner/examples/danang_mymaps.kml)**
* 📊 **[Google My Maps Standard 6-Column CSV Sample](skills/trip-planner/examples/danang_itinerary.csv)**
* 📖 **[Read the Full trip-planner Skill Documentation](skills/trip-planner/)**

---

## 🚀 Manual Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/jaeminiz/awesome-agent-skills.git
```

### 2. Register into Google Antigravity Global Skills
Copy the target skill directory to your Antigravity global skills folder:

```bash
# Windows (PowerShell)
Copy-Item -Path "awesome-agent-skills\skills\trip-planner" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force

# macOS / Linux
cp -r awesome-agent-skills/skills/trip-planner ~/.gemini/config/skills/
```

### 3. Register into Project Workspace (Local Agent Scope)
To activate skills only inside a specific repository or workspace:

```bash
mkdir -p .agents/skills
cp -r awesome-agent-skills/skills/trip-planner .agents/skills/
```

---

## 🤝 Contributing

Contributions of new high-quality agent skills are warmly welcome!

1. Fork this repository.
2. Create your skill directory under `skills/<skill-name>/` with a valid specification (`SKILL.md`):
   ```
   skills/my-awesome-skill/
   ├── SKILL.md            # YAML frontmatter (name, description) and actionable agent instructions
   ├── README.md           # Introduction, features, and usage guide
   ├── references/         # (Optional) Detailed domain playbooks
   └── resources/          # (Optional) Templates, scripts, and asset files
   ```
3. Add your skill entry to the [Skills Directory](#-skills-directory) in this `README.md`.
4. Submit a Pull Request (PR)!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - feel free to use, modify, and distribute for personal and commercial projects.