# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from .models import Locationdata
from .forms import LocationdataForm


# This function and associated data is passed onto urls pattern in urls.py of application
def accueil(request):
    return render(request, 'darkskymap/accueil.html', {})
    
def decouvrir(request):
    datadump_obj = Locationdata.objects.all().values()
    datadump_lst = [row for row in datadump_obj]
    datadump = dict()
    datadump['datadump'] = datadump_lst
    return render(request, 'darkskymap/decouvrir.html', datadump)

def partager(request):
    if request.method == 'POST':
        form = LocationdataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Lieu d'Observation sauvgardé.")
        else:
            return HttpResponse("Erreur de saisie. Veuillez recommencer SVP.")

    else:
        form = LocationdataForm()
        return render(request, 'darkskymap/partager.html', {})         

