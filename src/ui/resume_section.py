import streamlit as st


def show_resume_section(sections, skills):
    st.markdown("""
    <div style="font-size:15px;font-weight:700;color:#111827;margin-bottom:14px;">📄 Resume Analysis</div>
    """, unsafe_allow_html=True)

    with st.expander("📑 Parsed Resume Sections", expanded=True):
        for section, content in sections.items():
            st.markdown(f"### {section.title()}")
            if content.strip():
                st.write(content)
            else:
                st.info("Not Found")

    with st.expander("🎯 Detected Skills"):
        if skills:
            chips = "".join(f'<span class="chip chip-green">{s}</span>' for s in skills)
            st.markdown(f'<div style="display:flex;flex-wrap:wrap;gap:4px;padding:8px 0">{chips}</div>', unsafe_allow_html=True)
        else:
            st.warning("No skills detected.")