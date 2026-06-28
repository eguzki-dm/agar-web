from PIL import Image, ImageDraw
import streamlit as st

from app_config.settings import DETECTION_COLORS


def draw_boxes(
    image: Image.Image,
    detections: list[dict],
    show_labels: bool = True,
) -> Image.Image:
    img_copy = image.copy()
    draw = ImageDraw.Draw(img_copy)

    for i, det in enumerate(detections):
        box = det["box"]
        color = DETECTION_COLORS[i % len(DETECTION_COLORS)]
        draw.rectangle(box, outline=color, width=3)

        if show_labels:
            confidence = det.get("confidence", 1.0)
            label = f"#{i + 1} ({confidence:.2f})"
            x1, y1, _, _ = box
            text_position = (x1 + 3, y1 - 14)
            draw.text(text_position, label, fill=color)

    return img_copy


def show_image_with_boxes(image: Image.Image, detections: list[dict], caption: str = ""):
    annotated = draw_boxes(image, detections)
    st.image(annotated, caption=caption, use_container_width=True)


def show_crops_grid(crops: list, classifications: list, cols: int = 3):
    if not crops:
        return

    for i in range(0, len(crops), cols):
        row_crops = crops[i : i + cols]
        row_class = classifications[i : i + cols] if classifications else []
        columns = st.columns(cols)

        for j, col in enumerate(columns):
            if j < len(row_crops):
                with col:
                    st.image(row_crops[j], use_container_width=True)
                    if j < len(row_class):
                        c = row_class[j]
                        st.caption(f"{c['species']} ({c['confidence']:.0%})")


def display_crop_pipeline_step(step_number: int, title: str, description: str, image=None):
    st.subheader(title, anchor=False)
    st.markdown(description)
    if image is not None:
        st.image(image, use_container_width=True)
    st.divider()
