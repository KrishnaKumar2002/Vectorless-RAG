FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .env.example ./
RUN pip install --no-cache-dir -e .[dev]

COPY src/ ./src/

EXPOSE 8000

CMD ["make", "dev"]

