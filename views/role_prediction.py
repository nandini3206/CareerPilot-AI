import textwrap
import time
import streamlit as st
from components.cards import hero_header, empty_state_card
from role_prediction.predictor import RolePredictor
from role_prediction.explain import explain_prediction

@st.cache_resource
def get_role_predictor():
    return RolePredictor()

def show_role_prediction():
    """
    Renders the Career Intelligence Studio (Role Prediction) view controller.
    Driven by frozen backend outputs (RolePredictor & explain_prediction).
    """
    # =========================================================
    # 1. PURPLE HERO BANNER
    # =========================================================
    hero_header(
        title="Career Intelligence Studio",
        subtitle="AI-powered career matching to discover your optimal professional trajectory based on your background and skills.",
        icon="🎯"
    )

    resume_text = st.session_state.get("resume_text", "")
    resume_uploaded = st.session_state.get("resume_uploaded", False)

    if not resume_uploaded or not resume_text.strip():
        empty_state_card(
            title="No Active Resume Detected",
            message="Please upload a PDF resume in the Resume Studio or Home page first to generate AI career role predictions.",
            icon="📄"
        )
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(" Go to Resume Analysis ➔", key="btn_go_resume_analysis", type="primary"):
                st.session_state.current_page = "Resume Analysis"
                st.rerun()
        return

    # =========================================================
    # 2. WORKFLOW ANIMATION & PREDICTION EXECUTION
    # =========================================================
    predictor = get_role_predictor()

    if "role_prediction_results" not in st.session_state or st.session_state.get("predicted_for_resume") != st.session_state.get("resume_file_name"):
        st.markdown("### 🤖 AI Career Coach Analysis")
        progress_bar = st.progress(0)
        status_text = st.empty()

        workflow_stages = [
            (15, "✓ Reading Resume & Extracting Context..."),
            (35, "✓ Analyzing Key Skills & Competencies..."),
            (55, "✓ Evaluating Professional Background..."),
            (75, "✓ Matching Candidate Career Profile..."),
            (90, "✓ Ranking Optimal Target Roles..."),
            (100, "✓ Preparing AI Career Guidance..."),
        ]

        for pct, stage_msg in workflow_stages:
            status_text.markdown(f"<span style='color: #A5B4FC; font-weight: 600;'>{stage_msg}</span>", unsafe_allow_html=True)
            progress_bar.progress(pct)
            time.sleep(0.04)

        # Execute frozen backend model
        predictions = predictor.predict_top_k(resume_text, k=3)
        st.session_state["role_prediction_results"] = predictions
        st.session_state["predicted_for_resume"] = st.session_state.get("resume_file_name", "active_resume")
        
        status_text.empty()
        progress_bar.empty()
        st.rerun()

    predictions = st.session_state.get("role_prediction_results", [])
    if not predictions:
        st.error("Unable to generate role predictions from the provided resume text.")
        return

    primary_prediction = predictions[0]
    primary_role = primary_prediction["role"]
    primary_confidence = primary_prediction["confidence"]

    primary_explanation = explain_prediction(primary_role)
    primary_description = primary_explanation.get("description", "")

    # Role Icon Mapping
    role_icons = {
        "Machine Learning Engineer": "🤖",
        "Data Scientist": "📊",
        "AI Engineer": "⚡",
        "Data Engineer": "⚙️",
        "Backend Developer": "💻",
        "Full Stack Engineer": "🌐",
        "DevOps & Cloud Engineer": "☁️",
        "UI/UX & Product Designer": "🎨",
        "Software Engineer": "🛠️",
    }
    primary_icon = role_icons.get(primary_role, "💼")

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 3. HERO PREDICTION CARD (SPOTLIGHT MATCH)
    # =========================================================
    st.markdown("### 🏆 Top Predicted Career Role")

    hero_card_html = f"""<div class="glass-panel" style="background: linear-gradient(135deg, rgba(147, 51, 234, 0.18) 0%, rgba(99, 102, 241, 0.12) 100%); border: 1.5px solid rgba(168, 85, 247, 0.4); padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
<div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
<div>
<span class="skill-chip" style="background: rgba(168, 85, 247, 0.25); border-color: rgba(168, 85, 247, 0.5); color: #E9D5FF; font-weight: 700; padding: 0.35rem 0.85rem; margin-bottom: 0.75rem; display: inline-block;">
🌟 Primary Career Match
</span>
<h1 style="font-size: 2.25rem; font-weight: 800; color: #F8FAFC; margin: 0.25rem 0 0.5rem 0; display: flex; align-items: center; gap: 0.75rem;">
<span>{primary_icon}</span> {primary_role}
</h1>
<p style="color: #CBD5E1; font-size: 1rem; max-width: 680px; line-height: 1.6; margin-top: 0.5rem;">
{primary_description}
</p>
</div>
<div style="text-align: right; background: rgba(15, 23, 42, 0.6); padding: 1.25rem 1.5rem; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.1); min-width: 180px;">
<div style="font-size: 0.75rem; text-transform: uppercase; color: #A7F3D0; font-weight: 700; letter-spacing: 0.05em;">
Match Confidence
</div>
<div style="font-size: 2.5rem; font-weight: 900; color: #34D399; margin: 0.2rem 0;">
{primary_confidence:.1f}%
</div>
<div style="font-size: 0.78rem; color: #94A3B8;">
High Alignment
</div>
</div>
</div>
</div>"""

    st.markdown(hero_card_html, unsafe_allow_html=True)

    # =========================================================
    # 4. TOP-3 CAREER MATCHES
    # =========================================================
    st.markdown("### 🎯 Top 3 Recommended Roles")
    st.markdown("<p style='color: #94A3B8; font-size: 0.92rem; margin-bottom: 1.25rem;'>Based on comparative skill evaluation and profile alignment.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]

    for idx, match in enumerate(predictions):
        role_name = match["role"]
        conf = match["confidence"]
        explanation = explain_prediction(role_name)
        desc = explanation.get("description", "")
        icon = role_icons.get(role_name, "💼")
        is_top = (idx == 0)

        border_style = "border: 1.5px solid rgba(168, 85, 247, 0.5);" if is_top else ""
        badge_html = '<span style="background: rgba(16, 185, 129, 0.2); color: #34D399; font-size: 0.72rem; font-weight: 700; padding: 0.25rem 0.5rem; border-radius: 4px; float: right;">★ BEST MATCH</span>' if is_top else ''

        with cols[idx]:
            card_html = f"""<div class="glass-panel" style="{border_style} padding: 1.25rem; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
<div>
{badge_html}
<div style="font-size: 1.75rem; margin-bottom: 0.5rem;">{icon}</div>
<div style="font-weight: 700; font-size: 1.1rem; color: #F8FAFC; margin-bottom: 0.4rem;">
{role_name}
</div>
<div style="font-size: 0.85rem; color: #94A3B8; line-height: 1.5; margin-bottom: 1rem;">
{desc}
</div>
</div>
<div>
<div style="display: flex; justify-content: space-between; font-size: 0.82rem; font-weight: 600; margin-bottom: 0.35rem;">
<span style="color: #CBD5E1;">Match Probability</span>
<span style="color: #A7F3D0;">{conf:.1f}%</span>
</div>
<div style="background: rgba(255, 255, 255, 0.1); height: 8px; border-radius: 4px; overflow: hidden;">
<div style="background: linear-gradient(90deg, #6366F1 0%, #A855F7 100%); width: {conf}%; height: 100%; border-radius: 4px;"></div>
</div>
</div>
</div>"""
            st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 5. WHY THIS ROLE? (CAREER COACH INSIGHTS)
    # =========================================================
    st.markdown("### 💡 Why This Role Fits You")

    why_html = f"""<div class="glass-panel" style="border-left: 4px solid #A855F7; padding: 1.5rem;">
<div style="font-weight: 700; font-size: 1.1rem; color: #F8FAFC; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
<span>🤖</span> AI Career Alignment Overview
</div>
<p style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.7; margin: 0;">
{primary_description}
</p>
</div>"""

    st.markdown(why_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # 6. NEXT STEP CTA WORKFLOW
    # =========================================================
    cta_html = f"""<div class="hero-container" style="text-align: center; padding: 2.25rem 2rem;">
<h3 style="margin-bottom: 0.5rem; color: #F8FAFC;">💰 Ready to Predict Your Market Salary Range?</h3>
<p style="color: #94A3B8; font-size: 0.95rem; margin-bottom: 1.5rem; max-width: 600px; margin-left: auto; margin-right: auto;">
Now that your top role profile is identified, evaluate expected compensation benchmarks tailored to your skill set and domain experience.
</p>
</div>"""
    st.markdown(cta_html, unsafe_allow_html=True)

    c_btn1, c_btn2, c_btn3 = st.columns([1, 2, 1])
    with c_btn2:
        if st.button("Continue to Salary Prediction ➔", key="btn_next_salary", type="primary"):
            st.session_state.current_page = "Salary Prediction"
            st.rerun()
