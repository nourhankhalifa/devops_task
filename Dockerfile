# Use the official Python image as the base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . .
RUN pip install -r requirements.txt

# Expose the port on which your Flask app will run
EXPOSE 5000

# Set the environment variable for MongoDB URI
ENV MONGO_URI="mongodb://mongodb:27017"

CMD ["python", "app.py"]