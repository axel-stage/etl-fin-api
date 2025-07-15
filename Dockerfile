####################
# Python Container #
####################
ARG PYTHON_VERSION=3.12.11 \
    APP_PATH=/home/app \
    AUTHOR=dataengineer24 \
    DESCRIPTION="ETL pipeline for finance API" \
    USERNAME=monty \
    USER_UID=1000 \
    USER_GID=$USER_UID

# base container image
######################
FROM python:${PYTHON_VERSION}-slim-bookworm AS base

ARG AUTHOR \
    DESCRIPTION

LABEL org.opencontainers.image.authors=${AUTHOR} \
      org.opencontainers.image.description=${DESCRIPTION}

# build container image
#######################
FROM base AS build

ARG APP_PATH

WORKDIR ${APP_PATH}

COPY requirements.txt .

RUN python -m venv .venv
# Enable venv
ENV PATH=${APP_PATH}/.venv/bin:${PATH}

RUN python -m ensurepip --upgrade && \
    pip install -r requirements.txt --no-cache-dir --require-virtualenv

# app container image
#####################
FROM base

ARG APP_PATH \
    USERNAME \
    USER_UID \
    USER_GID

WORKDIR ${APP_PATH}

ENV PYTHONIOENCODING=utf-8 \
    LANG=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=${APP_PATH}/.venv/bin:${PATH}

RUN groupadd --gid ${USER_GID} ${USERNAME} && \
    useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} && \
    chown -R ${USER_UID}:${USER_GID} ${APP_PATH}

COPY --chown=${USER_UID}:${USER_GID} --from=build ${APP_PATH}/.venv .venv

COPY --chown=${USER_UID}:${USER_GID} src src

USER ${USERNAME}
ENTRYPOINT ["python", "./src/main.py"]
CMD ["--symbol", "MSFT"]
