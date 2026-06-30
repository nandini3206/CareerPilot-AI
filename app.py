import streamlit as st
from src.parsers.resume_parser import (
    extract_text,
    extract_sections
)
from src.ml.skill_extractor import extract_skills

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")
st.subheader("AI Career Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = extract_text("temp_resume.pdf")
    sections = extract_sections(resume_text)
    skills = extract_skills(resume_text)

    st.success("Resume Parsed Successfully!")

    st.subheader("📄 Parsed Resume Sections")

for section, content in sections.items():

    st.markdown(f"## {section.title()}")

    if content.strip():
        st.write(content)
    else:
        st.info("Not Found")

st.divider()

st.subheader("🎯 Detected Skills")

if skills:

    st.success(f"{len(skills)} skills detected")

    st.write(skills)

else:

    st.warning("No skills detected.")