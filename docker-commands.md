## Useful docker commands


- Declare image
        `FROM image_name:latest`
- Build image
        `docker build -f image_name:latest -t tag .`
- Run
        `docker run -it tag`


## Docker compose commands

- docker compose up
- docker compose down
- docker compose build

## Other docker compose commands

- docker compose run app_name /bin/bash
- docker compose up --build
- dcoker compose up --watch

## Curl commands

For terminal
```bash
curl http://localhost:12434/engines/v1/chat/completions \
 -H "Content-Type: application/json" \
 -d '{
        "model": "ai/gemma3",
        "messages": [
                {
                        "role": "system",
                        "content": "You are a helpful assistant."
                },
                {
                        "role": "user",
                        "content": "Please write 200 words about fall of Rome."
                }
        ]

}'
```

For container
```bash
curl http://model-runner.docker.internal/engines/v1/chat/completions \
 -H "Content-Type: application/json" \
 -d '{
        "model": "ai/gemma3",
        "messages": [
                {
                        "role": "system",
                        "content": "You are a helpful assistant."
                },
                {
                        "role": "user",
                        "content": "Please write 200 words about fall of Rome."
                }
        ]

}'
```