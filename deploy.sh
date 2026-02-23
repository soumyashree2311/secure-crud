#!/bin/bash

echo "Checking Docker..."
docker --version || { echo "Docker not installed"; exit 1; }

echo "Checking Docker Compose..."
docker compose version || { echo "Docker Compose not installed"; exit 1; }

echo "Cleaning old containers..."
docker compose down -v

echo "Building and starting..."
docker compose up --build -d

echo "Waiting for containers..."
sleep 10

echo "[SUCCESS] Application is live at http://localhost"