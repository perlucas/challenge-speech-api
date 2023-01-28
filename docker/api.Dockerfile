FROM python:3

WORKDIR /usr/src/app

COPY ./src .

COPY ./credentials.json /usr

RUN pip install --no-cache-dir -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/credentials.json"

