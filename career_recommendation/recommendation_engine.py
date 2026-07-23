"""
CareerPilot AI
Career Recommendation Engine
"""

from model_loader import CareerModelLoader
from ranker import CareerRanker


class CareerRecommendationEngine:

    def __init__(self):

        self.loader = CareerModelLoader()

        self.model = None
        self.embeddings = None
        self.metadata = None

        self.ranker = None

    # ==========================================================
    # Load Assets
    # ==========================================================

    def load(self):

        (
            self.model,
            self.embeddings,
            self.metadata,
        ) = self.loader.load_all()

        self.ranker = CareerRanker(
            model=self.model,
            metadata=self.metadata,
        )

        self.ranker.load_index()

        print("\nCareer Recommendation Engine Ready.")

    # ==========================================================
    # Local Recommendation
    # ==========================================================

    def recommend_local(
        self,
        query,
        skills=None,
        preferred_location=None,
        preferred_employment=None,
        experience_level=None,
        top_k=20,
    ):

        return self.ranker.rank_jobs(
            query=query,
            skills=skills,
            preferred_location=preferred_location,
            preferred_employment=preferred_employment,
            experience_level=experience_level,
            top_k=top_k,
        )

    # ==========================================================
    # Merge Recommendations
    # ==========================================================

    def merge_results(
        self,
        local_results,
        adzuna_results=None,
    ):

        merged = []

        seen = set()

        # -----------------------------
        # Local Recommendations
        # -----------------------------

        for job in local_results:

            title = str(job.get("title", "")).strip().lower()

            company = str(job.get("company", "")).strip().lower()

            key = (title, company)

            if key in seen:
                continue

            seen.add(key)

            job["source"] = "Local Dataset"

            merged.append(job)

        # -----------------------------
        # Adzuna Recommendations
        # -----------------------------

        if adzuna_results:

            for job in adzuna_results:

                title = str(job.get("title", "")).strip().lower()

                company = str(job.get("company", "")).strip().lower()

                key = (title, company)

                if key in seen:
                    continue

                seen.add(key)

                if "careerpilot_score" not in job:
                    job["careerpilot_score"] = 75.0

                job["source"] = "Adzuna"

                merged.append(job)

        merged = sorted(
            merged,
            key=lambda x: x["careerpilot_score"],
            reverse=True,
        )

        return merged

    # ==========================================================
    # Generate Why Match
    # ==========================================================

    def build_match_reason(
        self,
        job,
        skills=None,
    ):

        reasons = []

        if skills:

            job_skills = str(
                job.get("job_skills", "")
            ).lower()

            for skill in skills:

                if skill.lower() in job_skills:

                    reasons.append(skill)

        return reasons

    # ==========================================================
    # Recommend
    # ==========================================================

    def recommend(
        self,
        query,
        skills=None,
        preferred_location=None,
        preferred_employment=None,
        experience_level=None,
        adzuna_results=None,
        top_k=20,
    ):

        local_results = self.recommend_local(
            query=query,
            skills=skills,
            preferred_location=preferred_location,
            preferred_employment=preferred_employment,
            experience_level=experience_level,
            top_k=top_k,
        )

        final_results = self.merge_results(
            local_results,
            adzuna_results,
        )

        recommendations = []

        for job in final_results[:top_k]:

            job["why_match"] = self.build_match_reason(
                job,
                skills,
            )

            recommendations.append(job)

        return recommendations


# ==========================================================
# Main
# ==========================================================

def main():

    engine = CareerRecommendationEngine()

    engine.load()

    recommendations = engine.recommend(

        query="Machine Learning Engineer Python TensorFlow SQL Deep Learning",

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

    print("=" * 70)

    print("Career Recommendations")

    print("=" * 70)

    for i, job in enumerate(recommendations, start=1):

        print("\n")

        print("-" * 70)

        print(f"{i}. {job.get('title','')}")

        print(f"Company : {job.get('company','')}")

        print(f"Location : {job.get('location','')}")

        print(f"Score : {job.get('careerpilot_score',0):.2f}")

        print(f"Source : {job.get('source','')}")

        print(
            "Why Match :",
            ", ".join(job["why_match"])
            if job["why_match"]
            else "Semantic Match",
        )


if __name__ == "__main__":

    main()