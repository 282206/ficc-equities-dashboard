# Produces a text summary of top movers and basic commentary.
import pandas as pd
import os

CLEAN_DIR = 'data/cleaned'

def top_movers(n=5):
    rows = []
    for fname in os.listdir(CLEAN_DIR):
        if fname.endswith('_clean.csv'):
            df = pd.read_csv(os.path.join(CLEAN_DIR, fname), parse_dates=['Date'])
            last = df.iloc[-1]
            rows.append({'asset': fname.replace('_clean.csv',''), 'return_pct': float(last['Daily_Return']*100)})
    out = pd.DataFrame(rows).sort_values('return_pct', ascending=False)
    return out

if __name__ == '__main__':
    movers = top_movers(10)
    print('Top movers (latest daily return pct):')
    print(movers.head(10).to_string(index=False))
