#!/bin/bash

if [ -n "$DATABASE_USER" ] && [ -n "$DATABASE_PASSWORD" ] && [ -n "$DATABASE" ]; then
	sed -e "s/{{DATABASE_USER}}/$DATABASE_USER/g" -e "s/{{DATABASE_PASSWORD}}/$DATABASE_PASSWORD/" -e "s/{{DATABASE}}/$DATABASE/g" createdb.conf.template > /docker-entrypoint-initdb.d/entrypoint.sh
else
	echo "ERROR - Must specify: -e DATABASE_USER, DATABASE_PASSWORD and DATABASE"
	exit 1
fi

echo default-time-zone = 'Asia/Kolkata' >> /etc/mysql/my.cnf

exec "$@"