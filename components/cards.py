import streamlit as st

def hero_header(title: str, subtitle: str, icon: str = "✦"):
    """
    Renders the standardized top Hero section for every module page.
    """
    html = f"""
    <div class="hero-container">
        <div class="hero-title">
            <span>{icon}</span> {title}
        </div>
        <p class="hero-subtitle">{subtitle}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def empty_state_card(title: str, message: str, icon: str = "📄"):
    """
    Renders an empty state placeholder.
    """
    html = f"""
    <div class="empty-state-card">
        <div class="empty-state-icon">{icon}</div>
        <div class="empty-state-title">{title}</div>
        <div class="empty-state-text">{message}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def success_badge(message: str):
    """
    Renders a success confirmation pill.
    """
    html = f"""
    <div class="success-badge">
        <span>✓</span> {message}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def error_badge(message: str):
    """
    Renders an error / warning pill.
    """
    html = f"""
    <div class="error-badge">
        <span>⚠️</span> {message}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
