# APIpart2
curretly working....

#Part number 1 (5/7/2015)
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
``
