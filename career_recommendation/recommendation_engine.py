"""
CareerPilot AI
Career Recommendation Engine — Upgraded Dynamic Multi-Source Fusion
"""

import numpy as np
from typing import Dict, List, Any, Optional
from model_loader import CareerModelLoader
from ranker import CareerRanker


class CareerRecommendationEngine:

    def __init__(self):
        self.loader = CareerModelLoader()
        self.model = None
        self.embeddings = None
        self.metadata = None
        self.ranker = None

    def load(self):
        (
            self.model,
            self.embeddings,
            self.metadata,
        ) = self.loader.load_all()

        self.ranker = CareerRanker(
            model=self.model,
            metadata=self.metadata,
            embeddings=self.embeddings,
        )
        self.ranker.load_index()
        print("\nCareer Recommendation Engine Ready.")

    def recommend_local(
        self,
        query: str,
        skills: Optional[List[str]] = None,
        predicted_role: Optional[str] = None,
        predicted_salary: Optional[Any] = None,
        resume_text: Optional[str] = None,
        preferred_location: Optional[str] = None,
        preferred_employment: Optional[str] = None,
        experience_level: Optional[str] = None,
        top_k: int = 20,
    ) -> List[Dict[str, Any]]:

        return self.ranker.rank_jobs(
            query=query,
            skills=skills,
            predicted_role=predicted_role,
            predicted_salary=predicted_salary,
            resume_text=resume_text,
            preferred_location=preferred_location,
            preferred_employment=preferred_employment,
            experience_level=experience_level,
            top_k=top_k,
        )

    def merge_results(
        self,
        local_results: List[Dict[str, Any]],
        adzuna_results: Optional[List[Dict[str, Any]]] = None,
        skills: Optional[List[str]] = None,
        predicted_role: Optional[str] = None,
        predicted_salary: Optional[Any] = None,
        resume_text: Optional[str] = None,
        preferred_location: Optional[str] = None,
        preferred_employment: Optional[str] = None,
        experience_level: Optional[str] = None,
    ) -> List[Dict[str, Any]]:

        merged = []
        seen = set()

        # Local Recommendations
        for job in local_results:
            title = str(job.get("title", "")).strip().lower()
            company = str(job.get("company", "")).strip().lower()
            key = (title, company)

            if key in seen:
                continue
            seen.add(key)
            job["source"] = "Local Dataset"
            merged.append(job)

        # Adzuna Recommendations with Dynamic 10-Factor Scoring
        if adzuna_results:
            for job in adzuna_results:
                title = str(job.get("title", "")).strip().lower()
                company = str(job.get("company", "")).strip().lower()
                key = (title, company)

                if key in seen:
                    continue
                seen.add(key)

                # Compute dynamic similarity score for Adzuna job
                job_desc = str(job.get("description", "")) + " " + str(job.get("title", ""))
                sim_score = 0.75
                if self.model and job_desc.strip():
                    try:
                        q_emb = self.ranker.encode_query(predicted_role or title)
                        j_emb = self.model.encode([job_desc], convert_to_numpy=True, normalize_embeddings=True).astype("float32")
                        sim_score = float(np.dot(q_emb[0], j_emb[0]))
                    except Exception:
                        sim_score = 0.75

                meta = self.ranker.calculate_score(
                    similarity_score=sim_score,
                    job=job,
                    skills=skills,
                    predicted_role=predicted_role,
                    predicted_salary=predicted_salary,
                    resume_text=resume_text,
                    preferred_location=preferred_location,
                    preferred_employment=preferred_employment,
                    experience_level=experience_level,
                )

                job.update(meta)
                job["source"] = "Adzuna"
                merged.append(job)

        merged = sorted(
            merged,
            key=lambda x: x.get("match_score", x.get("careerpilot_score", 0)),
            reverse=True,
        )

        return merged

    def recommend(
        self,
        query: str,
        skills: Optional[List[str]] = None,
        predicted_role: Optional[str] = None,
        predicted_salary: Optional[Any] = None,
        resume_text: Optional[str] = None,
        preferred_location: Optional[str] = None,
        preferred_employment: Optional[str] = None,
        experience_level: Optional[str] = None,
        adzuna_results: Optional[List[Dict[str, Any]]] = None,
        top_k: int = 20,
    ) -> List[Dict[str, Any]]:

        local_results = self.recommend_local(
            query=query,
            skills=skills,
            predicted_role=predicted_role,
            predicted_salary=predicted_salary,
            resume_text=resume_text,
            preferred_location=preferred_location,
            preferred_employment=preferred_employment,
            experience_level=experience_level,
            top_k=top_k,
        )

        final_results = self.merge_results(
            local_results=local_results,
            adzuna_results=adzuna_results,
            skills=skills,
            predicted_role=predicted_role,
            predicted_salary=predicted_salary,
            resume_text=resume_text,
            preferred_location=preferred_location,
            preferred_employment=preferred_employment,
            experience_level=experience_level,
        )

        return final_results[:top_k]