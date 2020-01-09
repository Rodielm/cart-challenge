# Cart Challenge

This a challenge project developed with FastApi and PonyOrm

## Build the images 

```bash
docker build -t <name-image> .
```

## Run the container 

```bash
docker run -d --name <name-container> -v$PWD/app:/app  -p 80:80 <name-image>
```

if you want to change or test and automatically reload the project

```bash
docker run -d --name <name-container> -v$PWD/app:/app  -p 80:80 <name-image> /start-reload.sh
```
## Interactive API docs

Now go to http://<host:port>/docs. 

## Alternative API docs

Now go to http://<host:port>/redoc.