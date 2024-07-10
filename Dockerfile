FROM python:3.12-alpine
RUN apk update && apk --no-cache upgrade
RUN python -m pip install --upgrade pip && python -m pip cache purge

WORKDIR /usr/local/app

ENV APP_VERSION=v1

COPY requirements.txt /usr/local/app/
RUN apk --no-cache add build-base libffi-dev libstdc++ && \
    python -m pip install -r /usr/local/app/requirements.txt && \
    python -m pip cache purge && \
    apk del build-base

COPY src .

EXPOSE 8000 8080

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
