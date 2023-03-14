# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Set the environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=0000
ENV POSTGRES_DB=comments
ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432

# Expose the port on which the application will run
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
