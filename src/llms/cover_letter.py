from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_cover_letter(
    resume,
    job_description,
    company="the company",
    hiring_manager="Hiring Manager"
):

    prompt = f"""
You are an expert career coach.

Write a professional cover letter.

Resume:

{resume}

Job Description:

{job_description}

Company:
{company}

Hiring Manager:
{hiring_manager}

Requirements:

- Professional tone
- Around 300 words
- Mention matching skills
- Mention projects
- Show enthusiasm
- End professionally
- Do NOT use placeholders
"""

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.4

    )

    return completion.choices[0].message.content