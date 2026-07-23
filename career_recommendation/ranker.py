"""
CareerPilot AI
Career Recommendation Ranker
"""

import faiss
import numpy as np

from config import EMBEDDING_DATA_DIR

INDEX_FILE = EMBEDDING_DATA_DIR / "career_index.faiss"


class CareerRanker:

    def __init__(self, model, metadata):

        self.model = model
        self.metadata = metadata

        self.index = None

    # ==========================================================
    # Load FAISS Index
    # ==========================================================

    def load_index(self):

        print("Loading FAISS Index...")

        self.index = faiss.read_index(
            str(INDEX_FILE)
        )

        print(f"Indexed Jobs : {self.index.ntotal}")

    # ==========================================================
    # Create Query Embedding
    # ==========================================================

    def encode_query(self, query):

        embedding = self.model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.astype("float32")

    # ==========================================================
    # Semantic Search
    # ==========================================================

    def semantic_search(
        self,
        query,
        top_k=100,
    ):

        embedding = self.encode_query(query)

        scores, indices = self.index.search(
            embedding,
            top_k,
        )

        return scores[0], indices[0]
    # ==========================================================
    # Calculate CareerPilot Match Score
    # ==========================================================

    def calculate_score(
        self,
        similarity_score,
        job,
        skills=None,
        preferred_location=None,
        preferred_employment=None,
        experience_level=None,
    ):

        semantic_score = float(similarity_score) * 100

        semantic_score = max(0, min(100, semantic_score))

        # ------------------------------------------------------

        skill_score = 100

        if skills:

            job_skills = str(
                job.get("job_skills", "")
            ).lower()

            matched = 0

            for skill in skills:

                if skill.lower() in job_skills:
                    matched += 1

            skill_score = (
                matched / len(skills)
            ) * 100

        # ------------------------------------------------------

        experience_score = 100

        if experience_level:

            job_exp = str(
                job.get("experience_level", "")
            ).lower()

            if experience_level.lower() not in job_exp:
                experience_score = 50

        # ------------------------------------------------------

        location_score = 100

        if preferred_location:

            job_location = (

                str(job.get("location", ""))

                + " "

                + str(job.get("country", ""))

            ).lower()

            if preferred_location.lower() not in job_location:

                location_score = 50

        # ------------------------------------------------------

        employment_score = 100

        if preferred_employment:

            job_type = str(
                job.get(
                    "employment_type",
                    ""
                )
            ).lower()

            if preferred_employment.lower() not in job_type:

                employment_score = 50

        # ------------------------------------------------------

        final_score = (

            semantic_score * 0.60

            + skill_score * 0.20

            + experience_score * 0.10

            + location_score * 0.05

            + employment_score * 0.05

        )

        return round(final_score, 2)

    # ==========================================================
    # Rank Jobs
    # ==========================================================

    def rank_jobs(
        self,
        query,
        skills=None,
        preferred_location=None,
        preferred_employment=None,
        experience_level=None,
        top_k=20,
    ):

        scores, indices = self.semantic_search(
            query=query,
            top_k=100,
        )

        recommendations = []

        for similarity, index in zip(scores, indices):

            if index == -1:
                continue

            job = self.metadata.iloc[index].copy()

            score = self.calculate_score(
                similarity_score=similarity,
                job=job,
                skills=skills,
                preferred_location=preferred_location,
                preferred_employment=preferred_employment,
                experience_level=experience_level,
            )

            job["careerpilot_score"] = score

            recommendations.append(job)

        recommendations = sorted(
            recommendations,
            key=lambda x: x["careerpilot_score"],
            reverse=True,
        )

        return recommendations[:top_k]




    