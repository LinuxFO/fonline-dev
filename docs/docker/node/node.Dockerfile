FROM node:23.5.0-alpine3.21

RUN apk update \
    && apk upgrade

WORKDIR /var/www/app

CMD ["sh"]
