import streamlit as st

from src.ml.resume_quality import calculate_resume_quality
from src.ml.ats_scorer import calculate_ats_score
from src.ml.skill_matcher import compare_skills

from src.utils.session_manager import (
    initialize_session,
    process_resume,
    process_job_description,
    clear_session,
)


def show_resume_analysis():

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

        /* ---- Fix: Upload labels too light / invisible ---- */
        [data-testid="stFileUploader"] label p {
            color: #f5f6fa !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
        }

        /* ---- Fix: Resume Preview textarea contrast ---- */
        .stTextArea textarea {
            background-color: #1c212b !important;
            color: #f5f6fa !important;
            border: 1px solid #3a4150 !important;
            -webkit-text-fill-color: #f5f6fa !important;
            opacity: 1 !important;
        }
        .stTextArea textarea:disabled {
            background-color: #1c212b !important;
            color: #f5f6fa !important;
            -webkit-text-fill-color: #f5f6fa !important;
            opacity: 1 !important;
        }
        .stTextArea textarea::placeholder {
            color: #9aa4b2 !important;
        }
        .stTextArea label p {
            color: #d5d9e0 !important;
        }

        /* ---- Fix: Resume Overview metrics too light ---- */
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

        /* ---- Fix: Expander header turning white when opened ---- */
        [data-testid="stExpander"] summary {
            background-color: #1c212b !important;
            border-radius: 6px !important;
        }
        [data-testid="stExpander"] summary:hover {
            background-color: #262b36 !important;
        }
        [data-testid="stExpander"] summary p,
        [data-testid="stExpander"] summary span,
        [data-testid="stExpander"] summary svg {
            color: #f5f6fa !important;
            fill: #f5f6fa !important;
        }

        /* ---- Fix: Hero AI box - fill remaining space ---- */
        .hero-ai-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            min-height: 280px;
            border-radius: 16px;
            background-color: #161b22;
            border: 1px solid #30363d;
        }
        .hero-ai-box .hero-emoji {
            font-size: 6rem;
            line-height: 1;
            margin-bottom: 0.5rem;
        }
        .hero-ai-box .hero-caption {
            color: #c9d1d9;
            font-size: 1rem;
        }

        /* ---- Fix: Footer too big - make compact & centered ---- */
        .footer-box {
            text-align: center;
            max-width: 480px;
            margin: 0 auto;
        }
        .footer-box h2 {
            font-size: 1.3rem;
            margin-bottom: 0.1rem;
        }
        .footer-box h3 {
            font-size: 0.95rem;
            font-weight: 400;
            margin-top: 0;
            color: #c9d1d9;
        }
        .footer-box p {
            font-size: 0.85rem;
            margin: 0.3rem 0;
        }
        .footer-box ul {
            list-style: none;
            padding: 0;
            font-size: 0.82rem;
            margin: 0.4rem 0;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # ==========================================================
    # Hero Section
    # ==========================================================

    left, right = st.columns([3, 2])

    with left:

        st.title("📄 Resume Analysis")

        st.markdown(
            """
### Let CareerPilot AI analyze your resume

CareerPilot AI will:

- ✅ Parse your Resume
- ✅ Extract Resume Sections
- ✅ Detect Skills
- ✅ Calculate Resume Quality
- ✅ Calculate ATS Score (Optional)
- ✅ Compare Resume with Job Description
"""
        )

    with right:

        st.markdown(
            """
            <div class="hero-ai-box">
                <div class="hero-emoji">🤖</div>
                <div class="hero-caption">AI Resume Analyzer</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # ==========================================================
    # Upload Section
    # ==========================================================

    st.subheader("📂 Upload Documents")

    resume = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        key="resume_upload"
    )

    job = st.file_uploader(
        "Upload Job Description (TXT - Optional)",
        type=["txt"],
        key="jd_upload"
    )

    analyze = st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    )

    # ==========================================================
    # Analyze Resume
    # ==========================================================

    if analyze:

        if resume is None:

            st.warning("⚠️ Please upload your resume first.")

            st.stop()

        with st.spinner("🤖 CareerPilot AI is analyzing your resume..."):

            try:

                process_resume(resume)

                if job is not None:

                    process_job_description(job)

                st.success("✅ Resume analyzed successfully!")

            except Exception as e:

                st.error("❌ Failed to analyze the resume.")

                st.exception(e)

                return

    # ==========================================================
    # Wait Until Resume Is Uploaded
    # ==========================================================

    if not st.session_state.resume_uploaded:

        st.info("📄 Upload your resume to begin analysis.")

        return

    # ==========================================================
    # Load Session Data
    # ==========================================================

    resume_text = st.session_state.resume_text

    sections = st.session_state.resume_sections

    skills = st.session_state.resume_skills

    # ==========================================================
    # Resume Quality
    # ==========================================================

    resume_score = calculate_resume_quality(
        sections,
        resume_text
    )

    # ==========================================================
    # Resume Overview
    # ==========================================================

    st.divider()

    st.subheader("📊 Resume Overview")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Resume Quality",
            f"{resume_score}/100"
        )

    with c2:

        st.metric(
            "Skills Found",
            len(skills)
        )

    with c3:

        st.metric(
            "Words",
            len(resume_text.split())
        )

    st.divider()

    st.subheader("📋 Resume Information")

    left, right = st.columns(2)

    with left:

        st.markdown("### 📝 Summary")

        if sections["summary"].strip():

            st.success(sections["summary"])

        else:

            st.warning("Summary section not found.")

        st.markdown("### 🎓 Education")

        if sections["education"].strip():

            st.success(sections["education"])

        else:

            st.warning("Education section not found.")

    with right:

        st.markdown("### 💼 Experience")

        if sections["experience"].strip():

            st.success(sections["experience"])

        else:

            st.warning("Experience section not found.")

        st.markdown("### 🚀 Projects")

        if sections["projects"].strip():

            st.success(sections["projects"])

        else:

            st.warning("Projects section not found.")
    # ==========================================================
    # Skills
    # ==========================================================

    st.divider()

    st.subheader("🛠 Skills Detected")

    if skills:

        cols = st.columns(3)

        for i, skill in enumerate(skills):

            cols[i % 3].success(skill)

    else:

        st.warning(
            """
No predefined skills were detected.

Possible reasons:

• Resume uses uncommon skill names
• skills.txt needs more entries
• Resume text extraction failed
"""
        )

    # ==========================================================
    # Resume Statistics
    # ==========================================================

    st.divider()

    st.subheader("📈 Resume Statistics")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info("📄 Pages Parsed : 1")

    with c2:

        section_count = len(
            [value for value in sections.values() if value.strip()]
        )

        st.info(f"📂 Sections Found : {section_count}")

    with c3:

        st.info(f"🛠 Skills Detected : {len(skills)}")

    # ==========================================================
    # ATS Analysis
    # ==========================================================

    st.divider()

    st.subheader("🎯 ATS Analysis")

    if not st.session_state.job_uploaded:

        st.info(
            """
Upload a Job Description to unlock:

• ATS Score
• Skill Matching
• Missing Skills
• Resume vs Job Analysis
"""
        )

    else:

        ats_score = calculate_ats_score(

            resume_text,

            st.session_state.job_description

        )

        match = compare_skills(

            resume_text,

            st.session_state.job_description

        )

        st.metric(

            "ATS Score",

            f"{ats_score}%"

        )

        st.progress(min(ats_score / 100, 1.0))

        if ats_score >= 90:

            st.success("🎉 Excellent ATS Compatibility")

        elif ats_score >= 80:

            st.success("✅ Very Good ATS Compatibility")

        elif ats_score >= 70:

            st.info("👍 Good ATS Compatibility")

        else:

            st.warning(
                """
Your resume has a lower match with this Job Description.

Suggestions:

• Add missing skills only if you genuinely have them.
• Tailor project descriptions.
• Highlight relevant experience.
"""
            )

        st.divider()

        st.subheader("🛠 Skill Match")

        left, right = st.columns(2)

        with left:

            st.markdown("### ✅ Matching Skills")

            if match["matching"]:

                for skill in match["matching"]:

                    st.success(skill)

            else:

                st.warning("No matching skills found.")

        with right:

            st.markdown("### ❌ Missing Skills")

            if match["missing"]:

                for skill in match["missing"]:

                    st.error(skill)

            else:

                st.success("No missing skills.")

        st.divider()

        st.subheader("📊 ATS Summary")

        total = len(match["matching"]) + len(match["missing"])

        if total == 0:

            coverage = 0

        else:

            coverage = round(

                (len(match["matching"]) / total) * 100,

                1

            )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(

                "Matching Skills",

                len(match["matching"])

            )

        with c2:

            st.metric(

                "Missing Skills",

                len(match["missing"])

            )

        with c3:

            st.metric(

                "Skill Coverage",

                f"{coverage}%"

            )

    # ==========================================================
    # Resume Preview
    # ==========================================================

    st.divider()

    st.subheader("📄 Resume Preview")

    preview = resume_text[:2500]

    st.text_area(
        "Extracted Resume Text",
        preview,
        height=320,
        disabled=True
    )

    # ==========================================================
    # Parsed Resume Sections
    # ==========================================================

    st.divider()

    st.subheader("📂 Parsed Resume Sections")

    with st.expander("📝 Summary", expanded=False):

        if sections["summary"].strip():

            st.write(sections["summary"])

        else:

            st.info("Summary section not found.")

    with st.expander("🎓 Education"):

        if sections["education"].strip():

            st.write(sections["education"])

        else:

            st.info("Education section not found.")

    with st.expander("🛠 Skills"):

        if sections["skills"].strip():

            st.write(sections["skills"])

        else:

            st.info("Skills section not found.")

    with st.expander("🚀 Projects"):

        if sections["projects"].strip():

            st.write(sections["projects"])

        else:

            st.info("Projects section not found.")

    with st.expander("💼 Experience"):

        if sections["experience"].strip():

            st.write(sections["experience"])

        else:

            st.info("Experience section not found.")

    # ==========================================================
    # Analysis Summary
    # ==========================================================

    st.divider()

    st.subheader("📊 Analysis Summary")

    st.success(
        f"""
✅ Resume Quality Score : {resume_score}/100

✅ Skills Detected : {len(skills)}

✅ Resume Sections Parsed : {len([v for v in sections.values() if v.strip()])}
"""
    )

    if st.session_state.job_uploaded:

        st.info(
            f"""
ATS Score : {ats_score}%

Matching Skills : {len(match['matching'])}

Missing Skills : {len(match['missing'])}
"""
        )

    # ==========================================================
    # Uploaded Files
    # ==========================================================

    st.divider()

    st.subheader("📁 Uploaded Files")

    left, right = st.columns(2)

    with left:

        st.success(
            f"📄 Resume : {st.session_state.resume_file_name}"
        )

    with right:

        if st.session_state.job_uploaded:

            st.success(
                f"📋 Job Description : {st.session_state.job_file_name}"
            )

        else:

            st.info("No Job Description Uploaded")

    # ==========================================================
    # Resume Status
    # ==========================================================

    st.divider()

    st.subheader("📌 Current Status")

    status1, status2 = st.columns(2)

    with status1:

        if st.session_state.resume_uploaded:

            st.success("✅ Resume Loaded")

        else:

            st.warning("Resume Not Uploaded")

    with status2:

        if st.session_state.job_uploaded:

            st.success("✅ Job Description Loaded")

        else:

            st.info("Job Description Optional")

    # ==========================================================
    # ACTION BUTTONS
    # ==========================================================

    st.divider()

    st.subheader("⚙️ Actions")

    btn1, btn2 = st.columns(2)

    with btn1:

        if st.button(
            "🔄 Analyze Another Resume",
            use_container_width=True
        ):

            clear_session()

            st.rerun()

    with btn2:

        st.button(
            "📥 Download Report",
            use_container_width=True,
            disabled=True,
            help="PDF Report will be available in the next update."
        )

    # ==========================================================
    # QUICK INSIGHTS
    # ==========================================================

    st.divider()

    st.subheader("🚀 Quick Insights")

    insights = []

    if resume_score >= 85:
        insights.append("✅ Your resume quality is excellent.")
    elif resume_score >= 70:
        insights.append("👍 Your resume quality is good but can still be improved.")
    else:
        insights.append("⚠️ Your resume needs improvement.")

    if len(skills) >= 10:
        insights.append("🛠 Strong technical skillset detected.")
    elif len(skills) >= 5:
        insights.append("📈 A decent number of technical skills were detected.")
    else:
        insights.append("⚠️ Very few technical skills were detected.")

    if st.session_state.job_uploaded:

        if ats_score >= 85:
            insights.append("🎯 Excellent ATS compatibility with the uploaded Job Description.")
        elif ats_score >= 70:
            insights.append("👍 Good ATS compatibility.")
        else:
            insights.append("⚠️ Tailor your resume more closely to the Job Description.")

    else:

        insights.append("📄 Upload a Job Description to unlock ATS analysis.")

    for item in insights:

        st.write(item)

    # ==========================================================
    # DISCLAIMER
    # ==========================================================

    st.divider()

    st.info(
        """
**Disclaimer**

CareerPilot AI provides AI-assisted resume analysis based on
resume parsing, keyword matching, semantic similarity,
and machine learning models.

This analysis is intended to help improve your resume,
but it does not guarantee interview selection or job offers.
"""
    )

    # ==========================================================
    # FOOTER
    # ==========================================================

    st.divider()

    st.markdown(
        """
        <div class="footer-box">
            <h2>🚀 CareerPilot AI</h2>
            <h3>Your Personal AI Career Mentor</h3>
            <p>Analyze • Improve • Prepare • Get Hired</p>
            <hr>
            <p><strong>🔹 Powered By</strong></p>
            <ul>
                <li>📄 Resume Parsing</li>
                <li>🤖 Artificial Intelligence</li>
                <li>🧠 Machine Learning</li>
                <li>🎯 ATS Optimization</li>
                <li>🔍 Semantic Skill Matching</li>
            </ul>
            <hr>
            <p><strong>Developed by Nandini Bhatt</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    show_resume_analysis()