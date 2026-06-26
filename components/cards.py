import streamlit as st

from utils.i18n import t, get_localized_field


def disclaimer_card():
    st.markdown(
        f"""
        <div class="disclaimer-card" style="
            background-color: #fff3cd;
            border: 1px solid #ffc107;
            border-radius: 8px;
            padding: 1.2rem;
            margin: 1rem 0;
        ">
            <strong>{t('cards.disclaimer.title')}</strong><br><br>
            {t('cards.disclaimer.poc')}<br><br>
            {t('cards.disclaimer.warning')}
            <ul>
                <li>{t('cards.disclaimer.item1')}</li>
                <li>{t('cards.disclaimer.item2')}</li>
                <li>{t('cards.disclaimer.item3')}</li>
                <li>{t('cards.disclaimer.item4')}</li>
            </ul>
            {t('cards.disclaimer.footer')}
        </div>
        """,
        unsafe_allow_html=True,
    )


def disclaimer_short():
    st.caption(t("cards.disclaimer.short"))


def species_card(crop, species, confidence, species_info=None):
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(crop, use_container_width=True)

    with col2:
        st.subheader(species, anchor=False)
        st.markdown(f"**{t('detect.confidence.label')}:** {confidence:.1%}")

        if species_info:
            info = species_info.get(species, {})
            full_name = get_localized_field(info, "name") or info.get("name", t("results.not_available"))
            st.markdown(f"**{t('cards.species.full_name')}:** {full_name}")
            st.markdown(f"**{t('cards.species.gram')}:** {info.get('gram', t('results.not_available'))}")
            st.markdown(f"**{t('cards.species.shape')}:** {info.get('shape', t('results.not_available'))}")

            with st.expander(t("cards.species.description")):
                desc = get_localized_field(info, "description")
                st.markdown(desc if desc else t("cards.species.not_available"))

    st.divider()


def future_feature_card(title, description, status="planned"):
    status_icons = {
        "planned": "\U0001f4cb",
        "in_progress": "\U0001f504",
        "completed": "\u2705",
    }
    icon = status_icons.get(status, "\U0001f4cb")

    st.markdown(
        f"""
        <div class="feature-card" style="
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
        ">
            <strong>{icon} {title}</strong><br>
            {description}
        </div>
        """,
        unsafe_allow_html=True,
    )
