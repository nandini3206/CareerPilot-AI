import streamlit as st


def upload_section():
    st.markdown("""
    <style>
    .upload-header {
        font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 4px;
    }
    .upload-sub {
        font-size: 14px; color: #94A3B8; margin-bottom: 20px;
    }
    .upload-wrap {
        background: white; border: 1.5px solid #EDE9FE;
        border-radius: 16px; padding: 24px 24px 20px;
        box-shadow: 0 4px 16px rgba(91,33,182,0.07);
        margin-bottom: 20px;
    }
    .col-label {
        font-size: 14px; font-weight: 700; color: #374151; margin-bottom: 10px;
    }
    </style>

    <div class="upload-wrap">
        <div class="upload-header">📂 Upload & Analyze</div>
        <div class="upload-sub">Upload your resume and paste the job description to get AI-powered insights</div>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown('<div class="col-label">📄 Your Resume</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Upload",
            type=["pdf"],
            label_visibility="collapsed",
            help="PDF format · Max 10MB"
        )
        if uploaded_file:
            st.success(f"✅ {uploaded_file.name} ready")
        else:
            st.markdown("""
            <div style="font-size:12px;color:#94A3B8;padding:4px 0;">
                📌 Supports PDF · Max 10MB
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="col-label">💼 Job Description</div>', unsafe_allow_html=True)
        job_description = st.text_area(
            "JD",
            height=170,
            placeholder="Paste the complete job description here...\n\nTip: Include skills, requirements and responsibilities for the best results.",
            label_visibility="collapsed"
        )

    st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

    analyze = st.button(
        "✨  Analyze Resume",
        use_container_width=True,
        type="primary"
    )

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    return uploaded_file, job_description, analyze