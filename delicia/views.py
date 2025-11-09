from django.shortcuts import render
from .models import Pratos, Bebidas, Reservar

def index(request):
    return render (request, 'home/index.html')

def menu(request):
    pratos = Pratos.objects.all()
    return render (request, 'menu/index.html',{
        'pratos':pratos,
    })

def bebidas(request):
    bebidas = Bebidas.objects.filter(preco_por_taca=False)
    preco_por_taca= Bebidas.objects.filter(preco_por_taca=True)
    
    return render (request, 'bebidas/index.html',{
        'bebidas':bebidas,
        'preco_por_taca':preco_por_taca,
    })

def sobre(request):
    return render (request, 'sobre/index.html')

def contato(request):
    return render (request, 'contacto/index.html')

def reservar (request):
    if request.method == 'GET':
        return render (request, 'reservar/index.html')
    
    elif request.method == 'POST':
        reservar= Reservar()
        
        reservar.nome_completo= request.POST.get('nome')
        reservar.email= request.POST.get('email')
        reservar.telefone= request.POST.get('telefone')
        reservar.data= request.POST.get('data')
        reservar.hora= request.POST.get('hora')
        reservar.num_de_pessoas= request.POST.get('pessoas')
        reservar.observacoes= request.POST.get('observacoes')
        
        reservar.save()
        
        return render (request, 'reservar/index.html')
