from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('alltrainee', alltrainee),
    path('insert', insert),
    path('email<str:email>/', email),
    path('Name/<str:name>/', Name),
    path('update/<int:update>/', update,name='update'),
    path('id/<int:id>/', id),
    path('gpa/<int:gpa>/', gpa),
    path('delete/<int:d>/', delete,name='delete'),

]