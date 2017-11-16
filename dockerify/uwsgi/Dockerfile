FROM miniblog:latest

# Forward uwsgi logs to the docker log collector
RUN ln -sf /dev/stdout /var/log/uwsgi/djangoapp.log \
	&& ln -sf /dev/stdout /var/log/uwsgi/emperor.log

# The port number on which the application will run
EXPOSE 30000

RUN ls -la /app

RUN chmod +x /app/dockerify/uwsgi/entrypoint.sh \
    /app/dockerify/uwsgi/backup.sh /app/dockerify/uwsgi/backup.py \
    /app/dockerify/uwsgi/restore.sh /app/dockerify/uwsgi/restore.py

ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY ${DJANGO_SECRET_KEY:-'^141&epfu9xc1)ou_^qnx$uo4-z*n3a#s=d2lqutulog2o%!yu'}

RUN echo "export DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY" >> ~/.bashrc

ENTRYPOINT ["/app/dockerify/uwsgi/entrypoint.sh"]