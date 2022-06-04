FROM python:3.8
LABEL MAINTAINER="Taha Mousavi|TahaM8000@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /Toss-master
WORKDIR /Toss-master

COPY . /Toss-master


ADD requirements.txt /Toss-master
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "toos.wsgi"]
