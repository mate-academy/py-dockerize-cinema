# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a user to run the application
RUN adduser --disabled-password --no-create-home django-user

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Change ownership of the app directory
RUN chown -R django-user:django-user /app

# Switch to the non-root user
USER django-user

# Command to run the application
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]