## Django Demo Store


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
```

## Run and View 

SQLite DB is used for the project for the demonstration purposes. 
To run the project:
```bash
$ python3 /<absolute_path>/online_store/manage.py migrate
$ python3 /<absolute_path>/online_store/manage.py createsuperuser --username=admin --email=admin@example.com
$ python3 /<absolute_path>/online_store/manage.py runserver
```
Then visit `http://127.0.0.1:8000/` to view the app. 
Then visit `http://127.0.0.1:8000/admin` to see admin panel. 

Here's a screenshot of the store:
Home Page

![ScreenShot](https://raw.github.com/AkerkeKesha/django-demo-store/master/readme_pics/product_list.png)

Product page

![ScreenShot](https://raw.github.com/AkerkeKesha/django-demo-store/master/readme_pics/product_detail.png)
   


   