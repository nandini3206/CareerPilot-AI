"""
CareerPilot AI
Career Recommendation Inference — High-Level Wrapper
"""

import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

# Ensure career_recommendation directory is in sys.path
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from recommendation_engine import CareerRecommendationEngine
from adzuna_client import AdzunaClient


class CareerRecommendationInference:

    def __init__(self):
        self.engine = CareerRecommendationEngine()
        self.engine.load()
        self.adzuna = AdzunaClient()

    def recommend(
        self,
        predicted_role: str,
        skills: Optional[List[str]] = None,
        predicted_salary: Optional[Any] = None,
        resume_text: Optional[str] = None,
        preferred_location: str = "India",
        experience_level: str = "Entry",
        employment_type: str = "full_time",
        top_k: int = 15,
    ) -> List[Dict[str, Any]]:

        query = predicted_role or "Software Engineer"
        if skills:
            query += " " + " ".join(skills[:8])

        # Fetch Live Jobs from Adzuna
        try:
            live_jobs = self.adzuna.search_jobs(
                query=predicted_role or query,
                location=preferred_location,
                results_per_page=top_k,
            )
        except Exception as e:
            print("Adzuna API Fetch Notice:", e)
            live_jobs = []

        # Run Engine Multi-Factor Ranking
        recommendations = self.engine.recommend(
            query=query,
            skills=skills,
            predicted_role=predicted_role,
            predicted_salary=predicted_salary,
            resume_text=resume_text,
            preferred_location=preferred_location,
            preferred_employment=employment_type,
            experience_level=experience_level,
            adzuna_results=live_jobs,
            top_k=top_k,
        )

        return recommendations


# Main for manual test verification
def main():
    inference = CareerRecommendationInference()
    jobs = inference.recommend(
        predicted_role="Machine Learning Engineer",
        skills=["Python", "TensorFlow", "SQL", "Deep Learning"],
        predicted_salary="1200000",
        preferred_location="India",
        experience_level="Entry",
        top_k=5,
    )

    print("\n" + "=" * 80)
    print("CareerPilot AI Recommendations Test Output")
    print("=" * 80)

    for i, job in enumerate(jobs, start=1):
        print(f"\n--- Job #{i} ---")
        print(f"Title          : {job.get('title')}")
        print(f"Company        : {job.get('company')}")
        print(f"Location       : {job.get('location')}")
        print(f"Match Score    : {job.get('match_score')}%")
        print(f"Skill Coverage : {job.get('skill_coverage')}%")
        print(f"Matched Skills : {job.get('matched_skills')}")
        print(f"Missing Skills : {job.get('missing_skills')}")
        print(f"Reason         : {job.get('recommendation_reason')}")
        print(f"Source         : {job.get('source')}")


if __name__ == "__main__":
    main()