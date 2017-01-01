FROM mariadb

RUN apt-get update && apt-get -y install \
    vim \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

ARG MYSQL_PASSWORD
ENV MYSQL_PASSWORD ${MYSQL_PASSWORD}

COPY ./dockerify/mysql/entrypoint.sh /app-mysql/entrypoint.sh
COPY ./dockerify/mysql/createdb.conf.template /app-mysql/createdb.conf.template
COPY ./dockerify/mysql/miniblog.sql /app-mysql/miniblog.sql

WORKDIR /app-mysql/

RUN chmod +x entrypoint.sh
RUN ./entrypoint.sh

RUN chmod +x /docker-entrypoint-initdb.d/entrypoint.sh

RUN echo "export MYSQL_PASSWORD='$MYSQL_PASSWORD'" >> ~/.bashrc

RUN echo "alias ll='ls -la'" >> ~/.bashrc

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Port to use with TCP proxy
EXPOSE 3306
