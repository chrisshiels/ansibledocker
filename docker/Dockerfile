from library/alpine:latest

expose 80

run apk update && apk add nginx

run mkdir -p /run/nginx && chown nginx:nginx /run/nginx

copy root /

entrypoint /usr/sbin/nginx -c /etc/nginx/nginx.conf -g 'daemon off;'
