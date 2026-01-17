from django.shortcuts import render
from .forms import Reserva as f_reserva
from .models import Reserva as tb_reserva
#from django.http import HttpResponse

def criar(request):
    if request.method == 'POST':
        form= f_reserva(request.POST)
        
        if form.is_valid():
            # Salar no banco de dados
            tb_reserva.objects.create(
                nome= form.cleaned_data['nome'],
                telefone= form.cleaned_data['telefone'],
                email= form.cleaned_data['email'],
                data= form.cleaned_data['data'],
                hora= form.cleaned_data['hora'],
                pessoas= form.cleaned_data['pessoas'],
                observacoes= form.cleaned_data['observacoes'],
            )
            
            # Mostra a tela criar reserva com caixa de mensagem confirmando a criação da reserva
            return render (request, 'reservas/criar.html', {
                'form': f_reserva()
            })
            
        else:
            return render (request, 'reserva/criar.html',{
                'form':form
            })
    elif request.method == 'GET':
        return render (request, 'reservas/criar.html', {
            'form': f_reserva()
        })
