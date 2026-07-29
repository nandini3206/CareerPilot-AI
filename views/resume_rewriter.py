import textwrap
import streamlit as st
from components.cards import hero_header, empty_state_card
from src.llms.resume_rewriter import generate_full_rewritten_resume, create_docx_resume

PRESET_ROLES = {
    "Machine Learning Engineer": "Machine Learning Engineer / AI Specialist",
    "Data Scientist": "Data Scientist / Analytics Lead",
    "AI Engineer": "AI Engineer / LLM Systems Developer",
    "Backend Developer": "Backend Engineer / API Systems Architect",
    "Software Engineer": "Full Stack Software Engineer"
}

def show_resume_rewriter():
    """
    Renders the Resume Rewriter Studio view controller.
    Generates a SINGLE FULL HIGH-ATS REWRITTEN RESUME.
    Includes Copy to Clipboard and Download as Word (.docx) & Text (.txt).
    """
    # =========================================================
    # 1. PURPLE HERO SECTION
    # =========================================================
    hero_header(
        title="Resume Rewriter Studio",
        subtitle="Generate a single, complete High-ATS optimized resume with one-click Word (.docx) export.",
        icon="✍️"
    )

    resume_uploaded = st.session_state.get("resume_uploaded", False)
    resume_text = st.session_state.get("resume_text", "")
    file_name = st.session_state.get("resume_file_name", "Resume")
    clean_base_name = file_name.rsplit(".", 1)[0] if "." in file_name else file_name

    if not resume_uploaded:
        empty_state_card(
            title="Upload Candidate Resume to Enable Full Resume Rewriter",
            message="Please upload a PDF resume in Resume Intelligence Studio first to generate your High-ATS complete rewritten resume.",
            icon="✍️"
        )
        return

    # =========================================================
    # 2. REWRITE CONFIGURATION CONTROLS
    # =========================================================
    st.markdown("### ⚙️ High-ATS Rewrite Configuration")

    cfg1, cfg2 = st.columns(2)
    with cfg1:
        tone_option = st.selectbox(
            "Optimization Tone & Formula",
            options=["High ATS & Impact Optimized (XYZ Formula)", "Executive Leadership", "Technical & Concise"],
            index=0,
            key="sb_full_rewriter_tone"
        )
    with cfg2:
        target_role = st.text_input(
            "Target Job Role Context",
            value=st.session_state.get("selected_preset_role", "Machine Learning Engineer"),
            key="ti_full_rewriter_role"
        )

    # Trigger Generation
    btn_generate_full = st.button("✨ Generate Full High-ATS Rewritten Resume", type="primary", key="btn_gen_full_resume")

    full_resume_key = f"full_high_ats_resume_{clean_base_name}_{target_role}"

    if btn_generate_full or full_resume_key in st.session_state:
        if full_resume_key not in st.session_state or btn_generate_full:
            with st.spinner("Generating single complete High-ATS optimized resume via Groq LLaMA-3.3..."):
                try:
                    rewritten_doc = generate_full_rewritten_resume(
                        resume_text=resume_text,
                        target_role=target_role,
                        tone=tone_option
                    )
                    st.session_state[full_resume_key] = rewritten_doc
                except Exception as e:
                    st.error(f"Failed to generate rewritten resume: {e}")
                    return

        rewritten_resume_text = st.session_state.get(full_resume_key, "")

        if rewritten_resume_text:
            st.markdown("---")
            st.markdown("### 📄 Complete High-ATS Rewritten Resume")

            # Download & Copy Action Bar
            st.markdown(textwrap.dedent(f"""
            <div class="glass-panel" style="border-left: 4px solid #10B981; margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
                    <div>
                        <span style="font-weight: 700; color: #34D399; font-size: 1.05rem;">
                            ✓ High-ATS Optimization Complete
                        </span>
                        <div style="font-size: 0.82rem; color: #94A3B8; margin-top: 0.2rem;">
                            Formatted with commanding action verbs, XYZ metrics, and target ATS keywords.
                        </div>
                    </div>
                </div>
            </div>
            """).strip(), unsafe_allow_html=True)

            d_col1, d_col2, d_col3 = st.columns([1, 1, 1])

            # Generate Docx binary
            try:
                docx_bytes = create_docx_resume(rewritten_resume_text)
            except Exception as e:
                docx_bytes = b""

            with d_col1:
                st.download_button(
                    label="📥 Download as Word (.docx)",
                    data=docx_bytes,
                    file_name=f"{clean_base_name}_High_ATS.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key="btn_dl_docx",
                    type="primary"
                )

            with d_col2:
                st.download_button(
                    label="📄 Download as Text (.txt)",
                    data=rewritten_resume_text.encode("utf-8"),
                    file_name=f"{clean_base_name}_High_ATS.txt",
                    mime="text/plain",
                    key="btn_dl_txt",
                    type="primary"
                )

            with d_col3:
                st.info("📋 Click top-right of code box below to COPY full text")

            # Render Copyable Resume Code Box
            st.code(rewritten_resume_text, language=None)

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 3. NEXT WORKFLOW CTA
    # =========================================================
    cta_html = textwrap.dedent("""
    <div class="hero-container" style="text-align: center; padding: 2rem;">
        <h3 style="margin-bottom: 0.5rem;">🎯 Ready for Role Prediction & Salary Intelligence?</h3>
        <p style="color: #94A3B8; font-size: 0.95rem; margin-bottom: 1.25rem;">
            Proceed to the Career Intelligence Studio to predict target job roles, salary ranges, and job recommendations.
        </p>
    </div>
    """).strip()
    st.markdown(cta_html, unsafe_allow_html=True)

    c_btn1, c_btn2, c_btn3 = st.columns([1, 2, 1])
    with c_btn2:
        if st.button("🎯 Continue to Career Intelligence ➔", key="btn_next_ci", type="primary"):
            st.session_state.current_page = "Role Prediction"
            st.rerun()
