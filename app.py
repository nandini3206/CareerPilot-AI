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

elif page == "Resume Analysis":
    show_resume_analysis()

elif page == "ATS Score":
    show_ats_score()

elif page == "Resume Feedback":
    st.title("🤖 Resume Feedback")
    st.info("Coming Soon...")

elif page == "Role Prediction":
    st.title("💼 Role Prediction")
    st.info("Coming Soon...")

elif page == "Salary Prediction":
    st.title("💰 Salary Prediction")
    st.info("Coming Soon...")

elif page == "Career Recommendation":
    st.title("🧭 Career Recommendation")
    st.info("Coming Soon...")

elif page == "Learning Roadmap":
    st.title("📚 Learning Roadmap")
    st.info("Coming Soon...")

elif page == "Cover Letter":
    st.title("📄 Cover Letter Generator")
    st.info("Coming Soon...")

elif page == "Interview Questions":
    st.title("❓ Interview Question Generator")
    st.info("Coming Soon...")

elif page == "Voice Interview":
    st.title("🎤 AI Voice Interview")
    st.info("Coming Soon...")

elif page == "Analytics":
    st.title("📊 Analytics")
    st.info("Coming Soon...")

elif page == "Resume History":
    st.title("🕘 Resume History")
    st.info("Coming Soon...")

elif page == "About":
    st.title("ℹ️ About CareerPilot AI")

    st.markdown(
        """
### 🚀 CareerPilot AI

CareerPilot AI is an AI-powered career development platform that helps students and professionals:

- 📄 Analyze resumes
- 🎯 Improve ATS scores
- 🤖 Receive AI resume feedback
- 💼 Predict suitable job roles
- 💰 Estimate salary
- 🧭 Get personalized career recommendations
- 🎤 Practice AI mock interviews
- 📊 View analytics and career insights

---

**Developed by Nandini Bhatt**
"""
    )

else:
    st.error("Page not found.")