FROM python:3.10-alpine
LABEL org.opencontainers.image.source https://github.com/zbgn/docker-autocompose

WORKDIR /usr/src/app

COPY . .

RUN python ./setup.py install

ENTRYPOINT [ "python", "./autocompose.py" ]
