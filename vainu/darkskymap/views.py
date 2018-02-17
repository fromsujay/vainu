# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse


#def homepage(request):
#    return HttpResponse('Hello (again) World!')


def darkskymap(request):
    return render(request, 'darkskymap/darkskymap.html', {})
