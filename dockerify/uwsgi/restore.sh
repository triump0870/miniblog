#!/bin/bash

set -e

if [ -n "$MYSQL_PASSWORD" ]; then
    until mysql -h "miniblog-mysql" -u "apps" -p"$MYSQL_PASSWORD" -e '\s; show databases'; do
      >&2 echo "Mysql is unavailable - sleeping"
      sleep 2
    done

    >&2 echo "Mysql is up - executing command"

    mysql -h "miniblog-mysql" -u "apps" -p"$MYSQL_PASSWORD" miniblog < miniblog.sql
    echo "Database was restored"
    sleep 2
else
    echo "Error: please provide MYSQL_PASSWORD"
    exit 1
fi