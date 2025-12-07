# Aggregates KPIs across cleaned assets and writes summary CSV.
import pandas as pd
import os

CLEAN_DIR = 'data/cleaned'
OUT_DIR = 'data/analytics'
os.makedirs(OUT_DIR, exist_ok=True)

def compute_latest_kpis(df):
    last = df.iloc[-1]
    k = {}
    k['Latest_Close'] = last['Close']
    k['Latest_Return_pct'] = last['Daily_Return'] * 100
    vol30 = df['Daily_Return'].rolling(30).std().iloc[-1]
    k['30d_Volatility_annualized_pct'] = vol30 * (252**0.5) * 100 if not pd.isna(vol30) else None
    k['20d_MA'] = last.get('MA_20', None)
    k['50d_MA'] = last.get('MA_50', None)
    k['Latest_Spread_pct'] = last['Spread'] * 100 if 'Spread' in last else None
    return k

if __name__ == '__main__':
    rows = []
    for fname in os.listdir(CLEAN_DIR):
        if fname.endswith('_clean.csv'):
            df = pd.read_csv(os.path.join(CLEAN_DIR, fname), parse_dates=['Date'])
            k = compute_latest_kpis(df)
            k['asset'] = fname.replace('_clean.csv','')
            rows.append(k)
    out = pd.DataFrame(rows)
    out.to_csv(os.path.join(OUT_DIR, 'latest_kpis.csv'), index=False)
    print('Saved analytics/latest_kpis.csv')
