About
=====

Setting up database:

    python manage.py syncdb

Start up web server:

    python manage.py runserver

Reset database:

    rm indexing.db
    python manage.py syncdb
    
Adminstrative interface:

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Example use of API to submit quantities:

    python submission-api/submit.py

Important files
===============

    main/models.py
    main/views.py
