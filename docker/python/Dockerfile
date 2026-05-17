FROM python:3.13

# expose to nginx
EXPOSE 9000

RUN pip install poetry

WORKDIR /code
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && poetry install --no-root

# --reload: in dev mode, ask gunicorn to restart worker on any source file change
CMD ["gunicorn", "--workers=1", "--threads=2", "--bind=0.0.0.0:9000", "--reload", "app:app"]
