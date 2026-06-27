# 🏛️ ViduraAgent (विदुरएजण्ट)

> *"Foresight is the weapon of the wise against future adversity."*

**ViduraAgent** is an autonomous, lightweight market intelligence agent built using **Google Antigravity**. Named after the legendary ancient strategist known for his unmatched foresight, this agent tracks macro shifts, technological evolutions, and regulatory risks over 5-year and 10-year horizons, while delivering a daily pulse of social media and market realities.

---

## 🧭 Core Intelligence Capabilities

### 1. Dual-Horizon Projections (5 & 10 Years)
*   📈 **Stock Market**: Structural capital flows, macro-economic cycles, and sector rotations.
*   💻 **Information Technology**: Infrastructure scaling, SaaS evolution, and cloud paradigms.
*   🤖 **Artificial Intelligence**: Agentic workflows, hardware supply chains, and LLM commercialization.

### 2. India-First Strategic Focus
*   Mapping of national initiatives like the **IndiaAI Mission** and **Digital India**.
*   **Geographical Deep-Dives**: Seamless lookup of the top 5 government-focused tech hubs:
    *   *Bengaluru*: DeepTech, Aerospace, and GCC networks.
    *   *Hyderabad*: AI Centers of Excellence and Data Center Hubs.
    *   *NCR (Noida/Gurugram)*: Electronic Manufacturing & AI Operations.
    *   *Pune*: Enterprise Software & Industrial IoT.
    *   *Chennai*: FinTech Cities & Hardware Scale.

### 3. Daily Pulse & Risk Meter
*   **Social Listening**: Continuous scraping of media sentiment across financial networks.
*   **Risk Vector Mapping**: Real-time identification of regulatory blocks, geopolitical friction, and technological obsolescence.

---

## 🏗️ Lightweight Tech Stack

To ensure zero maintenance costs and instantaneous load times, ViduraAgent uses a decoupled **JSON-as-Database** architecture:

*   **Brain / Core**: Google Antigravity Agent & Python SDK.
*   **Data Aggregation**: `yfinance` (market metrics) and `duckduckgo_search` (media stream).
*   **Storage**: A single flat, auto-updating `dashboard_data.json` file.
*   **Frontend**: Vanilla HTML5, Tailwind CSS (via CDN), and asynchronous JavaScript.
*   **Hosting & Automation**: GitHub Pages (UI) + GitHub Actions (Daily CRON execution).

---

## 🚀 Directory Structure

```text
ViduraAgent/
├── .github/
│   └── workflows/
│       └── daily_update.yml  # Automated daily trigger (08:00 AM IST)
├── agent/
│   └── skills/
│       └── vidura_core/
│           └── agent/
│               └── skill.md  # 5/10-year macro strategic routing
├── tools/
│   └── daily_digest.py       # Live data gathering engine
└── frontend/
    ├── index.html            # Ultra-lightweight user dashboard
    └── dashboard_data.json   # Real-time state cache (overwritten daily)
```

---

## 🛠️ Local Initialization with Antigravity

1. Clone your fresh repository:
   ```bash
   git clone https://github.com
   cd ViduraAgent
   ```

2. Instruct your Antigravity environment to begin orchestration:
   > *"Vidura, parse the codebase structure, establish the daily_digest.py routine, and link the frontend interface to track dashboard_data.json autonomously."*
