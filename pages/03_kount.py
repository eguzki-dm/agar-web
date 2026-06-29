import json
import base64
from pathlib import Path
from datetime import datetime
import streamlit as st
from PIL import Image

from services.detection_service import DetectionService
from components.image_viewer import show_image_with_boxes
from components.charts import metrics_dashboard
from utils.i18n import t
from utils.session_state import init_session_state
from app_config.settings import EXAMPLE_IMAGES_DIR, RESULTS_DIR

init_session_state()

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

upload_tab, examples_tab = st.tabs([
    t("kount.tab.upload"),
    t("kount.tab.examples"),
])

with upload_tab:
    uploaded_file = st.file_uploader(
        t("kount.upload.label"),
        type=["png", "jpg", "jpeg"],
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.session_state.original_image = image
        st.success(t("kount.status.loaded"))

with examples_tab:
    st.markdown(t("kount.examples.select"))

    example_dir = Path(EXAMPLE_IMAGES_DIR)
    example_extensions = ("*.jpg", "*.jpeg", "*.png")
    example_files = []
    for ext in example_extensions:
        example_files.extend(example_dir.glob(ext))
    example_files = sorted(example_files)

    if not example_files:
        st.info(t("kount.examples.none"))
    else:
        cols = st.columns(3)
        for idx, img_path in enumerate(example_files):
            with cols[idx % 3]:
                thumb = Image.open(img_path).convert("RGB")
                st.image(thumb, width="stretch")
                fname = img_path.name
                if st.button(fname, key=f"example_{idx}", width="stretch"):
                    st.session_state.original_image = thumb.copy()
                    st.success(t("kount.status.loaded"))
                    st.rerun()

st.divider()

if st.session_state.original_image is not None:
    st.subheader(t("kount.loaded_image"))
    st.image(st.session_state.original_image, width="stretch")

    if st.button(t("kount.detect.button"), type="primary", width="stretch"):
        with st.spinner(t("kount.detect.button")):
            result = detector.detect(st.session_state.original_image)

        detections = result["detections"]
        st.session_state.detections = detections

        metadata = st.session_state.run_metadata
        metadata["detection_time_s"] = result["time_s"]

        st.success(t("kount.status.detected").format(count=result["count"], time=result["time_s"]))

        st.subheader(t("kount.detection_result"))
        show_image_with_boxes(
            st.session_state.original_image,
            detections,
            caption=t("kount.status.detected").format(count=result["count"], time=result["time_s"]),
        )

        metrics_dashboard(
            detections,
            st.session_state.classifications,
            st.session_state.run_metadata,
        )

        st.divider()

        json_data = json.dumps({
            "session_id": st.session_state.get("session_id", datetime.now().strftime("%Y%m%d_%H%M%S")),
            "timestamp": datetime.now().isoformat(),
            "total_detections": result["count"],
            "time_s": result["time_s"],
            "image_size": st.session_state.original_image.size,
            "detections": [
                {
                    "box": d["box"],
                    "confidence": d["confidence"],
                }
                for d in detections
            ],
        }, indent=2)

        col_json, _ = st.columns([1, 3])
        with col_json:
            st.download_button(
                label=t("kount.download_json"),
                data=json_data,
                file_name=f"kount_detections_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                width="stretch",
            )

        Path(RESULTS_DIR).mkdir(parents=True, exist_ok=True)
        json_path = Path(RESULTS_DIR) / f"kount_detections_{st.session_state.get('session_id', 'unknown')}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(json_data)

    st.divider()

    next_btn = st.button(
        t("kount.next.button"),
        width="stretch",
        disabled=not st.session_state.detections,
    )
    if next_btn:
        st.switch_page("pages/04_detect.py")
else:
    st.info(t("kount.no_image"))
