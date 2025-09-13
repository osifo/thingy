#!/bin/bash

PYTHONPATH=./src uvicorn server:app --reload --port=4000
