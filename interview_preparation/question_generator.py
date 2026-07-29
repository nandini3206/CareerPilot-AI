"""
Interview Question Generator
"""

from .knowledge_base import QUESTIONS
from .config import DEFAULT_QUESTIONS_PER_CATEGORY


class InterviewQuestionGenerator:
    """
    Generates interview questions based on the job role.
    Attempts LLM personalized generation first, and falls back to deterministic knowledge_base on any failure.
    """

    def __init__(self):
        self.questions = QUESTIONS

    def get_role_questions(self, role):
        """
        Fetch questions for a role from the deterministic knowledge base.
        """
        return self.questions.get(role)

    def _fallback_generate(self, role):
        """
        Deterministic fallback using knowledge_base.py.
        """
        role_data = self.get_role_questions(role)

        if role_data is None:
            # Fallback to Machine Learning Engineer if specified role is unknown in static KB
            role_data = self.get_role_questions("Machine Learning Engineer") or {
                "Technical": [],
                "HR": [],
                "Coding": [],
            }

        return {
            "Technical": role_data.get("Technical", [])[:DEFAULT_QUESTIONS_PER_CATEGORY],
            "HR": role_data.get("HR", [])[:DEFAULT_QUESTIONS_PER_CATEGORY],
            "Coding": role_data.get("Coding", [])[:DEFAULT_QUESTIONS_PER_CATEGORY],
        }

    def generate_questions(
        self,
        role: str,
        resume_text: str = "",
        extracted_skills: list = None,
        projects: list = None,
        predicted_role: str = "",
    ) -> dict:
        """
        Generate interview questions.
        Attempts LLM personalization via src/llms/interview_questions.py.
        On any error or missing key, falls back to deterministic knowledge base.
        """
        target_role = role or predicted_role or "Machine Learning Engineer"

        try:
            from src.llms.interview_questions import generate_personalized_questions

            llm_result = generate_personalized_questions(
                target_role=target_role,
                predicted_role=predicted_role,
                resume_text=resume_text,
                extracted_skills=extracted_skills,
                projects=projects,
            )

            # Ensure all 3 required keys exist and have non-empty data
            if (
                llm_result
                and isinstance(llm_result, dict)
                and len(llm_result.get("Technical", [])) > 0
                and len(llm_result.get("HR", [])) > 0
                and len(llm_result.get("Coding", [])) > 0
            ):
                return llm_result
        except Exception:
            # Silent fallback to deterministic knowledge base on any LLM or parsing error
            pass

        return self._fallback_generate(target_role)


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