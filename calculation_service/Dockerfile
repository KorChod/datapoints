FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /calculation_service/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /calculation_service/requirements.txt

WORKDIR /app/calculation_service
ADD . .
