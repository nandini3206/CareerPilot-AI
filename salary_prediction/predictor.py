"""
=========================================================
CareerPilot AI V2
Salary Prediction Predictor
=========================================================
Author : Nandini Bhatt
=========================================================
"""

import numpy as np
import pandas as pd

try:
    from .model_loader import load_model
    from .explain import explain_salary_factors
except ImportError:
    try:
        from salary_prediction.model_loader import load_model
        from salary_prediction.explain import explain_salary_factors
    except ImportError:
        from model_loader import load_model
        from explain import explain_salary_factors


class SalaryPredictor:
    """
    Predict salary using the trained Salary Prediction pipeline.
    Provides statistically grounded point estimates, prediction intervals,
    confidence levels derived from Random Forest ensemble variance, and input explanations.
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
        """
        Backwards-compatible float prediction.
        """
        detailed = self.predict_detailed(
            experience_level=experience_level,
            employment_type=employment_type,
            job_title=job_title,
            employee_residence=employee_residence,
            remote_ratio=remote_ratio,
            company_location=company_location,
            company_size=company_size,
        )
        return detailed["predicted_salary"]

    def predict_detailed(
        self,
        experience_level: str,
        employment_type: str,
        job_title: str,
        employee_residence: str,
        remote_ratio: int,
        company_location: str,
        company_size: str,
    ) -> dict:
        """
        Generates full statistically-grounded predictions, including:
        - Point estimate (Mean ensemble prediction)
        - Salary range (25th to 75th percentile of tree estimators)
        - Confidence score & level (Derived from Random Forest tree variance)
        - Explanation breakdown (Bound strictly to input parameters)
        """
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

        preprocessor = self.pipeline.named_steps["preprocessor"]
        model = self.pipeline.named_steps["model"]

        # Transform features & collect predictions across all decision tree estimators
        transformed_sample = preprocessor.transform(sample)
        tree_predictions = np.array([tree.predict(transformed_sample)[0] for tree in model.estimators_])

        mean_pred = float(np.mean(tree_predictions))
        std_pred = float(np.std(tree_predictions))

        # Statistically derived range (25th and 75th percentiles across decision trees)
        p25 = float(np.percentile(tree_predictions, 25))
        p75 = float(np.percentile(tree_predictions, 75))
        min_salary = round(max(10000.0, p25), 2)
        max_salary = round(max(min_salary, p75), 2)

        # Confidence percentage derived from Coefficient of Variation (CV = std / mean)
        cv = std_pred / max(1.0, mean_pred)
        confidence_pct = round(max(10.0, min(98.0, (1.0 - cv) * 100)), 1)

        if cv < 0.18:
            confidence_level = "High"
        elif cv < 0.35:
            confidence_level = "Moderate"
        else:
            confidence_level = "Low"

        # Generate factor explanations bound to real inputs
        explanation = explain_salary_factors(
            experience_level=experience_level,
            employment_type=employment_type,
            job_title=job_title,
            employee_residence=employee_residence,
            remote_ratio=remote_ratio,
            company_location=company_location,
            company_size=company_size,
            predicted_salary=round(mean_pred, 2),
        )

        return {
            "predicted_salary": round(mean_pred, 2),
            "salary_range": {
                "min": min_salary,
                "max": max_salary,
                "currency": "USD",
            },
            "confidence": {
                "percentage": confidence_pct,
                "level": confidence_level,
                "variance_usd": round(std_pred, 2),
            },
            "explanation": explanation,
        }


def main():
    predictor = SalaryPredictor()

    result = predictor.predict_detailed(
        experience_level="SE",
        employment_type="FT",
        job_title="Machine Learning Engineer",
        employee_residence="US",
        remote_ratio=100,
        company_location="US",
        company_size="M",
    )

    print("\n" + "=" * 60)
    print("CareerPilot AI - Salary Prediction Output")
    print("=" * 60)
    print(f"Predicted Salary : ${result['predicted_salary']:,.2f} USD")
    print(f"Salary Range     : ${result['salary_range']['min']:,.2f} - ${result['salary_range']['max']:,.2f} USD")
    print(f"Confidence       : {result['confidence']['percentage']}% ({result['confidence']['level']})")
    print(f"Summary          : {result['explanation']['summary']}")
    print("=" * 60)


if __name__ == "__main__":
    main()