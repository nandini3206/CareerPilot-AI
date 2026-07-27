"""
=========================================================
CareerPilot AI
Learning Roadmap View
=========================================================
"""

import streamlit as st

from src.integrations.learning_roadmap import (
    generate_learning_roadmap
)



def show_learning_roadmap():

    st.title("🗺️ Personalized Learning Roadmap")

    st.markdown(
        """
Build a personalized roadmap based on your predicted role
and resume skills.
"""
    )

    st.divider()

    # -----------------------------
    # Resume Validation
    # -----------------------------

    if not st.session_state.get("resume_uploaded", False):
        st.warning(
            "⚠ Please analyze your resume first from the Resume Analysis page."
        )
        return

    role = st.session_state.get("predicted_role")

    if not role:

        st.warning(
            "⚠️ Please generate Role Prediction first."
        )
        return

    skills = st.session_state.get(
        "resume_skills",
        []
    )

    if not skills:

        st.warning(
            "⚠️ No skills were extracted."
        )
        return

    st.success(f"🎯 Target Role : **{role}**")

    st.write("### 📌 Current Skills")

    st.write(", ".join(skills))
        # ------------------------------------------------------
    # Generate Roadmap
    # ------------------------------------------------------

    generate = st.button(
        "🗺️ Generate Learning Roadmap",
        use_container_width=True
    )

    if not generate:
        return

    with st.spinner("Generating your personalized roadmap..."):

        roadmap = generate_learning_roadmap(
            role,
            skills
        )

    st.success("Roadmap Generated Successfully!")

    st.divider()

    # ------------------------------------------------------
    # Missing Skills
    # ------------------------------------------------------

    st.subheader("📉 Skill Gap Analysis")

    missing_skills = roadmap["missing_skills"]

    if missing_skills:

        cols = st.columns(3)

        for index, skill in enumerate(missing_skills):
            cols[index % 3].warning(skill)

    else:

        st.success(
            "🎉 Great! You already possess all the core skills for this role."
        )

    st.divider()

    # ------------------------------------------------------
    # Weekly Learning Plan
    # ------------------------------------------------------

    st.subheader("📅 Weekly Learning Plan")

    weekly_plan = roadmap["weekly_plan"]

    if weekly_plan:

        for week, topics in weekly_plan.items():

            with st.expander(f"📘 {week}", expanded=True):

                for topic in topics:
                    st.markdown(f"- {topic}")

    else:

        st.info("No weekly roadmap available.")

    st.divider()

    # ------------------------------------------------------
    # Recommended Projects
    # ------------------------------------------------------

    st.subheader("💼 Recommended Projects")

    projects = roadmap["recommended_projects"]

    if projects:

        for project in projects:
            st.success(f"🚀 {project}")

    else:

        st.info("No project recommendations available.")

    st.divider()
        # ------------------------------------------------------
    # Progress Tracker
    # ------------------------------------------------------

    st.subheader("✅ Learning Checklist")

    checklist_items = (
        missing_skills if missing_skills else
        ["Continue practicing and building projects"]
    )

    for skill in checklist_items:
        st.checkbox(skill)

    st.divider()

    # ------------------------------------------------------
    # CareerPilot Tip
    # ------------------------------------------------------

    st.info(
        """
💡 **CareerPilot Tip**

Complete your weekly roadmap one step at a time.
Alongside learning concepts, build projects and update your
resume regularly. Practical experience will make your profile
much stronger for internships and placements.
"""
    )

    st.divider()

    st.caption(
        "🚀 CareerPilot AI • Learning Roadmap Module • Developed by Nandini Bhatt"
    )