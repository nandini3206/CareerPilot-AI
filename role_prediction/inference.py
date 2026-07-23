"""
====================================================
CareerPilot AI V2
Role Prediction Inference
====================================================
"""

from predictor import RolePredictor


# Load once
predictor = RolePredictor()


def predict_role(resume_text: str):

    """
    Predict job role from resume text.
    """

    return predictor.predict(resume_text)


if __name__ == "__main__":

    sample_resume = """

    Python Developer

    Skills:
    Python
    Machine Learning
    SQL
    TensorFlow
    Streamlit

    Projects:
    Built AI applications using LangChain.

    """

    role = predict_role(sample_resume)

    print()

    print("=" * 60)
    print("Predicted Role")
    print("=" * 60)
    print(role)