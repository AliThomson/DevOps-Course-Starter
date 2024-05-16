FROM python:3.12 AS base

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin/

# Install ToDo App
COPY . /app
WORKDIR /app
RUN poetry install

# ENV APP_PORT=5000
# EXPOSE ${APP_PORT}

FROM base AS production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base AS development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host=0.0.0.0