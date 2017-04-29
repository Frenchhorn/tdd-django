Python 3.5.3
Django 1.11

### run server
python manage.py runserver

### run functional tests
~~python functional_tests.py~~
python manage.py test functional_tests

### run tests
python manage.py test [appName]

### run all test
python manage.py test

### set database and table information
python manage.py makemigrations

### create database
python manage.py migrate
python manage.py migrate --noinput