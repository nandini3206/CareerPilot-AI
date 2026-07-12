from src.ml.skill_extractor import extract_skills


def compare_skills(resume_text, job_text):

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_text)

    matching = []

    missing = []

    for skill in job_skills:

        if skill in resume_skills:
            matching.append(skill)

        else:
            missing.append(skill)

    return {
        "matching": matching,
        "missing": missing
    }