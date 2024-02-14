FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y netcat-traditional curl

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install psycopg2-binary

COPY . /app

EXPOSE 8000

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
