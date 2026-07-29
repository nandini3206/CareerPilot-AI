import textwrap
import streamlit as st

def kpi_card(label: str, value: str, subtext: str = "", accent_color: str = "#6366F1"):
    """
    Renders a glowing dark glass KPI metric badge card.
    """
    html = textwrap.dedent(f"""
    <div class="kpi-container" style="border-left: 3px solid {accent_color}; background: rgba(17, 24, 39, 0.7); padding: 1rem 1.25rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08); margin-bottom: 0.75rem;">
        <div style="font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #64748B; margin-bottom: 0.25rem;">{label}</div>
        <div style="font-size: 1.75rem; font-weight: 800; color: {accent_color}; line-height: 1.1; margin-bottom: 0.25rem;">{value}</div>
        {f'<div style="font-size: 0.78rem; color: #94A3B8;">{subtext}</div>' if subtext else ''}
    </div>
    """).strip()
    st.markdown(html, unsafe_allow_html=True)
