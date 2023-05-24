from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views import generic
# from django.template import loader #Another way to display the templates using template, context and HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.http import Http404

from .models import Village, Cabain, Camper

 
# Create your views here.

def index(request):
    # Lógica para renderizar la página de índice
    return render(request, 'polls/index.html')

@login_required
def villages(request):
    villas = Village.objects.all()[::1]
    return render(request, 'polls/village.html', {"villages":villas})

@login_required
def select(request):
    return render(request, 'polls/select.html')

@login_required
def visucabagna(request, idvil):
    invilla=Village.objects.get(id=idvil)
    cabanas=Cabain.objects.filter(village_id = invilla.id)
    return render(request,"polls/cabain.html",{"cabanas":cabanas, "idvilla":idvil, 'invilla':invilla})

@login_required
def visucampista(request, idvil, idcab):
    incabana=Cabain.objects.get(id=idcab)
    campers=Camper.objects.filter(cabain_id = incabana.id)
    numcampers=len(campers)
    return render(request,"polls/campers.html", {"campers":campers, "cabana":incabana, "numcampers": numcampers, "idvilla":idvil, "idcab":idcab})

@login_required
def visu_profile_camper(request, idvil, idcab, idcamper):
    invilla=Village.objects.get(id=idvil)
    incabana = Cabain.objects.get(id=idcab)
    incamper=Camper.objects.get(id=idcamper)
    return render(request, "polls/campista.html", {"cabana":incabana, "villas":invilla, "camper":incamper, "idvilla":idvil, "idcab":idcab})


