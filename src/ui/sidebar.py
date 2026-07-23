import streamlit as st


def show_sidebar():
    with st.sidebar:

        st.markdown("""
        <style>
        [data-testid="stSidebarNav"] { display: none !important; }

        /* ── Hide buttons, keep clickable ── */
        section[data-testid="stSidebar"] .stButton { margin: 0 !important; padding: 0 !important; }
        section[data-testid="stSidebar"] .stButton > button {
            opacity: 0 !important;
            height: 44px !important;
            margin-top: -46px !important;
            width: 100% !important;
            position: relative !important;
            z-index: 999 !important;
            cursor: pointer !important;
            border: none !important;
            background: transparent !important;
            box-shadow: none !important;
            padding: 0 !important;
            min-height: 0 !important;
        }
        section[data-testid="stSidebar"] .stButton > button:hover {
            background: transparent !important;
            border: none !important;
        }

        /* ── Logo ── */
        .sb-logo {
            display:flex; align-items:center; gap:12px;
            padding: 6px 4px 14px;
            border-bottom: 2px solid #EDE9FE; margin-bottom: 10px;
        }
        .sb-logo-title { font-size:16px; font-weight:900; color:#0F172A; letter-spacing:-0.3px; }
        .sb-logo-sub   { font-size:11px; color:#94A3B8; margin-top:1px; }

        /* ── Nav items ── */
        .sb-nav {
            display:flex; align-items:center; gap:10px;
            padding: 11px 14px; border-radius: 10px;
            font-size: 14px; color: #64748B; font-weight: 500;
            margin-bottom: 2px;
        }
        .sb-nav.active {
            background: linear-gradient(135deg,#EDE9FE,#F5F3FF);
            color: #5B21B6 !important; font-weight: 700;
            border-left: 3px solid #5B21B6;
        }

        /* ── Misc ── */
        .sb-sect { font-size:10px; color:#94A3B8; padding:8px 14px 4px; letter-spacing:.1em; text-transform:uppercase; font-weight:800; }
        .sb-div  { height:1.5px; background:#EDE9FE; margin:10px 4px; }
        .sb-qa   { display:flex; align-items:center; gap:8px; padding:9px 14px; border-radius:8px; font-size:13px; color:#64748B; font-weight:500; margin-bottom:2px; }
        .sb-pro  {
            background:linear-gradient(135deg,#F5F3FF,#EDE9FE);
            border:1.5px solid #C4B5FD; border-radius:14px;
            padding:14px; margin:8px 0;
        }
        .sb-pro-t { font-size:14px; font-weight:800; color:#5B21B6; margin-bottom:5px; }
        .sb-pro-d { font-size:12px; color:#6B7280; line-height:1.6; }
        </style>
        """, unsafe_allow_html=True)

        # Logo
        st.markdown("""
        <div class="sb-logo">
            <span style="font-size:28px">🚀</span>
            <div>
                <div class="sb-logo-title">CareerPilot AI</div>
                <div class="sb-logo-sub">Your AI career mentor</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if "active_page" not in st.session_state:
            st.session_state["active_page"] = "Dashboard"

        pages = [
            ("🏠", "Dashboard"),
            ("🤖", "AI Insights"),
            ("📄", "Resume Analysis"),
            ("🗺️", "Learning Roadmap"),
            ("✉️", "Cover Letter"),
        ]

        for icon, page in pages:
            active = st.session_state["active_page"] == page
            cls = "sb-nav active" if active else "sb-nav"
            # Nav item HTML
            st.markdown(f'<div class="{cls}">{icon}&nbsp;&nbsp;{page}</div>', unsafe_allow_html=True)
            # Invisible button directly after (margin:0 so it sits on top)
            if st.button(f"{page}", key=f"nav_{page}", use_container_width=True, label_visibility="collapsed" if False else "visible"):
                st.session_state["active_page"] = page
                st.rerun()

        st.markdown('<div class="sb-div"></div>', unsafe_allow_html=True)
        st.markdown('<div class="sb-sect">Quick Actions</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="small")
        with c1:
            st.markdown('<div class="sb-qa">➕&nbsp;New</div>', unsafe_allow_html=True)
            if st.button("New Analysis", key="new_btn", use_container_width=True):
                keys = [k for k in list(st.session_state.keys()) if k != "active_page"]
                for k in keys:
                    del st.session_state[k]
                st.session_state["active_page"] = "Dashboard"
                st.rerun()
        with c2:
            st.markdown('<div class="sb-qa">📥&nbsp;Export</div>', unsafe_allow_html=True)
            st.button("Export", key="exp_btn", use_container_width=True)

        st.markdown('<div class="sb-div"></div>', unsafe_allow_html=True)

        dark_mode = st.toggle("🌙 Dark Mode", value=False)

        st.markdown("""
        <div class="sb-pro">
            <div class="sb-pro-t">👑 CareerPilot Pro</div>
            <div class="sb-pro-d">Multiple resume comparison and advanced AI insights.</div>
        </div>
        """, unsafe_allow_html=True)

        st.button("⚡ Upgrade to Pro", use_container_width=True, type="primary", key="upg_btn")

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
        st.caption("v1.0 · Built with ❤️ by Nandini Bhatt")

    return dark_mode