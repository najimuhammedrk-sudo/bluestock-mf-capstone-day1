import pandas as pd
import numpy as np
import os

RAW_DIR = "data/raw"

CSV_FILES = {
    "fund_master": "01_fund_master.csv",
    "nav_history": "02_nav_history.csv",
    "aum_data": "03_aum_by_fund_house.csv",
    "sip_data": "04_monthly_sip_inflows.csv",
    "category_inflows": "05_category_inflows.csv",
    "folio_count": "06_industry_folio_count.csv",
    "performance": "07_scheme_performance.csv",
    "transactions": "08_investor_transactions.csv",
    "portfolio": "09_portfolio_holdings.csv",
    "benchmark": "10_benchmark_indices.csv"
}

print("Loading all 10 datasets...")
for label, filename in CSV_FILES.items():
    filepath = os.path.join(RAW_DIR, filename)
    df = pd.read_csv(filepath)
    print(f"{label}: {df.shape} | Nulls: {df.isnull().sum().sum()}")

print("Data ingestion complete!")
