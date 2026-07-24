"""
Learning Roadmap Inference
"""

from .roadmap_generator import LearningRoadmapGenerator


class LearningRoadmapInference:
    """
    Inference class for generating personalized
    learning roadmaps.
    """

    def __init__(self):
        self.generator = LearningRoadmapGenerator()

    def predict(
        self,
        predicted_role,
        extracted_skills
    ):
        """
        Generate roadmap.
        """

        roadmap = self.generator.generate_roadmap(
            predicted_role,
            extracted_skills
        )

        return roadmap


def main():

    role = "Machine Learning Engineer"

    skills = [
        "Python",
        "SQL",
        "Pandas"
    ]

    inference = LearningRoadmapInference()

    result = inference.predict(
        role,
        skills
    )

    print("\n========== ROADMAP ==========\n")

    print("Target Role:")
    print(result["target_role"])

    print("\nMissing Skills:")

    for skill in result["missing_skills"]:
        print("-", skill)

    print("\nWeekly Plan:")

    for week, topics in result["weekly_plan"].items():

        print(f"\n{week}")

        for topic in topics:
            print(" •", topic)

    print("\nProjects:")

    for project in result["recommended_projects"]:
        print("-", project)


if __name__ == "__main__":
    main()