# --- Base Image ---
FROM python:3.13-slim

# --- Install system dependencies needed by psycopg2 ---
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# --- Set working directory ---
WORKDIR /app

# --- Copy requirements and install ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy application code ---
COPY . .

# --- Environment variables ---
ENV FLASK_APP=main.py
ENV PORT=3011

# --- Expose port ---
EXPOSE 3011

# --- Run using Gunicorn (production) ---
CMD ["gunicorn", "--bind", "0.0.0.0:3011", "main:app"]
