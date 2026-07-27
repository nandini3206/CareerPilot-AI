"""
====================================================
CareerPilot AI
Role Prediction Integration Layer
====================================================
"""

import sys
from pathlib import Path

ROLE_DIR = Path(__file__).resolve().parents[2] / "role_prediction"

if str(ROLE_DIR) not in sys.path:
    sys.path.insert(0, str(ROLE_DIR))

from inference import predict_role
from explain import explain_prediction


def predict_resume_role(resume_text: str):

    role = predict_role(resume_text)

    explanation = explain_prediction(role)

    return {
        "role": role,
        "description": explanation["description"]
    }