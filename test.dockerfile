# Use an official Python image as the base image
FROM python:3

# Install mailutils for the mail command and other necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends mailutils

# Install Python libraries required for OAuth2 authentication with Gmail
RUN pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Set the Python script and service account file to copy into the image
COPY script.py /app/script.py
COPY send_email.py /app/send_email.py

# Set the working directory
WORKDIR /app

# Copy the service account file from GitHub secrets
COPY service_account.json /app/service_account.json

# Run the Python script when the container starts
CMD ["python", "script.py"]
