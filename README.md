# 🌍 Global Mental Health Trends Dashboard

This project analyzes and visualizes mental health trends globally using WHO API data.

## 🧠 Features
- Data fetching using WHO API
- Data cleaning and transformation in Python
- Data storage in SQLite
- Dashboard visualization with Streamlit
- Additional visualizations and analysis in R
- SQL-based insights generation

## 📦 Setup
```bash
pip install -r requirements.txt
python data_pipeline/fetch_data.py
python data_pipeline/clean_transform.py
python data_pipeline/store_to_sqlite.py
streamlit run dashboard/app.py
```

## 📊 R Analysis
Use `mental_health_analysis.R` for visualizing data trends and statistical summaries.

## 💾 SQL Queries
Find queries in `sql/queries.sql` for insights generation.
