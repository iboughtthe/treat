# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the main.py script to the working directory
COPY main.py .

# Set the entry point for the container
ENTRYPOINT ["python", "main.py"]
docker build -t my-telegram-bot 
docker run -d -v $(PWD)/app.json:/app/app.json --name my-telegram-bot-container my-telegram-bot
