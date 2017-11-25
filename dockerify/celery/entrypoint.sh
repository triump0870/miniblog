#! /bin/bash

#pip install celery

exec celery -A miniblog worker --concurrency=20 --loglevel=info
