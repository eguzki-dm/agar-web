import streamlit as st


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


def has_detections():
    return len(st.session_state.detections) > 0


def has_classifications():
    return len(st.session_state.classifications) > 0


def clear_pipeline():
    st.session_state.detections = []
    st.session_state.classifications = []
    st.session_state.run_metadata = {}
