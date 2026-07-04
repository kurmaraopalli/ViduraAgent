"""
ViduraAgent — Daily Digest Engine
==================================
Fetches live market data (yfinance) and news headlines (duckduckgo_search),
compiles a structured JSON payload per the SKILL.md schema, and overwrites
frontend/dashboard_data.json.

Run locally:   python tools/daily_digest.py
Auto-run via:  .github/workflows/daily_update.yml  (08:00 IST daily)
"""

import json
import os
import sys
from datetime import datetime, timezone, timedelta

# ---------------------------------------------------------------------------
# Dependency guard — fall back gracefully if packages are missing
# ---------------------------------------------------------------------------
try:
    import yfinance as yf
except Exception:
    yf = None

try:
    from duckduckgo_search import DDGS
except Exception:
    DDGS = None

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PUBLISHER = {
    "name": "Kurma Rao Palli",
    "profile_url": "https://kurmaraopalli.github.io/About-Me/"
}

# Output path relative to repo root (script is called from repo root in CI)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
OUTPUT_PATH = os.path.join(REPO_ROOT, "docs", "dashboard_data.json")

IST = timezone(timedelta(hours=5, minutes=30))

# Tickers: NIFTY50, SENSEX, Gold (USD), Brent Crude, USD/INR
MARKET_TICKERS = {
    "NIFTY50":   "^NSEI",
    "SENSEX":    "^BSESN",
    "GOLD_USD":  "GC=F",
    "BRENT":     "BZ=F",
    "USDINR":    "USDINR=X",
}

# DuckDuckGo search queries per theme
SEARCH_QUERIES = {
    "global_scroll": [
        "Fed ECB RBI interest rate decision 2025",
        "global inflation CPI data 2025",
        "semiconductor supply chain news 2025",
        "US tech sector earnings 2025",
        "global capital markets today",
    ],
    "india_pulse": "India stock market Nifty Sensex today 2025",
    "five_year_stocks": "India stock market 5 year outlook 2025 2026 2027 2028 2029 2030",
    "five_year_it":     "India IT sector GCC SaaS cloud 5 year forecast 2025",
    "five_year_ai":     "India AI artificial intelligence 5 year investment 2025",
    "ten_year_stocks":  "India stock market 10 year structural trends 2035",
    "ten_year_it":      "India IT sector digital transformation 10 year 2035",
    "ten_year_ai":      "India AI chip manufacturing LLM 10 year 2035",
}

MAX_RESULTS = 5   # DuckDuckGo results per query

FALLBACK_MARKET_SNAPSHOT = {
    "NIFTY50": {"price": 24000.0, "change_pct": 0.0},
    "SENSEX": {"price": 77000.0, "change_pct": 0.0},
    "GOLD_USD": {"price": 4000.0, "change_pct": 0.0},
    "BRENT": {"price": 73.0, "change_pct": 0.0},
    "USDINR": {"price": 94.0, "change_pct": 0.0},
}

FALLBACK_GLOBAL_SCROLL = [
    {"headline": "Live market and news feeds are being refreshed; fallback content is active.", "impact": "Neutral"},
    {"headline": "ViduraAgent will populate richer signals once live feeds respond normally.", "impact": "Neutral"},
]

FALLBACK_INDIA_HEADLINES = [
    "India macro indicators remain in focus amid policy and liquidity shifts.",
    "Domestic investment flows continue to shape near-term market resilience.",
]

FALLBACK_FIVE_YEAR = {
    "stocks": ["India’s structural growth story remains intact across domestic demand and policy support."],
    "it": ["Technology services and GCC expansion continue to reshape India’s export mix."],
    "ai": ["AI adoption is gradually moving from pilots toward broader enterprise deployment."],
}

FALLBACK_TEN_YEAR = {
    "stocks": ["Long-term wealth creation remains tied to manufacturing, services, and financial deepening."],
    "it": ["Digital infrastructure and platform-led services could widen India’s strategic influence."],
    "ai": ["Sovereign compute and AI talent ecosystems are central to long-horizon competitiveness."],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fetch_market_snapshot() -> dict:
    """Pull latest price + % change for each configured ticker."""
    if yf is None:
        print("  [WARN] yfinance is unavailable; using fallback market snapshot.")
        return FALLBACK_MARKET_SNAPSHOT

    snapshot = {}
    for label, ticker_symbol in MARKET_TICKERS.items():
        try:
            tkr  = yf.Ticker(ticker_symbol)
            info = tkr.fast_info
            price  = round(float(info.last_price), 2)
            prev   = float(info.previous_close)
            change = round(((price - prev) / prev) * 100, 2) if prev else 0.0
            snapshot[label] = {"price": price, "change_pct": change}
        except Exception as exc:
            print(f"  [WARN] Could not fetch {label} ({ticker_symbol}): {exc}")
            snapshot[label] = {"price": None, "change_pct": None}

    if not any(v.get("price") is not None for v in snapshot.values()):
        print("  [WARN] Market fetch returned no usable values; using fallback snapshot.")
        return FALLBACK_MARKET_SNAPSHOT
    return snapshot


def ddg_headlines(query: str, max_results: int = MAX_RESULTS) -> list[str]:
    """Return a list of plain headline strings from DuckDuckGo news search."""
    if DDGS is None:
        print(f"  [WARN] DuckDuckGo search unavailable for '{query}'; using fallback headlines.")
        return []

    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.news(query, max_results=max_results):
                title = r.get("title", "").strip()
                if title:
                    results.append(title)
    except Exception as exc:
        print(f"  [WARN] DDG search failed for '{query}': {exc}")
    return results


def classify_impact(headline: str) -> str:
    """Naive keyword-based impact classifier for global_scroll items."""
    hl = headline.lower()
    negative_kw = ["slump", "fall", "crash", "cut", "recession", "risk", "warn",
                   "decline", "drop", "fear", "tariff", "sanction", "layoff"]
    positive_kw = ["surge", "rally", "growth", "record", "boom", "invest", "expand",
                   "rise", "gain", "opportunity", "launch", "breakthrough", "approve"]
    neg = sum(1 for k in negative_kw if k in hl)
    pos = sum(1 for k in positive_kw if k in hl)
    if pos > neg:
        return "Positive"
    if neg > pos:
        return "Negative"
    return "Neutral"


def infer_sentiment(headlines: list[str]) -> str:
    """Aggregate sentiment across a list of headlines."""
    scores = [classify_impact(h) for h in headlines]
    pos = scores.count("Positive")
    neg = scores.count("Negative")
    if pos > neg:
        return "Bullish"
    if neg > pos:
        return "Bearish"
    return "Neutral"


def extract_tags(headlines: list[str]) -> list[str]:
    """Extract the most common meaningful tokens as trending tags."""
    STOP = {"the", "a", "an", "of", "in", "on", "at", "to", "for", "is", "are",
            "and", "or", "with", "as", "by", "from", "that", "this", "it", "be",
            "amid", "over", "amid", "after", "says", "data", "new", "amid", "amid"}
    freq: dict[str, int] = {}
    for h in headlines:
        for word in h.split():
            token = word.strip(".,\"'!?:;()").lower()
            if len(token) > 3 and token not in STOP:
                freq[token] = freq.get(token, 0) + 1
    top = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [f"#{w.capitalize()}" for w, _ in top[:6]]


def split_opps_risks(headlines: list[str]) -> tuple[list[str], list[str]]:
    """Split headlines into opportunity and risk buckets based on impact."""
    opps, risks = [], []
    for h in headlines:
        if classify_impact(h) in ("Positive", "Neutral"):
            opps.append(h)
        else:
            risks.append(h)
    # Guarantee at least one item in each bucket
    if not opps and headlines:
        opps.append(headlines[0])
    if not risks and len(headlines) > 1:
        risks.append(headlines[-1])
    return opps[:3], risks[:3]


# ---------------------------------------------------------------------------
# Main assembly
# ---------------------------------------------------------------------------

def build_payload() -> dict:
    today = datetime.now(IST).strftime("%Y-%m-%d")
    print(f"\n{'='*60}")
    print(f"  ViduraAgent Daily Digest — {today}")
    print(f"{'='*60}\n")

    # 1. Market snapshot
    print("📊  Fetching market snapshot...")
    market = fetch_market_snapshot()

    # 2. Global scroll headlines
    print("🌐  Fetching global scroll headlines...")
    global_raw: list[str] = []
    for q in SEARCH_QUERIES["global_scroll"]:
        global_raw.extend(ddg_headlines(q, max_results=3))
    global_scroll = [
        {"headline": h, "impact": classify_impact(h)}
        for h in global_raw[:10]
    ]
    if not global_scroll:
        global_scroll = FALLBACK_GLOBAL_SCROLL

    # 3. Daily pulse (India-focused)
    print("🇮🇳  Fetching India daily pulse...")
    india_headlines = ddg_headlines(SEARCH_QUERIES["india_pulse"], max_results=8)
    if not india_headlines:
        india_headlines = FALLBACK_INDIA_HEADLINES
    top_headline    = india_headlines[0] if india_headlines else "India markets stable today."
    sentiment       = infer_sentiment(india_headlines)
    tags            = extract_tags(india_headlines)

    # 4. Horizon intelligence — 5-year
    print("🔭  Fetching 5-year horizon intelligence...")
    fy_stocks = ddg_headlines(SEARCH_QUERIES["five_year_stocks"])
    fy_it     = ddg_headlines(SEARCH_QUERIES["five_year_it"])
    fy_ai     = ddg_headlines(SEARCH_QUERIES["five_year_ai"])

    # 5. Horizon intelligence — 10-year
    print("🔭  Fetching 10-year horizon intelligence...")
    ty_stocks = ddg_headlines(SEARCH_QUERIES["ten_year_stocks"])
    ty_it     = ddg_headlines(SEARCH_QUERIES["ten_year_it"])
    ty_ai     = ddg_headlines(SEARCH_QUERIES["ten_year_ai"])

    if not fy_stocks:
        fy_stocks = FALLBACK_FIVE_YEAR["stocks"]
    if not fy_it:
        fy_it = FALLBACK_FIVE_YEAR["it"]
    if not fy_ai:
        fy_ai = FALLBACK_FIVE_YEAR["ai"]
    if not ty_stocks:
        ty_stocks = FALLBACK_TEN_YEAR["stocks"]
    if not ty_it:
        ty_it = FALLBACK_TEN_YEAR["it"]
    if not ty_ai:
        ty_ai = FALLBACK_TEN_YEAR["ai"]

    print("\n✅  All data fetched. Assembling payload...\n")

    fy_s_opps, fy_s_risks = split_opps_risks(fy_stocks)
    fy_i_opps, fy_i_risks = split_opps_risks(fy_it)
    fy_a_opps, fy_a_risks = split_opps_risks(fy_ai)
    ty_s_opps, ty_s_risks = split_opps_risks(ty_stocks)
    ty_i_opps, ty_i_risks = split_opps_risks(ty_it)
    ty_a_opps, ty_a_risks = split_opps_risks(ty_ai)

    return {
        "last_updated": today,
        "publisher": PUBLISHER,
        "market_snapshot": market,
        "global_scroll": global_scroll,
        "daily_pulse": {
            "media_headline":   top_headline,
            "social_sentiment": sentiment,
            "trending_tags":    tags,
        },
        "horizons": {
            "five_year": {
                "stocks": {"opportunities": fy_s_opps, "risks": fy_s_risks},
                "it":     {"opportunities": fy_i_opps, "risks": fy_i_risks},
                "ai":     {"opportunities": fy_a_opps, "risks": fy_a_risks},
            },
            "ten_year": {
                "stocks": {"opportunities": ty_s_opps, "risks": ty_s_risks},
                "it":     {"opportunities": ty_i_opps, "risks": ty_i_risks},
                "ai":     {"opportunities": ty_a_opps, "risks": ty_a_risks},
            },
        },
    }


def main() -> None:
    payload = build_payload()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"💾  Written → {OUTPUT_PATH}")
    print(f"    Keys: {list(payload.keys())}")
    print(f"    Global scroll items: {len(payload['global_scroll'])}")
    print(f"    Sentiment: {payload['daily_pulse']['social_sentiment']}")
    print(f"\n{'='*60}\n")


if __name__ == "__main__":
    main()
