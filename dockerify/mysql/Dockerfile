FROM mariadb

RUN apt-get update && apt-get -y install \
    vim \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

ARG DATABASE_USER
ENV DATABASE_USER ${DATABASE_USER}

ARG DATABASE_PASSWORD
ENV DATABASE_PASSWORD ${DATABASE_PASSWORD}

ARG DATABASE
ENV DATABASE ${DATABASE}

COPY ./dockerify/mysql/entrypoint.sh /app-mysql/entrypoint.sh
COPY ./dockerify/mysql/createdb.conf.template /app-mysql/createdb.conf.template

WORKDIR /app-mysql/

RUN chmod +x entrypoint.sh
RUN ./entrypoint.sh

RUN chmod +x /docker-entrypoint-initdb.d/entrypoint.sh

RUN echo "export DATABASE_PASSWORD='$DATABASE_PASSWORD'" >> ~/.bashrc
RUN echo "export DATABASE_USER='$DATABASE_USER'" >> ~/.bashrc
RUN echo "export DATABASE='$DATABASE'" >> ~/.bashrc

RUN echo "alias ll='ls -la'" >> ~/.bashrc

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Port to use with TCP proxy
EXPOSE 3306
