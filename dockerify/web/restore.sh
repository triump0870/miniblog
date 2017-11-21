#!/bin/bash

set -e

if [ -n "$DATABASE_HOST" ] && [ -n "$DATABASE_PASSWORD" ] && [ -n "$DATABASE_USER" ]; then
    until mysql -h "$DATABASE_HOST" -u"$DATABASE_USER" -p"$DATABASE_PASSWORD" -e '\s; show databases'; do
      >&2 echo "Database server is unavailable - sleeping"
      sleep 2
    done

    >&2 echo "Database server is up - executing command"

    mysql -h "$DATABASE_HOST" -u"$DATABASE_USER" -p"$DATABASE_PASSWORD" miniblog < miniblog.sql
    echo "Database was restored"
    sleep 2
else
    echo "Error: please provide DATABASE_HOST, DATABASE_USER and DATABASE_PASSWORD"
    exit 1
fi