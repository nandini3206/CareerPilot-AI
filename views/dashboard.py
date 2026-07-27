import streamlit as st
from PIL import Image
def show_dashboard():
    # ==========================================================
    # TOP FEATURES
    # ==========================================================
    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            "<div style='text-align:center;font-size:14px;'>🎯 <span style='color:#38BDF8;font-weight:600;'>ATS Optimization</span></div>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            "<div style='text-align:center;font-size:14px;'>🧠 <span style='color:#38BDF8;font-weight:600;'>ML Role Prediction</span></div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            "<div style='text-align:center;font-size:14px;'>🎤 <span style='color:#38BDF8;font-weight:600;'>Voice Interview AI</span></div>",
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            "<div style='text-align:center;font-size:14px;'>💰 <span style='color:#38BDF8;font-weight:600;'>Salary Intelligence</span></div>",
            unsafe_allow_html=True,
        )
    st.markdown("---")
    # ==========================================================
    # HERO SECTION
    # ==========================================================
    left, right = st.columns([1.4, 1])
    with left:
        logo = Image.open("assets/logo.png")
        logo_col, title_col = st.columns([0.12, 0.88])
        with logo_col:
            st.image(logo, width=90)
        with title_col:
            st.markdown(
                """
                <div class="hero-title">
                    CareerPilot <span class="hero-highlight">AI</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown(
            """
            <div class="hero-subtitle">
            Your Personal AI Career Mentor
            <br><br>
            Analyze • Improve • Prepare • Get Hired
            <br><br>
            CareerPilot AI helps you improve your resume,
            boost your ATS score,
            predict suitable roles,
            estimate salary,
            prepare for interviews,
            and receive personalized career guidance —
            all in one intelligent platform.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("🚀 Start Analysis"):
            st.session_state.page = "Resume Analysis"
            st.rerun()
    with right:
        st.markdown(
            """
            <div style="text-align:center;font-size:170px;padding-top:25px;">
                🤖
            </div>
            <div style="text-align:center;color:#94A3B8;font-size:18px;">
                AI Career Assistant
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.write("")
    st.write("")
    # ==========================================================
    # FEATURE CARDS
    # ==========================================================    # ==========================================================
    # FEATURE CARDS
    # ==========================================================
    st.markdown(
        """
        <div class="section-title">
            Everything You Need To Get Hired
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div style="font-size:42px;">📄</div>
                <div class="card-title">
                    Resume Analysis
                </div>
                <div class="card-text">
                    Upload your resume and receive
                    AI-powered feedback, ATS analysis,
                    and personalized improvement suggestions.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div style="font-size:42px;">🎤</div>
                <div class="card-title">
                    Voice Interview
                </div>
                <div class="card-text">
                    Practice mock interviews with AI,
                    receive scores, strengths,
                    weaknesses and improvement tips.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.write("")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div style="font-size:42px;">💼</div>
                <div class="card-title">
                    Career Recommendation
                </div>
                <div class="card-text">
                    Discover the best career path
                    using your skills, resume,
                    interests and experience.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            """
            <div class="feature-card">
                <div style="font-size:42px;">📊</div>
                <div class="card-title">
                    Analytics Dashboard
                </div>
                <div class="card-text">
                    Visualize ATS score,
                    salary prediction,
                    role matching
                    and career insights.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.write("")
    st.write("")
    st.write("")
    # ==========================================================
    # WHY CAREERPILOT
    # ==========================================================    # ==========================================================
    # WHY CAREERPILOT
    # ==========================================================
    st.markdown(
        """
        <div class="section-title">
            Why CareerPilot AI?
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info(
            """
### 🤖 AI Powered
Advanced Machine Learning and NLP models analyze your resume,
predict suitable roles, estimate salaries,
and provide personalized career guidance.
"""
        )
    with c2:
        st.success(
            """
### 📈 Professional Analytics
Track ATS scores, resume quality,
skill gaps, role matching,
and career progress with insightful analytics.
"""
        )
    with c3:
        st.warning(
            """
### 🎯 Career Focused
From resume optimization to interview preparation,
CareerPilot AI helps you become
job-ready with confidence.
"""
        )
    st.write("")
    st.write("")
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align:center; color:#94A3B8; padding:20px 0;">
            <h4 style="color:#38BDF8;">
                🚀 CareerPilot AI
            </h4>
            <p>
                Your Personal AI Career Mentor
            </p>
            <p style="font-size:14px;">
                Built with ❤️ using Streamlit • Machine Learning • AI
            </p>
            <p style="font-size:13px;">
                Developed by <b>Nandini Bhatt</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )