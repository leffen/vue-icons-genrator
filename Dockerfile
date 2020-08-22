FROM python:3.8-slim-buster AS base

RUN pip install --upgrade pip
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --user -r /app/requirements.txt
COPY *.py ./

ENTRYPOINT ["python", "vueicongen.py"]
