import streamlit as st


def show_ai_sections(ai_feedback, interview_questions, learning_roadmap):
    st.markdown("""
    <div style="font-size:15px;font-weight:700;color:#111827;margin-bottom:14px;">🤖 AI Insights</div>
    """, unsafe_allow_html=True)

    with st.expander("📝 AI Resume Feedback", expanded=True):
        st.markdown(ai_feedback)

    with st.expander("🎤 Interview Questions"):
        st.caption("Top questions likely to be asked based on your resume and JD.")
        lines = [l.strip() for l in interview_questions.split("\n") if l.strip()]
        for line in lines:
            st.markdown(line)

    with st.expander("📚 Personalized Learning Roadmap"):
        st.caption("Priority skills to learn based on your skill gaps.")
        sections = learning_roadmap.split("Priority")
        for chunk in sections:
            chunk = chunk.strip()
            if not chunk:
                continue
            lines = chunk.split("\n")
            title = f"Priority {lines[0].strip()}"
            body = "\n".join(lines[1:]).strip()
            st.markdown(f"**🔹 {title}**")
            st.caption(body[:300] + ("..." if len(body) > 300 else ""))
            st.markdown("")