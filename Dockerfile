FROM python:3.6.4
LABEL maintainer="raphaelm@sicara.com"

WORKDIR /app

RUN pip install --upgrade pip

ADD . /app

ENTRYPOINT ["python", "app.py"]
