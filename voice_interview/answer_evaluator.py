"""
AI Answer Evaluator
"""

import json
from groq import Groq

from .config import (
    GROQ_API_KEY,
    MODEL_NAME
)


class AnswerEvaluator:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def evaluate(
        self,
        role,
        question,
        answer
    ):

        prompt = f"""
You are an expert technical interviewer.

Candidate Role:
{role}

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer professionally.

Return ONLY valid JSON.

Return EXACTLY in this format:

{{
    "overall_score": 90,

    "scores": {{
        "technical_accuracy": 90,
        "communication": 90,
        "confidence": 90,
        "completeness": 90
    }},

    "strengths": [
        "Strength 1",
        "Strength 2"
    ],

    "improvements": [
        "Improvement 1",
        "Improvement 2"
    ],

    "better_answer": "Provide a better interview answer.",

    "follow_up_question": "Relevant follow-up interview question.",

    "keywords_missing": [
        "keyword1",
        "keyword2"
    ],

    "difficulty": "Easy",

    "confidence_level": "High",

    "recommended_topics": [
        "Topic 1",
        "Topic 2",
        "Topic 3"
    ],

    "hiring_signal": "Strong Hire"
}}

Rules:

1. Return ONLY JSON.
2. No markdown.
3. No explanation.
4. Scores must be between 0 and 100.
5. Always return every field.
"""

        response = self.client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "system",
                    "content": "You are an expert technical interviewer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3
        )

        result = response.choices[0].message.content.strip()

        try:

            return json.loads(result)

        except Exception:

            return {
                "overall_score": 0,

                "scores": {
                    "technical_accuracy": 0,
                    "communication": 0,
                    "confidence": 0,
                    "completeness": 0
                },

                "strengths": [],

                "improvements": [
                    "Unable to evaluate answer."
                ],

                "better_answer": "",

                "follow_up_question": "",

                "keywords_missing": [],

                "difficulty": "",

                "confidence_level": "",

                "recommended_topics": [],

                "hiring_signal": "",

                "error": "Failed to parse AI response."
            }


def main():

    evaluator = AnswerEvaluator()

    result = evaluator.evaluate(

        role="Machine Learning Engineer",

        question="Explain overfitting in Machine Learning.",

        answer="""
Overfitting happens when a model memorizes the training data
instead of learning the underlying pattern.
It performs well on training data but poorly on unseen data.
Regularization, Dropout, Cross Validation and more data can help
reduce overfitting.
"""
    )

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()