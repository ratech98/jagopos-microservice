# Use an official Python runtime as a parent image
FROM python:3.12

RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app
COPY Tesseract-OCR /app/Tesseract-OCR
COPY images /app/images

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirement.txt

# Define the command to run the application
CMD ["python", "main.py"]