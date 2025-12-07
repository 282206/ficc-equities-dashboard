# Multi-Asset Market Analytics Dashboard (FICC + Equities)

This repository contains a generator script and a ready-to-use demo project
for a multi-asset market analytics dashboard (equities, forex, commodities, bonds).

Files of interest:
- `generate_market_project.py` — script that scaffolds a demo project at
  `market-analytics-dashboard-full/` and creates a ZIP archive.
- `market-analytics-dashboard-full/` — generated demo project (created when you run the script).

Quick start:

```bash
python generate_market_project.py
```

Then install dependencies and run the dashboard:

```bash
pip install -r market-analytics-dashboard-full/requirements.txt
streamlit run market-analytics-dashboard-full/dashboard/streamlit_app.py
```

Notes:
- The generator writes demo cleaned CSVs so the dashboard works without external APIs.
- Re-running `generate_market_project.py` will replace the `market-analytics-dashboard-full/` folder.

If you want, I can run the generator and stage the resulting files for commit.
