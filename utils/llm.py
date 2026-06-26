from typing import Generator

GROQ_MODELS = [
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
]

DEFAULT_MODEL = "llama-3.1-8b-instant"


def stream_response(
    messages: list[dict],
    api_key: str,
    model: str,
    temperature: float,
    system_prompt: str = "",
) -> Generator[str, None, None]:
    try:
        from groq import Groq

        client = Groq(api_key=api_key)
        groq_messages = [{"role": "system", "content": system_prompt}] + [
            {"role": m["role"], "content": m["content"]} for m in messages
        ]
        stream = client.chat.completions.create(
            model=model,
            messages=groq_messages,
            temperature=temperature,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    except ImportError:
        yield "[Error] Instala: pip install groq"
    except Exception as e:
        yield f"[Error Groq] {e}"


def get_available_models(api_key: str = "") -> list[str]:
    if not api_key:
        return GROQ_MODELS
    try:
        from groq import Groq

        client = Groq(api_key=api_key)
        result = client.models.list()
        models = getattr(result, "data", result) if not isinstance(result, list) else result
        return sorted([m.id for m in models])
    except Exception:
        return GROQ_MODELS


def test_connection(api_key: str) -> tuple[bool, str]:
    try:
        from groq import Groq

        Groq(api_key=api_key).models.list()
        return True, "Groq conectado correctamente"
    except Exception as e:
        return False, str(e)
