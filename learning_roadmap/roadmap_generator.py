"""
Learning Roadmap Generator
"""

from .knowledge_base import ROADMAPS
from .config import DEFAULT_WEEKS


class LearningRoadmapGenerator:
    """
    Generates personalized learning roadmaps
    based on target role and existing skills.
    """

    def __init__(self):
        self.roadmaps = ROADMAPS

    def get_role_data(self, role):
        """
        Fetch roadmap data for a role.
        """

        if role not in self.roadmaps:
            return None

        return self.roadmaps[role]

    def find_missing_skills(self, role, user_skills):
        """
        Compare required skills with user's skills.
        """

        role_data = self.get_role_data(role)

        if role_data is None:
            return []

        required_skills = role_data["skills"]

        user_skill_set = {
            skill.strip().lower()
            for skill in user_skills
        }

        missing = []

        for skill in required_skills:

            if skill.lower() not in user_skill_set:
                missing.append(skill)

        return missing

    def divide_into_weeks(self, missing_skills):
        """
        Split skills into weekly roadmap.
        """

        if not missing_skills:
            return {}

        total = len(missing_skills)

        weeks = min(DEFAULT_WEEKS, total)

        roadmap = {}

        index = 0

        for week in range(1, weeks + 1):

            remaining = total - index
            remaining_weeks = weeks - week + 1

            count = max(
                1,
                remaining // remaining_weeks
            )

            roadmap[f"Week {week}"] = \
                missing_skills[index:index + count]

            index += count

        return roadmap


    def get_projects(self, role):
        """
        Get recommended projects for the role.
        """

        role_data = self.get_role_data(role)

        if role_data is None:
            return []

        return role_data.get("projects", [])

    def generate_roadmap(self, role, user_skills):
        """
        Generate complete learning roadmap.
        """

        missing_skills = self.find_missing_skills(
            role,
            user_skills
        )

        weekly_plan = self.divide_into_weeks(
            missing_skills
        )

        projects = self.get_projects(role)

        return {
            "target_role": role,
            "missing_skills": missing_skills,
            "weekly_plan": weekly_plan,
            "recommended_projects": projects
        }

def main():

    generator = LearningRoadmapGenerator()

    user_skills = [
        "Python",
        "SQL",
        "Pandas"
    ]

    roadmap = generator.generate_roadmap(
        "Machine Learning Engineer",
        user_skills
    )

    print("\n========== LEARNING ROADMAP ==========\n")

    print(f"Target Role : {roadmap['target_role']}")

    print("\nMissing Skills:")

    for skill in roadmap["missing_skills"]:
        print(f" - {skill}")

    print("\nWeekly Plan:")

    for week, topics in roadmap["weekly_plan"].items():
        print(f"\n{week}")

        for topic in topics:
            print(f"   • {topic}")

    print("\nProjects:")

    for project in roadmap["recommended_projects"]:
        print(f" - {project}")


if __name__ == "__main__":
    main()