# Portfolio Tracker — Project Handoff
**Last updated: April 28, 2026**

---

## WHO

**Cristóbal Escudero** — Weston, Florida (Savanna gated community). Works in logistics/freight forwarding at Fracht. Originally from Chile. Wife: **Fran**. Sons: **Domingo (13)** and **Renato (9)**.

---

## THE APP

**Live URL:** https://cesc-group.github.io/portfolio/
**GitHub repo:** github.com/cesc-group/portfolio (public)
**Single file:** `index.html` (2,871 lines)
**Stack:** Pure HTML/JS/CSS, Chart.js, DM Mono + Fraunces fonts, dark theme

**Cloudflare Worker:** https://yahoo-proxy.cristobalescudero.workers.dev
- Proxies Yahoo Finance API (bypasses CORS)
- Handles RSS feeds
- Decodes `%5E` → `^` for index tickers (^IPSA, ^GSPC, ^IXIC)
- Falls back query1 → query2 Yahoo hosts

**GitHub Actions:** `.github/workflows/update-prices.yml` + `.github/scripts/update_prices.py`
- Runs daily at 6pm ET weekdays
- Fetches mutual fund NAVs via yfinance (server-side)
- Updates `staticPx` values in index.html and commits

---

## PORTFOLIO DATA

### Core Account (Merrill Lynch managed, ~$105k)
All mutual funds use **hardcoded prices** (Yahoo Finance unreliable for these share classes):
- `feb4Px` = Feb 4 2026 baseline (back-calculated from brokerage cost basis)
- `staticPx` = current price (updated by GitHub Actions daily)

| Ticker | Name | Shares | Feb4Px | StaticPx |
|--------|------|--------|--------|---------|
| FIMKX | Fidelity Advisors FOC | 196 | 47.11 | updated daily |
| GSIMX | GS GQG Partners | 166 | 23.90 | updated daily |
| HILIX | Hartford International | 151 | 26.22 | updated daily |
| JVLIX | JHancock Disciplined Value | 306 | 26.15 | updated daily |
| LAIAX | Lord Abbett Intermediate | 493 | 10.43 | updated daily |
| MIMIX | MFS Muni Income | 628 | 8.20 | updated daily |
| NHMRX | Nuveen High Yield Muni | 144 | 14.34 | updated daily |
| OGGFX | JP Morgan Small Cap | 142 | 21.68 | updated daily |
| PAMYX | Putnam Strategic | 361 | 14.25 | updated daily |
| PVAL | Putnam Focused Large Cap | 56 | 48.67 | updated daily |
| SEEGX | JP Morgan Large Cap | 68 | 78.99 | updated daily |
| UBVSX | JP Morgan Undiscovered Mgr | 36 | 84.35 | updated daily |
| IEFA | iShares Core MSCI EAFE ETF | 36 | 95.56 | live Yahoo |
| SUB | iShares Short-Term Muni ETF | 38 | 107.11 | live Yahoo |
| VTV | Vanguard Value ETF | 79 | 203.48 | live Yahoo |
| VUG | Vanguard Growth ETF | **270sh** | 83.02 | live Yahoo |
| CASH1 | ML Bank Deposit | 911 | $1 fixed | $1 fixed |
| CASH2 | Blackrock Liquidity | 517 | $1 fixed | $1 fixed |

**VUG NOTE:** 270 shares total. There's a 45sh transfer artifact at $470.98 cost basis in Merrill — this is an internal ML transfer artifact, NOT a real purchase. Feb4Px is $83.02 (real market price). Using 270 shares with $83.02 gives correct total.

### Thematic Account (CMA-Edge self-directed, ~$12k)
All ETFs — live Yahoo prices via Cloudflare Worker. `staticPx` as fallback.

| Ticker | Name | Shares | Feb4Px | StaticPx |
|--------|------|--------|--------|---------|
| AIQ | Global X AI & Tech ETF | 16 | 50.19 | 53.51 |
| BOTZ | Global X Robotics & AI | 30 | 39.08 | 36.66 |
| GLD | SPDR Gold Trust | 1 | 466.15 | 431.04 |
| IGF | iShares S&P Global Infra | 14 | 66.15 | 67.35 |
| ITA | iShares US Aerospace & Def | 6 | 244.88 | 219.11 |
| PICK | iShares MSCI Global Metals | 24 | 61.30 | 61.76 |
| SMH | VanEck Semiconductor ETF | 4 | 375.55 | 481.85 |
| XLE | Energy Select Sector SPDR | 35 | 56.03 | 56.98 |
| XLV | Health Care Select SPDR | 5 | 151.40 | 146.24 |
| CASH3 | ML Direct Deposit | 1389 | $1 fixed | $1 fixed |

### Coinbase Wallet
| Asset | Qty | Avg Cost | Notes |
|-------|-----|----------|-------|
| ETH | 7.86526052 | $1,559.06 | 100% staked, $29.52/mo staking income |
| BTC | 0.005763 | $110,332 | |
| ADA | static | — | $0.86 |
| MANA | static | — | $0.21 |
| AXS | static | — | $0.10 |
| ANKR | static | — | $0.03 |
| UNI | static | — | $0.02 |
| POL | static | — | $0.01 |
| SNX/LTC/ALGO | static | — | <$0.01 each |

**Live crypto tickers fetched:** ETH-USD, BTC-USD, SOL-USD, BNB-USD, LINK-USD, DOGE-USD

### Binance Wallet (Kids + Family)
| Asset | Qty | Avg Cost | Notes |
|-------|-----|----------|-------|
| SOL | 3.59 | $27.82 | 5.30% APY |
| BNB | 0.32881864 | $484.59 | 0.70% APY |
| LINK | 9.38 | $11.30 | |
| DOGE | 251 | $0.2517 | |
| VET | 2060.255 | static | $15.17 |
| ADA | 26.9 | static | $6.77 |
| ICX | 73.74 | static | $2.79 |
| ONE | 633.5 | static | $1.45 |
| Vaulta | 15.25 | static | $1.37 |
| VTHO | 338.84 | static | $0.20 |

**Binance split 50/50 between Domingo and Renato** (BINANCE_KIDS array with qty/2)

### Family Stocks (Coinbase, bought Apr 27 2026 — 100% Fran)
| Ticker | Name | Qty | CostPx | Logo |
|--------|------|-----|--------|------|
| AMZN | Amazon | 0.38201 | 261.7733 | parqet |
| AAPL | Apple | 0.37526 | 266.4819 | parqet |
| TSLA | Tesla | 0.52934 | 377.8290 | parqet |
| NVDA | NVIDIA | 0.46506 | 215.0260 | parqet |

---

## KEY TECHNICAL DECISIONS

### Price Data Architecture
```
Mutual funds → staticPx only (Yahoo returns wrong data for these share classes)
ETFs → live Yahoo via Worker, staticPx fallback
Crypto → live Yahoo via Worker (ETH-USD, BTC-USD, etc.), avgCost fallback
Family stocks → live Yahoo via Worker, costPx fallback
Cash → fixedPrice: 1 always
```

### Critical Constants
- **P&L baseline date:** Feb 4, 2026 (`P1 = new Date('2026-02-03')`)
- **Wealth goal:** $200,000 by April 2028
- **Admin PIN:** 1062 (cosmetic only — visible in source)
- **MUTUAL_FUNDS array:** `['FIMKX','GSIMX','HILIX','JVLIX','LAIAX','MIMIX','NHMRX','OGGFX','PAMYX','PVAL','SEEGX','UBVSX']`

### getTotalWealth() — Single Source of Truth
```js
function getTotalWealth() {
  const etfVal = HOLDINGS.reduce(...)      // all ETF positions
  const crypto = getCryptoTotal()           // all wallets live
  const extCash = externalCash || 0        // user-entered bank cash
  const franStocks = getFamilyStocksTotal() // AMZN/AAPL/TSLA/NVDA
  return etfVal + crypto + extCash + franStocks;
}
```

### getCryptoTotal() — Uses avgCost as floor when prices not loaded
```js
function getCryptoTotal() {
  // if cryptoPrices[ticker] > 0: use live price × qty
  // else: use avgCost × qty (prevents showing $0 before Worker responds)
}
```

### LAIAX Bug (FIXED — do not revert)
LAIAX and all mutual funds in MUTUAL_FUNDS array MUST use staticPx only.
Yahoo Finance returns wrong/inflated prices for these Merrill share classes.
`getPrice()` checks `MUTUAL_FUNDS.includes(ticker)` → always returns `staticPx`.
**Never remove this check.**

---

## TAB STRUCTURE & ORDER

1. **Family** (default, open — no PIN)
2. **Markets** (open — no PIN)
3. **Overview** (PIN locked: 1062)
4. **Holdings** (PIN locked: 1062)
5. **Crypto** (PIN locked: 1062)
6. **Allocation** (PIN locked: 1062)

---

## FEATURE INVENTORY

### Ticker Ribbon (below nav)
- All 25 ETF positions + 6 live crypto cards scrolling
- Shows: ticker, today's % change, today's $ change, current price
- ↑/↓ colored green/red
- Hover to pause, drag to scroll manually
- Speed: `Math.max(58, halfWidth/70)`

### Overview Tab
**5 portfolio cards** (single row):
1. Total Wealth — ETF + Crypto + Stocks + Cash breakdown
2. Core — Merrill managed, P&L today + Feb 4
3. Thematic — CMA Edge self-directed
4. Stocks — Fran's portfolio value + P&L
5. Crypto — all wallets total, ETH value

**Chart** — clickable cards switch chart view. Multi-select via Ctrl+Click for comparison (% return mode). All 5 cards clickable including Stocks and Crypto.

**Sidebar** — sortable by Account/P&L%/Value. Includes crypto section. Crypto merged into P&L/Value sorts.

**SPY benchmark** — checkbox toggle overlays SPY on the chart

### Holdings Tab
- Full table with all positions
- Sortable columns (click headers)
- **% Portfolio** column default sort
- Sections: ETF Core → ETF Thematic → Stocks (Fran) → Crypto → External Cash
- Mutual funds show static prices, ETFs show live

### Crypto Tab
- Cards with CoinGecko logos
- Assets under $10 grouped as "Others"
- Live price per token shown
- Coinbase + Binance wallets combined

### Allocation Tab
- External cash input field (adds to total wealth everywhere)
- Cash recommendation based on VIX level
- $200k wealth goal progress bar with monthly run rate
- Target vs actual: Equities 75% / Crypto 15% / Cash 10%
- Rebalancing signals
- $35k bonus deployment note

### Markets Tab
- VIX, WTI Oil, Copper, Gold (live)
- FX: USD vs CLP, BRL, MXN, ARS, EUR
- Polymarket prediction markets (static Apr 2026)
- 6 Guru portfolios with 13F holdings
- Guru recommendations mapped to Cristóbal's portfolio

### Family Tab
**Market indices strip:**
- S&P 500 Composite (^GSPC) — green
- Nasdaq Composite (^IXIC) — blue
- IPSA Santiago 🇨🇱 (^IPSA) — teal, CLP, fallback: SP-IPSA.SN

**Interactive chart:**
- 1-year % return, all indices on same scale
- Click index card → switch pinned index
- Search bar with SVG magnifier → AI resolves company names to tickers
- AI uses Anthropic API (claude-sonnet-4-20250514, max_tokens:20)
- Up to 4 stocks overlaid + 1 pinned index = 5 curves max
- FIFO: oldest stock dropped when 5th added
- Pinned index: solid line. Stocks: dashed lines
- Legend strip shows color + ticker + 1-year %
- Clear button resets to index only
- Prefetch in background 2s after app load

**Three portfolio cards:**
- Domingo (age 13) — 50% Binance crypto
- Renato (age 9) — 50% Binance crypto
- Fran — 100% AMZN/AAPL/TSLA/NVDA stocks

**Leaderboard** — ranked by P&L

**OWNERSHIP object** — per-stock split {D:0, R:0, F:1} — all stocks currently 100% Fran

### PIN Lock
- Cosmetic only (PIN visible in source)
- PIN: 1062
- Locks: Overview, Holdings, Crypto, Allocation
- Unlocks for entire session once entered
- `adminUnlocked` boolean, `showTabLocked()` function

---

## PENDING / NOT YET BUILT

1. **$35k bonus deployment** — tranche tracker removed until money arrives. T1: SMH 20sh @$208 + VWO 175sh @$44.50. T2: ~$12k VOO/VTI. T3: opportunistic. Add back when bonus received.

2. **Binance Kids tab** — currently shows in Family tab. Could be separate tab later.

3. **DR Commercial Real Estate (Bonita Gardens, Las Terrenas)** — rated 6.5/10. Not pursuing until liquid portfolio hits $300-400k.

4. **Chart for Kids/Fran** — family tab chart shows market indices, not their personal performance. Their portfolio history is too short for meaningful charts.

---

## KNOWN ISSUES / WATCH OUT FOR

1. **LAIAX +130% bug** — was caused by Yahoo returning wrong data. Fixed by MUTUAL_FUNDS exclusion. Never remove that check.

2. **Safari PWA cache** — service worker removed (self-destructs now). If old version shows on phone, clear Safari website data for github.io in Settings → Safari → Advanced → Website Data.

3. **^IPSA encoding** — worker must decode `%5E` → `^` before hitting Yahoo. This is in the current worker.js. If IPSA stops working, check this decode logic first.

4. **VUG 270 shares** — DO NOT change back to 225. The 45sh artifact at $470.98 is excluded from P&L by using feb4Px=$83.02 for all 270 shares, not by reducing share count.

5. **Crypto loads after app** — `fetchCryptoPrices()` runs after loader closes (background). Allocation tab re-renders after crypto loads. If Allocation shows wrong total, wait 5 seconds and recheck.

6. **Family stocks duplicate bug** — FIXED. `renderFamily()` now clears all containers at the very start. Do not add any container-filling logic outside this clearing pattern.

7. **Auto-refresh every 5 minutes** — skips if `selTickers.size > 0` (user is in comparison mode).

---

## INVESTMENT PHILOSOPHY

- ETF-first, long-term compounding
- Feb 4, 2026 as clean P&L baseline for ALL positions
- Limit orders only, after 10am ET
- No cost basis confusion — just price movement since entry
- Crypto treated as separate bucket, static snapshot for minor assets
- Target allocation: Equities 75% / Crypto 15% / Cash 10%
- Wealth goal: $200,000 by April 2028

---

## FILE STRUCTURE IN REPO

```
portfolio/
├── index.html          ← main app (single file)
├── manifest.json       ← PWA manifest
├── sw.js               ← self-destructing service worker
├── icon-192.png        ← app icon
├── icon-512.png        ← app icon large
└── .github/
    ├── workflows/
    │   └── update-prices.yml   ← daily price updater
    └── scripts/
        └── update_prices.py    ← fetches mutual fund NAVs
```

---

## WHEN STARTING A NEW CHAT

Tell Claude:
1. Share this document
2. Share the current `index.html` from GitHub (raw URL or paste)
3. Mention: "This is a single-file portfolio tracker app. All context is in the handoff doc. The worker is already deployed at yahoo-proxy.cristobalescudero.workers.dev."
4. Always test changes in the sandbox first, then push to GitHub Pages for real testing (sandbox blocks the Cloudflare Worker so crypto/live prices won't show there)
