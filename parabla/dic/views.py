from django.shortcuts import render
from django.http import HttpResponse
from .models import Slowo, Zdanie
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    e=Slowo.objects.all()
    context={'output_list': e}
    return render(request, 'dic/index.html', context)


def primer(request, id):
    try:
        e = Slowo.objects.get(id=id)
        output = e.slowo_czesc
    except ObjectDoesNotExist:
        output = "Podane słowo nie istnieje"

    context = {'output': output}
    return render(request, 'dic/primer.html', context)

# Create your views here.
