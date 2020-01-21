# from __future__ import absolute_import
#
# import logging
#
# from celery.signals import after_task_publish
#
# # This will make sure the app is always imported when
# # Django starts so that shared_task will use this app.
# from .celery_app import app as celery_app
#
# logger = logging.getLogger(__name__)
#
#
# @after_task_publish.connect
# def update_sent_state(sender=None, body=None, **kwargs):
#     # the task may not exist if sent using `send_task` which
#     # sends tasks by name, so fall back to the default result backend
#     # if that is the case.
#     task = celery_app.tasks.get(sender)
#     logging.info("Task", task)
#
#     backend = task.backend if task else celery_app.backend
#
#     backend.store_result(body['id'], None, "SENT")
