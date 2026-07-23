import streamlit as st


def upload_section():
    st.markdown("""
    <style>
    .upload-header { font-size:20px; font-weight:800; color:#0F172A; margin-bottom:3px; }
    .upload-sub { font-size:14px; color:#94A3B8; margin-bottom:16px; }
    .col-label { font-size:14px; font-weight:700; color:#374151; margin-bottom:8px; display:block; }
    </style>
    <div class="upload-header">📂 Upload & Analyze</div>
    <div class="upload-sub">Upload your resume and paste the job description to get AI-powered insights</div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown('<span class="col-label">📄 Your Resume</span>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Upload your resume",
            type=["pdf"],
            label_visibility="collapsed",
            help="PDF format · Max 10MB"
        )
        if uploaded_file:
            st.success(f"✅ {uploaded_file.name} ready")

    with right:
        st.markdown('<span class="col-label">💼 Job Description</span>', unsafe_allow_html=True)
        job_description = st.text_area(
            "Job Description",
            height=170,
            placeholder="Paste the complete job description here...\n\nTip: Include skills, requirements and responsibilities for best results.",
            label_visibility="collapsed"
        )

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    analyze = st.button(
        "✨  Analyze Resume",
        use_container_width=True,
        type="primary"
    )

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    return uploaded_file, job_description, analyze