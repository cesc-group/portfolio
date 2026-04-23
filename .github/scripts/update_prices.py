#!/usr/bin/env python3
"""
Fetches latest NAV/price for all portfolio tickers via yfinance (server-side, no CORS)
and updates the staticPx values in index.html.
Runs as a GitHub Actions job after market close on weekdays.
"""

import re
import yfinance as yf
from datetime import datetime

# All tickers that need staticPx updated
# Mutual funds + ETFs — yfinance handles both server-side
TICKERS = [
    # Core — mutual funds
    'FIMKX', 'GSIMX', 'HILIX', 'JVLIX', 'LAIAX',
    'MIMIX', 'NHMRX', 'OGGFX', 'PAMYX', 'PVAL',
    'SEEGX', 'UBVSX',
    # Core — ETFs
    'IEFA', 'SUB', 'VTV', 'VUG',
    # Thematic — ETFs
    'AIQ', 'BOTZ', 'GLD', 'IGF', 'ITA',
    'PICK', 'SMH', 'XLE', 'XLV',
]

def fetch_prices(tickers):
    """Fetch latest closing prices for all tickers."""
    prices = {}
    print(f"Fetching {len(tickers)} tickers...")
    
    # Batch download — much faster than individual calls
    data = yf.download(tickers, period='5d', interval='1d', progress=False, auto_adjust=True)
    
    for ticker in tickers:
        try:
            if len(tickers) == 1:
                series = data['Close']
            else:
                series = data['Close'][ticker]
            
            # Get most recent non-null price
            series = series.dropna()
            if len(series) == 0:
                print(f"  {ticker}: no data")
                continue
            
            price = round(float(series.iloc[-1]), 2)
            prices[ticker] = price
            print(f"  {ticker}: ${price}")
        except Exception as e:
            print(f"  {ticker}: ERROR — {e}")
    
    return prices

def update_html(prices):
    """Update staticPx values in index.html."""
    with open('index.html', 'r') as f:
        content = f.read()
    
    updated = 0
    for ticker, price in prices.items():
        # Match pattern: ticker:'XXXX', ... staticPx:OLD_PRICE
        # Handles both integer and decimal prices
        pattern = rf"(ticker:'{re.escape(ticker)}'[^{{}}]*?staticPx:)[\d.]+"
        replacement = rf"\g<1>{price}"
        new_content, count = re.subn(pattern, replacement, content)
        if count > 0:
            content = new_content
            updated += 1
            print(f"  Updated {ticker} staticPx → {price}")
        else:
            print(f"  WARNING: {ticker} pattern not found in index.html")
    
    # Update the "Last updated" comment at top of HOLDINGS
    today = datetime.utcnow().strftime('%b %d, %Y')
    content = re.sub(
        r'// ── PRICE DATA — Last updated: [\w ,]+──',
        f'// ── PRICE DATA — Last updated: {today} ──',
        content
    )
    
    with open('index.html', 'w') as f:
        f.write(content)
    
    print(f"\nDone — updated {updated}/{len(prices)} tickers in index.html")
    return updated

if __name__ == '__main__':
    print(f"=== Price Update — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')} ===\n")
    
    prices = fetch_prices(TICKERS)
    
    if not prices:
        print("ERROR: No prices fetched. Aborting.")
        exit(1)
    
    update_html(prices)
    print("\nSuccess.")
