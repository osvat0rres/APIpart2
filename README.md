# APIpart2
curretly working....

I created a the tables (models.py )and insert the data from populated_db.py 
To view the information inside the the tables: 
```
python manage.py dbshell
```
Ones inside
```
.tables
SELECT * FROM myapp_name_of_table;
```
To generate DR diagram 
```
 python manage.py graph_models myapp > models.dot
```
go to Graphviz and pase the text inside models.dot

This command work to insert the values to the database
```
python manage.py populate_db
```

Install Django-Silk packages
This works as a live profiling and inspection tool for the djnago restframework. Silk intercepst and stores HTTP 
request and database queries before presenting them in a user interface for futher inspection

```
pip install django-silk
```
On in settings.py
```
INSTALLED_APP = [
   ...
    'silk',
]
MIDDLEWARE = [
   ...
   'silk.middleware.SilkyMiddleWare',
]
```
include in urls.py project level, then migrate
```
path('silk/', include('silk.urls', namespace='silk'))
```
Superuser
username: brandon
password: password

To run the test created, on terminal
```
python manage.py test
```
Install REST Client in VS code extension.
This work like insognia where you can send, cancel, and rerun HTTP request all inside VS code. 
Inside the api.http file, place the url of the view you want with the method and add the HTTP version and send request 

This command is to install Django web Token (JWT)
```
 pip install djangorestframework-simplejwt
```

