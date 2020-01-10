FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./test_requirements.txt /test_requirements.txt

WORKDIR /

RUN pip3 install -r test_requirements.txt

COPY ./app /app

COPY ./test.env /.env

COPY ./tests-start.sh /tests-start.sh

RUN chmod +x /tests-start.sh

# This will wait until the container start
CMD [ "bash","-c","while true; do sleep 1; done" ]

# After the container started
# docker exec -it container-name /tests-start.sh
