# A Simple Django Dynamic CURD (Create, Update, Read and Delete) Application Using Functional Based Views [click here](https://curdoperationapp.pythonanywhere.com)
We used Django and functional based views to develop a simple CRUD application to allow one to create a new task, Read task, update a task and delete a task. we used a postgresql database in this CRUD App. we can check the App data on [Railway.app](https://railway.app/)

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
 #### model.py
```
from django.db import models

# Create your models here.
class employe(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=254)
    phone=models.CharField(max_length=120)
    info=models.CharField(max_length=200)

```
 #### admin.py
 ```
from django.contrib import admin
from employe.models import employe


# Register your models here.
class showempdata(admin.ModelAdmin):
    list_display=('name','email','phone','info')

admin.site.register(employe,showempdata)
```
- Run commands `python manage.py makemigrations` and `python manage.py migrate`

### STEP 4: Create template folder in root directory 
- Connect template folder in `setting.py`
  ```
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'], # connect folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
  ]
  ```
### STEP 5: Create html files in template folder
- we creates 3 templates `index.py` for show the data in the table
- `adddata.html` for insert the data into the table
- `nav.html` for only navbar we coz we need navbar in every page so i created only one and paste it on every page .
- `update.html` for update the table data
 #### index.html 
 ```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        *{
            padding: 0;
            margin: 0;

        }

        .nav{
            background-color: skyblue;
            padding: 10px;
        }
.heading{
    text-align: center;
    padding: 20px;
}
.div{
  overflow-x: scroll;
  margin: 0 20px;
}
</style>
<title>Document</title>
</head>
<body>
    {% include 'nav.html' %}
    <h1 class="heading">Data table</h1>
    <div class="div">
    <table class="table">
        <thead>
          <tr>
            <th scope="col">SNO</th>
            <th scope="col">Name</th>
            <th scope="col">E-mail</th>
            <th scope="col">Phone</th>
            <th scope="col">Information</th>
          </tr>
        </thead>
        <tbody>

        {% for show in alldata %}
          <tr>
            <th scope="row">{{forloop.counter}}</th>
            <td>{{show.name}}</td>
            <td>{{show.email}}</td>
            <td>{{show.phone}}</td>
            <td>{{show.info}}</td>
            <td style="white-space: nowrap;">
                <a href="/delete/{{show.id}}" class="btn btn-danger md-sm button">Delete</a>
                <a href="/update/{{show.id}}" class="btn btn-success md-sm button">Update</a>
            </td>

          </tr>
        {% endfor %}
        </tbody>
     </table>
  </div>
</body>
</html>
```
 #### adddata.html
 ```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    <style>
        *{
            padding: 0;
            margin: 0;

        }
        .heading{
            text-align: center;
            color: black;

            padding: 20px;

        }
        body{
            background-color: skyblue;
        }

        .nav{
            background-color: skyblue;
            padding: 10px;
        }
        .form{
            padding: 0px 20%;

            border: none;
            background-color: skyblue;

        }

    </style>
    <title>Document</title>
</head>
<body>
    {% include 'nav.html' %}
    <h1 class="heading">Data form </h1>
    <form method="post" action="{% url 'adddata' %}" class="form-control form">
        {% csrf_token %}
        <div class="mb-3">
          <label class="form-label">Name</label>
          <input type="text" class="form-control" name="name" placeholder="enter your name">
        </div>
        <div class="mb-3">
            <label class="form-label">Email</label>
            <input type="email" class="form-control" name="email" placeholder="enter your E-mail">
          </div>
          <div class="mb-3">
            <label class="form-label">Phone</label>
            <input type="number" class="form-control" name="phone" placeholder="enter your number">
          </div>
          <div class="mb-3">
            <label class="form-label">Information</label>
            {% comment %} <input type="text" class="form-control" name="name" placeholder="enter your name"> {% endcomment %}
            <textarea name="info" id="" cols="30" rows="10" class="form-control"></textarea>
          </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
</body>
</html>
```
 #### nav.html
 ```
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid nav">
    <a class="navbar-brand" href="/">Crud App</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/adddata/">Add data</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```
 #### update.html
 ```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        *{
            padding: 0;
            margin: 0;
        }
        .heading{
            text-align: center;
            color: black;

            padding: 20px;
        }
        body{
            background-color: skyblue;
        }
        .nav{
            background-color: skyblue;
            padding: 10px;
        }
        .form{
            padding: 0px 20%;
            border: none;
            background-color: skyblue;
        }
    </style>
    <title>Document</title>
</head>
<body>
    {% include 'nav.html' %}
    <h1 class="heading">Update Data form </h1>
    <form method="post" action="/do_update/{{ud.id}}" class="form-control form">
        {% csrf_token %}
        <div class="mb-3">
          <label class="form-label">Name</label>
          <input type="text" class="form-control" name="name"  value="{{ud.name}}">
        </div>
        <div class="mb-3">
            <label class="form-label">Email</label>
            <input type="email" class="form-control" name="email" value="{{ud.email}}">
          </div>
          <div class="mb-3">
            <label class="form-label">Phone</label>
            <input type="number" class="form-control" name="phone" value='{{ud.phone}}'>
          </div>
          <div class="mb-3">
            <label class="form-label">Information</label>
            {% comment %} <input type="text" class="form-control" name="name" placeholder="enter your name"> {% endcomment %}
            <textarea name="info" id="" cols="30" rows="10" class="form-control">{{ud.info}}</textarea>
          </div>
        <button type="submit" class="btn btn-success">Update</button>
      </form>
</body>
</html>
```
### STEP 6: Connect all forms in `views.py` and create logic of CRUD App
```
from pdb import post_mortem
from django.shortcuts import render,redirect
from django.http import HttpResponse
from employe.models import employe

def home(request):
    alldata=employe.objects.all()

    return render(request,'index.html',{'alldata':alldata})

def adddata(request):
    try:
     if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        info=request.POST.get('info')

        sendform=employe(name=name,email=email,phone=phone,info=info)
        sendform.save()
        return redirect('/')


    except:
      return redirect('adddata')

    return render(request,'adddata.html')

def delete(request,SNO):
      alldata=employe.objects.get(pk=SNO)
      alldata.delete()
      return redirect('/')

def update(request,SNO):
  ud=employe.objects.get(pk=SNO)
  return render(request,'update.html',{'ud':ud})

def do_update(request,SNO):
  if request.method=='POST':
    update_name=request.POST.get('name')
    update_email=request.POST.get('email')
    update_phone=request.POST.get('phone')
    update_info=request.POST.get('info')

    ud=employe.objects.get(pk=SNO)

    ud.name=update_name
    ud.email=update_email
    ud.phone=update_phone
    ud.info=update_info

    ud.save()
    return redirect('/')
```
### STEP 7: Connect all  `views.py` function to `urls.py`
```
"""
URL configuration for crudapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import Settings
from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('adddata/',views.adddata , name='adddata'),
    path('delete/<int:SNO>',views.delete),
    path('update/<int:SNO>',views.update),
    path('do_update/<int:SNO>',views.do_update),


]
```
### STEP 8: Connect POSTGRESQL database if you want (optonal)
- go [Railway.app](https://railway.app/) and create a account
- click POSTGRESQL
- click connect
- copy all available variable values and paste into `setting.py`
- remove previous sqllite3 database (optional) from `setting.py`

  ```
  DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '', # paste value in ''
        'USER': '', # paste value in ''
        'PASSWORD': '', # paste value in ''
        'HOST': '', # paste value in ''
        'PORT': '', # paste value in ''
    }
 }```
 
### STEP 9: Run command
`python manage.py runserver`

#### Don't forget to create superuser for admin panned where you can see all the data
 - Run `python manage.py createsuperuser`
 - username
 - email
 - password
 - password again
#### If you forget admin password
- Run `python manage.py changepassword <user_name>`
