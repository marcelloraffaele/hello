FROM nginx:alpine

LABEL maintainer="Accenture <arch@accenture.com>"

COPY nginx.conf /etc/nginx

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]