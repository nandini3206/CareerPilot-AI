def calculate_careerpilot_score(
    ats_score,
    matching_skills,
    total_job_skills,
    resume_quality
):
    """
    Calculate overall CareerPilot Score.
    """

    if total_job_skills == 0:
        skill_score = 0

    else:
        skill_score = (
            len(matching_skills)
            / total_job_skills
        ) * 100

    final_score = (
        0.4 * ats_score
        +
        0.4 * skill_score
        +
        0.2 * resume_quality
    )

    return round(final_score, 2)