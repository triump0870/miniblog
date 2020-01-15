FROM miniblog:latest

# The port number on which the application will run
EXPOSE 30000

COPY --chown=app . ${APP_ROOT}
RUN ls -la /app/dockerify/web/
RUN chmod +x /app/dockerify/web/backup.sh /app/dockerify/web/backup.py \
    /app/dockerify/web/restore.sh /app/dockerify/web/restore.py

USER root

COPY ./dockerify/web/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./dockerify/web/start /start
RUN ls -la /app
RUN sed -i 's/\r//' /start
RUN chmod +x /start

ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY ${DJANGO_SECRET_KEY:-'^141&epfu9xc1)ou_^qnx$uo4-z*n3a#s=d2lqutulog2o%!yu'}

RUN echo "export DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY" >> ~/.bashrc

RUN ls -la /app/dockerify/web/
ENTRYPOINT ["/entrypoint"]