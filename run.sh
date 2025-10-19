#!/bin/bash

PYTHONPATH=./src  PYTHONUNBUFFERED=1 uv run uvicorn main:app --reload --port=4000
