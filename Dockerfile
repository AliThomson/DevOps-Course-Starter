FROM python:3.12

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin/

# Install ToDo App
COPY . /app
WORKDIR /app

RUN poetry install

# ENV APP_PORT=5000
# EXPOSE ${APP_PORT}

# Launch
ENTRYPOINT poetry run flask run --host=0.0.0.0