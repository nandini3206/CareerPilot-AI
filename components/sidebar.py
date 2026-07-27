import streamlit as st


MENU_ITEMS = [
    ("🏠", "Home"),
    ("📄", "Resume Analysis"),
    ("🎯", "ATS Score"),
    ("🤖", "Resume Feedback"),
    ("💼", "Role Prediction"),
    ("💰", "Salary Prediction"),
    ("🧭", "Career Recommendation"),
    ("📚", "Learning Roadmap"),
    ("📄", "Cover Letter"),
    ("❓", "Interview Questions"),
    ("🎤", "Voice Interview"),
    ("📊", "Analytics"),
    ("🕘", "Resume History"),
    ("ℹ️", "About"),
]


def sidebar():

    with st.sidebar:

        st.markdown(
            '<div style="text-align:center; padding-top:10px;">'
            '<h2 style="color:#38BDF8;margin-bottom:0;">🚀 CareerPilot AI</h2>'
            '<p style="color:#94A3B8;font-size:14px;">Your Personal AI Career Mentor</p>'
            '</div>',
            unsafe_allow_html=True,
        )

        st.divider()

        if "page" not in st.session_state:
            st.session_state.page = "Home"

        for icon, page in MENU_ITEMS:

            if st.button(
                f"{icon}  {page}",
                use_container_width=True,
                key=f"menu_{page}",
            ):
                st.session_state.page = page
                st.rerun()

        st.divider()

        st.markdown(
            """
            <div style="text-align:center">

            <p style="color:#94A3B8;font-size:13px;">
            Developed by
            </p>

            <h4 style="color:white;margin-top:-8px;">
            Nandini Bhatt
            </h4>

            </div>
            """,
            unsafe_allow_html=True,
        )