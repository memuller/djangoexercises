from __future__ import unicode_literals

from django.db import models

# Create your models here.

class InstrumentType(models.Model):
    name =      models.CharField(max_length=50)

class Instrument(models.Model):
    name =      models.CharField(max_length=200)
    model =     models.CharField(max_length=100)
    addedAt =   models.DateField()
    available = models.BooleanField(default=1)

    kind =      models.ForeignKey(InstrumentType)
