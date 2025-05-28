FROM nginx:alpine

LABEL maintainer="Raffaele Marcello <marcelloraffaele@gmail.com>"

COPY default.conf /etc/nginx/conf.d
COPY index.html /usr/share/nginx/html

EXPOSE 8080

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]