import streamlit as st

from config.settings import APP_NAME
from utils.i18n import t
from components.cards import disclaimer_card

st.title(f"\U0001f9eb {t('home.title')}")
st.subheader(t("home.subtitle"), anchor=False)

st.markdown(
    f"""
    {t('home.intro')}
    - **{t('home.bullet.detection')}**
    - **{t('home.bullet.counting')}**
    - **{t('home.bullet.classification')}**

    {t('home.based_on.intro')}
    - **{t('home.based_on.kount')}**
    - **{t('home.based_on.detect')}**
    """
)

st.divider()

st.subheader(t("home.pipeline"))

col1, col2, col3, col4, col5 = st.columns(5, gap="small")

with col1:
    st.markdown(
        f"""
        <div style="
            background:#e3f2fd;
            border:2px solid #1565c0;
            border-radius:12px;
            padding:1.2rem 0.5rem;
            text-align:center;
            height:140px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="font-size:2rem;">\U0001f4e4</div>
            <div style="font-weight:600;color:#1565c0;font-size:1rem;">{t('home.pipeline.upload.title')}</div>
            <div style="color:#1565c0;font-size:0.75rem;opacity:0.8;">{t('home.pipeline.upload.subtitle')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="
            background:#fff3e0;
            border:2px solid #e65100;
            border-radius:12px;
            padding:1.2rem 0.5rem;
            text-align:center;
            height:140px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="font-size:2rem;">\U0001f50d</div>
            <div style="font-weight:600;color:#e65100;font-size:1rem;">{t('home.pipeline.kount.title')}</div>
            <div style="color:#e65100;font-size:0.75rem;opacity:0.8;">{t('home.pipeline.kount.subtitle')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div style="
            background:#f3e5f5;
            border:2px solid #6a1b9a;
            border-radius:12px;
            padding:1.2rem 0.5rem;
            text-align:center;
            height:140px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="font-size:2rem;">\u2702\ufe0f</div>
            <div style="font-weight:600;color:#6a1b9a;font-size:1rem;">{t('home.pipeline.crop.title')}</div>
            <div style="color:#6a1b9a;font-size:0.75rem;opacity:0.8;">{t('home.pipeline.crop.subtitle')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        f"""
        <div style="
            background:#e8f5e9;
            border:2px solid #2e7d32;
            border-radius:12px;
            padding:1.2rem 0.5rem;
            text-align:center;
            height:140px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="font-size:2rem;">\U0001f9ea</div>
            <div style="font-weight:600;color:#2e7d32;font-size:1rem;">{t('home.pipeline.detect.title')}</div>
            <div style="color:#2e7d32;font-size:0.75rem;opacity:0.8;">{t('home.pipeline.detect.subtitle')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col5:
    st.markdown(
        f"""
        <div style="
            background:#fff8e1;
            border:2px solid #f9a825;
            border-radius:12px;
            padding:1.2rem 0.5rem;
            text-align:center;
            height:140px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="font-size:2rem;">\U0001f4ca</div>
            <div style="font-weight:600;color:#f9a825;font-size:1rem;">{t('home.pipeline.results.title')}</div>
            <div style="color:#f9a825;font-size:0.75rem;opacity:0.8;">{t('home.pipeline.results.subtitle')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

st.subheader(t("home.dataset"))
st.markdown(
    f"""
    - **{t('home.dataset.images')}**
    - **{t('home.dataset.annotations')}**
    - {t('home.dataset.configs')}
    - {t('home.dataset.source')}
    - {t('home.dataset.authors')}
    - {t('home.dataset.title')}
    """
)

st.divider()

disclaimer_card()
