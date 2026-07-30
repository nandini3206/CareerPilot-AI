"""
CareerPilot AI
FAISS Index Builder
"""

import numpy as np

try:
    import faiss
    HAS_FAISS = True
except ImportError:
    HAS_FAISS = False

from career_recommendation.config import (
    EMBEDDINGS_FILE,
    EMBEDDING_DATA_DIR,
)

INDEX_FILE = EMBEDDING_DATA_DIR / "career_index.faiss"


class CareerFAISSIndex:

    def __init__(self):
        self.embeddings = None
        self.index = None

    def load_embeddings(self):
        print("=" * 60)
        print("Loading Career Embeddings")
        print("=" * 60)
        self.embeddings = np.load(EMBEDDINGS_FILE)
        self.embeddings = self.embeddings.astype("float32")
        print(f"Embeddings Shape : {self.embeddings.shape}")

    def build_index(self):
        if not HAS_FAISS:
            print("FAISS module unavailable; skipping index building.")
            return
        print("\nBuilding FAISS Index...")
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(self.embeddings)
        print(f"Indexed Jobs : {self.index.ntotal}")

    def save_index(self):
        if not HAS_FAISS or self.index is None:
            print("FAISS index unavailable; nothing to save.")
            return
        print("\nSaving Index...")
        faiss.write_index(
            self.index,
            str(INDEX_FILE)
        )
        print(f"Saved:\n{INDEX_FILE}")

    def run(self):
        self.load_embeddings()
        self.build_index()
        self.save_index()
        print("\nCareer FAISS Index processing completed.")


def main():
    builder = CareerFAISSIndex()
    builder.run()


if __name__ == "__main__":
    main()