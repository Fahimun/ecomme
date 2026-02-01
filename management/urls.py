from django.urls import path
from .views import *

urlpatterns = [

    path('home/',home, name ="home"),
    path('contacts/',contacts, name="contacts"),
    path('contacts/detail/<int:id>'),
   
]