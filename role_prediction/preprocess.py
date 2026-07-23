from pathlib import Path
import pandas as pd
import re


# ==========================
# Project Paths
# ==========================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATASET = PROJECT_ROOT / "datasets" / "role_prediction" / "raw" / "Resume.csv"

PROCESSED_DATASET = (
    PROJECT_ROOT
    / "datasets"
    / "role_prediction"
    / "processed"
    / "processed_resume.csv"
)


# ==========================
# Load Dataset
# ==========================

def load_dataset():
    print("=" * 60)
    print("CareerPilot AI - Resume Preprocessor")
    print("=" * 60)

    print(f"\nLoading dataset:\n{RAW_DATASET}")

    df = pd.read_csv(RAW_DATASET)

    print("\n✅ Dataset Loaded Successfully!")

    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    return df


# ==========================
# Clean Resume Text
# ==========================

def clean_resume(text):
    """
    Cleans resume text for NLP.
    """

    if pd.isna(text):
        return ""

    text = str(text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove phone numbers
    text = re.sub(r"\+?\d[\d\s\-()]{8,}\d", " ", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)

    # Keep letters, numbers and common programming symbols
    text = re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip().lower()


# ==========================
# Preprocess Dataset
# ==========================

def preprocess_dataset(df):

    print("\nCleaning resume text...")

    df = df.copy()

    df["clean_resume"] = (
        df["Resume_str"]
        .fillna("")
        .astype(str)
        .apply(clean_resume)
    )

    print("✅ Resume text cleaned!")

    return df


# ==========================
# Save Dataset
# ==========================

def save_dataset(df):

    df.to_csv(PROCESSED_DATASET, index=False)

    print("\n✅ Processed dataset saved!")

    print(f"\nSaved at:\n{PROCESSED_DATASET}")


# ==========================
# Main
# ==========================

if __name__ == "__main__":

    df = load_dataset()

    processed_df = preprocess_dataset(df)

    save_dataset(processed_df)

    print("\n🎉 Preprocessing Completed Successfully!")