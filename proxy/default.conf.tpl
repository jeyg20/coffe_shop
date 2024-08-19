server {
    listen 80;

    location /static {
        alias /app/staticfiles;
    }

    location /media {
        alias /app/media;
    }

    location / {
        proxy_pass http://localhost:8000;
        include /etc/nginx/proxy_params;
    }
}
