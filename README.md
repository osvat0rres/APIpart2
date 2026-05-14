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
include in urls.py project level
```
path('silk/', include('silk.urls', namespace='silk'))
```
