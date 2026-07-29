"""
=========================================================
CareerPilot AI V2
Salary Prediction Inference
=========================================================
Author : Nandini Bhatt
=========================================================
"""

try:
    from .predictor import SalaryPredictor
except ImportError:
    try:
        from salary_prediction.predictor import SalaryPredictor
    except ImportError:
        from predictor import SalaryPredictor

# Single instance loader
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
    Predict float salary using the trained model.
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


def predict_salary_detailed(
    experience_level: str,
    employment_type: str,
    job_title: str,
    employee_residence: str,
    remote_ratio: int,
    company_location: str,
    company_size: str,
) -> dict:
    """
    Predict detailed dictionary output containing predicted salary, salary range,
    confidence score, and input-bound factor explanations.
    """
    return predictor.predict_detailed(
        experience_level=experience_level,
        employment_type=employment_type,
        job_title=job_title,
        employee_residence=employee_residence,
        remote_ratio=remote_ratio,
        company_location=company_location,
        company_size=company_size,
    )


if __name__ == "__main__":
    result = predict_salary_detailed(
        experience_level="SE",
        employment_type="FT",
        job_title="Machine Learning Engineer",
        employee_residence="US",
        remote_ratio=100,
        company_location="US",
        company_size="M",
    )

    print("\n" + "=" * 60)
    print("CareerPilot AI - Salary Inference Verification")
    print("=" * 60)
    print(f"Predicted Salary : ${result['predicted_salary']:,.2f} USD")
    print(f"Salary Range     : ${result['salary_range']['min']:,.2f} - ${result['salary_range']['max']:,.2f} USD")
    print(f"Confidence       : {result['confidence']['percentage']}% ({result['confidence']['level']})")
    print(f"Summary          : {result['explanation']['summary']}")
    print("=" * 60)