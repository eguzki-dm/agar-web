import streamlit as st

from locales.en import TRANSLATIONS as EN
from locales.es import TRANSLATIONS as ES

LANGUAGES = {
    "en": EN,
    "es": ES,
}


def get_language() -> str:
    return st.session_state.get("language", "en")


def t(key: str) -> str:
    lang = get_language()
    translations = LANGUAGES.get(lang, EN)
    if key in translations:
        return translations[key]
    if key in EN:
        return EN[key]
    return key


def get_localized_field(data: dict, field: str) -> str | list:
    lang = get_language()
    entry = data.get(field, "")
    if isinstance(entry, dict):
        return entry.get(lang, entry.get("en", ""))
    return entry
