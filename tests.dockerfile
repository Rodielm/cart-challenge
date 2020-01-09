FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./test_requirements.txt /test_requirements.txt

WORKDIR /

RUN pip3 install -r test_requirements.txt

EXPOSE 8888

COPY ./app /app

COPY ./tests-start.sh /tests-start.sh

COPY ./test.env /.env

RUN chmod +x /tests-start.sh

# This will wait until the container start
CMD [ "bash","-c","while true; do sleep 1; done" ]

# After the container started
# docker exec -it imagename /tests-start.sh
