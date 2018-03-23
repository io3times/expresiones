from django.shortcuts import render
from django.http import HttpResponse
from .models import Slowo, Zdanie
from django.core.exceptions import ObjectDoesNotExist

def index(request, id):
    try:
        e = Slowo.objects.get(id=id)
        output = e.slowo_slowo
    except ObjectDoesNotExist:
        output="Podane słowo nie istnieje"


    context={'output': output}
    return render(request, 'dic/index.html', context)



# Create your views here.
