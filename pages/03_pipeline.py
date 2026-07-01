import base64
from pathlib import Path
import streamlit as st
from PIL import Image

from utils.i18n import t
from services.plate_detection_service import PlateDetectionService
from services.detection_service import DetectionService
from services.cropping_service import CroppingService
from services.padding_service import PaddingService
from services.crop_measurement_service import CropMeasurementService
from services.area_scaling_service import AreaScalingService
from services.classification_service import ClassificationService
from app_config.settings import EXAMPLE_IMAGES_DIR

st.title(t("pipeline.title"))
st.markdown(t("pipeline.subtitle"))

show_tutorial = st.checkbox(t("pipeline.show_tutorial"))

if show_tutorial:
    with st.expander("\U0001f4d6 " + t("pipeline.tutorial.title"), expanded=True):
        col_text, col_demo = st.columns([1, 1])

        with col_text:
            for i in range(7):
                st.markdown(t(f"pipeline.tutorial.{i}"))
                if i < 6:
                    st.markdown("<h3 style='text-align:center;'>\u2193</h3>", unsafe_allow_html=True)

        with col_demo:
            st.markdown(f"### \U0001f9e0 {t('tutorial.demo.title')}")
            st.markdown(t("tutorial.demo.desc"))

            if st.button("\U000025b6 " + t("tutorial.demo.button"), use_container_width=True):
                st.session_state.tutorial_step = 1
                st.session_state.tutorial_data = {}
                st.rerun()

            st.divider()

            step = st.session_state.get("tutorial_step", 0)

            if step >= 1:
                example_path = Path(EXAMPLE_IMAGES_DIR) / "11_CAAL.jpg"
                if not example_path.exists():
                    st.error("Example image not found.")
                else:
                    image = Image.open(example_path).convert("RGB")
                    data = st.session_state.tutorial_data

                    # ── Step 1: Upload / Load ──
                    if step >= 1:
                        st.success("\U00002705 " + t("tutorial.step1.label"))
                        if step == 1:
                            st.image(image, width=500, caption="11_CAAL.jpg — 11 C. albicans colonies")
                            st.markdown(t("tutorial.step1.detail"))
                            if st.button(t("tutorial.next"), key="next1", use_container_width=True):
                                st.session_state.tutorial_step = 2
                                st.rerun()

                    # ── Step 2: Plate detection ──
                    if step >= 2:
                        st.success("\U00002705 " + t("tutorial.step2.label"))
                        if "plate" not in data:
                            plate = PlateDetectionService().detect_plate(image, debug=True)
                            data["plate"] = plate
                            st.session_state.tutorial_data = data
                        plate = data["plate"]
                        if step == 2:
                            col1, col2 = st.columns([3, 2])
                            with col1:
                                if plate.get("debug_image"):
                                    st.image(plate["debug_image"],
                                             caption=t("tutorial.plate_detected"),
                                             use_container_width=True)
                            with col2:
                                if plate["detected"]:
                                    st.metric(t("tutorial.plate.diameter"), f"{plate['diameter_px']} px")
                                    st.metric(t("tutorial.plate.mm_per_px"), f"{plate['mm_per_pixel']:.6f}")
                                    st.metric(t("tutorial.plate.area"), f"{plate['area_px']:.0f} px\u00b2")
                                else:
                                    st.warning(t("tutorial.plate.not_found"))
                            st.markdown(t("tutorial.step2.detail"))
                            if st.button(t("tutorial.next"), key="next2", use_container_width=True):
                                st.session_state.tutorial_step = 3
                                st.rerun()

                    # ── Step 3: Colony detection ──
                    if step >= 3:
                        st.success("\U00002705 " + t("tutorial.step3.label"))
                        if "detections" not in data:
                            result = DetectionService().detect(image, detection_mode="full")
                            data["detections"] = result["detections"]
                            data["detection_count"] = result["count"]
                            data["detection_time"] = result["time_s"]
                            st.session_state.tutorial_data = data
                        detections = data["detections"]
                        if step == 3:
                            from services.detection_service import DetectionService as DS
                            img_with_boxes = DS().draw_boxes(image, detections)
                            st.image(img_with_boxes, width=500,
                                     caption=t("tutorial.detect.count").format(count=data["detection_count"]))
                            st.markdown(t("tutorial.step3.detail"))
                            if st.button(t("tutorial.next"), key="next3", use_container_width=True):
                                st.session_state.tutorial_step = 4
                                st.rerun()

                    # ── Step 4: Crop + Padding ──
                    if step >= 4:
                        st.success("\U00002705 " + t("tutorial.step4.label"))
                        if "padded_crops" not in data:
                            cropper = CroppingService()
                            padder = PaddingService()
                            raw = cropper.raw_crops(image, detections)
                            padded = padder.pad_crops(raw)
                            data["raw_crops"] = raw
                            data["padded_crops"] = padded
                            st.session_state.tutorial_data = data
                        raw_crops = data["raw_crops"]
                        padded_crops = data["padded_crops"]
                        data["demo_crops"] = raw_crops[:3]
                        data["demo_padded"] = padded_crops[:3]
                        if step == 4:
                            n_show = min(3, len(raw_crops))
                            st.markdown(t("tutorial.crop.count").format(count=len(raw_crops)))
                            for i in range(n_show):
                                col_r, col_p = st.columns(2)
                                with col_r:
                                    st.image(raw_crops[i], width=150,
                                             caption=f"{t('tutorial.crop.raw')} #{i+1} ({raw_crops[i].size[0]}x{raw_crops[i].size[1]})")
                                with col_p:
                                    st.image(padded_crops[i], width=150,
                                             caption=f"{t('tutorial.crop.padded')} #{i+1} (224x224)")
                            st.markdown(t("tutorial.step4.detail"))
                            if st.button(t("tutorial.next"), key="next4", use_container_width=True):
                                st.session_state.tutorial_step = 5
                                st.rerun()

                    # ── Step 5: AI Prediction ──
                    if step >= 5:
                        st.success("\U00002705 " + t("tutorial.step5.label"))
                        if "classifications" not in data:
                            classifier = ClassificationService()
                            classifications = classifier.classify(padded_crops[:3])
                            data["classifications"] = classifications
                            st.session_state.tutorial_data = data
                        classifications = data["classifications"]
                        demo_padded = data["demo_padded"]
                        if step == 5:
                            n_show = min(3, len(classifications))
                            for i in range(n_show):
                                st.markdown(f"**{t('detect.colony.label').format(number=i+1)}**")
                                col_img, col_pred = st.columns([1, 2])
                                with col_img:
                                    st.image(demo_padded[i], width=150)
                                with col_pred:
                                    st.markdown(f"**{t('detect.species.label')}:** {classifications[i]['species']}")
                                    st.markdown(f"**{t('detect.confidence.label')}:** {classifications[i]['confidence']:.2%}")
                            st.markdown(t("tutorial.step5.detail"))
                            if st.button(t("tutorial.next"), key="next5", use_container_width=True):
                                st.session_state.tutorial_step = 6
                                st.rerun()

                    # ── Step 6: Classification result ──
                    if step >= 6:
                        st.success("\U00002705 " + t("tutorial.step6.label"))
                        classifications = data.get("classifications", [])
                        if step == 6:
                            from collections import Counter
                            n_show = min(3, len(classifications))
                            for i in range(n_show):
                                cls = classifications[i]
                                st.markdown(f"**{t('detect.colony.label').format(number=i+1)}**")
                                st.markdown(f"- {t('detect.species.label')}: **{cls['species']}**")
                                st.markdown(f"- {t('detect.confidence.label')}: {cls['confidence']:.2%}")
                                if cls.get("probabilities"):
                                    with st.expander(t("detect.probabilities.title")):
                                        for sp, prob in cls["probabilities"].items():
                                            st.markdown(f"{sp}: `{prob:.4f}`")
                                st.divider()
                            st.markdown(t("tutorial.step6.detail"))
                            st.balloons()
                            if st.button("\U0001f504 " + t("tutorial.restart"), use_container_width=True):
                                st.session_state.tutorial_step = 0
                                st.session_state.tutorial_data = {}
                                st.rerun()

                    if step >= 1:
                        st.progress(min(step / 6, 1.0))

st.divider()

steps = [
    (
        t("pipeline.step1.title"),
        t("pipeline.step1.desc"),
        t("pipeline.step1.source"),
    ),
    (
        t("pipeline.step2.title"),
        t("pipeline.step2.desc"),
        t("pipeline.step2.source"),
    ),
    (
        t("pipeline.step3.title"),
        t("pipeline.step3.desc"),
        t("pipeline.step3.source"),
    ),
    (
        t("pipeline.step4.title"),
        t("pipeline.step4.desc"),
        t("pipeline.step4.source"),
    ),
    (
        t("pipeline.step5.title"),
        t("pipeline.step5.desc"),
        t("pipeline.step5.source"),
    ),
    (
        t("pipeline.step6.title"),
        t("pipeline.step6.desc"),
        t("pipeline.step6.source"),
    ),
    (
        t("pipeline.step7.title"),
        t("pipeline.step7.desc"),
        t("pipeline.step7.source"),
    ),
]

for i, (title, desc, source) in enumerate(steps, 1):
    with st.container():
        cols = st.columns([1, 4, 2])
        with cols[0]:
            st.markdown(f"## {i}")
        with cols[1]:
            st.subheader(title, anchor=False)
            st.markdown(desc)
        with cols[2]:
            st.code(source, language="text")
    if i < len(steps):
        st.markdown("<h3 style='text-align:center;'>\u2193</h3>", unsafe_allow_html=True)
    st.divider()
