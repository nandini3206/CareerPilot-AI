import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_interview_questions(
    resume_text,
    job_description
):
    """
    Generate interview questions
    based on resume and job description.
    """

    prompt = f"""
You are an experienced technical interviewer.

Interview the candidate for the following job.

Job Description:

{job_description}

Candidate Resume:

{resume_text}

Generate exactly 8 interview questions.

Structure the interview as follows:

1. Two Technical Questions
2. Two Project-Based Questions
3. Two Scenario-Based Questions
4. Two HR / Behavioral Questions

Rules:

- Questions should become progressively more difficult.
- Focus on the candidate's resume.
- Include important missing skills from the job description.
- Do NOT provide answers.
- Return only a numbered list.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5,
        max_tokens=600
    )

    return response.choices[0].message.content