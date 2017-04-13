from django.contrib import admin

# Register your models here.
from .models import Instrument, InstrumentType

admin.site.register(Instrument)
admin.site.register(InstrumentType)
