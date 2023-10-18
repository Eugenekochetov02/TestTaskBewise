#!/bin/bash

poetry config virtualenvs.create false

poetry install

cd app

alembic upgrade head

cd src

gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000