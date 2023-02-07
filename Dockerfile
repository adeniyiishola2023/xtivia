# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the working directory in container image
COPY ./finalscript.py .

# Update packages

RUN apt-get update -y 

# Install boto3 library
RUN pip install boto3

# Install aws cli for 
RUN pip install awscli

# Set the command to run the Python script
CMD ["python3", "finalscript.py"]


