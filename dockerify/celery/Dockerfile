FROM miniblog:latest

COPY --chown=app . ${APP_ROOT}

RUN ls -la /app/dockerify/celery/
RUN chmod +x /app/dockerify/celery/entrypoint.sh

RUN ls -la /app/dockerify/celery/
ENTRYPOINT ["/app/dockerify/celery/entrypoint.sh"]