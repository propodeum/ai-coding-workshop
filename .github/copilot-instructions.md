# Copilot Instructions

<!-- ─────────────────────────────────────────────────────────────────── -->
<!-- BEGIN: workshop baseline — do not edit during the workshop          -->
<!-- ─────────────────────────────────────────────────────────────────── -->

## Stack

- Frontend: Next.js 15 (App Router, TypeScript) in `frontend/`
- Backend: FastAPI (Python 3.12) in `backend/`
- Package managers: `npm` (frontend), `uv` (backend)
- Task runner: `just`

## How to run things

- Start everything: `just dev`
- Install dependencies: `just install`
- See all commands: `just`

Do not suggest `python main.py`, raw `uvicorn ...`, or `pip install` — use `just` and `uv` instead.

## Adding dependencies

- Backend: `cd backend && uv add <package>` (not `pip install`)
- Frontend: `cd frontend && npm install <package>`

## Calling an LLM

Use the existing client. Do not add a new SDK or wrap a new HTTP call.

```python
from llm import chat
reply = chat("your prompt here")
```

It is configured for OpenRouter; the API key lives in `.env` as `OPENROUTER_API_KEY`. Browse models at https://openrouter.ai/models. To use a different model, pass `model="provider/name"` to `chat()`.

## Environment

- Secrets go in `.env` (root). Never commit it.
- Anything the browser needs goes in `frontend/.env.local` and must be prefixed `NEXT_PUBLIC_`.
- Never put secrets in `NEXT_PUBLIC_*` — they ship to the browser.

<!-- ─────────────────────────────────────────────────────────────────── -->
<!-- END: workshop baseline                                              -->
<!-- ─────────────────────────────────────────────────────────────────── -->


<!-- ─────────────────────────────────────────────────────────────────── -->
<!-- Your rules — add anything you want the AI to do or avoid below.     -->
<!-- ─────────────────────────────────────────────────────────────────── -->

## My rules
