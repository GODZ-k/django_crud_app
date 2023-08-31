from django.contrib import admin
from employe.models import employe


# Register your models here.
class showempdata(admin.ModelAdmin):
    list_display=('name','email','phone','info')

admin.site.register(employe,showempdata)