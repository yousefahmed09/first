from django.shortcuts import render
from django.http import HttpResponse

def alltrackes(request):
    return HttpResponse('<h1> python c++  java script <h1>')

def idtrackes(request):
    return HttpResponse('<h1> you in tracks id page<h1>')

def updatetrackes(request):
    return HttpResponse('<h1> you in tracks update page <h1>')

def mindmaptrackes(request):
    return HttpResponse('<h1>you in tracks mindmap page <h1>')

# Create your views here.
