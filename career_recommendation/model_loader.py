"""
CareerPilot AI
Career Recommendation Model Loader
"""

import joblib
import numpy as np

from sentence_transformers import SentenceTransformer

from config import (
    EMBEDDINGS_FILE,
    METADATA_FILE,
    EMBEDDING_MODEL,
)


class CareerModelLoader:

    def __init__(self):

        self.model = None
        self.embeddings = None
        self.metadata = None

    # ==========================================================
    # Load Sentence Transformer
    # ==========================================================

    def load_model(self):

        if self.model is None:

            print("Loading SentenceTransformer...")

            self.model = SentenceTransformer(
                EMBEDDING_MODEL
            )

            print("Model Loaded Successfully.")

        return self.model

    # ==========================================================
    # Load Embeddings
    # ==========================================================

    def load_embeddings(self):

        if self.embeddings is None:

            print("Loading Career Embeddings...")

            self.embeddings = np.load(
                EMBEDDINGS_FILE
            )

            print(
                f"Embeddings Loaded : {self.embeddings.shape}"
            )

        return self.embeddings

    # ==========================================================
    # Load Metadata
    # ==========================================================

    def load_metadata(self):

        if self.metadata is None:

            print("Loading Career Metadata...")

            self.metadata = joblib.load(
                METADATA_FILE
            )

            print(
                f"Metadata Loaded : {len(self.metadata)}"
            )

        return self.metadata

    # ==========================================================
    # Load Everything
    # ==========================================================

    def load_all(self):

        self.load_model()

        self.load_embeddings()

        self.load_metadata()

        print("\nCareer Recommendation Assets Ready.")

        return (
            self.model,
            self.embeddings,
            self.metadata,
        )


# ==========================================================
# Main
# ==========================================================

def main():

    loader = CareerModelLoader()

    loader.load_all()


if __name__ == "__main__":

    main()