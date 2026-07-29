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
    missing_skills=None,
    ats_score=None
):
    """
    Generate AI-powered Executive Resume Coaching feedback using Groq LLaMA-3.3.
    Focuses on writing quality, impact, clarity, action verbs, and storytelling rather than ATS metrics.
    """

    prompt = f"""
You are an executive resume coach and elite tech recruiter.

Analyze the following candidate resume for writing quality, bullet impact, narrative flow, and professional presentation.

Resume Content:
{resume_text}

Return your response in clean Markdown with the following exact headings:

# 📝 Executive Summary
- Provide a 2-3 sentence overview of the resume's overall writing style, narrative flow, and recruiter impact.

# 🟢 High Impact Strengths
- Highlight 2-3 strong points where bullets effectively demonstrate quantifiable results or strong technical ownership.

# 🟡 Writing & Impact Weaknesses
- Point out 2-3 weak areas where bullet points describe generic duties rather than measurable achievements.
- Mention any passive language, weak action verbs, or lack of quantitative metrics.

# 💡 Actionable Improvement Coaching
- Give 3 concrete, high-impact writing suggestions (e.g., how to rephrase bullets using Action Verb + Task + Quantified Result).
- Focus on clarity, professional tone, and recruiter storytelling.
- Do NOT mention ATS scores or algorithms.
- Keep the response professional, concise, and under 300 words.
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
        max_tokens=600
    )

    return response.choices[0].message.content