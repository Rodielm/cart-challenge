FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY ./app /app

COPY ./backend.env /.env



