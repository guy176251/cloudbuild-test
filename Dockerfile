FROM tiangolo/uwsgi-nginx:python3.9-2021-10-02

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./main.py ./
