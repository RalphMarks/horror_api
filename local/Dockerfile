FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev python3-dev git procps

# Install dependencies
COPY ./requirements /requirements
RUN pip install --upgrade pip
RUN pip install -r /requirements/base.txt

RUN mkdir /code
WORKDIR /code

RUN useradd --create-home --shell /bin/bash user
USER user

ENTRYPOINT ["sh", "/code/local/entrypoint.sh"]
