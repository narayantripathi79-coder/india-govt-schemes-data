import pandas as pd
from datetime import date

# Demo structured data (proof of concept)
schemes = [
    {
        "scheme_id": "pm_awas_yojana",
        "scheme_name": "Pradhan Mantri Awas Yojana",
        "category": "Social Welfare",
        "beneficiary_type": "All",
        "eligibility": "Economically weaker sections",
        "benefits": "Housing assistance",
        "funding_type": "Central",
        "state": "All India",
        "launch_year": 2015,
        "source_url": "https://www.myscheme.gov.in",
        "last_updated": str(date.today())
    }
]

df = pd.DataFrame(schemes)

df.to_csv("data/processed/govt_schemes.csv", index=False)
df.to_json("data/processed/govt_schemes.json", orient="records", indent=2)

print("✅ Government schemes data structured successfully")
