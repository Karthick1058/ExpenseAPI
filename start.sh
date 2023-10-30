#!/bin/sh
source env/bin/activate
export FLASK_APP=./src/main/app.py
flask --debug run -h 0.0.0.0