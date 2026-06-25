import streamlit as st

from utils.i18n import t

st.title(t("about.title"))

st.markdown(t("about.subtitle"))

st.divider()

st.subheader(t("about.kount.title"))

st.markdown(
    f"""
    **{t('about.kount.title')}**

    **{t('about.kount.function')}**

    **{t('about.kount.tech')}**
    """
)

st.subheader(t("about.detect.title"))

st.markdown(
    f"""
    **{t('about.detect.function')}**

    **{t('about.detect.species')}**

    **{t('about.detect.tech')}**
    """
)

st.subheader(t("about.dataset.title"))

st.markdown(t("about.dataset.content"))

st.divider()

st.subheader(t("about.architecture.title"))

st.code(
    """
agar-web/
\u251c\u2500\u2500 app.py
\u251c\u2500\u2500 config/              # Configuraci\u00f3n centralizada
\u251c\u2500\u2500 pages/               # P\u00e1ginas de Streamlit
\u251c\u2500\u2500 services/            # L\u00f3gica de negocio (detecci\u00f3n, clasificaci\u00f3n, preprocesado)
\u251c\u2500\u2500 components/          # Componentes UI reutilizables
\u251c\u2500\u2500 data/                # Datos (species_info.json)
\u251c\u2500\u2500 locales/             # Traducciones i18n
\u251c\u2500\u2500 utils/               # Utilidades
\u2514\u2500\u2500 .memory/             # Memoria del proyecto
""",
    language="text",
)
