"""OpenRouter LLM client.

OpenRouter is OpenAI-compatible, so we use the official `openai` SDK
pointed at OpenRouter's base URL. Browse models at https://openrouter.ai/models.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DEFAULT_MODEL = "openai/gpt-4o-mini"


def _client() -> OpenAI:
    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set. Add it to .env "
            "(get a key at https://openrouter.ai/keys)."
        )
    return OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)


def chat(message: str, model: str = DEFAULT_MODEL) -> str:
    """Send a single user message, return the assistant's reply."""
    response = _client().chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content or ""
