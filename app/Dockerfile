FROM python:3.11

RUN mkdir /bewise_app

WORKDIR /bewise_app

COPY pyproject.toml .

RUN pip install poetry

COPY . .

RUN chmod a+x app.sh
