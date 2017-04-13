#!/bin/bash

manage='python manage.py'

# Runs the damn dev server
if [ $# -eq 0 ]; then
  $manage runserver

# Update migrations
elif [ "$1" = 'update' ]; then
  $manage makemigrations school

# Migrations
# also fucking updates migrations because that's usually what you want
elif [ "$1" = 'migrate' ]; then
  ./$(basename $0) update
  $manage migrate
fi
