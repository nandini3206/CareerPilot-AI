import textwrap
import streamlit as st
from components.cards import hero_header, empty_state_card
from components.metrics import kpi_card
from components.charts import create_section_completeness_chart, create_resume_composition_donut
from src.ml.resume_quality import calculate_resume_quality
from src.llms.resume_feedback import generate_resume_feedback

def show_resume_feedback():
    """
    Renders the Resume Feedback Studio view controller.
    Focuses on writing quality, narrative clarity, action verbs, and bullet impact (How to improve).
    Differentiated from ATS Score Studio.
    """
    # =========================================================
    # 1. HERO SECTION
    # =========================================================
    hero_header(
        title="Resume Feedback Studio",
        subtitle="AI-powered executive resume coaching, writing quality, action verbs & bullet impact feedback.",
        icon="💬"
    )

    resume_uploaded = st.session_state.get("resume_uploaded", False)
    resume_text = st.session_state.get("resume_text", "")
    resume_sections = st.session_state.get("resume_sections", {})
    resume_skills = st.session_state.get("resume_skills", [])
    file_name = st.session_state.get("resume_file_name", "")

    if not resume_uploaded:
        empty_state_card(
            title="Upload Candidate Resume to Generate Writing Feedback",
            message="Please upload a PDF resume in Resume Intelligence Studio first to unlock AI writing coaching.",
            icon="💬"
        )
        return

    # Small Context Notice Card
    notice_html = textwrap.dedent("""
    <div class="glass-panel" style="border-left: 3px solid #06B6D4; padding: 0.85rem 1.25rem; margin-bottom: 1.5rem;">
        <span style="font-size: 0.88rem; color: #CBD5E1;">
            💡 <b>Executive Coaching Mode:</b> This studio builds upon your ATS analysis and focuses on <b>writing quality</b>, <b>bullet impact</b>, <b>action verbs</b>, and <b>recruiter storytelling</b>.
        </span>
    </div>
    """).strip()
    st.markdown(notice_html, unsafe_allow_html=True)

    # Calculate Deterministic ML Metrics
    quality_score = calculate_resume_quality(resume_sections, resume_text)
    word_count = len(resume_text.split())
    has_contact = "Email & Phone Present" if ("@" in resume_text and any(c.isdigit() for c in resume_text)) else "Missing Contact"

    # =========================================================
    # 2. WRITING & QUALITY DIAGNOSTIC OVERVIEW (ML)
    # =========================================================
    st.markdown("### 📊 Writing Quality Overview")

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        kpi_card("Overall Quality", f"{quality_score}%", "Structure & Depth (ML)", "#6366F1")
    with k2:
        kpi_card("Resume Volume", f"{word_count}", "Total Words Extracted", "#06B6D4")
    with k3:
        kpi_card("Skill Entities", f"{len(resume_skills)}", "Extracted Tech Skills", "#10B981")
    with k4:
        kpi_card("Contact Details", "Verified" if "@" in resume_text else "Check Info", has_contact, "#8B5CF6")

    st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 3. STRUCTURAL COMPLETENESS & COMPOSITION (ML)
    # =========================================================
    c_col1, c_col2 = st.columns(2)
    with c_col1:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("#### 🍰 Section Word Distribution")
        st.plotly_chart(create_resume_composition_donut(resume_sections), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c_col2:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("#### 📑 Structural Completeness Meter")
        st.plotly_chart(create_section_completeness_chart(resume_sections), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    # =========================================================
    # 4. EXECUTIVE RECRUITER LLM FEEDBACK REPORT (GROQ LLAMA-3.3)
    # =========================================================
    st.markdown("### 🤖 Executive Resume Coaching Report")
    st.markdown("<p style='color: #94A3B8; font-size: 0.9rem;'>Click below to synthesize natural language recruiter guidance on writing clarity and bullet impact.</p>", unsafe_allow_html=True)

    feedback_cache_key = f"llm_writing_coaching_{file_name}_{len(resume_text)}"
    generate_btn = st.button("✨ Generate Executive Writing Feedback", type="primary", key="btn_gen_writing_fb")

    if generate_btn or feedback_cache_key in st.session_state:
        if feedback_cache_key not in st.session_state or generate_btn:
            with st.spinner("Connecting to Groq LLaMA-3.3 Executive Coaching Engine..."):
                try:
                    llm_output = generate_resume_feedback(
                        resume_text=resume_text
                    )
                    st.session_state[feedback_cache_key] = llm_output
                except Exception as e:
                    st.error(f"Failed to generate LLM feedback: {e}")
                    return

        raw_llm_markdown = st.session_state.get(feedback_cache_key, "")

        if raw_llm_markdown:
            st.markdown(textwrap.dedent(f"""
            <div class="glass-panel" style="border-left: 4px solid #6366F1; margin-bottom: 1.5rem;">
                <div style="font-weight: 700; font-size: 1.1rem; color: #F8FAFC;">
                    📝 Recruiter Writing & Storytelling Evaluation
                </div>
            </div>
            """).strip(), unsafe_allow_html=True)

            st.markdown(raw_llm_markdown)

    st.markdown("---")

    # =========================================================
    # 5. PRIORITY ACTIONABLE RECOMMENDATIONS (RECRUITER IMPACT)
    # =========================================================
    st.markdown("### 💡 Priority Actionable Recommendations")

    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown(textwrap.dedent("""
        <div class="glass-panel" style="border-left: 3px solid #EF4444;">
            <div style="font-weight: 700; color: #FCA5A5; margin-bottom: 0.5rem;">🔴 High Priority</div>
            <p style="font-size: 0.85rem; color: #94A3B8; line-height: 1.5;">
                <b>Rewrite Weak Duty Bullets:</b> Convert passive responsibility statements (e.g. "Responsible for code") into active impact statements.
            </p>
        </div>
        """).strip(), unsafe_allow_html=True)

    with r2:
        st.markdown(textwrap.dedent("""
        <div class="glass-panel" style="border-left: 3px solid #F59E0B;">
            <div style="font-weight: 700; color: #FBBF24; margin-bottom: 0.5rem;">🟡 Medium Priority</div>
            <p style="font-size: 0.85rem; color: #94A3B8; line-height: 1.5;">
                <b>Add Quantified Metrics:</b> Incorporate specific numerical outcomes (% performance gain, $ saved, users served) in experience bullets.
            </p>
        </div>
        """).strip(), unsafe_allow_html=True)

    with r3:
        st.markdown(textwrap.dedent("""
        <div class="glass-panel" style="border-left: 3px solid #6366F1;">
            <div style="font-weight: 700; color: #A5B4FC; margin-bottom: 0.5rem;">🔵 Optional Enhancements</div>
            <p style="font-size: 0.85rem; color: #94A3B8; line-height: 1.5;">
                <b>Stronger Action Verbs:</b> Begin every bullet with commanding power verbs like <i>Architected</i>, <i>Pioneered</i>, <i>Optimized</i>.
            </p>
        </div>
        """).strip(), unsafe_allow_html=True)

    st.markdown("---")

    # =========================================================
    # 6. SECTION-BY-SECTION WRITING REVIEW (PARSER)
    # =========================================================
    st.markdown("### 📑 Section-by-Section Content & Writing Review")

    sections_meta = [
        ("summary", "📜 Executive Summary", "Focus: Clarity, confidence, and high-level value proposition."),
        ("experience", "💼 Work Experience", "Focus: Impact, action verbs, and quantitative achievements."),
        ("projects", "🚀 Technical Projects", "Focus: Technical depth, outcomes, and architecture choices."),
        ("skills", "🛠️ Skill Entities", "Focus: Categorization, readability, and modern tech stack."),
        ("education", "🎓 Education & Credentials", "Focus: Presentation, degrees, and academic distinction."),
    ]

    for sec_key, sec_title, sec_guide in sections_meta:
        with st.expander(sec_title, expanded=(sec_key == "experience")):
            st.markdown(f"<p style='color: #6366F1; font-size: 0.82rem; font-weight: 600; margin-bottom: 0.5rem;'>💡 {sec_guide}</p>", unsafe_allow_html=True)
            content = resume_sections.get(sec_key, "").strip()
            if content:
                st.write(content)
            else:
                st.info(f"No {sec_key.capitalize()} section detected by parser.")

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 7. NEXT WORKFLOW CTA
    # =========================================================
    cta_html = textwrap.dedent("""
    <div class="hero-container" style="text-align: center; padding: 2rem;">
        <h3 style="margin-bottom: 0.5rem;">✍️ Ready to Rewrite Bullet Points into Metric Statements?</h3>
        <p style="color: #94A3B8; font-size: 0.95rem; margin-bottom: 1.25rem;">
            Proceed to the Resume Rewriter Studio to transform weak bullets into commanding XYZ-formula achievements.
        </p>
    </div>
    """).strip()
    st.markdown(cta_html, unsafe_allow_html=True)

    c_btn1, c_btn2, c_btn3 = st.columns([1, 2, 1])
    with c_btn2:
        if st.button("✍️ Continue to Resume Rewriter ➔", key="btn_next_rewriter", type="primary"):
            st.session_state.current_page = "Resume Rewriter"
            st.rerun()
