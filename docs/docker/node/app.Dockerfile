FROM node:23.5.0-alpine3.21

RUN apk update \
    && apk upgrade

WORKDIR /var/www/app

COPY ./app/package*.json .

USER node

RUN npm install

COPY --chown=node:node ./app .

CMD ["sh"]
