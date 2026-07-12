import os

from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_resume_feedback(
    resume_text,
    missing_skills,
    ats_score
):
    """
    Generate AI-powered resume feedback using Groq.
    """

    prompt = f"""
You are an experienced ATS recruiter and career mentor.

Analyze the following candidate's resume.

ATS Score:
{ats_score}

Missing Skills:
{", ".join(missing_skills)}

Resume:
{resume_text}

Return the response in Markdown.

Use exactly the following sections:

# Strengths
- Mention the candidate's strongest technical skills.
- Mention positive points in the resume.
- Mention good projects or achievements.

# Weaknesses
- Mention important missing skills.
- Mention resume problems.
- Mention anything reducing the ATS score.

# Suggestions
- Give practical resume improvements.
- Suggest missing technical skills to learn.
- Suggest better project ideas if required.
- Suggest how to improve resume impact using measurable achievements.
- Do NOT recommend online courses.
- Do NOT mention certifications unless absolutely necessary.

Keep the response professional, concise, and under 250 words.
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
        max_tokens=500
    )

    return response.choices[0].message.content