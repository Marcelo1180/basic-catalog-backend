FROM python:3.9.7-slim-buster

ARG version

LABEL maintainer="Marcelo Arteaga <arteagamarcelo@gmail.com>"
LABEL version="${version}"

WORKDIR /home/nobody

RUN apt-get update && apt-get install -y \
        pipenv \
    && rm -rf /var/lib/apt/lists/* \
    && chown -R nobody:nogroup /home/nobody

COPY --chown=nobody:nogroup Pipfile Pipfile.lock ./

RUN pipenv install --ignore-pipfile --deploy --system

COPY --chown=nobody:nogroup . .

EXPOSE 8000

CMD ["waitress-serve","--listen=0.0.0.0:8000","base.wsgi:application"]
