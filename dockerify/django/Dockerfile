# The base image
FROM python:3.4
MAINTAINER Rohan Roy <rohan@rohanroy.com>

ENV PYTHONUNBUFFERED 1
#ENV C_FORCE_ROOT true # intentionally kept it commented

ENV APP_USER app
ENV APP_ROOT /app

# Install all debian packages
RUN apt-get update && apt-get install -y \
        gcc \
        mysql-client \
        libmysqlclient-dev \
        postgresql-client \
        libpq-dev \
		sqlite3 \
        python3-dev \
        build-essential \
        vim \
        man \
        sudo \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Add the user
RUN groupadd -r ${APP_USER} \
    && useradd -r -m \
    --home-dir ${APP_ROOT} \
    -s /usr/sbin/nologin \
    -g ${APP_USER} ${APP_USER}

# Set the working directory to app home directory
WORKDIR ${APP_ROOT}

# Run the commands
RUN mkdir app-requirements/
COPY ./requirements.txt app-requirements/

# Install all the django dependencies
RUN pip install --upgrade pip
RUN pip install -r app-requirements/requirements.txt

# Add user to sudo
RUN chpasswd && usermod -aG sudo ${APP_USER}
RUN echo "${APP_USER} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${APP_USER} && \
    chmod 0440 /etc/sudoers.d/${APP_USER}

# Change the permission of the log directories
RUN chown -R ${APP_USER}:${APP_USER} /var/log/ ${APP_ROOT}/ /usr/local/bin/ /var/run/

# change the timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Specify the user to execute all commands below
USER ${APP_USER}

# Create the log directory for uwsgi and the shared directory for static files
RUN mkdir -p /var/log/app_logs
RUN mkdir /var/log/uwsgi

COPY --chown=app . ${APP_ROOT}