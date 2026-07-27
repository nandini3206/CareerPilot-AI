"""
=========================================================
CareerPilot AI
Backend Loader
=========================================================
"""

import sys
from pathlib import Path


def activate_backend(backend_name: str):
    """
    Activate one backend package by cleaning conflicting modules
    and putting its folder at the front of sys.path.
    """

    project_root = Path(__file__).resolve().parents[2]
    backend_dir = project_root / backend_name

    # Remove conflicting cached modules
    for module in [
        "config",
        "predictor",
        "model_loader",
        "inference",
        "preprocess",
        "trainer",
        "explain",
    ]:
        sys.modules.pop(module, None)

    # Remove previous backend paths
    sys.path = [
        p for p in sys.path
        if not (
            p.endswith("role_prediction")
            or p.endswith("salary_prediction")
            or p.endswith("learning_roadmap")
            or p.endswith("interview_preparation")
        )
    ]

    # Activate required backend
    sys.path.insert(0, str(backend_dir))