#/bin/bash
python manage.py makemigrations 
sleep 5;
 python manage.py migrate
