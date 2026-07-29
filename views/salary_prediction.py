import textwrap
import time
import streamlit as st
from components.cards import hero_header, empty_state_card
from components.metrics import kpi_card
from salary_prediction.inference import predict_salary_detailed

def show_salary_prediction():
    """
    Renders the Salary Prediction Studio (AI Compensation Advisor) view controller.
    Driven 100% by outputs from the frozen Salary Prediction backend.
    """
    # =========================================================
    # 1. PURPLE HERO BANNER
    # =========================================================
    hero_header(
        title="Salary Prediction Studio",
        subtitle="Estimate your expected annual market compensation using AI-powered salary prediction.",
        icon="💰"
    )

    resume_text = st.session_state.get("resume_text", "")
    resume_uploaded = st.session_state.get("resume_uploaded", False)

    if not resume_uploaded or not resume_text.strip():
        empty_state_card(
            title="No Active Resume Detected",
            message="Please upload a PDF resume in the Resume Studio or Home page first to evaluate AI salary benchmarks.",
            icon="📄"
        )
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(" Go to Resume Analysis ➔", key="btn_go_resume_analysis", type="primary"):
                st.session_state.current_page = "Resume Analysis"
                st.rerun()
        return

    # Extract target job title from Role Prediction results if available
    role_predictions = st.session_state.get("role_prediction_results", [])
    default_job_title = role_predictions[0]["role"] if role_predictions else "Machine Learning Engineer"

    # Infer experience level default from resume section length
    exp_text = st.session_state.get("resume_sections", {}).get("experience", "")
    if len(exp_text.split()) > 200:
        default_exp = "SE"
    elif len(exp_text.split()) > 80:
        default_exp = "MI"
    else:
        default_exp = "EN"

    st.markdown("### 🎛️ Candidate Profile & Compensation Parameters")
    st.markdown("<p style='color: #94A3B8; font-size: 0.88rem; margin-bottom: 1rem;'>Select profile variables to evaluate expected market compensation across different work setups.</p>", unsafe_allow_html=True)

    p1, p2, p3, p4 = st.columns(4)
    with p1:
        exp_level = st.selectbox(
            "Experience Tier",
            options=["EN", "MI", "SE", "EX"],
            index=["EN", "MI", "SE", "EX"].index(default_exp),
            format_func=lambda x: {
                "EN": "Entry-level (0-2 Yrs)",
                "MI": "Mid-level (2-5 Yrs)",
                "SE": "Senior-level (5+ Yrs)",
                "EX": "Executive-level (8+ Yrs)"
            }.get(x, x),
            key="sel_exp_level"
        )
    with p2:
        job_title = st.selectbox(
            "Target Role",
            options=[
                "Machine Learning Engineer",
                "Data Scientist",
                "AI Engineer",
                "Data Engineer",
                "Backend Developer",
                "Full Stack Engineer",
                "DevOps & Cloud Engineer",
                "UI/UX & Product Designer",
                "Software Engineer",
                "Lead Data Scientist"
            ],
            index=0 if default_job_title not in [
                "Machine Learning Engineer", "Data Scientist", "AI Engineer",
                "Data Engineer", "Backend Developer", "Full Stack Engineer",
                "DevOps & Cloud Engineer", "UI/UX & Product Designer", "Software Engineer"
            ] else [
                "Machine Learning Engineer", "Data Scientist", "AI Engineer",
                "Data Engineer", "Backend Developer", "Full Stack Engineer",
                "DevOps & Cloud Engineer", "UI/UX & Product Designer", "Software Engineer"
            ].index(default_job_title),
            key="sel_job_title"
        )
    with p3:
        comp_loc = st.selectbox(
            "Company Location",
            options=["US", "CA", "GB", "DE", "IN", "FR", "JP"],
            index=0,
            format_func=lambda x: {"US": "United States (US)", "CA": "Canada (CA)", "GB": "United Kingdom (GB)", "DE": "Germany (DE)", "IN": "India (IN)", "FR": "France (FR)", "JP": "Japan (JP)"}.get(x, x),
            key="sel_comp_loc"
        )
    with p4:
        remote_val = st.selectbox(
            "Remote Work Setup",
            options=[100, 50, 0],
            index=0,
            format_func=lambda x: {100: "100% Fully Remote", 50: "50% Hybrid Work", 0: "Onsite / In-Office"}.get(x, str(x)),
            key="sel_remote_val"
        )

    cache_key = f"{exp_level}_{job_title}_{comp_loc}_{remote_val}"

    # =========================================================
    # 2. AI COMPENSATION ANALYSIS WORKFLOW
    # =========================================================
    if "salary_prediction_results" not in st.session_state or st.session_state.get("salary_cache_key") != cache_key:
        st.markdown("### 🤖 AI Compensation Workflow")
        progress_bar = st.progress(0)
        status_text = st.empty()

        workflow_stages = [
            (15, "✓ Reading Career Profile..."),
            (35, "✓ Loading Salary Model..."),
            (55, "✓ Evaluating Compensation Factors..."),
            (75, "✓ Computing Salary Estimate..."),
            (90, "✓ Preparing Compensation Report..."),
            (100, "✓ Salary Prediction Complete 🎉"),
        ]

        for pct, stage_msg in workflow_stages:
            status_text.markdown(f"<span style='color: #A5B4FC; font-weight: 600;'>{stage_msg}</span>", unsafe_allow_html=True)
            progress_bar.progress(pct)
            time.sleep(0.04)

        # Execute frozen backend prediction
        backend_result = predict_salary_detailed(
            experience_level=exp_level,
            employment_type="FT",
            job_title=job_title,
            employee_residence="US",
            remote_ratio=remote_val,
            company_location=comp_loc,
            company_size="M"
        )

        st.session_state["salary_prediction_results"] = backend_result
        st.session_state["salary_cache_key"] = cache_key
        status_text.empty()
        progress_bar.empty()
        st.rerun()

    result = st.session_state.get("salary_prediction_results", {})
    if not result:
        st.error("Unable to retrieve salary predictions from the backend model.")
        return

    pred_salary = result.get("predicted_salary", 0.0)
    salary_range = result.get("salary_range", {})
    min_sal = salary_range.get("min", 0.0)
    max_sal = salary_range.get("max", 0.0)

    confidence = result.get("confidence", {})
    conf_pct = confidence.get("percentage", 0.0)
    conf_level = confidence.get("level", "Moderate")

    explanation = result.get("explanation", {})
    exp_summary = explanation.get("summary", "")

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 3. HERO SALARY CARD
    # =========================================================
    st.markdown("### 🏆 Estimated Annual Salary")

    hero_card_html = f"""<div class="glass-panel" style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(99, 102, 241, 0.12) 100%); border: 1.5px solid rgba(16, 185, 129, 0.4); padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.5rem;">
<div>
<span class="skill-chip" style="background: rgba(16, 185, 129, 0.25); border-color: rgba(16, 185, 129, 0.5); color: #34D399; font-weight: 700; padding: 0.35rem 0.85rem; margin-bottom: 0.75rem; display: inline-block;">
💵 Estimated Annual Compensation
</span>
<h1 style="font-size: 3rem; font-weight: 900; color: #F8FAFC; margin: 0.25rem 0 0.25rem 0;">
${pred_salary:,.0f} <span style="font-size: 1.25rem; font-weight: 600; color: #94A3B8;">USD / Year</span>
</h1>
<p style="color: #CBD5E1; font-size: 0.95rem; margin: 0;">
Target benchmark for <b>{job_title}</b> ({explanation.get("experience_tier", exp_level)})
</p>
</div>
<div style="text-align: right; background: rgba(15, 23, 42, 0.6); padding: 1.25rem 1.75rem; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.1); min-width: 200px;">
<div style="font-size: 0.75rem; text-transform: uppercase; color: #A7F3D0; font-weight: 700; letter-spacing: 0.05em;">
Prediction Stability
</div>
<div style="font-size: 2.25rem; font-weight: 900; color: #34D399; margin: 0.2rem 0;">
{conf_level} <span style="font-size: 1.2rem; font-weight: 700; color: #A5B4FC;">({conf_pct:.1f})</span>
</div>
<div style="font-size: 0.78rem; color: #94A3B8;">
Backend Confidence Level
</div>
</div>
</div>
</div>"""

    st.markdown(hero_card_html, unsafe_allow_html=True)

    # =========================================================
    # 4. EXPECTED SALARY RANGE
    # =========================================================
    st.markdown("### 📊 Expected Salary Range")
    st.markdown("<p style='color: #94A3B8; font-size: 0.92rem; margin-bottom: 1.25rem;'>Statistically derived compensation range from the backend Random Forest ensemble model.</p>", unsafe_allow_html=True)

    range_width = max_sal - min_sal

    range_card_html = f"""<div class="glass-panel" style="padding: 1.75rem; border-left: 4px solid #10B981; margin-bottom: 2rem;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
<div>
<div style="font-size: 0.8rem; text-transform: uppercase; color: #94A3B8; font-weight: 700;">Lower Range Limit</div>
<div style="font-size: 1.5rem; font-weight: 800; color: #CBD5E1;">${min_sal:,.0f} USD</div>
</div>
<div style="text-align: center;">
<div style="font-size: 0.8rem; text-transform: uppercase; color: #34D399; font-weight: 700;">Expected Point Estimate</div>
<div style="font-size: 1.85rem; font-weight: 900; color: #34D399;">${pred_salary:,.0f} USD</div>
</div>
<div style="text-align: right;">
<div style="font-size: 0.8rem; text-transform: uppercase; color: #94A3B8; font-weight: 700;">Upper Range Limit</div>
<div style="font-size: 1.5rem; font-weight: 800; color: #CBD5E1;">${max_sal:,.0f} USD</div>
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.08); height: 12px; border-radius: 6px; position: relative; overflow: hidden;">
<div style="background: linear-gradient(90deg, #10B981 0%, #6366F1 50%, #A855F7 100%); width: 100%; height: 100%; border-radius: 6px;"></div>
</div>
</div>"""

    st.markdown(range_card_html, unsafe_allow_html=True)

    # =========================================================
    # 5. COMPENSATION FACTORS
    # =========================================================
    st.markdown("### 🧩 Compensation Factors")

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1:
        st.markdown(f"""<div class="glass-panel" style="padding: 0.85rem; text-align: center;">
<div style="font-size: 0.72rem; text-transform: uppercase; color: #64748B; font-weight: 700;">Experience Level</div>
<div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC; margin-top: 0.25rem;">{explanation.get("experience_tier", exp_level)}</div>
</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="glass-panel" style="padding: 0.85rem; text-align: center;">
<div style="font-size: 0.72rem; text-transform: uppercase; color: #64748B; font-weight: 700;">Job Title</div>
<div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC; margin-top: 0.25rem;">{job_title}</div>
</div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="glass-panel" style="padding: 0.85rem; text-align: center;">
<div style="font-size: 0.72rem; text-transform: uppercase; color: #64748B; font-weight: 700;">Company Size</div>
<div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC; margin-top: 0.25rem;">{explanation.get("company_scale", "Medium")}</div>
</div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="glass-panel" style="padding: 0.85rem; text-align: center;">
<div style="font-size: 0.72rem; text-transform: uppercase; color: #64748B; font-weight: 700;">Remote Setup</div>
<div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC; margin-top: 0.25rem;">{explanation.get("work_setup", "Remote")}</div>
</div>""", unsafe_allow_html=True)
    with c5:
        st.markdown(f"""<div class="glass-panel" style="padding: 0.85rem; text-align: center;">
<div style="font-size: 0.72rem; text-transform: uppercase; color: #64748B; font-weight: 700;">Company Location</div>
<div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC; margin-top: 0.25rem;">{comp_loc}</div>
</div>""", unsafe_allow_html=True)
    with c6:
        st.markdown(f"""<div class="glass-panel" style="padding: 0.85rem; text-align: center;">
<div style="font-size: 0.72rem; text-transform: uppercase; color: #64748B; font-weight: 700;">Employment Type</div>
<div style="font-weight: 700; font-size: 0.88rem; color: #F8FAFC; margin-top: 0.25rem;">{explanation.get("employment_type", "Full-Time")}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 6. AI COMPENSATION SUMMARY
    # =========================================================
    st.markdown("### 💡 AI Compensation Summary")

    summary_html = f"""<div class="glass-panel" style="border-left: 4px solid #6366F1; padding: 1.5rem; margin-bottom: 2rem;">
<div style="font-weight: 700; font-size: 1.1rem; color: #F8FAFC; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
<span>🤖</span> Backend Compensation Analysis Summary
</div>
<p style="color: #CBD5E1; font-size: 0.98rem; line-height: 1.7; margin: 0;">
"{exp_summary}"
</p>
</div>"""

    st.markdown(summary_html, unsafe_allow_html=True)

    # =========================================================
    # 7. COMPENSATION SNAPSHOT
    # =========================================================
    st.markdown("### 📈 Compensation Snapshot")

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        kpi_card("Annual Salary", f"${pred_salary:,.0f}", "Base Target", "#10B981")
    with k2:
        kpi_card("Prediction Stability", f"{conf_level}", f"{conf_pct:.1f} Score", "#6366F1")
    with k3:
        kpi_card("Salary Range", f"${min_sal:,.0f} - ${max_sal:,.0f}", f"Width ${range_width:,.0f}", "#A855F7")
    with k4:
        kpi_card("Work Setup", f"{explanation.get('work_setup', 'Remote')}", "Remote Ratio", "#06B6D4")

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 8. CTA WORKFLOW BANNER
    # =========================================================
    cta_html = f"""<div class="hero-container" style="text-align: center; padding: 2.25rem 2rem;">
<h3 style="margin-bottom: 0.5rem; color: #F8FAFC;">🚀 Ready to Discover Matching Job Opportunities?</h3>
<p style="color: #94A3B8; font-size: 0.95rem; margin-bottom: 1.5rem; max-width: 650px; margin-left: auto; margin-right: auto;">
Continue to Job Recommendations to explore opportunities aligned with your predicted salary and career profile.
</p>
</div>"""
    st.markdown(cta_html, unsafe_allow_html=True)

    c_btn1, c_btn2, c_btn3 = st.columns([1, 2, 1])
    with c_btn2:
        if st.button("Continue to Job Recommendations ➔", key="btn_next_jobs", type="primary"):
            st.session_state.current_page = "Job Recommendations"
            st.rerun()
