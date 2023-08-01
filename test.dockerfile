# Use the Python image from Docker Hub
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY my_script.py .

# Install any required dependencies using pip
RUN pip install pandas  # Replace with your dependencies, if any

# Define the command to run the Python script
CMD ["python", "my_script.py"]
