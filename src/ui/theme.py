import streamlit as st

LIGHT = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* { font-family: 'Inter', system-ui, sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stApp { background: #F8F7FF !important; }
section[data-testid="stSidebar"] { background: #ffffff !important; border-right: 2px solid #EDE9FE; }

/* Hide sidebar nav buttons */
section[data-testid="stSidebar"] .stButton > button {
    opacity: 0 !important; height: 44px !important;
    margin-top: -46px !important; width: 100% !important;
    position: relative !important; z-index: 99 !important;
    cursor: pointer !important; border: none !important;
    background: transparent !important; box-shadow: none !important;
    padding: 0 !important;
}

/* Analyze button */
section[data-testid="stMain"] .stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #5B21B6, #7C3AED) !important;
    color: white !important; border: none !important;
    border-radius: 12px !important; font-weight: 700 !important;
    font-size: 15px !important; padding: 14px !important;
    box-shadow: 0 4px 20px rgba(91,33,182,0.3) !important;
}
section[data-testid="stMain"] .stButton > button {
    border-radius: 10px !important; font-weight: 600 !important;
    border: 1.5px solid #EDE9FE !important;
    background: white !important; color: #5B21B6 !important;
}

.stTabs [data-baseweb="tab-list"] { gap:0; border-bottom:2px solid #EDE9FE; background:transparent; }
.stTabs [data-baseweb="tab"] { background:transparent; color:#94A3B8 !important; font-size:14px !important; font-weight:600 !important; padding:12px 22px !important; border-bottom:3px solid transparent; }
.stTabs [aria-selected="true"] { color:#5B21B6 !important; border-bottom:3px solid #5B21B6 !important; background:transparent !important; }

[data-testid="stFileUploader"] { background:#FAFAFA; border:2px dashed #C4B5FD !important; border-radius:12px !important; padding:8px !important; }
.stTextArea textarea { background:white !important; border:2px solid #EDE9FE !important; border-radius:12px !important; font-size:14px !important; color:#374151 !important; }
.stTextArea textarea:focus { border-color:#8B5CF6 !important; box-shadow:0 0 0 3px rgba(139,92,246,0.15) !important; }
.stProgress > div > div { height:8px; border-radius:8px; }
div[data-testid="stMetric"] { background:white; border:1.5px solid #EDE9FE; border-radius:12px; padding:18px; box-shadow:0 2px 12px rgba(91,33,182,0.07); }
details summary { background:white !important; border:1.5px solid #EDE9FE !important; border-radius:12px !important; font-weight:700 !important; font-size:14px !important; color:#111827 !important; padding:14px 16px !important; }
.chip { display:inline-block; padding:5px 14px; border-radius:20px; font-size:12px; font-weight:600; margin:3px; }
.chip-green { background:#DCFCE7; color:#15803D; border:1px solid #BBF7D0; }
.chip-red   { background:#FEE2E2; color:#B91C1C; border:1px solid #FECACA; }
</style>
"""

DARK = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* { font-family: 'Inter', system-ui, sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Base dark ── */
.stApp { background: #0D1117 !important; }
.stApp, .stApp p, .stApp span, .stApp div, .stApp label { color: #E2E8F0 !important; }
h1, h2, h3, h4, h5, h6 { color: #F1F5F9 !important; }

section[data-testid="stSidebar"] { background: #161B22 !important; border-right: 2px solid #21262D; }
section[data-testid="stSidebar"] * { color: #C9D1D9 !important; }
section[data-testid="stSidebar"] .stButton > button {
    opacity: 0 !important; height: 44px !important;
    margin-top: -46px !important; width: 100% !important;
    position: relative !important; z-index: 99 !important;
    cursor: pointer !important; border: none !important;
    background: transparent !important; box-shadow: none !important; padding: 0 !important;
}

/* ── Dark cards via HTML ── */
.dark-card { background: #1C2128 !important; border-color: #30363D !important; }

section[data-testid="stMain"] .stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7C3AED, #A855F7) !important;
    color: white !important; border: none !important;
    border-radius: 12px !important; font-weight: 700 !important;
    font-size: 15px !important; padding: 14px !important;
    box-shadow: 0 4px 20px rgba(124,58,237,0.4) !important;
}
section[data-testid="stMain"] .stButton > button {
    border-radius: 10px !important; font-weight: 600 !important;
    border: 1.5px solid #30363D !important;
    background: #1C2128 !important; color: #A78BFA !important;
}

.stTabs [data-baseweb="tab-list"] { gap:0; border-bottom:2px solid #21262D; background:transparent; }
.stTabs [data-baseweb="tab"] { background:transparent !important; color:#8B949E !important; font-size:14px !important; font-weight:600 !important; padding:12px 22px !important; border-bottom:3px solid transparent; }
.stTabs [aria-selected="true"] { color:#A78BFA !important; border-bottom:3px solid #A78BFA !important; background:transparent !important; }

[data-testid="stFileUploader"] { background:#1C2128 !important; border:2px dashed #30363D !important; border-radius:12px !important; padding:8px !important; }
[data-testid="stFileUploader"] * { color:#C9D1D9 !important; }
[data-testid="stFileUploader"] button { background:#21262D !important; color:#A78BFA !important; border:1px solid #30363D !important; }

.stTextArea textarea { background:#1C2128 !important; border:2px solid #30363D !important; border-radius:12px !important; font-size:14px !important; color:#C9D1D9 !important; }
.stTextArea textarea:focus { border-color:#7C3AED !important; box-shadow:0 0 0 3px rgba(124,58,237,0.2) !important; }
.stTextArea textarea::placeholder { color:#484F58 !important; }

.stProgress > div > div { height:8px; border-radius:8px; }
.stProgress > div { background:#21262D !important; }

div[data-testid="stMetric"] { background:#1C2128 !important; border:1.5px solid #30363D !important; border-radius:12px !important; padding:18px !important; }
div[data-testid="stMetric"] * { color:#E2E8F0 !important; }
div[data-testid="stMetricValue"] { color:#F1F5F9 !important; }

details summary { background:#1C2128 !important; border:1.5px solid #30363D !important; border-radius:12px !important; font-weight:700 !important; font-size:14px !important; color:#F1F5F9 !important; padding:14px 16px !important; }
details { background:#161B22 !important; border:1px solid #21262D !important; border-radius:12px !important; }

/* Success / warning / info */
div[data-testid="stAlert"] { background:#1C2128 !important; border-color:#30363D !important; border-radius:12px !important; }
div[data-testid="stAlert"] * { color:#E2E8F0 !important; }

.chip { display:inline-block; padding:5px 14px; border-radius:20px; font-size:12px; font-weight:600; margin:3px; }
.chip-green { background:#0D4429 !important; color:#3FB950 !important; border:1px solid #238636 !important; }
.chip-red   { background:#3D0C0C !important; color:#FF7B72 !important; border:1px solid #6E2C2C !important; }

/* Toggle */
.stToggle label { color:#C9D1D9 !important; }
</style>
"""

def apply_theme(dark_mode: bool):
    st.markdown(DARK if dark_mode else LIGHT, unsafe_allow_html=True)
    if dark_mode:
        # Inject dark hero/card colors
        st.markdown("""
        <style>
        .hero-title { color: #F1F5F9 !important; }
        .hero-sub   { color: #8B949E !important; }
        .score-wrap, .ph-wrap, .feat-card, .upload-wrap, .cp-card, .sb-pro-card {
            background: #1C2128 !important;
            border-color: #30363D !important;
        }
        .feat-title { color: #A78BFA !important; }
        .feat-desc  { color: #8B949E !important; }
        .score-lbl  { color: #8B949E !important; }
        .score-msg  { background: #21262D !important; }
        .ph-title   { color: #A78BFA !important; }
        .ph-sub     { color: #8B949E !important; }
        .upload-header { color: #F1F5F9 !important; }
        .upload-sub    { color: #8B949E !important; }
        .col-label     { color: #C9D1D9 !important; }
        .cp-metric-label { color: #8B949E !important; }
        .cp-metric-sub   { color: #8B949E !important; }
        .motiv-banner { background: linear-gradient(135deg,#1C2128,#21262D) !important; border-color:#30363D !important; }
        </style>
        """, unsafe_allow_html=True)