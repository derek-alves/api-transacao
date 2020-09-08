FROM python:3.8.3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps

COPY requirements.txt /backend
RUN pip install -r requirements.txt
COPY . /backend/