from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):

    #dictonary
    people =[
        {
            "name":"odi",
            "age":20,
            "phone":"0183247827"
            
        }
    ]

    my_list =['apple','mango','bananna']

    context = {
        'peo':people,
        'myl':my_list

    }

    return render(request,'management/home.html',context) 

def contacts(request):
    contacts = Contact.objects.all()
    context = {
       'contact':contacts
  

    }

    # print(type (contacts))
    return render(request,'management/contacts.html',context)

def detail(request):
    # contact = Contact.objects.get(id=id)
    return render(request,'management/detail.html')



