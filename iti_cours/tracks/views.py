from django.shortcuts import render,redirect

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
    context={'tracks':Track.objects.all().order_by('-id')}
    return render(request,'tracks/list.html',context)


def gettrackbyid(request,id):
    return HttpResponse(f'<p>We are in track {id}</p>')


def updatetrack(request,id):
    if request.method == 'POST':
        Track.objects.filter(id=id).update(name=request.POST['trackname'])
        return redirect('/track/allTracks')

    return render(request, 'tracks/update.html', {'id': id})




def deletetrack(request,id):
   Track.objects.filter(id=id).update(bo=False)
   return redirect('/track/allTracks')
# Create your views here.
