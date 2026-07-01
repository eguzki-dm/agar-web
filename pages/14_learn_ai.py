import streamlit as st
from utils.i18n import t

st.title(t("learn.title"))
st.markdown(t("learn.subtitle"))

for i in range(1, 15):
    with st.expander(t(f"learn.concept_{i}.title")):
        st.markdown(t(f"learn.concept_{i}.content"))
