FROM nginx:alpine

LABEL maintainer="Raffaele Marcello <marcelloraffaele@gmail.com>"

COPY nginx.conf /etc/nginx

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]