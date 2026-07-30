import base64
import os
import streamlit as st

def get_svg_logo_html(width=36, height=36):
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
    never misinterprets 4+ space indented HTML lines as Markdown code blocks.
    """
    return "\n".join(line.strip() for line in html_str.splitlines() if line.strip())

def render_sidebar():
    """
    Renders the Enterprise SaaS AI Sidebar Navigation for CareerPilot AI.
    Inspired by Microsoft Copilot, Notion AI, Cursor, Linear, and Vercel Dashboard.
    
    Features:
    1. Premium Brand Header (Circular glowing logo, Title, Subtitle, Version 2.0 Badge)
    2. Dynamic Resume Status Card (Active Skills & ATS Ready indicators)
    3. AI System Status Readiness Breakdown
    4. Hierarchical Studio Groups & Child Navigation
    5. Enterprise Footer (AI Stack, Designer Credits, Version Tag)
    """
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

    if "expanded_studios" not in st.session_state:
        st.session_state.expanded_studios = {
            "Resume Studio": False,
            "Career Intelligence": False,
            "Learning Studio": False,
            "Interview Lab": False,
        }

    resume_uploaded = st.session_state.get("resume_uploaded", False)
    file_name = st.session_state.get("resume_file_name", "Uploaded Resume")
    resume_skills = st.session_state.get("resume_skills", []) or st.session_state.get("extracted_skills", [])

    with st.sidebar:
        # =========================================================
        # 1. SIDEBAR BRAND HEADER
        # =========================================================
        logo_img = get_svg_logo_html(width=36, height=36)
        header_html = clean_html(f"""
<div class="sidebar-header" style="padding: 1rem 0.5rem 0.85rem 0.5rem; border-bottom: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 0.85rem;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.25rem;">
<div style="display: flex; align-items: center; gap: 0.75rem;">
<div style="position: relative; display: inline-block;">
<div style="position: absolute; inset: -4px; background: radial-gradient(circle, rgba(99, 102, 241, 0.6) 0%, transparent 70%); border-radius: 50%; filter: blur(6px);"></div>
<div style="position: relative;">{logo_img}</div>
</div>
<div>
<div style="font-size: 1.15rem; font-weight: 800; color: #F8FAFC; letter-spacing: -0.02em; line-height: 1.1;">CareerPilot AI</div>
<div style="font-size: 0.72rem; font-weight: 600; color: #94A3B8;">AI Career Platform</div>
</div>
</div>
<span style="background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3); color: #A5B4FC; padding: 0.15rem 0.45rem; border-radius: 9999px; font-size: 0.68rem; font-weight: 700;">
v2.0
</span>
</div>
</div>
""")
        st.markdown(header_html, unsafe_allow_html=True)

        # =========================================================
        # 2. RESUME STATUS CARD
        # =========================================================
        if resume_uploaded:
            status_card_html = clean_html(f"""
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 10px; padding: 0.65rem 0.75rem; margin-bottom: 0.85rem;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.25rem;">
<div style="font-size: 0.78rem; font-weight: 700; color: #34D399; display: flex; align-items: center; gap: 0.35rem;">
<span style="width: 7px; height: 7px; background: #34D399; border-radius: 50%; display: inline-block; box-shadow: 0 0 8px #34D399;"></span>
Resume Loaded
</div>
<span style="font-size: 0.68rem; background: rgba(16, 185, 129, 0.2); color: #34D399; padding: 0.1rem 0.4rem; border-radius: 4px; font-weight: 700;">ATS Ready</span>
</div>
<div style="font-size: 0.76rem; color: #CBD5E1; font-weight: 500; text-overflow: ellipsis; overflow: hidden; whitespace: nowrap;">
📄 {file_name[:20]}
</div>
<div style="font-size: 0.7rem; color: #94A3B8; margin-top: 0.2rem;">
⚡ {len(resume_skills)} Extracted Skills
</div>
</div>
""")
        else:
            status_card_html = clean_html("""
<div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.22); border-radius: 10px; padding: 0.65rem 0.75rem; margin-bottom: 0.85rem;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.2rem;">
<div style="font-size: 0.78rem; font-weight: 700; color: #FBBF24; display: flex; align-items: center; gap: 0.35rem;">
<span style="width: 7px; height: 7px; background: #FBBF24; border-radius: 50%; display: inline-block;"></span>
No Resume Loaded
</div>
</div>
<div style="font-size: 0.72rem; color: #94A3B8; line-height: 1.3;">
Upload resume in <b>Resume Studio</b> to unlock AI features.
</div>
</div>
""")
        st.markdown(status_card_html, unsafe_allow_html=True)

        # =========================================================
        # 3. DYNAMIC AI READINESS PANEL
        # =========================================================
        st_res = "Loaded" if resume_uploaded else "Not Loaded"
        st_res_clr = "#34D399" if resume_uploaded else "#FBBF24"
        
        st_ats = "Ready" if resume_uploaded else "Waiting"
        st_ats_clr = "#34D399" if resume_uploaded else "#64748B"
        
        st_intel = "Ready" if resume_uploaded else "Waiting"
        st_intel_clr = "#34D399" if resume_uploaded else "#64748B"
        
        st_inter = "Ready" if resume_uploaded else "Locked"
        st_inter_clr = "#34D399" if resume_uploaded else "#64748B"

        ai_status_html = clean_html(f"""
<div style="background: rgba(17, 24, 39, 0.6); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 0.5rem 0.65rem; margin-bottom: 1rem;">
<div style="font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #64748B; margin-bottom: 0.4rem;">
AI SYSTEM STATUS
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.35rem; font-size: 0.7rem;">
<div><span style="color: #94A3B8;">Resume:</span> <b style="color: {st_res_clr};">{st_res}</b></div>
<div><span style="color: #94A3B8;">ATS:</span> <b style="color: {st_ats_clr};">{st_ats}</b></div>
<div><span style="color: #94A3B8;">Intel:</span> <b style="color: {st_intel_clr};">{st_intel}</b></div>
<div><span style="color: #94A3B8;">Interview:</span> <b style="color: {st_inter_clr};">{st_inter}</b></div>
</div>
</div>
""")
        st.markdown(ai_status_html, unsafe_allow_html=True)

        curr = st.session_state.current_page

        # =========================================================
        # 4. NAVIGATION LIST
        # =========================================================
        st.markdown("<div style='font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #64748B; margin-bottom: 0.4rem; padding-left: 0.2rem;'>NAVIGATION</div>", unsafe_allow_html=True)

        # 🏠 Home
        is_home_active = curr == "Home"
        if st.button("🏠 Home", key="nav_home", type="primary" if is_home_active else "secondary"):
            st.session_state.current_page = "Home"
            st.rerun()

        # Helper Renderer for Studios & Children (Enterprise Tree Style)
        def render_studio_group(studio_name, icon, children_dict):
            is_expanded = st.session_state.expanded_studios.get(studio_name, False)
            arrow = "▼" if is_expanded else "▶"
            
            studio_label = f"{icon} {studio_name}"
            if st.button(studio_label, key=f"studio_toggle_{studio_name}"):
                st.session_state.expanded_studios[studio_name] = not is_expanded
                st.rerun()

            if is_expanded:
                st.markdown('<div class="nav-child-wrapper">', unsafe_allow_html=True)
                for child_label, page_key in children_dict.items():
                    is_active = curr == page_key
                    nav_label = child_label
                    
                    if st.button(nav_label, key=f"child_nav_{page_key}", type="primary" if is_active else "secondary"):
                        st.session_state.current_page = page_key
                        st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

        # 📄 Resume Studio
        render_studio_group(
            "Resume Studio",
            "📄",
            {
                "Resume Analysis": "Resume Analysis",
                "ATS Score": "ATS Score",
                "Resume Feedback": "Resume Feedback",
                "Resume Rewriter": "Resume Rewriter",
            },
        )

        # 🎯 Career Intelligence
        render_studio_group(
            "Career Intelligence",
            "🎯",
            {
                "Role Prediction": "Role Prediction",
                "Salary Prediction": "Salary Prediction",
                "Job Recommendations": "Job Recommendations",
            },
        )

        # 🎓 Learning Studio
        render_studio_group(
            "Learning Studio",
            "🎓",
            {
                "Learning Roadmap": "Learning Roadmap",
            },
        )

        # 🎤 Interview Lab
        render_studio_group(
            "Interview Lab",
            "🎤",
            {
                "Interview Questions": "Interview Questions",
                "Voice Interview": "Voice Interview",
            },
        )

        # 📊 Career Analytics
        is_analytics_active = curr == "Analytics"
        if st.button("📊 Career Analytics", key="nav_analytics", type="primary" if is_analytics_active else "secondary"):
            st.session_state.current_page = "Analytics"
            st.rerun()

        # ℹ️ About
        is_about_active = curr == "About"
        if st.button("ℹ️ About Platform", key="nav_about", type="primary" if is_about_active else "secondary"):
            st.session_state.current_page = "About"
            st.rerun()

        # Reset Session Footer Button
        st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
        if st.button("🔄 Reset Session State", key="btn_reset_session"):
            if "resume_uploaded" in st.session_state:
                del st.session_state["resume_uploaded"]
            st.session_state.current_page = "Home"
            st.rerun()

        # =========================================================
        # 5. SIDEBAR ENTERPRISE FOOTER
        # =========================================================
        footer_sidebar_html = clean_html("""
<div style="margin-top: 1.5rem; padding-top: 0.85rem; border-top: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.72rem; color: #64748B;">
<div style="font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.35rem; color: #94A3B8;">
POWERED BY MODERN AI
</div>
<div style="color: #64748B; line-height: 1.4; margin-bottom: 0.65rem;">
Sentence Transformers • Groq LLaMA-3 • Whisper • PyTorch
</div>
<div style="display: flex; justify-content: space-between; align-items: center; color: #94A3B8; font-weight: 500;">
<span>By <b>Nandini Bhatt</b></span>
<span style="font-size: 0.68rem; color: #64748B;">v2.0</span>
</div>
</div>
""")
        st.markdown(footer_sidebar_html, unsafe_allow_html=True)
