# **macacaedu** | Movement Education - Online Platform

![macaca](static/img/macaca.png)

> HUGE WIP

## Develop

### setup

On a python3 environment:

    # install dependencies
    pip install -r requirements.txt

    # create empty database
    ./manage.py migrate

    # add test data
    ./manage.py studytestdata
    ./manage.py movertestdata

### run

Then start the test server:

    ./manage.py runserver

It will be available at http://localhost:8000/ by default.

Default superuser is username `test`, password `test`.
