from django.shortcuts import render
from django.http import HttpResponse

from .models import Trainee

def alltrainee(request):
    context={'alltrainee': Trainee.objects.all()}
    return render(request,'trainee/list.html',context)


def insert(request):
    print(request.POST)
    if request.method=='POST':
        name=request.POST['trainee_name']
        email=request.POST['tremail']
        Trainee.objects.create(name=name,email=email)
        return HttpResponse(f'<h1> Trainee {name} inserted successfully</h1>')
    return render(request,'trainee/insert.html')


def Name(request,Name):
    return HttpResponse(f'<h1> you in trainee {Name} page <h1>')
def email(request,email):
    return HttpResponse(f'<h1> you in trainee {email} page <h1>')
def update(request,update):
    return HttpResponse(f'<h1> you in update {update} page <h1>')
def id(request,id):
    return HttpResponse(f'<h1> you in trainee {id} page <h1>')
def gpa(request,gpa):
    return HttpResponse(f'<h1> trainee  {gpa}  <h1>')
def delete(request,d):
    return HttpResponse(f'<h1> you in delete   {d}  <h1>')


# Create your views here.
