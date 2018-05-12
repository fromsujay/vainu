# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here. Each field below represents column in database table.
class Locationdata(models.Model):
    locationid = models.CharField(max_length = 70, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    observationdate = models.DateField()
    
    
    def __str__(self):
        return self.locationid
        
        
