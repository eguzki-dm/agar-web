import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from utils.i18n import t


def species_distribution_chart(classifications: list[dict]) -> go.Figure:
    if not classifications:
        return None

    species_counts = {}
    for c in classifications:
        s = c["species"]
        species_counts[s] = species_counts.get(s, 0) + 1

    df = pd.DataFrame(
        {
            "Species": list(species_counts.keys()),
            "Count": list(species_counts.values()),
        }
    )
    df["Percentage"] = (df["Count"] / df["Count"].sum() * 100).round(1)

    fig = px.bar(
        df,
        x="Species",
        y="Count",
        text="Count",
        color="Species",
        color_discrete_sequence=px.colors.qualitative.Set2,
        title=t("charts.distribution.title"),
        labels={"Count": t("charts.distribution.y_label"), "Species": t("charts.distribution.x_label")},
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(
        xaxis_title="",
        yaxis_title=t("charts.distribution.y_label"),
        showlegend=False,
        height=400,
    )

    return fig


def probability_heatmap(classifications: list[dict]) -> go.Figure:
    if not classifications:
        return None

    species_order = list(classifications[0]["probabilities"].keys())

    data = []
    labels = []
    for i, c in enumerate(classifications):
        labels.append(f"#{i + 1}: {c['species']}")
        data.append([c["probabilities"][s] for s in species_order])

    df = pd.DataFrame(data, columns=species_order, index=labels)

    fig = px.imshow(
        df,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="Purples",
        title=t("charts.heatmap.title"),
        labels={
            "x": t("charts.heatmap.x_label"),
            "y": t("charts.heatmap.y_label"),
            "color": t("charts.heatmap.color_label"),
        },
    )

    fig.update_layout(height=200 + len(classifications) * 40)

    return fig


def probability_table(classifications: list[dict]) -> pd.DataFrame:
    if not classifications:
        return pd.DataFrame()

    rows = []
    for i, c in enumerate(classifications):
        row = {t("charts.table.colony"): f"#{i + 1}", t("charts.table.predicted"): c["species"]}
        for species, prob in c["probabilities"].items():
            row[species] = f"{prob:.4f}"
        rows.append(row)

    return pd.DataFrame(rows)


def metrics_dashboard(detections: list, classifications: list, metadata: dict, show_classification: bool = True):
    if show_classification:
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                t("charts.metrics.detected"),
                len(detections),
            )

        with col2:
            st.metric(
                t("charts.metrics.classified"),
                len(classifications),
            )

        with col3:
            time_det = metadata.get("detection_time_s", 0)
            st.metric(t("charts.metrics.time_kount"), f"{time_det} s")

        with col4:
            time_cls = metadata.get("classification_time_s", 0)
            if time_cls:
                st.metric(t("charts.metrics.time_detect"), f"{time_cls} s")
            else:
                st.metric(t("charts.metrics.time_detect"), "\u2014")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                t("charts.metrics.detected"),
                len(detections),
            )

        with col2:
            time_det = metadata.get("detection_time_s", 0)
            st.metric(t("charts.metrics.time_kount"), f"{time_det} s")
