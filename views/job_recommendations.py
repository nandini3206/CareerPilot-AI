import base64
import os
import textwrap
import streamlit as st
import pandas as pd
from typing import Dict, List, Any

# Check if FAISS is available in environment
try:
    from career_recommendation.ranker import HAS_FAISS
except Exception:
    HAS_FAISS = False

# Lazy-load inference engine singleton to avoid redundant loading
@st.cache_resource
def get_recommendation_inference():
    try:
        from career_recommendation.inference import CareerRecommendationInference
        return CareerRecommendationInference()
    except Exception as e:
        st.error(f"Error loading Career Recommendation Engine: {e}")
        return None

def get_svg_logo_html(width=48, height=48):
    svg_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.svg")
    if os.path.exists(svg_path):
        with open(svg_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        return f'<img src="data:image/svg+xml;base64,{b64}" width="{width}" height="{height}" style="vertical-align: middle; display: inline-block;">'
    return "✦"

def show_job_recommendations():
    """
    Renders the Upgraded Job Recommendation Engine UI for CareerPilot AI.
    Reads ONLY existing session_state variables (skills, role, salary, resume_text).
    Does NOT modify any existing frozen module or session_state keys.
    """
    # Informational message if FAISS fallback mode is active
    if not HAS_FAISS:
        st.info("ℹ️ FAISS not available. Using cosine similarity search.")

    # ---------------------------------------------------------
    # 1. READ CANDIDATE PROFILE FROM SESSION STATE (READ-ONLY)
    # ---------------------------------------------------------
    resume_uploaded = st.session_state.get("resume_uploaded", False)
    resume_skills = st.session_state.get("resume_skills", []) or st.session_state.get("extracted_skills", [])
    
    # Extract candidate predicted role (handles string or dict format)
    raw_role = st.session_state.get("predicted_role", "") or st.session_state.get("role_prediction", "")
    if isinstance(raw_role, dict):
        predicted_role = raw_role.get("predicted_role", "Machine Learning Engineer")
    else:
        predicted_role = str(raw_role) if raw_role else "Machine Learning Engineer"

    # Extract candidate predicted salary
    raw_sal = st.session_state.get("predicted_salary", "") or st.session_state.get("salary_prediction", "")
    if isinstance(raw_sal, dict):
        predicted_salary = raw_sal.get("predicted_salary", "1200000")
    else:
        predicted_salary = str(raw_sal) if raw_sal else "1200000"

    resume_text = st.session_state.get("resume_text", "")

    # Initialize local UI view state (Compare & Saved lists)
    if "saved_jobs" not in st.session_state:
        st.session_state.saved_jobs = set()
    if "compare_jobs" not in st.session_state:
        st.session_state.compare_jobs = []

    # ---------------------------------------------------------
    # 2. HERO HEADER
    # ---------------------------------------------------------
    logo_img = get_svg_logo_html(width=48, height=48)
    hero_html = textwrap.dedent(f"""
    <div class="hero-container" style="padding: 2rem; position: relative;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
            <div>
                <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
                    {logo_img}
                    <h1 style="font-size: 2rem; font-weight: 800; color: #F8FAFC; margin: 0;">
                        AI Job Recommendation Engine
                    </h1>
                </div>
                <p style="font-size: 0.95rem; color: #94A3B8; margin: 0; max-width: 680px;">
                    Personalized multi-factor career matching analyzing skills, predicted role trajectory, salary alignment, and live market openings.
                </p>
            </div>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <span style="background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3); color: #A5B4FC; padding: 0.4rem 0.85rem; border-radius: 9999px; font-size: 0.82rem; font-weight: 600;">
                    🎯 Role: {predicted_role[:24]}
                </span>
                <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); color: #34D399; padding: 0.4rem 0.85rem; border-radius: 9999px; font-size: 0.82rem; font-weight: 600;">
                    ⚡ {len(resume_skills)} Extracted Skills
                </span>
            </div>
        </div>
    </div>
    """).strip()
    st.markdown(hero_html, unsafe_allow_html=True)

    if not resume_uploaded and not resume_skills:
        st.info("💡 **Tip**: Upload a resume in **Resume Studio** to get maximum personalization and automatic skill extraction.")

    # ---------------------------------------------------------
    # 3. INTERACTIVE FILTERS BAR
    # ---------------------------------------------------------
    with st.expander("🔍 Search & Filter Controls", expanded=True):
        col_f1, col_f2, col_f3, col_f4 = st.columns([2, 1, 1, 1])
        with col_f1:
            search_query = st.text_input("Target Job Title / Keywords", value=predicted_role)
        with col_f2:
            pref_location = st.selectbox("Preferred Location", ["India", "Remote", "United States", "United Kingdom", "All Locations"])
        with col_f3:
            exp_level = st.selectbox("Experience Level", ["Entry", "Junior", "Mid", "Senior", "Lead"])
        with col_f4:
            emp_type = st.selectbox("Employment Type", ["Full-time", "Contract", "Internship", "Part-time"])

        col_s1, col_s2 = st.columns([2, 1])
        with col_s1:
            min_score = st.slider("Minimum Match Score % Filter", min_value=50, max_value=95, value=60, step=5)
        with col_s2:
            st.markdown("<div style='margin-top: 1.6rem;'></div>", unsafe_allow_html=True)
            run_search = st.button("🚀 Fetch Matches", type="primary", use_container_width=True)

    # ---------------------------------------------------------
    # 4. EXECUTE RECOMMENDATION ENGINE
    # ---------------------------------------------------------
    inference = get_recommendation_inference()
    if not inference:
        st.warning("Recommendation Engine unavailable. Please check system configurations.")
        return

    with st.spinner("Analyzing profile vectors & scanning live career market..."):
        jobs = inference.recommend(
            predicted_role=search_query or predicted_role,
            skills=resume_skills,
            predicted_salary=predicted_salary,
            resume_text=resume_text,
            preferred_location="" if pref_location == "All Locations" else pref_location,
            experience_level=exp_level,
            employment_type=emp_type.lower().replace("-", "_"),
            top_k=20,
        )

    # Filter by min_score
    filtered_jobs = [j for j in jobs if j.get("match_score", j.get("careerpilot_score", 0)) >= min_score]

    # ---------------------------------------------------------
    # 5. SIDE-BY-SIDE JOB COMPARISON DRAWER / CONTAINER
    # ---------------------------------------------------------
    if st.session_state.compare_jobs:
        with st.expander(f"⚖️ Job Comparison Drawer ({len(st.session_state.compare_jobs)} selected)", expanded=True):
            comp_cols = st.columns(len(st.session_state.compare_jobs))
            for idx, c_job in enumerate(st.session_state.compare_jobs):
                with comp_cols[idx]:
                    st.markdown(f"### {c_job.get('title')}")
                    st.caption(f"🏢 {c_job.get('company')} | 📍 {c_job.get('location')}")
                    
                    m_score = c_job.get('match_score', 80)
                    s_cov = c_job.get('skill_coverage', 75)
                    st.metric("Overall Match", f"{m_score}%")
                    st.progress(s_cov / 100.0, text=f"Skill Coverage: {s_cov}%")
                    
                    matched_list = c_job.get("matched_skills", [])
                    missing_list = c_job.get("missing_skills", [])
                    
                    st.markdown(f"**Matched ({len(matched_list)}):** " + (", ".join(matched_list[:4]) if matched_list else "Semantic Match"))
                    st.markdown(f"**Missing ({len(missing_list)}):** " + (", ".join(missing_list[:4]) if missing_list else "None"))
                    
                    if st.button(f"❌ Remove", key=f"btn_remove_comp_{idx}"):
                        st.session_state.compare_jobs.pop(idx)
                        st.rerun()

            if st.button("Clear All Comparisons", key="btn_clear_comp"):
                st.session_state.compare_jobs = []
                st.rerun()

        st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 6. RENDER JOB RECOMMENDATION CARDS
    # ---------------------------------------------------------
    st.markdown(f"### 🎯 Top Career Opportunities ({len(filtered_jobs)} Found)")

    if not filtered_jobs:
        st.warning("No job recommendations met the current filter criteria. Try lowering the minimum match score filter or selecting 'All Locations'.")
        return

    for idx, job in enumerate(filtered_jobs, start=1):
        title = job.get("title", "Career Opportunity")
        company = job.get("company", "Top Employer")
        location = job.get("location", "Flexible / Remote")
        employment_type = job.get("employment_type", "Full-time")
        source = job.get("source", "CareerPilot AI")
        redirect_url = job.get("redirect_url", "#")
        
        match_score = job.get("match_score", job.get("careerpilot_score", 75))
        skill_coverage = job.get("skill_coverage", 70)
        matched_skills = job.get("matched_skills", [])
        missing_skills = job.get("missing_skills", [])
        reason = job.get("recommendation_reason", "High overall profile alignment.")
        
        # Display Card
        with st.container():
            # Card Top Header HTML
            card_header_html = textwrap.dedent(f"""
            <div class="glass-panel" style="margin-bottom: 0.5rem; padding: 1.25rem; border-left: 4px solid #6366F1;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.75rem;">
                    <div>
                        <div style="font-size: 1.2rem; font-weight: 800; color: #F8FAFC; margin-bottom: 0.25rem;">
                            {title}
                        </div>
                        <div style="font-size: 0.9rem; color: #94A3B8; font-weight: 500;">
                            🏢 <b style="color: #CBD5E1;">{company}</b> &nbsp;•&nbsp; 📍 {location} &nbsp;•&nbsp; 💼 {employment_type}
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.6rem;">
                        <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); color: #34D399; padding: 0.35rem 0.75rem; border-radius: 8px; font-size: 0.95rem; font-weight: 800;">
                            🎯 {match_score}% Match
                        </span>
                        <span style="background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.25); color: #A5B4FC; padding: 0.35rem 0.6rem; border-radius: 8px; font-size: 0.75rem; font-weight: 600;">
                            {source}
                        </span>
                    </div>
                </div>
            </div>
            """).strip()
            st.markdown(card_header_html, unsafe_allow_html=True)

            # Skill Coverage Bar
            col_b1, col_b2 = st.columns([3, 1])
            with col_b1:
                st.progress(skill_coverage / 100.0, text=f"Skill Coverage: {skill_coverage}%")
            with col_b2:
                if job.get("salary_min") or job.get("salary_max"):
                    sal_text = f"💰 ${int(job.get('salary_min', 0)):,} - ${int(job.get('salary_max', 0)):,}" if job.get("salary_max") else f"💰 ${int(job.get('salary_min', 0)):,}"
                    st.caption(sal_text)
                else:
                    st.caption("💰 Competitive Salary")

            # Matched & Missing Skill Chips
            col_sk1, col_sk2 = st.columns(2)
            with col_sk1:
                st.markdown("**Matched Skills**")
                if matched_skills:
                    chips = "".join([f'<span class="skill-chip" style="background: rgba(16, 185, 129, 0.15); border-color: rgba(16, 185, 129, 0.3); color: #34D399;">✔ {s}</span>' for s in matched_skills[:6]])
                    st.markdown(f'<div style="margin-bottom: 0.5rem;">{chips}</div>', unsafe_allow_html=True)
                else:
                    st.markdown("<span style='font-size:0.82rem; color:#94A3B8;'>Semantic Profile Match</span>", unsafe_allow_html=True)

            with col_sk2:
                st.markdown("**Missing Skills (Learning Opportunities)**")
                if missing_skills:
                    chips = "".join([f'<span class="skill-chip" style="background: rgba(245, 158, 11, 0.15); border-color: rgba(245, 158, 11, 0.3); color: #FBBF24;">❌ {s}</span>' for s in missing_skills[:6]])
                    st.markdown(f'<div style="margin-bottom: 0.5rem;">{chips}</div>', unsafe_allow_html=True)
                else:
                    st.markdown("<span style='font-size:0.82rem; color:#34D399;'>100% Skill Requirements Satisfied!</span>", unsafe_allow_html=True)

            # Structured Recommendation Reason Box
            reason_box = textwrap.dedent(f"""
            <div style="background: rgba(17, 24, 39, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 0.75rem 1rem; margin: 0.5rem 0 1rem 0;">
                <div style="font-size: 0.78rem; font-weight: 700; color: #8B5CF6; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">
                    💡 RECOMMENDATION REASON
                </div>
                <div style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.5;">
                    {reason}
                </div>
            </div>
            """).strip()
            st.markdown(reason_box, unsafe_allow_html=True)

            # Action Buttons Row (Apply, Save, Compare, Learning Roadmap)
            btn_c1, btn_c2, btn_c3, btn_c4 = st.columns([1, 1, 1, 1.5])
            
            with btn_c1:
                if redirect_url and redirect_url != "#":
                    st.markdown(f'<a href="{redirect_url}" target="_blank" style="text-decoration:none;"><button style="width:100%; background: linear-gradient(135deg, #10B981 0%, #059669 100%); color:#FFF; border:none; padding:0.5rem; border-radius:6px; font-size:0.82rem; font-weight:700; cursor:pointer;">🚀 Apply Now</button></a>', unsafe_allow_html=True)
                else:
                    if st.button("🚀 Apply Now", key=f"btn_apply_{idx}_{job.get('title')[:5]}"):
                        st.toast("Application portal link initiated.")

            with btn_c2:
                is_saved = title in st.session_state.saved_jobs
                btn_label = "⭐ Saved" if is_saved else "📌 Save Job"
                if st.button(btn_label, key=f"btn_save_{idx}_{job.get('title')[:5]}"):
                    if is_saved:
                        st.session_state.saved_jobs.remove(title)
                        st.toast(f"Removed {title} from saved jobs.")
                    else:
                        st.session_state.saved_jobs.add(title)
                        st.toast(f"Saved {title} to your target list!")
                    st.rerun()

            with btn_c3:
                is_in_comp = any(c.get("title") == title for c in st.session_state.compare_jobs)
                comp_label = "✔ In Compare" if is_in_comp else "⚖️ Compare"
                if st.button(comp_label, key=f"btn_comp_{idx}_{job.get('title')[:5]}"):
                    if not is_in_comp:
                        if len(st.session_state.compare_jobs) >= 4:
                            st.toast("Comparison limit reached (max 4 jobs).")
                        else:
                            st.session_state.compare_jobs.append(job)
                            st.toast(f"Added {title} to comparison drawer!")
                            st.rerun()

            with btn_c4:
                if missing_skills:
                    if st.button("🎓 Bridge via Learning Roadmap", key=f"btn_roadmap_{idx}_{job.get('title')[:5]}"):
                        st.session_state.current_page = "Learning Roadmap"
                        st.rerun()
                else:
                    st.button("✨ Fully Qualified", key=f"btn_qual_{idx}_{job.get('title')[:5]}", disabled=True)

            st.markdown("<div style='margin-bottom: 1.75rem;'></div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
