FROM python:alpine

COPY flaskapp.py  /opt/flaskapp.py
COPY wsgi.py /opt/wsgi.py
COPY params.ini /opt/params.ini
COPY socket /opt/socket
WORKDIR /opt/
COPY requirements.txt /tmp/requirements.txt
RUN \
    addgroup -g 101 flaskapp && \
    adduser -G flaskapp -u 101 -h /opt -s /bin/sh -D flaskapp && \ 
    chown -R 101:101 /opt && \
    apk add --no-cache --virtual zlib-dev gcc libc-dev libffi-dev && \
    pip install -Ur /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

CMD ["uwsgi", "--callable", "flaskapp", "--ini", "/opt/params.ini", "--enable-threads"]
