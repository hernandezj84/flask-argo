#!/bin/bash
gunicorn --chdir src wsgi:app --bind 0.0.0.0:5000 --workers 4 --log-level DEBUG