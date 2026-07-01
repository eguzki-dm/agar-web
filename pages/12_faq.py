import streamlit as st

from utils.i18n import t

st.title(t("faq.title"))

questions = [
    (t("faq.q5.question"), t("faq.q5.answer")),
    (t("faq.q6.question"), t("faq.q6.answer")),
    (t("faq.q7.question"), t("faq.q7.answer")),
    (t("faq.q8.question"), t("faq.q8.answer")),
]

for question, answer in questions:
    with st.expander(question):
        st.markdown(answer)
