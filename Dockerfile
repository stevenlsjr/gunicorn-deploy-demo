FROM python:3.8-slim
WORKDIR /app/
RUN groupadd -g 1000 python && \
  useradd -m \
  -u 1000 -g 1000 python && \
  chown python:python /app/
ADD --chown=python:python ./Pipfile ./Pipfile.lock /app/
RUN apt update && \
    apt install -y \
      build-essential \
      libpq-dev  && \
    pip install pipenv
RUN pipenv install --system --deploy && \
    apt remove build-essential -y

ADD --chown=python:python ./ /app/
USER python
