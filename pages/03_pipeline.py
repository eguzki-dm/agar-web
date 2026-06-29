import streamlit as st

from utils.i18n import t

st.title(t("pipeline.title"))
st.markdown(t("pipeline.subtitle"))

show_tutorial = st.checkbox(t("pipeline.show_tutorial"))

if show_tutorial:
    with st.expander("\U0001f4d6 " + t("pipeline.tutorial.title"), expanded=True):
        for i in range(7):
            st.markdown(t(f"pipeline.tutorial.{i}"))
            if i < 6:
                st.markdown("<h3 style='text-align:center;'>\u2193</h3>", unsafe_allow_html=True)

st.divider()

steps = [
    (
        t("pipeline.step1.title"),
        t("pipeline.step1.desc"),
        t("pipeline.step1.source"),
    ),
    (
        t("pipeline.step2.title"),
        t("pipeline.step2.desc"),
        t("pipeline.step2.source"),
    ),
    (
        t("pipeline.step3.title"),
        t("pipeline.step3.desc"),
        t("pipeline.step3.source"),
    ),
    (
        t("pipeline.step4.title"),
        t("pipeline.step4.desc"),
        t("pipeline.step4.source"),
    ),
    (
        t("pipeline.step5.title"),
        t("pipeline.step5.desc"),
        t("pipeline.step5.source"),
    ),
    (
        t("pipeline.step6.title"),
        t("pipeline.step6.desc"),
        t("pipeline.step6.source"),
    ),
    (
        t("pipeline.step7.title"),
        t("pipeline.step7.desc"),
        t("pipeline.step7.source"),
    ),
]

for i, (title, desc, source) in enumerate(steps, 1):
    with st.container():
        cols = st.columns([1, 4, 2])
        with cols[0]:
            st.markdown(f"## {i}")
        with cols[1]:
            st.subheader(title, anchor=False)
            st.markdown(desc)
        with cols[2]:
            st.code(source, language="text")
    if i < len(steps):
        st.markdown("<h3 style='text-align:center;'>\u2193</h3>", unsafe_allow_html=True)
    st.divider()
