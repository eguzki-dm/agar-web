import streamlit as st

from utils.i18n import t

st.title(t("ack.title"))

st.divider()

st.subheader(t("ack.program.title"))
st.markdown(t("ack.program.desc"))

st.divider()

st.subheader(t("ack.mentor.title"))
st.markdown(t("ack.mentor.desc"))

st.divider()

st.subheader(t("ack.classmates.title"))
st.markdown(t("ack.classmates.desc"))

st.divider()

st.subheader(t("ack.dataset.title"))
st.markdown(t("ack.dataset.desc"))

st.divider()

st.subheader(t("ack.patch.title"))
st.markdown(t("ack.patch.desc"))

st.divider()

st.subheader(t("ack.staff.title"))
st.markdown(t("ack.staff.desc"))
