FROM mariadb

ARG MYSQL_PASSWORD
ENV MYSQL_PASSWORD ${MYSQL_PASSWORD}

COPY ./dockerify/mysql/entrypoint.sh /app-mysql/entrypoint.sh
COPY ./dockerify/mysql/createdb.conf.template /app-mysql/createdb.conf.template
COPY ./dockerify/data/miniblog.sql /app-mysql/miniblog.sql

WORKDIR /app-mysql/

RUN chmod +x entrypoint.sh
RUN ./entrypoint.sh

RUN chmod +x /docker-entrypoint-initdb.d/entrypoint.sh

RUN echo "export MYSQL_PASSWORD='$MYSQL_PASSWORD'" >> ~/.bashrc

# Port to use with TCP proxy
EXPOSE 3306
