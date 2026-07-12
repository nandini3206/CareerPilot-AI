import streamlit as st


def _score_ring(score: float):
    score = float(score)
    if score >= 85:
        color, label, bg = "#22C55E", "Excellent!", "#F0FDF4"
    elif score >= 70:
        color, label, bg = "#8B5CF6", "Good Match", "#F5F3FF"
    else:
        color, label, bg = "#EF4444", "Keep Going!", "#FEF2F2"

    circ = 251.3
    offset = circ * (1 - score / 100)

    st.markdown(f"""
    <style>
    @keyframes ringIn {{
        from {{ stroke-dashoffset: {circ:.1f}; }}
        to   {{ stroke-dashoffset: {offset:.1f}; }}
    }}
    @keyframes cardIn {{
        from {{ opacity:0; transform:translateY(10px); }}
        to   {{ opacity:1; transform:translateY(0); }}
    }}
    .score-wrap {{
        background: white;
        border: 2px solid #EDE9FE;
        border-radius: 20px;
        padding: 24px 20px 20px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(91,33,182,0.12);
        animation: cardIn 0.6s ease-out;
    }}
    .score-lbl {{
        font-size: 12px; font-weight: 700; color: #9ca3af;
        text-transform: uppercase; letter-spacing: .08em; margin-bottom: 14px;
    }}
    .ring-anim {{
        stroke-dashoffset: {circ:.1f};
        animation: ringIn 1.4s cubic-bezier(.4,0,.2,1) forwards 0.3s;
    }}
    .score-msg {{
        background: {bg}; border-radius: 10px;
        padding: 10px 14px; font-size: 13px;
        color: {color}; font-weight: 600;
        margin-top: 12px; line-height: 1.5;
    }}
    </style>
    <div class="score-wrap">
        <div class="score-lbl">Overall Match Score</div>
        <svg viewBox="0 0 100 100" width="150" height="150" style="display:block;margin:0 auto 4px;">
            <circle cx="50" cy="50" r="40" fill="none" stroke="#F3F4F6" stroke-width="9"/>
            <circle cx="50" cy="50" r="40" fill="none" stroke="{color}" stroke-width="9"
                stroke-dasharray="{circ:.1f}"
                stroke-linecap="round"
                transform="rotate(-90 50 50)"
                class="ring-anim"/>
            <text x="50" y="44" text-anchor="middle"
                font-size="19" font-weight="800" fill="#111827"
                font-family="system-ui,sans-serif">{int(score)}%</text>
            <text x="50" y="60" text-anchor="middle"
                font-size="9" font-weight="700" fill="{color}"
                font-family="system-ui,sans-serif">{label}</text>
        </svg>
        <div class="score-msg">{_score_tip(score)}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    st.button("📊 View Full Analysis →", use_container_width=True, key="view_btn")


def _score_tip(score):
    if score >= 85: return "🎉 Outstanding! You're a top candidate for this role."
    if score >= 70: return "👍 Good fit! Focus on missing skills to boost your score."
    return "💪 Work on the missing skills and AI suggestions to improve."


def _placeholder():
    st.markdown("""
    <style>
    @keyframes float {
        0%,100% { transform: translateY(0px); }
        50%      { transform: translateY(-10px); }
    }
    @keyframes pulse {
        0%,100% { box-shadow: 0 8px 32px rgba(91,33,182,0.12); }
        50%      { box-shadow: 0 8px 40px rgba(91,33,182,0.22); }
    }
    .ph-wrap {
        background: white; border: 2px dashed #C4B5FD;
        border-radius: 20px; padding: 32px 20px;
        text-align: center; min-height: 290px;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        animation: pulse 3s ease-in-out infinite;
    }
    .ph-icon  { font-size:52px; animation: float 2.8s ease-in-out infinite; margin-bottom:16px; }
    .ph-title { font-size:16px; font-weight:800; color:#5B21B6; margin-bottom:8px; }
    .ph-sub   { font-size:13px; color:#9ca3af; line-height:1.7; }
    </style>
    <div class="ph-wrap">
        <div class="ph-icon">🚀</div>
        <div class="ph-title">Overall Match Score</div>
        <div class="ph-sub">Upload your resume and paste a<br>job description to see your score</div>
    </div>
    """, unsafe_allow_html=True)


def show_hero():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    .stApp, .stApp * { font-family: 'Inter', system-ui, sans-serif !important; }

    @keyframes heroIn {
        from { opacity:0; transform: translateY(20px); }
        to   { opacity:1; transform: translateY(0); }
    }
    @keyframes tagIn {
        from { opacity:0; transform: translateX(-10px); }
        to   { opacity:1; transform: translateX(0); }
    }

    .hero-main { animation: heroIn 0.5s ease-out; }

    .hero-title {
        font-size: 40px !important;
        font-weight: 900 !important;
        color: #0F172A !important;
        letter-spacing: -1px;
        line-height: 1.15;
        margin-bottom: 6px;
    }
    .hero-sub {
        font-size: 16px;
        color: #64748B;
        font-weight: 400;
        margin-bottom: 10px;
    }
    .hero-tag {
        font-size: 15px;
        font-weight: 700;
        margin-bottom: 0;
        animation: tagIn 0.6s ease-out 0.1s both;
    }
    .t1{color:#5B21B6} .t2{color:#7C3AED} .t3{color:#EC4899} .t4{color:#D97706}

    /* Feature cards */
    .feat-outer { margin-top: 20px; }
    .feat-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
    }
    .feat-card {
        background: white;
        border: 1.5px solid #EDE9FE;
        border-radius: 14px;
        padding: 18px 12px 14px;
        text-align: center;
        box-shadow: 0 2px 12px rgba(91,33,182,0.07);
        cursor: default;
        transition: all 0.25s ease;
        animation: heroIn 0.5s ease-out both;
    }
    .feat-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 28px rgba(91,33,182,0.15);
        border-color: #C4B5FD;
    }
    .feat-card:nth-child(1) { animation-delay: 0.05s; }
    .feat-card:nth-child(2) { animation-delay: 0.10s; }
    .feat-card:nth-child(3) { animation-delay: 0.15s; }
    .feat-card:nth-child(4) { animation-delay: 0.20s; }

    .feat-icon  { font-size: 28px; margin-bottom: 10px; }
    .feat-title {
        font-size: 13px; font-weight: 700;
        color: #5B21B6; margin-bottom: 4px;
    }
    .feat-desc { font-size: 12px; color: #94A3B8; line-height: 1.5; }
    </style>
    """, unsafe_allow_html=True)

    left, right = st.columns([3, 2], gap="large")

    with left:
        st.markdown("""
        <div class="hero-main">
            <div class="hero-title">🚀 CareerPilot AI</div>
            <div class="hero-sub">Your Personal AI Career Mentor</div>
            <div class="hero-tag">
                <span class="t1">Analyze</span> &nbsp;•&nbsp;
                <span class="t2">Improve</span> &nbsp;•&nbsp;
                <span class="t3">Prepare</span> &nbsp;•&nbsp;
                <span class="t4">Get Hired</span>
            </div>
        </div>
        <div class="feat-outer">
        <div class="feat-grid">
            <div class="feat-card">
                <div class="feat-icon">🤖</div>
                <div class="feat-title">Smart Analysis</div>
                <div class="feat-desc">AI-powered resume scoring</div>
            </div>
            <div class="feat-card">
                <div class="feat-icon">🎯</div>
                <div class="feat-title">Skill Match</div>
                <div class="feat-desc">Compare with job description</div>
            </div>
            <div class="feat-card">
                <div class="feat-icon">💡</div>
                <div class="feat-title">AI Feedback</div>
                <div class="feat-desc">Personalized improvement tips</div>
            </div>
            <div class="feat-card">
                <div class="feat-icon">🎤</div>
                <div class="feat-title">Interview Prep</div>
                <div class="feat-desc">Curated interview questions</div>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        if "careerpilot_score" in st.session_state:
            _score_ring(st.session_state["careerpilot_score"])
        else:
            _placeholder()

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    st.markdown("<hr style='border:none;border-top:2px solid #EDE9FE;margin:0 0 20px 0'>", unsafe_allow_html=True)