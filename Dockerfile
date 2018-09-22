FROM python:3.6.4
LABEL maintainer="raphaelm@sicara.com"

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app", "--reload", "-t", "120"]
