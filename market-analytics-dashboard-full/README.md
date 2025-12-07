# Multi-Asset Market Analytics Dashboard (FICC + Equities)

**Overview**
Beginner-friendly project that collects multi-asset market data (equities, forex, commodities, bond yields),
computes market-analytics KPIs (returns, volatility, spreads, correlations, yield-curve slope),
and exposes them through an interactive Streamlit dashboard and Python notebooks/scripts.

Generated on: 2025-12-07 16:04 UTC

**Folder structure**
```
market-analytics-dashboard-full/
├── data/
│   ├── equities/
│   ├── forex/
│   ├── commodities/
│   ├── bonds/
│   └── cleaned/
├── notebooks/
├── dashboard/
├── docs/
├── README.md
└── requirements.txt
```

**How to run**
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. (Optional) Populate API keys (AlphaVantage, FRED) if you use those sources.
3. Run data collection scripts or use the notebooks (not required — demo cleaned CSVs are included).
4. Launch dashboard:
   ```
   streamlit run dashboard/streamlit_app.py
   ```

**KPIs computed**
- Daily Return, Cumulative Return
- Moving Averages (20, 50)
- Rolling Volatility (7, 30)
- Spread (High-Low / Close)
- Amihud Illiquidity proxy
- Correlation matrix
- Yield curve slope (10Y - 2Y)

