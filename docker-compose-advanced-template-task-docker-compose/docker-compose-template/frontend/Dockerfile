FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /usr/share/nginx/html/static
COPY styles.css /usr/share/nginx/html/static/styles.css
