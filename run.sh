#!/bin/sh

# Runs the damn dev server at 127.0.0.1:8000, if no parameter is passed.
# $ ./run.sh
if [ $# -eq 0 ]; then
  python manage.py runserver
fi
