FROM python:3.9.7-slim-buster

ARG version

LABEL maintainer="Marcelo Arteaga <arteagamarcelo@gmail.com>"
LABEL version="${version}"

WORKDIR /home/nobody

RUN apt-get update && apt-get install -y \
        pipenv \
    && rm -rf /var/lib/apt/lists/* \
    && chown -R nobody:nogroup /home/nobody

# COPY --chown=nobody:nogroup Pipfile Pipfile.lock ./.
COPY --chown=nobody:nogroup . .

RUN pipenv install --ignore-pipfile --deploy --system

# COPY --chown=nobody:nogroup . .

# ENV PORT=8000
EXPOSE $PORT
# CMD ["waitress-serve","--listen=0.0.0.0:$PORT","base.wsgi:application"]
# CMD ["waitress-serve","--port=$PORT","base.wsgi:application"]
CMD ["python","manage.py","runserver","0.0.0.0:${PORT}"]
