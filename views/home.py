import base64
import os
import textwrap
import streamlit as st

def get_svg_logo_html(width=48, height=48):
    """
    Loads assets/logo.svg and returns base64 img tag.
    Bulletproof — never breaks Markdown parsing.
    """
    svg_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.svg")
    if os.path.exists(svg_path):
        with open(svg_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        return f'<img src="data:image/svg+xml;base64,{b64}" width="{width}" height="{height}" style="vertical-align: middle; display: inline-block;">'
    return "✦"

def show_home():
    """
    Renders the CareerPilot AI Home Landing Page.
    Outcome-focused, clean, premium dark AI SaaS aesthetic.
    """
    # =========================================================
    # 1. HERO SECTION
    # =========================================================
    logo_img = get_svg_logo_html(width=52, height=52)
    hero_html = textwrap.dedent(f"""
    <div class="hero-container" style="text-align: center; padding: 3rem 2rem;">
        <div style="margin-bottom: 1.25rem; display: flex; align-items: center; justify-content: center; gap: 0.75rem;">
            {logo_img}
            <span style="font-size: 1.6rem; font-weight: 800; letter-spacing: 0.05em; color: #F8FAFC;">CAREERPILOT AI</span>
        </div>
        <h1 style="font-size: 2.75rem; font-weight: 800; line-height: 1.2; margin-bottom: 1rem; background: linear-gradient(135deg, #FFFFFF 0%, #CBD5E1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Navigate Your Career Path with AI Precision
        </h1>
        <p style="font-size: 1.1rem; color: #94A3B8; max-width: 720px; margin: 0 auto 2rem auto; line-height: 1.6;">
            From optimizing your resume for ATS algorithms to predicting your earning potential and mastering voice mock interviews — CareerPilot is your autonomous AI career copilot.
        </p>
    </div>
    """).strip()
    st.markdown(hero_html, unsafe_allow_html=True)

    # Primary Action CTA Button (Fold-Visible)
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        if st.button("✨ Start Your Career Journey ➔", key="btn_start_journey", type="primary"):
            st.session_state.current_page = "Resume Analysis"
            st.rerun()

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 2. WHY CAREERPILOT AI? (CORE BENEFITS & OUTCOMES)
    # =========================================================
    st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Why CareerPilot AI?</h2>", unsafe_allow_html=True)
    
    b1, b2 = st.columns(2)
    with b1:
        c1_html = textwrap.dedent("""
        <div class="glass-panel">
            <div class="glass-card-header">🎯 Beat the ATS Filters</div>
            <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.5;">
                Extract keywords, match entity criteria, and optimize your resume structure to ensure 90%+ alignment with target employer requirements.
            </p>
        </div>
        """).strip()
        st.markdown(c1_html, unsafe_allow_html=True)

        c2_html = textwrap.dedent("""
        <div class="glass-panel">
            <div class="glass-card-header">📚 Close Your Skill Gaps</div>
            <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.5;">
                Identify missing technical competencies and receive structured week-by-week milestone roadmaps complete with portfolio project ideas.
            </p>
        </div>
        """).strip()
        st.markdown(c2_html, unsafe_allow_html=True)

    with b2:
        c3_html = textwrap.dedent("""
        <div class="glass-panel">
            <div class="glass-card-header">💰 Know Your Market Worth</div>
            <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.5;">
                Access data-backed machine learning compensation models tailored to your experience level, job title, and geographic location.
            </p>
        </div>
        """).strip()
        st.markdown(c3_html, unsafe_allow_html=True)

        c4_html = textwrap.dedent("""
        <div class="glass-panel">
            <div class="glass-card-header">🎤 Interview with Confidence</div>
            <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.5;">
                Practice live technical and behavioral mock interviews with speech-to-text voice recognition and instant AI performance feedback.
            </p>
        </div>
        """).strip()
        st.markdown(c4_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 3. COMPLETE CAREER JOURNEY WORKFLOW (6-STEP PIPELINE)
    # =========================================================
    st.markdown("<h2 style='text-align: center; margin-bottom: 0.5rem;'>The 6-Step Career Journey</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; margin-bottom: 2rem;'>A complete end-to-end guidance pipeline designed for your success.</p>", unsafe_allow_html=True)

    steps_html = textwrap.dedent("""
    <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; margin-bottom: 3rem;">
        <div class="glass-panel" style="flex: 1; min-width: 150px; text-align: center; padding: 1.25rem 0.75rem;">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📄</div>
            <div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC;">1. Upload Resume</div>
            <div style="font-size: 0.78rem; color: #64748B; margin-top: 0.25rem;">Parse & Extract</div>
        </div>
        <div class="glass-panel" style="flex: 1; min-width: 150px; text-align: center; padding: 1.25rem 0.75rem;">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📊</div>
            <div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC;">2. AI Resume Analysis</div>
            <div style="font-size: 0.78rem; color: #64748B; margin-top: 0.25rem;">ATS & Keywords</div>
        </div>
        <div class="glass-panel" style="flex: 1; min-width: 150px; text-align: center; padding: 1.25rem 0.75rem;">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎯</div>
            <div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC;">3. Career Intelligence</div>
            <div style="font-size: 0.78rem; color: #64748B; margin-top: 0.25rem;">Role & Salary ML</div>
        </div>
        <div class="glass-panel" style="flex: 1; min-width: 150px; text-align: center; padding: 1.25rem 0.75rem;">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎓</div>
            <div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC;">4. Learning Roadmap</div>
            <div style="font-size: 0.78rem; color: #64748B; margin-top: 0.25rem;">Bridge Skill Gaps</div>
        </div>
        <div class="glass-panel" style="flex: 1; min-width: 150px; text-align: center; padding: 1.25rem 0.75rem;">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎤</div>
            <div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC;">5. Interview Prep</div>
            <div style="font-size: 0.78rem; color: #64748B; margin-top: 0.25rem;">Voice Mock AI</div>
        </div>
        <div class="glass-panel" style="flex: 1; min-width: 150px; text-align: center; padding: 1.25rem 0.75rem; border-color: rgba(16, 185, 129, 0.4);">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎉</div>
            <div style="font-weight: 700; font-size: 0.88rem; color: #34D399;">6. Career Ready</div>
            <div style="font-size: 0.78rem; color: #10B981; margin-top: 0.25rem;">Offer Secured</div>
        </div>
    </div>
    """).strip()
    st.markdown(steps_html, unsafe_allow_html=True)

    # =========================================================
    # 4. PRODUCT STUDIOS OVERVIEW
    # =========================================================
    st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Explore Product Studios</h2>", unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown(textwrap.dedent("""
        <div class="glass-panel">
            <div class="glass-card-header">📄 Resume Studio</div>
            <p style="font-size: 0.85rem; color: #94A3B8;">PDF text parsing, section extraction, ATS keyword scoring, and bullet rewriter.</p>
        </div>
        """).strip(), unsafe_allow_html=True)

    with s2:
        st.markdown(textwrap.dedent("""
        <div class="glass-panel">
            <div class="glass-card-header">🎯 Career Intelligence</div>
            <p style="font-size: 0.85rem; color: #94A3B8;">ML classification engine predicting roles and regression model calculating salary ranges.</p>
        </div>
        """).strip(), unsafe_allow_html=True)

    with s3:
        st.markdown(textwrap.dedent("""
        <div class="glass-panel">
            <div class="glass-card-header">🎓 Learning Studio</div>
            <p style="font-size: 0.85rem; color: #94A3B8;">Skill gap analyzer generating customized week-by-week milestone learning paths.</p>
        </div>
        """).strip(), unsafe_allow_html=True)

    with s4:
        st.markdown(textwrap.dedent("""
        <div class="glass-panel">
            <div class="glass-card-header">🎤 Interview Lab</div>
            <p style="font-size: 0.85rem; color: #94A3B8;">AI question generator and real-time Whisper speech-to-text voice mock interview simulator.</p>
        </div>
        """).strip(), unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 4rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 5. POWERED BY MODERN AI (FOOTER TECH BADGES & CREDITS)
    # =========================================================
    footer_html = textwrap.dedent("""
    <div style="text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 2rem; margin-top: 2rem;">
        <div style="font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: #64748B; margin-bottom: 1rem;">
            POWERED BY MODERN AI & MACHINE LEARNING
        </div>
        <div style="margin-bottom: 1.5rem;">
            <span class="skill-chip">PyTorch</span>
            <span class="skill-chip">Scikit-Learn</span>
            <span class="skill-chip">FAISS Vector Index</span>
            <span class="skill-chip">Whisper Voice AI</span>
            <span class="skill-chip">Groq LLaMA-3</span>
            <span class="skill-chip">PyMuPDF</span>
            <span class="skill-chip">Streamlit</span>
        </div>
        <div style="color: #94A3B8; font-size: 0.88rem; font-weight: 500;">
            Designed &amp; Developed by <b style="color: #F8FAFC;">Nandini Bhatt</b>
        </div>
        <div style="margin-top: 0.3rem; color: #64748B; font-size: 0.8rem;">
            &copy; 2026 CareerPilot AI
        </div>
    </div>
    """).strip()
    st.markdown(footer_html, unsafe_allow_html=True)
