"""
CareerPilot AI
FAISS Index Builder
"""

import faiss
import numpy as np

from config import (
    EMBEDDINGS_FILE,
    EMBEDDING_DATA_DIR,
)

INDEX_FILE = EMBEDDING_DATA_DIR / "career_index.faiss"


class CareerFAISSIndex:

    def __init__(self):

        self.embeddings = None
        self.index = None

    # ==========================================================
    # Load Embeddings
    # ==========================================================

    def load_embeddings(self):

        print("=" * 60)
        print("Loading Career Embeddings")
        print("=" * 60)

        self.embeddings = np.load(EMBEDDINGS_FILE)

        self.embeddings = self.embeddings.astype("float32")

        print(f"Embeddings Shape : {self.embeddings.shape}")

    # ==========================================================
    # Build Index
    # ==========================================================

    def build_index(self):

        print("\nBuilding FAISS Index...")

        dimension = self.embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(self.embeddings)

        print(f"Indexed Jobs : {self.index.ntotal}")

    # ==========================================================
    # Save Index
    # ==========================================================

    def save_index(self):

        print("\nSaving Index...")

        faiss.write_index(
            self.index,
            str(INDEX_FILE)
        )

        print(f"Saved:\n{INDEX_FILE}")

    # ==========================================================
    # Run
    # ==========================================================

    def run(self):

        self.load_embeddings()

        self.build_index()

        self.save_index()

        print("\nCareer FAISS Index Created Successfully.")


def main():

    builder = CareerFAISSIndex()

    builder.run()


if __name__ == "__main__":

    main()