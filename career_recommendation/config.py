"""
CareerPilot AI
Career Recommendation Configuration
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# Project Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ============================================================
# Dataset Paths
# ============================================================

DATASET_DIR = PROJECT_ROOT / "datasets" / "internship_recommendation"

RAW_DATA_DIR = DATASET_DIR / "raw"
PROCESSED_DATA_DIR = DATASET_DIR / "processed"
EMBEDDING_DATA_DIR = DATASET_DIR / "embeddings"

# ============================================================
# Raw Dataset Files
# ============================================================

JOBS_IN_DATA = RAW_DATA_DIR / "jobs_in_data.csv"

INDIA_SALARY_DATA = RAW_DATA_DIR / "Data_Science_Jobs_in_India.csv"

DATA_SCIENCE_JOBS = RAW_DATA_DIR / "Data_Science_Jobs.csv"

JOB_POSTINGS = RAW_DATA_DIR / "job_postings.csv"

JOB_SKILLS = RAW_DATA_DIR / "job_skills.csv"

JOB_SUMMARY = RAW_DATA_DIR / "job_summary.csv"

# ============================================================
# Processed Files
# ============================================================

MERGED_DATASET = PROCESSED_DATA_DIR / "career_jobs.csv"

EMBEDDINGS_FILE = EMBEDDING_DATA_DIR / "career_embeddings.npy"

METADATA_FILE = EMBEDDING_DATA_DIR / "career_metadata.pkl"

# ============================================================
# Embedding Model
# ============================================================

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ============================================================
# Recommendation Settings
# ============================================================

TOP_K_RESULTS = 20

SIMILARITY_THRESHOLD = 0.35

# ============================================================
# Adzuna Configuration
# ============================================================

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")

ADZUNA_API_KEY = os.getenv("ADZUNA_API_KEY")

# India = "in"
# UK = "gb"
# US = "us"

ADZUNA_COUNTRY = "in"

DEFAULT_RESULTS = 20

# ============================================================
# Create Required Folders
# ============================================================

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

EMBEDDING_DATA_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    print("Career Recommendation Configuration")

    print("\nRaw Dataset Directory")
    print(RAW_DATA_DIR)

    print("\nProcessed Dataset")
    print(MERGED_DATASET)

    print("\nEmbedding Directory")
    print(EMBEDDING_DATA_DIR)

    print("\nConfiguration Loaded Successfully.")

   