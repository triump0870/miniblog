#!/bin/bash

if [ -n "$MYSQL_PASSWORD" ]; then
	sed -e "s/{{MYSQL_PASSWORD}}/$MYSQL_PASSWORD/" createdb.conf.template > /docker-entrypoint-initdb.d/entrypoint.sh
else
	echo "ERROR - Must specify: -e MYSQL_PASSWORD"
	exit 1
fi

echo default-time-zone = 'Asia/Kolkata' >> /etc/mysql/my.cnf

exec "$@"