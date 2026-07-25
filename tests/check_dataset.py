import pandas as pd

print("=" * 50)
print("CareerPilot AI - Dataset Checker")
print("=" * 50)

try:
    print("\nLoading dataset...")

    df = pd.read_csv(
        "datasets/role_prediction/raw/Resume.csv",
        encoding="utf-8"
    )

    print("✅ Dataset Loaded Successfully!")

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

except Exception as e:
    print("\n❌ ERROR:")
    print(type(e).__name__)
    print(e)