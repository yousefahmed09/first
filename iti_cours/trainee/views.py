from django.shortcuts import render
from django.http import HttpResponse

def  alltrainee(request):
    alltrainee = [[1,'ali'],[2,'mohammed'],[3,'ahmed'],[4,'yousef'],[5,'amir']]
    return render(request,'trainee/list.html',{'alltrainee':alltrainee})

def Name(request,Name):
    return HttpResponse(f'<h1> you in trainee {Name} page <h1>')
def update(request,update):
    return HttpResponse(f'<h1> you in update {update} page <h1>')
def id(request,id):
    return HttpResponse(f'<h1> you in trainee {id} page <h1>')
def gpa(request,gpa):
    return HttpResponse(f'<h1> trainee  {gpa}  <h1>')
def delete(request,d):
    return HttpResponse(f'<h1> you in delete   {d}  <h1>')

# Create your views here.
