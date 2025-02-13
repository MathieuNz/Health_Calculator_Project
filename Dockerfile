FROM python:3.11.2

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p static

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE $PORT

CMD ["python", "app.py"]