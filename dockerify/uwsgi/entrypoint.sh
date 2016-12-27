#!/bin/bash

set -e

python manage.py makemigrations
python manage.py migrate

# start uwsgi
exec uwsgi --emperor dockerify/uwsgi/ --gid www-data

# Forward app logs to docker log collector
tail -n0 -F /var/log/app_logs/*.log &

