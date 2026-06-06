import requests
import pandas as pd
import os

RAW_DIR = "data/raw"

SCHEMES = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in SCHEMES.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data["data"])
    df.to_csv(f"{RAW_DIR}/live_{name}_nav.csv", index=False)
    print(f"Saved {name} — {len(df)} records")

print("Live NAV fetch complete!")
