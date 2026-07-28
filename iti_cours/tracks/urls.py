from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('alltracks', alltrackes),
    path('idtracks', idtrackes),
    path('updatetrackes', updatetrackes),
    path('mindmaptrackes', mindmaptrackes),

]