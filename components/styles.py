import streamlit as st


def load_css():
    st.markdown(
        """
<style>

/* ===========================================
   APP BACKGROUND
=========================================== */

.stApp{
    background:#0B1120;
    color:white;
}

/* ===========================================
   REMOVE DEFAULT STREAMLIT SPACING
=========================================== */

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
    padding-left:3rem;
    padding-right:3rem;
}

/* ===========================================
   HIDE STREAMLIT UI
=========================================== */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

[data-testid="stToolbar"]{
    display:none;
}

[data-testid="stDecoration"]{
    display:none;
}

/* Keep header transparent instead of hiding it */

header{
    background:transparent !important;
}

/* ===========================================
   SIDEBAR
=========================================== */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid rgba(255,255,255,.08);
}

/* ===========================================
   HERO TITLE
=========================================== */

.hero-title{

    font-size:66px;

    font-weight:800;

    color:white;

    line-height:1.1;

}

.hero-highlight{

    color:#38BDF8;

}

.hero-subtitle{

    font-size:18px;

    color:#CBD5E1;

    line-height:1.8;

    margin-top:20px;

}

/* ===========================================
   BUTTONS
=========================================== */

.stButton > button{

    background:linear-gradient(
        90deg,
        #2563EB,
        #06B6D4);

    color:white;

    border:none;

    border-radius:16px;

    padding:14px 28px;

    font-size:18px;

    font-weight:700;

    transition:0.35s;

}

.stButton > button:hover{

    transform:translateY(-3px);

    box-shadow:0 0 25px rgba(6,182,212,.45);

}

/* ===========================================
   FEATURE CARDS
=========================================== */

.feature-card{

    background:#1E293B;

    padding:30px;

    border-radius:18px;

    border:1px solid rgba(255,255,255,.08);

    transition:0.35s;

    min-height:220px;

}

.feature-card:hover{

    transform:translateY(-6px);

    border:1px solid #38BDF8;

    box-shadow:0 0 30px rgba(56,189,248,.20);

}

.card-title{

    color:white;

    font-size:24px;

    font-weight:700;

    margin-top:18px;

}

.card-text{

    color:#CBD5E1;

    line-height:1.7;

    margin-top:10px;

}

/* ===========================================
   METRIC CARD
=========================================== */

.metric-card{

    background:#1E293B;

    border-radius:18px;

    padding:22px;

    text-align:center;

}

.metric-value{

    color:#38BDF8;

    font-size:38px;

    font-weight:800;

}

.metric-label{

    color:#CBD5E1;

}

/* ===========================================
   SECTION TITLE
=========================================== */

.section-title{

    color:white;

    font-size:36px;

    font-weight:800;

    margin-bottom:20px;

}

/* ===========================================
   FOOTER
=========================================== */

.footer{

    color:#94A3B8;

    text-align:center;

    margin-top:80px;

    padding-bottom:20px;

}

/* ===========================================
   SCROLLBAR
=========================================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#334155;

    border-radius:20px;

}

::-webkit-scrollbar-thumb:hover{

    background:#38BDF8;

}

</style>
        """,
        unsafe_allow_html=True,
    )