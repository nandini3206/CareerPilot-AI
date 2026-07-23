"""
=========================================
CareerPilot AI
Role Prediction Model Loader
=========================================
"""

import joblib

from config import (
    BEST_MODEL,
    LABEL_ENCODER,
)


def load_model():

    model = joblib.load(BEST_MODEL)

    return model


def load_label_encoder():

    encoder = joblib.load(LABEL_ENCODER)

    return encoder


def load_all():

    model = load_model()

    encoder = load_label_encoder()

    return model, encoder
