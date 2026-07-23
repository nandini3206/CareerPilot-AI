from pathlib import Path

# ==========================
# Project Root
# ==========================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================
# Dataset Paths
# ==========================

RAW_DATASET = PROJECT_ROOT / "datasets" / "role_prediction" / "raw" / "Resume.csv"

PROCESSED_DATASET = (
    PROJECT_ROOT
    / "datasets"
    / "role_prediction"
    / "processed"
    / "processed_resume.csv"
)

# ==========================
# Model Paths
# ==========================

MODEL_DIR = PROJECT_ROOT / "models" / "role_prediction"

BEST_MODEL = MODEL_DIR / "best_model.pkl"

LABEL_ENCODER = MODEL_DIR / "label_encoder.pkl"

METRICS = MODEL_DIR / "metrics.json"

# ==========================
# Embeddings
# ==========================
EMBEDDINGS = PROJECT_ROOT / "embeddings" / "role_prediction_embeddings.npy"
# ==========================
# Sentence Transformer
# ==========================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


