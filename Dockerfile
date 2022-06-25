FROM python:3.8
LABEL MAINTAINER="Taha Mousavi|TahaM8000@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /Toos-master
WORKDIR /Toos-master

COPY . /Toos-master


ADD requirements.txt /Toos-master
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "toos.wsgi"]
