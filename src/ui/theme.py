import streamlit as st

LIGHT = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* { font-family: 'Inter', system-ui, sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stApp { background: #F8F7FF !important; }

section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 2px solid #EDE9FE;
    min-width: 240px !important;
}

/* Main content left padding fix */
.main .block-container { padding-left: 0 !important; }

/* Sidebar buttons invisible overlay */
section[data-testid="stSidebar"] .stButton button {
    opacity: 0 !important;
    height: 40px !important;
    margin-top: -42px !important;
    width: 100% !important;
    position: relative !important;
    z-index: 99 !important;
    cursor: pointer !important;
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
}

/* Primary buttons */
button[kind="primary"], .stButton button[kind="primary"] {
    background: linear-gradient(135deg, #5B21B6, #7C3AED) !important;
    color: white !important; border: none !important;
    border-radius: 10px !important; font-weight: 700 !important;
    font-size: 14px !important; padding: 12px 24px !important;
    box-shadow: 0 4px 14px rgba(91,33,182,0.3) !important;
    transition: all 0.2s !important;
}
button[kind="primary"]:hover {
    background: linear-gradient(135deg, #4C1D95, #6D28D9) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(91,33,182,0.4) !important;
}

/* Secondary buttons */
.stButton button {
    border-radius: 10px !important; font-weight: 600 !important;
    font-size: 13px !important;
    border: 1.5px solid #EDE9FE !important;
    background: white !important; color: #5B21B6 !important;
    transition: all 0.2s !important;
}
.stButton button:hover {
    border-color: #C4B5FD !important;
    box-shadow: 0 4px 12px rgba(91,33,182,0.1) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 0; border-bottom: 2px solid #EDE9FE; background: transparent;
}
.stTabs [data-baseweb="tab"] {
    background: transparent; color: #94A3B8 !important;
    font-size: 14px !important; font-weight: 600 !important;
    padding: 12px 22px !important; border-bottom: 3px solid transparent;
}
.stTabs [aria-selected="true"] {
    color: #5B21B6 !important;
    border-bottom: 3px solid #5B21B6 !important;
    background: transparent !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: #FAFAFA; border: 2px dashed #C4B5FD;
    border-radius: 12px; padding: 8px;
}
[data-testid="stFileUploader"]:hover { border-color: #8B5CF6; }

/* Text area */
.stTextArea textarea {
    background: white; border: 2px solid #EDE9FE !important;
    border-radius: 12px !important; font-size: 14px !important;
    color: #374151 !important; line-height: 1.6 !important;
    transition: border 0.2s !important;
}
.stTextArea textarea:focus {
    border-color: #8B5CF6 !important;
    box-shadow: 0 0 0 3px rgba(139,92,246,0.15) !important;
}

/* Progress */
.stProgress > div > div { height: 8px; border-radius: 8px; }

/* Expanders */
details summary {
    background: white !important; border: 1.5px solid #EDE9FE !important;
    border-radius: 12px !important; font-weight: 700 !important;
    font-size: 14px !important; color: #111827 !important;
    padding: 14px 16px !important;
}

/* Metric */
div[data-testid="stMetric"] {
    background: white; border: 1.5px solid #EDE9FE;
    border-radius: 12px; padding: 18px;
    box-shadow: 0 2px 12px rgba(91,33,182,0.07);
}

/* Chip styles */
.chip {
    display: inline-block; padding: 5px 14px;
    border-radius: 20px; font-size: 12px;
    font-weight: 600; margin: 3px;
    transition: transform 0.15s;
}
.chip:hover { transform: scale(1.05); }
.chip-green { background: #DCFCE7; color: #15803D; border: 1px solid #BBF7D0; }
.chip-red   { background: #FEE2E2; color: #B91C1C; border: 1px solid #FECACA; }

/* Success/info/warning boxes */
.stSuccess, .stInfo, .stWarning {
    border-radius: 12px !important; font-weight: 500 !important;
}

/* Toggle */
.stToggle { margin: 4px 0 !important; }
</style>
"""

DARK = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* { font-family: 'Inter', system-ui, sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stApp { background: #0B1120 !important; color: #F1F5F9 !important; }

section[data-testid="stSidebar"] {
    background: #111827 !important;
    border-right: 2px solid #1E293B;
    min-width: 240px !important;
}

section[data-testid="stSidebar"] .stButton button {
    opacity: 0 !important; height: 40px !important;
    margin-top: -42px !important; width: 100% !important;
    position: relative !important; z-index: 99 !important;
    cursor: pointer !important; border: none !important;
    background: transparent !important; box-shadow: none !important;
}

button[kind="primary"], .stButton button[kind="primary"] {
    background: linear-gradient(135deg, #7C3AED, #A855F7) !important;
    color: white !important; border: none !important;
    border-radius: 10px !important; font-weight: 700 !important;
    font-size: 14px !important;
    box-shadow: 0 4px 14px rgba(139,92,246,0.35) !important;
}
button[kind="primary"]:hover {
    background: linear-gradient(135deg, #6D28D9, #9333EA) !important;
}

.stButton button {
    border-radius: 10px !important; font-weight: 600 !important;
    font-size: 13px !important;
    border: 1.5px solid #334155 !important;
    background: #1E293B !important; color: #A855F7 !important;
}
.stButton button:hover { border-color: #6D28D9 !important; }

.stTabs [data-baseweb="tab-list"] { gap:0; border-bottom:2px solid #1E293B; background:transparent; }
.stTabs [data-baseweb="tab"] { background:transparent;color:#64748B !important;font-size:14px !important;font-weight:600 !important;padding:12px 22px !important;border-bottom:3px solid transparent; }
.stTabs [aria-selected="true"] { color:#A855F7 !important;border-bottom:3px solid #A855F7 !important;background:transparent !important; }

[data-testid="stFileUploader"] { background:#1E293B;border:2px dashed #334155;border-radius:12px;padding:8px; }
.stTextArea textarea { background:#1E293B !important;border:2px solid #334155 !important;border-radius:12px !important;font-size:14px !important;color:#CBD5E1 !important; }
.stTextArea textarea:focus { border-color:#7C3AED !important;box-shadow:0 0 0 3px rgba(124,58,237,0.2) !important; }
.stProgress > div > div { height:8px;border-radius:8px; }
details summary { background:#1E293B !important;border:1.5px solid #334155 !important;border-radius:12px !important;font-weight:700 !important;font-size:14px !important;color:#F1F5F9 !important;padding:14px 16px !important; }
div[data-testid="stMetric"] { background:#1E293B;border:1.5px solid #334155;border-radius:12px;padding:18px; }

.chip { display:inline-block;padding:5px 14px;border-radius:20px;font-size:12px;font-weight:600;margin:3px; }
.chip-green { background:#14532D;color:#4ADE80;border:1px solid #166534; }
.chip-red   { background:#7F1D1D;color:#FCA5A5;border:1px solid #991B1B; }
</style>
"""

def apply_theme(dark_mode: bool):
    st.markdown(DARK if dark_mode else LIGHT, unsafe_allow_html=True)