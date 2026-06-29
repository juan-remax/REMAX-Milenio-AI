FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install --no-cache-dir . aiosqlite

COPY src/ src/

RUN mkdir -p /app/data

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
