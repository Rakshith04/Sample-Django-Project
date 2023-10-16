# Use an official Python runtime as a base image
FROM python:3.11.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

RUN chmod -R 755 /app/BusinessApp/templates/
# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh

# Grant execution permissions to the entrypoint script
RUN chmod +x /app/entrypoint.sh

# Expose the port that Django runs on
EXPOSE 8000

# Set the entry point to the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
