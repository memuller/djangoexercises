from django.shortcuts import render
from django.http import HttpResponse

from .models import Instrument, InstrumentType

def index(request):
    return render(request, 'index.html', {'title': 'dhjksad'})
    #return HttpResponse("Aaaah.")
