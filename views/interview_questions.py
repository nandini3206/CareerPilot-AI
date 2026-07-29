import streamlit as st
from components.cards import hero_header, empty_state_card
from components.metrics import kpi_card


@st.cache_resource
def get_interview_inference():
    """
    Cached getter for InterviewPreparationInference backend.
    """
    try:
        from interview_preparation.inference import InterviewPreparationInference
        return InterviewPreparationInference()
    except Exception as e:
        st.error(f"Error loading Interview Questions Engine: {e}")
        return None


def show_interview_questions():
    """
    Renders the Interview Questions Studio view controller.
    Driven 100% by outputs from the InterviewPreparationInference backend.
    """
    # =========================================================
    # SECTION 1: HERO SECTION
    # =========================================================
    hero_header(
        title="🎤 Interview Questions Studio",
        subtitle="Personalized AI-powered interview question synthesis based on your resume profile and target role.",
        icon="🎤"
    )

    # =========================================================
    # REUSE EXISTING SESSION STATE (No duplicate parsing)
    # =========================================================
    resume_text = st.session_state.get("resume_text", "")
    resume_skills = st.session_state.get("resume_skills", [])
    resume_sections = st.session_state.get("resume_sections", {})
    projects = resume_sections.get("projects", [])

    role_prediction_results = st.session_state.get("role_prediction_results", [])
    default_role = role_prediction_results[0]["role"] if role_prediction_results else "Machine Learning Engineer"

    # =========================================================
    # SECTION 2: INTERVIEW ROLE SELECTOR
    # =========================================================
    st.markdown("### 🎯 Target Interview Role")
    available_roles = [
        "Machine Learning Engineer",
        "AI Engineer",
        "Data Scientist",
        "Backend Developer",
        "Full Stack Developer",
        "Software Engineer",
        "Data Engineer",
        "Data Analyst",
    ]

    selected_index = available_roles.index(default_role) if default_role in available_roles else 0

    c1, c2 = st.columns([3, 1])
    with c1:
        target_role = st.selectbox(
            "Interview Role",
            options=available_roles,
            index=selected_index,
            key="sel_interview_target_role",
        )
    with c2:
        st.markdown("<div style='margin-top: 1.7rem;'></div>", unsafe_allow_html=True)
        generate_btn = st.button("✨ Generate Questions", key="btn_gen_interview_q", type="primary")

    cache_key = f"iq_cache_{target_role}_{len(resume_skills)}_{len(projects)}"

    if generate_btn or cache_key not in st.session_state:
        inference = get_interview_inference()
        if inference:
            with st.spinner(f"Generating personalized interview questions for {target_role}..."):
                questions_data = inference.predict(
                    target_role=target_role,
                    predicted_role=default_role,
                    resume_text=resume_text,
                    extracted_skills=resume_skills,
                    projects=projects
                )
                st.session_state[cache_key] = questions_data
                st.session_state["generated_interview_questions"] = questions_data

    questions_data = st.session_state.get(cache_key) or st.session_state.get("generated_interview_questions", {})

    if not questions_data:
        empty_state_card(
            title="No Questions Generated",
            message="Click 'Generate Questions' above to synthesize personalized interview questions.",
            icon="⚠️"
        )
        return

    # Extract Question Categories (Strict schema: Technical, HR, Coding)
    tech_qs = questions_data.get("Technical", [])
    hr_qs = questions_data.get("HR", [])
    coding_qs = questions_data.get("Coding", [])

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    # Metrics Summary
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        kpi_card(label="🎯 Selected Role", value=target_role, subtext="Target Focus", accent_color="#6366F1")
    with m2:
        kpi_card(label="⚙️ Technical Questions", value=f"{len(tech_qs)} Questions", subtext="Domain Probing", accent_color="#8B5CF6")
    with m3:
        kpi_card(label="👥 HR & Behavioral", value=f"{len(hr_qs)} Questions", subtext="Culture & Soft Skills", accent_color="#06B6D4")
    with m4:
        kpi_card(label="💻 Coding Problems", value=f"{len(coding_qs)} Problems", subtext="Algorithmic Practice", accent_color="#10B981")

    st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 3: THREE PREMIUM TABS (Technical, HR, Coding)
    # =========================================================
    tab_tech, tab_hr, tab_coding = st.tabs(["⚙️ Technical Questions", "👥 HR & Behavioral Questions", "💻 Algorithmic Coding Practice"])

    def render_question_cards(q_list, category_icon, category_color="#6366F1"):
        if not q_list:
            st.info("No questions available in this category.")
            return

        for idx, q_text in enumerate(q_list, start=1):
            card_html = f"""<div class="glass-panel" style="padding: 1.25rem 1.5rem; margin-bottom: 1rem; border-left: 4px solid {category_color};">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
<div style="font-size: 0.82rem; font-weight: 700; color: #A5B4FC; text-transform: uppercase; letter-spacing: 0.05em;">
{category_icon} Question #{idx}
</div>
<span class="skill-chip" style="background: rgba(99, 102, 241, 0.15); color: #A5B4FC; border-color: rgba(99, 102, 241, 0.3); font-size: 0.75rem;">
{target_role}
</span>
</div>
<div style="font-size: 1.05rem; font-weight: 700; color: #F8FAFC; line-height: 1.45;">
{q_text}
</div>
</div>"""
            st.markdown(card_html, unsafe_allow_html=True)

    with tab_tech:
        render_question_cards(tech_qs, "⚙️ Technical", "#6366F1")

    with tab_hr:
        render_question_cards(hr_qs, "👥 HR & Behavioral", "#06B6D4")

    with tab_coding:
        render_question_cards(coding_qs, "💻 Coding", "#10B981")

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

    # Next Step CTA to Voice Interview
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("Practice in Voice Interview Studio 🎙️ ➔", key="btn_q_to_voice", type="primary"):
            st.session_state.current_page = "Voice Interview"
            st.rerun()
    # =========================================================
    # SECTION 5: VOICE INTERVIEW CTA BUTTON
    # =========================================================
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("Practice in Voice Interview Studio 🎙️ ➔", key="btn_q_to_voice", type="primary"):
            st.session_state.current_page = "Voice Interview"
            st.rerun()
