import imp
from django.urls import URLPattern, path
from . import  views


urlpatterns = [
    path('',views.home),
    path('home/' , views.change),
]
