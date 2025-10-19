#!/bin/bash

PYTHONPATH=./src uv run uvicorn main:app --reload --port=4000
