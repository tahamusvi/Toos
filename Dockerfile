FROM python:3.8
LABEL MAINTAINER="Taha Mousavi|TahaM8000@gmail.com"

ENV PYTHONUNBUFFERED 1
WORKDIR /django

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
