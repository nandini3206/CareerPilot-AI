import os
import json
import re
from dotenv import load_dotenv

load_dotenv()


def generate_interview_questions(resume_text: str, job_description: str) -> str:
    """
    Legacy wrapper for resume + job description prompt.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "GROQ_API_KEY not configured."

    try:
        from groq import Groq
        client = Groq(api_key=api_key)

        prompt = f"""
You are an experienced technical interviewer.

Interview the candidate for the following job.

Job Description:
{job_description}

Candidate Resume:
{resume_text}

Generate exactly 8 interview questions:
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
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=600,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating interview questions: {e}"


def generate_personalized_questions(
    target_role: str,
    predicted_role: str = "",
    resume_text: str = "",
    extracted_skills: list = None,
    projects: list = None,
) -> dict:
    """
    Generates personalized interview questions via LLM.
    Returns valid JSON dictionary with keys 'Technical', 'HR', 'Coding' containing plain text question strings.
    If API key is missing or call fails, raises Exception (caller handles fallback).
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not configured in environment")

    from groq import Groq
    client = Groq(api_key=api_key)

    skills_str = ", ".join(extracted_skills) if extracted_skills else "Not specified"
    projects_str = ", ".join(projects) if projects else "Not specified"
    resume_summary = resume_text[:1500] if resume_text else "Not provided"

    prompt = f"""
You are an expert technical interviewer conducting an interview for the target role: "{target_role}".

Candidate Context:
- Target Interview Role: {target_role}
- Predicted Career Role: {predicted_role or target_role}
- Extracted Resume Skills: {skills_str}
- Portfolio Projects: {projects_str}
- Resume Snippet: {resume_summary}

Generate 15 highly relevant interview questions (5 Technical, 5 HR/Behavioral, 5 Coding) tailored to the candidate's target role and resume context.

CRITICAL INSTRUCTION:
Return ONLY a raw, valid JSON object with NO markdown formatting, NO backticks, NO markdown codeblocks (```json ... ```), NO prefix, and NO suffix.

The JSON MUST conform to this exact schema:
{{
  "Technical": [
    "Question 1 string",
    "Question 2 string",
    "Question 3 string",
    "Question 4 string",
    "Question 5 string"
  ],
  "HR": [
    "Question 1 string",
    "Question 2 string",
    "Question 3 string",
    "Question 4 string",
    "Question 5 string"
  ],
  "Coding": [
    "Question 1 string",
    "Question 2 string",
    "Question 3 string",
    "Question 4 string",
    "Question 5 string"
  ]
}}

RULES FOR QUESTION STRINGS:
- Each item MUST be a plain text question string.
- Do NOT include question numbers (e.g., write "Explain gradient descent." NOT "1. Explain gradient descent.").
- Do NOT include markdown bolding, answers, explanations, or metadata.
- Technical questions should probe candidate's resume skills, projects, and target role concepts.
- HR questions should ask behavioral questions referencing projects/experience.
- Coding questions should specify concise algorithmic/coding problem statements suitable for entry/mid level interview.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt.strip()}],
        temperature=0.5,
        max_tokens=1000,
    )

    raw_content = response.choices[0].message.content.strip()

    # Strip markdown codeblocks if model returns ```json ... ```
    if raw_content.startswith("```"):
        lines = raw_content.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        raw_content = "\n".join(lines).strip()

    data = json.loads(raw_content)

    # Validate schema
    if not isinstance(data, dict):
        raise ValueError("LLM response is not a JSON dictionary")

    required_keys = ["Technical", "HR", "Coding"]
    for key in required_keys:
        if key not in data or not isinstance(data[key], list):
            raise ValueError(f"Missing or invalid key '{key}' in LLM output JSON")

        cleaned_list = []
        for item in data[key]:
            q_str = str(item).strip()
            # Remove leading numbers like "1. Question"
            q_str = re.sub(r"^\d+[\.\)]\s*", "", q_str)
            if q_str:
                cleaned_list.append(q_str)
        data[key] = cleaned_list

    return data