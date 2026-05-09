# Dockerfile --> vulnerable
FROM ubuntu:20.04

# Install everything as root (BAD!)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    wget \
    vim \
    netcat \
    nmap \
    telnet \
    git

# Install Python packages
COPY app/requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

# Copy application
COPY app/app.py /app/

# Secrets in image (!BAD)
COPY app/.env.example /app/.env

# Hardcoded secrets (BAD!)
ENV DATABASE_URL="postgresql://admin:SuperSecret123@db:5432/mydb"
ENV API_KEY="sk_live_abc123xyz789"

WORKDIR /app

# Running as root (BAD!)
CMD ["python3", "app.py"]

