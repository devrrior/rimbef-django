Fauna Project
=============

Basic Commands
--------------

::

    $ docker-compose build
    $ docker-compose up

    $ docker-compose run fauna python manage.py makemigrations
    $ docker-compose run fauna python manage.py migrate
    $ docker-compose run fauna python manage.py shell
    $ docker-compose run fauna python manage.py createsuperuser

Backend
--------------

::

    $ http://0.0.0.0:8080 -> backoffice
