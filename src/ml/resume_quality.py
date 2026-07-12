import re


def calculate_resume_quality(sections, resume_text):
    """
    Calculate Resume Quality Score.
    """

    score = 0

    # -----------------------------
    # Contact Information
    # -----------------------------

    email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume_text)

    phone = re.search(r"\b\d{10}\b", resume_text)

    if email and phone:
        score += 15

    # -----------------------------
    # Summary
    # -----------------------------

    if sections["summary"].strip():
        score += 15

    # -----------------------------
    # Education
    # -----------------------------

    if sections["education"].strip():
        score += 15

    # -----------------------------
    # Skills
    # -----------------------------

    if sections["skills"].strip():
        score += 20

    # -----------------------------
    # Projects
    # -----------------------------

    if sections["projects"].strip():
        score += 20

    # -----------------------------
    # Experience
    # -----------------------------

    if sections["experience"].strip():
        score += 10

    # -----------------------------
    # Resume Length
    # -----------------------------

    word_count = len(resume_text.split())

    if 200 <= word_count <= 800:
        score += 5

    return score