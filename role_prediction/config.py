from pathlib import Path

# ==========================
# Project Root
# ==========================
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================
# Dataset Mode Configuration
# Options: "tech_roles" (default, fine-grained tech roles) or "original" (24 legacy broad domains)
# ==========================
DATASET_MODE = "tech_roles"

# ==========================
# Dataset Paths
# ==========================
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

# Active dataset path based on DATASET_MODE
PROCESSED_DATASET = PROCESSED_TECH_DATASET if DATASET_MODE == "tech_roles" else PROCESSED_ORIGINAL_DATASET

# ==========================
# Model Paths
# ==========================
MODEL_DIR = PROJECT_ROOT / "models" / "role_prediction"
BEST_MODEL = MODEL_DIR / "best_model.pkl"
LABEL_ENCODER = MODEL_DIR / "label_encoder.pkl"
METRICS = MODEL_DIR / "metrics.json"

# ==========================
# Embeddings Path
# ==========================
EMBEDDINGS = PROJECT_ROOT / "embeddings" / f"role_prediction_{DATASET_MODE}_embeddings.npy"

# ==========================
# Sentence Transformer Model
# ==========================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
