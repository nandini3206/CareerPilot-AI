"""
=========================================================
CareerPilot AI V2
Salary Prediction Model Loader
=========================================================
Author : Nandini Bhatt
=========================================================
"""

import joblib

from config import MODEL_PATH


class SalaryModelLoader:
    """
    Load the trained Salary Prediction pipeline.
    """

    def __init__(self):
        self.pipeline = None

    def load(self):

        if self.pipeline is None:

            print("=" * 60)
            print("Loading Salary Prediction Model...")
            print("=" * 60)

            self.pipeline = joblib.load(MODEL_PATH)

            print("Model Loaded Successfully!")

        return self.pipeline


loader = SalaryModelLoader()


def load_model():

    return loader.load()


if __name__ == "__main__":

    model = load_model()

    print()
    print(type(model))