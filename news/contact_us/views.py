import re
from django.shortcuts import render
from .models import contact_us, rajan

# Create your views here.
def contact_us(request):
    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        data = rajan(fname=fname, lname=lname, email=email, message=message)
        data.save()
    else:
        pass
    
    return render(request ,"contact_us.html")