from django.db import models

# Create your models here.
class employe(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=254)
    phone=models.CharField(max_length=120)
    info=models.CharField(max_length=200)