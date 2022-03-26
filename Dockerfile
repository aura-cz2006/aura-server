FROM python:3.9.10
RUN mkdir /code
RUN mkdir /code/api

COPY /api /code/api
COPY poetry.lock /code
COPY pyproject.toml /code

WORKDIR /code
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
