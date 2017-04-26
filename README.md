# run server
python manage.py runserver

# run functional tests
python functional_tests.py

# run tests
python manage.py test [appName]

# set database and table information
python manage.py makemigrations

# create database
python manage.py migrate
python manage.py migrate --noinput