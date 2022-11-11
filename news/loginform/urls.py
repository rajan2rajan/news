from django.urls import path
from . import views


urlpatterns = [
    path('loginform/',views.loginform , name="loginform"),
    
          
]