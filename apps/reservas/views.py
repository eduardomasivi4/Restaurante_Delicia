from django.shortcuts import render
from .forms import Reserva
#from django.http import HttpResponse

def criar(request):
    if request.method == 'POST':
        form= Reserva(request.POST)
        
        if form.is_valid():
            nome= form.cleaned_data('nome')
            telefone= form.cleaned_data('telefone')
            email= form.cleaned_data('email')
            data= form.cleaned_data('data')
            hora= form.cleaned_data('hora')
            pessoas= form.cleaned_data('pessoas')
            observacoes= form.cleaned_data('observacoes')
            
            # Salar no banco de dados
        else:
            return render (request, 'reserva/criar.html',{
                'form':form
            })
    elif request.method == 'GET':
        return render (request, 'reservas/criar.html', {
            'form': Reserva()
        })
