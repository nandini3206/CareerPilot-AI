"""
Interview Question Generator
"""

from .knowledge_base import QUESTIONS
from .config import DEFAULT_QUESTIONS_PER_CATEGORY


class InterviewQuestionGenerator:
    """
    Generates interview questions based on the
    predicted job role.
    """

    def __init__(self):
        self.questions = QUESTIONS

    def get_role_questions(self, role):
        """
        Fetch questions for a role.
        """

        return self.questions.get(role)

    def generate_questions(self, role):
        """
        Generate interview questions.
        """

        role_data = self.get_role_questions(role)

        if role_data is None:
            return {
                "Technical": [],
                "HR": [],
                "Coding": []
            }

        return {

            "Technical":
                role_data["Technical"][:DEFAULT_QUESTIONS_PER_CATEGORY],

            "HR":
                role_data["HR"][:DEFAULT_QUESTIONS_PER_CATEGORY],

            "Coding":
                role_data["Coding"][:DEFAULT_QUESTIONS_PER_CATEGORY]

        }
def main():

    generator = InterviewQuestionGenerator()

    role = "Machine Learning Engineer"

    questions = generator.generate_questions(role)

    print("\n========== INTERVIEW PREPARATION ==========\n")

    for category, items in questions.items():

        print(f"{category} Questions")

        print("-" * 30)

        for i, question in enumerate(items, start=1):
            print(f"{i}. {question}")

        print()


if __name__ == "__main__":
    main()