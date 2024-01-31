#!/usr/bin/env bash
# Setting up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install nginx -y

sudo ufw allow 'Nginx HTTP'

echo 'Hello World!' >/var/www/html/index.nginx-debian.html

mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >/data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu: /data

printf %s "server {
    listen 80;
    listen [::]:80 default_server;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" >/etc/nginx/sites-available/default

service nginx restart
