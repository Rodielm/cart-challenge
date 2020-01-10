# Cart Challenge

This a challenge project developed with FastApi and PonyOrm

## Build the images 

```bash
docker build -t <name-image> . -f <dockerfile> .

```

## Run the container

```bash
docker run -d --name <name-container> -v$PWD/app:/app  -p 80:80 <name-image>
```

if you want to change or test and automatically reload the project

```bash
docker run -d --name <name-container> -v$PWD/app:/app  -p 80:80 <name-image> /start-reload.sh
```

## Run the test 

```bash
docker run -d --name <name-container> -v$PWD/app:/app  -p 80:8888 <name-image>
```

if you want to change or test and automatically reload the project

```bash
docker run -d --name <name-container> -v$PWD/app:/app  -p 80:8888 <name-image> /start-reload.sh
```

## Execute the Tests

```bash
docker exec -it <name-container-test> /tests-start.sh
```

## Interactive API docs

Now go to http://<host:port>/docs. 

## Alternative API docs

Now go to http://<host:port>/redoc.