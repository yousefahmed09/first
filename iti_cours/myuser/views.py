from django.shortcuts import render
from django.http import HttpResponse

def  alluser(request):
    myuser = [[1,'ali'],[2,'mohammed'],[3,'ahmed'],[4,'yousef'],[5,'amir']]
    return render(request,'myuser/list.html',{'myuser':myuser})

def login(request):
    return HttpResponse('<h1>you in login page<h1>')

def logout(request):
    return HttpResponse('<h1>you in logout page<h1>')

def sing_up(request):
    return HttpResponse('<h1>you in sing up page<h1>')
# Create your views here.
