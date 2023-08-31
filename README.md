# A Simple Django Dynamic CURD (Create, Update, Read and Delete) Application Using Functional Based Views
We used Django and functional based views to develop a simple CRUD application to allow one to create a new task, Read task, update a task and delete a task. we used a postgresql database in this CRUD App. we can check the App data on WWW.Railway.app.com

### Working Demo
https://github.com/GODZ-k/django_crud_app/assets/131422684/dd71c379-9322-4881-9fb4-1e8bbed73cf9

### STEP 1: create a project 
- use `django-admin startproject project_name` to create a project .
- craete `views.py` where `setting.py` and `url.py` have and connect `views.py` in `url.py` `from project_Name import views`
- `from django.shortcut import render` in `views.py`

### STEP 2: create a app and add it to INSTALLED_APPS
- Create App using `python manage.py startapp app_name` and connect in `setting.py`
 - Let app_name = employe
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
        'employe', # app_name
]
```

### STEP 3: Create App model and associate form
```
from django.db import models

# Create your models here.
class employe(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=254)
    phone=models.CharField(max_length=120)
    info=models.CharField(max_length=200)
```

