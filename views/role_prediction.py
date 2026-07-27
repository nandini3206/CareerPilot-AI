"""
====================================================
CareerPilot AI
Role Prediction
====================================================
"""

import streamlit as st

from src.integrations.role_prediction import predict_resume_role


# ==========================================================
# Page
# ==========================================================

def show_role_prediction():

    st.title("🎯 Role Prediction")

    st.caption(
        "Predict the most suitable career role using your analyzed resume."
    )

    st.divider()

    # ------------------------------------------------------
    # Resume Check
    # ------------------------------------------------------

    if not st.session_state.get("resume_uploaded", False):

        st.warning(
            "⚠ Please analyze your resume first from the Resume Analysis page."
        )

        return

    resume_text = st.session_state.resume_text
    resume_skills = st.session_state.resume_skills
    resume_sections = st.session_state.resume_sections
    resume_name = st.session_state.resume_file_name

    # ------------------------------------------------------
    # Resume Overview
    # ------------------------------------------------------

    st.subheader("📄 Resume Overview")

    c1, c2, c3 = st.columns(3)

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

    with c3:
        st.metric(
            "Sections",
            len(resume_sections)
        )

    st.divider()

    # ------------------------------------------------------
    # Predict Button
    # ------------------------------------------------------

    predict = st.button(
        "🚀 Predict Career Role",
        use_container_width=True
    )

    if not predict:
        return

    # ------------------------------------------------------
    # Prediction
    # ------------------------------------------------------

    with st.spinner("Analyzing resume..."):

        result = predict_resume_role(
            resume_text
        )

    predicted_role = result["role"]
    description = result["description"]
    st.session_state["predicted_role"] = predicted_role
    st.session_state["predicted_role_description"] = description

    st.success("Prediction Completed Successfully!")

    st.divider()

    # ------------------------------------------------------
    # Prediction Result
    # ------------------------------------------------------

    st.subheader("🏆 Predicted Career Role")

    st.info(
        f"### {predicted_role}"
    )

    st.write(description)

    st.divider()

    # ------------------------------------------------------
    # Resume Skills
    # ------------------------------------------------------

    st.subheader("🧠 Skills Detected")

    if resume_skills:

        cols = st.columns(3)

        for index, skill in enumerate(sorted(resume_skills)):

            cols[index % 3].success(skill)

    else:

        st.warning("No skills detected.")

    st.divider()
        # ------------------------------------------------------
    # Resume Sections
    # ------------------------------------------------------

    st.subheader("📑 Resume Sections")

    if resume_sections:

        section_names = list(resume_sections.keys())

        cols = st.columns(2)

        for index, section in enumerate(section_names):

            cols[index % 2].info(f"✅ {section.title()}")

    else:

        st.warning("No resume sections detected.")

    st.divider()

    # ------------------------------------------------------
    # Career Insights
    # ------------------------------------------------------

    st.subheader("💡 Career Insights")

    st.markdown(
        f"""
Based on the analysis of your resume, the model predicts that your
profile aligns most closely with **{predicted_role}**.

This prediction is generated using your resume content and detected
skills. It represents the career path that best matches your current
profile.
"""
    )

    st.divider()

    # ------------------------------------------------------
    # Recommended Next Steps
    # ------------------------------------------------------

    st.subheader("🚀 Recommended Next Steps")

    recommendations = [

        "Improve project portfolio related to the predicted role.",

        "Strengthen core technical and domain-specific skills.",

        "Build 2–3 advanced projects aligned with this career path.",

        "Practice interview questions for this role.",

        "Keep your resume updated with measurable achievements."

    ]

    for item in recommendations:

        st.markdown(f"- {item}")

    st.divider()

    # ------------------------------------------------------
    # Career Readiness
    # ------------------------------------------------------

    st.subheader("📈 Career Readiness")

    score = min(
        40 + len(resume_skills) * 3,
        100
    )

    st.progress(score / 100)

    st.metric(
        "Estimated Readiness",
        f"{score}%"
    )

    if score >= 80:

        st.success(
            "Excellent profile. Continue polishing projects and interview preparation."
        )

    elif score >= 60:

        st.info(
            "Good foundation. Add stronger projects and certifications."
        )

    else:

        st.warning(
            "Your profile can be strengthened by adding more relevant skills and projects."
        )

    st.divider()

    # ------------------------------------------------------
    # Suggested Career Paths
    # ------------------------------------------------------

    st.subheader("🧭 Suggested Career Growth")

    st.markdown(
        """
- Internship Preparation
- Resume Improvement
- Interview Preparation
- Skill Enhancement
- Industry Certifications
- Real-world AI/ML Projects
"""
    )

    st.divider()
        # ------------------------------------------------------
    # Learning Recommendations
    # ------------------------------------------------------

    st.subheader("📚 Recommended Learning Plan")

    learning_plan = {
        "ENGINEERING": [
            "Master Data Structures & Algorithms",
            "Build Full Stack Projects",
            "Learn System Design Basics",
            "Practice LeetCode regularly"
        ],
        "INFORMATION-TECHNOLOGY": [
            "Strengthen Python & SQL",
            "Learn Cloud Computing",
            "Build AI/ML Projects",
            "Study APIs & Deployment"
        ],
        "DATA SCIENCE": [
            "Practice Machine Learning",
            "Improve Statistics",
            "Master Pandas & NumPy",
            "Build End-to-End ML Projects"
        ]
    }

    roadmap = learning_plan.get(
        predicted_role.upper(),
        [
            "Continue improving domain knowledge",
            "Build industry-level projects",
            "Practice interview questions",
            "Earn relevant certifications"
        ]
    )

    for step in roadmap:
        st.markdown(f"✅ {step}")

    st.divider()

    # ------------------------------------------------------
    # Quick Action Checklist
    # ------------------------------------------------------

    st.subheader("📝 Action Checklist")

    checklist = [
        "Update resume with latest projects",
        "Optimize LinkedIn profile",
        "Apply for internships",
        "Practice aptitude & coding",
        "Prepare HR interview answers",
        "Keep learning consistently"
    ]

    for item in checklist:
        st.checkbox(item, value=False)

    st.divider()

    # ------------------------------------------------------
    # CareerPilot Tip
    # ------------------------------------------------------

    st.info(
        """
💡 **CareerPilot Tip**

Your predicted role is based on your current resume.
As you add stronger projects, certifications, internships,
and technical skills, your predicted role may improve or
become more specialized.
"""
    )

    st.divider()

    # ------------------------------------------------------
    # Footer
    # ------------------------------------------------------

    st.caption(
        "🚀 CareerPilot AI • Role Prediction Module • Developed by Nandini Bhatt"
    )
