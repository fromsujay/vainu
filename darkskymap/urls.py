from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views


# Creates url pattern that will look for information in views.py
urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
    url(r'^decouvrir/', views.decouvrir, name='decouvrir'),
    url(r'^partager/', views.partager, name='partager'),
    url(r'^cartedepollutionlumineuse/', views.cartedepollutionlumineuse, name='cartedepollutionlumineuse'),    
]
