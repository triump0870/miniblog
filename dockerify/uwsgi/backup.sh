#!/bin/bash

set -e

if [ -n "$MYSQL_PASSWORD" ]; then
    export BACKUP_FILE="miniblog-"$(date +"%F-%H-%M")
    mysqldump -h "miniblog-mysql" -u "apps" -p$MYSQL_PASSWORD miniblog > "$BACKUP_FILE".sql
    echo "Mysql dump was saved inside $BACKUP_FILE.sql"
    echo "Database dumping was successful"
else
    echo "Error: Provide the MYSQL_PASSWORD"
fi

python /app/dockerify/uwsgi/backup.py