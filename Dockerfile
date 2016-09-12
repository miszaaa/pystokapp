FROM python:2.7

RUN apt-get update && apt-get install -y vim \
    wget \
    tar \
    libpq-dev \
    python-dev \
    build-essential

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . /code
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000
