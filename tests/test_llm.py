from src.parsers.resume_parser import extract_text

from src.llms.resume_feedback import (
    generate_resume_feedback
)

resume = extract_text("temp_resume.pdf")

feedback = generate_resume_feedback(

    resume,

    ["SQL", "Docker"],

    72

)

print(feedback)
