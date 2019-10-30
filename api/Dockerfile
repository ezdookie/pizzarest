FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /api
WORKDIR /usr/src/api

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
