from django.shortcuts import render
from django.http import HttpResponse
def name(request):
    return HttpResponse('<h1> you in trainee name page <h1>')
def update(request):
    return HttpResponse('<h1> you in trainee update page <h1>')
def id(request):
    return HttpResponse('<h1> you in trainee id page <h1>')
def gpa(request):
    return HttpResponse('<h1> you in trainee gpa page <h1>')
def Cgpa(request):
    return HttpResponse('<h1> you in trainee Cgpa page <h1>')

# Create your views here.
