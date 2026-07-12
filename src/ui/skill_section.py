import streamlit as st


def show_skill_section(skill_result):
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:15px;font-weight:700;color:#111827;margin-bottom:12px;">🛠 Skill Analysis</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div style="font-size:13px;font-weight:600;color:#111827;margin-bottom:8px;">✅ Matching Skills</div>', unsafe_allow_html=True)
        if skill_result["matching"]:
            chips = "".join(f'<span class="chip chip-green">{s}</span>' for s in skill_result["matching"])
            st.markdown(f'<div style="display:flex;flex-wrap:wrap;gap:4px;">{chips}</div>', unsafe_allow_html=True)
        else:
            st.info("No matching skills found.")

    with col2:
        st.markdown('<div style="font-size:13px;font-weight:600;color:#111827;margin-bottom:8px;">❌ Missing Skills</div>', unsafe_allow_html=True)
        if skill_result["missing"]:
            chips = "".join(f'<span class="chip chip-red">{s}</span>' for s in skill_result["missing"])
            st.markdown(f'<div style="display:flex;flex-wrap:wrap;gap:4px;">{chips}</div>', unsafe_allow_html=True)
        else:
            st.success("No missing skills! 🎉")