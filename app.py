import streamlit as st

from config.settings import APP_NAME, APP_VERSION
from utils.session_state import init_session_state
from utils.i18n import t, get_language
from components.cards import disclaimer_short

st.set_page_config(
    page_title=APP_NAME,
    page_icon="icons/icono.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session_state()

pages = [
    st.Page("pages/01_home.py", title="Home", icon="🏠"),
    st.Page("pages/02_pipeline.py", title="Pipeline", icon="🔬"),
    st.Page("pages/03_kount.py", title="μKount", icon="🔍"),
    st.Page("pages/04_detect.py", title="μDetect", icon="🧪"),
    st.Page("pages/05_results.py", title="Results", icon="📊"),
    st.Page("pages/06_about.py", title="About", icon="ℹ️"),
    st.Page("pages/07_future_features.py", title="Future Features", icon="🚀"),
    st.Page("pages/08_disclaimer.py", title="Disclaimer", icon="⚠️"),
    st.Page("pages/09_acknowledgments.py", title="Acknowledgments", icon="🙏"),
]

with st.sidebar:
    import base64
    with open("icons/icono.png", "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
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
        'by <a href="https://github.com/eguzki-dm" target="_blank">Eguzkiñe</a>'
        '</p>',
        unsafe_allow_html=True,
    )
    st.divider()

    lang = get_language()
    lang_label = t("sidebar.language")
    new_lang = st.selectbox(
        lang_label,
        options=["en", "es"],
        format_func=lambda x: "🇬🇧 English" if x == "en" else "🇪🇸 Español",
        index=0 if lang == "en" else 1,
        key="language_selector",
        label_visibility="collapsed",
    )
    if new_lang != lang:
        st.session_state.language = new_lang
        st.rerun()

    st.divider()

    pg = st.navigation(pages)

    st.divider()

    if st.session_state.original_image is not None:
        if st.button(t("sidebar.restart"), use_container_width=True):
            st.session_state.original_image = None
            st.session_state.detections = []
            st.session_state.classifications = []
            st.session_state.run_metadata = {}
            st.rerun()

    disclaimer_short()

pg.run()
