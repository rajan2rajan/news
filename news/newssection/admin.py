import imp
from django.contrib import admin
from newssection.models import Newsdata

# Register your models here.

class Newsdata_admin(admin.ModelAdmin):
    list_data = ('title','image','newsby','date','detail')
    
admin.site.register(Newsdata , Newsdata_admin)
