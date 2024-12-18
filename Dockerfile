# take image from docker
FROM python:3.9-alpine3.13

# give name of maintainer
LABEL maintainer="_ab_codes"

# to run on one terminal
ENV PYTHONUNBUFFERED=1

ARG false

# copy requirements to docker tmp folder and copy .app to docker /app folder. define docker to work on WORKDIR is /app port will 8000
COPY requirements.txt /tmp/requirements.txt
COPY requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# first -m venv to create environment, pip upgrade to latest, install pip require, remove req file from tmp folder on docker
# create user named django-user, without password and home folder
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    [if ARG=true];\
        /py/bin/pip install -r /tmp/requirements.dev.txt && \
    rm -rf /tmp && \
    adduser \
            --disabled-password \
            --no-create-home \
            django-user

# give the path for run py files
ENV PATH="/py/bin:$PATH"

USER django-user
