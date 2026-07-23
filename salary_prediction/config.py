"""
=========================================================
CareerPilot AI V2
Salary Prediction Configuration
=========================================================
Author : Nandini Bhatt
Module : Salary Prediction
=========================================================
"""

from pathlib import Path

# =========================================================
# Project Paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_DIR = PROJECT_ROOT / "datasets" / "salary_prediction"
RAW_DATA_DIR = DATASET_DIR / "raw"
PROCESSED_DATA_DIR = DATASET_DIR / "processed"

MODELS_DIR = PROJECT_ROOT / "models" / "salary_prediction"

# =========================================================
# Dataset
# =========================================================

DATASET_PATH = RAW_DATA_DIR / "salaries.csv"
PROCESSED_DATASET = PROCESSED_DATA_DIR / "processed_salary.csv"

# =========================================================
# Saved Files
# =========================================================

MODEL_PATH = MODELS_DIR / "salary_model.pkl"
PIPELINE_PATH = MODELS_DIR / "preprocessing_pipeline.pkl"

METRICS_PATH = MODELS_DIR / "metrics.json"

# =========================================================
# Dataset Columns
# =========================================================

TARGET_COLUMN = "salary_in_usd"

FEATURE_COLUMNS = [

    "experience_level",
    "employment_type",
    "job_title",
    "employee_residence",
    "remote_ratio",
    "company_location",
    "company_size",

]

# =========================================================
# Training Parameters
# =========================================================

TEST_SIZE = 0.20

RANDOM_STATE = 42

N_ESTIMATORS = 300

MAX_DEPTH = 20

MIN_SAMPLES_SPLIT = 2

MIN_SAMPLES_LEAF = 1

# =========================================================
# Create Required Directories
# =========================================================

MODELS_DIR.mkdir(parents=True, exist_ok=True)

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)