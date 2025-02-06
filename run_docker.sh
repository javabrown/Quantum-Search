#!/bin/bash

# Define container and image name
CONTAINER_NAME="quantum_env"
IMAGE_NAME="quantum_env"

echo "🛑 Checking for existing container..."

# Check if container exists before stopping and removing
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "🛑 Stopping and removing existing container: $CONTAINER_NAME"
    docker stop $CONTAINER_NAME >/dev/null 2>&1
    docker rm $CONTAINER_NAME >/dev/null 2>&1
else
    echo "✅ No existing container found. Skipping removal."
fi

echo "🗑️ Checking for existing Docker image..."

# Check if the image exists before removing
if docker images -q $IMAGE_NAME >/dev/null 2>&1; then
    echo "🗑️ Removing old Docker image: $IMAGE_NAME"
    docker rmi $IMAGE_NAME >/dev/null 2>&1
else
    echo "✅ No existing image found. Skipping removal."
fi

echo "🐳 Building a fresh Docker image..."
# Build the new Docker image
docker build -t $IMAGE_NAME .

echo "🚀 Running the new Docker container..."
# Run the container with mounted volumes
docker run -it --rm \
    -p 8888:8888 \
    -v "$(pwd)/src:/workspace/src" \
    -v "$(pwd)/output:/workspace/output" \
    --name $CONTAINER_NAME \
    $IMAGE_NAME
