# Horror API
This project let you search movie data using omdb api

## Development

### Run with Docker

#### Requirements

- Install [Docker and Docker compose](https://docs.docker.com/compose/install/)
- Notice docker-related files are placed under `local` folder.

#### Change dir to `local`

```bash
cd local
```

#### Build the image

```bash
make build
```

#### Start the service

```bash
make up
```

#### Stop the service

```bash
make down
```

### Run tests

with the service running:

```bash
make test
```
