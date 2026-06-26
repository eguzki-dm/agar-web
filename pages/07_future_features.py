import streamlit as st

from components.cards import future_feature_card
from utils.i18n import t

st.title(t("future.title"))
st.markdown(t("future.subtitle"))

st.divider()

st.subheader(t("future.phase2.title"))

st.markdown(t("future.phase2.desc"))

future_feature_card(
    t("future.feature.move_boxes"),
    t("future.feature.move_boxes.desc"),
    "planned",
)

future_feature_card(
    t("future.feature.resize_boxes"),
    t("future.feature.resize_boxes.desc"),
    "planned",
)

future_feature_card(
    t("future.feature.delete_boxes"),
    t("future.feature.delete_boxes.desc"),
    "planned",
)

future_feature_card(
    t("future.feature.add_boxes"),
    t("future.feature.add_boxes.desc"),
    "planned",
)

st.divider()

st.subheader(t("future.phase3.title"))

st.markdown(t("future.phase3.desc"))

future_feature_card(
    t("future.feature.micro_description"),
    t("future.feature.micro_description.desc"),
    "planned",
)

future_feature_card(
    t("future.feature.clinical"),
    t("future.feature.clinical.desc"),
    "planned",
)

future_feature_card(
    t("future.feature.industrial"),
    t("future.feature.industrial.desc"),
    "planned",
)

future_feature_card(
    t("future.feature.pharma"),
    t("future.feature.pharma.desc"),
    "planned",
)

st.divider()

st.subheader(t("future.phase4.title"))

st.markdown(t("future.phase4.desc"))

future_feature_card(
    t("future.feature.chatbot_micro"),
    t("future.feature.chatbot_micro.desc"),
    "completed",
)

future_feature_card(
    t("future.feature.chatbot_results"),
    t("future.feature.chatbot_results.desc"),
    "completed",
)

future_feature_card(
    t("future.feature.chatbot_safety"),
    t("future.feature.chatbot_safety.desc"),
    "completed",
)

st.warning(
    t("future.chatbot_warning"),
    icon="\u26a0\ufe0f",
)

st.divider()

st.subheader(t("future.roadmap.title"))

roadmap = [
    ("\u2705", t("future.roadmap.phase1"), t("future.roadmap.completed")),
    ("\U0001f504", t("future.roadmap.phase2"), t("future.roadmap.pending")),
    ("\u2b1c", t("future.roadmap.phase3"), t("future.roadmap.pending")),
    ("\u2b1c", t("future.roadmap.phase4"), t("future.roadmap.pending")),
    ("\u2b1c", t("future.roadmap.phase5"), t("future.roadmap.pending")),
    ("\u2705", t("future.roadmap.phase6"), t("future.roadmap.completed")),
    ("\u2705", t("future.roadmap.phase7"), t("future.roadmap.completed")),
]

for icon, phase, status in roadmap:
    cols = st.columns([1, 6, 2])
    with cols[0]:
        st.markdown(f"{icon}")
    with cols[1]:
        st.markdown(f"**{phase}**")
    with cols[2]:
        st.markdown(f"*{status}*")
