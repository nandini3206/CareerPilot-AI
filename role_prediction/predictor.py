"""
====================================================
CareerPilot AI V2
Role Prediction Predictor
====================================================
"""

import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize

from config import EMBEDDING_MODEL
from model_loader import load_all


class RolePredictor:

    def __init__(self):

        print("Loading Role Prediction Model...")

        self.model, self.encoder = load_all()

        self.embedding_model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        print("Model Loaded Successfully!")

    def preprocess(self, resume_text):

        if resume_text is None:
            return ""

        return str(resume_text).strip()

    def create_embedding(self, resume_text):

        embedding = self.embedding_model.encode(
            [resume_text],
            convert_to_numpy=True,
        )

        embedding = normalize(
            embedding,
            norm="l2",
        )

        return embedding

    def predict(self, resume_text):

        resume_text = self.preprocess(
            resume_text
        )

        embedding = self.create_embedding(
            resume_text
        )

        prediction = self.model.predict(
            embedding
        )[0]

        role = self.encoder.inverse_transform(
            [prediction]
        )[0]

        return role

