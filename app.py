import os
import cv2

cv2.setNumThreads(1)
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import streamlit as st

from app_config.settings import APP_NAME, APP_VERSION
from utils.session_state import init_session_state
from utils.i18n import t, get_language
from utils.theme import inject_theme_css
from components.cards import disclaimer_short

st.set_page_config(
    page_title=APP_NAME,
    page_icon="icons/icono.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session_state()
inject_theme_css()

pages = {
    t("nav.section.home"): [
        st.Page("pages/01_home.py", title=t("nav.home"), icon="🏠"),
    ],
    t("nav.section.learn"): [
        st.Page("pages/02_fundamentals.py", title=t("nav.fundamentals"), icon="📖"),
        st.Page("pages/03_pipeline.py", title=t("nav.how_it_works"), icon="🔬"),
        st.Page("pages/14_learn_ai.py", title=t("learn.nav"), icon="🧠"),
    ],
    "\u03bcKount & \u03bcDetect": [
        st.Page("pages/04_kount.py", title=t("nav.kount"), icon="🔍"),
        st.Page("pages/05_detect.py", title=t("nav.detect"), icon="🧪"),
        st.Page("pages/06_results.py", title=t("nav.results"), icon="📊"),
    ],
    t("nav.section.more"): [
        st.Page("pages/11_cuora.py", title=t("nav.cuora"), icon="🧠"),
        st.Page("pages/08_future_features.py", title=t("nav.future"), icon="🚀"),
        st.Page("pages/09_disclaimer.py", title=t("nav.disclaimer"), icon="⚠️"),
        st.Page("pages/12_faq.py", title=t("nav.faq"), icon="❓"),
        st.Page("pages/10_acknowledgments.py", title=t("nav.acknowledgments"), icon="🙏"),
        st.Page("pages/13_about.py", title=t("nav.about"), icon="⚙️"),
    ],
}

with st.sidebar:
    pg = st.navigation(pages)

    import base64
    with open("icons/icono.png", "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <div class="logo-wrapper" style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{img_b64}"
                 style="width: 200px; mix-blend-mode: multiply;" />
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(f"<h1 style='text-align: center;'>{APP_NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'><em>v{APP_VERSION}</em></p>", unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align: center; font-size: 0.85rem;">'
        'by Eguzkiñe<br>'
        '<a href="https://github.com/eguzki-dm" target="_blank"><img src="https://img.shields.io/badge/GitHub-eguzki--dm-181717?style=flat-square&logo=github" alt="GitHub"></a> '
        '<a href="https://orcid.org/0000-0002-7151-1639" target="_blank"><img src="https://img.shields.io/badge/ORCID-0000--0002--7151--1639-A6CE39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID"></a> '
        '<a href="https://es.linkedin.com/in/eguzkine-dm" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-eguzkine--dm-0A66C2?style=flat-square&logo=linkedin" alt="LinkedIn"></a>'
        '</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="font-size: 0.85rem; text-align: center;">'
        + t("sidebar.microbiology_cta") + '<br>'
        '<a href="https://www.instagram.com/lifeisaboutmicrobiology/" target="_blank">'
        + t("sidebar.microbiology_handle") + '</a></p>',
        unsafe_allow_html=True,
    )


    st.divider()

    lang = get_language()
    new_lang = st.radio(
        "Idioma",
        options=["en", "es"],
        format_func=lambda x: "GB" if x == "en" else "ES",
        index=0 if lang == "en" else 1,
        key="language_selector",
        label_visibility="collapsed",
        horizontal=True,
    )
    if new_lang != lang:
        st.session_state.language = new_lang
        st.rerun()

    st.divider()

    if st.session_state.original_image is not None:
        if st.button(t("sidebar.restart"), width="stretch"):
            st.session_state.original_image = None
            st.session_state.detections = []
            st.session_state.classifications = []
            st.session_state.run_metadata = {}
            st.rerun()


    disclaimer_short()


pg.run()
