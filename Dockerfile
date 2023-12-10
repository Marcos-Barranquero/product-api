# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install Poetry
RUN pip install poetry

# Configure Poetry
RUN poetry config virtualenvs.in-project true

# Install project dependencies
RUN poetry install --no-interaction --no-ansi

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run main.py when the container launches
CMD ["poetry", "run", "main"]