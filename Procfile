web: gunicorn config.wsgi:application
worker: celery worker --app=miniblog.taskapp --loglevel=info
