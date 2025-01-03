# Docs

TODO.

## Build

```text
docker build --file ./docker/node/node.Dockerfile --tag node:dev .
```

```text
docker run --name node --rm --volume ${PWD}/app:/var/www/app -it node:dev
```

```text
npm create rspress@latest
```
