# Example visualization using Plotly
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/cleaned/aapl_clean.csv', parse_dates=['Date'])
fig = px.line(df, x='Date', y='Close', title='AAPL Price')
fig.show()

# Correlation heatmap example
assets = ['aapl','infy','tcs']
dfs = []
for a in assets:
    try:
        d = pd.read_csv(f'data/cleaned/{a}_clean.csv', parse_dates=['Date'])
        d = d[['Date','Daily_Return']].rename(columns={'Daily_Return':a})
        dfs.append(d)
    except Exception as e:
        print('Missing', a)
if dfs:
    merged = dfs[0]
    for d in dfs[1:]:
        merged = merged.merge(d, on='Date', how='inner')
    corr = merged.set_index('Date').corr()
    fig2 = px.imshow(corr, text_auto=True, title='Return Correlation Matrix')
    fig2.show()
