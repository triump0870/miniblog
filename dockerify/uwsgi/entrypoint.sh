#!/bin/bash

set -e

if [ "$DEBUG" == "True" ]; then
	# check if the postgres service is up before starting django migration
    until export MYSQL_PASSWORD=$MYSQL_PASSWORD; mysql -h "miniblog-mysql" -u "apps" -p"$MYSQL_PASSWORD" -e '\s; show databases'; do
      >&2 echo "Mysql is unavailable - sleeping"
      sleep 5
    done

    >&2 echo "Mysql is up - executing command"
fi

yes | python ./src/manage.py migrate

# Forward app logs to docker log collector
tail -n0 -F /var/logs/app_logs/*.log &

# start uwsgi
exec uwsgi --emperor dockerify/uwsgi/ --gid www-data

