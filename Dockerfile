FROM python:3.9.1-alpine

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /app/

COPY requirements.txt tmp/requirements.txt
RUN set -eux \
    && apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    build-base \
    python3-dev \
    postgresql-client \
    &&  apk add --no-cache postgresql-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r tmp/requirements.txt \
    && rm -rf /root/.cache/pip \
    && rm -rf tmp

EXPOSE 8000

WORKDIR /app

CMD gunicorn application.wsgi --bind "0.0.0.0:8000" --reload

