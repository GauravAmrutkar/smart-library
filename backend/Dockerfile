FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY . .

RUN uv sync

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]