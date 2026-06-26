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
It work by intercepting HTTP request and database queries and storing detailed  performance data, which you cam view in a web-based UI.

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
need to install OpenAPI sopurt usning drf-spectacular
```
 pip install drf-spectacular
```
After you install it, add the app to setting.py and REST_FRAMEWORK with the SPECTACULAR_SETTINGS.
Run this cammand
```
python manage.py spectacular --color --file schema.yml
```
Filtering 
Add in install apps
```
'django_filters'
'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
```
```
pip install django-filter
```
To add pagination
Just set the number of pages to any number
```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
```
