#!/bin/sh

# Replace the UWSGI uri in the Nginx tcp proxy configuration.
if [ -n "$UWSGI_URI" ] && [ -n "$SERVER_NAME" ]; then
    sed -e "s/{{UWSGI_URI}}/$UWSGI_URI/;s/{{SERVER_NAME}}/$SERVER_NAME/" nginx.conf.template > /etc/nginx/nginx.conf
else
    echo "ERROR - Must specify: -e UWSGI_URI=<hostname:port> SERVER_NAME=<server_name>"
    exit 1
fi

tail -n0 -F /var/log/nginx/access.log -F /var/log/nginx/error.log &

exec "$@"