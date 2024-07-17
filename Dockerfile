FROM python:3.12 AS base

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin/

# Copy only the comparatively stable files needed by the poetry install 
# so that we don't have to rerun it everytime a code file changes
COPY pyproject.toml poetry.toml /app/
WORKDIR /app
RUN poetry install
COPY todo_app /app/todo_app

FROM base AS production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base AS development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base as test 
ENTRYPOINT poetry run pytest