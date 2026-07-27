import streamlit as st

# ==========================================
# MENU ITEMS
# ==========================================

MENU_ITEMS = [
    ("🏠", "Home"),

    ("📄", "Resume Analysis"),
    ("🎯", "ATS Score"),
    ("💬", "Resume Feedback"),
    ("✍️", "Resume Rewriter"),

    ("🎯", "Role Prediction"),
    ("💰", "Salary Prediction"),
    ("💼", "Job Recommendations"),

    ("📚", "Learning Roadmap"),
    ("📝", "Cover Letter"),
    ("❓", "Interview Questions"),
    ("🎤", "Voice Interview"),

    ("📊", "Analytics"),

    ("ℹ️", "About"),
]


# ==========================================
# SECTION HEADING
# ==========================================

def section_heading(title):
    st.markdown(
        f"""
        <div style="
            color:#38BDF8;
            font-size:14px;
            font-weight:700;
            letter-spacing:1px;
            margin-top:8px;
            margin-bottom:8px;
            text-transform:uppercase;">
            {title}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================
# SIDEBAR
# ==========================================

def sidebar():

    with st.sidebar:

        # ------------------------------
        # Logo
        # ------------------------------

        st.markdown(
            """
            <div style="text-align:center;padding-top:5px;">

                <h2 style="color:#38BDF8;margin-bottom:0;">
                    🚀 CareerPilot AI
                </h2>

                <p style="
                    color:#CBD5E1;
                    font-size:14px;
                    margin-top:6px;
                    margin-bottom:8px;">
                    Analyze • Improve • Prepare • Get Hired
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        if "page" not in st.session_state:
            st.session_state.page = "Home"

        # ------------------------------
        # HOME
        # ------------------------------

        icon, page = MENU_ITEMS[0]

        if st.button(
            f"{icon}  {page}",
            use_container_width=True,
            key="Home",
        ):
            st.session_state.page = page
            st.rerun()

        st.divider()

        # ------------------------------
        # Resume Intelligence
        # ------------------------------

        section_heading("Resume Intelligence")

        for icon, page in MENU_ITEMS[1:5]:

            if st.button(
                f"{icon}  {page}",
                use_container_width=True,
                key=page,
            ):
                st.session_state.page = page
                st.rerun()

        st.divider()

        # ------------------------------
        # Career Insights
        # ------------------------------

        section_heading("Career Insights")

        for icon, page in MENU_ITEMS[5:8]:

            if st.button(
                f"{icon}  {page}",
                use_container_width=True,
                key=page,
            ):
                st.session_state.page = page
                st.rerun()

        st.divider()

        # ------------------------------
        # Career Preparation
        # ------------------------------

        section_heading("Career Preparation")

        for icon, page in MENU_ITEMS[8:12]:

            if st.button(
                f"{icon}  {page}",
                use_container_width=True,
                key=page,
            ):
                st.session_state.page = page
                st.rerun()

        st.divider()

        # ------------------------------
        # Dashboard
        # ------------------------------

        section_heading("Dashboard")

        icon, page = MENU_ITEMS[12]

        if st.button(
            f"{icon}  {page}",
            use_container_width=True,
            key=page,
        ):
            st.session_state.page = page
            st.rerun()

        st.divider()

        # ------------------------------
        # About
        # ------------------------------

        icon, page = MENU_ITEMS[13]

        if st.button(
            f"{icon}  {page}",
            use_container_width=True,
            key=page,
        ):
            st.session_state.page = page
            st.rerun()

        st.divider()

        # ------------------------------
        # Footer
        # ------------------------------

        st.markdown(
            """
            <div style="text-align:center;padding-top:10px;">

            <p style="
                color:#94A3B8;
                font-size:12px;
                margin-bottom:4px;">
                Developed by
            </p>

            <h4 style="
                color:white;
                margin-top:0;
                margin-bottom:0;">
                Nandini Bhatt
            </h4>

            <p style="
                color:#64748B;
                font-size:11px;">
                CareerPilot AI v2
            </p>

            </div>
            """,
            unsafe_allow_html=True,
        )