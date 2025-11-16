#!/bin/sh
set -e

echo "[entrypoint] Initializing..."

# Asegura directorio para sshd
mkdir -p /run/sshd

echo "[entrypoint] Starting SSH service..."
/usr/sbin/sshd

echo "[entrypoint] Starting Python application..."
python /app/app.py &

echo "[entrypoint] All services started. Keeping container alive..."
tail -f /dev/null
