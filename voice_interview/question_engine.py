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
        total_questions=5
    ):
        """
        Generate interview questions and prepare interview.
        """

        generated = self.generator.generate_questions(role)

        selected_questions = []

        # --------------------------
        # Technical
        # --------------------------

        technical = generated.get("Technical", [])

        random.shuffle(technical)

        selected_questions.extend(technical[:2])

        # --------------------------
        # HR
        # --------------------------

        hr = generated.get("HR", [])

        random.shuffle(hr)

        selected_questions.extend(hr[:2])

        # --------------------------
        # Coding
        # --------------------------

        coding = generated.get("Coding", [])

        random.shuffle(coding)

        selected_questions.extend(coding[:1])

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