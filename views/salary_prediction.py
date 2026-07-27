"""
====================================================
CareerPilot AI
Salary Prediction
====================================================
"""

import streamlit as st

from src.integrations.salary_prediction import (
    predict_resume_salary
)


def show_salary_prediction():

    st.title("💰 Salary Prediction")

    st.caption(
        "Estimate your expected annual salary using AI."
    )

    st.divider()

    # --------------------------------------------------
    # Resume Check
    # --------------------------------------------------

    if not st.session_state.get("resume_uploaded", False):

        st.warning(
            "⚠ Please analyze your resume first."
        )

        return

    resume_name = st.session_state.resume_file_name
    resume_skills = st.session_state.resume_skills

    # --------------------------------------------------
    # Resume Overview
    # --------------------------------------------------

    st.subheader("📄 Resume Overview")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Resume",
            resume_name
        )

    with c2:
        st.metric(
            "Skills Found",
            len(resume_skills)
        )

    st.divider()

    # --------------------------------------------------
    # Prediction Inputs
    # --------------------------------------------------

    st.subheader("⚙ Prediction Details")

    col1, col2 = st.columns(2)

    with col1:

        experience = st.selectbox(

            "Experience Level",

            ["EN", "MI", "SE", "EX"]

        )

        employment = st.selectbox(

            "Employment Type",

            ["FT", "PT", "CT", "FL"]

        )

        remote = st.slider(

            "Remote Ratio",

            0,

            100,

            100

        )

    with col2:

        job_title = st.text_input(

            "Job Title",

            value="Machine Learning Engineer"

        )

        residence = st.text_input(

            "Employee Residence",

            value="US"

        )

        company_location = st.text_input(

            "Company Location",

            value="US"

        )

        company_size = st.selectbox(

            "Company Size",

            ["S", "M", "L"]

        )

    st.divider()

    predict = st.button(

        "💰 Predict Salary",

        use_container_width=True

    )

    if not predict:

        return

    with st.spinner("Predicting Salary..."):

        result = predict_resume_salary(

            experience,

            employment,

            job_title,

            residence,

            remote,

            company_location,

            company_size,

        )

    salary = result["salary"]
        # --------------------------------------------------
    # Prediction Result
    # --------------------------------------------------

    st.success("Salary Prediction Completed Successfully!")

    st.divider()

    st.subheader("💰 Estimated Annual Salary")

    st.metric(
        label="Predicted Salary (USD)",
        value=f"${salary:,.2f}"
    )

    st.progress(min(float(salary) / 300000, 1.0))

    st.caption(
        "The progress bar represents the estimated salary relative "
        "to a reference upper range of $300,000."
    )

    st.divider()

    # --------------------------------------------------
    # Prediction Summary
    # --------------------------------------------------

    st.subheader("📊 Prediction Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Experience", experience)

    with c2:
        st.metric("Employment", employment)

    with c3:
        st.metric("Remote", f"{remote}%")

    st.divider()

    # --------------------------------------------------
    # Career Insights
    # --------------------------------------------------

    st.subheader("💡 Salary Insights")

    if salary >= 200000:

        st.success(
            "Excellent earning potential. Continue building advanced "
            "skills and leadership experience."
        )

    elif salary >= 120000:

        st.info(
            "Strong salary range. Expanding your technical expertise "
            "and portfolio can further improve your earning potential."
        )

    elif salary >= 70000:

        st.warning(
            "Solid starting point. Gaining experience, certifications, "
            "and impactful projects can significantly increase salary."
        )

    else:

        st.error(
            "This estimate is on the lower side. Focus on strengthening "
            "your skills, projects, and practical experience."
        )

    st.divider()

    # --------------------------------------------------
    # Input Summary
    # --------------------------------------------------

    st.subheader("📝 Prediction Inputs")

    st.markdown(f"**Job Title:** {job_title}")
    st.markdown(f"**Employee Residence:** {residence}")
    st.markdown(f"**Company Location:** {company_location}")
    st.markdown(f"**Company Size:** {company_size}")

    st.divider()
        # --------------------------------------------------
    # Salary Growth Tips
    # --------------------------------------------------

    st.subheader("📈 How to Increase Your Salary")

    tips = [
        "Build industry-level AI/ML projects.",
        "Master Data Structures & Algorithms.",
        "Earn cloud certifications (AWS, Azure, GCP).",
        "Contribute to open-source projects.",
        "Maintain an updated GitHub portfolio.",
        "Optimize your LinkedIn profile.",
        "Practice coding interviews regularly.",
        "Stay updated with the latest AI technologies."
    ]

    for tip in tips:
        st.markdown(f"✅ {tip}")

    st.divider()

    # --------------------------------------------------
    # Career Growth Roadmap
    # --------------------------------------------------

    st.subheader("🚀 Career Growth Roadmap")

    roadmap = {
        "0-2 Years":
            "Focus on internships, strong projects, and building core technical skills.",

        "2-5 Years":
            "Take ownership of projects, learn system design, and mentor juniors.",

        "5+ Years":
            "Move toward senior engineering, AI leadership, architecture, or management roles."
    }

    for stage, description in roadmap.items():

        with st.expander(stage):

            st.write(description)

    st.divider()

    # --------------------------------------------------
    # Quick Checklist
    # --------------------------------------------------

    st.subheader("📝 Salary Improvement Checklist")

    checklist = [
        "Strong Resume",
        "Professional LinkedIn Profile",
        "Active GitHub Portfolio",
        "Relevant Certifications",
        "Internship Experience",
        "Mock Interview Practice"
    ]

    for item in checklist:
        st.checkbox(item)

    st.divider()

    # --------------------------------------------------
    # Important Note
    # --------------------------------------------------

    st.info(
        """
💡 **Note**

This salary estimate is generated using a trained machine learning model
based on factors such as experience level, employment type, job title,
location, remote work ratio, and company size.

Actual compensation may vary depending on the company, market conditions,
benefits, negotiation, and individual experience.
"""
    )

    st.divider()

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    st.caption(
        "🚀 CareerPilot AI • Salary Prediction Module • Developed by Nandini Bhatt"
    )