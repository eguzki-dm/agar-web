import streamlit as st

_DARK_CSS = """
.logo-wrapper {
    background: white !important;
    border-radius: 8px !important;
    padding: 8px !important;
}
.disclaimer-card {
    background-color: #3d3200 !important;
    border-color: #ffc107 !important;
    color: #ffecb0 !important;
}
.disclaimer-card strong {
    color: #ffc107;
}
.disclaimer-banner {
    background-color: #4a1515 !important;
    border-color: #dc3545 !important;
}
.disclaimer-banner h2,
.disclaimer-banner p {
    color: #f5c6cb !important;
}
.feature-card {
    background-color: #2d2d2d !important;
    border-color: #444 !important;
    color: #ddd !important;
}
.step-card-1 {
    background: #1a3a5c !important;
    border-color: #1565c0 !important;
}
.step-card-1 div {
    color: #90caf9 !important;
}
.step-card-2 {
    background: #3d2b1a !important;
    border-color: #e65100 !important;
}
.step-card-2 div {
    color: #ffcc80 !important;
}
.step-card-3 {
    background: #2a1a3d !important;
    border-color: #6a1b9a !important;
}
.step-card-3 div {
    color: #ce93d8 !important;
}
.step-card-4 {
    background: #1a3d1a !important;
    border-color: #2e7d32 !important;
}
.step-card-4 div {
    color: #a5d6a7 !important;
}
.step-card-5 {
    background: #3d3200 !important;
    border-color: #f9a825 !important;
}
.step-card-5 div {
    color: #fff176 !important;
}
"""


def inject_theme_css():
    if st.get_option("theme.base") == "dark":
        st.markdown(f"<style>{_DARK_CSS}</style>", unsafe_allow_html=True)
    else:
        st.markdown("<style></style>", unsafe_allow_html=True)
