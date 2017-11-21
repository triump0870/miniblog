FROM miniblog:latest

# The port number on which the application will run
EXPOSE 30000

COPY --chown=app . ${APP_ROOT}
RUN ls -la /app/dockerify/web/
RUN chmod +x /app/dockerify/web/entrypoint.sh \
    /app/dockerify/web/backup.sh /app/dockerify/web/backup.py \
    /app/dockerify/web/restore.sh /app/dockerify/web/restore.py

ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY ${DJANGO_SECRET_KEY:-'^141&epfu9xc1)ou_^qnx$uo4-z*n3a#s=d2lqutulog2o%!yu'}

RUN echo "export DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY" >> ~/.bashrc

RUN ls -la /app/dockerify/web/
ENTRYPOINT ["/app/dockerify/web/entrypoint.sh"]