"""
Interview Preparation Inference
"""

from .question_generator import InterviewQuestionGenerator


class InterviewPreparationInference:
    """
    Generates interview questions
    for the predicted role.
    """

    def __init__(self):
        self.generator = InterviewQuestionGenerator()

    def predict(self, predicted_role):
        """
        Generate interview preparation content.
        """

        return self.generator.generate_questions(predicted_role)


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