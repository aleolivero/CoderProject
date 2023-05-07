FROM public.ecr.aws/zeet/lambdahandler:v0.2.0 as base

RUN yum install -y amazon-linux-extras && amazon-linux-extras install -y python3.8
RUN ln -s /usr/bin/python3.8 /usr/bin/python3 || true
RUN ln -s /usr/bin/pip3.8 /usr/bin/pip3 || true

# Instalar el repositorio EPEL y actualizar SQLite
RUN yum install -y epel-release && \
    yum update -y sqlite

WORKDIR /app

COPY . .

RUN sed -i 's/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \["*"\]/g' ./*/settings.py

ARG PYTHONUNBUFFERED
ARG UVICORN_HOST
ARG ZEET_APP
ARG ZEET_PROJECT
ARG GIT_COMMIT_SHA
ARG ZEET_ENVIRONMENT
ARG GUNICORN_CMD_ARGS

RUN pip3 install -r requirements.txt
