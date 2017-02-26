#!/bin/bash

set -e

if [ -n "$DATABASE_PASSWORD" ] && [ -n "$DATABASE_USER" ]; then
    until mysql -h "miniblog-mysql" -u"$DATABASE_USER" -p"$DATABASE_PASSWORD" -e '\s; show databases'; do
      >&2 echo "Mysql is unavailable - sleeping"
      sleep 2
    done

    >&2 echo "Mysql is up - executing command"

    mysql -h "miniblog-mysql" -u"$DATABASE_USER" -p"$DATABASE_PASSWORD" miniblog < miniblog.sql
    echo "Database was restored"
    sleep 2
else
    echo "Error: please provide DATABASE_USER and DATABASE_PASSWORD"
    exit 1
fi