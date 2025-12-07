# Multi-Asset Market Analytics Dashboard (FICC + Equities)

**Overview**  
This project is a **Python-based multi-asset market analytics dashboard** designed for **FICC (Fixed Income, Currencies, Commodities) and Equities**.  
It collects, cleans, and analyzes market data, computes key financial KPIs, and presents insights through interactive dashboards, simulating real-world workflows in **sales & trading and quantitative analysis**.

---

## Features

- **Data Collection**
  - Equities (AAPL, MSFT, INFY, TCS, NIFTY)
  - FX, Commodities, Bonds (placeholders for future expansion)
  - Supports APIs: `yfinance`, `AlphaVantage`, `FRED`  

- **Data Cleaning & Feature Engineering**
  - Daily Return, Cumulative Return
  - Moving Averages (20-day, 50-day)
  - Rolling Volatility (7-day, 30-day)
  - Spread (High-Low / Close)
  - Amihud Illiquidity proxy
  - Cleans and stores data in `data/cleaned/`  

- **Analytics**
  - Aggregates KPIs across assets
  - Produces `latest_kpis.csv` summary
  - Computes correlations between asset returns  

- **Visualizations**
  - Price trends, returns, rolling volatility
  - Interactive correlation matrices using Plotly

- **Interactive Dashboard**
  - Built with Streamlit
  - Select assets, view metrics, visualize trends
  - Display top movers (highest daily returns)
  - Real-time interaction with multiple assets

- **Documentation**
  - `docs/KPI_definitions.md` explains each financial metric

---

## Project Structure

market-analytics-dashboard-full/
├── data/
│ ├── equities/
│ ├── forex/
│ ├── commodities/
│ ├── bonds/
│ └── cleaned/
├── notebooks/ # Python scripts to fetch, clean, analyze data
├── dashboard/ # Streamlit interactive dashboard
├── docs/ # KPI definitions
├── README.md
├── requirements.txt
└── generate_market_project.py # Generates the project structure & demo data
---

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
python notebooks/01_data_collection.py
python notebooks/02_data_cleaning.py
python notebooks/03_kpi_calculations.py
python notebooks/04_visualizations.py
streamlit run dashboard/streamlit_app.py


KPIs Computed

Daily Return: (P_t - P_{t-1}) / P_{t-1}
Cumulative Return: Product of (1 + daily returns) - 1
Moving Averages: 20-day and 50-day simple moving averages
Rolling Volatility: 7-day and 30-day standard deviation of returns
Spread: (High - Low) / Close
Amihud Illiquidity Proxy: |Return| / Volume
Correlation Matrix: Pearson correlation of daily returns
Yield Curve Slope: 10Y yield - 2Y yield (placeholder for bonds)

Technologies Used

Python, Pandas, NumPy
Plotly for interactive visualizations
Streamlit for the dashboard
finance, AlphaVantage, FRED API (data sources)

License

This project is licensed under the MIT License.
