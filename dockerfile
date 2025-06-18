# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app


# Define a mount point with the VOLUME instruction to restrict and persist data access at /app/data.
# Only files mounted from the host to this directory will be accessible to the container,
# limiting the container's file access to the specified host directory.
VOLUME /app/data

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app

COPY test-data/my-file.txt /app/test-data/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the source directory contents into the container at /app
COPY src/mcpfsserver /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=server.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
