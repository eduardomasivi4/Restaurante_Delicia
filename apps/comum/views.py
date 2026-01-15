from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    return render(request, 'comum/home.html')

def sobre(request):
    return render(request, 'comum/sobre.html')