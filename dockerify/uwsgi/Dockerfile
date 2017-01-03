# The base image
FROM python:3.4

# Install all debian packages
RUN apt-get update && apt-get install -y \
        gcc \
        mysql-client libmysqlclient-dev\
        postgresql-client libpq-dev \
		sqlite3 \
        python3-dev \
        build-essential \
        vim \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN mkdir app-requirements/

COPY ./requirements.txt app-requirements/

RUN mkdir -p /var/log/app_logs

WORKDIR /app/
# install all the django dependencies
RUN pip install -r /app-requirements/requirements.txt

COPY . /app/

# Create the log directory for uwsgi and the shared directory for static files
RUN mkdir /var/log/uwsgi /shared

# Forward uwsgi logs to the docker log collector
RUN ln -sf /dev/stdout /var/log/uwsgi/djangoapp.log \
	&& ln -sf /dev/stdout /var/log/uwsgi/emperor.log


VOLUME /shared

# The port number on which the application will run
EXPOSE 30000

RUN chmod +x /app/dockerify/uwsgi/entrypoint.sh
RUN chmod +x /app/dockerify/uwsgi/backup.sh
RUN chmod +x /app/dockerify/uwsgi/backup.py

ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY ${DJANGO_SECRET_KEY:-'^141&epfu9xc1)ou_^qnx$uo4-z*n3a#s=d2lqutulog2o%!yu'}

RUN echo "export DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY" >> ~/.bashrc

ARG DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE ${DJANGO_SETTINGS_MODULE:-'miniblog.settings.development'}

RUN echo "export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE" >> ~/.bashrc

RUN echo "alias ll='ls -la'" >> ~/.bashrc

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

ENTRYPOINT ["/app/dockerify/uwsgi/entrypoint.sh"]