"""
====================================================
CareerPilot AI V2
Role Prediction Predictor
====================================================
"""

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize

try:
    from role_prediction.config import EMBEDDING_MODEL
    from role_prediction.model_loader import load_all
except ImportError:
    from config import EMBEDDING_MODEL
    from model_loader import load_all


class RolePredictor:

    def __init__(self):
        print("Loading Role Prediction Model...")
        self.model, self.encoder = load_all()
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)
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
        resume_text = self.preprocess(resume_text)
        embedding = self.create_embedding(resume_text)
        prediction = self.model.predict(embedding)[0]
        role = self.encoder.inverse_transform([prediction])[0]
        return role

    def predict_top_k(self, resume_text, k=3):
        """
        Returns top-k predicted roles with normalized confidence percentages.
        """
        resume_text = self.preprocess(resume_text)
        embedding = self.create_embedding(resume_text)

        if hasattr(self.model, "decision_function"):
            scores = self.model.decision_function(embedding)
            if scores.ndim > 1:
                scores = scores[0]
            exp_scores = np.exp(scores - np.max(scores))
            probs = exp_scores / np.sum(exp_scores)
        else:
            probs = self.model.predict_proba(embedding)[0]

        top_indices = np.argsort(probs)[::-1][:k]
        top_roles = self.encoder.inverse_transform(top_indices)
        top_probs = probs[top_indices]

        return [
            {"role": role, "confidence": round(float(prob) * 100, 2)}
            for role, prob in zip(top_roles, top_probs)
        ]
