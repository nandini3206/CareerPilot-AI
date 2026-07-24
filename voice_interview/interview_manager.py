"""
Interview Manager
"""

from datetime import datetime


class InterviewManager:

    def __init__(self):

        self.role = ""

        self.questions = []

        self.answers = []

        self.evaluations = []

        self.current_question = 0

        self.started_at = None

        self.finished_at = None

    # ---------------------------------------------------
    # Interview Setup
    # ---------------------------------------------------

    def start(self, role, questions):

        self.role = role

        self.questions = questions

        self.answers = []

        self.evaluations = []

        self.current_question = 0

        self.started_at = datetime.now()

    # ---------------------------------------------------
    # Current Question
    # ---------------------------------------------------

    def has_next_question(self):

        return self.current_question < len(self.questions)

    def get_next_question(self):

        if not self.has_next_question():
            return None

        question = self.questions[self.current_question]

        self.current_question += 1

        return question

    # ---------------------------------------------------
    # Save Answer
    # ---------------------------------------------------

    def save_answer(
        self,
        question,
        answer,
        evaluation
    ):

        self.answers.append({

            "question": question,

            "answer": answer
        })

        self.evaluations.append(evaluation)

    # ---------------------------------------------------
    # Overall Score
    # ---------------------------------------------------

    def average_score(self):

        if len(self.evaluations) == 0:
            return 0

        total = sum(

            evaluation.get(
                "overall_score",
                0
            )

            for evaluation in self.evaluations

        )

        return round(
            total / len(self.evaluations),
            2
        )

    # ---------------------------------------------------
    # Technical Score
    # ---------------------------------------------------

    def technical_score(self):

        values = [

            evaluation["scores"]["technical_accuracy"]

            for evaluation in self.evaluations

            if "scores" in evaluation

        ]

        if not values:
            return 0

        return round(sum(values) / len(values), 2)

    # ---------------------------------------------------
    # Communication
    # ---------------------------------------------------

    def communication_score(self):

        values = [

            evaluation["scores"]["communication"]

            for evaluation in self.evaluations

            if "scores" in evaluation

        ]

        if not values:
            return 0

        return round(sum(values) / len(values), 2)

    # ---------------------------------------------------
    # Confidence
    # ---------------------------------------------------

    def confidence_score(self):

        values = [

            evaluation["scores"]["confidence"]

            for evaluation in self.evaluations

            if "scores" in evaluation

        ]

        if not values:
            return 0

        return round(sum(values) / len(values), 2)

    # ---------------------------------------------------
    # Completeness
    # ---------------------------------------------------

    def completeness_score(self):

        values = [

            evaluation["scores"]["completeness"]

            for evaluation in self.evaluations

            if "scores" in evaluation

        ]

        if not values:
            return 0

        return round(sum(values) / len(values), 2)

    # ---------------------------------------------------
    # Collect Strengths
    # ---------------------------------------------------

    def strengths(self):

        strengths = []

        for evaluation in self.evaluations:

            strengths.extend(

                evaluation.get(
                    "strengths",
                    []
                )

            )

        return list(dict.fromkeys(strengths))

    # ---------------------------------------------------
    # Collect Improvements
    # ---------------------------------------------------

    def improvements(self):

        improvements = []

        for evaluation in self.evaluations:

            improvements.extend(

                evaluation.get(
                    "improvements",
                    []
                )

            )

        return list(dict.fromkeys(improvements))

    # ---------------------------------------------------
    # Finish
    # ---------------------------------------------------

    def finish(self):

        self.finished_at = datetime.now()

    # ---------------------------------------------------
    # Report
    # ---------------------------------------------------

    def generate_report(self):

        self.finish()

        report = {

            "role": self.role,

            "started_at": str(self.started_at),

            "finished_at": str(self.finished_at),

            "questions_attempted": len(self.answers),

            "overall_score": self.average_score(),

            "technical_accuracy": self.technical_score(),

            "communication": self.communication_score(),

            "confidence": self.confidence_score(),

            "completeness": self.completeness_score(),

            "strengths": self.strengths(),

            "improvements": self.improvements(),

            "answers": self.answers,

            "evaluations": self.evaluations

        }

        return report