import streamlit as st

from utils.i18n import t

st.title(t("disclaimer.title"))

st.markdown(
    f"""
    <div class="disclaimer-banner" style="
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        text-align: center;
    ">
        <h2 style="color: #721c24;">{t('disclaimer.banner.title')}</h2>
        <p style="font-size: 1.2rem; color: #721c24;">
            <strong>{t('disclaimer.banner.text')}</strong>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

st.header(t("disclaimer.limitations.title"))

limitations = [
    ("\U0001f52c", t("disclaimer.limitation1.title"), t("disclaimer.limitation1.desc")),
    ("\U0001f9ea", t("disclaimer.limitation2.title"), t("disclaimer.limitation2.desc")),
    ("\u26a0\ufe0f", t("disclaimer.limitation3.title"), t("disclaimer.limitation3.desc")),
    ("\U0001f4cb", t("disclaimer.limitation4.title"), t("disclaimer.limitation4.desc")),
    ("\U0001f468\u200d\U0001f52c", t("disclaimer.limitation5.title"), t("disclaimer.limitation5.desc")),
    ("\U0001f916", t("disclaimer.limitation6.title"), t("disclaimer.limitation6.desc")),
]

for icon, title, desc in limitations:
    st.subheader(title, anchor=False)
    st.markdown(desc)
    st.divider()

st.header(t("disclaimer.responsible_use.title"))

st.markdown(
    f"""
    {t('disclaimer.responsible_use.intro')}
    1. {t('disclaimer.responsible_use.item1')}
    2. {t('disclaimer.responsible_use.item2')}
    3. {t('disclaimer.responsible_use.item3')}
    4. {t('disclaimer.responsible_use.item4')}

    {t('disclaimer.responsible_use.footer')}
    """
)

st.divider()

st.header(t("disclaimer.version.title"))

st.markdown(
    f"""
    **{t('disclaimer.version.info')}**

    {t('disclaimer.version.desc')}

    **{t('disclaimer.version.status')}**
    """
)
