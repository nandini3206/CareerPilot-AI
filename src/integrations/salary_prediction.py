"""
=========================================================
CareerPilot AI
Salary Prediction Integration Layer
=========================================================
"""

import sys
import importlib
from pathlib import Path

# -------------------------------------------------------
# Activate Salary Backend
# -------------------------------------------------------

SALARY_DIR = Path(__file__).resolve().parents[2] / "salary_prediction"

# Remove conflicting cached modules
for module in [
    "config",
    "predictor",
    "model_loader",
    "inference",
]:
    if module in sys.modules:
        del sys.modules[module]

# Remove old backend path if present
sys.path = [
    p for p in sys.path
    if not p.endswith("role_prediction")
]

# Add salary backend
sys.path.insert(0, str(SALARY_DIR))

# Import salary backend
salary_inference = importlib.import_module("inference")


def predict_resume_salary(
    experience_level,
    employment_type,
    job_title,
    employee_residence,
    remote_ratio,
    company_location,
    company_size,
):

    salary = salary_inference.predict_salary(
        experience_level=experience_level,
        employment_type=employment_type,
        job_title=job_title,
        employee_residence=employee_residence,
        remote_ratio=remote_ratio,
        company_location=company_location,
        company_size=company_size,
    )

    return {
        "salary": salary
    }