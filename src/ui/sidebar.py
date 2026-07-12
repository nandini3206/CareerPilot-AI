import streamlit as st


def show_sidebar():
    with st.sidebar:
        st.markdown("""
        <style>
        [data-testid="stSidebarNav"] { display: none !important; }

        .sb-logo {
            display: flex; align-items: center; gap: 12px;
            padding: 8px 4px 16px; margin-bottom: 8px;
            border-bottom: 2px solid #EDE9FE;
        }
        .sb-logo-title {
            font-size: 17px; font-weight: 900; color: #0F172A;
            letter-spacing: -0.3px;
        }
        .sb-logo-sub { font-size: 11px; color: #94A3B8; margin-top: 1px; }

        .sb-nav-item {
            display: flex; align-items: center; gap: 10px;
            padding: 11px 14px; border-radius: 10px;
            font-size: 14px; color: #64748B; font-weight: 500;
            margin-bottom: 2px; cursor: pointer;
            transition: all 0.18s ease;
        }
        .sb-nav-item:hover { background: #F5F3FF; color: #5B21B6; }
        .sb-nav-item.active {
            background: linear-gradient(135deg, #EDE9FE, #F5F3FF);
            color: #5B21B6; font-weight: 700;
            border-left: 3px solid #5B21B6;
        }

        .sb-section {
            font-size: 10px; color: #94A3B8; padding: 10px 14px 4px;
            letter-spacing: .1em; text-transform: uppercase; font-weight: 800;
        }
        .sb-divider { height: 1.5px; background: #EDE9FE; margin: 10px 4px; }

        .sb-pro-card {
            background: linear-gradient(135deg, #F5F3FF, #EDE9FE);
            border: 1.5px solid #C4B5FD; border-radius: 14px;
            padding: 14px 14px 12px; margin: 8px 0;
        }
        .sb-pro-title {
            font-size: 14px; font-weight: 800; color: #5B21B6; margin-bottom: 5px;
        }
        .sb-pro-desc {
            font-size: 12px; color: #6B7280; line-height: 1.6; margin-bottom: 2px;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sb-logo">
            <span style="font-size:30px">🚀</span>
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
            cls = "sb-nav-item active" if active else "sb-nav-item"
            st.markdown(f'<div class="{cls}">{icon}&nbsp;&nbsp;{page}</div>', unsafe_allow_html=True)
            if st.button(page, key=f"nav_{page}", use_container_width=True):
                st.session_state["active_page"] = page
                st.rerun()

        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="sb-section">Quick Actions</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="small")
        with c1:
            st.markdown('<div class="sb-nav-item" style="font-size:13px;">➕&nbsp;New</div>', unsafe_allow_html=True)
            if st.button("New", key="new_btn", use_container_width=True):
                for k in list(st.session_state.keys()):
                    if k != "active_page":
                        del st.session_state[k]
                st.session_state["active_page"] = "Dashboard"
                st.rerun()
        with c2:
            st.markdown('<div class="sb-nav-item" style="font-size:13px;">📥&nbsp;Export</div>', unsafe_allow_html=True)
            st.button("Export", key="exp_btn", use_container_width=True)

        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

        dark_mode = st.toggle("🌙 Dark Mode", value=False)

        st.markdown("""
        <div class="sb-pro-card">
            <div class="sb-pro-title">👑 CareerPilot Pro</div>
            <div class="sb-pro-desc">Multiple resume comparison, batch analysis and advanced AI insights.</div>
        </div>
        """, unsafe_allow_html=True)

        st.button("⚡ Upgrade to Pro", use_container_width=True, type="primary", key="upg_btn")

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        st.caption("v1.0 · Built with ❤️ by Nandini Bhatt")

    return dark_mode