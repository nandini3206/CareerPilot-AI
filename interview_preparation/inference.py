"""
Interview Preparation Inference
"""

from .question_generator import InterviewQuestionGenerator


class InterviewPreparationInference:
    """
    Generates interview questions for the target career role.
    """

    def __init__(self):
        self.generator = InterviewQuestionGenerator()

    def predict(
        self,
        predicted_role: str = "Machine Learning Engineer",
        resume_text: str = "",
        extracted_skills: list = None,
        projects: list = None,
        target_role: str = None,
    ) -> dict:
        """
        Generate interview preparation content.
        Preserves 100% backward compatibility with single positional role argument predict(role).
        """
        active_role = target_role or predicted_role or "Machine Learning Engineer"

        return self.generator.generate_questions(
            role=active_role,
            resume_text=resume_text,
            extracted_skills=extracted_skills,
            projects=projects,
            predicted_role=predicted_role,
        )


def main():
    role = "Machine Learning Engineer"

    inference = InterviewPreparationInference()

    result = inference.predict(role)

    print("\n========== INTERVIEW PREPARATION ==========\n")

    for category, questions in result.items():
        print(f"{category} Questions")
        print("-" * 30)

        for i, question in enumerate(questions, start=1):
            print(f"{i}. {question}")

        print()


if __name__ == "__main__":
    main()