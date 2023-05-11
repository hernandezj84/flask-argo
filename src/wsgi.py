"""Wsgi application for gunicorn"""
import logging
from src.app import app

if __name__ == "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(logging.DEBUG)
    app.run(host='0.0.0.0', debug=True)
