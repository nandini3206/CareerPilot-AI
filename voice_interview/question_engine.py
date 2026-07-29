"""
Voice Interview Question Engine
"""

import random

from interview_preparation.question_generator import (
    InterviewQuestionGenerator
)


class VoiceQuestionEngine:

    def __init__(self):
        self.generator = InterviewQuestionGenerator()
        self.questions = []
        self.current_index = 0

    def start_interview(
        self,
        role,
        total_questions=5,
        existing_questions_dict=None
    ):
        """
        Generate interview questions and prepare interview.
        Reuses existing generated questions from session_state['generated_interview_questions']
        if available to avoid duplicate LLM calls.
        """
        generated = existing_questions_dict

        # Attempt to pull canonical generated questions from Streamlit session state if available
        if generated is None:
            try:
                import streamlit as st
                generated = st.session_state.get("generated_interview_questions")
            except Exception:
                generated = None

        # Fall back to question generator if no pre-generated questions exist in state
        if not generated or not isinstance(generated, dict):
            generated = self.generator.generate_questions(role)

        selected_questions = []

        # --------------------------
        # Technical
        # --------------------------
        technical = generated.get("Technical", [])
        if technical:
            tech_copy = list(technical)
            random.shuffle(tech_copy)
            selected_questions.extend(tech_copy[:2])

        # --------------------------
        # HR
        # --------------------------
        hr = generated.get("HR", [])
        if hr:
            hr_copy = list(hr)
            random.shuffle(hr_copy)
            selected_questions.extend(hr_copy[:2])

        # --------------------------
        # Coding
        # --------------------------
        coding = generated.get("Coding", [])
        if coding:
            coding_copy = list(coding)
            random.shuffle(coding_copy)
            selected_questions.extend(coding_copy[:1])

        random.shuffle(selected_questions)

        self.questions = selected_questions[:total_questions]
        self.current_index = 0

    def has_next_question(self):
        return self.current_index < len(self.questions)

    def next_question(self):
        if not self.has_next_question():
            return None

        question = self.questions[self.current_index]
        self.current_index += 1
        return question

    def total_questions(self):
        return len(self.questions)

    def reset(self):
        self.questions = []
        self.current_index = 0


def main():
    engine = VoiceQuestionEngine()
    engine.start_interview(
        role="Machine Learning Engineer",
        total_questions=5
    )

    print()
    while engine.has_next_question():
        print(engine.next_question())
        print("-" * 50)


if __name__ == "__main__":
    main()