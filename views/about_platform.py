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

def show_about_platform():
    """
    Renders the About Platform SaaS page for CareerPilot AI.
    UI-only, static information page with design system integration.
    """
    # ---------------------------------------------------------
    # SECTION 1: PREMIUM HERO
    # ---------------------------------------------------------
    logo_img = get_svg_logo_html(width=56, height=56)
    hero_html = textwrap.dedent(f"""
    <div class="hero-container" style="text-align: center; padding: 3rem 2rem; position: relative;">
        <div style="display: flex; justify-content: center; align-items: center; gap: 1rem; margin-bottom: 1.25rem;">
            {logo_img}
            <span style="font-size: 2.2rem; font-weight: 800; letter-spacing: -0.02em; color: #F8FAFC;">
                CareerPilot AI
            </span>
        </div>
        <div style="display: flex; justify-content: center; align-items: center; gap: 0.75rem; margin-bottom: 1.25rem;">
            <span style="background: rgba(99, 102, 241, 0.2); border: 1px solid rgba(99, 102, 241, 0.4); color: #A5B4FC; padding: 0.35rem 0.85rem; border-radius: 9999px; font-size: 0.85rem; font-weight: 600;">
                🚀 CareerPilot AI
            </span>
            <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); color: #34D399; padding: 0.35rem 0.85rem; border-radius: 9999px; font-size: 0.85rem; font-weight: 600;">
                ● Production Ready
            </span>
        </div>
        <h1 style="font-size: 2.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 1rem; background: linear-gradient(135deg, #FFFFFF 0%, #CBD5E1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Your Personal AI Career Mentor
        </h1>
        <p style="font-size: 1.1rem; color: #94A3B8; max-width: 800px; margin: 0 auto; line-height: 1.7;">
            A complete AI-powered platform that helps students and professionals analyze resumes, improve ATS compatibility, predict career paths, prepare for interviews, and accelerate career growth.
        </p>
    </div>
    """).strip()
    st.markdown(hero_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # SECTION 2: MISSION
    # ---------------------------------------------------------
    mission_html = textwrap.dedent("""
    <div class="glass-panel" style="padding: 2rem; border-left: 4px solid #6366F1;">
        <div style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #6366F1; margin-bottom: 0.5rem;">
            OUR MISSION
        </div>
        <h2 style="font-size: 1.6rem; margin-bottom: 1rem; color: #F8FAFC;">
            Bridging the Employability Gap Through Intelligent AI
        </h2>
        <p style="font-size: 1rem; color: #CBD5E1; line-height: 1.7; margin-bottom: 1rem;">
            CareerPilot AI is designed to bridge the gap between education and employability using Artificial Intelligence.
        </p>
        <p style="font-size: 1rem; color: #94A3B8; line-height: 1.7;">
            It combines resume analysis, career prediction, interview preparation, and personalized learning into one integrated platform.
        </p>
    </div>
    """).strip()
    st.markdown(mission_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # SECTION 3: PLATFORM FEATURES
    # ---------------------------------------------------------
    st.markdown("<h2 style='text-align: center; margin-bottom: 0.5rem;'>Platform Features</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; margin-bottom: 2rem;'>9 integrated intelligent modules driving career preparation and growth</p>", unsafe_allow_html=True)

    features = [
        ("📄", "Resume Intelligence", "Deep PDF text parsing, structural extraction, and section identification."),
        ("🎯", "ATS Score Analysis", "Keyword match scoring, vector similarity, and compatibility breakdown."),
        ("✨", "Resume Rewriter", "AI-powered bullet point enhancer and achievement quantifier."),
        ("🤖", "AI Role Prediction", "ML classification model for job role targeting and skill alignment."),
        ("💰", "Salary Prediction", "Data-backed regression modeling for earning potential estimation."),
        ("📚", "Learning Roadmap", "Customized week-by-week skill development paths and projects."),
        ("💼", "Interview Questions", "Tailored technical and behavioral question generation."),
        ("🎙", "Voice Interview", "Real-time speech-to-text voice mock interview simulator with feedback."),
        ("📊", "Career Analytics", "Comprehensive visualizations, skill distributions, and readiness tracking.")
    ]

    f_cols = st.columns(3)
    for idx, (icon, name, desc) in enumerate(features):
        with f_cols[idx % 3]:
            feat_html = textwrap.dedent(f"""
            <div class="glass-panel" style="min-height: 140px; display: flex; flex-direction: column; justify-content: flex-start;">
                <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.6rem;">
                    <span style="font-size: 1.5rem;">{icon}</span>
                    <span style="font-size: 1.05rem; font-weight: 700; color: #F8FAFC;">{name}</span>
                </div>
                <p style="font-size: 0.88rem; color: #94A3B8; line-height: 1.5; margin: 0;">
                    {desc}
                </p>
            </div>
            """).strip()
            st.markdown(feat_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # SECTION 4: TECHNOLOGY STACK
    # ---------------------------------------------------------
    st.markdown("<h2 style='text-align: center; margin-bottom: 0.5rem;'>Technology Stack</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; margin-bottom: 2rem;'>Powered by state-of-the-art machine learning libraries and AI models</p>", unsafe_allow_html=True)

    tech_categories = [
        ("🐍 Programming", ["Python"]),
        ("🖥 Frontend", ["Streamlit"]),
        ("🤖 Machine Learning", ["Scikit-learn", "Sentence Transformers"]),
        ("🔍 Vector Search", ["FAISS"]),
        ("🧠 AI Models", ["Groq LLM", "Groq Whisper"]),
        ("📊 Libraries", ["Pandas", "NumPy", "Matplotlib"]),
        ("🚀 Deployment", ["GitHub", "Streamlit Cloud"]),
    ]

    t_cols = st.columns(4)
    for idx, (cat_name, items) in enumerate(tech_categories):
        with t_cols[idx % 4]:
            items_badges = "".join([f'<span class="skill-chip" style="margin-top: 0.4rem;">• {item}</span>' for item in items])
            tech_html = textwrap.dedent(f"""
            <div class="glass-panel" style="min-height: 130px;">
                <div style="font-size: 0.95rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.75rem;">{cat_name}</div>
                <div style="display: flex; flex-wrap: wrap; gap: 0.3rem;">
                    {items_badges}
                </div>
            </div>
            """).strip()
            st.markdown(tech_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # SECTION 5: PLATFORM ARCHITECTURE
    # ---------------------------------------------------------
    st.markdown("<h2 style='text-align: center; margin-bottom: 0.5rem;'>Platform Architecture</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; margin-bottom: 2rem;'>End-to-end data flow and intelligence processing pipeline</p>", unsafe_allow_html=True)

    pipeline_steps = [
        ("Resume Upload", "PDF/Text Parsing"),
        ("Resume Intelligence", "Section & Skill Extraction"),
        ("ATS Analysis", "Match Scoring & Keyword Gap"),
        ("Role Prediction", "ML Career Targeting"),
        ("Salary Prediction", "Earning Estimation"),
        ("Learning Roadmap", "Custom Skill Path"),
        ("Interview Questions", "Targeted Q&A Generation"),
        ("Voice Interview", "Speech-to-Text Practice"),
        ("Career Analytics", "Readiness Summary")
    ]

    arch_html = '<div style="display: flex; flex-direction: column; align-items: center; gap: 0.5rem; max-width: 650px; margin: 0 auto;">'
    for step_idx, (title, sub) in enumerate(pipeline_steps):
        arch_html += textwrap.dedent(f"""
        <div class="glass-panel" style="width: 100%; padding: 0.85rem 1.25rem; margin-bottom: 0; display: flex; justify-content: space-between; align-items: center; border-left: 3px solid #06B6D4;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="background: rgba(6, 182, 212, 0.15); color: #06B6D4; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: 700;">{step_idx + 1}</span>
                <span style="font-weight: 700; color: #F8FAFC; font-size: 0.95rem;">{title}</span>
            </div>
            <span style="font-size: 0.82rem; color: #94A3B8;">{sub}</span>
        </div>
        """).strip()

        if step_idx < len(pipeline_steps) - 1:
            arch_html += '<div style="color: #6366F1; font-size: 1.2rem; font-weight: bold; line-height: 1;">↓</div>'
    arch_html += '</div>'

    st.markdown(arch_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # SECTION 6: DEVELOPMENT HIGHLIGHTS
    # ---------------------------------------------------------
    st.markdown("<h2 style='text-align: center; margin-bottom: 0.5rem;'>Development Highlights</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; margin-bottom: 2rem;'>Key metrics and technical capabilities built into CareerPilot AI</p>", unsafe_allow_html=True)

    kpis = [
        ("9", "Core Modules"),
        ("AI", "Powered Engine"),
        ("PDF", "Resume Parsing"),
        ("Voice", "Mock Interview"),
        ("90%+", "ATS Optimization"),
        ("Live", "Career Analytics"),
        ("ML", "Machine Learning"),
        ("STT", "Browser Voice Support")
    ]

    kpi_cols = st.columns(4)
    for idx, (stat, label) in enumerate(kpis):
        with kpi_cols[idx % 4]:
            kpi_html = textwrap.dedent(f"""
            <div class="glass-panel" style="text-align: center; padding: 1.25rem 0.75rem;">
                <div style="font-size: 1.75rem; font-weight: 800; color: #A5B4FC; margin-bottom: 0.25rem;">{stat}</div>
                <div style="font-size: 0.85rem; font-weight: 600; color: #94A3B8;">{label}</div>
            </div>
            """).strip()
            st.markdown(kpi_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # SECTION 7: DEVELOPER PROFILE
    # ---------------------------------------------------------
    st.markdown("<h2 style='text-align: center; margin-bottom: 1.5rem;'>Developer Profile</h2>", unsafe_allow_html=True)

    dev_card_html = textwrap.dedent("""
    <div class="glass-panel" style="padding: 2rem; max-width: 800px; margin: 0 auto; text-align: center; border-top: 3px solid #8B5CF6;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">👩‍💻</div>
        <div style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #8B5CF6; margin-bottom: 0.3rem;">
            DEVELOPED BY
        </div>
        <h2 style="font-size: 1.8rem; font-weight: 800; color: #F8FAFC; margin-bottom: 0.5rem;">
            Nandini Bhatt
        </h2>
        <div style="font-size: 1rem; font-weight: 600; color: #A5B4FC; margin-bottom: 0.75rem;">
            B.Tech Artificial Intelligence &amp; Machine Learning
        </div>
        <p style="font-size: 0.95rem; color: #94A3B8; max-width: 600px; margin: 0 auto; line-height: 1.6;">
            Passionate about AI, Machine Learning, NLP, and Career Technology.
        </p>
    </div>
    """).strip()
    st.markdown(dev_card_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # SECTION 8: FUTURE ROADMAP
    # ---------------------------------------------------------
    st.markdown("<h2 style='text-align: center; margin-bottom: 0.5rem;'>Future Roadmap</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; margin-bottom: 2rem;'>Upcoming planned features and ecosystem expansions</p>", unsafe_allow_html=True)

    roadmap_items = [
        ("✔ Live Job Recommendations", "Real-time live job market scraping and matching via Adzuna / LinkedIn API."),
        ("✔ AI Career Coach", "Conversational AI mentor for continuous career guidance and goal tracking."),
        ("✔ Company-wise Interview Preparation", "Targeted question banks customized for FAANG and top tech companies."),
        ("✔ Resume Version History", "Save, compare, and manage multiple customized resume variations."),
        ("✔ Recruiter Dashboard", "Talent sourcing portal for recruiters to discover candidate matches."),
        ("✔ Skill Gap Tracking", "Progress dashboard tracking skill acquisition over time."),
        ("✔ Multi-language Support", "Multi-lingual resume parsing and voice interview support.")
    ]

    for item_title, item_desc in roadmap_items:
        road_html = textwrap.dedent(f"""
        <div class="glass-panel" style="margin-bottom: 0.75rem; border-left: 3px solid #10B981; padding: 1rem 1.25rem;">
            <div style="font-size: 1rem; font-weight: 700; color: #34D399; margin-bottom: 0.25rem;">
                {item_title}
            </div>
            <div style="font-size: 0.85rem; color: #94A3B8;">
                {item_desc}
            </div>
        </div>
        """).strip()
        st.markdown(road_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # SECTION 9: FOOTER
    # ---------------------------------------------------------
    footer_html = textwrap.dedent("""
    <div style="text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 2rem; margin-top: 2rem;">
        <div style="font-size: 1.1rem; font-weight: 800; color: #F8FAFC; margin-bottom: 0.5rem;">
            CareerPilot AI
        </div>
        <p style="font-size: 0.88rem; color: #94A3B8; max-width: 600px; margin: 0 auto 1rem auto; line-height: 1.5;">
            Built using Python, Streamlit, Machine Learning, Groq AI, and modern NLP technologies.
        </p>
        <div style="color: #64748B; font-size: 0.8rem;">
            © 2026 CareerPilot AI
        </div>
    </div>
    """).strip()
    st.markdown(footer_html, unsafe_allow_html=True)
