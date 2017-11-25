#!/bin/bash


# Change the owner of the $APP_ROOT directory
sudo chown -R $APP_USER:$APP_USER $APP_ROOT

if [ "$DEBUG" == "True" ]; then
	# check if the postgres service is up before starting django migration
    until export MYSQL_PASSWORD=$DATABASE_PASSWORD; export DATABASE_HOST=$DATABASE_HOST; mysql -h "$DATABASE_HOST" -u"$DATABASE_USER" -p"$DATABASE_PASSWORD" -e '\s; show databases'; do
      >&2 echo "Database server is unavailable - sleeping"
      sleep 5
    done

    >&2 echo "Database server is up - executing command"
fi

exec "$@"