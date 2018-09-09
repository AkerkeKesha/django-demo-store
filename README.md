#django-demo-store

Otus, Web-Dev course, Django app - demo of online store.
The main page lists all the products. For the purpose of this hw 
only 3 products are in DB. Click on a product to see its further details
For details of homework: https://otus.ru



## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv --python=$(which python3) venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ cd online_store/
$ python3 manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

