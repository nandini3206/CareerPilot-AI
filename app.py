import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="CareerPilot AI — Autonomous AI Career Copilot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# 2. IMPORTS & INITIALIZATION
# =========================================================
from components.styles import load_css
from components.sidebar import render_sidebar
from src.utils.session_manager import initialize_session
from views.home import show_home
from views.resume_analysis import show_resume_analysis
from views.ats_score import show_ats_score
from views.resume_feedback import show_resume_feedback
from views.resume_rewriter import show_resume_rewriter
from views.role_prediction import show_role_prediction
from views.salary_prediction import show_salary_prediction
from views.learning_roadmap import show_learning_roadmap
from views.interview_questions import show_interview_questions
from views.voice_interview import show_voice_interview
from views.career_analytics import show_career_analytics
from views.about_platform import show_about_platform

# Load V2 Design System CSS
load_css()

# Initialize Session State Variables
initialize_session()

# Render Hierarchical VS Code / Notion Style Sidebar Navigation
render_sidebar()

# Get Current Router State (Defaults to "Home")
page = st.session_state.get("current_page", "Home")

# =========================================================
# 3. PAGE ROUTER DISPATCHER
# =========================================================
if page == "Home":
    show_home()
elif page in ["Resume Analysis", "Resume Intelligence"]:
    show_resume_analysis()
elif page == "ATS Score":
    show_ats_score()
elif page == "Resume Feedback":
    show_resume_feedback()
elif page == "Resume Rewriter":
    show_resume_rewriter()
elif page in ["Role Prediction", "Career Intelligence"]:
    show_role_prediction()
elif page in ["Salary Prediction", "Salary Studio"]:
    show_salary_prediction()

elif page in ["Learning Roadmap", "Learning Studio"]:
    show_learning_roadmap()
elif page in ["Interview Questions", "Interview Preparation"]:
    show_interview_questions()
elif page in ["Voice Interview", "Interview Lab"]:
    show_voice_interview()
elif page in ["Career Analytics", "Analytics"]:
    show_career_analytics()
elif page in ["About", "About Platform"]:
    show_about_platform()
else:
    # Workspace placeholder for future modules
    st.markdown(
        f"""
        <div class="hero-container">
            <div class="hero-title">📌 {page}</div>
            <p class="hero-subtitle">This workspace module is part of the next scheduled implementation step.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("← Return to Home Page"):
        st.session_state.current_page = "Home"
        st.rerun()