FROM python:3.11.5-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . /app/
COPY ./requirements.txt /app/

RUN chmod +x ./scripts/start.sh

RUN pip install -r requirements.txt

ENTRYPOINT [ "sh", "-c", "./scripts/start.sh" ]
