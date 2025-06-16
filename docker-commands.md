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

- docker compose run app /bin/bash
- docker compose up --build