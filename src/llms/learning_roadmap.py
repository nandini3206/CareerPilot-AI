import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_learning_roadmap(
    resume_text,
    missing_skills
):
    """
    Generate a personalized learning roadmap.
    """

    prompt = f"""
You are an experienced AI career mentor.

The candidate already knows the skills mentioned in the resume.

Resume:

{resume_text}

Missing Skills:

{", ".join(missing_skills)}

Create a personalized learning roadmap.

Instructions:

- Prioritize the missing skills from beginner to advanced.
- Explain why each skill is important.
- Mention important topics to learn.
- Suggest one practical task or mini-project for each skill.
- Do NOT recommend online courses.
- Do NOT recommend certifications.
- Keep the roadmap practical.
- Return the answer in Markdown.

Use the following format.

# Personalized Learning Roadmap

## Priority 1

Skill:

Why Learn:

Topics:

Practice Task:

## Priority 2

...

"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.4,
        max_tokens=700

    )

    return response.choices[0].message.content