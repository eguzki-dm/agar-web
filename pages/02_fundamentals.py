import base64
import streamlit as st

from utils.i18n import t

with open("icons/Cuora.png", "rb") as f:
    cuora_b64 = base64.b64encode(f.read()).decode()

st.title(t("fundamentals.title"))

col_left, col_right = st.columns([3, 1])

with col_left:
    st.markdown(t("fundamentals.welcome"))
    st.subheader(t("fundamentals.context.title"))
    st.markdown(t("fundamentals.context.content"))
    st.markdown(t("fundamentals.industries"))
    st.subheader(t("fundamentals.classification.title"))
    st.markdown(t("fundamentals.classification.content"))
    st.subheader(t("fundamentals.limitations.title"))
    st.markdown(t("fundamentals.limitations.content"))
    st.subheader(t("fundamentals.support.title"))
    st.markdown(t("fundamentals.support.content"))

with col_right:
    st.image(f"data:image/png;base64,{cuora_b64}", width=250)
    st.markdown(
        f'<p style="text-align:center;font-size:0.85rem;opacity:0.7;margin-top:0.5rem;">'
        f'Cuora — {t("fundamentals.cuora_caption")}</p>',
        unsafe_allow_html=True,
    )

st.divider()

st.subheader(t("fundamentals.detection_strategies.title"))
st.markdown(t("fundamentals.detection_strategies.intro"))
st.markdown(t("fundamentals.detection_strategies.sahi"))
st.markdown(t("fundamentals.detection_strategies.full"))

st.divider()
st.subheader(t("fundamentals.classification_strategies.title"))
st.markdown(t("fundamentals.classification_strategies.intro"))
st.markdown(t("fundamentals.classification_strategies.flash"))
st.markdown(t("fundamentals.classification_strategies.robust"))
