"""
====================================================
CareerPilot AI V2
Role Prediction Inference Wrapper
====================================================
"""

try:
    from role_prediction.predictor import RolePredictor
except ImportError:
    from predictor import RolePredictor

# Load singleton instance
predictor = None

def get_predictor():
    global predictor
    if predictor is None:
        predictor = RolePredictor()
    return predictor

def predict_role(resume_text: str):
    """
    Predict job role from resume text.
    """
    p = get_predictor()
    return p.predict(resume_text)

def predict_top_roles(resume_text: str, k: int = 3):
    """
    Predict top-k job roles with confidence percentages.
    """
    p = get_predictor()
    return p.predict_top_k(resume_text, k=k)

if __name__ == "__main__":
    sample_resume = """
    Python Developer
    Skills: Python, Machine Learning, SQL, PyTorch, Streamlit
    Projects: Built AI applications using LangChain.
    """
    role = predict_role(sample_resume)
    top_3 = predict_top_roles(sample_resume, 3)

    print("\n" + "=" * 60)
    print("Top Predicted Role:", role)
    print("Top 3 Predictions:", top_3)
    print("=" * 60)