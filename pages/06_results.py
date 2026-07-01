import json
from datetime import datetime
import streamlit as st

from components.charts import (
    species_distribution_chart,
    probability_heatmap,
    probability_table,
    metrics_dashboard,
)
from components.cards import disclaimer_card
from app_config.settings import YOLO_CONFIDENCE_THRESHOLD
from components.cfu_calculator import render_cfu_calculator
from services.pdf_report import generate_pdf
from utils.i18n import t, get_language, get_localized_field

st.title(t("results.title"))
st.markdown(t("results.subtitle"))

detections = st.session_state.detections
classifications = st.session_state.classifications

if not detections:
    st.warning(t("results.warning.no_data"))
    st.stop()

tab_kount, tab_detect = st.tabs([t("results.tab.kount"), t("results.tab.detect")])

with tab_kount:
    st.subheader(t("results.summary.title"))
    metrics_dashboard(detections, classifications, st.session_state.run_metadata)

    mode_labels = {
        "full": t("kount.detection_mode.full"),
        "sahi": t("kount.detection_mode.sahi"),
    }
    current_mode = st.session_state.get("detection_mode", "full")
    st.info(
        f"**{t('kount.detection_mode.title')}:** {mode_labels.get(current_mode, current_mode)}"
        f"  \n**Confidence threshold:** {YOLO_CONFIDENCE_THRESHOLD}"
    )

    st.divider()

    render_cfu_calculator()

    st.divider()
    disclaimer_card()

with tab_detect:
    if classifications:
        st.subheader(t("results.species_distribution.title"))

        fig = species_distribution_chart(classifications)
        if fig:
            st.plotly_chart(fig, width="stretch")

        st.divider()

        st.subheader(t("results.percentage.title"))

        species_counts = {}
        for c in classifications:
            s = c["species"]
            species_counts[s] = species_counts.get(s, 0) + 1

        total = sum(species_counts.values())
        cols = st.columns(len(species_counts))
        for i, (species, count) in enumerate(sorted(species_counts.items())):
            with cols[i]:
                pct = (count / total * 100) if total > 0 else 0
                st.metric(species, f"{count} ({pct:.1f}%)")

        st.divider()

        st.subheader(t("results.probability_table.title"))

        df = probability_table(classifications)
        if not df.empty:
            st.dataframe(df, width="stretch", hide_index=True)

        st.divider()

        st.subheader(t("results.probability_map.title"))
        fig2 = probability_heatmap(classifications)
        if fig2:
            st.plotly_chart(fig2, width="stretch")

        st.divider()

        st.subheader(t("results.species_info.title"))

        try:
            with open("data/species_info.json", encoding="utf-8") as f:
                species_info = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            species_info = {}

        detected_species = set(c["species"] for c in classifications)
        for species in sorted(detected_species):
            info = species_info.get(species, {})
            with st.expander(f"\U0001f4d6 {species} \u2014 {info.get('name', '')}"):
                desc = get_localized_field(info, "description")
                clinical = get_localized_field(info, "clinical_significance")
                industrial = get_localized_field(info, "industrial_relevance")
                pharma = get_localized_field(info, "pharmaceutical_applications")
                habitats = get_localized_field(info, "common_habitats")
                warnings = get_localized_field(info, "warnings")
                biosafety = get_localized_field(info, "biosafety_notes")
                references = info.get("references", [])

                st.markdown(f"**{t('results.description')}:** {desc}")
                st.markdown(f"**{t('results.clinical_significance')}:** {clinical}")
                st.markdown(f"**{t('results.industrial_relevance')}:** {industrial}")
                st.markdown(f"**{t('results.pharmaceutical_applications')}:** {pharma}")

                if habitats:
                    st.markdown(f"**{t('results.common_habitats')}:**")
                    for h in habitats:
                        st.markdown(f"- {h}")

                if warnings:
                    st.markdown(f"**{t('results.warnings')}:**")
                    for w in warnings:
                        st.markdown(f"- \u26a0\ufe0f {w}")

                if biosafety:
                    st.markdown(f"**{t('results.biosafety_notes')}:** {biosafety}")

                if references:
                    st.markdown(f"**{t('results.references')}:**")
                    for r in references:
                        st.markdown(f"- {r}")

        st.divider()

        pdf_bytes = generate_pdf(
            st.session_state.detections,
            st.session_state.classifications,
            species_counts,
            st.session_state.session_id,
        )
        col_pdf, col_json = st.columns(2)
        with col_pdf:
            st.download_button(
                label=t("results.download_pdf"),
                data=pdf_bytes,
                file_name=f"ukount_report_{st.session_state.session_id}.pdf",
                mime="application/pdf",
                type="primary",
                width="stretch",
            )

        crop_measurements = st.session_state.get("crop_measurements", [])
        export_data = {
            "session_id": st.session_state.session_id,
            "detections": [
                {
                    "box": d["box"],
                    "detection_confidence": d["confidence"],
                    "predicted_species": st.session_state.classifications[i]["species"],
                    "classification_confidence": st.session_state.classifications[i]["confidence"],
                    "probabilities": st.session_state.classifications[i]["probabilities"],
                }
                for i, d in enumerate(st.session_state.detections)
                if i < len(st.session_state.classifications)
            ],
            "crop_measurements": crop_measurements,
            "summary": {
                "total_detections": len(st.session_state.detections),
                "total_classified": len(st.session_state.classifications),
                "species_counts": species_counts,
            },
        }
        with col_json:
            st.download_button(
                label=t("results.download_json"),
                data=json.dumps(export_data, indent=2, ensure_ascii=False),
                file_name=f"ukount_results_{st.session_state.session_id}.json",
                mime="application/json",
                type="primary",
                width="stretch",
            )

        st.divider()
        disclaimer_card()
    else:
        st.info(t("results.no_classifications"))
        st.divider()
        disclaimer_card()
