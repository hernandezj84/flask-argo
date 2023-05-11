FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY test test
COPY src src
# Copying entry point
COPY docker/docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
