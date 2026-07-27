import streamlit as st
from src.ml.resume_quality import calculate_resume_quality
from src.utils.session_manager import initialize_session
def show_resume_feedback():
    # ==========================================================
    # Initialize Session
    # ==========================================================
    initialize_session()
    st.title("📝 Resume Feedback")
    st.markdown(
        """
Receive detailed feedback to improve your resume quality,
increase ATS compatibility, and strengthen your chances of
getting shortlisted.
"""
    )
    st.divider()
    # ==========================================================
    # Validate Resume
    # ==========================================================
    if not st.session_state.resume_uploaded:
        st.warning(
            "⚠ Please upload and analyze your resume first from the Resume Analysis page."
        )
        return
    # ==========================================================
    # Load Session Data
    # ==========================================================
    resume_text = st.session_state.resume_text
    sections = st.session_state.resume_sections
    with st.spinner("Analyzing Resume..."):
        resume_quality = calculate_resume_quality(
            sections,
            resume_text
        )
    # ==========================================================
    # Overall Feedback
    # ==========================================================
    st.subheader("⭐ Overall Resume Feedback")
    if resume_quality >= 90:
        overall_feedback = (
            "Excellent resume! It is well structured, ATS-friendly, "
            "and contains strong technical information."
        )
    elif resume_quality >= 80:
        overall_feedback = (
            "Very good resume. Minor improvements can further increase "
            "your interview chances."
        )
    elif resume_quality >= 70:
        overall_feedback = (
            "Good resume, but several sections can be strengthened "
            "to improve recruiter impact."
        )
    elif resume_quality >= 60:
        overall_feedback = (
            "Average resume. Consider improving formatting, content, "
            "and project descriptions."
        )
    else:
        overall_feedback = (
            "Your resume requires significant improvements before "
            "applying for competitive positions."
        )
    st.success(overall_feedback)
    st.metric(
        "Resume Quality Score",
        f"{resume_quality}/100"
    )
    st.progress(float(resume_quality) / 100)
    st.divider()

    # ==========================================================
    # Resume Quality Breakdown
    # ==========================================================

    st.subheader("📊 Resume Quality Breakdown")

    breakdown = {
        "Contact Information": 100 if sections.get("contact") else 0,
        "Professional Summary": 100 if sections.get("summary") else 0,
        "Education": 100 if sections.get("education") else 0,
        "Skills": 100 if sections.get("skills") else 0,
        "Projects": 100 if sections.get("projects") else 0,
        "Experience": 100 if sections.get("experience") else 0,
        "Certifications": 100 if sections.get("certifications") else 0,
    }

    for section_name, score in breakdown.items():

        col1, col2 = st.columns([3, 1])

        with col1:

            st.write(section_name)

            st.progress(score / 100)

        with col2:

            st.write(f"**{score}%**")

    st.divider()

    # ==========================================================
    # Section-wise Feedback
    # ==========================================================

    st.subheader("📄 Section-wise Feedback")

    if sections.get("summary"):

        st.success(
            "Professional Summary: Present. Keep it concise and tailor it to each job application."
        )

    else:

        st.warning(
            "Professional Summary: Missing. Add a short summary highlighting your strengths, skills, and career objective."
        )

    if sections.get("projects"):

        st.success(
            "Projects: Good. Include measurable results, technologies used, and your specific contributions."
        )

    else:

        st.warning(
            "Projects: Missing. Add academic or personal projects to showcase practical experience."
        )

    if sections.get("skills"):

        st.success(
            "Skills: Present. Organize them into categories such as Programming Languages, Frameworks, Tools, and Databases."
        )

    else:

        st.warning(
            "Skills: Missing. Add both technical and soft skills relevant to your target role."
        )

    if sections.get("experience"):

        st.success(
            "Experience: Present. Use action verbs and quantify achievements wherever possible."
        )

    else:

        st.info(
            "Experience: No work experience detected. Highlight internships, freelance work, or major academic projects instead."
        )

    if sections.get("education"):

        st.success(
            "Education: Present. Include your CGPA, relevant coursework, and academic achievements if applicable."
        )

    else:

        st.warning(
            "Education: Missing. Add your educational qualifications."
        )

    st.divider()

    # ==========================================================
    # Recruiter Observations
    # ==========================================================

    st.subheader("👨‍💼 Recruiter Observations")

    observations = []

    if len(resume_text.split()) < 300:
        observations.append(
            "Your resume appears relatively short. Recruiters generally prefer detailed project descriptions and technical achievements."
        )

    if len(resume_text.split()) > 800:
        observations.append(
            "Your resume is quite lengthy. Consider keeping it concise and focused."
        )

    if sections.get("projects") and sections.get("skills"):
        observations.append(
            "Your technical profile is supported by project work, which is a strong positive."
        )

    if not sections.get("summary"):
        observations.append(
            "A missing professional summary reduces the initial impact for recruiters."
        )

    if not observations:

        st.success(
            "Your resume presents a balanced profile with no major structural concerns."
        )

    else:

        for observation in observations:

            st.info(observation)

    st.divider()

    # ==========================================================
    # Resume Strengths
    # ==========================================================
    st.subheader("✅ Resume Strengths")
    strengths = []
    if sections.get("contact"):
        strengths.append("Contact information is present.")
    if sections.get("education"):
        strengths.append("Education section is available.")
    if sections.get("skills"):
        strengths.append("Skills section is included.")
    if sections.get("projects"):
        strengths.append("Projects section is included.")
    if sections.get("experience"):
        strengths.append("Experience section is available.")
    if len(resume_text.split()) > 300:
        strengths.append("Resume contains sufficient technical content.")
    if strengths:
        for item in strengths:
            st.success(item)
    else:
        st.warning("No major strengths could be detected.")
    st.divider()
    # ==========================================================
    # Areas for Improvement
    # ==========================================================
    st.subheader("⚠ Areas for Improvement")
    improvements = []
    if not sections.get("summary"):
        improvements.append(
            "Add a professional summary at the beginning of your resume."
        )
    if not sections.get("experience"):
        improvements.append(
            "Include internship or work experience if available."
        )
    if not sections.get("projects"):
        improvements.append(
            "Add technical projects that demonstrate your skills."
        )
    if not sections.get("certifications"):
        improvements.append(
            "Include relevant certifications to strengthen your profile."
        )
    if len(resume_text.split()) < 250:
        improvements.append(
            "Resume content is quite short. Add more details about projects, achievements, and technical work."
        )
    if resume_quality < 80:
        improvements.append(
            "Improve formatting and organize sections for better ATS compatibility."
        )
    if improvements:
        for item in improvements:
            st.warning(item)
    else:
        st.success(
            "Excellent! No major improvement areas were detected."
        )
    st.divider()
    # ==========================================================
    # Section Presence Analysis
    # ==========================================================
    st.subheader("📋 Resume Section Analysis")
    section_names = [
        "contact",
        "summary",
        "education",
        "skills",
        "projects",
        "experience",
        "certifications"
    ]
    for section in section_names:
        pretty_name = section.replace("_", " ").title()
        if sections.get(section):
            st.success(f"✅ {pretty_name}")
        else:
            st.error(f"❌ {pretty_name}")
    st.divider()    # ==========================================================
    # Final Recommendations
    # ==========================================================
    st.subheader("🎯 Final Recommendations")
    recommendations = []
    if resume_quality >= 90:
        recommendations.append(
            "Your resume is already highly competitive. Continue tailoring it for each job application."
        )
    if not sections.get("summary"):
        recommendations.append(
            "Add a strong professional summary to quickly communicate your value to recruiters."
        )
    if not sections.get("projects"):
        recommendations.append(
            "Include 2–4 technical projects with technologies used and measurable outcomes."
        )
    if not sections.get("experience"):
        recommendations.append(
            "Highlight internships, freelance work, hackathons, or leadership experience."
        )
    if not sections.get("certifications"):
        recommendations.append(
            "Add certifications from Coursera, Google, Microsoft, AWS, or similar platforms."
        )
    if len(resume_text.split()) < 300:
        recommendations.append(
            "Expand your project descriptions by mentioning your contributions, technologies, and results."
        )
    if not recommendations:
        recommendations.append(
            "Excellent work! No major improvements were detected."
        )
    for index, recommendation in enumerate(recommendations, start=1):
        st.write(f"**{index}.** {recommendation}")
    st.divider()
    # ==========================================================
    # Resume Readiness Checklist
    # ==========================================================
    st.subheader("📋 Resume Readiness Checklist")
    checklist = {
        "Contact Information": sections.get("contact"),
        "Professional Summary": sections.get("summary"),
        "Education": sections.get("education"),
        "Technical Skills": sections.get("skills"),
        "Projects": sections.get("projects"),
        "Experience": sections.get("experience"),
        "Certifications": sections.get("certifications")
    }
    for item, status in checklist.items():
        if status:
            st.success(f"✅ {item}")
        else:
            st.warning(f"⚠ {item}")
    st.divider()
    # ==========================================================
    # Resume Readiness Indicator
    # ==========================================================
    st.subheader("🚀 Resume Readiness")
    if resume_quality >= 90:
        st.success(
            "🌟 Ready to Apply — Your resume is highly competitive."
        )
    elif resume_quality >= 80:
        st.success(
            "✅ Almost Ready — A few small improvements will make it even stronger."
        )
    elif resume_quality >= 70:
        st.warning(
            "👍 Good Foundation — Improve a few sections before applying."
        )
    elif resume_quality >= 60:
        st.warning(
            "⚠ Needs Improvement — Strengthen your resume before applying."
        )
    else:
        st.error(
            "❌ Not Ready Yet — Your resume requires significant improvement."
        )
    st.divider()
    # ==========================================================
    # Footer
    # ==========================================================
    st.caption(
        "CareerPilot AI • Resume Feedback • Personalized Resume Review"
    )