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

yes | python manage.py migrate
yes | python manage.py collectstatic --noinput
#python manage.py loaddata fixture miniblog.json

# start uwsgi
exec uwsgi --emperor dockerify/uwsgi/ --gid www-data

# Forward app logs to docker log collector
tail -n0 -F /var/log/app_logs/*.log &

