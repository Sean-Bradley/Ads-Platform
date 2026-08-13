FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ARG APP_VERSION=development

ENV APP_VERSION=$APP_VERSION

CMD ["python", "run.py"]