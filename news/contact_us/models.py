from email import message
from unicodedata import name
from django.db import models

# Create your models here.
class contact_us(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    
class rajan(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    message = models.TextField()

