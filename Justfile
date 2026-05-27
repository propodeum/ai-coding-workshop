set shell := ["bash", "-uc"]

# Show available commands
default:
    @just --list --unsorted

# Install all dependencies (frontend + backend)
install:
    cd frontend && npm install
    cd backend && uv sync

# Start frontend and backend together
dev:
    #!/usr/bin/env bash
    set -uo pipefail
    trap 'kill 0' EXIT INT TERM
    echo ""
    echo "  Frontend → http://localhost:3000"
    echo "  Backend  → http://localhost:8000"
    echo ""
    echo "  In Codespaces, open the Ports tab and click the globe icon on port 3000."
    echo ""
    (cd backend && uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000) &
    (cd frontend && npm run dev) &
    wait

# Start only the frontend
frontend:
    cd frontend && npm run dev

# Start only the backend
backend:
    cd backend && uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
