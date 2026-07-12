import streamlit as st
from datetime import datetime


def _card(icon, label, value_html, status, status_color, sub, bar_color, bar_pct):
    return f"""
    <div style="background:white;border:1.5px solid #EDE9FE;border-radius:12px;padding:16px 14px;
                box-shadow:0 2px 8px rgba(91,33,182,0.07);height:100%;">
        <div style="font-size:22px;margin-bottom:6px;">{icon}</div>
        <div style="font-size:11px;color:#9ca3af;font-weight:500;margin-bottom:4px;text-transform:uppercase;letter-spacing:.04em;">{label}</div>
        <div style="font-size:24px;font-weight:800;color:#111827;margin-bottom:2px;">{value_html}</div>
        <div style="font-size:12px;font-weight:600;color:{status_color};margin-bottom:4px;">{status}</div>
        <div style="font-size:11px;color:#9ca3af;">{sub}</div>
        <div style="background:#f3f4f6;border-radius:4px;height:5px;margin-top:10px;overflow:hidden;">
            <div style="width:{min(bar_pct,100)}%;height:5px;border-radius:4px;background:{bar_color};"></div>
        </div>
    </div>
    """


def show_metrics(careerpilot_score, ats_score, skill_percentage, resume_quality,
                 matching_count=0, missing_count=0, sections_found=0):

    careerpilot_score = float(careerpilot_score)
    ats_score         = float(ats_score)
    skill_percentage  = float(skill_percentage)
    resume_quality    = float(resume_quality)

    st.markdown("""
    <div style="font-size:16px;font-weight:700;color:#111827;margin-bottom:2px;">📊 Dashboard Overview</div>
    <div style="font-size:12px;color:#9ca3af;margin-bottom:16px;">Quick summary of your resume analysis</div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="small")

    # ATS Score
    ats_lbl = "Excellent" if ats_score >= 80 else ("Good" if ats_score >= 65 else "Needs Work")
    ats_clr = "#16A34A" if ats_score >= 80 else ("#D97706" if ats_score >= 65 else "#DC2626")
    ats_bar = "#22C55E" if ats_score >= 80 else ("#F59E0B" if ats_score >= 65 else "#EF4444")
    ats_sub = "Top 15% applicants" if ats_score >= 80 else "Room to improve"
    with c1:
        st.markdown(_card("🎯","ATS Score",f"{ats_score:.0f}%",ats_lbl,ats_clr,ats_sub,ats_bar,ats_score), unsafe_allow_html=True)

    # Skill Match
    total  = matching_count + missing_count
    sk_lbl = "Good Match" if skill_percentage >= 70 else ("Partial Match" if skill_percentage >= 50 else "Low Match")
    sk_clr = "#16A34A" if skill_percentage >= 70 else ("#D97706" if skill_percentage >= 50 else "#DC2626")
    sk_bar = "#22C55E" if skill_percentage >= 70 else ("#F59E0B" if skill_percentage >= 50 else "#EF4444")
    with c2:
        st.markdown(_card("✅","Skill Match",f"{skill_percentage:.0f}%",sk_lbl,sk_clr,f"{matching_count} / {total} skills matched",sk_bar,skill_percentage), unsafe_allow_html=True)

    # Missing Skills
    with c3:
        st.markdown(_card("❌","Missing Skills",str(missing_count),"Need Improvement","#DC2626","High priority skills","#EF4444",min(missing_count*6,100)), unsafe_allow_html=True)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    c4, c5, c6 = st.columns(3, gap="small")

    # Resume Quality
    rq_lbl = "Very Good" if resume_quality >= 80 else ("Good" if resume_quality >= 65 else "Needs Work")
    rq_clr = "#16A34A" if resume_quality >= 80 else ("#D97706" if resume_quality >= 65 else "#DC2626")
    rq_bar = "#14B8A6" if resume_quality >= 80 else ("#F59E0B" if resume_quality >= 65 else "#EF4444")
    with c4:
        st.markdown(_card("📄","Resume Quality",f"{resume_quality:.0f}%",rq_lbl,rq_clr,"Well structured",rq_bar,resume_quality), unsafe_allow_html=True)

    # Sections Found
    sf_lbl = "Almost Complete" if sections_found >= 8 else ("Good" if sections_found >= 6 else "Incomplete")
    sf_clr = "#16A34A" if sections_found >= 8 else ("#D97706" if sections_found >= 6 else "#DC2626")
    with c5:
        st.markdown(_card("📋","Sections Found",f'{sections_found} <span style="font-size:14px;color:#9ca3af;font-weight:400">/ 10</span>',sf_lbl,sf_clr,"Missing: Certifications","#6366F1",sections_found*10), unsafe_allow_html=True)

    # Analysis Date
    now = datetime.now()
    with c6:
        st.markdown(f"""
        <div style="background:white;border:1.5px solid #EDE9FE;border-radius:12px;padding:16px 14px;
                    box-shadow:0 2px 8px rgba(91,33,182,0.07);height:100%;">
            <div style="font-size:22px;margin-bottom:6px;">📅</div>
            <div style="font-size:11px;color:#9ca3af;font-weight:500;margin-bottom:4px;text-transform:uppercase;letter-spacing:.04em;">Analysis Date</div>
            <div style="font-size:20px;font-weight:800;color:#111827;margin-bottom:2px;">{now.strftime("%d %b %Y")}</div>
            <div style="font-size:12px;color:#6b7280;">{now.strftime("%I:%M %p")}</div>
            <div style="font-size:11px;color:#9ca3af;margin-top:4px;">Just now</div>
            <div style="background:#f3f4f6;border-radius:4px;height:5px;margin-top:10px;overflow:hidden;">
                <div style="width:100%;height:5px;border-radius:4px;background:#8B5CF6;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Motivational banner
    st.markdown("""
    <div style="background:linear-gradient(135deg,#f5f3ff,#ede9fe);border:1.5px solid #ddd6fe;
                border-radius:12px;padding:18px 22px;display:flex;align-items:center;
                gap:14px;margin-top:14px;">
        <span style="font-size:36px;">🚀</span>
        <div>
            <div style="font-size:15px;font-weight:700;color:#5B21B6;">Keep learning, keep improving, keep growing!</div>
            <div style="font-size:12px;color:#7C3AED;margin-top:3px;">You're on your way to landing your dream job. Stay consistent!</div>
        </div>
    </div>
    """, unsafe_allow_html=True)