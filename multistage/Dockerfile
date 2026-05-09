# Dockerfile --> multistage optimized image

# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy dependency file
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Copy runtime dependencies only
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application
COPY app/app.py .

# Create non-root user
RUN useradd -m appuser

# Switch user
USER appuser

# Run application
CMD ["python", "app.py"]
