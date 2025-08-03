FROM python:3.9

ENV PYTHONDOWNWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /RTG

COPY requirements.txt /RTG/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /RTG/