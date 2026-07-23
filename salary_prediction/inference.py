"""
=========================================================
CareerPilot AI V2
Salary Prediction Inference
=========================================================
Author : Nandini Bhatt
=========================================================
"""

from predictor import SalaryPredictor


# Load once
predictor = SalaryPredictor()


def predict_salary(
    experience_level: str,
    employment_type: str,
    job_title: str,
    employee_residence: str,
    remote_ratio: int,
    company_location: str,
    company_size: str,
) -> float:
    """
    Predict salary using the trained Salary Prediction model.
    """

    return predictor.predict(
        experience_level=experience_level,
        employment_type=employment_type,
        job_title=job_title,
        employee_residence=employee_residence,
        remote_ratio=remote_ratio,
        company_location=company_location,
        company_size=company_size,
    )


if __name__ == "__main__":

    salary = predict_salary(
        experience_level="SE",
        employment_type="FT",
        job_title="Machine Learning Engineer",
        employee_residence="US",
        remote_ratio=100,
        company_location="US",
        company_size="M",
    )

    print("\n" + "=" * 60)
    print("CareerPilot AI - Salary Inference")
    print("=" * 60)
    print(f"Predicted Salary (USD): ${salary:,.2f}")
    print("=" * 60)