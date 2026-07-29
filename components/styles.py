import streamlit as st

def load_css():
    """
    Injects CareerPilot AI Design System CSS rules into Streamlit.
    Enforces dark obsidian theme, glassmorphism, glowing accents, 
    and compact IDE-style sidebar navigation (Notion, Linear, Cursor).
    """
    css = """
    <style>
    /* =========================================================
       1. CORE DESIGN TOKENS & CSS VARIABLES
       ========================================================= */
    :root {
        --bg-base: #090D16;
        --bg-surface-1: #111827;
        --bg-surface-2: #1F2937;
        --bg-glass: rgba(17, 24, 39, 0.75);
        --border-subtle: rgba(255, 255, 255, 0.08);
        --border-glowing: rgba(99, 102, 241, 0.4);
        --primary-accent: #6366F1;
        --secondary-accent: #8B5CF6;
        --ai-glow: #06B6D4;
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --text-muted: #64748B;
        --success: #10B981;
        --warning: #F59E0B;
        --danger: #EF4444;
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --transition: all 0.12s ease;
    }

    /* =========================================================
       2. APPLICATION CANVAS & TYPOGRAPHY
       ========================================================= */
    .stApp {
        background-color: var(--bg-base) !important;
        background-image: 
            radial-gradient(circle at 85% 10%, rgba(99, 102, 241, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 15% 90%, rgba(6, 182, 212, 0.06) 0%, transparent 40%) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    }

    /* Hide default Streamlit header bar decoration */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    
    footer {
        visibility: hidden;
    }

    /* Block Container Spacing */
    .block-container {
        padding-top: 1.25rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }

    /* =========================================================
       3. HERO HEADER COMPONENT
       ========================================================= */
    .hero-container {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.4) 100%);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-lg);
        padding: 1.75rem 2rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(16px);
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        position: relative;
        overflow: hidden;
    }

    .hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, var(--primary-accent) 0%, var(--ai-glow) 100%);
    }

    /* =========================================================
       4. REUSABLE GLASS CARDS & TILES
       ========================================================= */
    .glass-panel {
        background: var(--bg-glass);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 1.5rem;
        margin-bottom: 1.25rem;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 24px -6px rgba(0, 0, 0, 0.4);
        transition: var(--transition);
    }

    .glass-panel:hover {
        border-color: var(--border-glowing);
        transform: translateY(-2px);
    }

    .glass-card-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Skill Tag Chips */
    .skill-chip {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        border: 1px solid rgba(99, 102, 241, 0.3);
        color: #A5B4FC;
        padding: 0.25rem 0.65rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.2rem;
    }

    /* =========================================================
       5. MAIN PAGE BUTTONS OVERRIDE
       ========================================================= */
    .stMainBlockContainer .stButton > button {
        background: linear-gradient(135deg, var(--primary-accent) 0%, var(--secondary-accent) 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        padding: 0.65rem 1.4rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35) !important;
        transition: var(--transition) !important;
        width: 100%;
    }

    .stMainBlockContainer .stButton > button:hover {
        opacity: 0.92 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5) !important;
    }

    /* =========================================================
       6. STREAMLIT EXPANDER ACCORDION DARK MODE OVERRIDE
       ========================================================= */
    div[data-testid="stExpander"] {
        background: rgba(17, 24, 39, 0.75) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3) !important;
        margin-bottom: 0.75rem !important;
        overflow: hidden !important;
    }

    div[data-testid="stExpander"] details {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
    }

    div[data-testid="stExpander"] details summary {
        background: rgba(17, 24, 39, 0.9) !important;
        background-color: rgba(17, 24, 39, 0.9) !important;
        color: #F8FAFC !important;
        font-weight: 600 !important;
        border-radius: var(--radius-md) !important;
        padding: 0.75rem 1rem !important;
        transition: var(--transition) !important;
    }

    div[data-testid="stExpander"] details[open] summary {
        background: rgba(31, 41, 55, 0.95) !important;
        background-color: rgba(31, 41, 55, 0.95) !important;
        color: #A5B4FC !important;
        border-bottom: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) var(--radius-md) 0 0 !important;
    }

    div[data-testid="stExpander"] details summary:hover {
        background: rgba(31, 41, 55, 0.8) !important;
        color: #A5B4FC !important;
    }

    div[data-testid="stExpanderDetails"] {
        background: rgba(11, 14, 23, 0.85) !important;
        background-color: rgba(11, 14, 23, 0.85) !important;
        color: #CBD5E1 !important;
        padding: 1.25rem 1rem !important;
        border-top: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    div[data-testid="stExpander"] p, 
    div[data-testid="stExpander"] div, 
    div[data-testid="stExpander"] span {
        color: #CBD5E1 !important;
    }

    div[data-testid="stExpander"] details summary p, 
    div[data-testid="stExpander"] details summary span {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }

    div[data-testid="stExpander"] details[open] summary p, 
    div[data-testid="stExpander"] details[open] summary span {
        color: #A5B4FC !important;
        font-weight: 700 !important;
    }

    /* =========================================================
       7. COMPACT IDE-STYLE SIDEBAR BRANDING & TREE NAVIGATION
       ========================================================= */
    section[data-testid="stSidebar"] {
        background-color: #0B0E17 !important;
        border-right: 1px solid var(--border-subtle) !important;
    }

    .sidebar-header {
        padding: 0.85rem 0.4rem 0.65rem 0.4rem;
        border-bottom: 1px solid var(--border-subtle);
        margin-bottom: 0.6rem;
    }

    /* Prominent Brand Identity Styling */
    .brand-mark {
        font-size: 1.35rem !important;
        font-weight: 800 !important;
        color: #F8FAFC !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        gap: 0.35rem !important;
        letter-spacing: -0.02em !important;
        line-height: 1.1 !important;
        text-align: left !important;
    }

    .brand-mark img {
        width: 32px !important;
        height: 32px !important;
        display: inline-block !important;
        vertical-align: middle !important;
    }

    .resume-status-badge {
        margin-top: 0.4rem;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 0.35rem;
    }

    .status-loaded {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.25);
        color: #34D399;
    }

    .status-missing {
        background: rgba(245, 158, 11, 0.1);
        border: 1px solid rgba(245, 158, 11, 0.25);
        color: #FBBF24;
    }

    /* TIGHT VERTICAL SPACING & RESET OF ALL SIDEBAR BUTTONS */
    div[data-testid="stSidebarUserContent"] .stButton {
        margin-bottom: 0px !important;
        margin-top: 0px !important;
        padding: 0px !important;
    }

    div[data-testid="stSidebarUserContent"] .stButton > button {
        background: transparent !important;
        background-color: transparent !important;
        color: var(--text-secondary) !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        text-align: left !important;
        padding: 0.2rem 0.5rem !important;
        min-height: 28px !important;
        line-height: 1.2 !important;
        font-size: 0.84rem !important;
        font-weight: 500 !important;
        justify-content: flex-start !important;
        border-radius: 4px !important;
        margin: 0.05rem 0 !important;
        width: 100% !important;
        transition: var(--transition) !important;
    }

    /* Subtle Hover State */
    div[data-testid="stSidebarUserContent"] .stButton > button:hover {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #F8FAFC !important;
    }

    /* Active Page Item — Thin Left Border & Soft Background Glow */
    div[data-testid="stSidebarUserContent"] .stButton > button[kind="primary"] {
        background: rgba(99, 102, 241, 0.12) !important;
        color: #A5B4FC !important;
        font-weight: 600 !important;
        border-left: 2px solid var(--primary-accent) !important;
        border-radius: 0 4px 4px 0 !important;
    }

    /* Compact 14px Indentation for Child Items */
    .nav-child-wrapper {
        padding-left: 0px !important;
        margin-top: 0.05rem !important;
        margin-bottom: 0.15rem !important;
    }

    .nav-child-wrapper .stButton > button {
        padding-left: 14px !important;
        font-size: 0.82rem !important;
        color: #94A3B8 !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
