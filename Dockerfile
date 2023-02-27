FROM python:3.10-alpine
WORKDIR /usr/src/app
COPY . .
RUN apk update
RUN apk add musl-dev mariadb-dev gcc
RUN pip install -r ./requirements.txt
RUN rm -rf /var/cache/apk/* /tmp/* /var/tmp/*
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
# docker build -t pedrotti/python:django .