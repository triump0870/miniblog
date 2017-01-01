"""
This file's contents were moved to `generic/utils.py`.
NOTE: This file will be removed in future release.

"""

import socket
import logging

PROJECT = "MINIBLOG"

old_factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    """
    Add custom attributes to the python LogRecord class.

    - ip
    - host
    - project

    These can be accessed from formatters.

    Example:
    ========
    format: "[%(asctime)s] [%(ip)s %(host)s] [%(project)s] %(levelname)s %(message)s",

    """
    record = old_factory(*args, **kwargs)
    host = socket.gethostname()

    record.host = host
    record.ip = socket.gethostbyname(host)
    record.project = PROJECT

    return record
