from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('name', name),
    path('update', update),
    path('id', id),
    path('gpa', gpa),
    path('Cgpa', Cgpa),

]