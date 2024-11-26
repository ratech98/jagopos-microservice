# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install Tesseract-OCR and other system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Copy additional directories
COPY Tesseract-OCR /app/Tesseract-OCR
COPY images /app/images

# Install Python dependencies
RUN pip install --no-cache-dir numpy==1.26.0
RUN pip install --no-cache-dir -r /app/requirement.txt

ENV TESSERACT_CMD="/usr/bin/tesseract"
# Expose the port for the Flask app
EXPOSE 8080

# Define the command to run the application
CMD ["python", "main.py"]
