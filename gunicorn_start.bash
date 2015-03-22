#!/bin/bash

NAME='miniblog'
DJANGODIR='/webapps/django/miniblog'
SOCKFILE='/webapps/django/run/gunicorn.sock'
USER='django'
GROUP='webapps'
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=miniblog.settings
DJANGO_WSGI_MODULE=miniblog.wsgi

echo "Starting $NAME as `whoami`"

#Activate the vertual environment
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

#Create the run directory if it doesn't exists
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

#Start the Django Unicorn
#Program meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
	--name $NAME \
	--workers $NUM_WORKERS \
	--user=$USER --group=$GROUP \
	--bind=unix:$SOCKFILE \
	--log-level=debug \
	--log-file=-