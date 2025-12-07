# Data collection script (yfinance for equities; placeholders for FX/commodities/bonds)
import yfinance as yf
import os

os.makedirs('data/equities', exist_ok=True)

EQUITIES = {
    'AAPL': 'AAPL',
    'MSFT': 'MSFT',
    'INFY': 'INFY.NS',
    'TCS': 'TCS.NS',
    'NIFTY': '^NSEI'
}

def fetch_equities(equities, start='2020-01-01', end=None, interval='1d'):
    for name, symbol in equities.items():
        print(f"Fetching {name} ({symbol})...")
        df = yf.download(symbol, start=start, end=end, interval=interval, progress=False)
        if df.empty:
            print(f"Warning: no data for {symbol}")
            continue
        df.reset_index(inplace=True)
        df.to_csv(f"data/equities/{name.lower()}.csv", index=False)
        print(f"Saved data/equities/{name.lower()}.csv")

if __name__ == '__main__':
    fetch_equities(EQUITIES)
    print('Done. Add FX/commodities/bonds collection as needed.')
