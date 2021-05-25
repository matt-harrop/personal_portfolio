#!/bin/sh
sudo git pull origin main
sudo pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
sudo systemctl restart nginx
sudo systemctl restart gunicorn
