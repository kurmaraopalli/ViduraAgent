# 🏛️ ViduraAgent (विदुरएजण्ट)

> *"Foresight is the weapon of the wise against future adversity."*

**ViduraAgent** is an autonomous, lightweight macro-economic and technology intelligence strategist built using **Google Antigravity**. Named after the legendary ancient Indian master of foresight, this agent tracks long-term structural shifts, technology adoption curves, and regulatory risks over 5-year and 10-year horizons, while maintaining a daily pulse on current market realities.

---

## 🧭 Core Strategic Domain Mandates

### 1. Dual-Horizon Projections (5 & 10 Years)
*   📈 **Stock Market**: Structural capital flows, mutual fund retail participation (SIP trends), index re-ratings, and capital flow vectors.
*   💻 **Information Technology**: Global Capability Centers (GCCs), SaaS-to-PaaS migrations, enterprise cloud paradigms, and tech talent corridors.
*   🤖 **Artificial Intelligence**: Sovereign GPU clusters (IndiaAI Mission), agentic workflow scaling, chip assembly ecosystems, and AGI knowledge economy transition.

### 2. India-First Strategic Bias
*   Deep mapping of national programs (IndiaAI Mission, Production Linked Incentives (PLI 2.0), Digital Public Infrastructure (UPI, ONDC, Account Aggregators)).
*   **Geographical Hub Tracking**: Focus on India's top 5 tech and DeepTech clusters:
    *   *Bengaluru*: DeepTech, Aerospace, and global GCC networks.
    *   *Hyderabad*: Enterprise SaaS, AI CoEs, and renewable data center spires.
    *   *NCR (Noida/Gurugram)*: AI operations, hardware scale, and mobile manufacturing.
    *   *Pune*: Embedded systems, industrial IoT, and enterprise middleware.
    *   *Chennai*: SaaS hubs, fintech cities, and hardware fabrication.

---

## 🔌 Data Sources & Intel Feeds

ViduraAgent pulls intelligence programmatically using raw APIs and headless search indexers:
*   📊 **Financial Market Indicators**: Live feeds from **Yahoo Finance (`yfinance`)** tracking:
    *   **NIFTY 50** (`^NSEI`) — Indian large-cap benchmark indicator.
    *   **SENSEX** (`^BSESN`) — BSE flagship index.
    *   **Gold (USD)** (`GC=F`) — Global safe-haven asset gauge.
    *   **Brent Crude** (`BZ=F`) — Global energy inflation indicator.
    *   **USD/INR** (`USDINR=X`) — Sovereign currency corridor.
*   📰 **Macro & Regulatory News**: Custom query streams via **DuckDuckGo News Indexer (`duckduckgo_search`)** to extract real-time geopolitical policy changes, central bank policy shifts (RBI/Fed/ECB), and technology adoption curves.

---

## 🏗️ Premium Tech Stack & Architecture

ViduraAgent is designed with a decoupled **Zero-Infrastructure-Cost** design:
*   **Intelligence Engine**: Python 3.11 script compiling dynamic web updates into a flat, valid JSON feed.
*   **Database**: Standard JSON state storage (`docs/dashboard_data.json`) acting as a lightweight, zero-maintenance state store.
*   **Orchestration / CI**: **GitHub Actions** executing automatically every morning at **08:00 AM IST** (`30 2 * * *` CRON) to gather updates, validate JSON schemas, and commit/push changes.
*   **Dashboard Frontend**: Vanilla HTML5 and pure CSS3 using advanced HSL color tokens for transition animations.
*   **Hosting**: Serverless delivery via **GitHub Pages** serving straight from the `/docs` folder.
*   **Theme Engine**: Custom LocalStorage-based theme engine supporting **☀️ Light**, **🌙 Dark**, and **⚙️ Auto** (system OS theme matching and live change event monitoring).
*   **XSS Protection**: Complete context-escaping on all dynamic elements using custom escaping routines, plus absolute URL scheme verification on publisher links.

---

## 🎨 Architectural Icon Design

To reflect ViduraAgent's identity, all dashboard layout items utilize AI-generated, flat-vector symbols inspired by ancient Indian temple architecture and sacred geometry:

| Icon | Architectural Representation | Concept |
|---|---|---|
| 🏛️ **Logo** | Sarnath Ashoka Pillar + Temple Shikhara arch + Lotus base | Master of Indian foresight and governance |
| 📈 **Stocks** | Stylized Dravidian Gopuram temple tower | Tiers rising upward like an ascending bar chart |
| 💻 **IT** | Sacred Sri Yantra geometric mandala | Complex network systems, cloud nodes, and code paths |
| 🤖 **AI** | Sun God Surya with radiating geometric lines | Radiance, higher vision, and synthetic intelligence |
| 🐚 **Pulse** | Sacred Conch (Shankha) | Proclaiming daily news, announcements, and market pulse |
| 🛕 **Horizon 5** | Solid Sanchi Stupa dome | Grounded, stable near-term milestones |
| 🕌 **Horizon 10** | Curvilinear Nagara Shikhara spire | Aspirational, long-term heights pointing to the future |
| 🪷 **Scroll** | 8-Petal Lotus (Padma) | Symmetrical global feed loop and holistic view |

*Note: All elements contain automatic, inline SVG fallbacks and CSS filter maps to guarantee perfect visibility in both light and dark themes.*

---

## 🚀 Repository Structure

```text
ViduraAgent/
├── .github/
│   └── workflows/
│       └── daily_update.yml   # Daily Action CRON (08:00 AM IST)
├── agent/
│   └── skills/
│       └── vidura_core/
│           └── agent/
│               └── SKILL.md   # Core strategist mandate and system persona
├── docs/                      # Primary site directory for GitHub Pages
│   ├── index.html             # UI with light/dark toggles & SVG fallbacks
│   ├── dashboard_data.json    # Real-time state cache (refreshed daily)
│   └── icons/                 # Custom generated Indian style vector assets
│       ├── logo.png
│       ├── stocks.png
│       ├── it.png
│       ├── ai.png
│       ├── pulse.png
│       ├── horizon5.png
│       ├── horizon10.png
│       └── scroll.png
└── tools/
    ├── daily_digest.py        # Python scraper & analyzer (saves to docs/)
    ├── setup_icons.py         # Copies generated PNG icons to docs/icons/
    └── cleanup.py             # Removes legacy duplicate folders and files
```

---

## 🛠️ Local Installation & Development

### 1. Setup the Files
Ensure you run setup to populate the custom icons and remove duplicate folders:
```bash
python tools/setup_icons.py
python tools/cleanup.py
```

### 2. Manual Data Generation
To pull fresh live feed data locally:
```bash
pip install yfinance duckduckgo-search
python tools/daily_digest.py
```

### 3. Serving
Simply open `docs/index.html` in your web browser. It contains an inline data cache that guarantees it will render cleanly using a `file://` protocol fallback even if closed behind CORS restrictions!
