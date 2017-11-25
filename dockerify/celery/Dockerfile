FROM miniblog:latest

COPY --chown=app ./dockerify/celery/entrypoint.sh ${APP_ROOT}/entrypoint.sh
RUN chmod +x ${APP_ROOT}/entrypoint.sh

COPY --chown=app ./miniblog ${APP_ROOT}

ENTRYPOINT ["./entrypoint.sh"]