# Multi-stage Dockerfile for todo-list-cli

# Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Copy project files
COPY pyproject.toml .
COPY src/ src/
COPY README.md .
COPY LICENSE .

# Install the package
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Copy installed package from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/todo /usr/local/bin/todo
COPY --from=builder /app /app

# Create a directory for task data
RUN mkdir -p /data
WORKDIR /data

# Set environment variable to disable color when not in TTY
ENV PYTHONUNBUFFERED=1

# Default command
ENTRYPOINT ["todo"]
CMD ["--help"]

# Labels
LABEL maintainer="codeforgood-org"
LABEL description="A powerful command-line todo list manager"
LABEL version="1.0.0"
