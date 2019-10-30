FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /api
WORKDIR /usr/src/api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x wait-for-it.sh

CMD ./wait-for-it.sh -t 30 db:5432 --strict -- python manage.py runserver 0.0.0.0:8000
