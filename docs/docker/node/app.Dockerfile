FROM node:23.6.0-alpine3.21

RUN apk update \
    && apk upgrade

WORKDIR /usr/src/app

COPY ./app/package*.json .

RUN npm install

COPY --chown=node:node ./app .

CMD ["npm", "run", "dev"]
