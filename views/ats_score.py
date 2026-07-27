import streamlit as st
from src.ml.ats_scorer import calculate_ats_score
from src.ml.resume_quality import calculate_resume_quality
from src.ml.skill_matcher import compare_skills
from src.ml.careerpilot_score import calculate_careerpilot_score
from src.utils.session_manager import initialize_session
def show_ats_score():
    # ==========================================================
    # Initialize Session
    # ==========================================================
    initialize_session()

    # ==========================================================
    # Custom CSS Fixes
    # ==========================================================
    st.markdown(
        """
        <style>
        /* ---- Fix: Metric labels/values too light on dark background ---- */
        [data-testid="stMetric"] {
            background-color: #1c212b !important;
            border-radius: 10px !important;
            padding: 0.75rem 1rem !important;
            border: 1px solid #30363d !important;
        }
        [data-testid="stMetricLabel"] p {
            color: #b7bfca !important;
            font-weight: 500 !important;
        }
        [data-testid="stMetricValue"] {
            color: #f5f6fa !important;
            font-weight: 700 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🎯 ATS Dashboard")
    st.markdown(
        """
Analyze how well your resume matches the uploaded Job Description.
This dashboard calculates:
- 🚀 CareerPilot Score
- 🎯 ATS Score
- 📄 Resume Quality
- 🛠 Skill Coverage
- 💡 ATS Suggestions
"""
    )
    st.divider()
    # ==========================================================
    # Validate Resume & JD
    # ==========================================================
    if not st.session_state.resume_uploaded:
        st.warning(
            "⚠️ Please upload your resume first from the Resume Analysis page."
        )
        return
    if not st.session_state.job_uploaded:
        st.info(
            """
📄 No Job Description detected.
Please upload a Job Description in the Resume Analysis page
to access the ATS Dashboard.
"""
        )
        return
    # ==========================================================
    # Load Data
    # ==========================================================
    resume_text = st.session_state.resume_text
    sections = st.session_state.resume_sections
    job_description = st.session_state.job_description
    # ==========================================================
    # Calculate Scores
    # ==========================================================
    with st.spinner("Analyzing Resume..."):
        resume_quality = calculate_resume_quality(
            sections,
            resume_text
        )
        ats_score = calculate_ats_score(
            resume_text,
            job_description
        )
        match = compare_skills(
            resume_text,
            job_description
        )
        matching_skills = match["matching"]
        missing_skills = match["missing"]
        total_job_skills = (
            len(matching_skills)
            + len(missing_skills)
        )
        if total_job_skills == 0:
            skill_coverage = 0
        else:
            skill_coverage = round(
                (len(matching_skills) / total_job_skills) * 100,
                1
            )
        careerpilot_score = calculate_careerpilot_score(
            ats_score=ats_score,
            matching_skills=matching_skills,
            total_job_skills=total_job_skills,
            resume_quality=resume_quality
        )

        # ------------------------------------------------------
        # Fix: some ML helpers (e.g. calculate_careerpilot_score,
        # calculate_ats_score, calculate_resume_quality) may return
        # numpy scalar types (numpy.float32 / numpy.int64) instead
        # of native Python types. st.progress() and other Streamlit
        # widgets reject numpy scalars with:
        #   StreamlitAPIException: Progress Value has invalid type: float32
        # Casting everything to native Python float/int here prevents
        # that error anywhere these values are used below.
        # ------------------------------------------------------
        resume_quality = float(resume_quality)
        ats_score = float(ats_score)
        skill_coverage = float(skill_coverage)
        careerpilot_score = float(careerpilot_score)

    # ==========================================================
    # Hero Section
    # ==========================================================
    st.subheader("🚀 CareerPilot Score")
    st.metric(
        label="Overall CareerPilot Score",
        value=f"{careerpilot_score:.1f}/100"
        
    )
    st.progress(
        min(careerpilot_score / 100, 1.0)
    )
    
    st.divider()    # ==========================================================
    # Dashboard Metrics
    # ==========================================================
    st.subheader("📊 Dashboard Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "🎯 ATS Score",
            f"{ats_score:.1f}%"
        )
    with col2:
        st.metric(
            "📄 Resume Quality",
            f"{resume_quality}/100"
        )
    with col3:
        st.metric(
            "🛠 Skill Coverage",
            f"{skill_coverage}%"
        )
    with col4:
        st.metric(
            "✅ Matching Skills",
            len(matching_skills)
        )
    st.divider()
    # ==========================================================
    # Skills Analysis
    # ==========================================================
    left, right = st.columns(2)
    with left:
        st.subheader("✅ Matching Skills")
        if matching_skills:
            for skill in sorted(matching_skills):
                st.success(skill)
        else:
            st.warning("No matching skills found.")
    with right:
        st.subheader("❌ Missing Skills")
        if missing_skills:
            for skill in sorted(missing_skills):
                st.error(skill)
        else:
            st.success("No missing skills detected!")
    st.divider()
    # ==========================================================
    # Skill Coverage Progress
    # ==========================================================
    st.subheader("📈 Skill Coverage")
    st.progress(min(skill_coverage / 100, 1.0))
    st.write(
        f"Your resume currently covers **{skill_coverage}%** "
        "of the required skills in the Job Description."
    )
    st.divider()    # ==========================================================
    # ATS Suggestions
    # ==========================================================
    st.subheader("💡 ATS Improvement Suggestions")
    suggestions = []
    if ats_score < 70:
        suggestions.append(
            "Improve keyword matching by including more relevant skills from the Job Description."
        )
    if resume_quality < 75:
        suggestions.append(
            "Improve the overall structure of your resume by adding complete sections and better formatting."
        )
    if skill_coverage < 70:
        suggestions.append(
            "Add more technical skills that are mentioned in the Job Description."
        )
    if len(missing_skills) > 0:
        suggestions.append(
            "Consider learning and mentioning the missing skills if you possess them."
        )
    if len(suggestions) == 0:
        st.success(
            "🎉 Excellent! Your resume is highly optimized for this role."
        )
    else:
        for suggestion in suggestions:
            st.info(suggestion)
    st.divider()
    # ==========================================================
    # Performance Badge
    # ==========================================================
    st.subheader("🏅 Overall Performance")
    if careerpilot_score >= 90:
        st.success(
            "🌟 Excellent Resume! Highly competitive for this role."
        )
    elif careerpilot_score >= 80:
        st.success(
            "✅ Very Strong Resume! Only minor improvements are recommended."
        )
    elif careerpilot_score >= 70:
        st.warning(
            "👍 Good Resume! Some improvements can significantly increase your chances."
        )
    elif careerpilot_score >= 60:
        st.warning(
            "⚠️ Average Resume. Improve your skills and ATS optimization."
        )
    else:
        st.error(
            "❌ Your resume needs significant improvement before applying."
        )
    st.divider()
    # ==========================================================
    # Analysis Summary
    # ==========================================================
    st.subheader("📝 Analysis Summary")
    st.write(
        f"""
### Overall Evaluation
- 🚀 CareerPilot Score : **{careerpilot_score:.1f}/100**
- 🎯 ATS Score : **{ats_score:.1f}%**
- 📄 Resume Quality : **{resume_quality}/100**
- 🛠 Skill Coverage : **{skill_coverage}%**
- ✅ Matching Skills : **{len(matching_skills)}**
- ❌ Missing Skills : **{len(missing_skills)}**
"""
    )
    st.divider()    # ==========================================================
    # Top Missing Skills
    # ==========================================================
    st.subheader("🎯 Priority Skills to Add")
    if missing_skills:
        top_skills = sorted(missing_skills)[:10]
        cols = st.columns(2)
        for i, skill in enumerate(top_skills):
            with cols[i % 2]:
                st.warning(f"🔹 {skill}")
    else:
        st.success("🎉 Your resume already covers all detected job skills!")
    st.divider()
    # ==========================================================
    # Recommendations
    # ==========================================================
    st.subheader("📌 Recommendations")
    recommendations = []
    if ats_score < 80:
        recommendations.append(
            "Increase keyword relevance by naturally incorporating important terms from the Job Description."
        )
    if resume_quality < 80:
        recommendations.append(
            "Improve resume formatting, section organization, and project descriptions."
        )
    if skill_coverage < 80:
        recommendations.append(
            "Highlight additional relevant technical skills and tools that you already know."
        )
    if len(matching_skills) < len(missing_skills):
        recommendations.append(
            "Focus on closing the skill gap before applying to maximize your interview chances."
        )
    if not recommendations:
        recommendations.append(
            "Your resume is well optimized. Keep tailoring it slightly for every application."
        )
    for index, recommendation in enumerate(recommendations, start=1):
        st.write(f"{index}. {recommendation}")
    st.divider()
    # ==========================================================
    # Score Breakdown
    # ==========================================================
    st.subheader("📊 CareerPilot Score Breakdown")
    st.write("The CareerPilot Score is calculated using:")
    st.markdown(
        """
- **40%** → ATS Score
- **40%** → Skill Match
- **20%** → Resume Quality
"""
    )
    st.info(
        "A higher CareerPilot Score indicates that your resume is better aligned with the selected job role."
    )
    st.divider()
    # ==========================================================
    # Footer
    # ==========================================================
    st.caption(
        "CareerPilot AI • ATS Dashboard • Powered by Resume Analysis, Skill Matching & CareerPilot Score"
    )