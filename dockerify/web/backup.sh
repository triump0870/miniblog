#!/bin/bash

set -e

if [ -n "$DATABASE_HOST" ] && [ -n "$DATABASE_PASSWORD" ] && [ -n "$DATABASE_USER" ]; then
    export BACKUP_FILE="miniblog-"$(date +"%F-%H-%M")
    mysqldump -h "$DATABASE_HOST" -u"$DATABASE_USER" -p$DATABASE_PASSWORD miniblog > "$BACKUP_FILE".sql
    echo "Mysql dump was saved inside $BACKUP_FILE.sql"
    echo "Database dumping was successful"
else
    echo "Error: Provide DATABASE_HOST, DATABASE_USER and DATABASE_PASSWORD"
fi

python /app/dockerify/web/backup.py