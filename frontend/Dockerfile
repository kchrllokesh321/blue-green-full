FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf || true

RUN printf 'events {}\n\
http {\n\
    server {\n\
        listen 80;\n\
        server_name _;\n\
        root /usr/share/nginx/html;\n\
        index index.html;\n\
        location / {\n\
            try_files $uri $uri/ =404;\n\
        }\n\
    }\n\
}\n' > /etc/nginx/nginx.conf

COPY index.html /usr/share/nginx/html/index.html
