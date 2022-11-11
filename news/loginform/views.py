import imp
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .models import login_form


# Create your views here.
def loginform(request):
    if request.method=="POST":
        name = request.POST.get('name')
        create_password = request.POST.get('create_password')
        password = request.POST.get('password')
        email = request.POST.get('email')
        location = request.POST.get('location')
    
        data = login_form(name=name,create_password=create_password,password=password,email=email,location=location)
        data.save()
        
    else:
        pass  
  
    return render(request ,"loginform.html")

def showing(request):
    
    return render(request , "base.html")


