import base64
import streamlit as st

from services.preprocessing_service import PreprocessingService
from services.classification_service import ClassificationService
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

if not st.session_state.detections:
    st.warning(t("detect.warning.no_detections"))
    if st.button(t("detect.button.back")):
        st.switch_page("pages/03_kount.py")
    st.stop()

if st.session_state.original_image is None:
    st.error(t("detect.error.no_image"))
    st.stop()

image = st.session_state.original_image
detections = st.session_state.detections

st.success(t("detect.status.ready").format(count=len(detections)))

st.subheader(t("kount.detection_result"))
show_image_with_boxes(image, detections, caption=t("detect.status.ready").format(count=len(detections)))

st.divider()

preprocessor = PreprocessingService()
classifier = ClassificationService()

if st.button(t("detect.process.button"), type="primary", width="stretch"):
    with st.spinner(t("detect.process.button")):
        st.subheader(t("pipeline.title"), anchor=False)

        display_crop_pipeline_step(
            1,
            t("detect.step1.title"),
            t("detect.step1.desc"),
        )

        crops, processed_crops = preprocessor.process_crops(image, detections)

        st.markdown(t("detect.status.crops_extracted").format(count=len(crops)))

        display_crop_pipeline_step(
            2,
            t("detect.step2.title"),
            t("detect.step2.desc"),
        )

        cols = st.columns(min(4, len(processed_crops)))
        for i, col in enumerate(cols):
            if i < len(processed_crops):
                with col:
                    st.image(processed_crops[i], width="stretch", caption=t("detect.colony.label").format(number=i + 1))

        st.divider()

        st.subheader(t("detect.title"), anchor=False)

        classifications = classifier.classify(processed_crops)
        st.session_state.classifications = classifications

    st.success(t("detect.status.classified").format(count=len(classifications)))

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

    for i, (det, cls) in enumerate(zip(detections, classifications)):
        st.markdown(f"<h4>{t('detect.colony.label').format(number=i + 1)}</h4>", unsafe_allow_html=True)
        cols = st.columns([1, 1])

        with cols[0]:
            ps = PreprocessingService()
            crop = ps.crop_colony(image, det["box"])
            processed = ps.apply_black_background(crop)

            st.image(processed, width="stretch", caption=t("detect.colony.processed"))

        with cols[1]:
            st.markdown(f"**{t('detect.species.label')}:** {cls['species']}")
            st.markdown(f"**{t('detect.confidence.label')}:** {cls['confidence']:.2%}")
            st.markdown(f"**{t('detect.detection_precision')}:** {det['confidence']:.2f}")

            with st.expander(t("detect.probabilities.title")):
                for sp, prob in cls["probabilities"].items():
                    st.markdown(f"{sp}: `{prob:.4f}`")

        st.divider()
else:
    if st.session_state.detections:
        st.info(t("detect.info.run"))
