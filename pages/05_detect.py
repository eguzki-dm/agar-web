import base64
import time
from collections import Counter
import streamlit as st

from services.cropping_service import CroppingService
from services.classification_service import ClassificationService
from services.crop_measurement_service import CropMeasurementService
from services.padding_service import PaddingService
from services.plate_detection_service import PlateDetectionService
from services.area_scaling_service import AreaScalingService
from services.multimodal_classification_service import MultimodalClassificationService
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

st.markdown(f"### {t('detect.mode.title')}")

mode_options = ["flash", "robust"]
mode_labels = {
    "flash": t("detect.mode.flash"),
    "robust": t("detect.mode.robust"),
}
mode_descriptions = {
    "flash": t("detect.mode.flash.desc"),
    "robust": t("detect.mode.robust.desc"),
}

selected_mode = st.radio(
    t("detect.mode.title"),
    options=mode_options,
    format_func=lambda x: mode_labels[x],
    index=0,
    label_visibility="collapsed",
)
st.caption(mode_descriptions[selected_mode])

cropper = CroppingService()
classifier = ClassificationService()
padder = PaddingService()

st.divider()

if st.button(t("detect.process.button"), type="primary", width="stretch"):
    with st.status(t("pipeline.title"), expanded=True) as status:

        if selected_mode == "robust":
            # ── Plate detection ──
            status.update(label=t("detect.step.plate"), state="running")
            plate_result = PlateDetectionService().detect_plate(image)

            if not plate_result.get("detected"):
                st.warning(t("detect.warning.plate_not_found"))
                status.update(label=t("detect.status.fallback"), state="running")
                use_robust = False
            else:
                mm_per_pixel = plate_result["mm_per_pixel"]
                st.markdown(f"**{t('detect.mm_per_pixel')}:** {mm_per_pixel:.6f}")
                if plate_result.get("debug_image"):
                    st.image(plate_result["debug_image"], width=300, caption=t("detect.plate_debug"))
                use_robust = True
        else:
            use_robust = False

        # ── Crop extraction ──
        status.update(label=t("detect.step1.title"), state="running")

        display_crop_pipeline_step(
            1,
            t("detect.step1.title"),
            t("detect.step1.desc"),
        )

        if use_robust:
            raw_crops = cropper.raw_crops(image, detections)
            padded_crops = padder.pad_crops(raw_crops)
            st.session_state.processed_crops = padded_crops
            display_crops = padded_crops
        else:
            crops, processed_crops = cropper.process_crops(image, detections)
            st.session_state.processed_crops = processed_crops
            display_crops = processed_crops

        st.markdown(t("detect.status.crops_extracted").format(count=len(display_crops)))

        # ── Show crop previews ──
        status.update(label=t("detect.step2.title"), state="running")

        display_crop_pipeline_step(
            2,
            t("detect.step2.title"),
            t("detect.step2.desc"),
        )

        cols = st.columns(min(4, len(display_crops)))
        for i, col in enumerate(cols):
            if i < len(display_crops):
                with col:
                    st.image(display_crops[i], width=100, caption=t("detect.colony.label").format(number=i + 1))

        st.divider()

        # ── Classification ──
        status.update(label=t("detect.title"), state="running")

        if use_robust:
            measurements = CropMeasurementService().measure_crops(padded_crops)
            area_scaler = AreaScalingService()
            measurements = area_scaler.process_crops(measurements, mm_per_pixel)
            scaled_areas = [m["area_scaled"] for m in measurements]
            st.session_state.crop_measurements = measurements

            multimodal = MultimodalClassificationService()
            t0 = time.perf_counter()
            classifications = multimodal.classify(padded_crops, scaled_areas)
            t1 = time.perf_counter()
        else:
            measurements = CropMeasurementService().measure_crops(processed_crops)
            st.session_state.crop_measurements = measurements

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
