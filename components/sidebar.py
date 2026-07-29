import base64
import os
import textwrap
import streamlit as st

def get_svg_logo_html(width=32, height=32):
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


def render_sidebar():
    """
    Renders the modern, dark-themed compact hierarchical sidebar navigation
    inspired by Notion, Linear, Cursor, and VS Code Explorer.
    Collapsed by default, tight vertical list with 14px child indentation.
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

    with st.sidebar:
        # Header / Brand Identity (SVG Logo enlarged ~30% to 32px)
        logo_img = get_svg_logo_html(width=32, height=32)
        header_html = textwrap.dedent(f"""
        <div class="sidebar-header">
            <div class="brand-mark">
                {logo_img}
                <span>CareerPilot AI</span>
            </div>
        </div>
        """).strip()
        st.markdown(header_html, unsafe_allow_html=True)

        # Candidate Profile / Resume Status Banner
        resume_uploaded = st.session_state.get("resume_uploaded", False)
        file_name = st.session_state.get("resume_file_name", "")

        if resume_uploaded:
            status_html = textwrap.dedent(f"""
            <div class="resume-status-badge status-loaded">
                <span>✓</span> <b>Active:</b> {file_name[:14]}...
            </div>
            """).strip()
        else:
            status_html = textwrap.dedent("""
            <div class="resume-status-badge status-missing">
                <span>⚠️</span> <b>No Resume Loaded</b>
            </div>
            """).strip()
            
        st.markdown(status_html, unsafe_allow_html=True)
        st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)

        curr = st.session_state.current_page

        # 🏠 Home
        is_home_active = curr == "Home"
        if st.button("🏠  Home", key="nav_home", type="primary" if is_home_active else "secondary"):
            st.session_state.current_page = "Home"
            st.rerun()

        # Helper Renderer for Studios & Children (Compact IDE Tree Style)
        def render_studio_group(studio_name, icon, children_dict):
            is_expanded = st.session_state.expanded_studios.get(studio_name, False)
            arrow = "▼" if is_expanded else "▶"
            
            studio_label = f"{arrow} {icon} {studio_name}"
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
        if st.button("📊  Career Analytics", key="nav_analytics", type="primary" if is_analytics_active else "secondary"):
            st.session_state.current_page = "Analytics"
            st.rerun()

        # ℹ️ About
        is_about_active = curr == "About"
        if st.button("ℹ️  About Platform", key="nav_about", type="primary" if is_about_active else "secondary"):
            st.session_state.current_page = "About"
            st.rerun()

        # Reset Session Footer Button
        st.markdown("<div style='margin-top: 1.25rem;'></div>", unsafe_allow_html=True)
        if st.button("🔄 Reset Session State", key="btn_reset_session"):
            if "resume_uploaded" in st.session_state:
                del st.session_state["resume_uploaded"]
            st.session_state.current_page = "Home"
            st.rerun()
