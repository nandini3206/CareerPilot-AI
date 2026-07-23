"""
CareerPilot AI
Career Recommendation Embedding Engine
"""

import time
import joblib
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer

from config import (
    MERGED_DATASET,
    EMBEDDINGS_FILE,
    METADATA_FILE,
    EMBEDDING_MODEL,
)


class CareerEmbeddingEngine:

    def __init__(self):

        self.model = None
        self.dataset = None
        self.embeddings = None

    # ==========================================================
    # Load Model
    # ==========================================================

    def load_model(self):

        print("=" * 60)
        print("Loading Sentence Transformer")
        print("=" * 60)

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        print(f"Model Loaded : {EMBEDDING_MODEL}")

    # ==========================================================
    # Load Dataset
    # ==========================================================

    def load_dataset(self):

        print("\nLoading processed dataset...")

        self.dataset = pd.read_csv(MERGED_DATASET)

        print(f"Rows : {len(self.dataset)}")

        if "embedding_text" not in self.dataset.columns:
            raise ValueError("embedding_text column not found.")

    # ==========================================================
    # Prepare Text
    # ==========================================================

    def prepare_text(self):

        print("\nPreparing text...")

        self.dataset["embedding_text"] = (

            self.dataset["embedding_text"]

            .fillna("")

            .astype(str)

        )

        print("Text preparation completed.")
    # ==========================================================
    # Generate Embeddings
    # ==========================================================

    def generate_embeddings(self):

        print("\nGenerating embeddings...")

        texts = self.dataset["embedding_text"].tolist()

        start_time = time.time()

        self.embeddings = self.model.encode(
            texts,
            batch_size=256,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        end_time = time.time()

        print(f"\nEmbeddings Generated : {len(self.embeddings)}")
        print(f"Shape                : {self.embeddings.shape}")
        print(f"Time Taken           : {end_time - start_time:.2f} seconds")

    # ==========================================================
    # Save Embeddings
    # ==========================================================

    def save_embeddings(self):

        print("\nSaving embeddings...")

        np.save(
            EMBEDDINGS_FILE,
            self.embeddings
        )

        print(f"Saved:\n{EMBEDDINGS_FILE}")

    # ==========================================================
    # Save Metadata
    # ==========================================================

    def save_metadata(self):

        print("\nSaving metadata...")

        metadata_columns = [
            "job_link",
            "title",
            "company",
            "location",
            "country",
            "experience_level",
            "employment_type",
            "job_skills",
            "job_summary",
        ]

        available_columns = [
            column
            for column in metadata_columns
            if column in self.dataset.columns
        ]

        metadata = self.dataset[
            available_columns
        ].copy()

        joblib.dump(
            metadata,
            METADATA_FILE
        )

        print(f"Saved:\n{METADATA_FILE}")

    # ==========================================================
    # Run Pipeline
    # ==========================================================

    def run(self):

        self.load_model()

        self.load_dataset()

        self.prepare_text()

        self.generate_embeddings()

        self.save_embeddings()

        self.save_metadata()

        print("\nCareer Recommendation Embeddings Created Successfully.")

# ==========================================================
# Main
# ==========================================================

def main():

    engine = CareerEmbeddingEngine()

    engine.run()


if __name__ == "__main__":

    main()