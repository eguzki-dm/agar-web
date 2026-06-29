import streamlit as st
from utils.i18n import t

DILUTION_OPTIONS = {
    "10\u207b\u00b9": -1,
    "10\u207b\u00b2": -2,
    "10\u207b\u00b3": -3,
    "10\u207b\u2074": -4,
    "10\u207b\u2075": -5,
    "10\u207b\u2076": -6,
    "10\u207b\u2077": -7,
    "10\u207b\u2078": -8,
}

_SUPERSCRIPT = str.maketrans("0123456789", "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079")


def _format_scientific(value: float) -> str:
    mantissa, exp_str = f"{value:.2e}".split("e")
    exp = int(exp_str)
    mantissa_float = float(mantissa)
    mantissa_display = f"{mantissa_float:.2f}".rstrip("0").rstrip(".")
    exp_superscript = str(exp).translate(_SUPERSCRIPT)
    return f"{mantissa_display} \u00d7 10{exp_superscript}"


def _validation_message(colony_count: int) -> str | None:
    if colony_count < 30:
        return t("results.cfu.validation.low")
    elif colony_count <= 300:
        return t("results.cfu.validation.valid")
    else:
        return t("results.cfu.validation.high")


def render_cfu_calculator():
    colony_count_source = len(st.session_state.get("detections", []))
    initial_colony = colony_count_source if colony_count_source > 0 else st.session_state.cfu_colony_count

    st.markdown(f"### {t('results.cfu.title')}")
    st.markdown(f"> {t('results.cfu.subtitle')}")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        colony_count = st.number_input(
            t("results.cfu.colony_count"),
            min_value=0,
            max_value=9999,
            value=initial_colony,
            step=1,
            key="cfu_colony_count_input",
        )
        st.session_state.cfu_colony_count = colony_count

        sample_type = st.radio(
            t("results.cfu.sample_type"),
            [t("results.cfu.liquid"), t("results.cfu.solid")],
            index=0 if st.session_state.cfu_sample_type == "Liquid" else 1,
            key="cfu_sample_type_input",
        )
        st.session_state.cfu_sample_type = "Liquid" if sample_type == t("results.cfu.liquid") else "Solid"

    with col2:
        dilution_label = st.selectbox(
            t("results.cfu.dilution"),
            list(DILUTION_OPTIONS.keys()),
            index=abs(st.session_state.cfu_dilution_exponent) - 1 if -9 < st.session_state.cfu_dilution_exponent < 0 else 0,
            key="cfu_dilution_input",
        )
        st.session_state.cfu_dilution_exponent = DILUTION_OPTIONS[dilution_label]

        volume = st.number_input(
            t("results.cfu.volume"),
            min_value=0.0,
            max_value=10.0,
            value=st.session_state.cfu_volume_plated,
            step=0.01,
            format="%.2f",
            key="cfu_volume_input",
        )
        st.session_state.cfu_volume_plated = volume

    st.divider()

    errors = []
    if colony_count <= 0:
        errors.append(t("results.cfu.error.colonies"))
    if volume <= 0:
        errors.append(t("results.cfu.error.volume"))
    if st.session_state.cfu_dilution_exponent is None:
        errors.append(t("results.cfu.error.dilution"))

    if errors:
        for err in errors:
            st.error(err)
        return

    dilution_factor = 10 ** st.session_state.cfu_dilution_exponent
    cfu = colony_count / (dilution_factor * volume)

    unit = t("results.cfu.unit_g") if st.session_state.cfu_sample_type == "Solid" else t("results.cfu.unit_ml")

    st.markdown(
        f"""
        <div style="
            background-color: #f8f9fa;
            border: 2px solid #dda4f7;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            margin-bottom: 1rem;
        ">
            <p style="font-size: 1rem; color: #666; margin: 0 0 0.5rem 0;">
                {t('results.cfu.result')}
            </p>
            <p style="font-size: 2rem; font-weight: 700; color: #1a1a1a; margin: 0.5rem 0;">
                {_format_scientific(cfu)} {unit}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    validation_msg = _validation_message(colony_count)
    if validation_msg:
        st.markdown(validation_msg)

    st.markdown(
        f"""
        <div style="
            background-color: #fff3cd;
            border: 1px solid #ffc107;
            border-radius: 8px;
            padding: 0.8rem 1rem;
            margin-top: 0.5rem;
            font-size: 0.85rem;
            color: #664d03;
        ">
            \u26a0\ufe0f {t('results.cfu.disclaimer')}
        </div>
        """,
        unsafe_allow_html=True,
    )
