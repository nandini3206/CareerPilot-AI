import base64
import os
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

def clean_html(html_str: str) -> str:
    """
    Strips leading and trailing whitespace per line to ensure Streamlit 
    never misinterprets 4+ space indented HTML lines as Markdown code blocks (<pre><code>).
    """
    return "\n".join(line.strip() for line in html_str.splitlines() if line.strip())

def show_home():
    """
    Renders the Enhanced CareerPilot AI Home Landing Page.
    Polished with modern AI SaaS design system elements, glassmorphism, 
    interactive KPI cards, platform ecosystem flow, and subtle micro-animations.
    """
    # =========================================================
    # 1. ENHANCED HERO SECTION WITH GRADIENT GLOW & PARTICLES
    # =========================================================
    logo_img = get_svg_logo_html(width=56, height=56)
    hero_html = clean_html(f"""
<div class="hero-container" style="text-align: center; padding: 3.5rem 2rem; position: relative; overflow: hidden; background: radial-gradient(circle at 50% 20%, rgba(99, 102, 241, 0.18) 0%, rgba(6, 182, 212, 0.08) 50%, rgba(11, 14, 23, 0.95) 100%); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 16px; backdrop-filter: blur(16px);">
<div style="position: absolute; top: -40px; left: 15%; width: 140px; height: 140px; background: rgba(99, 102, 241, 0.25); filter: blur(50px); border-radius: 50%; pointer-events: none;"></div>
<div style="position: absolute; bottom: -40px; right: 15%; width: 140px; height: 140px; background: rgba(6, 182, 212, 0.2); filter: blur(50px); border-radius: 50%; pointer-events: none;"></div>
<div style="margin-bottom: 1.25rem; display: flex; align-items: center; justify-content: center; gap: 0.85rem; position: relative;">
<div style="position: relative; display: inline-block;">
<div style="position: absolute; inset: -8px; background: radial-gradient(circle, rgba(99, 102, 241, 0.6) 0%, transparent 70%); border-radius: 50%; filter: blur(8px);"></div>
<div style="position: relative;">{logo_img}</div>
</div>
<span style="font-size: 1.75rem; font-weight: 800; letter-spacing: 0.04em; color: #F8FAFC;">CAREERPILOT AI</span>
</div>
<h1 style="font-size: 2.85rem; font-weight: 800; line-height: 1.2; margin-bottom: 1.15rem; background: linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 50%, #A5B4FC 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
Navigate Your Career Path with AI Precision
</h1>
<p style="font-size: 1.12rem; color: #94A3B8; max-width: 760px; margin: 0 auto 2.25rem auto; line-height: 1.65; font-weight: 400;">
From optimizing your resume for ATS algorithms to predicting your earning potential and mastering voice mock interviews — CareerPilot is your autonomous AI career copilot.
</p>
</div>
""")
    st.markdown(hero_html, unsafe_allow_html=True)

    # Primary Action CTA Button
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        if st.button("✨ Start Your Career Journey ➔", key="btn_start_journey", type="primary", use_container_width=True):
            st.session_state.current_page = "Resume Analysis"
            st.rerun()

    st.markdown("<div style='margin-bottom: 2.25rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 2. PLATFORM STATISTICS (RESPONSIVE KPI METRICS ROW)
    # =========================================================
    kpi_html = clean_html("""
<div style="display: flex; flex-wrap: wrap; gap: 0.85rem; justify-content: center; margin-bottom: 2.5rem;">
<div class="glass-panel" style="flex: 1; min-width: 170px; text-align: center; padding: 1rem 0.75rem; border-top: 2px solid #6366F1;">
<div style="font-size: 1.4rem; font-weight: 800; color: #A5B4FC; margin-bottom: 0.2rem;">🎯 95%</div>
<div style="font-size: 0.8rem; font-weight: 600; color: #94A3B8;">Resume Match Accuracy</div>
</div>
<div class="glass-panel" style="flex: 1; min-width: 170px; text-align: center; padding: 1rem 0.75rem; border-top: 2px solid #06B6D4;">
<div style="font-size: 1.4rem; font-weight: 800; color: #67E8F9; margin-bottom: 0.2rem;">🤖 12</div>
<div style="font-size: 0.8rem; font-weight: 600; color: #94A3B8;">AI Career Modules</div>
</div>
<div class="glass-panel" style="flex: 1; min-width: 170px; text-align: center; padding: 1rem 0.75rem; border-top: 2px solid #10B981;">
<div style="font-size: 1.4rem; font-weight: 800; color: #34D399; margin-bottom: 0.2rem;">📄 ATS</div>
<div style="font-size: 0.8rem; font-weight: 600; color: #94A3B8;">Resume Intelligence</div>
</div>
<div class="glass-panel" style="flex: 1; min-width: 170px; text-align: center; padding: 1rem 0.75rem; border-top: 2px solid #8B5CF6;">
<div style="font-size: 1.4rem; font-weight: 800; color: #C084FC; margin-bottom: 0.2rem;">🎙 Voice</div>
<div style="font-size: 0.8rem; font-weight: 600; color: #94A3B8;">Mock Simulation</div>
</div>
<div class="glass-panel" style="flex: 1; min-width: 170px; text-align: center; padding: 1rem 0.75rem; border-top: 2px solid #F59E0B;">
<div style="font-size: 1.4rem; font-weight: 800; color: #FBBF24; margin-bottom: 0.2rem;">⚡ Real-time</div>
<div style="font-size: 0.8rem; font-weight: 600; color: #94A3B8;">AI Analytics</div>
</div>
</div>
""")
    st.markdown(kpi_html, unsafe_allow_html=True)

    # =========================================================
    # 3. TRUST STRIP BANNER
    # =========================================================
    trust_html = clean_html("""
<div style="background: rgba(17, 24, 39, 0.5); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 10px; padding: 0.75rem 1.25rem; text-align: center; margin-bottom: 3rem;">
<div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #64748B; margin-bottom: 0.5rem;">
🚀 BUILT WITH MODERN AI &amp; MACHINE LEARNING
</div>
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 0.4rem;">
<span class="skill-chip">Sentence Transformers</span>
<span class="skill-chip">Machine Learning</span>
<span class="skill-chip">Groq LLMs</span>
<span class="skill-chip">Whisper Voice AI</span>
<span class="skill-chip">Vector Search</span>
<span class="skill-chip">Interactive Analytics</span>
</div>
</div>
""")
    st.markdown(trust_html, unsafe_allow_html=True)

    # =========================================================
    # 4. WHY CAREERPILOT AI? (CORE BENEFITS & OUTCOMES)
    # =========================================================
    st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Why CareerPilot AI?</h2>", unsafe_allow_html=True)
    
    b1, b2 = st.columns(2)
    with b1:
        c1_html = clean_html("""
<div class="glass-panel" style="border-left: 3px solid #6366F1; transition: transform 0.2s ease;">
<div class="glass-card-header">🎯 Beat the ATS Filters</div>
<p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.55; margin: 0;">
Extract keywords, match entity criteria, and optimize your resume structure to ensure 90%+ alignment with target employer requirements.
</p>
</div>
""")
        st.markdown(c1_html, unsafe_allow_html=True)

        c2_html = clean_html("""
<div class="glass-panel" style="border-left: 3px solid #06B6D4; transition: transform 0.2s ease;">
<div class="glass-card-header">📚 Close Your Skill Gaps</div>
<p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.55; margin: 0;">
Identify missing technical competencies and receive structured week-by-week milestone roadmaps complete with portfolio project ideas.
</p>
</div>
""")
        st.markdown(c2_html, unsafe_allow_html=True)

    with b2:
        c3_html = clean_html("""
<div class="glass-panel" style="border-left: 3px solid #10B981; transition: transform 0.2s ease;">
<div class="glass-card-header">💰 Know Your Market Worth</div>
<p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.55; margin: 0;">
Access data-backed machine learning compensation models tailored to your experience level, job title, and geographic location.
</p>
</div>
""")
        st.markdown(c3_html, unsafe_allow_html=True)

        c4_html = clean_html("""
<div class="glass-panel" style="border-left: 3px solid #8B5CF6; transition: transform 0.2s ease;">
<div class="glass-card-header">🎤 Interview with Confidence</div>
<p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.55; margin: 0;">
Practice live technical and behavioral mock interviews with speech-to-text voice recognition and instant AI performance feedback.
</p>
</div>
""")
        st.markdown(c4_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 5. PRODUCT STUDIOS OVERVIEW
    # =========================================================
    st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Explore Product Studios</h2>", unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown(clean_html("""
<div class="glass-panel" style="min-height: 140px; border-top: 3px solid #6366F1;">
<div class="glass-card-header">📄 Resume Studio</div>
<p style="font-size: 0.85rem; color: #94A3B8; line-height: 1.5; margin: 0;">PDF text parsing, section extraction, ATS keyword scoring, and bullet rewriter.</p>
</div>
"""), unsafe_allow_html=True)

    with s2:
        st.markdown(clean_html("""
<div class="glass-panel" style="min-height: 140px; border-top: 3px solid #06B6D4;">
<div class="glass-card-header">🎯 Career Intelligence</div>
<p style="font-size: 0.85rem; color: #94A3B8; line-height: 1.5; margin: 0;">ML classification engine predicting roles and regression model calculating salary ranges.</p>
</div>
"""), unsafe_allow_html=True)

    with s3:
        st.markdown(clean_html("""
<div class="glass-panel" style="min-height: 140px; border-top: 3px solid #10B981;">
<div class="glass-card-header">🎓 Learning Studio</div>
<p style="font-size: 0.85rem; color: #94A3B8; line-height: 1.5; margin: 0;">Skill gap analyzer generating customized week-by-week milestone learning paths.</p>
</div>
"""), unsafe_allow_html=True)

    with s4:
        st.markdown(clean_html("""
<div class="glass-panel" style="min-height: 140px; border-top: 3px solid #8B5CF6;">
<div class="glass-card-header">🎤 Interview Lab</div>
<p style="font-size: 0.85rem; color: #94A3B8; line-height: 1.5; margin: 0;">AI question generator and real-time Whisper speech-to-text voice mock interview simulator.</p>
</div>
"""), unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 6. CAREERPILOT AI ECOSYSTEM WORKFLOW PREVIEW
    # =========================================================
    st.markdown("<h2 style='text-align: center; margin-bottom: 0.5rem;'>CareerPilot AI Ecosystem</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; margin-bottom: 2rem;'>How our intelligent modules interconnect to drive end-to-end career acceleration</p>", unsafe_allow_html=True)

    eco_flow_html = clean_html("""
<div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 0.5rem; max-width: 960px; margin: 0 auto 3.5rem auto;">
<div class="glass-panel" style="padding: 0.65rem 0.95rem; margin: 0; font-size: 0.84rem; font-weight: 700; color: #F8FAFC; border-left: 3px solid #6366F1;">
📄 Resume Intelligence
</div>
<div style="color: #6366F1; font-weight: bold;">➔</div>
<div class="glass-panel" style="padding: 0.65rem 0.95rem; margin: 0; font-size: 0.84rem; font-weight: 700; color: #F8FAFC; border-left: 3px solid #06B6D4;">
🤖 Role Prediction
</div>
<div style="color: #06B6D4; font-weight: bold;">➔</div>
<div class="glass-panel" style="padding: 0.65rem 0.95rem; margin: 0; font-size: 0.84rem; font-weight: 700; color: #F8FAFC; border-left: 3px solid #10B981;">
💰 Salary Prediction
</div>
<div style="color: #10B981; font-weight: bold;">➔</div>
<div class="glass-panel" style="padding: 0.65rem 0.95rem; margin: 0; font-size: 0.84rem; font-weight: 700; color: #F8FAFC; border-left: 3px solid #F59E0B;">
🎯 Job Recommendation
</div>
<div style="color: #F59E0B; font-weight: bold;">➔</div>
<div class="glass-panel" style="padding: 0.65rem 0.95rem; margin: 0; font-size: 0.84rem; font-weight: 700; color: #F8FAFC; border-left: 3px solid #8B5CF6;">
📚 Learning Roadmap
</div>
<div style="color: #8B5CF6; font-weight: bold;">➔</div>
<div class="glass-panel" style="padding: 0.65rem 0.95rem; margin: 0; font-size: 0.84rem; font-weight: 700; color: #F8FAFC; border-left: 3px solid #EC4899;">
🎙 Interview Lab
</div>
<div style="color: #EC4899; font-weight: bold;">➔</div>
<div class="glass-panel" style="padding: 0.65rem 0.95rem; margin: 0; font-size: 0.84rem; font-weight: 700; color: #34D399; border-left: 3px solid #10B981;">
📊 Career Analytics
</div>
</div>
""")
    st.markdown(eco_flow_html, unsafe_allow_html=True)

    # =========================================================
    # 7. POWERED BY MODERN AI (FOOTER TECH BADGES & CREDITS)
    # =========================================================
    footer_html = clean_html("""
<div style="text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 2rem; margin-top: 2rem;">
<div style="font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: #64748B; margin-bottom: 1rem;">
POWERED BY MODERN AI &amp; MACHINE LEARNING
</div>
<div style="margin-bottom: 1.5rem; display: flex; flex-wrap: wrap; justify-content: center; gap: 0.4rem;">
<span class="skill-chip" style="transition: transform 0.2s ease;">PyTorch</span>
<span class="skill-chip" style="transition: transform 0.2s ease;">Scikit-Learn</span>
<span class="skill-chip" style="transition: transform 0.2s ease;">Sentence Transformers</span>
<span class="skill-chip" style="transition: transform 0.2s ease;">FAISS Vector Index</span>
<span class="skill-chip" style="transition: transform 0.2s ease;">Whisper Voice AI</span>
<span class="skill-chip" style="transition: transform 0.2s ease;">Groq LLaMA-3</span>
<span class="skill-chip" style="transition: transform 0.2s ease;">PyMuPDF</span>
<span class="skill-chip" style="transition: transform 0.2s ease;">Streamlit</span>
</div>
<div style="color: #94A3B8; font-size: 0.88rem; font-weight: 500;">
Designed &amp; Developed by <b style="color: #F8FAFC;">Nandini Bhatt</b>
</div>
<div style="margin-top: 0.3rem; color: #64748B; font-size: 0.8rem;">
&copy; 2026 CareerPilot AI
</div>
</div>
""")
    st.markdown(footer_html, unsafe_allow_html=True)
