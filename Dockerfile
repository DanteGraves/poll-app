# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the environment variable for Django
ENV DJANGO_SETTINGS_MODULE=hyperion.settings

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
