from src.parsers.resume_parser import extract_text

from src.llms.learning_roadmap import (
    generate_learning_roadmap
)

resume = extract_text("temp_resume.pdf")

roadmap = generate_learning_roadmap(

    resume,

    [
        "SQL",
        "Docker",
        "AWS",
        "FastAPI"
    ]

)

print(roadmap)