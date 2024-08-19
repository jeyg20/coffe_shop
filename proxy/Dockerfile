FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

# Copy Nginx configuration files
COPY ./default.conf.tpl /etc/nginx/conf.d/
COPY ./proxy_params /etc/nginx/

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT [ "sh", "-c", "/start.sh" ]
