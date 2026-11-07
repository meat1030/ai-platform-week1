FROM python:3.11-slim

WORKDIR /app

COPY app.py .
COPY .env .

RUN pip install --no-cache-dir google-genai python-dotenv

CMD ["python", "app.py"]
