import time
import base64
import streamlit as st

from services.detection_service import DetectionService
from components.image_viewer import show_image_with_boxes
from components.charts import metrics_dashboard
from utils.i18n import t

with open("icons/uKount.png", "rb") as f:
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
st.title(t("kount.title"))
st.markdown(t("kount.subtitle"))

detector = DetectionService()

upload_tab, synthetic_tab = st.tabs([t("kount.tab.upload"), t("kount.tab.synthetic")])

with upload_tab:
    uploaded_file = st.file_uploader(
        t("kount.upload.label"),
        type=["png", "jpg", "jpeg"],
    )

    if uploaded_file is not None:
        from PIL import Image

        image = Image.open(uploaded_file).convert("RGB")
        st.session_state.original_image = image
        st.success(t("kount.status.loaded"))

with synthetic_tab:
    st.markdown(t("kount.synthetic.desc"))

    col_w, col_h = st.columns(2)
    with col_w:
        synth_width = st.slider(t("kount.synthetic.width"), 400, 1200, 800, key="synth_w")
    with col_h:
        synth_height = st.slider(t("kount.synthetic.height"), 300, 900, 600, key="synth_h")

    if st.button(t("kount.synthetic.button"), use_container_width=True):
        with st.spinner(t("kount.tab.synthetic")):
            time.sleep(0.5)
            image, _ = detector.generate_synthetic_plate(synth_width, synth_height)
            st.session_state.original_image = image
            st.success(t("kount.status.generated"))
            st.rerun()

st.divider()

if st.session_state.original_image is not None:
    st.subheader(t("kount.loaded_image"))
    st.image(st.session_state.original_image, use_container_width=True)

    if st.button(t("kount.detect.button"), type="primary", use_container_width=True):
        with st.spinner(t("kount.detect.button")):
            result = detector.detect(st.session_state.original_image)

        detections = result["detections"]
        st.session_state.detections = detections

        metadata = st.session_state.run_metadata
        metadata["detection_time_ms"] = result["time_ms"]

        st.success(t("kount.status.detected").format(count=result["count"], time=result["time_ms"]))

        st.subheader(t("kount.detection_result"))
        show_image_with_boxes(
            st.session_state.original_image,
            detections,
            caption=t("kount.status.detected").format(count=result["count"], time=result["time_ms"]),
        )

        metrics_dashboard(
            detections,
            st.session_state.classifications,
            st.session_state.run_metadata,
        )

    st.divider()

    if st.session_state.detections:
        if st.button(t("kount.next.button"), use_container_width=True):
            st.switch_page("pages/04_detect.py")
else:
    st.info(t("kount.no_image"))
