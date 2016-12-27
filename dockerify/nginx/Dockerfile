FROM nginx:1.11

# Install all debian packages
RUN apt-get update && apt-get install -y \
	vim \
	net-tools \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY ./dockerify/nginx/entrypoint.sh /app-nginx/entrypoint.sh
COPY ./dockerify/nginx/nginx.conf.template /app-nginx/nginx.conf.template
RUN mkdir -p /app/static/

EXPOSE 80

WORKDIR /app-nginx/

# Use the configuration script as the entrypoint
RUN chmod +x /app-nginx/entrypoint.sh

ENV UWSGI_URI miniblog-uwsgi:30000

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN echo "alias ll='ls -la'" >> ~/.bashrc

ENTRYPOINT ["/app-nginx/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

