# Use an official Python image as the base image
FROM python:3

# Install mailutils for the mail command and other necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends mailutils

# Set the Python script to copy into the image
COPY script.py /app/script.py
COPY send_email.py /app/send_email.py

# Set the working directory
WORKDIR /app

# Run the Python script when the container starts
CMD ["python", "script.py"]
