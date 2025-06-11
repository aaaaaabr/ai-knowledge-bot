# ---------- Stage 1: Build Layer ----------
FROM python:3.10-slim AS builder

WORKDIR /app

# Avoid interactive prompts + optimize caching
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install pip packages in isolated layer
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt

# ---------- Stage 2: Final Layer ----------
FROM python:3.10-slim

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /install /usr/local
COPY . .

# Security: Create non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expose Streamlit port
EXPOSE 8501

# Entry point
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
