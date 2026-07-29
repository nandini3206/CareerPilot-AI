from pathlib import Path
import pandas as pd
import re

# ==========================
# Project Paths & Config Import
# ==========================
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATASET = PROJECT_ROOT / "datasets" / "role_prediction" / "raw" / "Resume.csv"

PROCESSED_ORIGINAL_DATASET = (
    PROJECT_ROOT
    / "datasets"
    / "role_prediction"
    / "processed"
    / "processed_resume.csv"
)

PROCESSED_TECH_DATASET = (
    PROJECT_ROOT
    / "datasets"
    / "role_prediction"
    / "processed"
    / "processed_tech_resume.csv"
)


# ==========================
# Load Raw Dataset
# ==========================
def load_dataset():
    print("=" * 60)
    print("CareerPilot AI - Resume Preprocessor")
    print("=" * 60)
    print(f"\nLoading dataset:\n{RAW_DATASET}")

    df = pd.read_csv(RAW_DATASET)

    print("\n[OK] Dataset Loaded Successfully!")
    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    return df


# ==========================
# Clean Resume Text (Original intact)
# ==========================
def clean_resume(text):
    """
    Cleans resume text for NLP processing.
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
    # Keep letters, numbers, and technical symbols
    text = re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text)
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip().lower()


# ==========================
# Original Preprocessing Pipeline (Intact)
# ==========================
def preprocess_dataset(df):
    """
    Original pipeline preserving raw 24 broad categories.
    """
    print("\nCleaning resume text for original pipeline...")

    df = df.copy()
    df["clean_resume"] = (
        df["Resume_str"]
        .fillna("")
        .astype(str)
        .apply(clean_resume)
    )

    print("[OK] Original resume text cleaned!")
    return df


# ==========================
# Fine-Grained Tech Role Preprocessing Pipeline
# ==========================
def map_tech_role(row):
    """
    Deterministic rule-based mapping function that classifies real human resumes
    from Resume.csv into fine-grained modern tech roles using word-boundary regex matches.
    """
    t = str(row.get("clean_resume", "")).lower()
    cat = str(row.get("Category", "")).upper()

    def matches(keywords):
        for kw in keywords:
            if re.search(r"\b" + re.escape(kw) + r"\b", t):
                return True
        return False

    if matches(["machine learning", "mlops", "scikit-learn", "deep learning", "neural network", "computer vision", "pytorch", "tensorflow"]):
        return "Machine Learning Engineer"
    if matches(["llm", "langchain", "rag", "prompt engineering", "vector database", "openai", "faiss", "pinecone", "generative ai"]):
        return "AI Engineer"
    if matches(["data engineer", "etl", "pyspark", "hadoop", "data pipeline", "airflow", "bigquery", "snowflake", "redshift", "kafka"]):
        return "Data Engineer"
    if matches(["data science", "data scientist", "predictive modeling", "tableau", "power bi"]) or (cat == "INFORMATION-TECHNOLOGY" and matches(["pandas", "statistics", "numpy"])):
        return "Data Scientist"
    if matches(["devops", "kubernetes", "ci/cd", "terraform", "ansible", "cloud engineer"]) or (cat == "ENGINEERING" and matches(["aws", "azure", "gcp", "docker"])):
        return "DevOps & Cloud Engineer"
    if matches(["backend", "django", "fastapi", "flask", "postgresql", "mongodb", "rest api", "microservices", "redis"]):
        return "Backend Developer"
    if cat == "DESIGNER" or matches(["figma", "ui/ux", "wireframing", "user research", "adobe xd", "prototyping"]):
        return "UI/UX & Product Designer"
    if matches(["full stack", "react", "angular", "vue", "typescript"]) and cat in ["INFORMATION-TECHNOLOGY", "ENGINEERING"]:
        return "Full Stack Engineer"
    if cat in ["INFORMATION-TECHNOLOGY", "ENGINEERING"]:
        return "Software Engineer"
    return None


def preprocess_tech_roles_dataset(df):
    """
    Curated Tech Role Preprocessing Pipeline.
    Filters real human resumes from tech/engineering categories and applies deterministic
    skill mapping into fine-grained modern technology roles.
    """
    print("\nProcessing curated tech roles pipeline...")
    df = df.copy()
    df["clean_resume"] = df["Resume_str"].fillna("").astype(str).apply(clean_resume)

    # Filter tech-relevant categories from Resume.csv
    tech_categories = ["INFORMATION-TECHNOLOGY", "ENGINEERING", "DESIGNER", "DIGITAL-MEDIA", "BUSINESS-DEVELOPMENT", "CONSULTANT", "FINANCE"]
    tech_df = df[df["Category"].isin(tech_categories)].copy()

    # Map each resume to a specific tech role
    tech_df["Category"] = tech_df.apply(map_tech_role, axis=1)

    # Drop unmapped non-tech rows
    tech_df = tech_df.dropna(subset=["Category"]).copy()

    # Filter classes with at least 5 samples
    valid_cats = tech_df["Category"].value_counts()[tech_df["Category"].value_counts() >= 5].index
    tech_df = tech_df[tech_df["Category"].isin(valid_cats)].copy()

    # Cap largest classes at 40 to maintain balanced training weight
    tech_df = tech_df.groupby("Category").head(40).reset_index(drop=True)

    print("[OK] Curated tech-role dataset created!")
    print("Class Distribution:")
    print(tech_df["Category"].value_counts())

    return tech_df


# ==========================
# Save Processed Datasets
# ==========================
def save_datasets(orig_df, tech_df):
    PROCESSED_ORIGINAL_DATASET.parent.mkdir(parents=True, exist_ok=True)

    orig_df.to_csv(PROCESSED_ORIGINAL_DATASET, index=False)
    print(f"\n[OK] Original dataset saved at:\n{PROCESSED_ORIGINAL_DATASET}")

    tech_df.to_csv(PROCESSED_TECH_DATASET, index=False)
    print(f"[OK] Curated Tech-Role dataset saved at:\n{PROCESSED_TECH_DATASET}")


# ==========================
# Main Execution
# ==========================
if __name__ == "__main__":
    raw_df = load_dataset()

    # Process original dataset (intact)
    processed_orig_df = preprocess_dataset(raw_df)

    # Process curated tech roles dataset
    processed_tech_df = preprocess_tech_roles_dataset(raw_df)

    # Save both datasets cleanly
    save_datasets(processed_orig_df, processed_tech_df)

    print("\n[SUCCESS] Dual Preprocessing Completed Successfully!")