FROM python:3.11

RUN pip install poetry

RUN pip install email-validator

RUN poetry config virtualenvs.create false

WORKDIR /workspace

COPY . .

RUN poetry install

CMD ["uvicorn", "src.main:api", "--reload", "--host", "0.0.0.0"]