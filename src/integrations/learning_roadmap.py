"""
=========================================================
CareerPilot AI
Learning Roadmap Integration
=========================================================
"""

from learning_roadmap.inference import LearningRoadmapInference


class LearningRoadmapService:
    """
    Integration layer for Learning Roadmap.
    """

    def __init__(self):
        self.inference = LearningRoadmapInference()

    def generate(
        self,
        predicted_role,
        extracted_skills
    ):
        """
        Generate personalized roadmap.
        """

        return self.inference.predict(
            predicted_role,
            extracted_skills
        )


# Singleton instance
_service = LearningRoadmapService()


def generate_learning_roadmap(
    predicted_role,
    extracted_skills
):
    """
    Public function used by Streamlit views.
    """

    return _service.generate(
        predicted_role,
        extracted_skills
    )