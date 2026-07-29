"""
=========================================================
CareerPilot AI V2
Salary Prediction Explanation Engine
=========================================================
Author : Nandini Bhatt
Module : Salary Prediction
=========================================================
"""

EXPERIENCE_LEVEL_MAP = {
    "EN": "Entry-level / Junior (0-2 Yrs)",
    "MI": "Mid-level / Intermediate (2-5 Yrs)",
    "SE": "Senior-level / Specialist (5+ Yrs)",
    "EX": "Executive-level / Leadership (8+ Yrs)",
}

EMPLOYMENT_TYPE_MAP = {
    "FT": "Full-Time",
    "PT": "Part-Time",
    "CT": "Contract",
    "FL": "Freelance",
}

COMPANY_SIZE_MAP = {
    "S": "Small (1 - 50 employees)",
    "M": "Medium (50 - 250 employees)",
    "L": "Large (250+ employees)",
}


def explain_salary_factors(
    experience_level: str,
    employment_type: str,
    job_title: str,
    employee_residence: str,
    remote_ratio: int,
    company_location: str,
    company_size: str,
    predicted_salary: float,
) -> dict:
    """
    Generates statistically grounded, input-bound explanations for salary predictions.
    References only verified feature inputs without hallucinating metrics.
    """
    exp_desc = EXPERIENCE_LEVEL_MAP.get(experience_level, experience_level)
    emp_desc = EMPLOYMENT_TYPE_MAP.get(employment_type, employment_type)
    size_desc = COMPANY_SIZE_MAP.get(company_size, company_size)

    work_setup = (
        "100% Fully Remote"
        if remote_ratio == 100
        else ("50% Hybrid Work" if remote_ratio == 50 else "Onsite / In-Office")
    )

    location_match = (
        f"Domestic ({company_location})"
        if employee_residence == company_location
        else f"Cross-Border (Residence: {employee_residence}, Employer: {company_location})"
    )

    factors = []
    
    if experience_level in ["SE", "EX"]:
        factors.append(f"High experience tier ({exp_desc}) strongly elevates base compensation.")
    else:
        factors.append(f"Experience tier ({exp_desc}) sets foundational market compensation.")

    if company_location in ["US", "CA", "GB", "DE"]:
        factors.append(f"Employer location ({company_location}) aligns with high-tier technology markets.")
    else:
        factors.append(f"Employer location ({company_location}) reflects regional cost-of-living adjustments.")

    if remote_ratio == 100:
        factors.append("100% remote flexibility retains global talent market benchmark standard.")

    if company_size == "L":
        factors.append("Large corporate scale (250+ employees) supports competitive compensation bandwidth.")

    summary = (
        f"Predicted annual salary of ${predicted_salary:,.2f} USD is driven by your "
        f"{exp_desc} profile as a {job_title} working {work_setup} for a {size_desc} company in {company_location}."
    )

    return {
        "job_title": job_title,
        "experience_tier": exp_desc,
        "employment_type": emp_desc,
        "company_scale": size_desc,
        "work_setup": work_setup,
        "location_context": location_match,
        "primary_factors": factors,
        "summary": summary,
    }


if __name__ == "__main__":
    result = explain_salary_factors(
        experience_level="SE",
        employment_type="FT",
        job_title="Machine Learning Engineer",
        employee_residence="US",
        remote_ratio=100,
        company_location="US",
        company_size="M",
        predicted_salary=150000.0,
    )
    print(result)
