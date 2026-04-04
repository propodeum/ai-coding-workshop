# Python 3.12 + Node.js 20 on Debian Bookworm
FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

# Install Node.js 20.x
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
