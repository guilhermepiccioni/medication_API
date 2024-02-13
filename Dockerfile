# Use the official Python image as base image
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y netcat-traditional curl

# Copy only the requirements.txt file to the container
COPY requirements.txt /app/

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install psycopg2-binary

# Install Alembic
RUN pip install alembic

# Copy the source code into the container
COPY . /app

# Expose the port that FastAPI runs on
EXPOSE 8000

# Initialize alembic
RUN rm -rf alembic && alembic init alembic

# Upgrade the database
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000
