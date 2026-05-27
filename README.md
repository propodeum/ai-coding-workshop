# AI Coding Workshop

## Quick Start

1. Click **"Use this template"** → **"Create a new repository"**
2. On your new repo, click the green **Code** button → **Codespaces** tab → **Create codespace on main**
3. Wait for the environment to build (first time takes ~2 minutes)
4. In the terminal, run:

   ```bash
   just dev
   ```

5. Your browser will open the frontend automatically. If not, open the **Ports** tab and click the globe icon on port 3000.

That's it. You're ready to build.

## Using an LLM

The backend ships with an OpenRouter client so you can call any LLM from your code.

1. Get a key at [openrouter.ai/keys](https://openrouter.ai/keys) and paste it into `.env`:

   ```
   OPENROUTER_API_KEY=sk-or-...
   ```

2. From Python, use the helper:

   ```python
   from llm import chat
   reply = chat("Say hi in one word.")
   ```

3. Or hit the example endpoint:

   ```bash
   curl -X POST http://localhost:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Say hi in one word."}'
   ```

Browse models at [openrouter.ai/models](https://openrouter.ai/models). The default is `openai/gpt-4o-mini` — cheap and fast.

## Available commands

Type `just` in the terminal to see all commands:

| Command         | What it does                                   |
|-----------------|------------------------------------------------|
| `just dev`      | Start frontend and backend together            |
| `just install`  | Install all dependencies                       |
| `just frontend` | Run only the frontend                          |
| `just backend`  | Run only the backend                           |

## Project Structure

```
├── backend/          # Python backend (FastAPI)
├── frontend/         # Next.js frontend
├── .devcontainer/    # Codespace configuration
├── Justfile          # Task runner — see `just` for commands
├── .env.example      # Environment variable template
└── .env              # Your local environment variables (auto-created, git-ignored)
```

## Ports

| Port | Service             |
|------|---------------------|
| 3000 | Frontend (Next.js)  |
| 8000 | Backend (FastAPI)   |
