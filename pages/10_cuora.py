import base64
import streamlit as st

from utils.auth import check_authentication, render_login_page, logout as auth_logout
from utils.i18n import t, get_language
from utils.llm import DEFAULT_MODEL, stream_response
from utils.session_state import clear_chat, add_message, export_conversation

with open("icons/Cuora.png", "rb") as f:
    cuora_avatar = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"

if not check_authentication():
    render_login_page()
    st.stop()

user = st.session_state.get("user", {})
name = user.get("name", t("cuora.default_name"))
pic = user.get("picture", "")

st.markdown(
    f'<div style="text-align:center;margin-bottom:1.5rem;">'
    f"<h1>{t('cuora.title')}</h1>"
    f'<p style="font-size:0.95rem;opacity:0.8;">'
    f"{t('cuora.subtitle')}"
    f'</p>'
    f'</div>',
    unsafe_allow_html=True,
)

if pic:
    st.markdown(
        f'<div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-bottom:1rem;">'
        f'<img src="{pic}" style="width:36px;height:36px;border-radius:50%" referrerpolicy="no-referrer"/>'
        f'<span style="font-weight:600">{name}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )
else:
    st.markdown(f'<p style="text-align:center;">👤 <strong>{name}</strong></p>', unsafe_allow_html=True)

col_clear, col_export, col_logout = st.columns([1, 1, 1])
with col_clear:
    if st.button(t("cuora.clear_chat"), use_container_width=True):
        clear_chat()
        st.rerun()
with col_export:
    if st.session_state.get("messages"):
        export_text = export_conversation()
        st.download_button(
            t("cuora.export"),
            data=export_text,
            file_name=f"cuora_{st.session_state.get('session_id', 'chat')}.txt",
            mime="text/plain",
            use_container_width=True,
        )
with col_logout:
    if st.button(t("cuora.logout"), use_container_width=True):
        auth_logout()

messages_container = st.container()
with messages_container:
    for msg in st.session_state.get("messages", []):
        avatar = cuora_avatar if msg["role"] == "assistant" else None
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

api_key = st.secrets.get("GROQ_API_KEY", "")

if not api_key:
    st.error(t("cuora.api_key_error"))
    st.stop()

user_input = st.chat_input(t("cuora.chat_placeholder"))

if user_input:
    add_message("user", user_input)

    with messages_container:
        with st.chat_message("user"):
            st.markdown(user_input)

    llm_messages = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state["messages"]
    ]

    with messages_container:
        with st.chat_message("assistant", avatar=cuora_avatar):
            placeholder = st.empty()
            placeholder.markdown(t("cuora.analyzing"))
            full = ""
            try:
                for chunk in stream_response(
                    messages=llm_messages,
                    api_key=api_key,
                    model=DEFAULT_MODEL,
                    temperature=0.1,
                    system_prompt=t("cuora.prompt"),
                ):
                    if not full:
                        placeholder.markdown("")
                    full += chunk
                    placeholder.markdown(full + "▌")
                placeholder.markdown(full)
            except Exception as e:
                full = f"[Error] {e}"
                placeholder.error(full)

    add_message("assistant", full)
    st.rerun()
