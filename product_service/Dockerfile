# Use the official slim version of Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Update the package list and install essential build tools and gcc
RUN apt-get update && apt-get install -y build-essential gcc

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
# using pip with no cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Remove build dependencies to keep the image slim
RUN apt-get remove -y build-essential gcc && apt-get autoremove -y && apt-get clean

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 to be accessible from outside the container
EXPOSE 5000

# Define the command to run the application when the container starts
CMD ["python", "product_service.py"]
