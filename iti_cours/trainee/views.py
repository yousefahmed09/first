from django.shortcuts import render,redirect
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


def update_email(request,updatee):
    if request.method=='POST':
        Trainee.objects.filter(id=updatee).update(email=request.POST['tremail'])
        return redirect('/trainee/alltrainee')
    return render(request, 'trainee/update_email.html', {'id': id})

def update_name(request,updaten):
    if request.method=='POST':
        Trainee.objects.filter(id=updaten).update(name=request.POST['trainee_name'])
        return redirect('/trainee/alltrainee')
    return render(request, 'trainee/update_name.html', {'id': id})
def Name(request,Name):
    return HttpResponse(f'<h1> you in trainee {Name} page <h1>')

def email(request,email):
    return HttpResponse(f'<h1> you in trainee {email} page <h1>')
def id(request,id):
    return HttpResponse(f'<h1> you in trainee {id} page <h1>')
def gpa(request,gpa):
    return HttpResponse(f'<h1> trainee  {gpa}  <h1>')
def delete(request,d):
    Trainee.objects.filter(id=d).update(bo=False)
    return redirect('/trainee/alltrainee')


# Create your views here.
