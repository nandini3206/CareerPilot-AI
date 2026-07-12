import streamlit as st
from datetime import datetime


def metric_card(title, value, subtitle, progress, icon):

    with st.container(border=True):

        st.markdown(f"### {icon} {title}")

        st.metric("", value)

        st.progress(int(progress))

        st.caption(subtitle)


def show_metrics(

    careerpilot_score,
    ats_score,
    skill_percentage,
    resume_quality,
    matching_count=0,
    missing_count=0,
    sections_found=0

):

    st.write("")
    st.markdown("## 📊 Dashboard Overview")
    st.caption("Quick summary of your resume analysis")

    st.write("")

    total = matching_count + missing_count

    row1 = st.columns(3)

    with row1[0]:

        metric_card(

            "ATS Score",

            f"{ats_score:.0f}%",

            "Applicant Tracking System",

            ats_score,

            "🎯"

        )

    with row1[1]:

        metric_card(

            "Skill Match",

            f"{skill_percentage:.0f}%",

            f"{matching_count} Matching Skills",

            skill_percentage,

            "✅"

        )

    with row1[2]:

        progress = min(missing_count * 10, 100)

        metric_card(

            "Missing Skills",

            str(missing_count),

            "Skills to Improve",

            progress,

            "❌"

        )

    st.write("")

    row2 = st.columns(3)

    with row2[0]:

        metric_card(

            "Resume Quality",

            f"{resume_quality:.0f}%",

            "Resume Completeness",

            resume_quality,

            "📄"

        )

    with row2[1]:

        section_progress = min(sections_found * 10, 100)

        metric_card(

            "Sections Found",

            str(sections_found),

            "Resume Structure",

            section_progress,

            "📑"

        )

    with row2[2]:

        now = datetime.now()

        with st.container(border=True):

            st.markdown("### 📅 Analysis Date")

            st.metric(

                "",

                now.strftime("%d %b %Y")

            )

            st.caption(

                now.strftime("%I:%M %p")

            )

    st.write("")

    with st.container(border=True):

        left, right = st.columns([1,5])

        with left:

            st.markdown("# 🚀")

        with right:

            st.markdown("### Keep Learning. Keep Growing.")

            st.caption(

                "You're already building a strong profile. Focus on improving missing skills, increasing ATS score, and strengthening your projects to maximize interview opportunities."

            )

            st.progress(int(careerpilot_score))