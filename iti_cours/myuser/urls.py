from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('alluser',alluser),
    path('login',login),
    path('logout', logout),
    path('sing_up', sing_up ),

]
