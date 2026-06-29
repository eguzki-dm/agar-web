import base64
import streamlit as st

from app_config.settings import APP_NAME
from utils.i18n import t
from components.cards import disclaimer_card

with open("icons/icono.png", "rb") as f:
    logo = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"

st.markdown(
    f'<div style="text-align:center;">'
    f'<img src="{logo}" style="width:200px;max-width:80%;">'
    f'<h1 style="margin-top:1rem;">{t("home.title")}</h1>'
    f'</div>',
    unsafe_allow_html=True,
)
st.subheader(t("home.subtitle"), anchor=False)

st.markdown(t("home.supporting"))

st.divider()

st.subheader(t("home.whatis.title"))
st.markdown(t("home.whatis.content"))

st.divider()

st.subheader(t("home.architecture.title"))
col_arch1, col_arch2 = st.columns(2)
with col_arch1:
    st.markdown(t("home.arch.kount"))
with col_arch2:
    st.markdown(t("home.arch.detect"))

st.divider()

st.subheader(t("home.pipeline"))

col1, col2, col3, col4, col5 = st.columns(5, gap="small")

with col1:
    st.markdown(
        f"""
        <div class="step-card-1" style="
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
        <div class="step-card-2" style="
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
        <div class="step-card-3" style="
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
        <div class="step-card-4" style="
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
        <div class="step-card-5" style="
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

st.subheader(t("home.scope.title"))
st.markdown(t("home.scope.content"))

st.divider()

st.subheader(t("home.dataset"))
st.markdown(t("home.dataset.content"))

st.divider()

st.subheader(t("home.notice.title"))
st.markdown(t("home.notice.items"))

st.divider()

disclaimer_card()
