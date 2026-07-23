"""
CareerPilot AI
Career Recommendation Inference
"""

from recommendation_engine import CareerRecommendationEngine
from adzuna_client import AdzunaClient


class CareerRecommendationInference:

    def __init__(self):

        self.engine = CareerRecommendationEngine()
        self.engine.load()

        self.adzuna = AdzunaClient()

    # ==========================================================
    # Generate Recommendations
    # ==========================================================

    def recommend(
        self,
        predicted_role,
        skills,
        preferred_location="India",
        experience_level="Entry",
        employment_type="full_time",
        top_k=10,
    ):

        # --------------------------------------------
        # Build Search Query
        # --------------------------------------------

        query = predicted_role

        if skills:

            query += " " + " ".join(skills)

        # --------------------------------------------
        # Live Jobs
        # --------------------------------------------

        try:

            live_jobs = self.adzuna.search_jobs(
                query=query,
                location=preferred_location,
                results_per_page=top_k,
            )

        except Exception as e:

            print("Adzuna Error:", e)

            live_jobs = []

        # --------------------------------------------
        # AI Recommendations
        # --------------------------------------------

        recommendations = self.engine.recommend(

            query=query,

            skills=skills,

            preferred_location=preferred_location,

            preferred_employment=employment_type,

            experience_level=experience_level,

            adzuna_results=live_jobs,

            top_k=top_k,

        )

        return recommendations


# ==========================================================
# Main
# ==========================================================

def main():

    inference = CareerRecommendationInference()

    jobs = inference.recommend(

        predicted_role="Machine Learning Engineer",

        skills=[
            "Python",
            "TensorFlow",
            "SQL",
            "Deep Learning",
        ],

        preferred_location="India",

        experience_level="Entry",

        top_k=5,

    )

    print("\n")

    print("=" * 80)
    print("CareerPilot AI Recommendations")
    print("=" * 80)

    for i, job in enumerate(jobs, start=1):

        print("\n")

        print("-" * 80)

        print(f"{i}. {job.get('title','')}")

        print(f"Company : {job.get('company','')}")

        print(f"Location : {job.get('location','')}")

        print(f"CareerPilot Score : {job.get('careerpilot_score',0):.2f}")

        print(f"Source : {job.get('source','')}")

        if job.get("why_match"):

            print("Matched Skills :", ", ".join(job["why_match"]))

        if job.get("salary_min"):

            print(f"Salary Min : {job.get('salary_min')}")

        if job.get("salary_max"):

            print(f"Salary Max : {job.get('salary_max')}")

        if job.get("redirect_url"):

            print(f"Apply : {job.get('redirect_url')}")


if __name__ == "__main__":

    main()