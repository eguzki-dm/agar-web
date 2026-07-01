import streamlit as st
from utils.i18n import t

st.title(t("learn.title"))
st.markdown(t("learn.subtitle"))

for i in range(1, 13):
    with st.expander(t(f"learn.concept_{i}.title")):
        st.markdown(t(f"learn.concept_{i}.content"))

st.divider()

st.subheader(t("learn.pipeline.title"))
st.markdown(t("learn.pipeline.intro"))

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1], gap="small")
icons = ["📷", "🟦", "✂️", "📏", "🧠"]
labels = [
    t("learn.pipeline.step1"),
    t("learn.pipeline.step2"),
    t("learn.pipeline.step3"),
    t("learn.pipeline.step4"),
    t("learn.pipeline.step5"),
]
for col, icon, label in zip([col1, col2, col3, col4], icons[:4], labels[:4]):
    with col:
        st.markdown(
            f"""<div style="text-align:center;padding:1rem;border:1px solid #ccc;
                border-radius:8px;height:130px;display:flex;flex-direction:column;
                justify-content:center;">
                <div style="font-size:2.5rem;">{icon}</div>
                <div style="font-size:0.8rem;margin-top:0.5rem;">{label}</div>
            </div>""",
            unsafe_allow_html=True,
        )

st.markdown(
    """<p style="text-align:center;font-size:1.5rem;margin:0.5rem 0;">→</p>""",
    unsafe_allow_html=True,
)

col6, col7, col8 = st.columns(3)
with col6:
    st.markdown(
        f"""<div style="text-align:center;padding:1rem;border:1px solid #ccc;
            border-radius:8px;height:130px;display:flex;flex-direction:column;
            justify-content:center;">
            <div style="font-size:2.5rem;">🔬</div>
            <div style="font-size:0.8rem;margin-top:0.5rem;">{t('learn.pipeline.step5')}</div>
        </div>""",
        unsafe_allow_html=True,
    )
with col7:
    st.markdown(
        f"""<div style="text-align:center;padding:1rem;border:1px solid #ccc;
            border-radius:8px;height:130px;display:flex;flex-direction:column;
            justify-content:center;">
            <div style="font-size:2.5rem;">🏷️</div>
            <div style="font-size:0.8rem;margin-top:0.5rem;">{t('learn.pipeline.step6')}</div>
        </div>""",
        unsafe_allow_html=True,
    )
with col8:
    st.markdown(
        f"""<div style="text-align:center;padding:1rem;border:1px solid #ccc;
            border-radius:8px;height:130px;display:flex;flex-direction:column;
            justify-content:center;">
            <div style="font-size:2.5rem;">🔥</div>
            <div style="font-size:0.8rem;margin-top:0.5rem;">{t('learn.pipeline.step7')}</div>
        </div>""",
        unsafe_allow_html=True,
    )

st.divider()
st.markdown(t("learn.pipeline.detail"))
