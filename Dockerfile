FROM python:3.12-slim
WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --only main --no-root

COPY . /app
CMD ["python", "main.py"]
