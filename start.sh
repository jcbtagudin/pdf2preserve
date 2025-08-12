#!/bin/bash
set -e

echo "🚀 Starting PDF2Preserve on Railway..."

# Create uploads directory
mkdir -p /tmp/uploads
chmod 755 /tmp/uploads

# Set environment
export PYTHONUNBUFFERED=1
export PYTHONPATH=/app

# Start the application
exec gunicorn app:app \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 1 \
    --threads 2 \
    --timeout 300 \
    --max-requests 1000 \
    --max-requests-jitter 100 \
    --preload \
    --access-logfile - \
    --error-logfile -