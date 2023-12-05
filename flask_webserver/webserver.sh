#!/bin/bash

export FLASK_APP=./webserver.py
# export IP="127.0.0.1"  # default ip
export IP="0.0.0.0"
# export IP="192.168.10.10"
# export PORT="5000"     # default port
export PORT="8080"

flask run -h "$IP" -p "$PORT"
if [ -n "$IP" ] && [ -n "$PORT" ]; then      # -n: not null
  flask run --debugger -h "$IP" -p "$PORT"
else
  flask run
fi
