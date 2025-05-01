# Use the official Python 3.13 Alpine image as the base image
FROM python:3.13-alpine

# Set the maintainer's contact information
LABEL maintainer="volodymyr.vinohradov@gmail.com"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT="/usr/local/"

# Set the working directory inside the container
WORKDIR /app

# Copy dependency files into the container
COPY pyproject.toml uv.lock ./

# Install dependencies, sync with uv, and clean up unnecessary files
RUN pip install --no-cache-dir uv \
    && uv --no-cache-dir sync \
    && pip uninstall -y pip setuptools wheel uv \
    && rm -rf /root/.cache /root/.pip

# Copy the rest of the application code into the container
COPY . .

# Create necessary directories, set permissions, and make entrypoint executable
RUN adduser --disabled-password --no-create-home kram3ko && \
    mkdir -p /files/media /files/static && \
    chown -R kram3ko:kram3ko /files && \
    chmod -R 755 /files && \
    chmod +x entrypoint.sh

# Switch to the non-root user
USER kram3ko

# Define the entrypoint for the container
ENTRYPOINT ["sh", "entrypoint.sh"]
