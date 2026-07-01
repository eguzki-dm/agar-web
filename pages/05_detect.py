import base64
import time
from collections import Counter
import streamlit as st

from services.cropping_service import CroppingService
from services.classification_service import ClassificationService
from services.pendiente_de_validar.crop_measurement_service import CropMeasurementService
from components.image_viewer import show_image_with_boxes, display_crop_pipeline_step
from components.cards import species_card
from utils.i18n import t

with open("icons/uDetect.png", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
    <div class="logo-wrapper" style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_b64}"
             style="width: 400px; mix-blend-mode: multiply;" />
    </div>
    """,
    unsafe_allow_html=True,
)
st.title(t("detect.title"))
st.markdown(t("detect.subtitle"))
if "detections" not in st.session_state or not st.session_state.detections:
    st.warning(t("detect.warning.no_detections"))
    if st.button(t("detect.button.back")):
        st.switch_page("pages/04_kount.py")
    st.stop()

if "original_image" not in st.session_state or st.session_state.original_image is None:
    st.error(t("detect.error.no_image"))
    st.stop()

image = st.session_state.original_image
detections = st.session_state.detections

st.success(t("detect.status.ready").format(count=len(detections)))

st.subheader(t("kount.detection_result"))
show_image_with_boxes(image, detections, caption=t("detect.status.ready").format(count=len(detections)))

st.divider()

cropper = CroppingService()
classifier = ClassificationService()

if st.button(t("detect.process.button"), type="primary", width="stretch"):
    with st.status(t("pipeline.title"), expanded=True) as status:
        status.update(label=t("detect.step1.title"), state="running")

        display_crop_pipeline_step(
            1,
            t("detect.step1.title"),
            t("detect.step1.desc"),
        )

        crops, processed_crops = cropper.process_crops(image, detections)
        st.session_state.processed_crops = processed_crops

        measurements = CropMeasurementService().measure_crops(processed_crops)
        st.session_state.crop_measurements = measurements

        st.markdown(t("detect.status.crops_extracted").format(count=len(crops)))

        status.update(label=t("detect.step2.title"), state="running")

        display_crop_pipeline_step(
            2,
            t("detect.step2.title"),
            t("detect.step2.desc"),
        )

        cols = st.columns(min(4, len(processed_crops)))
        for i, col in enumerate(cols):
            if i < len(processed_crops):
                with col:
                    st.image(processed_crops[i], width=100, caption=t("detect.colony.label").format(number=i + 1))

        st.divider()

        status.update(label=t("detect.title"), state="running")

        t0 = time.perf_counter()
        classifications = classifier.classify(processed_crops)
        t1 = time.perf_counter()
        st.session_state.classifications = classifications
        st.session_state.run_metadata["classification_time_s"] = round(t1 - t0, 2)

        status.update(
            label=t("detect.status.classified").format(count=len(classifications)),
            state="complete",
            expanded=False,
        )

    species_counts = Counter(cls["species"] for cls in classifications)
    top_two = [sp for sp, _ in species_counts.most_common(2)]
    st.toast(
        t("detect.toast.done").format(
            count=len(classifications),
            species=", ".join(top_two),
        ),
        icon="✅",
    )

st.divider()

if st.session_state.classifications:
    st.subheader(t("detect.results.title"))

    classifications = st.session_state.classifications

    import json

    species_info_path = "data/species_info.json"
    try:
        with open(species_info_path, encoding="utf-8") as f:
            species_info = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        species_info = {}

    processed_crops = st.session_state.get("processed_crops", [])
    for i, (det, cls) in enumerate(zip(detections, classifications)):
        st.markdown(f"<h4>{t('detect.colony.label').format(number=i + 1)}</h4>", unsafe_allow_html=True)
        cols = st.columns([1, 1])

        with cols[0]:
            if i < len(processed_crops):
                st.image(processed_crops[i], width=100, caption=t("detect.colony.processed"))

        with cols[1]:
            st.markdown(f"**{t('detect.species.label')}:** {cls['species']}")
            st.markdown(f"**{t('detect.confidence.label')}:** {cls['confidence']:.2%}")
            st.markdown(f"**{t('detect.detection_precision')}:** {det['confidence']:.2f}")

            with st.expander(t("detect.probabilities.title")):
                for sp, prob in cls["probabilities"].items():
                    st.markdown(f"{sp}: `{prob:.4f}`")

        st.divider()

    if st.button(t("detect.button.results"), type="primary", width="stretch"):
        st.switch_page("pages/06_results.py")
else:
    if st.session_state.detections:
        st.info(t("detect.info.run"))
