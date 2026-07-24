"""
Prompt Templates
"""

RESUME_REWRITE_PROMPT = """
You are an expert ATS Resume Writer.

Rewrite the following resume professionally.

Requirements:

- Improve grammar
- Improve ATS score
- Use strong action verbs
- Keep facts unchanged
- Keep formatting clean
- Make projects impactful
- Make experience professional
- Keep output concise

Resume:

{resume_text}

Return only the rewritten resume.
"""