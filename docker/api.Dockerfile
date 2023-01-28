FROM python:3

WORKDIR /usr/src/app

COPY ./src .

COPY ./credentials.json .

RUN pip install --no-cache-dir -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/credentials.json"

