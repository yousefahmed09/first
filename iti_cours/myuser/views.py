from django.shortcuts import render
from django.http import HttpResponse
def login(request):
    return HttpResponse('<h1>you in login page<h1>')

def logout(request):
    return HttpResponse('<h1>you in logout page<h1>')

def sing_up(request):
    return HttpResponse('<h1>you in sing up page<h1>')
# Create your views here.
