# Cleans raw CSVs and produces cleaned CSVs in data/cleaned with KPI columns.
import pandas as pd
import os

RAW_DIR = 'data/equities'
CLEAN_DIR = 'data/cleaned'
os.makedirs(CLEAN_DIR, exist_ok=True)

def clean_equity(path_in, path_out):
    df = pd.read_csv(path_in, parse_dates=['Date'])
    df = df.dropna(subset=['Close'])
    df = df.sort_values('Date').reset_index(drop=True)
    df['Daily_Return'] = df['Close'].pct_change()
    df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod() - 1
    df['MA_20'] = df['Close'].rolling(20).mean()
    df['MA_50'] = df['Close'].rolling(50).mean()
    df['Volatility_7'] = df['Daily_Return'].rolling(7).std()
    df['Volatility_30'] = df['Daily_Return'].rolling(30).std()
    df['Spread'] = (df['High'] - df['Low']) / df['Close']
    df.to_csv(path_out, index=False)
    return df

if __name__ == '__main__':
    for fname in os.listdir(RAW_DIR):
        if fname.endswith('.csv'):
            name = fname.replace('.csv','')
            print('Cleaning', fname)
            clean_equity(os.path.join(RAW_DIR, fname), os.path.join(CLEAN_DIR, f'{name}_clean.csv'))
    print('Cleaning complete.')
