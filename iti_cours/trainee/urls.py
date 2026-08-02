from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('alltrainee', alltrainee),
    path('insert', insert),
    path('email<str:email>/', email),
    path('Name/<str:name>/', Name),
    path('update_name/<int:updaten>/', update_name,name='update_name'),
    path('update_email/<int:updatee>/', update_email, name='update_email'),
    path('id/<int:id>/', id),
    path('gpa/<int:gpa>/', gpa),
    path('delete/<int:d>/', delete,name='delete'),

]