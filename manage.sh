#!/usr/bin/env bash

uv run \
    --python cpython3.13\
    python src/manage.py ${@}