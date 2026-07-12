from src.ml.semantic_match import calculate_similarity


def calculate_ats_score(resume_text, job_description):
    """
    Calculate ATS score using semantic similarity.
    """

    similarity = calculate_similarity(
        resume_text,
        job_description
    )

    ats_score = round(similarity * 100, 2)

    return round(ats_score, 2)