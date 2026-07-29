import streamlit as st
from components.cards import hero_header, empty_state_card
from components.metrics import kpi_card

@st.cache_resource
def get_learning_inference():
    """
    Cached getter for the frozen LearningRoadmapInference backend.
    """
    try:
        from learning_roadmap.inference import LearningRoadmapInference
        return LearningRoadmapInference()
    except Exception as e:
        st.error(f"Error loading Learning Roadmap Engine: {e}")
        return None

def show_learning_roadmap():
    """
    Renders the Learning Studio view controller.
    Driven 100% by outputs from the frozen Learning Roadmap backend.
    """
    # =========================================================
    # SECTION 1: HERO SECTION
    # =========================================================
    hero_header(
        title="📚 Learning Studio",
        subtitle="Personalized AI-powered learning roadmap based on your target career role and current skill set.",
        icon="📚"
    )

    resume_text = st.session_state.get("resume_text", "")
    resume_uploaded = st.session_state.get("resume_uploaded", False)

    # Infer target role and extracted skills from session state
    role_preds = st.session_state.get("role_prediction_results", [])
    default_role = role_preds[0]["role"] if role_preds else "Machine Learning Engineer"

    user_skills = st.session_state.get("extracted_skills", [
        "Python", "SQL", "Pandas"
    ])

    if not resume_uploaded and not role_preds:
        empty_state_card(
            title="No Learning Roadmap Available",
            message="Please complete Role Prediction and Resume Analysis first to generate your personalized learning roadmap.",
            icon="📄"
        )
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            if st.button(" Go to Resume Analysis ➔", key="btn_learn_no_profile", type="primary"):
                st.session_state.current_page = "Resume Analysis"
                st.rerun()
        return

    # Role Selector Dropdown
    st.markdown("### 🎯 Target Career Role & Skill Profile")
    available_roles = ["Machine Learning Engineer", "Data Scientist", "Data Analyst"]
    
    selected_role = st.selectbox(
        "Target Role",
        options=available_roles,
        index=available_roles.index(default_role) if default_role in available_roles else 0,
        key="sel_learning_target_role"
    )

    # Fetch roadmap from frozen backend
    inference = get_learning_inference()
    roadmap_data = None
    if inference:
        try:
            roadmap_data = inference.predict(selected_role, user_skills)
        except Exception as e:
            st.error(f"Error generating learning roadmap: {e}")

    if not roadmap_data:
        empty_state_card(
            title="No Learning Roadmap Data",
            message="No learning roadmap available. Please complete Role Prediction and Resume Analysis first.",
            icon="⚠️"
        )
        return

    target_role = roadmap_data.get("target_role", selected_role)
    missing_skills = roadmap_data.get("missing_skills", [])
    weekly_plan = roadmap_data.get("weekly_plan", {})
    recommended_projects = roadmap_data.get("recommended_projects", [])

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 2: LEARNING ROADMAP OVERVIEW METRICS
    # =========================================================
    st.markdown("### 📊 Learning Roadmap Overview")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        kpi_card(
            label="🎯 Target Role",
            value=target_role,
            subtext="Active Goal",
            accent_color="#6366F1"
        )
    with m2:
        kpi_card(
            label="⚠️ Missing Skills",
            value=f"{len(missing_skills)} Skills",
            subtext="Identified Gaps",
            accent_color="#EF4444"
        )
    with m3:
        kpi_card(
            label="📅 Total Duration",
            value=f"{len(weekly_plan)} Weeks",
            subtext="Paced Plan",
            accent_color="#8B5CF6"
        )
    with m4:
        kpi_card(
            label="🛠️ Portfolio Projects",
            value=f"{len(recommended_projects)} Projects",
            subtext="Portfolio Items",
            accent_color="#10B981"
        )

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 3: SKILL GAP ANALYSIS
    # =========================================================
    st.markdown("### 🔍 Skill Gap Analysis")
    st.markdown("<p style='color: #94A3B8; font-size: 0.9rem; margin-bottom: 1rem;'>Skills required for target role mastery that are missing from your current profile.</p>", unsafe_allow_html=True)

    if missing_skills:
        skill_chips_html = "".join([
            f'<div style="background: rgba(239, 68, 68, 0.12); border: 1px solid rgba(239, 68, 68, 0.4); color: #FCA5A5; font-weight: 700; padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.9rem; display: inline-block; margin-right: 0.5rem; margin-bottom: 0.5rem;">⚡ {skill}</div>'
            for skill in missing_skills
        ])
        st.markdown(f'<div style="margin-bottom: 2rem;">{skill_chips_html}</div>', unsafe_allow_html=True)
    else:
        st.success("🎉 Outstanding! You already possess all key skills for this target role!")

    st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 4: WEEKLY LEARNING TIMELINE
    # =========================================================
    st.markdown("### 📅 Weekly Learning Timeline")
    st.markdown("<p style='color: #94A3B8; font-size: 0.9rem; margin-bottom: 1.25rem;'>Structured week-by-week skill acquisition roadmap.</p>", unsafe_allow_html=True)

    if weekly_plan:
        for week_title, topics in weekly_plan.items():
            topics_html = "".join([
                f'<div style="color: #CBD5E1; font-size: 0.95rem; margin-bottom: 0.35rem; display: flex; align-items: center; gap: 0.5rem;">'
                f'<span style="color: #6366F1; font-weight: 900;">•</span> <b>{topic}</b>'
                f'</div>'
                for topic in topics
            ])

            week_card_html = f"""<div class="glass-panel" style="padding: 1.25rem 1.5rem; margin-bottom: 1rem; border-left: 4px solid #6366F1;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
<div style="font-size: 1.15rem; font-weight: 800; color: #F8FAFC; display: flex; align-items: center; gap: 0.5rem;">
<span>🗓️</span> {week_title}
</div>
<span class="skill-chip" style="background: rgba(99, 102, 241, 0.2); color: #A5B4FC; border-color: rgba(99, 102, 241, 0.4); font-size: 0.78rem;">
{len(topics)} Focus Module{"s" if len(topics) > 1 else ""}
</span>
</div>
<div>{topics_html}</div>
</div>"""
            st.markdown(week_card_html, unsafe_allow_html=True)
    else:
        st.info("No weekly plan needed for this profile.")

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 5: RECOMMENDED PORTFOLIO PROJECTS
    # =========================================================
    st.markdown("### 🛠️ Recommended Portfolio Projects")
    st.markdown("<p style='color: #94A3B8; font-size: 0.9rem; margin-bottom: 1.25rem;'>Practical hands-on projects to demonstrate competence for your target role.</p>", unsafe_allow_html=True)

    if recommended_projects:
        p1, p2, p3 = st.columns(3)
        cols = [p1, p2, p3]
        project_icons = ["💻", "📊", "🚀", "⚡", "🤖"]

        for idx, project_name in enumerate(recommended_projects):
            col = cols[idx % 3]
            icon = project_icons[idx % len(project_icons)]

            with col:
                project_card_html = f"""<div class="glass-panel" style="padding: 1.5rem; margin-bottom: 1.25rem; text-align: center; height: 100%;">
<div style="font-size: 2.2rem; margin-bottom: 0.5rem;">{icon}</div>
<h4 style="color: #F8FAFC; font-size: 1.1rem; font-weight: 800; margin-bottom: 0.75rem;">{project_name}</h4>
<span class="skill-chip" style="background: rgba(16, 185, 129, 0.15); color: #34D399; border-color: rgba(16, 185, 129, 0.4); font-size: 0.75rem;">
🎯 {target_role}
</span>
</div>"""
                st.markdown(project_card_html, unsafe_allow_html=True)
    else:
        st.info("No project recommendations returned for this role.")

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # SECTION 6: LEARNING WORKFLOW (EXPLANATORY PIPELINE)
    # =========================================================
    st.markdown("### ⚙️ Learning Roadmap Engine Pipeline")
    
    pipeline_html = """<div class="glass-panel" style="padding: 1.75rem 2rem; margin-bottom: 2rem;">
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; text-align: center;">
<div style="flex: 1; min-width: 140px;">
<div style="font-size: 1.5rem;">📄</div>
<div style="font-weight: 700; color: #F8FAFC; font-size: 0.9rem;">Resume Skills</div>
<div style="font-size: 0.75rem; color: #94A3B8;">Candidate Profile</div>
</div>
<div style="color: #6366F1; font-weight: 900; font-size: 1.2rem;">➔</div>
<div style="flex: 1; min-width: 140px;">
<div style="font-size: 1.5rem;">⚡</div>
<div style="font-weight: 700; color: #F8FAFC; font-size: 0.9rem;">Skill Gap Analysis</div>
<div style="font-size: 0.75rem; color: #94A3B8;">Taxonomy Difference</div>
</div>
<div style="color: #6366F1; font-weight: 900; font-size: 1.2rem;">➔</div>
<div style="flex: 1; min-width: 140px;">
<div style="font-size: 1.5rem;">📅</div>
<div style="font-weight: 700; color: #F8FAFC; font-size: 0.9rem;">Weekly Learning Plan</div>
<div style="font-size: 0.75rem; color: #94A3B8;">Paced Allocation</div>
</div>
<div style="color: #6366F1; font-weight: 900; font-size: 1.2rem;">➔</div>
<div style="flex: 1; min-width: 140px;">
<div style="font-size: 1.5rem;">🛠️</div>
<div style="font-weight: 700; color: #F8FAFC; font-size: 0.9rem;">Portfolio Projects</div>
<div style="font-size: 0.75rem; color: #94A3B8;">Role Portfolio</div>
</div>
</div>
</div>"""
    st.markdown(pipeline_html, unsafe_allow_html=True)

    # Next CTA
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("Continue to Interview Prep ➔", key="btn_learn_to_interview", type="primary"):
            st.session_state.current_page = "Interview Questions"
            st.rerun()
