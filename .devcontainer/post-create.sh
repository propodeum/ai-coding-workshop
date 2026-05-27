#!/usr/bin/env bash
set -euo pipefail

# Copy env template if not present
cp -n .env.example .env 2>/dev/null || true

# Wire frontend → backend URL for Codespaces, so fetch() from the browser works
if [ -n "${CODESPACE_NAME:-}" ]; then
  cat > frontend/.env.local <<EOF
NEXT_PUBLIC_API_URL=https://${CODESPACE_NAME}-8000.app.github.dev
EOF
fi

# Install all dependencies up front
just install

echo "Setup complete."
