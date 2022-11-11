from operator import iconcat
from tkinter import NE
from django.shortcuts import render
from .models import Newsdata
from django.core.paginator import Paginator

# Create your views here.


# for searching and showing data 


def newssection(request):
    if request.method=="GET":
        result = request.GET.get('query')
        if result==None:
            data = Newsdata.objects.all()
        else :
            data= Newsdata.objects.filter(title__icontains = result) 
        data = {"data":data , 'query':result}
            
    return render(request ,'news.html',data)

            


    # data = Newsdata.objects.all()
    
    # return render(request, 'news.html',{'data':data})
          




"""for slug"""         
def ide(request, slug):
    data = Newsdata.objects.get(slug=slug)
    # here two parameter are passed one is slug (predefined not by me) and another is request .At get first one is it that we definded in the model and another is predefinded
    return render(request , 'newsdetail.html' , {'data':data})
    
    
    
