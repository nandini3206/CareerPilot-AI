import os
import tempfile
import streamlit as st

from src.parsers.resume_parser import (
    extract_text,
    extract_sections
)

from src.ml.skill_extractor import extract_skills


# ==========================================================
# Initialize Session State
# ==========================================================

def initialize_session():

    defaults = {

        "resume_uploaded": False,
        "job_uploaded": False,

        "resume_text": "",
        "resume_sections": {},
        "resume_skills": [],

        "job_description": "",

        "resume_file_name": "",
        "job_file_name": "",

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


# ==========================================================
# Process Resume
# ==========================================================

def process_resume(uploaded_resume):

    if uploaded_resume is None:
        return

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_resume.getvalue())

        pdf_path = tmp.name

    try:

        resume_text = extract_text(pdf_path)

        sections = extract_sections(resume_text)

        skills = extract_skills(resume_text)

        st.session_state.resume_uploaded = True

        st.session_state.resume_text = resume_text

        st.session_state.resume_sections = sections

        st.session_state.resume_skills = skills

        st.session_state.resume_file_name = uploaded_resume.name

    finally:

        if os.path.exists(pdf_path):

            os.remove(pdf_path)


# ==========================================================
# Process Job Description
# ==========================================================

def process_job_description(uploaded_jd):

    if uploaded_jd is None:

        return

    jd_text = uploaded_jd.read().decode("utf-8")

    st.session_state.job_uploaded = True

    st.session_state.job_description = jd_text

    st.session_state.job_file_name = uploaded_jd.name


# ==========================================================
# Reset Everything
# ==========================================================

def clear_session():

    keys = [

        "resume_uploaded",
        "job_uploaded",

        "resume_text",
        "resume_sections",
        "resume_skills",

        "job_description",

        "resume_file_name",
        "job_file_name",

    ]

    for key in keys:

        if key in st.session_state:

            del st.session_state[key]

    initialize_session()