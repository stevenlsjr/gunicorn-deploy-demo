FROM python:3.8-slim
WORKDIR /app/
RUN groupadd -g 1000 python && \
  useradd -m \
  -u 1000 -g 1000 python && \
  chown python:python /app/
ADD --chown=python:python ./Pipfile ./Pipfile.lock /app/
RUN pip install pipenv && \
    pipenv install --system --deploy

ADD --chown=python:python ./ /app/
USER python
