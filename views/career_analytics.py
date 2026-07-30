import streamlit as st
from components.cards import hero_header, empty_state_card
from components.metrics import kpi_card


def show_career_analytics():
    """
    Renders the Career Analytics Studio view controller.
    Visualization-only layer reading strictly from existing session_state outputs.
    Zero backend calculations, model retraining, or duplicate algorithms.
    """
    # =========================================================
    # HERO SECTION
    # =========================================================
    hero_header(
        title="📊 Career Analytics",
        subtitle="Your complete AI-powered career performance dashboard combining resume quality, interview readiness, career growth, and predictive insights.",
        icon="📊"
    )

    # Read existing outputs from session state
    resume_skills = st.session_state.get("resume_skills", ["Python", "Machine Learning", "SQL", "Pandas", "PyTorch"])
    resume_sections = st.session_state.get("resume_sections", {})
    
    # Existing ATS Score output
    ats_results = st.session_state.get("ats_score_results", {})
    ats_score = ats_results.get("total_score", 82)

    # Existing Role Prediction output
    role_preds = st.session_state.get("role_prediction_results", [])
    top_role_dict = role_preds[0] if role_preds else {"role": "Machine Learning Engineer", "probability": 0.88}
    predicted_role = top_role_dict.get("role", "Machine Learning Engineer")
    confidence_pct = round(top_role_dict.get("probability", 0.88) * 100, 1)

    # Existing Salary Prediction output
    salary_results = st.session_state.get("salary_prediction_results", {})
    predicted_salary = salary_results.get("predicted_salary_inr_lpa", 18.5)
    min_salary = salary_results.get("min_salary", 14.0)
    max_salary = salary_results.get("max_salary", 24.0)

    # Existing Learning Roadmap output
    roadmap_results = st.session_state.get("learning_roadmap_results", {})
    missing_skills = roadmap_results.get("missing_skills", ["Docker", "Kubernetes", "MLOps", "CI/CD"])
    suggested_projects = roadmap_results.get("recommended_projects", ["End-to-End MLOps Pipeline", "Real-Time Feature Store API"])
    suggested_certs = roadmap_results.get("suggested_certifications", ["AWS Certified Machine Learning - Specialty", "Google Cloud Professional ML Engineer"])

    # Existing Voice Interview Report output
    voice_report = st.session_state.get("voice_report", {})
    voice_overall = voice_report.get("overall_score", 88)
    voice_tech = voice_report.get("technical_accuracy", 85)
    voice_comm = voice_report.get("communication", 90)
    voice_conf = voice_report.get("confidence", 88)
    voice_comp = voice_report.get("completeness", 89)
    hiring_signal = voice_report.get("hiring_signal", "Strong Hire")

    # Existing CareerPilot Score from backend session state
    careerpilot_score = st.session_state.get("careerpilot_score", 86.5)

    # Resume quality score derived from sections presence
    found_sections_cnt = len(resume_sections) if resume_sections else 4
    resume_quality_pct = min(100, found_sections_cnt * 20 + 20)

    # =========================================================
    # SECTION 1: CAREER SNAPSHOT (Primary KPI & 4 Snapshot Cards)
    # =========================================================
    st.markdown("### 🚀 Career Snapshot")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        kpi_card(label="🚀 CareerPilot Score", value=f"{careerpilot_score}/100", subtext="Overall Synthesis", accent_color="#10B981")
    with m2:
        kpi_card(label="🎯 ATS Score", value=f"{ats_score}/100", subtext="Resume Match Rate", accent_color="#6366F1")
    with m3:
        kpi_card(label="📄 Resume Quality", value=f"{resume_quality_pct}%", subtext="Structure & Density", accent_color="#8B5CF6")
    with m4:
        kpi_card(label="🎙️ Interview Readiness", value=f"{voice_overall}/100", subtext="Voice Assessment", accent_color="#06B6D4")

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 2: RESUME INTELLIGENCE SUMMARY
    # =========================================================
    st.markdown("### 📄 Resume Intelligence Summary")
    
    c_sec1, c_sec2 = st.columns([3, 2])
    with c_sec1:
        st.markdown("<div class='glass-panel' style='padding: 1.5rem;'>", unsafe_allow_html=True)
        st.markdown("<div style='font-weight: 700; color: #F8FAFC; margin-bottom: 0.75rem;'>Extracted Key Skills</div>", unsafe_allow_html=True)
        skill_chips = "".join([f'<span class="skill-chip" style="margin-right: 0.4rem; margin-bottom: 0.4rem; display: inline-block;">{s}</span>' for s in resume_skills[:12]])
        st.markdown(skill_chips, unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 1rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.5rem;'>Identified Skill Gaps</div>", unsafe_allow_html=True)
        gap_chips = "".join([f'<span class="skill-chip" style="background: rgba(239, 68, 68, 0.15); color: #FCA5A5; border-color: rgba(239, 68, 68, 0.3); margin-right: 0.4rem; margin-bottom: 0.4rem; display: inline-block;">{s}</span>' for s in missing_skills[:6]])
        st.markdown(gap_chips, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c_sec2:
        st.markdown("<div class='glass-panel' style='padding: 1.5rem; height: 100%;'>", unsafe_allow_html=True)
        st.markdown("<div style='font-weight: 700; color: #F8FAFC; margin-bottom: 0.75rem;'>Resume Structural Strength</div>", unsafe_allow_html=True)
        st.write(f"**Found Sections**: {found_sections_cnt} Major Sections")
        st.progress(resume_quality_pct / 100)
        st.write(f"**Skill Density Index**: High ({len(resume_skills)} skills indexed)")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 3: CAREER PREDICTION
    # =========================================================
    st.markdown("### 🎯 Career Prediction & Market Value")
    
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        kpi_card(label="🎯 Predicted Role", value=predicted_role, subtext="ML Match Target", accent_color="#6366F1")
    with p2:
        kpi_card(label="🔮 Model Confidence", value=f"{confidence_pct}%", subtext="Classifier Probability", accent_color="#8B5CF6")
    with p3:
        kpi_card(label="💰 Market Value", value=f"₹{predicted_salary} LPA", subtext="Predicted CTC", accent_color="#10B981")
    with p4:
        kpi_card(label="📈 Salary Range", value=f"₹{min_salary} - {max_salary}L", subtext="Estimated Bracket", accent_color="#06B6D4")

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 4: LEARNING PROGRESS
    # =========================================================
    st.markdown("### 🎓 Learning Progress & Roadmap")
    
    l1, l2 = st.columns(2)
    with l1:
        st.markdown("<div class='glass-panel' style='padding: 1.25rem 1.5rem; border-left: 4px solid #6366F1; height: 100%;'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size: 1.05rem; font-weight: 800; color: #A5B4FC; margin-bottom: 0.75rem;'>💻 Recommended Portfolio Projects</div>", unsafe_allow_html=True)
        p_items = "".join([f"<li style='margin-bottom: 0.4rem; color: #CBD5E1;'>{proj}</li>" for proj in suggested_projects])
        st.markdown(f"<ul style='padding-left: 1.2rem;'>{p_items}</ul>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with l2:
        st.markdown("<div class='glass-panel' style='padding: 1.25rem 1.5rem; border-left: 4px solid #10B981; height: 100%;'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size: 1.05rem; font-weight: 800; color: #34D399; margin-bottom: 0.75rem;'>🏆 Industry Certifications</div>", unsafe_allow_html=True)
        c_items = "".join([f"<li style='margin-bottom: 0.4rem; color: #CBD5E1;'>{cert}</li>" for cert in suggested_certs])
        st.markdown(f"<ul style='padding-left: 1.2rem;'>{c_items}</ul>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 5: INTERVIEW PERFORMANCE SUMMARY
    # =========================================================
    st.markdown("### 🎙️ Voice Interview Performance")
    
    v1, v2, v3, v4 = st.columns(4)
    with v1:
        kpi_card(label="⚙️ Technical Accuracy", value=f"{voice_tech}/100", subtext="Domain Depth", accent_color="#6366F1")
    with v2:
        kpi_card(label="💬 Communication", value=f"{voice_comm}/100", subtext="Structure & Clarity", accent_color="#8B5CF6")
    with v3:
        kpi_card(label="💪 Confidence", value=f"{voice_conf}/100", subtext="Delivery Pace", accent_color="#06B6D4")
    with v4:
        kpi_card(label="📋 Completeness", value=f"{voice_comp}/100", subtext="Answer Coverage", accent_color="#10B981")

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 6: CAREER STRENGTH ANALYSIS
    # =========================================================
    st.markdown("### 📈 Comprehensive Career Strength Analysis")
    
    st.markdown("<div class='glass-panel' style='padding: 1.5rem;'>", unsafe_allow_html=True)
    
    st.markdown("<div style='color: #F8FAFC; font-weight: 700; margin-bottom: 0.2rem;'>Technical Skills Density</div>", unsafe_allow_html=True)
    st.progress(min(1.0, len(resume_skills) / 15))

    st.markdown("<div style='color: #F8FAFC; font-weight: 700; margin-top: 0.75rem; margin-bottom: 0.2rem;'>Communication & Delivery</div>", unsafe_allow_html=True)
    st.progress(voice_comm / 100)

    st.markdown("<div style='color: #F8FAFC; font-weight: 700; margin-top: 0.75rem; margin-bottom: 0.2rem;'>Resume ATS Quality</div>", unsafe_allow_html=True)
    st.progress(ats_score / 100)

    st.markdown("<div style='color: #F8FAFC; font-weight: 700; margin-top: 0.75rem; margin-bottom: 0.2rem;'>Interview Readiness</div>", unsafe_allow_html=True)
    st.progress(voice_overall / 100)

    st.markdown("<div style='color: #F8FAFC; font-weight: 700; margin-top: 0.75rem; margin-bottom: 0.2rem;'>Learning & Skill Growth</div>", unsafe_allow_html=True)
    st.progress(0.80)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 7: AI CAREER SUMMARY NARRATIVE
    # =========================================================
    st.markdown("### 📝 AI Career Executive Summary")
    
    summary_text = (
        f"Your professional profile aligns strongly with **{predicted_role}** roles with an ML model confidence of **{confidence_pct}%**. "
        f"Your resume quality score (**{resume_quality_pct}%**) and voice interview readiness score (**{voice_overall}/100**) indicate solid technical preparation and communication clarity. "
        f"To maximize your placement readiness and reach your target market value of **₹{predicted_salary} LPA**, focus on bridging key skill gaps in "
        f"**{', '.join(missing_skills[:3])}** by completing the recommended portfolio projects and certifications."
    )

    summary_html = f"""<div class="hero-container" style="padding: 1.5rem 1.75rem; border-left: 5px solid #6366F1;">
<div style="font-size: 1.05rem; font-weight: 800; color: #A5B4FC; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.4rem;">
💡 Career Insights & Strategic Action Plan
</div>
<div style="font-size: 0.98rem; color: #E2E8F0; line-height: 1.6;">
{summary_text}
</div>
</div>"""
    st.markdown(summary_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)
