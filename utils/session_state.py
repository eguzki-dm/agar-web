import streamlit as st
from datetime import datetime


def init_session_state():
    if "original_image" not in st.session_state:
        st.session_state.original_image = None
    if "detections" not in st.session_state:
        st.session_state.detections = []
    if "classifications" not in st.session_state:
        st.session_state.classifications = []
    if "run_metadata" not in st.session_state:
        st.session_state.run_metadata = {}
    if "language" not in st.session_state:
        st.session_state.language = "en"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    if "cfu_colony_count" not in st.session_state:
        st.session_state.cfu_colony_count = 0
    if "cfu_sample_type" not in st.session_state:
        st.session_state.cfu_sample_type = "Liquid"
    if "cfu_dilution_exponent" not in st.session_state:
        st.session_state.cfu_dilution_exponent = -1
    if "cfu_volume_plated" not in st.session_state:
        st.session_state.cfu_volume_plated = 0.1


def has_detections():
    return len(st.session_state.detections) > 0


def has_classifications():
    return len(st.session_state.classifications) > 0


def clear_pipeline():
    st.session_state.detections = []
    st.session_state.classifications = []
    st.session_state.run_metadata = {}


def clear_chat():
    st.session_state.messages = []


def add_message(role: str, content: str):
    msg = {
        "role": role,
        "content": content,
        "timestamp": datetime.now().strftime("%H:%M"),
    }
    st.session_state.messages.append(msg)


def export_conversation() -> str:
    lines = [
        f"# Cuora — Sesión {st.session_state.get('session_id', 'N/A')}",
        "---",
    ]
    for msg in st.session_state.get("messages", []):
        role_label = "Tú" if msg["role"] == "user" else "Cuora"
        lines.append(f"\n[{msg['timestamp']}] {role_label}:")
        lines.append(msg["content"])
    return "\n".join(lines)
