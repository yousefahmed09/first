from django.shortcuts import render

from django.http import HttpResponse
from .models import Track
def insert(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST['trackname']
        Track.objects.create(name=name)
        return HttpResponse(f'<h1> Trainee {name} inserted successfully</h1>')
    return render(request, 'tracks/insert.html')



def allTracks(request):
    context={'tracks':Track.objects.all()}
    return render(request,'tracks/list.html',context)


def gettrackbyid(request,id):
    return HttpResponse(f'<p>We are in track {id}</p>')


def updatetrack(request,id):
    return HttpResponse(f'<p>We are in update {id}</p>')

def deletetrack(request,id):
    return HttpResponse(f'<p>We are in delete track {id}</p>')
# Create your views here.
