import imp
import re
from django.shortcuts import render


# Create your views here.


def home(request):
    
    return render(request , 'home.html')

def change(request):
    
    return render( request , "home.html")
