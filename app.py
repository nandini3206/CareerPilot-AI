import streamlit as st

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================
# IMPORTS
# ==========================

from components.styles import load_css
from components.sidebar import sidebar

from views.dashboard import show_dashboard
from views.resume_analysis import show_resume_analysis
from views.ats_score import show_ats_score
from views.resume_feedback import show_resume_feedback
from views.role_prediction import show_role_prediction
from views.salary_prediction import show_salary_prediction
from views.learning_roadmap import show_learning_roadmap
from views.resume_rewriter import show_resume_rewriter

# Later import these
# from views.resume_rewriter import show_resume_rewriter
# from views.job_recommendation import show_job_recommendation
# from views.cover_letter import show_cover_letter
# from views.interview_questions import show_interview_questions
# from views.voice_interview import show_voice_interview
# from views.analytics import show_analytics

# ==========================
# LOAD GLOBAL CSS
# ==========================

load_css()

# ==========================
# SIDEBAR
# ==========================

sidebar()

# ==========================
# DEFAULT PAGE
# ==========================

if "page" not in st.session_state:
    st.session_state.page = "Home"

page = st.session_state.page

# ==========================
# ROUTER
# ==========================

if page == "Home":
    show_dashboard()

# =====================================
# Resume Intelligence
# =====================================

elif page == "Resume Analysis":
    show_resume_analysis()

elif page == "ATS Score":
    show_ats_score()

elif page == "Resume Feedback":
    show_resume_feedback()

elif page == "Resume Rewriter":
    show_resume_rewriter()

# =====================================
# Career Insights
# =====================================

elif page == "Role Prediction":
    show_role_prediction()

elif page == "Salary Prediction":
    show_salary_prediction()

elif page == "Job Recommendations":
    st.title("💼 Job Recommendations")
    st.info("Coming Soon...")

# =====================================
# Career Preparation
# =====================================

elif page == "Learning Roadmap":
    show_learning_roadmap()

elif page == "Cover Letter":
    st.title("📝 Cover Letter Generator")
    st.info("Coming Soon...")

elif page == "Interview Questions":
    st.title("❓ Interview Questions")
    st.info("Coming Soon...")

elif page == "Voice Interview":
    st.title("🎤 AI Voice Interview")
    st.info("Coming Soon...")

# =====================================
# Dashboard
# =====================================

elif page == "Analytics":
    st.title("📊 Career Analytics")
    st.info("Coming Soon...")

# =====================================
# About
# =====================================

elif page == "About":

    st.title("ℹ️ About CareerPilot AI")

    st.markdown("""
# 🚀 CareerPilot AI

CareerPilot AI is an AI-powered career development platform designed to help students and professionals throughout their career journey.

### Resume Intelligence
- 📄 Resume Analysis
- 🎯 ATS Score
- 💬 Resume Feedback
- ✍️ Resume Rewriter

### Career Insights
- 🎯 Role Prediction
- 💰 Salary Prediction
- 💼 Job Recommendations

### Career Preparation
- 📚 Learning Roadmap
- 📝 Cover Letter Generator
- ❓ Interview Questions
- 🎤 Voice Interview

### Dashboard
- 📊 Career Analytics

---

**Developed by Nandini Bhatt**
""")

else:
    st.error("Page not found.")