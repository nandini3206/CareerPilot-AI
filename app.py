import streamlit as st

from src.parsers.resume_parser import extract_text, extract_sections
from src.ml.skill_extractor import extract_skills
from src.ml.ats_scorer import calculate_ats_score
from src.ml.skill_matcher import compare_skills
from src.ml.careerpilot_score import calculate_careerpilot_score
from src.ml.resume_quality import calculate_resume_quality
from src.llms.resume_feedback import generate_resume_feedback
from src.llms.interview_questions import generate_interview_questions
from src.llms.learning_roadmap import generate_learning_roadmap
from src.llms.cover_letter import generate_cover_letter

from src.ui.page_config import setup_page
from src.ui.sidebar import show_sidebar
from src.ui.theme import apply_theme
from src.ui.hero import show_hero
from src.ui.inputs import upload_section
from src.ui.metrics import show_metrics
from src.ui.skill_section import show_skill_section
from src.ui.ai_sections import show_ai_sections
from src.ui.resume_section import show_resume_section
from src.ui.footer import show_footer

setup_page()
dark_mode = show_sidebar()
apply_theme(dark_mode)

active_page = st.session_state.get("active_page", "Dashboard")

st.markdown('<div style="padding:28px 36px 0 36px;">', unsafe_allow_html=True)

# ==================================================
# DASHBOARD — hero + upload + results
# ==================================================
if active_page == "Dashboard":

    show_hero()

    uploaded_file, job_description, analyze = upload_section()

    if uploaded_file is not None and analyze:

        progress = st.progress(0)
        status   = st.empty()

        status.info("📄 Uploading Resume..."); progress.progress(5)
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        status.info("📖 Reading Resume..."); progress.progress(15)
        resume_text = extract_text("temp_resume.pdf")

        status.info("📑 Extracting Sections..."); progress.progress(25)
        sections = extract_sections(resume_text)

        status.info("🎯 Detecting Skills..."); progress.progress(35)
        skills = extract_skills(resume_text)

        status.info("📄 Evaluating Resume..."); progress.progress(45)
        resume_quality = calculate_resume_quality(sections, resume_text)

        if job_description.strip():

            status.info("🎯 Calculating ATS..."); progress.progress(50)
            ats_score = calculate_ats_score(resume_text, job_description)

            status.info("💻 Comparing Skills..."); progress.progress(60)
            skill_result = compare_skills(resume_text, job_description)

            status.info("🤖 Generating AI Feedback..."); progress.progress(68)
            ai_feedback = generate_resume_feedback(resume_text, skill_result["missing"], ats_score)

            status.info("🎤 Generating Interview Questions..."); progress.progress(76)
            interview_questions = generate_interview_questions(resume_text, job_description)

            status.info("📚 Building Learning Roadmap..."); progress.progress(84)
            learning_roadmap = generate_learning_roadmap(resume_text, skill_result["missing"])

            status.info("✉️ Generating Cover Letter..."); progress.progress(92)
            cover_letter = generate_cover_letter(resume_text, job_description)

            careerpilot_score = calculate_careerpilot_score(
                ats_score, skill_result["matching"],
                len(skill_result["matching"]) + len(skill_result["missing"]),
                resume_quality
            )
            total_skills     = len(skill_result["matching"]) + len(skill_result["missing"])
            skill_percentage = round((len(skill_result["matching"]) / total_skills) * 100, 2) if total_skills > 0 else 0
            sections_found   = sum(1 for v in sections.values() if v.strip())

            st.session_state.update({
                "careerpilot_score":   careerpilot_score,
                "ats_score":           ats_score,
                "skill_percentage":    skill_percentage,
                "resume_quality":      resume_quality,
                "matching_count":      len(skill_result["matching"]),
                "missing_count":       len(skill_result["missing"]),
                "sections_found":      sections_found,
                "skill_result":        skill_result,
                "ai_feedback":         ai_feedback,
                "interview_questions": interview_questions,
                "learning_roadmap":    learning_roadmap,
                "cover_letter":        cover_letter,
                "sections":            sections,
                "skills":              skills,
                "resume_text":         resume_text,
                "job_description":     job_description,
            })

            progress.progress(100)
            status.success("✅ Analysis Complete!")
            st.rerun()  # rerun so hero updates with score ring

        else:
            st.warning("⚠️ Please paste a Job Description to analyze.")

    # Show results below upload if analysis done
    if "careerpilot_score" in st.session_state:
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        show_metrics(
            st.session_state["careerpilot_score"],
            st.session_state["ats_score"],
            st.session_state["skill_percentage"],
            st.session_state["resume_quality"],
            matching_count=st.session_state["matching_count"],
            missing_count=st.session_state["missing_count"],
            sections_found=st.session_state["sections_found"]
        )
        show_skill_section(st.session_state["skill_result"])

# ==================================================
# AI INSIGHTS
# ==================================================
elif active_page == "AI Insights":
    st.markdown("""
    <div style="font-size:28px;font-weight:800;color:#111827;margin-bottom:4px;">🤖 AI Insights</div>
    <div style="font-size:14px;color:#9ca3af;margin-bottom:20px;">AI-generated feedback, interview prep and skill recommendations</div>
    <hr style="border:none;border-top:1.5px solid #EDE9FE;margin-bottom:20px;">
    """, unsafe_allow_html=True)
    if "ai_feedback" in st.session_state:
        show_ai_sections(
            st.session_state["ai_feedback"],
            st.session_state["interview_questions"],
            st.session_state["learning_roadmap"]
        )
    else:
        st.info("🔍 Run an analysis from the Dashboard first.")

# ==================================================
# RESUME ANALYSIS
# ==================================================
elif active_page == "Resume Analysis":
    st.markdown("""
    <div style="font-size:28px;font-weight:800;color:#111827;margin-bottom:4px;">📄 Resume Analysis</div>
    <div style="font-size:14px;color:#9ca3af;margin-bottom:20px;">Parsed sections and detected skills from your resume</div>
    <hr style="border:none;border-top:1.5px solid #EDE9FE;margin-bottom:20px;">
    """, unsafe_allow_html=True)
    if "sections" in st.session_state:
        show_resume_section(st.session_state["sections"], st.session_state["skills"])
    else:
        st.info("🔍 Run an analysis from the Dashboard first.")

# ==================================================
# LEARNING ROADMAP
# ==================================================
elif active_page == "Learning Roadmap":
    st.markdown("""
    <div style="font-size:28px;font-weight:800;color:#111827;margin-bottom:4px;">🗺️ Learning Roadmap</div>
    <div style="font-size:14px;color:#9ca3af;margin-bottom:20px;">Personalized skill learning plan based on your gaps</div>
    <hr style="border:none;border-top:1.5px solid #EDE9FE;margin-bottom:20px;">
    """, unsafe_allow_html=True)
    if "learning_roadmap" in st.session_state:
        st.markdown(st.session_state["learning_roadmap"])
    else:
        st.info("🔍 Run an analysis from the Dashboard first.")

# ==================================================
# COVER LETTER
# ==================================================
elif active_page == "Cover Letter":
    st.markdown("""
    <div style="font-size:28px;font-weight:800;color:#111827;margin-bottom:4px;">✉️ Cover Letter</div>
    <div style="font-size:14px;color:#9ca3af;margin-bottom:20px;">AI-generated cover letter tailored to your resume and job description</div>
    <hr style="border:none;border-top:1.5px solid #EDE9FE;margin-bottom:20px;">
    """, unsafe_allow_html=True)
    if "cover_letter" in st.session_state:
        st.markdown(st.session_state["cover_letter"])
        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 Download .txt",
                data=st.session_state["cover_letter"],
                file_name="cover_letter.txt", mime="text/plain",
                use_container_width=True)
        with c2:
            if st.button("🔄 Regenerate", use_container_width=True):
                with st.spinner("Regenerating..."):
                    new = generate_cover_letter(
                        st.session_state["resume_text"],
                        st.session_state["job_description"]
                    )
                    st.session_state["cover_letter"] = new
                    st.rerun()
    else:
        st.info("🔍 Run an analysis from the Dashboard first.")

st.markdown('</div>', unsafe_allow_html=True)
show_footer()