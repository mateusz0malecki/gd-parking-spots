ARG         PLATFORM=linux/amd64
ARG         PYTHON_VER=3.12

# ==========
# BUILD STAGE
# ==========
FROM        --platform=${PLATFORM} python:${PYTHON_VER} AS builder

# Download the latest uv installer, install it and then remove it
ADD         https://astral.sh/uv/install.sh /install.sh
RUN         chmod -R 755 /install.sh && /install.sh && rm /install.sh

# Set up the UV environment path correctly
ENV         PATH="/root/.local/bin:${PATH}"

WORKDIR     /code

COPY        ./pyproject.toml .

ARG         DEV=false
RUN         if [ $DEV = "true" ]; \
                then uv sync ; \
            else uv sync --no-dev ; \
            fi

# ==========
# RUN STAGE
# ==========
FROM        --platform=${PLATFORM} python:${PYTHON_VER}-slim AS run

WORKDIR     /code/src

COPY        ./src/ /code/src
COPY        ./src/.env /code/src/.env

COPY        --from=builder /code/.venv /code/.venv

ENV         PATH="/code/.venv/bin:$PATH"
ENV         PYTHONUNBUFFERED=1

CMD         ["bash", "-c", "uvicorn src.asgi:app --reload --host 0.0.0.0 --port 8000"]