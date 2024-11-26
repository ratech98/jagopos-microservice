FROM python:3.12

RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev

WORKDIR /app

COPY . /app
COPY Tesseract-OCR /app/Tesseract-OCR
COPY images /app/images

RUN pip install --no-cache-dir -r /app/requirement.txt

# Expose the port that Cloud Run uses
EXPOSE 8080

# Set the entrypoint to start your application on the correct port
CMD ["python", "main.py"]
