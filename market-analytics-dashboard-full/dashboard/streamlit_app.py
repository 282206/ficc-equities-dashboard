# dashboard/streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title='Market Analytics Dashboard', layout='wide')
st.title('Multi-Asset Market Analytics Dashboard (FICC + Equities) - Data Analyst View')

CLEAN_DIR = 'data/cleaned'
assets = sorted([f.replace('_clean.csv','') for f in os.listdir(CLEAN_DIR) if f.endswith('_clean.csv')])

if not assets:
    st.warning('No cleaned assets found. Run data collection & cleaning notebooks first.')
else:
    asset = st.sidebar.selectbox('Choose asset', options=assets)
    df = pd.read_csv(os.path.join(CLEAN_DIR, asset + '_clean.csv'), parse_dates=['Date'])

    st.subheader(f'{asset.upper()} — Latest price & KPIs')
    latest = df.iloc[-1]
    c1, c2, c3 = st.columns(3)
    c1.metric('Latest Close', f"{latest['Close']:.2f}")
    c1.metric('Latest Daily Return (%)', f"{latest['Daily_Return']*100:.2f}")
    c2.metric('20d MA', f"{latest['MA_20']:.2f}" if not pd.isna(latest['MA_20']) else 'n/a')
    c2.metric('50d MA', f"{latest['MA_50']:.2f}" if not pd.isna(latest['MA_50']) else 'n/a')
    vol30 = df['Daily_Return'].rolling(30).std().iloc[-1]
    c3.metric('30d Volatility (ann., %)', f"{vol30*(252**0.5)*100:.2f}" if not pd.isna(vol30) else 'n/a')

    fig = px.line(df, x='Date', y='Close', title=f"{asset.upper()} Price")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader('Returns & Volatility')
    fig2 = px.line(df, x='Date', y='Daily_Return', title='Daily Returns')
    st.plotly_chart(fig2, use_container_width=True)

    # Correlation
    st.subheader('Correlation with other assets (returns)')
    other = st.multiselect('Compare with', options=[a for a in assets if a!=asset], default=assets[:2])
    if other:
        dfs = [df[['Date','Daily_Return']].rename(columns={'Daily_Return':asset})]
        for o in other:
            d = pd.read_csv(os.path.join(CLEAN_DIR, o + '_clean.csv'), parse_dates=['Date'])
            dfs.append(d[['Date','Daily_Return']].rename(columns={'Daily_Return':o}))
        merged = dfs[0]
        for d in dfs[1:]:
            merged = merged.merge(d, on='Date', how='inner')
        corr = merged.set_index('Date').corr()
        st.write(corr)
        fig3 = px.imshow(corr, text_auto=True, title='Return Correlation Matrix')
        st.plotly_chart(fig3, use_container_width=True)

st.sidebar.markdown('---')
if st.sidebar.button('Show top movers (latest day)'):
    rows = []
    for f in os.listdir('data/cleaned'):
        if f.endswith('_clean.csv'):
            d = pd.read_csv(os.path.join('data/cleaned', f), parse_dates=['Date'])
            rows.append({'asset': f.replace('_clean.csv',''), 'return_pct': float(d['Daily_Return'].iloc[-1]*100)})
    import pandas as pd
    out = pd.DataFrame(rows).sort_values('return_pct', ascending=False)
    st.write(out.head(20))
