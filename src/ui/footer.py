import streamlit as st

def show_footer():
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    st.markdown("""
    <hr style="border:none;border-top:1px solid #e5e7eb;margin-bottom:12px;">
    <div style="text-align:center;font-size:12px;color:#9ca3af;padding-bottom:16px;">
        Made with ❤️ by <strong>Nandini Bhatt</strong> · CareerPilot AI v1.0
    </div>
    """, unsafe_allow_html=True)