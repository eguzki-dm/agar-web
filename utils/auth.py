import streamlit as st
import json
import base64
from utils.i18n import t


def get_oauth_config() -> dict:
    return {
        "client_id": st.secrets["GOOGLE_CLIENT_ID"],
        "client_secret": st.secrets["GOOGLE_CLIENT_SECRET"],
        "redirect_uri": st.secrets.get("REDIRECT_URI", "http://localhost:8501"),
    }


def check_authentication() -> bool:
    return st.session_state.get("authenticated", False)


def render_login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            f'<div style="text-align:center;padding:2rem;border-radius:12px;'
            f'border:1px solid #dee2e6;margin-top:3rem;">'
            f"<h1 style='font-size:2rem;'>{t('cuora.title')}</h1>"
            f"<p style='margin-bottom:2rem;opacity:0.8;'>"
            f"{t('cuora.login_title')}"
            f"</p>"
            f"</div>",
            unsafe_allow_html=True,
        )

        try:
            from streamlit_oauth import OAuth2Component

            cfg = get_oauth_config()
            if not cfg["client_id"]:
                st.error(t("cuora.login_error"))
                return

            oauth2 = OAuth2Component(
                client_id=cfg["client_id"],
                client_secret=cfg["client_secret"],
                authorize_endpoint="https://accounts.google.com/o/oauth2/v2/auth",
                token_endpoint="https://oauth2.googleapis.com/token",
                refresh_token_endpoint="https://oauth2.googleapis.com/token",
                revoke_token_endpoint="https://oauth2.googleapis.com/revoke",
            )

            result = oauth2.authorize_button(
                name=t("cuora.login_button"),
                redirect_uri=cfg["redirect_uri"],
                scope="openid email profile",
                width="stretch",
            )

            if result and "token" in result:
                _process_oauth_result(result)

        except ImportError:
            st.warning(t("cuora.oauth_missing"))
            _render_dev_bypass()


def _process_oauth_result(result: dict):
    token = result["token"]
    id_token = token.get("id_token", "")
    try:
        payload = id_token.split(".")[1]
        payload += "=" * (4 - len(payload) % 4)
        user_info = json.loads(base64.urlsafe_b64decode(payload))
    except Exception:
        user_info = {}

    st.session_state["authenticated"] = True
    st.session_state["user"] = {
        "email": user_info.get("email", "usuario@desconocido.com"),
        "name": user_info.get("name", "Usuario"),
        "picture": user_info.get("picture", ""),
    }
    st.rerun()


def _render_dev_bypass():
    st.markdown("---")
    st.caption(t("cuora.dev_mode"))
    name = st.text_input(t("cuora.username_label"))
    if st.button(t("cuora.dev_login")) and name:
        st.session_state["authenticated"] = True
        st.session_state["user"] = {
            "email": f"{name.lower()}@dev.local",
            "name": name,
            "picture": "",
        }
        st.rerun()


def logout():
    keys_to_clear = ["authenticated", "user", "messages", "session_id"]
    for k in keys_to_clear:
        if k in st.session_state:
            del st.session_state[k]
    st.rerun()
