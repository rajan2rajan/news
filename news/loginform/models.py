import email
from unicodedata import name
from django.db import models

# Create your models here.
class loginform(models.Model):
    name = models.CharField(max_length=20)
    create_password = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=20)
    
    
class login_form(models.Model):
    name = models.CharField(max_length=20)
    create_password = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=20)
    news_image = models.FileField(upload_to='news/' , max_length=250 , null=True , default=None)
