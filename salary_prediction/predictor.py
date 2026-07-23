"""
=========================================================
CareerPilot AI V2
Salary Prediction Predictor
=========================================================
Author : Nandini Bhatt
=========================================================
"""

import pandas as pd

from model_loader import load_model


class SalaryPredictor:
    """
    Predict salary using the trained Salary Prediction pipeline.
    """

    def __init__(self):
        self.pipeline = load_model()

    def predict(
        self,
        experience_level: str,
        employment_type: str,
        job_title: str,
        employee_residence: str,
        remote_ratio: int,
        company_location: str,
        company_size: str,
    ) -> float:

        sample = pd.DataFrame(
            [
                {
                    "experience_level": experience_level,
                    "employment_type": employment_type,
                    "job_title": job_title,
                    "employee_residence": employee_residence,
                    "remote_ratio": remote_ratio,
                    "company_location": company_location,
                    "company_size": company_size,
                }
            ]
        )

        prediction = self.pipeline.predict(sample)[0]

        return round(float(prediction), 2)


def main():

    predictor = SalaryPredictor()

    salary = predictor.predict(
        experience_level="SE",
        employment_type="FT",
        job_title="Machine Learning Engineer",
        employee_residence="US",
        remote_ratio=100,
        company_location="US",
        company_size="M",
    )

    print("\n" + "=" * 60)
    print("CareerPilot AI - Salary Prediction")
    print("=" * 60)
    print(f"Predicted Salary (USD): ${salary:,.2f}")
    print("=" * 60)


if __name__ == "__main__":
    main()