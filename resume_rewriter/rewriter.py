"""
Resume Rewriter using Groq
"""

from groq import Groq

from .config import (
    GROQ_API_KEY,
    MODEL_NAME,
    MAX_TOKENS,
    TEMPERATURE
)

from .prompt_templates import RESUME_REWRITE_PROMPT


class ResumeRewriter:
    """
    AI Resume Rewriter using Groq.
    """

    def __init__(self):

        if not GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY not found in environment variables."
            )

        self.client = Groq(api_key=GROQ_API_KEY)

    def rewrite_resume(self, resume_text):
        """
        Rewrite resume using Groq.
        """

        prompt = RESUME_REWRITE_PROMPT.format(
            resume_text=resume_text
        )

        response = self.client.chat.completions.create(

            model=MODEL_NAME,

            temperature=TEMPERATURE,

            max_tokens=MAX_TOKENS,

            messages=[
                {
                    "role": "system",
                    "content": "You are an expert ATS resume writer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()


def main():

    sample_resume = """
    Name: John Doe

    Skills:
    Python
    SQL
    Machine Learning

    Projects:
    Built a stock prediction app.

    Experience:
    Worked on ML projects.
    """

    rewriter = ResumeRewriter()

    rewritten = rewriter.rewrite_resume(sample_resume)

    print("\n========== REWRITTEN RESUME ==========\n")

    print(rewritten)


if __name__ == "__main__":
    main()