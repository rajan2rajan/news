from email.policy import default
from enum import unique
import imp
from tkinter.messagebox import NO
from autoslug import AutoSlugField
from django.db import models
from prompt_toolkit import HTML
from sqlalchemy import null
from tinymce.models import HTMLField


# Create your models here.

class Newsdata(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from ='title',unique=True , null = True , default = None)
    image = models.FileField(upload_to='newssection/',max_length=100,null=True , default=None)
    newsby = models.CharField(max_length=20)
    date = models.DateField()
    detail = HTMLField()
