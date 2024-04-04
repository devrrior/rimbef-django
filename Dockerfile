FROM python:3.8.19-slim-bullseye
LABEL maintainer="Cimab <ing.tatiana.mejia@gmail.com>"

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TARGET_ENV=base

RUN mkdir /var/secrets

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements/ ./requirements/

RUN pip install -r ./requirements/${TARGET_ENV}.txt

COPY . .