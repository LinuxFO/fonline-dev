FROM node:23.6.0-alpine3.21

RUN apk update \
    && apk upgrade

WORKDIR /usr/src/app

CMD ["sh"]
