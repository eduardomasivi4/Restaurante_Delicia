from django.shortcuts import render
from .models import Pratos
#from django.http import HttpResponse

# Create your views here.

def listar(request):
    pratos = Pratos.objects.all()
    return render (request, 'menu/lista.html', {
        'pratos' : pratos
    })