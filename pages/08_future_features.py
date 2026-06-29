import streamlit as st

from components.cards import future_feature_card
from utils.i18n import t

st.title(t("future.title"))
st.markdown(t("future.subtitle"))

st.divider()

future_feature_card(
    t("future.feature.edit_boxes"),
    t("future.feature.edit_boxes.desc"),
    "completed",
)

future_feature_card(
    t("future.feature.improve_cnn"),
    t("future.feature.improve_cnn.desc"),
    "planned",
)
