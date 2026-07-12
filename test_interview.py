from src.parsers.resume_parser import extract_text

from src.llms.interview_questions import (
    generate_interview_questions
)

resume = extract_text("temp_resume.pdf")

job_description = """
Looking for a Machine Learning Intern.

Required Skills:
Python
SQL
Machine Learning
Docker
Git
Streamlit
"""

questions = generate_interview_questions(
    resume,
    job_description
)

print(questions)