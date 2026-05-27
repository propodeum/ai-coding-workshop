# Python 3.12 + Node.js 20 on Debian Bookworm
FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

# Node.js 20.x
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# just — task runner
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh \
    | bash -s -- --to /usr/local/bin

# uv — fast Python package manager (auto-manages venvs)
RUN pip install --no-cache-dir uv
